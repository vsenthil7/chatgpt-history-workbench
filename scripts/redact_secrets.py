#!/usr/bin/env python3
"""
Redacts credential-shaped strings from raw/ (and readable/ when it exists) before they go to GitHub. [claude, T004]
Adapted from claude-history-workbench/scripts/redact_secrets.py (local rule D3).

Difference from the Claude version: the patterns are the BLOCK patterns of scripts/secret_scan.py itself,
so whatever the pre-push scan blocks is exactly what gets redacted (no second list to drift). Placeholders
that match a pattern are redacted too — over-redacting a fake value is cheap, leaking a real one is not.

Each value becomes  [REDACTED:<kind>:sha256-<first 12 hex of sha256(value)>]
so the same value can be matched across files without exposing it. The un-redacted original stays in
Senthil's export zip (source/SOURCE_CHECKSUMS.md). Every rewritten .json file is checked to still parse.

Usage: python -I redact_secrets.py <repo_dir>       (writes source/REDACTIONS.md)
verify_raw.py imports redact_text() to rebuild the expected redacted content.
"""
import hashlib, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # our own scripts/ folder only
from secret_scan import BLOCK  # noqa: E402

PATTERNS = {k.replace(" ", "-").replace("/", "-"): re.compile(v) for k, v in BLOCK.items()}


def redact_text(s, log=None, path=None):
    for kind, rx in PATTERNS.items():
        def sub(m):
            tag = hashlib.sha256(m.group(0).encode()).hexdigest()[:12]
            if log is not None:
                log.append((path, kind, tag))
            return f"[REDACTED:{kind}:sha256-{tag}]"
        s = rx.sub(sub, s)
    return s


if __name__ == "__main__":
    repo, log, broken = sys.argv[1], [], []
    for top in ("raw", "readable"):
        for d, _, fs in os.walk(os.path.join(repo, top)):
            for fn in fs:
                p = os.path.join(d, fn)
                try:
                    s = open(p, encoding="utf-8", newline="").read()
                except UnicodeDecodeError:
                    continue
                rel = os.path.relpath(p, repo).replace("\\", "/")
                n = redact_text(s, log, rel)
                if n != s:
                    if fn.endswith(".json"):
                        try:
                            json.loads(n)
                        except ValueError:
                            broken.append(rel)
                            continue  # leave the file untouched; reported below
                    open(p, "w", encoding="utf-8", newline="").write(n)
    agg = {}
    for p, k, t in log:
        if p in broken:
            continue
        agg[(p, k, t)] = agg.get((p, k, t), 0) + 1
    os.makedirs(os.path.join(repo, "source"), exist_ok=True)
    with open(os.path.join(repo, "source/REDACTIONS.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("# Redactions\n\nCredential-shaped strings removed before pushing to GitHub (patterns = BLOCK list of "
                "scripts/secret_scan.py). Fidelity of affected files: VERBATIM except these values. "
                "Originals: Senthil's export zip.\n\n"
                "Action for Senthil: rotate/revoke any of these that were real keys — they were in chat history.\n\n"
                f"Totals: {sum(agg.values())} values in {len({p for p, _, _ in agg})} files, "
                f"{len({t for _, _, t in agg})} distinct.\n\n"
                "| file | kind | sha256 prefix | count |\n|---|---|---|---|\n")
        for (p, k, t), c in sorted(agg.items()):
            f.write(f"| `{p}` | {k} | `{t}` | {c} |\n")
    print(f"redactions={sum(agg.values())} files={len({p for p, _, _ in agg})} distinct_values={len({t for _, _, t in agg})}")
    if broken:
        print("NOT REDACTED (would break JSON):", *broken, sep="\n  ")
        sys.exit(1)
