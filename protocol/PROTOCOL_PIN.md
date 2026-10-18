# Protocol Pin

Repository: vsenthil7/chatgpt-history-workbench
Global layer: **vsenthil7/ai-workspace-standards @ 93e0d89 → STANDARDS.md (S1.0)**, from 2026-10-18 (T002).
Protocol: **Git Turn Protocol v1.2** — vsenthil7/ai-tool-support-kb, `protocol/git-turn/GIT_TURN_PROTOCOL_v1.2_20261012_1215.md`, commit 5266ee4.
Local rule: close every turn with `scripts/turn_close/turn_close.py` (master: ai-tool-support-kb `scripts/turn_close/`). Settings: `.turn_close.json`.
Template repo: vsenthil7/claude-history-workbench @ 0c1ee3e (layout, scripts, record format).

## Dated decisions
- 2026-10-18 21:32 (T001): repo name `chatgpt-history-workbench`, mirroring `claude-history-workbench`.
- 2026-10-18 21:34 (T002): Senthil created the repo; bootstrapped from the Claude workbench layout.
- 2026-10-18 21:47 (T004): plan v0.1 approved ("go 21:47"); files > 95 MB Drive-only with pointer rows (S4).
- 2026-10-18 21:59 (T004, D3 here): redaction = every match of secret_scan.py's BLOCK list (ALLOW honoured), logged append-only in source/REDACTIONS.md; verify_raw.py proves raw/ = export apart from those.
- 2026-10-18 22:00 (T004): bulk imports run on Senthil's PC clone (C:\Users\v_sen\develop\chatgpt-history-workbench); the zip is read in place from G:\My Drive. Batch commits listed in the turn record.
