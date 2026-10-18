# T003 — 2026-10-18 21:39 Europe/London — export located, hashed, inventoried; plan v0.1

## Metadata
- Read at: ea77763
- Repo: vsenthil7/chatgpt-history-workbench · branch main
- AI / surface / model: claude · claude.ai chat with cloud workspace + PC bridge (senbhu, Windows) · Opus 5.5 (claude-opus-5-5)
- Session / page: session_01LsHkXSMf4NVpYpHa7YL5GZ (log c67e47e6)
- Protocol: Git Turn Protocol v1.2
- Turn class: live
- User input fidelity: VERBATIM
- Assistant response fidelity: VERBATIM

## USER INPUT

````
go 21:39
````

## ACTIONS / RESULTS
- Pulled main (ea77763, up to date).
- Drive metadata: `Chatgpt-export-20261014.zip`, 920,955,775 bytes. The Drive connector returns files inline, so 921 MB cannot come through it → used the PC bridge instead.
- Found the zip on the PC at `G:\My Drive\chatgpt-export\` (Google Drive for desktop), same size. That folder holds only the zip.
- Hashed in place: SHA-256 `43f44e15d5f29d6407e248993c9fda647298420d93b69ad6c5a0fdc4a96b9115` → `source/SOURCE_CHECKSUMS.md`.
- Wrote `scripts/inventory_export.py`, copied it to the PC temp folder (SHA-256 matched both sides: f1d36b2b…7c61), and ran it on the zip in place. The zip was not extracted or changed.
- Inventory results (SHA-256 matched both sides) → `index/exports/20261014/`: entries CSV (1,700), conversations CSV (811), summary MD.
- Searched Drive and PC for a memory export since 10 Oct: none found.
- Checked the PC: workbench clones live in `C:\Users\v_sen\develop`; git 2.53 and git-lfs 3.7.1 are installed.
- Plan v0.1 → `docs/plans/chatgpt-history_claude_plan_import_v01_20261018_2145.md` (status PROPOSED).

### Failures and recoveries
- First copy of the script to the PC failed (ENOENT: temp folder did not exist) → created the folder, then rewrote the file.
- Bringing the inventory back: the output was too large for the tool result and was saved as a file. Decoded it from that file and checked all three hashes.

## USAGE (MEASURED — session log via `scripts/usage_session.py`, up to the commit)
| model calls | input | cache read | cache write | output | effective units |
|---|---|---|---|---|---|
| 27 | 54 | 5,573,835 | 47,543 | 19,922 | 752,134 |

Previous turn on this page, final (incl. after its commit): 19 calls · 445,532 effective units.
CSV: `usage/chatgpt-history_claude_usage_session-c67e47e6_20261018_2144.csv`. Usage after this commit goes into the next turn's record.

## ASSISTANT RESPONSE

````
Export found on your PC's Google Drive folder, hashed and inventoried without extracting it: 811 chats (May 2025–Oct 2026), 27,158 messages, 1,679 files. It has no memory file — ChatGPT's export never includes memory. Plan v0.1 is in Git; two decisions needed: large files (>95 MB) Drive-only pointer vs LFS, and a separate memory export.

Git Evidence
- Repo: vsenthil7/chatgpt-history-workbench · main
- Turn: T003 · Read at: ea77763
- Commit: <THIS-COMMIT>
- Verified: ls-remote main = local head
- Usage: 27 calls · 752,134 effective units (MEASURED, to commit)
- Research: Drive metadata; zip read in place on PC (G:\My Drive); inventory script output hash-checked both sides; claude-history importer + SOURCE_CHECKSUMS read for parity; GitHub 100 MB file limit and 1 GB free LFS quota (known limits)
- Gaps: no memory file in the ChatGPT data export; 4 entries >95 MB need a decision; import not started (waits for go)
````
