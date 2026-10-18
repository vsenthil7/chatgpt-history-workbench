# Finding — claude-history-workbench still holds credential-shaped strings — 2026-10-18 23:00

Found by: claude, T006 of chatgpt-history-workbench, while checking whether the Claude workbench shares the JSON-escaping gap fixed here.
Scope of this note: report only. Nothing was changed in claude-history-workbench (repo boundary; needs Senthil's "go").

## What was run
`python3 -I scripts/secret_scan.py raw readable` (this repo's copy, same BLOCK patterns as the master) on a clone of
vsenthil7/claude-history-workbench @ 0c1ee3e (shallow, read-only).

## Result
- **1,539 blocking lines** (712 phone-like warnings) in 214 files: 199 raw/conversations, 14 readable/conversations, 1 raw/projects.
- By kind (lines): credentialed URL 770 · assigned password/secret 645 · GitHub token 42 · OpenAI/Anthropic-style key 25 · private key 18 · bearer token 13 · Stripe live key 11 · JWT ~10.
- Per file and kind (no values): `chatgpt-history_claude_finding_claude-history-secret-scan_20261018_2300.csv`.

## Why
That repo's `redact_secrets.py` redacts only two kinds (Anthropic `sk-ant-api03-…`, Google `AIza…`). Its pre-commit scan runs on staged files at turn close, and bulk imports went in as batches.
Many hits will be test fixtures inside replayed code, but GitHub tokens, Stripe live keys and private keys should be treated as real until checked.

## Proposed next step (needs "go", runs in that repo)
1. Copy this repo's redactor (all BLOCK kinds, ALLOW honoured, JSON value level, append-only log) and `scan_containers.py`.
2. Redact raw/ + readable/, rerun verify_raw there (needs that export's zips), then push.
3. Senthil: rotate GitHub tokens, Stripe live keys, and any real DB passwords/keys listed.
History: the values stay in earlier commits of that private repo until history is rewritten. Rotation is the real fix; a history rewrite would need a force push and Senthil's explicit say-so.
