# EngageOS — which files are current (16 Sep 2026, 18:40)

**Five are current.** Everything earlier is superseded and kept only for the audit trail.

| Use this | What it is |
|---|---|
| `claude_v042_engageos_sprint_tracker_traceability_20260916_1840.xlsx` | **Tracker**, the execution record. Now holds every finding with its disposition (V001's 18, updated, plus F-050 to F-054), gates CG-G0 to CG-G11, the S00 to S19 plan, 100 events, a 14-item handover and four audit passes. Start here. |
| `claude_v047_engageos_whatsapp_product_workbook_20260916_1840.xlsx` | **Product workbook**, the backlog and its status. Still 100 stories / 399 points. The hardening programme stays on its own sheet. |
| `engageos_v0.46.0_src.zip` | **The product.** 62 suites / 512 tests, 100% coverage. 11 of the tests ran against a real Postgres. All 14 CI steps pass from a clean unzip. |
| `audit_kit_v110.zip` | **The reusable part**, for your other eleven products. Unchanged this release. |
| `chatgpt_review_V001_MoPr07-engageos_whatsapp_20260913_2300.xlsx` | **External review V001.** Keep it. Every F-CG finding traces back to a row in it. |

## Supersession rule
The higher version always wins. The workbook (v047) and the tracker (v042) are numbered separately. The timestamps in the filenames show their order.

## What changed in this release
Phase 3 of the response to the review. Everything that could be done without Meta access or a paying customer is done:

- **F-CG-003, code half.** The signup callback now runs Meta's Embedded Signup steps:
  - it exchanges the sign-up code for a token, and `debug_token` confirms the token is valid, belongs to this app and carries both WhatsApp permissions;
  - the account (WABA) and phone number come from Meta's own answer;
  - an account id or number forged on the URL is refused.

  Nothing invents a token any more. This has not yet run against real Meta.
- **F-CG-004, first slice.** Tenant connections are now stored in Postgres and survive a restart. The database refuses any token that isn't encrypted. All other data is still held in memory only.
- **F-CG-005, closed.** The shipped server was run against a **real Postgres 16.13**. It started, came back after a restart with its tenants intact, and answered 503 on `/readyz` while the database was stopped.
- **F-CG-008, slice.** Agents can log out, and an owner can cut off every session a departed agent holds, on every server instance.
- **F-CG-009 / S07.** Added rate limits, type checks on every request body, and a rule that tokens are only sent to Meta's own hosts (SSRF). CSRF cannot happen by design, and a test checks that stays true.
- **S00.** Added an SBOM (software bill of materials) and a dependency-audit policy. `npm audit` finds 0 vulnerabilities.

Running things on a clean machine, instead of reading them, turned up **five new defects**:

- migrations failed on their second run (F-050);
- a check the record said was in CI was never in the CI file (F-051);
- a database restart crashed the server (F-052);
- the build relied on a tool that was never declared (F-053);
- the smoke test could never pass, so **CI has never been green end to end** (F-054).

All five are fixed.

## If you only have twenty minutes
1. Open the tracker and read **Senthil_Handover**. Item 3 now lists `META_APP_ID` and `ENGAGEOS_CRED_KEY`. Item 5 is now "External review V002".
2. Send the zip to the reviewer. `docs/REVIEW_PACK.md` opens with six claims to try to break.
3. Item 13, choosing one target customer (ICP), is still the biggest single unblock.

## What is true about the product
**312 of 399 points** (80 of 100 stories) are done in code. The 15 Sep version of this file said 309, but the traceability matrix has said 312 since v040. **Zero are Done**, because Done means listed and paid for. A real database is not a real customer.
