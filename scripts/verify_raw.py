#!/usr/bin/env python3
"""
Proves raw/ matches the ChatGPT export zip, apart from logged redactions. [claude, T004]
Mirrors claude-history-workbench/scripts/verify_raw.py.

Checks:
 1. zip SHA-256 equals the value in source/SOURCE_CHECKSUMS.md
 2. every chat in conversations-00N.json has exactly one raw file, and that file is JSON-equal to the
    chat object after the same redaction as scripts/redact_secrets.py (text level + JSON value level, T006); no extra chat files on disk
 3. every raw/data/<name> equals the zip entry after the same redaction (byte compare)

Usage: python -I verify_raw.py <export.zip> <repo_dir>
Exit 0 = identical (apart from logged redactions); 1 = differences (printed).
"""
import datetime as dt, hashlib, json, os, re, sys, zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from redact_secrets import redact_text, redact_json_text  # noqa: E402

ZIP, REPO = sys.argv[1], sys.argv[2]
bad = []
h = hashlib.sha256()
with open(ZIP, "rb") as f:
    for b in iter(lambda: f.read(1 << 20), b""):
        h.update(b)
want = re.search(r"\b([0-9a-f]{64})\s+" + re.escape(os.path.basename(ZIP)),
                 open(os.path.join(REPO, "source/SOURCE_CHECKSUMS.md"), encoding="utf-8").read())
if not want or want.group(1) != h.hexdigest():
    bad.append(f"zip sha256 {h.hexdigest()} != SOURCE_CHECKSUMS.md")

z = zipfile.ZipFile(ZIP)
expected_paths, n_chats = set(), 0
for n in sorted(x for x in z.namelist() if x.startswith("conversations-") and x.endswith(".json")):
    for c in json.loads(z.read(n)):
        n_chats += 1
        cid = c.get("conversation_id") or c.get("id")
        t = dt.datetime.fromtimestamp(c["create_time"], dt.timezone.utc)
        rel = f"raw/conversations/{t:%Y}/{t:%m}/{t:%Y%m%d_%H%M}_{cid[:8]}.json"
        expected_paths.add(rel)
        p = os.path.join(REPO, rel)
        if not os.path.exists(p):
            bad.append(f"missing {rel}"); continue
        exp = json.loads(redact_json_text(json.dumps(c, ensure_ascii=False), reserialise=True))
        if json.load(open(p, encoding="utf-8")) != exp:
            bad.append(f"differs {rel}")

on_disk = set()
for d, _, fs in os.walk(os.path.join(REPO, "raw", "conversations")):
    on_disk |= {os.path.relpath(os.path.join(d, f), REPO).replace("\\", "/") for f in fs}
bad += [f"extra {x}" for x in sorted(on_disk - expected_paths)]

n_data = 0
ddir = os.path.join(REPO, "raw", "data")
for fn in sorted(os.listdir(ddir)) if os.path.isdir(ddir) else []:
    n_data += 1
    src = z.read(fn)
    try:
        t = src.decode("utf-8")
        src = (redact_json_text(t) if fn.endswith(".json") else redact_text(t)).encode("utf-8")
    except UnicodeDecodeError:
        pass
    if open(os.path.join(ddir, fn), "rb").read() != src:
        bad.append(f"differs raw/data/{fn}")

# 4. attachments (S4, T005): every row of index/files_*.csv; git rows byte-equal (after redaction), drive-only rows
#    SHA-256-equal to the zip entry; no file in raw/files/ that the index does not list
n_files = n_drive = 0
fdir = os.path.join(REPO, "raw", "files")
idx = [os.path.join(REPO, "index", f) for f in sorted(os.listdir(os.path.join(REPO, "index")))
       if f.startswith("files_") and f.endswith(".csv")] if os.path.isdir(fdir) else []
listed = set()
for path in idx:
    import csv
    for r in csv.DictReader(open(path, encoding="utf-8")):
        if r["location"] == "drive-only":
            n_drive += 1
            hh = hashlib.sha256()
            with z.open(r["entry"]) as f:
                for b in iter(lambda: f.read(1 << 20), b""):
                    hh.update(b)
            if hh.hexdigest() != r["sha256"]:
                bad.append(f"drive-only sha256 differs {r['entry']}")
            continue
        n_files += 1
        listed.add(r["stored_path"])
        p = os.path.join(REPO, r["stored_path"])
        if not os.path.exists(p):
            bad.append(f"missing {r['stored_path']}"); continue
        src = z.read(r["entry"])
        got = open(p, "rb").read()
        if got != src:
            try:
                t = src.decode("utf-8")
                src = (redact_json_text(t) if r["stored_path"].endswith(".json") else redact_text(t)).encode("utf-8")
            except UnicodeDecodeError:
                pass
            if got != src:
                bad.append(f"differs {r['stored_path']}")
if os.path.isdir(fdir):
    bad += [f"extra raw/files/{f}" for f in sorted(os.listdir(fdir)) if f"raw/files/{f}" not in listed]

print(f"zip sha256 ok: {not any(b.startswith('zip') for b in bad)} · chats in export {n_chats} · chat files {len(on_disk)} · data files {n_data}"
      f" · attachments in git {n_files} · drive-only {n_drive} · problems {len(bad)}")
for b in bad[:50]:
    print(" ", b)
sys.exit(1 if bad else 0)
