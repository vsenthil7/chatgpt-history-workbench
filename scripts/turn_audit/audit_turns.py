#!/usr/bin/env python3
# Copy of vsenthil7/ai-tool-support-kb scripts/turn_audit/audit_turns.py (master; byte-identical copy also in ai-workspace-standards). Change it there first. [claude, 2026-10-20]
"""Audit turn records against Git Turn Protocol v1.2 §2 (+ §5 Git Evidence block).
Read-only. Usage: python3 -I scripts/turn_audit/audit_turns.py T045 T047 ...  (run from repo root)
Prints a markdown checklist: one row per turn, one column per check, with the file that holds the evidence.
REPAIRED = the miss is named in a repairs/ note (v2, T056)."""
import glob, re, subprocess, sys

def sh(*a):
    return subprocess.run(a, capture_output=True, text=True).stdout

CHECKS = [
    ("C1 record file", "turns/YYYY/MM/DD/T###-*.md exists"),
    ("C2 Read at", "Metadata has `Read at:`"),
    ("C3 user input", "`## USER INPUT` + input fidelity label"),
    ("C4 reply", "`## ASSISTANT RESPONSE` + response fidelity label"),
    ("C5 actions", "`## ACTIONS / RESULTS`"),
    ("C6 usage", "`## USAGE` with a label + a CSV named in it exists"),
    ("C7 evidence block", "reply ends with Git Evidence: Repo, Turn, Commit, Verified, Usage, Research, Gaps"),
    ("C8 timeline", "index/timeline.md has a line naming the record"),
    ("C9 one commit", "exactly one `turn(...): T###` commit adds the record"),
    ("C10 pushed", "that commit is on origin/main"),
    ("C11 secrets", "secret_scan.py clean on the commit's files (re-run now)"),
]

timeline = open("index/timeline.md", encoding="utf-8").read()
# A miss named in a repairs/ note counts as REPAIRED (records are never edited).
repairs = {f: open(f, encoding="utf-8").read() for f in glob.glob("repairs/*.md")}
def repaired(t, word):
    return [f for f, txt in repairs.items() if re.search(rf"\b{t}\b", txt) and word in txt]
print("| Turn | " + " | ".join(c[0] for c in CHECKS) + " |")
print("|---" * (len(CHECKS) + 1) + "|")
notes = []
for t in sys.argv[1:]:
    files = [f for f in glob.glob(f"turns/*/*/*/{t}-*.md")]
    res = {}
    if not files:
        print(f"| {t} | " + " | ".join(["NO"] + ["-"] * (len(CHECKS) - 1)) + " |")
        continue
    f = files[0]
    s = open(f, encoding="utf-8").read()
    res["C1"] = True
    res["C2"] = bool(re.search(r"^- Read at: \w+", s, re.M))
    res["C3"] = "## USER INPUT" in s and "User input fidelity:" in s
    res["C4"] = "## ASSISTANT RESPONSE" in s and "Assistant response fidelity:" in s
    res["C5"] = "## ACTIONS / RESULTS" in s
    csvs = re.findall(r"usage/[\w/.\-]+\.csv", s)
    res["C6"] = bool(re.search(r"^## USAGE \((MEASURED|USER-STATED|ESTIMATE|UNAVAILABLE)", s, re.M)) and bool(csvs) and all(glob.glob(c) for c in csvs)
    ev = s.split("Git Evidence")[-1] if "Git Evidence" in s else ""
    need = ["- Repo:", "- Turn:", "- Commit:", "- Verified:", "- Usage:", "- Research:", "- Gaps:"]
    missing = [n[2:-1] for n in need if n not in ev]
    res["C7"] = not missing
    if missing:
        fix = repaired(t, missing[0])
        notes.append(f"{t}: Git Evidence block missing {', '.join(missing)}" + (f" — REPAIRED in {fix[0]}" if fix else ""))
        if fix:
            res["C7"] = "REPAIRED"
    res["C8"] = f.split("/")[-1] in timeline
    log = sh("git", "log", "origin/main", "--format=%h %s", "--diff-filter=A", "--", f).split("\n")
    commits = [l for l in log if l.strip()]
    res["C9"] = len(commits) == 1 and re.search(rf"turn\(\w[\w-]*\): {t}\b", commits[0]) is not None
    sha = commits[0].split()[0] if commits else ""
    res["C10"] = bool(sha) and sha in sh("git", "log", "origin/main", "--format=%h")
    if sha:
        changed = [x for x in sh("git", "show", "--name-only", "--format=", sha).split("\n") if x]
        out = subprocess.run(["python3", "-I", "scripts/secret_scan.py", *changed], capture_output=True, text=True)
        res["C11"] = out.returncode == 0 and "0 blocking" in out.stdout
    else:
        res["C11"] = False
    print(f"| {t} | " + " | ".join(res[c[0].split()[0]] if res[c[0].split()[0]] == "REPAIRED" else ("OK" if res[c[0].split()[0]] else "NO") for c in CHECKS) + f" |  ")
    notes.append(f"{t}: record `{f}` · commit {sha or 'none'}")
print()
print("Checks:")
for c in CHECKS:
    print(f"- **{c[0]}** — {c[1]}")
print()
print("Evidence:")
for n in notes:
    print(f"- {n}")
