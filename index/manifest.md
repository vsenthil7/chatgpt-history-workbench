# Manifest — chatgpt-history-workbench — 2026-10-18

One ChatGPT data export imported so far: **20261014** (`Chatgpt-export-20261014.zip`, 920,955,775 bytes, SHA-256 in `source/SOURCE_CHECKSUMS.md`). The zip stays on Senthil's Google Drive (`My Drive/chatgpt-export/`) and is never copied into Git.

## What is in Git
| what | where | count | fidelity |
|---|---|---|---|
| chats | `raw/conversations/YYYY/MM/YYYYMMDD_HHMM_<id8>.json` | 811 (2025-05-23 → 2026-10-13) | VERBATIM except logged redactions |
| readable chats | `readable/conversations/YYYY/MM/<same stem>.md` | 811 · 25,577 messages | DERIVED (text, thoughts, voice transcripts verbatim) |
| other data files | `raw/data/` | 9 | byte copies (logged redactions) |
| attachments | `raw/files/<file id>__<real name>` | 1,634 · 518 MB | byte copies (text files may carry logged redactions) |
| chat index | `index/conversations.csv` | 811 rows | DERIVED (size = ESTIMATE, chars/4) |
| ChatGPT Projects | `index/projects.csv` | 142 project ids (names are not in the export) · 546 chats in projects | DERIVED |
| attachments index | `index/files_20261014.csv` | 1,679 rows (git / drive-only) | DERIVED, SHA-256 per file |
| export inventory | `index/exports/20261014/` | entries, chats, summary | DERIVED |
| export baseline | `index/exports/baseline_20261014.md` | — | for comparing the next export |

## Not in Git, on purpose
| what | why | listed in |
|---|---|---|
| 3 attachments over 95 MB + `chat.html` | GitHub 100 MB file limit; chat.html is a rendered copy of the chats | `index/large_files.csv` |
| 42 zips/xlsx with credentials inside | not rewritten; kept unchanged in the Drive zip | `index/held_back_files.csv`, `source/CONTAINER_SECRET_HITS_20261014.csv` |
| `user.json` | account email and birth year, not history | `source/SOURCE_CHECKSUMS.md` |

## Not in the export at all
- **827 files** that chats refer to (382 with their names) are missing from the zip → `index/missing_files_20261014.csv` (UNRECOVERABLE from this export; `compare_exports.py` reports if a later export brings any back).
- **Saved memory**: ChatGPT's data export does not include it.
- **ChatGPT Project names**: only the ids (`g-p-…`) are in the export.

## Redactions
`source/REDACTIONS.md`: 3 runs, 134 values in total (98 + 27 + 9; a file can appear in more than one run). Run 3 (T006) caught 9 values that JSON escaping had hidden from runs 1–2.

## How to check
`python -I scripts/verify_raw.py <export zip> .` → exit 0 = every chat, data file and attachment equals the zip apart from the logged redactions, and every Drive-only item's SHA-256 matches.

## Next export
Follow the import order in `AGENTS.md`, then `python3 -I scripts/compare_exports.py . <NEW> 20261014`.

## Added 2026-10-20 [claude, T010]
| what | where | note |
|---|---|---|
| repair notes | `repairs/` | additive corrections to pushed turns (records never edited) |
| turn audit | `docs/reports/turn-audit_20261020/` | audit outputs + session-log extracts (input + final reply per turn, byte copies) |
| audit scripts | `scripts/turn_audit/` | `audit_turns.py` (copy of master) · `final_replies.py` (reply extractor) |
| handover | `context/latest-handover.md`, `handover/…next-page-prompt_v00N_…md` | append-only handover; immutable next-page prompts |
