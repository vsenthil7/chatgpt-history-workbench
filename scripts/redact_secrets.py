#!/usr/bin/env python3
"""
Redacts credential-shaped strings from raw/ (and readable/ when it exists) before they go to GitHub. [claude, T004]
Adapted from claude-history-workbench/scripts/redact_secrets.py (local rule D3).

Difference from the Claude version: the patterns are the BLOCK patterns of scripts/secret_scan.py itself,
and its ALLOW list is honoured, so whatever the pre-push scan blocks is exactly what gets redacted
(no second list to drift). Lists are read with ast, because secret_scan.py scans when imported.

Each value becomes  [REDACTED:<kind>:sha256-<first 12 hex of sha256(value)>]
so the same value can be matched across files without exposing it. The un-redacted original stays in
Senthil's export zip (source/SOURCE_CHECKSUMS.md). Every rewritten .json file is checked to still parse.

Usage: python -I redact_secrets.py <repo_dir>       (writes source/REDACTIONS.md)
verify_raw.py imports redact_text() to rebuild the expected redacted content.
"""
import ast, hashlib, json, os, re, sys

# secret_scan.py runs its scan at import time (no __name__ guard; it is a shared copy, not edited here),
# so read its BLOCK and ALLOW lists as data with ast instead of importing it.  [T004 fix after first run]
_src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "secret_scan.py"), encoding="utf-8").read()
_vals = {t.id: ast.literal_eval(n.value) for n in ast.parse(_src).body if isinstance(n, ast.Assign)
         for t in n.targets if isinstance(t, ast.Name) and t.id in ("BLOCK", "ALLOW")}
BLOCK, ALLOW = _vals["BLOCK"], _vals["ALLOW"]

# labels must not contain the scan's trigger words, or the placeholder itself is flagged ("secret:sha256-...")
PATTERNS = {k.replace("secret", "value").replace(" ", "-").replace("/", "-"): re.compile(v) for k, v in BLOCK.items()}


# Optional legacy pass (T007): a repo that redacted earlier with other labels lists those patterns in
# scripts/redact_legacy.json ({"kind": "regex", ...}, applied first, in order, no ALLOW) so verify still
# reproduces the old placeholders exactly. No file = no legacy pass.
_lp = os.path.join(os.path.dirname(os.path.abspath(__file__)), "redact_legacy.json")
LEGACY = {k: re.compile(v) for k, v in json.load(open(_lp, encoding="utf-8")).items()} if os.path.exists(_lp) else {}


def redact_text(s, log=None, path=None):
    for kind, rx in LEGACY.items():
        def lsub(m, kind=kind):
            tag = hashlib.sha256(m.group(0).encode()).hexdigest()[:12]
            if log is not None:
                log.append((path, kind, tag))
            return f"[REDACTED:{kind}:sha256-{tag}]"
        s = rx.sub(lsub, s)
    for kind, rx in PATTERNS.items():
        def sub(m):
            if any(a in m.group(0) for a in ALLOW):  # same allow-list as the scan (placeholders)
                return m.group(0)
            tag = hashlib.sha256(m.group(0).encode()).hexdigest()[:12]
            if log is not None:
                log.append((path, kind, tag))
            return f"[REDACTED:{kind}:sha256-{tag}]"
        s = rx.sub(sub, s)
    return s


# ---- JSON value level (T006 fix) --------------------------------------------------------------------------
# Text-level redaction cannot see a value hidden by JSON escaping (e.g. password=\"abc…\" or a key after \n).
# So for JSON files every decoded string value is redacted too. Same function in redactor and verify_raw.

def _redact_obj(o, pairs, log, path):
    if isinstance(o, str):
        r = redact_text(o, log, path)
        if r != o:
            pairs.append((o, r))
        return r
    if isinstance(o, list):
        return [_redact_obj(v, pairs, log, path) for v in o]
    if isinstance(o, dict):
        return {k: _redact_obj(v, pairs, log, path) for k, v in o.items()}
    return o


def redact_json_text(s, log=None, path=None, reserialise=False):
    """Text-level redaction, then value-level on the parsed JSON.
    reserialise=True (our own chat files): write back as json.dump(indent=1, ensure_ascii=False) + LF, the importer's format.
    reserialise=False (byte copies): patch only the encoded changed strings in place; falls back to reserialising
    only if that cannot reproduce the redacted object."""
    s1 = redact_text(s, log, path)
    try:
        o = json.loads(s1)
    except ValueError:
        return s1
    pairs = []
    o2 = _redact_obj(o, pairs, log, path)
    if not pairs:
        return s1
    nl = "\n" if s.endswith("\n") else ""  # keep the file's own trailing newline (T007)
    if reserialise:
        return json.dumps(o2, ensure_ascii=False, indent=1) + nl
    s2 = s1
    for old, new in pairs:
        for ea in (False, True):
            s2 = s2.replace(json.dumps(old, ensure_ascii=ea)[1:-1], json.dumps(new, ensure_ascii=ea)[1:-1])
    try:
        if json.loads(s2) == o2:
            return s2
    except ValueError:
        pass
    return json.dumps(o2, ensure_ascii=False, indent=1) + nl


def is_chat_file(rel):
    return rel.replace("\\", "/").startswith("raw/conversations/")


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
                if fn.endswith(".json"):
                    n = redact_json_text(s, log, rel, reserialise=is_chat_file(rel))
                else:
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
    logp = os.path.join(repo, "source/REDACTIONS.md")
    first = not os.path.exists(logp)
    # APPEND a dated section per run, never overwrite: a rerun on already-redacted files finds 0 and must not
    # erase the earlier log.  [T004]
    with open(logp, "a", encoding="utf-8", newline="\n") as f:
        if first:
            f.write("# Redactions\n\nCredential-shaped strings removed before pushing to GitHub (patterns = BLOCK "
                    "list of scripts/secret_scan.py, its ALLOW list honoured). Fidelity of affected files: VERBATIM "
                    "except these values. Originals: Senthil's export zip.\n\n"
                    "Action for Senthil: rotate/revoke any of these that were real keys — they were in chat history.\n"
                    "One section per redactor run (append-only).\n")
        import datetime as _dt
        f.write(f"\n## Run {_dt.datetime.now(_dt.timezone.utc):%Y-%m-%d %H:%M} UTC\n\n"
                f"Totals: {sum(agg.values())} values in {len({p for p, _, _ in agg})} files, "
                f"{len({t for _, _, t in agg})} distinct.\n\n"
                "| file | kind | sha256 prefix | count |\n|---|---|---|---|\n")
        for (p, k, t), c in sorted(agg.items()):
            f.write(f"| `{p}` | {k} | `{t}` | {c} |\n")
    print(f"redactions={sum(agg.values())} files={len({p for p, _, _ in agg})} distinct_values={len({t for _, _, t in agg})}")
    if broken:
        print("NOT REDACTED (would break JSON):", *broken, sep="\n  ")
        sys.exit(1)
