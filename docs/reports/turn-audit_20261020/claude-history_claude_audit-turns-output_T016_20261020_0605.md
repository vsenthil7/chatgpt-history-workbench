| Turn | C1 record file | C2 Read at | C3 user input | C4 reply | C5 actions | C6 usage | C7 evidence block | C8 timeline | C9 one commit | C10 pushed | C11 secrets |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T016 | OK | OK | OK | OK | OK | OK | OK | NO | OK | OK | OK |  

Checks:
- **C1 record file** — turns/YYYY/MM/DD/T###-*.md exists
- **C2 Read at** — Metadata has `Read at:`
- **C3 user input** — `## USER INPUT` + input fidelity label
- **C4 reply** — `## ASSISTANT RESPONSE` + response fidelity label
- **C5 actions** — `## ACTIONS / RESULTS`
- **C6 usage** — `## USAGE` with a label + a CSV named in it exists
- **C7 evidence block** — reply ends with Git Evidence: Repo, Turn, Commit, Verified, Usage, Research, Gaps
- **C8 timeline** — index/timeline.md has a line naming the record
- **C9 one commit** — exactly one `turn(...): T###` commit adds the record
- **C10 pushed** — that commit is on origin/main
- **C11 secrets** — secret_scan.py clean on the commit's files (re-run now)

Evidence:
- T016: record `turns/2026/10/18/T016-2303-secret-cleanup-all-kinds.md` · commit d6f2073
