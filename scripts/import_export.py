#!/usr/bin/env python3
"""
chatgpt-history-workbench importer, v1 (2026-10-18, T004). Mirrors claude-history-workbench/scripts/import_export.py.

Reads a ChatGPT data-export zip IN PLACE (never extracts or changes it; stdlib only) and writes:

  raw/conversations/YYYY/MM/<YYYYMMDD_HHMM>_<id8>.json   VERBATIM chat object (parsed + re-serialised,
                                                          json.dump(ensure_ascii=False, indent=1), LF endings)
  raw/data/<name>.json                                   VERBATIM byte copies of the other data files
  index/import_conversations_<exportdate>.csv            one row per chat: id, raw path, source file, bytes, json-equal check

Chat files are re-serialised, so not byte-identical to the export; each is read back and checked to be
JSON-equal to its object in conversations-00N.json (column json_equal). Exits 1 on any mismatch or collision.

NOT copied (by decision, see source/SOURCE_CHECKSUMS.md): user.json (account email, birth year),
chat.html (159 MB, rendered copy of the same chats; Drive-only, pointer in index/large_files.csv).
Attachments (file_*.dat) are slice S4, not this script.

Usage: python -I import_export.py <export.zip> <repo_dir> <exportdate YYYYMMDD>
"""
import csv, datetime as dt, json, os, sys, zipfile

ZIP, REPO, TAG = sys.argv[1], sys.argv[2], sys.argv[3]
SKIP = {"user.json", "chat.html"}
z = zipfile.ZipFile(ZIP)


def wjson(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
        f.write("\n")


# S3: other data files, byte copies
data_done = []
for i in z.infolist():
    n = i.filename
    if "/" in n or n.startswith(("file_", "file-")) or n.startswith("conversations-") or n in SKIP:
        continue
    p = os.path.join(REPO, "raw", "data", n)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    b = z.read(n)
    open(p, "wb").write(b)
    assert len(b) == i.file_size
    data_done.append((n, i.file_size))

# S2: one file per chat
rows, seen, bad = [], set(), 0
for n in sorted(x for x in z.namelist() if x.startswith("conversations-") and x.endswith(".json")):
    for c in json.loads(z.read(n)):
        cid = c.get("conversation_id") or c.get("id")
        t = dt.datetime.fromtimestamp(c["create_time"], dt.timezone.utc)
        stem = f"{t:%Y%m%d_%H%M}_{cid[:8]}"
        if stem in seen:
            print("COLLISION", stem, cid); bad += 1; continue
        seen.add(stem)
        rel = f"raw/conversations/{t:%Y}/{t:%m}/{stem}.json"
        p = os.path.join(REPO, rel)
        wjson(p, c)
        ok = json.load(open(p, encoding="utf-8")) == c
        bad += 0 if ok else 1
        rows.append([cid, rel, n, os.path.getsize(p), "yes" if ok else "NO"])

os.makedirs(os.path.join(REPO, "index"), exist_ok=True)
with open(os.path.join(REPO, "index", f"import_conversations_{TAG}.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(["conversation_id", "raw_path", "source_file", "bytes", "json_equal"])
    w.writerows(sorted(rows, key=lambda r: r[1]))

print(f"data files copied: {len(data_done)} ({sum(s for _, s in data_done):,} bytes): {', '.join(n for n, _ in data_done)}")
print(f"chats written: {len(rows)} ({sum(r[3] for r in rows):,} bytes) · json-equal: {sum(r[4] == 'yes' for r in rows)} · problems: {bad}")
sys.exit(1 if bad else 0)
