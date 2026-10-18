#!/usr/bin/env python3
"""
S9: compare two ChatGPT export inventories so nothing is missed between exports. [claude, T006]
Input: the folders written by inventory_export.py, index/exports/<OLD>/ and index/exports/<NEW>/.
With only <NEW> it writes the BASELINE report (what the first export holds).

Compares
  chats   (chatgpt-history_inventory_conversations_<date>.csv, key conversation_id):
          new · gone from the export · changed (updated time or message count differs) · same
  entries (chatgpt-history_inventory_entries_<date>.csv, key zip entry name):
          new · gone · changed (size or CRC-32 differs) · same
  missing (index/missing_files_<OLD>.csv, if present): files that were unrecoverable in OLD and are now in NEW
Writes index/exports/compare_<OLD>_vs_<NEW>.md (or baseline_<NEW>.md) and a CSV with every difference.

Usage: python3 -I compare_exports.py <repo_dir> <NEW> [<OLD>]
"""
import csv, os, sys

REPO, NEW = sys.argv[1], sys.argv[2]
OLD = sys.argv[3] if len(sys.argv) > 3 else None
ex = os.path.join(REPO, "index", "exports")


def load(date, kind, key):
    p = os.path.join(ex, date, f"chatgpt-history_inventory_{kind}_{date}.csv")
    return {r[key]: r for r in csv.DictReader(open(p, encoding="utf-8"))}


nc, ne = load(NEW, "conversations", "conversation_id"), load(NEW, "entries", "entry")
L = []
if OLD is None:
    out = os.path.join(ex, f"baseline_{NEW}.md")
    months = {}
    for r in nc.values():
        months[r["created_utc"][:7]] = months.get(r["created_utc"][:7], 0) + 1
    L = [f"# Baseline — ChatGPT export {NEW}", "",
         f"- chats: {len(nc)} · first {min(r['created_utc'] for r in nc.values())} · last {max(r['created_utc'] for r in nc.values())}",
         f"- latest update in any chat: {max(r['updated_utc'] for r in nc.values())} (next export: chats changed after this show as 'changed')",
         f"- zip entries: {len(ne)} · attachments (file_*): {sum(1 for e in ne if e.startswith('file'))}",
         "", "Run `compare_exports.py <repo> <NEXT> " + NEW + "` after the next export's inventory to get the differences."]
    rows = []
else:
    oc, oe = load(OLD, "conversations", "conversation_id"), load(OLD, "entries", "entry")
    out = os.path.join(ex, f"compare_{OLD}_vs_{NEW}.md")
    rows = []
    for k in sorted(set(nc) | set(oc)):
        a, b = oc.get(k), nc.get(k)
        st = "new" if a is None else "gone" if b is None else (
            "changed" if (a["updated_utc"], a["messages"]) != (b["updated_utc"], b["messages"]) else "same")
        if st != "same":
            rows.append(["chat", k, (b or a)["title"], st, a and a["messages"], b and b["messages"]])
    for k in sorted(set(ne) | set(oe)):
        a, b = oe.get(k), ne.get(k)
        st = "new" if a is None else "gone" if b is None else (
            "changed" if (a["bytes"], a["crc32"]) != (b["bytes"], b["crc32"]) else "same")
        if st != "same":
            rows.append(["entry", k, (b or a)["real_name"], st, a and a["bytes"], b and b["bytes"]])
    mp = os.path.join(REPO, "index", f"missing_files_{OLD}.csv")
    if os.path.exists(mp):
        for r in csv.DictReader(open(mp, encoding="utf-8")):
            if f"{r['file_id']}.dat" in ne:
                rows.append(["recovered", r["file_id"], r["name_if_known"], "now in export", "", ""])
    cnt = {}
    for r in rows:
        cnt[(r[0], r[3])] = cnt.get((r[0], r[3]), 0) + 1
    L = [f"# Compare ChatGPT exports {OLD} → {NEW}", "",
         f"- chats: {len(oc)} → {len(nc)} · " + " · ".join(f"{s} {cnt.get(('chat', s), 0)}" for s in ("new", "changed", "gone")),
         f"- entries: {len(oe)} → {len(ne)} · " + " · ".join(f"{s} {cnt.get(('entry', s), 0)}" for s in ("new", "changed", "gone")),
         f"- previously missing files now present: {cnt.get(('recovered', 'now in export'), 0)}",
         "- 'gone' chats are NOT deleted from Git: raw/ keeps them; this report only says the newer export lacks them.",
         "", f"Every difference: `{os.path.basename(out)[:-3]}.csv`"]
with open(out, "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(L) + "\n")
with open(out[:-3] + ".csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(["kind", "key", "name", "status", "old", "new"]); w.writerows(rows)
print("\n".join(L))
