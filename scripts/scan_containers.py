#!/usr/bin/env python3
"""
Read-only secret scan INSIDE zip containers (zip, xlsx, docx, pptx, jar…) under a folder. [claude, T005]
secret_scan.py reads these as compressed bytes and cannot see a key inside, e.g. a .env in a project zip.

Uses secret_scan.py's BLOCK and ALLOW lists (read with ast; importing it would run a scan).
Nested zips are opened one level deep. Members over 50 MB or not UTF-8-decodable (errors=ignore) are still scanned
as text with errors ignored, like secret_scan.py. Never prints or stores the values — only file, member, kind, count.

Usage: python -I scan_containers.py <folder> <out_csv>
Exit 0 = no hits, 1 = hits (listed in out_csv).
"""
import ast, csv, io, os, re, sys, zipfile

here = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(here, "secret_scan.py"), encoding="utf-8").read()
vals = {t.id: ast.literal_eval(n.value) for n in ast.parse(src).body if isinstance(n, ast.Assign)
        for t in n.targets if isinstance(t, ast.Name) and t.id in ("BLOCK", "ALLOW")}
BLOCK = {k: re.compile(v) for k, v in vals["BLOCK"].items()}
ALLOW = vals["ALLOW"]
folder, out = sys.argv[1], sys.argv[2]
hits, n_cont, n_members, errors = {}, 0, 0, []


def scan_zip(zf, label, depth):
    global n_members
    for m in zf.infolist():
        if m.is_dir():
            continue
        try:
            data = zf.read(m)
        except Exception as e:  # encrypted / broken member
            errors.append(f"{label}!{m.filename}: {type(e).__name__}")
            continue
        n_members += 1
        if depth == 0 and zipfile.is_zipfile(io.BytesIO(data)):
            try:
                scan_zip(zipfile.ZipFile(io.BytesIO(data)), f"{label}!{m.filename}", 1)
            except Exception as e:
                errors.append(f"{label}!{m.filename}: {type(e).__name__}")
            continue
        text = data.decode("utf-8", errors="ignore")
        for kind, rx in BLOCK.items():
            for mt in rx.finditer(text):
                if not any(a in mt.group(0) for a in ALLOW):
                    key = (label, m.filename, kind)
                    hits[key] = hits.get(key, 0) + 1


for fn in sorted(os.listdir(folder)):
    p = os.path.join(folder, fn)
    if not os.path.isfile(p) or not zipfile.is_zipfile(p):
        continue
    n_cont += 1
    try:
        scan_zip(zipfile.ZipFile(p), fn, 0)
    except Exception as e:
        errors.append(f"{fn}: {type(e).__name__}")

with open(out, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(["container", "member", "kind", "count"])
    for (c, m, k), n in sorted(hits.items()):
        w.writerow([c, m, k, n])
print(f"containers {n_cont} · members scanned {n_members} · hits {sum(hits.values())} in "
      f"{len({c for c, _, _ in hits})} containers · unreadable {len(errors)}")
for e in errors[:15]:
    print("  unreadable:", e)
sys.exit(1 if hits else 0)
