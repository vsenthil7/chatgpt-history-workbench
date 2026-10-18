#!/usr/bin/env python3
"""Inventory a ChatGPT data-export zip WITHOUT extracting it. [claude, T003]

Reads the zip in place (stdlib only) and writes:
  <out_dir>/chatgpt-history_inventory_entries_<exportdate>.csv  - every zip entry (name, size, crc, real name from
                                                                  conversation_asset_file_names.json, extension)
  <out_dir>/chatgpt-history_inventory_conversations_<exportdate>.csv - one row per chat (id, title, created, updated,
                                                                  message count, model, source file)
  <out_dir>/chatgpt-history_inventory_summary_<exportdate>.md   - counts, date range, sizes, categories
Usage: python -I inventory_export.py <export.zip> <out_dir> <exportdate YYYYMMDD>
Rerun on every later export; compare the CSVs between export dates.
"""
import csv, datetime as dt, hashlib, json, os, sys, zipfile
from collections import Counter

zpath, out, tag = sys.argv[1], sys.argv[2], sys.argv[3]
os.makedirs(out, exist_ok=True)
h = hashlib.sha256()
with open(zpath, "rb") as f:
    for b in iter(lambda: f.read(1 << 20), b""):
        h.update(b)
sha = h.hexdigest()
z = zipfile.ZipFile(zpath)
names = {}
if "conversation_asset_file_names.json" in z.namelist():
    names = json.loads(z.read("conversation_asset_file_names.json"))


def ts(x):
    return dt.datetime.fromtimestamp(x, dt.timezone.utc).strftime("%Y-%m-%d %H:%M") if x else ""


ext_ct, ext_sz = Counter(), Counter()
with open(os.path.join(out, f"chatgpt-history_inventory_entries_{tag}.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["entry", "bytes", "compressed", "crc32", "real_name", "real_ext"])
    for i in z.infolist():
        real = names.get(i.filename, "")
        ext = os.path.splitext(real or i.filename)[1].lower() or "(none)"
        ext_ct[ext] += 1
        ext_sz[ext] += i.file_size
        w.writerow([i.filename, i.file_size, i.compress_size, f"{i.CRC:08x}", real, ext])

convs, models, months = [], Counter(), Counter()
for n in sorted(x for x in z.namelist() if x.startswith("conversations-") and x.endswith(".json")):
    for c in json.loads(z.read(n)):
        msgs = [m for m in (c.get("mapping") or {}).values() if m.get("message")]
        mdl = c.get("default_model_slug") or ""
        models[mdl] += 1
        months[ts(c.get("create_time"))[:7]] += 1
        convs.append([c.get("conversation_id") or c.get("id"), c.get("title") or "", ts(c.get("create_time")),
                      ts(c.get("update_time")), len(msgs), mdl, c.get("gizmo_id") or "", n])
with open(os.path.join(out, f"chatgpt-history_inventory_conversations_{tag}.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["conversation_id", "title", "created_utc", "updated_utc", "messages", "model", "gpt_id", "source_file"])
    w.writerows(sorted(convs, key=lambda r: r[2]))

top = {n: z.getinfo(n).file_size for n in z.namelist() if "/" not in n and not n.startswith("file")}
user_keys = sorted(json.loads(z.read("user.json")).keys()) if "user.json" in top else []
dates = sorted(r[2] for r in convs if r[2])
L = [f"# Inventory — ChatGPT export {tag}", "",
     f"- Zip: `{os.path.basename(zpath)}` · {os.path.getsize(zpath):,} bytes · SHA-256 `{sha}`",
     f"- Entries: {len(z.infolist()):,} · uncompressed {sum(i.file_size for i in z.infolist()):,} bytes",
     f"- Conversations: {len(convs):,} · first {dates[0] if dates else '-'} · last {dates[-1] if dates else '-'} (UTC, created)",
     f"- Messages (nodes with a message): {sum(r[4] for r in convs):,}",
     f"- Asset files named in conversation_asset_file_names.json: {len(names):,}",
     f"- user.json keys: {', '.join(user_keys)} (values not copied here)", "",
     "## Top-level data files", "| file | bytes |", "|---|---|"]
L += [f"| {n} | {s:,} |" for n, s in sorted(top.items())]
L += ["", "## Asset files by real extension", "| ext | count | MB |", "|---|---|---|"]
L += [f"| {e} | {c} | {ext_sz[e]/1048576:.1f} |" for e, c in ext_ct.most_common()]
L += ["", "## Chats by month (created)", "| month | chats |", "|---|---|"]
L += [f"| {m} | {c} |" for m, c in sorted(months.items())]
L += ["", "## Default model per chat", "| model | chats |", "|---|---|"]
L += [f"| {m or '(none)'} | {c} |" for m, c in models.most_common()]
L += ["", "## Entries over 95 MB (GitHub 100 MB per-file limit)", "| entry | real name | MB |", "|---|---|---|"]
L += [f"| {i.filename} | {names.get(i.filename, '')} | {i.file_size/1048576:.1f} |"
      for i in sorted(z.infolist(), key=lambda i: -i.file_size) if i.file_size > 95 * 1048576]
open(os.path.join(out, f"chatgpt-history_inventory_summary_{tag}.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
print("\n".join(L))
