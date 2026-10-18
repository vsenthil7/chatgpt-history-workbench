# Plan v0.1 — import the ChatGPT export into Git — 2026-10-18 21:45 Europe/London

Status: PROPOSED — waiting for Senthil's "go". Author: claude (T003).

## What the export holds (from `index/exports/20261014/`, read in place, nothing extracted)
- Zip 920,955,775 bytes, SHA-256 `43f44e15…9115`; 1,700 entries; 1.65 GB unpacked.
- **811 chats**, 2025-05-23 → 2026-10-13, 27,158 message nodes, in 9 files `conversations-000…008.json` (203 MB).
- **1,679 attached/generated files** stored as `file_….dat`; 1,520 have their real name in `conversation_asset_file_names.json` (750 png, 245 jpg, 156 zip, 87 md, 66 xlsx, 48 txt, 40 json, 20 pdf, 2 mp4 …).
- Other data: `library_files.json`, `group_chats.json`, `shared_conversations.json`, `message_feedback.json`, `user_settings.json`, `export_manifest.json`, `chat.html` (159 MB, a rendered copy of the same chats).
- **No saved-memory file.** ChatGPT's data export does not contain memory. Nothing else is in the Drive folder, and no memory file was found on the PC since 10 Oct.

## Where the work runs
On Senthil's PC through the bridge, because the cloud workspace cannot reach Google Drive and the connector cannot carry a 921 MB file.
Clone: `C:\Users\v_sen\develop\chatgpt-history-workbench`, next to his other workbenches. The zip is read straight from `G:\My Drive` and never copied or changed.

## Large files — decision proposed
GitHub refuses files over 100 MB, and GitHub LFS's free quota is 1 GB.
**Proposal:** files over 95 MB stay in Drive only. Git keeps a pointer row with name, size and SHA-256 in `index/large_files.csv`.
That covers 3 attachments (two screen-recording mp4s, 328 MB and 139 MB; one WhatsApp-export zip, 221 MB) and `chat.html` (159 MB, derived).
Everything else goes into Git, about 0.8 GB, pushed in batches.

## Slices
| # | Slice | Output |
|---|---|---|
| S1 | Clone on PC, add `scripts/import_export.py` (stdlib, streams each conversations-00N.json) | script in Git |
| S2 | Raw chats: one file per chat `raw/conversations/YYYY/MM/YYYYMMDD_HHMM_<id8>.json` (VERBATIM, re-serialised) | 811 files |
| S3 | Raw data files: library_files, group_chats, shared_conversations, message_feedback, user_settings, export_manifest, asset name map → `raw/` byte copies | 7 files |
| S4 | Attachments under 95 MB → `raw/files/<file_id>__<real name>` byte copies; large-file pointers | ~1,675 files + csv |
| S5 | Redaction scan of everything (credentials) before push; log in `source/REDACTIONS.md` | log |
| S6 | `scripts/verify_raw.py`: zip SHA-256 = source, every chat JSON-equal to the export, every byte copy CRC-equal | exit 0 |
| S7 | Readable chats `readable/conversations/YYYY/MM/<stem>.md` (main branch of each tree; text verbatim, tool calls summarised) | 811 files |
| S8 | `index/conversations.csv` (+ GPT/project id, files linked), `index/manifest.md`, timeline | indexes |
| S9 | Export-to-export compare script (`scripts/compare_exports.py`), run once as the baseline | baseline report |

Push in batches (≤ ~200 MB per push). Every batch commit is listed in the turn record.
One turn per slice group: T004 = S1–S3, T005 = S4–S6, T006 = S7–S9.

## Open decisions for Senthil
1. Large files over 95 MB: Drive-only pointer (proposed), or Git LFS?
2. Memory: export it from ChatGPT (Settings → Personalization → Manage memories) and drop it into `My Drive/chatgpt-export/`, so it can be imported in S3.
