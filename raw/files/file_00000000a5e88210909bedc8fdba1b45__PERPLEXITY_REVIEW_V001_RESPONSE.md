# Response to Perplexity independent review V001

**Review:** Perplexity Computer, independent second reviewer, 16 September 2026, 19:32 BST — verdict CONTINUE at 6.1/10; 12 new findings (PX-001..PX-012), 2 BLOCKER, 3 HIGH.
**Response:** codebase v0.37.0, workbook v037, tracker v030, 20 September 2026.

## Position

Accepted in full, and the sequencing argument is accepted as the most important part of it: PX-S0 (async platform
boundary), PX-S1 (enforce what is sold) and PX-S2 (close the gate's blind spots) were executed *before* any adapter
work, exactly as the review's dependency graph requires. Nothing in S37–S41 has been started on top of the old core.

Gate G0 stays closed. The enterprise-ready claim stays withdrawn. Nothing in this release moves enterprise readiness;
it moves the thing under it — whether the core can host a real adapter at all.

## What this release closes

| ID | Severity | Finding | State after v0.37.0 | Permanent regression |
| --- | --- | --- | --- | --- |
| PX-001 | BLOCKER | Entire platform boundary synchronous | **FIXED.** Nine platform interfaces are Promise-returning (the review's four plus OAuthClient, PaymentProvider, the live-sweep SlackApi, ResponseUrlPoster, ModalOpener); `IncidentWorkflow.declare/resolve/reopen`, timeline capture, degradation, breaker and the ack contract are async; every platform call runs under a 10 s budget and a timeout is a degraded result, never a hang. | `tests/px/asyncBoundary.test.ts` — TS compiler API over the interfaces + reflection over real adapter instances + a floating-promise rule over `src/` and `scripts/` |
| PX-002 | BLOCKER | Plan limits unenforced: `claimWrite` tested, `checkWrite`/`recordWrite` shipped | **FIXED.** `recordWrite` deleted; `declare()` and `reopen()` call `await entitlements.claimWrite()`; without a shared meter the in-process counter is still incremented. | `tests/px/enforcementWiring.test.ts` — builds the production composition, declares `limit` then `limit+1`, asserts the store's counter; two-workflow/one-store race; monthly reset once per cycle |
| PX-003 | HIGH | Two user-facing Slack paths outside the boot gate | **FIXED.** `REQUIRED_PROVIDERS` is a closed set of ten (adds `responseUrlPoster`, `modalOpener` and — not in the review — `oauth`); `ProviderSet` is typed to exactly those keys (compile-time assertion); every provider implements `healthcheck()` and production probes all of them. The `console.log` closure is now `StdoutResponseUrlPoster`, named and refused. | `tests/px/providerGate.test.ts` — structural closed-set assertion; correctly-named-but-failing adapter refused; fully-faked-but-healthy composition PERMITTED |
| PX-004 | HIGH | Queued declares lost on SIGTERM | **FIXED.** Deferred work is a persisted descriptor (`deferred_work`, migration 0014) written before the ack returns, leased while running, deleted after delivery; `SlashCommandAck` is Drainable and registered first with `Lifecycle`; `restore()` reloads pending rows; 3 attempts then a definite failure. | `tests/px/ackDurability.test.ts` — SIGTERM drain, kill -9 restore, lease across replicas, give-up path, export/purge as tenant data |
| PX-005 | HIGH | Key rotation had no possible caller | **FIXED (rotation path); KMS remains S43.** `EnvKeyVault` loads every `ENCRYPTION_KEY_<id>`, `ENCRYPTION_KEY_CURRENT` selects; `POST /ops/rotate-keys` re-encrypts under the current key, idempotent and resumable; boot warns while any record references a non-current key. | `tests/px/identityAndWindows.test.ts` — k1 → k2 read and re-write, stale warning, idempotent second run |
| PX-006 | MEDIUM | Leases dedupe concurrency, not frequency | **FIXED.** `job_leases.last_run_at` (migration 0013); `acquireDue` grants only when the stored last run is older than the interval; `recordRun` advances it. | `tests/px/leaseFrequency.test.ts` — five restarts in a day run the daily sweep once; second replica refused inside the interval |
| PX-007 | MEDIUM | Paging union cannot express D-OC7 targets | **FIXED.** `PagingProviderId = pagerduty \| opsgenie \| jsm \| compass \| webhook`; config accepts all five. | `tests/px/identityAndWindows.test.ts` |
| PX-008 | MEDIUM | Workflow handed a literal provider name | **FIXED.** The workflow receives the constructed adapter; `wf.pagingProviderId()` is asserted equal to the inventory. | same |
| PX-009 | MEDIUM | Financial model never computed | **FIXED in the workbook.** Cached values written for all 18 months; the review's figures reproduced (M18 net +$444, cumulative −$213,302, 305 paying accounts); sensitivity rows added. | workbook `Financial_Model` |
| PX-010 | MEDIUM | Sessions cannot be revoked | **FIXED.** `installEpoch` claim; resolver refuses any token whose epoch is not the workspace's current one; uninstall / reinstall / data deletion / `bumpEpoch` revoke immediately; tenant deletion also forgets the in-process install record. | `tests/px/identityAndWindows.test.ts` |
| PX-011 | MEDIUM | Replay window bounded by row count | **FIXED.** `loadSince(now − 6 h, cap 50,000)`; window documented against Slack's retry behaviour next to the ack budget. | same + `tests/px/pgStores.integration.test.ts` |
| PX-012 | LOW–MED | Positioning undersells the price gap; free tier covers 4/5 modules | **ADDRESSED in docs and workbook.** Pricing moved to workspace-size bands (D-OC8, awaiting ratification); PRICING_FAQ regenerated from the engine and gate-tested; Risk_Register and LISTING guidance updated. | `tests/pricingDoc.test.ts` |

## What this release found that the review did not

- **PX-013 — F-033's atomic id allocator was not on the declare path.** Found mechanically by the new audit check A10 run
  against V037 itself: `SequenceAllocator.claimNext` was fully tested and called by nothing in `src/` or `scripts/`, so
  two replicas under blue/green could still mint the same `INC-` id. Fixed: `declare()` claims the id from the shared
  allocator; production refuses a workflow registry built without it (`atomicIds` in the durability inventory).
- **The OAuth client was also outside the gate** (PX-003 listed two paths; there were three).
- **Two sync-throwing stubs and one floating `.then`** — caught by the new PX-001 gate on its first run, before the
  review would have.
- **`Lifecycle.shutdown` re-checked pending per drainable, not per round** — draining the ack queue produced sink rows
  that the same round then reported as lost. Fixed and covered by the SIGTERM test.

## Still open, with owners

| ID | What remains | Sprint |
| --- | --- | --- |
| PX-014 | `DegradationService` replay queue is in memory and nothing replays it (A12) | S42 |
| PX-015 | `EventReceiver` retry queue is not drained at shutdown (A12); low risk today because the runtime handler never fails | S42 |
| CF-012 / PX-005 | KMS-backed vault behind the `SecretsVault` contract | S43 |
| D-OC8 | Banded pricing implemented and reversible in one table; needs ratification | Senthil |
| — | Real adapters (Slack, OAuth, poster, views.open, Stripe, paging, AI, status page) — now drop-ins behind async contracts | S38, S40, S41, S45, S46 |

## Evidence

`npx tsc` clean over `src/` + `scripts/`; `npx tsc -p tsconfig.all.json` clean; `npx jest --coverage`: 60 suites, 624
tests (616 run, 8 gated on a real Postgres), **100.00% statements / branches / functions / lines over `src/` and
`scripts/`** — `scripts/` is inside the gate for the first time (A9 closed). Built artifact: `APP_ENV=production` refuses
naming all ten providers and their probe results; `APP_ENV=development` boots, answers `/health` and `/ops/composition`,
and drains cleanly on SIGTERM. `node audit.mjs` v3: A10 clean, A11 clean, A13 clean; A12 reports PX-014/PX-015.
