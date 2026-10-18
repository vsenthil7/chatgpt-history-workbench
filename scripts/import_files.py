#!/usr/bin/env python3
"""
Slice S4: attachments of a ChatGPT data export → raw/files/. [claude, T005]
Separate from import_export.py on purpose: re-running that one would rewrite (un-redact) the chat files.

Reads the zip IN PLACE (stdlib only). For every entry file_*.dat / file-*.dat:
  - real name from conversation_asset_file_names.json; unnamed entries get "(unnamed)" + an extension
    sniffed from the first bytes (png/jpg/gif/webp/pdf/zip/ogg/mp4/json/txt), else ".dat"
  - stored as raw/files/<entry without .dat>__<real name>  (file id prefix keeps 184 repeated names apart)
  - entries > 95 MB are NOT written (GitHub 100 MB file limit, plan v0.1 decision): Drive-only, pointer row
Writes index/files_<exportdate>.csv: entry, real_name, stored_path, bytes, sha256, location (git|drive-only), sniffed
and adds chat.html (also Drive-only) to index/large_files.csv with its SHA-256.
Byte copies are VERBATIM; redact_secrets.py may later change text files (logged), verify_raw.py checks them.

Usage: python -I import_files.py <export.zip> <repo_dir> <exportdate YYYYMMDD>
Refuses to overwrite an existing raw/files/ file whose bytes differ (protects redacted files on a rerun).
"""
import csv, hashlib, json, os, re, sys, zipfile

ZIP, REPO, TAG = sys.argv[1], sys.argv[2], sys.argv[3]
LIMIT = 95 * 1048576
z = zipfile.ZipFile(ZIP)
names = json.loads(z.read("conversation_asset_file_names.json"))
RESERVED = {"con", "prn", "aux", "nul", *(f"com{i}" for i in range(1, 10)), *(f"lpt{i}" for i in range(1, 10))}
MAGIC = [(b"\x89PNG", ".png"), (b"\xff\xd8\xff", ".jpg"), (b"GIF8", ".gif"), (b"%PDF", ".pdf"),
         (b"PK\x03\x04", ".zip"), (b"OggS", ".ogg"), (b"RIFF", ".webp")]


def sniff(head):
    for m, e in MAGIC:
        if head.startswith(m):
            return e
    if head[4:8] == b"ftyp":
        return ".mp4"
    s = head.lstrip()[:1]
    if s in (b"{", b"["):
        return ".json"
    try:
        head.decode("utf-8")
        return ".txt"
    except UnicodeDecodeError:
        return ".dat"


def safe(n):
    n = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", n).rstrip(" .")
    stem, ext = os.path.splitext(n)
    if stem.lower() in RESERVED:
        stem = "_" + stem
    if len(stem) > 110:
        stem = stem[:110]
    return stem + ext


def sha_and_size(info):
    h, n = hashlib.sha256(), 0
    with z.open(info) as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b); n += len(b)
    return h.hexdigest(), n


rows, large, written, kept, conflict = [], [], 0, 0, []
os.makedirs(os.path.join(REPO, "raw", "files"), exist_ok=True)
for i in z.infolist():
    if not i.filename.startswith(("file_", "file-")):
        continue
    fid = i.filename[:-4] if i.filename.endswith(".dat") else i.filename
    real = names.get(i.filename, "")
    with z.open(i) as f:
        head = f.read(16)
    sn = sniff(head)
    stored = f"{fid}__{safe(real) if real else '(unnamed)' + sn}"
    sha, size = sha_and_size(i)
    if i.file_size > LIMIT:
        rows.append([i.filename, real, "", size, sha, "drive-only", sn])
        large.append([i.filename, real, size, sha, "attachment over 95 MB"])
        continue
    rel = f"raw/files/{stored}"
    p = os.path.join(REPO, rel)
    data = z.read(i)
    if os.path.exists(p):
        if open(p, "rb").read() != data:
            conflict.append(rel)  # e.g. already redacted: leave it
        kept += 1
    else:
        open(p, "wb").write(data); written += 1
    rows.append([i.filename, real, rel, size, sha, "git", sn])

ci = z.getinfo("chat.html")
sha, size = sha_and_size(ci)
large.append(["chat.html", "", size, sha, "rendered copy of the chats (derived), 159 MB"])

with open(os.path.join(REPO, "index", f"files_{TAG}.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(["entry", "real_name", "stored_path", "bytes", "sha256", "location", "sniffed_ext"])
    w.writerows(sorted(rows))
with open(os.path.join(REPO, "index", "large_files.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(["export", "entry", "real_name", "bytes", "sha256", "why_drive_only", "where"])
    for r in large:
        w.writerow([TAG, *r, "Drive: My Drive/chatgpt-export/Chatgpt-export-20261014.zip (entry inside the zip)"])

g = [r for r in rows if r[5] == "git"]
print(f"attachments: {len(rows)} · in git {len(g)} ({sum(r[3] for r in g):,} bytes) · new {written} · already there {kept}"
      f" · drive-only {len(rows) - len(g)} · unnamed {sum(1 for r in rows if not r[1])} · conflicts {len(conflict)}")
for c in conflict[:20]:
    print("  differs (left as is):", c)
