#!/usr/bin/env python3
"""
Hold back attachments that carry credentials INSIDE them (found by scan_containers.py). [claude, T005]
They are not redacted (rewriting a zip changes it); they stay Drive-only, like files over 95 MB.

For every container named in <hits_csv>:
  - MOVE raw/files/<container> to <hold_dir> (a move, never a delete; the original also stays in the export zip)
  - set its row in index/files_<exportdate>.csv to location=drive-only (verify_raw.py then checks its SHA-256
    against the zip instead of looking for it on disk)
  - list it in index/held_back_files.csv with the number of hits and the kinds
Idempotent: a second run finds nothing left to move and keeps the rows as they are.

Usage: python -I hold_back.py <hits_csv> <repo_dir> <exportdate YYYYMMDD> <hold_dir>
"""
import csv, os, shutil, sys
from collections import defaultdict

hits_csv, repo, tag, hold = sys.argv[1:5]
kinds, counts = defaultdict(set), defaultdict(int)
for r in csv.DictReader(open(hits_csv, encoding="utf-8")):
    c = r["container"].split("!")[0]
    kinds[c].add(r["kind"]); counts[c] += int(r["count"])

idx = os.path.join(repo, "index", f"files_{tag}.csv")
rows = list(csv.DictReader(open(idx, encoding="utf-8")))
by_stored = {os.path.basename(r["stored_path"]): r for r in rows if r["stored_path"]}
os.makedirs(hold, exist_ok=True)
moved = missing = 0
held = []
for c in sorted(kinds):
    r = by_stored.get(c)
    if r is None:
        print("NOT IN INDEX:", c); missing += 1; continue
    src = os.path.join(repo, r["stored_path"])
    if os.path.exists(src):
        shutil.move(src, os.path.join(hold, c)); moved += 1
    r["location"] = "drive-only"
    held.append([r["entry"], r["real_name"], r["stored_path"], r["bytes"], r["sha256"], counts[c], " | ".join(sorted(kinds[c]))])

with open(idx, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), lineterminator="\n")
    w.writeheader(); w.writerows(rows)
heldp = os.path.join(repo, "index", "held_back_files.csv")
old = {r["entry"]: r for r in csv.DictReader(open(heldp, encoding="utf-8"))} if os.path.exists(heldp) else {}
with open(heldp, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(["entry", "real_name", "would_be_path", "bytes", "sha256", "credential_hits_inside", "kinds", "export"])
    seen = set()
    for h in held:
        w.writerow([*h, tag]); seen.add(h[0])
    for e, r in old.items():  # keep rows from earlier runs/exports
        if e not in seen:
            w.writerow(list(r.values()))
print(f"held back: {len(held)} containers · moved now {moved} · not in index {missing} · hold dir {hold}")
sys.exit(1 if missing else 0)
