| Turn | C1 record file | C2 Read at | C3 user input | C4 reply | C5 actions | C6 usage | C7 evidence block | C8 timeline | C9 one commit | C10 pushed | C11 secrets |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T001 | OK | OK | OK | OK | OK | NO | NO | NO | OK | OK | OK |  
| T002 | OK | OK | OK | OK | OK | OK | OK | NO | NO | OK | OK |  
| T003 | OK | OK | OK | OK | OK | OK | OK | NO | OK | OK | OK |  
| T004 | OK | OK | OK | OK | OK | OK | OK | NO | OK | OK | OK |  
| T005 | OK | OK | OK | OK | OK | OK | OK | NO | OK | OK | OK |  
| T006 | OK | OK | OK | OK | OK | OK | OK | NO | OK | OK | OK |  
| T007 | OK | OK | OK | NO | NO | NO | NO | NO | OK | OK | OK |  
| T008 | OK | OK | OK | OK | OK | NO | NO | NO | OK | OK | OK |  
| T009 | OK | OK | OK | NO | OK | OK | OK | NO | OK | OK | OK |  

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
- T001: Git Evidence block missing Repo, Turn, Commit, Verified, Usage, Research, Gaps
- T001: record `turns/2026/10/18/T001-2132-repo-name.md` · commit 13c1d0b
- T002: record `turns/2026/10/18/T002-2134-bootstrap-repo-git-turns.md` · commit 13c1d0b
- T003: record `turns/2026/10/18/T003-2139-export-inventory-plan-v01.md` · commit 56dc7a1
- T004: record `turns/2026/10/18/T004-2147-import-chats-data-redact-verify.md` · commit bea80ff
- T005: record `turns/2026/10/18/T005-2205-attachments-held-back-verify.md` · commit d16b3e6
- T006: record `turns/2026/10/18/T006-2242-readable-indexes-compare-json-redaction-fix.md` · commit d2503ec
- T007: Git Evidence block missing Repo, Turn, Commit, Verified, Usage, Research, Gaps
- T007: record `turns/2026/10/18/T007-2303-claude-history-cleanup-pointer.md` · commit 7125c09
- T008: Git Evidence block missing Repo, Turn, Commit, Verified, Usage, Research, Gaps
- T008: record `turns/2026/10/18/T008-0713-plan-repo-and-import-approach.md` · commit 9a54ac0
- T009: record `turns/2026/10/20/T009-0550-gtp-audit-repair.md` · commit 83135b9

| Turn | C1 record file | C2 Read at | C3 user input | C4 reply | C5 actions | C6 usage | C7 evidence block | C8 timeline | C9 one commit | C10 pushed | C11 secrets |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T013 | OK | OK | OK | OK | OK | OK | OK | NO | NO | OK | OK |  
| T014 | OK | OK | NO | NO | NO | NO | NO | NO | NO | OK | OK |  
| T015 | OK | OK | NO | NO | NO | NO | NO | NO | OK | OK | OK |  
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
- T013: record `turns/2026/10/14/T013-0819-turn-close-script.md` · commit 0c1ee3e
- T014: Git Evidence block missing Repo, Turn, Commit, Verified, Usage, Research, Gaps
- T014: record `turns/2026/10/17/T014-1458-move-to-global-layer.md` · commit 0c1ee3e
- T015: Git Evidence block missing Repo, Turn, Commit, Verified, Usage, Research, Gaps
- T015: record `turns/2026/10/17/T015-1514-bump-standards-pin.md` · commit 0c1ee3e
- T016: record `turns/2026/10/18/T016-2303-secret-cleanup-all-kinds.md` · commit d6f2073

[exited with code 0]
