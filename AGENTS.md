# AGENTS.md — ChatGPT History Workbench

Read this first on every AI surface (Claude, ChatGPT, Perplexity, Codex, Claude Code, any human).

This **private** repository is the import of Senthil's ChatGPT data export (chats, memory, uploaded/generated files) into Git, built the same way as `vsenthil7/claude-history-workbench`, plus the working record of the import itself. 100% internal.

## Repo boundary
- Single landing place for the ChatGPT history. Everything is imported here first, unsorted by product.
- Per-product repos link back to files here by path; history is not copied twice.
- Always private: it holds full chat history.
- Later exports are re-imported periodically and compared with earlier ones, so whatever each export contains is tracked and nothing is missed.

## Global layer
Read `vsenthil7/ai-workspace-standards` @ `93e0d89` → `STANDARDS.md` before the first turn on any page (same pin as claude-history-workbench on 2026-10-18).
Local rules: `protocol/PROTOCOL_PIN.md`.

## Protocol
Git Turn Protocol v1.2 (`vsenthil7/ai-tool-support-kb` → `protocol/git-turn/GIT_TURN_PROTOCOL_v1.2_20261012_1215.md`, commit `5266ee4`), as in claude-history-workbench.
Close every turn with: `python3 -I scripts/turn_close/turn_close.py --turn T### --topic ... --ai ... --research ... --gaps ...` (settings: `.turn_close.json`).

## Folder map (mirrors claude-history-workbench)
| Folder | Holds |
|---|---|
| `source/` | export checksums, redaction log — proof of where everything came from |
| `raw/exports/<YYYYMMDD>/` | each ChatGPT export kept as received — VERBATIM |
| `raw/conversations/YYYY/MM/` | one chat per file — VERBATIM except logged redactions |
| `raw/memories/`, `raw/files/` | memory and file categories of the export |
| `readable/conversations/YYYY/MM/` | DERIVED readable version of each chat |
| `index/` | conversations.csv, manifest, timeline, export-to-export diff |
| `scripts/` | importer, verifier, redactor, usage, turn close — rerunnable |
| `usage/` | per-session MEASURED usage |
| `docs/plans/` | versioned plans, one file per version |
| `turns/YYYY/MM/DD/` | one file per turn (`T###-HHMM-topic.md`) |
| `context/`, `protocol/`, `handover/` | state, pin, next-page prompt |

File names for derived/working files: `chatgpt-history_<ai>_<type>_<topic>_YYYYMMDD_HHMM.<ext>`.

## Provenance values
`VERBATIM`, `RECONSTRUCTED` (labelled), `UNRECOVERABLE`. Never present a reconstruction as an original.

## Rules carried from Senthil's standards
- Every turn starts with pull-and-merge; never overwrite other AIs' work.
- No deletes of files or branches without Senthil's explicit say-so.
- Live-looking credentials are redacted before push and logged in `source/REDACTIONS.md`.

## Fresh-page bootstrap
Read in order: `AGENTS.md` → `protocol/PROTOCOL_PIN.md` → `context/current-state.md` → `handover/NEXT_PAGE_PROMPT_CURRENT.md` → `index/timeline.md` → only the turns/plans needed.
