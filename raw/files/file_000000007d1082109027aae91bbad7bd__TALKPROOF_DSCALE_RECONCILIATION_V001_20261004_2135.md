# TalkProof — D1–D7 Scale Reconciliation (narrow evidence gate)

**Artifact:** `TALKPROOF_DSCALE_RECONCILIATION_V001_20261004_2135.md` · **Date:** 2026-10-04 21:35 · **Role:** independent evidence reconciler
**Inputs read:** V5 (`TALKPROOF_REQUIREMENT_RECOVERY_V5_20261004_2058.md`, Parts 38/41/43/44/45/46), V5 Gate Review (`TALKPROOF_V5_GATE_REVIEW_V001_20261004_2115.md`, immutable), backend ZIP (`talkproof-backend-master`), admin ZIP (`talkproof-admin-main`), Flutter ZIP (`talkproof-app-master`). Original Product Owner review brief: **not attached**; its D1–D7 names and provider-progression stages were supplied verbatim in the gate instruction and are used as the authoritative source.
**Governance honoured:** nothing built; V5 unmodified; gate review unmodified; no V6; no PO decision taken; no FR/NFR ID, sprint, architecture or code created. The five accepted gate-review corrections (R-36, R-44/45, R-D26, R-EV7, R-SCALE) are taken as given and not reopened, except where R-SCALE itself requires this D-level re-read.
**Row numbering:** V5 Part 38 numbering is used throughout (44 = Config resolver, 45 = WhatsApp). After R-44/45 is applied in V6 these two numbers swap to V4 order (44 = WhatsApp, 45 = Config resolver). Every row below names the capability so the swap cannot cause ambiguity.

---

## A. Authoritative source and interpretation

### A.1 Authoritative scale (as supplied)

D1 SPECIFIED · D2 DESIGNED · D3 IMPLEMENTED · D4 CONTRACT VERIFIED · D5 LIVE INTEGRATED · D6 PRODUCT E2E VERIFIED · D7 PRODUCTION READY.

### A.2 Interpretation applied to every row (one rule set, applied uniformly)

| Level | Test applied to repository evidence |
|---|---|
| D1 | A requirement exists; nothing in the repository designs or implements the capability (E-01 class AB). |
| D2 | A design artefact exists but the capability itself is not implemented: interface/seam/abstract class, stub returning fixed or fake values, configuration-only, documentation-only design (E-01 classes SEAM, ST, CO, P where the partial part does not deliver the required capability, and documented runbooks). |
| D3 | The capability is actually implemented in production code, whether or not it is hard-coded, unintegrated, defective at integration, or only mock-tested (E-01 classes IW, INI, HC, and P where the required capability is delivered). |
| D4 | All six gate conditions hold: (1) production implementation/adapter exists; (2) the contract is clearly defined; (3) tests exercise that production implementation rather than replacing it; (4) requests/inputs and responses/outputs are validated against the documented/sample contract; (5) required error/edge behaviour is tested; (6) the evidence genuinely establishes contract compatibility. A test stub may replace the **external provider**, never the production adapter. Interface existence, mocked implementation, fake-ID stubs, unit coverage, tests that mock the adapter away, and unrelated acceptance tests cannot establish D4 (per the brief) **and do not themselves fix the D1/D2/D3 level — that is determined independently by the rows above** (per the 21:20 correction). |
| D5 | A recorded live execution against the real external provider or a real deployment, present as an artefact in a repository. |
| D6 | A recorded product-level end-to-end run (real stack, real providers) present as an artefact. |
| D7 | Operated-in-production evidence (deployment records, runbook exercised, monitoring) present as an artefact. |

Two consequences of A.2 for this reconciliation:
- The authoritative D1/D2 boundary differs from the E-01 working scale in one place that matters: a designed interface with a Noop/Fake implementation is D2 (DESIGNED) even when no concrete target yet exists to plug into. This moves row 32.
- The authoritative D4 is reachable without credentials or a live run. The gate review's "nothing can reach D4" rested on the E-01 reading "no live run ⇒ no D4", which the brief explicitly corrects. Every candidate was therefore re-audited (Section C).

### A.3 How partial-vs-requirement judgements were handled

Where V5 lowered a row because the implementation does not deliver what the requirement specifies (rows 16, 18, 21, 22, 23, 27, 29, 38), both scales classify the result identically (capability not implemented as required ⇒ D2). Those rows were re-read, not carried blindly; none moves. Where V5 kept D3 for a narrow-but-real implementation (rows 37, 42), the same rule holds and none moves.

### A.4 Test-execution basis

The backend test suite runs against a real PostgreSQL test database (`services/api/tests/conftest.py:33-66`, `TEST_DB_URL`, transactional `db_session`), not SQLite or mocks. CI (`.github/workflows/ci.yml:28-45`) provisions `postgres:15-alpine`. Provider boundaries are patched as inventoried in V5 Part 44. Pass counts are taken from V5 Part 44 (E-01 §J) and were not re-executed here; this reconciliation re-read the test *sources*, which is what the D4 question turns on.

---

## B. 46-row reconciliation

Columns: **V5 D** = V5 Part 38 value · **Gate corr.** = value after R-36/R-44/45 · **Auth. D** = highest level supported under A.2 · **Changed?** = vs gate-corrected value. Split rows keep split values; the first value is the "primary" used for distribution counts, matching V5's convention.

| # | Capability | V5 D | Gate-review correction | Authoritative-scale D | Changed? | Evidence | Reason |
|---|---|---|---|---|---|---|---|
| 1 | Tenancy Tier A (RLS) | D2 (RLS) / D3 (app) | — | D2 (RLS) / D3 (app) | No | `core/tenancy.py` helpers defined, never called; no `POLICY` in `alembic/versions`; app-layer tenant scoping wired | RLS is designed (helpers) not implemented ⇒ D2; app scoping implemented ⇒ D3 |
| 2 | Tenancy Tier B / C | D3 / D2 | — | D3 / D2 | No | `isolation_service.py:118-131,146-187`; no `search_path` routing; Tier C dict manifest | B: `CREATE SCHEMA` implemented, routing absent — capability partially delivered ⇒ D3 as V5; C config-only ⇒ D2 |
| 3 | Auth core | D3 | — | D3 | No | `auth_service.py`, `mfa_service.py`, `config.py:37`; tests exercise real argon2/JWT; HS256 hard-coded | Implemented, hard-coded ⇒ D3. Internal contract (JWT claims) is tested but no external documented contract applies; D4 not claimed |
| 4 | SSO OIDC / SAML / SCIM | D2 / D2 / D3 | — | D2 / D2 / D3 | No | `routes/sso.py` 3 routes; `_exchange_code` returns token JSON as claims; no SAML ACS; `routes/scim.py:37-80` POST/GET/PATCH Users; `scim_service.py:75` URN | OIDC partial (no id_token validation) and SAML seam ⇒ D2; SCIM implemented ⇒ D3. SCIM D4 audited and rejected (C.11) |
| 5 | RBAC | D3 | — | D3 | No | `core/rbac.py:234-273` | Implemented and wired |
| 6 | Audit chain | D3 | — | D3 | No | `audit_repo.py:29-39`; `forensics.py:140-157`; no `with_for_update` | Implemented; CD-07 defect does not change level |
| 7 | SIEM export | D3 | — | D3 | No | `siem_service.py:21-67` HMAC + `_post`; `tests/unit/test_m04_forensics.py:254-269` patch `_post` | Implemented, no caller. D4 rejected: contract is TalkProof-proprietary (no external documented contract), transport patched (C.4) |
| 8 | BYO key store / router | D2 (router) / D3 (store) | — | D2 (router) / D3 (store) | No | `decrypt_secret` only in `core/crypto.py`; resolve result discarded | Router does not deliver key resolution ⇒ D2; store implemented ⇒ D3 |
| 9 | Test-connection | D2 | — | D2 | No | `provider_service.py:162-171` length check | Stub ⇒ D2 |
| 10 | HiL engine | D3 | — | D3 | No | `hil_service.py`; `escalate_overdue` definition only | Implemented; escalation unscheduled |
| 11 | Governed AI envelope | D3 | — | D3 | No | `ai_service.py` envelope around stub | Implemented |
| 12 | Governed AI provider calls | D2 | — | D2 | No | `ai_service.py:79-93` constant envelope | Stub ⇒ D2 |
| 13 | Guardrails | D3 | — | D3 | No | `core/guardrails.py` regex/substring | Implemented |
| 14 | 3-model consensus | D3 | — | D3 | No | `orchestrator_service.py` real anthropic/openai/genai SDK calls, env keys; `tests/unit/test_orchestrator_service.py:158-277` patch SDK modules with `MagicMock` | Implemented (D3). D4 rejected: response fixtures are MagicMocks, no documented sample responses, no request assertions (C.5) |
| 15 | Transcription | D3 (inline) / D2 (abstraction) | — | D3 (inline) / D2 (abstraction) | No | inline whisper call in `orchestrator_service.py:319`; `services/transcription/base.py` Protocol + result type only; orchestrator imports none of it | Inline implemented ⇒ D3; abstraction is interface-only ⇒ D2. D4 rejected (C.5) |
| 16 | Hash + canonical + offline verify | D2 | — | D2 | No | `certified_voice_service.py:145-153` seven-key payload; no algorithm id; server-side self-check only | Capability as specified (FR-054(1) fields, FR-055 offline verify) not implemented ⇒ D2 (A.3) |
| 17 | RFC3161 TSA | D1 | — | D1 | No | absent | Specified only |
| 18 | Blockchain anchor | D2 | — | D2 | No | `iota_service.py:180-198` lazy `import iota_client` under `pragma: no cover`; not in `requirements.txt`; env stub id; `anchor_tx_id` never written | Unrunnable submit function + env stub; per-outcome anchor not implemented ⇒ D2 (A.3) |
| 19 | Certified PDF | D3 | — | D3 | No | `pdf_service.py` reportlab campaign report | Implemented (campaign-level) |
| 20 | S3 Object Lock | D1 | — | D1 | No | no bucket/lock provisioning anywhere in repo | Specified only |
| 21 | Client portal | D2 | — | D2 | No | no portal, no signed link; authenticated verify API only | Required capability not implemented ⇒ D2 |
| 22 | Campaign carrier abstraction + selection | D2 | — | D2 | No | `campaign_carrier/resolver.py:109-112` vs `config.py:46` (CD-01); `twilio_adapter.py:39` `_place` stub; Telnyx/Vonage absent; `tests/unit/test_exotel_service.py:29` patches whole `httpx` module | Abstraction/resolver code is implemented, but no functioning carrier sits behind it (Exotel mis-wired, Twilio stub) — the selectable-carrier capability is not delivered ⇒ row D2 unchanged. Exotel D4 rejected (C.6) |
| 23 | M12 PSTN out/in + numbers | D2 | — | D2 | No | stub dial/provision in `telephony_service.py`; inbound webhook `routes/webhooks.py:156-213` real to DB; `X-Exotel-Signature` HMAC scheme undocumented (EV-02) | Outbound/numbers stub ⇒ D2; inbound-to-DB path is D3-grade but the capability row (out + in + numbers) stays D2. No split added: gate review accepted the row and Task 3 did not request one |
| 24 | Recording dual-channel + storage | D1 (dual) / D3 (storage) | — | D1 (dual) / D3 (storage) | No | no dual-channel code; `storage/drivers/s3.py`, `drive.py` real; no production `.put(` caller | Dual absent ⇒ D1; storage drivers implemented ⇒ D3. Storage D4 audited and rejected (C.1); split preserved |
| 25 | Chat REST | D3 | — | D3 | No | `chat_service.py`, `routes/chat.py` | Implemented |
| 26 | Chat realtime + presence | D2 | — | D2 | No | no WebSocket; presence REST only | Required realtime capability not implemented ⇒ D2 |
| 27 | E2E DMs | D2 | — | D2 | No | flag + ciphertext-required; no keys/client crypto | Not implemented as required ⇒ D2 |
| 28 | Meetings scheduling | D3 | — | D3 | No | `meeting_service.py` DB + stub SFU token | Implemented |
| 29 | Meeting rec/transcript/summary | D2 | — | D2 | No | state rows; client-posted transcript; stub summary | Not implemented as required ⇒ D2 |
| 30 | Push + email | D2 | — | D2 | No | `notification_service.py` `_dispatch` stub | Stub ⇒ D2 |
| 31 | Flutter app (web/desktop) | D3 | — | D3 | No | `talkproof-app-master/lib/src/api` REST client; `android/` only; `test/` 19 files use MockClient; `integration_test/` 4 journeys not run | Implemented REST client ⇒ D3. No live E2E artefact; D4 not applicable (no external contract fixture) |
| 32 | Flutter mobile native | D1 | — | **D2** | **Yes — raised** | `lib/src/mobile/biometric_gate.dart:1-16` `abstract class BiometricAuthenticator` + `FakeBiometricAuthenticator`; `lib/src/mobile/call_controller.dart:9-15` `abstract class NativeCallBridge` + `NoopCallBridge`; `pubspec.yaml` has no platform plugins; no `ios/` | Designed interfaces with Noop/Fake implementations exist in product code ⇒ D2 DESIGNED under A.2. The gate review called this row scale-sensitive and resolved it D1 under E-01 ("no native target"); the authoritative scale defines D2 by design existence, not by target existence |
| 33 | Admin portal | D3 | — | D3 | No | `talkproof-admin-main/src` wired to real routes; 33 Vitest files, 24 use `vi.spyOn/vi.mock`; `tests/e2e/*.spec.ts` 11 Playwright specs (V5 says 12 — count re-taken from ZIP: 11), not run | Implemented ⇒ D3 |
| 34 | Observability | D3 | — | D3 | No | `routes/ops.py` health/ready/prometheus | Implemented minimal |
| 35 | Resilience | D2 | — | D2 | No | `core/resilience.py` primitives; only `routes/ops.py` imports | Primitives wrap nothing ⇒ D2 |
| 36 | DR | D1 | R-36 → D2 | D2 | No (vs gate) | `docs/40_operations/DR_RUNBOOK.md`; `docs/15_deployment/DEPLOYMENT.md §11`; `deploy/scripts/backup.sh` absent | Documented design, no executable artefact ⇒ D2. R-36 stands |
| 37 | GDPR export/erase | D3 | — | D3 | No | `compliance_service.py` narrow | Implemented (narrow) |
| 38 | TCPA consent | D2 | — | D2 | No | `require_consent` never called; DNC absent | Enforcement not implemented ⇒ D2 |
| 39 | KMS envelope | D2 | — | D2 | No | Fernet from JWT secret | Not implemented as required ⇒ D2 |
| 40 | Security headers / rate limit | D3 / D2 | — | D3 / D2 | No | `main.py:78-81` four middlewares, no `RateLimitMiddleware` | Headers implemented ⇒ D3; limiter unregistered but implemented… kept D2 per V5 split (limiter does not deliver rate limiting) |
| 41 | White-label | D3 (UNABLE beyond D3) | — | D3 | No | `whitelabel_service.py`; no custom-domain provisioning | Implemented ⇒ D3; custom-domain part remains unverifiable from repo |
| 42 | AI ledger | D3 | — | D3 | No | `ai_ledger_service.py` M07 only; orchestrator has no ledger reference | Implemented (narrow) |
| 43 | Storage abstraction | D3 | — | D3 | No | `storage/base.py`, `drivers/s3.py`, `drivers/drive.py`, `resolver.py`; `tests/unit/test_m23_s3_driver.py`, `test_m23_drive_driver.py`, `tests/integration/test_m23_storage_acceptance.py`; no production caller of `resolve_storage`/`put` | Implemented ⇒ D3. D4 rejected on three named gaps (C.1). This is the closest non-qualifying candidate in the repo |
| 44 | Config resolver | D3 (UNABLE as integrated) | — | **D4** (component) | **Yes — raised** | `services/config_resolver.py` (production class, real `ConfigRepository`/`AuditRepository`); contract documented in module docstring and `docs/92_planning/_plan_S46_M28_config_resolver.md:4-7`; `tests/unit/test_config_resolver.py` 22 tests + `tests/integration/test_config_resolver_acceptance.py` 2 tests, all against real Postgres, zero mocks; no importer in `app/` outside its own module | All six D4 conditions met for the component contract (C.2). Not integrated into any runtime path ⇒ cannot be D5. "UNABLE" is resolved: the component level is determinable from code; integration is a D5 question |
| 45 | WhatsApp channel | D2 (outbound) / D3 (inbound) | — | D2 (outbound send) / D3 (outbound governance, scheduling, persistence) / **D4** (inbound webhook + signature verification) / D2 (provider adapter) | **Yes — split refined; inbound raised** | `whatsapp_service.py:143-150` `_send` returns `wamid_<hash>`; `routes/webhooks.py:53-63,215-290`; `tests/integration/test_s34c_whatsapp_webhook.py` (6 tests through real route + DB, Meta-documented payload shape, `sha256=` HMAC); no `hub.verify_token` GET handler anywhere | Outbound send is a fake-ID stub with no Graph adapter ⇒ D2; governance/scheduling/persistence implemented ⇒ D3; inbound POST contract verified (C.3) ⇒ D4; adapter absent ⇒ D2. Primary (first) value stays D2 |
| 46 | Inbound calling + polymorphic pipeline | D3 | — | D3 | No | `pipeline_service.py`, `orchestrator` polymorphic source; `tests/integration/test_i02_pipeline_acceptance.py` over stubbed carrier; recording key never written | Implemented logic ⇒ D3; no external contract fixture ⇒ D4 not reachable |

**Row-count invariant:** 46 rows.

---

## C. D4 candidate audit

Each candidate was inspected for: production implementation; what the tests actually call; fixtures; documented/sample provider responses; request-schema and response-schema validation; callback/webhook contract; failure cases; authentication/signature contract; provider-neutral mapping; whether assertions establish the contract or merely exercise code.

### C.1 Storage abstraction — S3 and Drive adapters (rows 24, 43) — **D4 NOT JUSTIFIED** (D3 stands)

What is there (`services/api/app/services/storage/drivers/s3.py`, `drive.py`; `tests/unit/test_m23_s3_driver.py`, `test_m23_drive_driver.py`):
- Production adapters are real: `S3Driver.put/get/exists/delete` call `boto3` `put_object/get_object/head_object/delete_object` with `Bucket/Key/Body/ContentType`; `DriveDriver` maps keys via `appProperties.tp_key` and uses `files().list/create/update/get_media/delete`. (Condition 1 met.)
- Tests call the production driver and substitute only the provider client via `monkeypatch.setattr(d, "_client", ...)` (`test_m23_s3_driver.py:60-64`, `test_m23_drive_driver.py:86-89`). (Condition 3 met for S3; see Drive caveat.)
- The S3 fake enforces boto3's keyword-only parameter names and raises a `ClientError`-shaped exception (`.response["Error"]["Code"]`, `ResponseMetadata.HTTPStatusCode`) — shapes that do match botocore's documented structure. Error cases covered: NoSuchKey→404, 404 status→404, AccessDenied propagates (`:107-114`), unconfigured→503, idempotent delete.

Why D4 is not established:
1. **No documented/sample contract artefact.** The fakes are hand-authored; nothing in the test or repo ties them to an AWS/Google sample response or API reference. Condition 4 requires validation *against the documented/sample contract*; here the fake *is* the contract.
2. **Request construction is not asserted.** `Bucket` is accepted and discarded by the fake (`FakeS3Client.put_object` stores by `Key` only); no test asserts the configured bucket, endpoint, region or credentials reach the client. The credential/endpoint → `boto3.client(...)` construction is `pragma: no cover` (`s3.py:52-62`) and untested; the same for Drive (`drive.py:54-62`). The authoritative progression lists "request construction" and "authentication/signing" as stages; neither is verified.
3. **Drive substitutes more than the provider.** `googleapiclient.http.MediaIoBaseUpload/MediaIoBaseDownload` are monkeypatched out (`test_m23_drive_driver.py:95-102`), so the upload/download media path of the production adapter is replaced, not exercised. Condition 3 fails for Drive.

Position: D3 for both adapters. This is the strongest non-qualifying candidate in the repository; the gap to D4 is narrow for S3 (a fixture derived from the S3 API reference plus request assertions) and wider for Drive. The absence of an application writer is a separate (D5) matter and was **not** used to reject D4 — adapter contract verification and application integration were kept distinct as instructed.

### C.2 Config resolver (row 44) — **D4 JUSTIFIED** (component level)

- Production implementation: `app/services/config_resolver.py` `ConfigResolver` (request-scoped; real `ConfigRepository` + `AuditRepository`). Condition 1.
- Contract clearly defined: campaign > tenant > platform > default; a present row with NULL value wins over lower levels; cache keyed on scope+key not default; `invalidate(key|None)`; optional resolution audit; `resolve_with_source` returns the winning level. Documented in the module docstring (`:1-13,38-44`) and `docs/92_planning/_plan_S46_M28_config_resolver.md:4-7`; traced to BR-18 in V4 Part 3. Condition 2.
- Tests exercise the production class against the real test database with no mocks: `tests/unit/test_config_resolver.py` (22 tests: precedence ×3, scope-only ×2, missing-key/default ×2, NULL-row-wins, source reporting ×2, repo lookups ×2, cache ×5, `resolve_with_source` ×2, audit ×3) and `tests/integration/test_config_resolver_acceptance.py` (full precedence + audit; source levels distinct). Conditions 3, 4, 5.
- Assertions establish the contract (which level wins, what source is reported, what is audited), not merely that code ran. Condition 6.
- No external provider is involved, so "documented/sample provider responses" reduces to the documented behavioural contract above; that is the correct reading for an internal component.

Not integrated: `grep -rn config_resolver app --include=*.py` finds no importer outside the module. That blocks D5 (LIVE INTEGRATED), not D4. V5's "UNABLE TO VERIFY (as integrated)" is resolved as: **D4 as a component; not integrated (D5 not reached)**.

### C.3 WhatsApp (row 45) — split audit

| Sub-capability | Production code | Tests | Verdict |
|---|---|---|---|
| Outbound sending | `_send` returns `f"wamid_{hash}"` (`whatsapp_service.py:143-150`); no Graph API client anywhere | `test_s34d_whatsapp_outbound.py` exercises policy/persistence around the stub | **D4 NOT JUSTIFIED**; level D2 (stub returning fake IDs; capability not implemented) |
| Outbound governance / scheduling / persistence | `send_outbound`, `_enforce_send_policy`, `_service_window_open`, `enqueue_scheduled`, `dispatch_due` | real DB tests | D3 (implemented); no external contract ⇒ D4 not applicable |
| Signature verification | `_validate_whatsapp_hmac` (`routes/webhooks.py:53-63`): `X-Hub-Signature-256` = `sha256=` + HMAC-SHA256(app secret, raw body), constant-time compare — the scheme Meta documents | `test_s34c_whatsapp_webhook.py:91-104`: valid, wrong, missing signature through the real route | **D4 JUSTIFIED** for the documented signature contract. Secret is a process-wide env value with `dev-secret` default (CD-05), not tenant-configurable — a configuration-maturity gap (blocks D5), not a contract gap |
| Inbound webhook handling (POST) | `_extract_whatsapp_message` parses `entry[].changes[].value.metadata.display_phone_number` + `messages[0].{from,id,text.body}`; always-200 to Meta; unknown number ignored; status-only ignored; invalid JSON 422 | `test_s34c_whatsapp_webhook.py:25-54` payload is Meta's documented webhook structure (`object`, `entry`, `changes[].field="messages"`, `messaging_product`, `metadata`, `messages[]`, `statuses[]`); six tests run the production route end-to-end into the real DB and assert stored thread/message | **D4 JUSTIFIED** for the POST message-event contract |
| Webhook registration handshake (GET `hub.mode`/`hub.verify_token`/`hub.challenge`) | **absent** — `grep -rn "hub.mode\|hub.verify\|hub.challenge" app tests` → nothing | — | Not implemented. Meta cannot register the endpoint without it. Recorded as an evidence fact for V6/EV-03; it caps the inbound sub-capability at D4 and is a hard blocker for D5 |
| Provider adapter (Graph send) | absent; `_send` seam only | — | D2 (seam) |
| Runtime / live integration | no artefact | — | not D5 (Section D) |

Row 45 result: D2 (outbound send) / D3 (outbound governance) / **D4 (inbound POST + signature)** / D2 (adapter). V4's "inbound D4" is therefore **confirmed** under the authoritative scale for the POST contract; V5's lowering of it to D3 rested on the "not live" reading that the brief corrects.

### C.4 SIEM export (row 7) — **D4 NOT JUSTIFIED**

`siem_service.py` implements HMAC-SHA256 signing (`sign_payload/verify_signature`) and an `export` that batches events and posts via `_post` (`httpx.post`, `pragma: no cover`). Tests (`tests/unit/test_m04_forensics.py:254-269`) patch `_post` and assert status handling. The signing contract is TalkProof-defined (no external receiver specification in the repo), so condition 2 has no documented external counterpart, and request construction/transport is untested. D3.

### C.5 AI provider calls and transcription (rows 14, 15) — **D4 NOT JUSTIFIED**

`orchestrator_service.py` makes real `anthropic`, `openai` (chat + whisper) and `genai` SDK calls with env keys and literal model names. `tests/unit/test_orchestrator_service.py:158-277` replace the SDK modules with `MagicMock` objects; response fixtures are MagicMock attribute chains, not documented sample responses; no test asserts the request payload sent to any SDK; the `json.loads(raw)` parse path (CD-16) is exercised only on test-authored strings. Real calls existing in production code establish D3 and nothing more (as the brief states). D3 both rows; EV-01 unchanged.

### C.6 Campaign carrier / Exotel (rows 22, 23) — **D4 NOT JUSTIFIED**

`exotel_service.py:46-68` builds the documented `/v1/Accounts/{sid}/Calls/connect` request with basic auth and form fields, but `tests/unit/test_exotel_service.py:29-43` patch the entire `httpx` module, assert nothing about URL/payload/auth, and use a one-key stub response. The inbound Exotel webhook's `X-Exotel-Signature` HMAC scheme is an assumption (EV-02). CD-01 breaks the production wiring. Row 22 D2, row 23 D2 (B).

### C.7 Inbound calling + polymorphic pipeline (row 46) — **D4 NOT JUSTIFIED**

`test_i02_pipeline_acceptance.py` verifies pipeline logic over a stubbed carrier; no external contract fixture; recording key never written. D3.

### C.8 Flutter app and admin portal (rows 31, 33) — **D4 NOT JUSTIFIED**

Flutter tests use `MockClient`; admin Vitest mocks hooks; Playwright/integration_test not run. These are unit/mock tests of clients against TalkProof's own API, with no provider contract to verify. D3 both.

### C.9 Blockchain anchor (row 18) — **D4 NOT JUSTIFIED**

Submit function unrunnable (undeclared `iota_client`, deprecated API, `pragma: no cover`), stub id path only. D2.

### C.10 Audit chain, auth, RBAC, guardrails, GDPR (rows 3, 5, 6, 13, 37) — not D4 candidates

Internal capabilities with no external contract; tested on production code against the real DB. They are D3 by definition (IMPLEMENTED). D4 was not awarded because the brief's D4 is "contract verified" against a *relevant documented/sample contract*; none exists for these beyond the code's own schemas. (Row 44 differs in that BR-18 and the S46 plan state the resolver's contract independently of the code.)

### C.11 SCIM (row 4, SCIM part) — **D4 NOT JUSTIFIED**

Implements POST/GET/PATCH `/Users` and returns the `urn:ietf:params:scim:schemas:core:2.0:User` schema (`scim_service.py:75`). Tests (`test_m02_auth.py:348-402`) send flat JSON and a non-RFC `{"active": false}` PATCH body (RFC 7644 uses `Operations[]`), assert only `userName`/`active`; no ListResponse, filter, error schema or `ServiceProviderConfig`. Contract compatibility with RFC 7643/7644 is not established. D3.

### C.12 Summary

| Candidate | Classification |
|---|---|
| Config resolver (row 44) | **D4 JUSTIFIED** (component; not integrated) |
| WhatsApp inbound POST + signature (row 45, sub-capability) | **D4 JUSTIFIED** (POST contract; GET handshake absent) |
| S3 driver (rows 24/43) | D4 NOT JUSTIFIED — narrow gap |
| Drive driver (rows 24/43) | D4 NOT JUSTIFIED |
| SIEM (7), AI calls (14), transcription (15), Exotel (22/23), pipeline (46), Flutter (31), admin (33), IOTA (18), SCIM (4), WhatsApp outbound (45) | D4 NOT JUSTIFIED |
| INSUFFICIENT EVIDENCE | none — every candidate was decidable from repository evidence |

---

## D. D5 / D6 / D7 evidence audit

Searched: `docs/09_test_results` (one file: `TEST_RESULTS_TEMPLATE.md`, a blank template), `docs/15_deployment/DEPLOYMENT.md`, `docs/40_operations/*`, `deploy/` (`staging.env` only — a template with CHANGE_ME values, telephony "leave blank / mock"), `.github/workflows/ci.yml` (runs lint + pytest against a CI Postgres; no provider credentials, no deployment step), `docs/92_planning/session_history`, `SPRINT_TRACKER.md`/`TRACEABILITY.md` (tracker claims only), `tests/api` (Playwright API, 64 skipped without live server), `tests/manual/*.md` (manual test notes from April 2026 — procedural, not run records with captured provider traffic), admin `tests/e2e` (no `playwright-report`/`test-results` directory), Flutter `integration_test` (no run artefact).

| Level | Evidence found | Result |
|---|---|---|
| D5 LIVE INTEGRATED | No recorded live call to Anthropic/OpenAI/Gemini/Whisper, Exotel, Meta, S3, Drive, IOTA, Stripe or any SSO IdP. `deploy/staging.env` is a template; `docker-compose.prod.yml` is configuration. | **None supported.** Runtime evidence required and unavailable in all three repositories. |
| D6 PRODUCT E2E VERIFIED | No end-to-end run artefact; admin Playwright and Flutter integration_test not run; backend `tests/api` skipped. | **None supported.** |
| D7 PRODUCTION READY | No deployment record, no exercised runbook (`backup.sh` absent), no monitoring evidence. | **None supported.** |

Configuration files, code comments, tracker "DONE" entries and mocked tests were not treated as live-integration evidence. Rows 44 and 45-inbound stop at D4 for exactly this reason.

---

## E. Changed-row register

`Row | V5/gate-review D | authoritative D | delta | exact reason`

| Row | V5 / gate-review D | Authoritative D | Delta | Exact reason |
|---|---|---|---|---|
| 32 Flutter mobile native | D1 | D2 | +1 (raised) | `BiometricAuthenticator`/`NativeCallBridge` abstract interfaces with Fake/Noop implementations exist in `lib/src/mobile/`; under the authoritative scale a designed interface is D2 regardless of whether a native target exists yet. Gate review had flagged this row scale-sensitive. |
| 44 Config resolver | D3, UNABLE TO VERIFY (as integrated) | D4 (component); not integrated | +1 (raised); UNABLE resolved | Six D4 conditions met on production code against real DB with no mocks (C.2). Non-integration is a D5 question and no longer prevents determining the level. |
| 45 WhatsApp (inbound sub-capability only) | D3 (inbound) | D4 (inbound POST + signature) | +1 on secondary value; primary D2 unchanged | Production route tested end-to-end with Meta's documented payload shape and documented signature scheme, including error cases (C.3). Registration handshake absent — caps at D4. |
| 45 WhatsApp (split refinement) | D2 (outbound) / D3 (inbound) | D2 (outbound send) / D3 (outbound governance) / D4 (inbound) / D2 (adapter) | split only | Task 3 required separation of sending, inbound handling, signature verification, adapter and runtime. |

Lowered rows: **none.** Rows 1–31, 33–43, 46: unchanged (reassessed, Section B). Row 36 stays at the R-36 value.

---

## F. Corrected D-level distribution

Counting the primary (first) value of split rows, V5 convention:

| Level | Gate-corrected (V5 + R-36) | Authoritative | Movement |
|---|---|---|---|
| D1 | 4 (17, 20, 24, 32) | **3** (17, 20, 24) | −1 |
| D2 | 19 | **20** | +1 (32) |
| D3 | 23 | **22** | −1 (44) |
| D4 | 0 | **1** (44) | +1 |
| D5 | 0 | 0 | — |
| D6 | 0 | 0 | — |
| D7 | 0 | 0 | — |
| **Total** | 46 | **46** | |

Secondary D4 values: row 45 (inbound). Secondary D3 values unchanged elsewhere.

| Category | Rows |
|---|---|
| Unchanged | 43 rows (all except 32, 44, 45) |
| Raised | 2 primary (32, 44) + 1 secondary (45 inbound) |
| Lowered | 0 |
| Split (new or refined) | 1 (45) |
| Unable to determine | 1 (row 41, custom-domain part beyond D3 — unchanged); row 44's "unable" is resolved |

Disposition tally against the V4 tracker column (V5 Part 38 "Disp." semantics): row 32 V4 D2 → auth. D2 = CONFIRMED (was LOWERED); row 44 V4 D4 → auth. D4 = CONFIRMED (was UNABLE); row 45 V4 "D3 (inbound D4)" → outbound D2 LOWERED / inbound D4 CONFIRMED, row disposition stays LOWERED on its primary value. New tally: **25 confirmed / 20 lowered / 0 raised / 1 unable to verify.** ("Raised" here means raised above the V4 tracker claim; nothing exceeds what V4 claimed.)

---

## G. Impact on V5 / V5 Gate Review

| Item | Changes? | Exact impact |
|---|---|---|
| Corrected tally 23 confirmed / 21 lowered / 0 raised / 2 unable | **Yes** | Becomes 25 / 20 / 0 / 1 (Section F). |
| "No D4 survives" conclusion (V5 Part 38 and Part 43; gate review §1 totals) | **Yes** | Two V4 D4 claims survive under the authoritative scale: row 44 (Config resolver, component level) and row 45's inbound secondary value. The other seven V4 D4 removals (rows 4, 7, 24/43, 31, 33, 46) stand. |
| Part 38 | **Yes** | Rows 32, 44, 45 values and dispositions; the row-count/tally sentence; the "No V4 D4 survives" sentence; the distribution line. R-SCALE's "provisional" label is replaced by "authoritative D1–D7 (reconciled 2026-10-04 21:35)" on every row. |
| Part 41 (proof-chain table) | **No D-level change.** | No proof-chain stage moves (hash, TSA, anchor, PDF, portal are unchanged). The R-SCALE label on Part 41 is replaced as above. Gate review §4 additions (EV-01 on transcription stage; approver not in hash) still apply. |
| Part 43 (D4 audit) | **Yes** | The sentence "Zero D4+ survives" and the per-row lowering reasons for 44 and 45 are superseded by Section C; the prohibited-bases paragraph is unaffected and is strengthened (D4 here was awarded on contract evidence, not on any prohibited basis). The three Part 12 checks are unaffected. |
| Part 45 (EV items) | **Yes, narrowly** | EV-03 gains the fact that the Meta GET verification handshake is absent (required before any live inbound test); EV-08 ("definitions not supplied; may move D2↔D3 only") is **closed** by this artifact — the movement was D1→D2 (32) and D3→D4 (44, 45-inbound), so EV-08's "D2↔D3 only" prediction was wrong, as the gate review §2 anticipated. EV-01/02/04/05/06/07 unchanged (EV-07 at its R-EV7 wording). |
| Part 46 (PO decision evidence) | **Yes, labels only** | Any D-level quoted in the decision pack for rows 32, 44, 45 must show the Section B value; the "provisional" qualifier is dropped everywhere. No decision option changes; D-01..D-26 remain unapproved; D-26 remains open per R-D26. |
| Gate review §2 blocker ("final D-level certification BLOCKED pending definitions") | **Resolved** | Subject to the independent review of this artifact that the brief schedules next. |
| Gate review §1 per-row ACCEPT verdicts | **Unchanged for 43 rows** | Rows 32 (ACCEPT of D1), 44 (ACCEPT of D3/UNABLE) and 45 (ACCEPT of D3 inbound) were accepted *under the E-01 scale*, which §2 explicitly made provisional; no code fact in those rows is contradicted. |

None of these sections is rewritten here.

---

## H. Exact V6 delta instructions

V6 = V5 + the five accepted gate corrections + the following, and nothing else:

1. **Scale.** Replace the "D-scale used for reconciliation" paragraph (V5 line 10) with the authoritative D1–D7 names and the interpretation in Section A.2 of this artifact. Remove every "provisional (E-01 working scale…)" label introduced by R-SCALE and replace it with "authoritative D1–D7 (reconciled `TALKPROOF_DSCALE_RECONCILIATION_V001_20261004_2135.md`)".
2. **Part 38 row 32** (Flutter mobile native): V5 D `D1` → `D2`; Disp. `LOWERED` → `CONFIRMED`; add evidence `lib/src/mobile/biometric_gate.dart`, `lib/src/mobile/call_controller.dart` (abstract interfaces + Fake/Noop); keep "no plugins, no iOS" in the code column; EV-05 unchanged.
3. **Part 38 Config resolver row** (V5 #44 → V4-order #45 after R-44/45): V5 D `D3` → `D4 (component; not integrated — D5 not reached)`; Disp. `UNABLE TO VERIFY (as integrated; code D3)` → `CONFIRMED`; evidence `services/config_resolver.py`, `tests/unit/test_config_resolver.py`, `tests/integration/test_config_resolver_acceptance.py`, `docs/92_planning/_plan_S46_M28_config_resolver.md`; keep the CD-08 "no production caller" fact.
4. **Part 38 WhatsApp row** (V5 #45 → V4-order #44 after R-44/45): V5 D → `D2 (outbound send) / D3 (outbound governance, scheduling, persistence) / D4 (inbound webhook POST + signature verification) / D2 (provider adapter)`; Disp. stays `LOWERED` (primary); add the evidence fact "Meta GET verification handshake (`hub.verify_token`) absent" to the code column; EV-03 retained.
5. **Part 38 tally and distribution lines.** Disposition tally → `CONFIRMED 25 · LOWERED 20 · RAISED 0 · UNABLE TO VERIFY 1`; distribution → `D1 × 3 · D2 × 20 · D3 × 22 · D4 × 1 · D5–D7 × 0`; replace "No V4 D4 survives" with "Two V4 D4 claims survive (Config resolver, component level; WhatsApp inbound secondary value); seven do not".
6. **Part 43.** Replace "Zero D4+ survives" with the Section C.12 summary; add the three S3-driver gaps (C.1) as the reason row 43 remains D3; keep the prohibited-bases paragraph and the Part 12 checks verbatim.
7. **Part 45.** EV-03: append "GET verification handshake absent — must exist before any live inbound test". EV-08: mark CLOSED by this artifact, with the note that actual movement was D1→D2 and D3→D4, not D2↔D3.
8. **Part 46.** Update the quoted D-levels for the three rows; drop "provisional"; no other change.
9. **Part 47 (delta ledger).** Add one entry per item 1–8 citing this artifact. Note the row-number swap from R-44/45 in the same entry as items 3 and 4.
10. **Do not** add any new CD entry, requirement, FR/NFR ID, sprint, or decision. The handshake absence and the S3 `_client()` construction being untested are evidence facts recorded in the code column / Part 43 only.

---

## I. Remaining external-verification dependencies

| ID | Dependency | Max D until satisfied | Status after this artifact |
|---|---|---|---|
| EV-01 | Live AI/Whisper responses (rows 14, 15) | D3 | Open; D4 requires contract fixtures first (C.5) |
| EV-02 | Exotel API behaviour, real signature header, recording URL (rows 22, 23, 46) | D3 / D2 | Open; CD-01 fix precedes any live test |
| EV-03 | Meta WhatsApp live inbound + Graph send (row 45) | D4 inbound / D2 outbound | Open; **GET verification handshake must be implemented before a live inbound test is possible** |
| EV-04 | Staging/deployment logs (RLS, Tier B, SIEM, storage) | D3 (D4 for config resolver component) | Open |
| EV-05 | Admin Playwright + Flutter integration_test on a live stack (rows 31, 32, 33) | D3 | Open |
| EV-06 | Tracker quotation revalidation | n/a | Open (document evidence) |
| EV-07 | DR restore test record (row 36) | D2 | Open (R-EV7 wording) |
| EV-08 | Authoritative D1–D7 definitions | — | **Closed** by this artifact (subject to its independent review) |

No D5, D6 or D7 can be awarded to any row until the relevant EV item carries a recorded run artefact in a repository.

---

## J. Final gate verdict

**D-SCALE RECONCILED — READY FOR V6**

D-level changes V6 must incorporate **in addition to** the five accepted V5-gate corrections (R-36, R-44/45, R-D26, R-EV7, R-SCALE):

1. Row 32 Flutter mobile native: **D1 → D2**, disposition LOWERED → CONFIRMED.
2. Config resolver row (V5 #44 / V4-order #45): **D3 → D4 (component; not integrated)**, disposition UNABLE TO VERIFY → CONFIRMED.
3. WhatsApp row (V5 #45 / V4-order #44): inbound secondary value **D3 → D4**; split refined to outbound send D2 / outbound governance D3 / inbound D4 / adapter D2; primary D2 and LOWERED disposition unchanged; handshake-absent fact recorded.
4. Tally **25 / 20 / 0 / 1**; distribution **D1 3 · D2 20 · D3 22 · D4 1 · D5–D7 0**; "no D4 survives" replaced per Section G.
5. EV-08 closed; EV-03 narrowed per Section H item 7.

All other 43 rows: unchanged under the authoritative scale. No row lowered. No D5/D6/D7 awarded. V6 is **not** created by this artifact; the next operation is the independent review of this reconciliation.

Summary line: 46 rows reassessed / 43 unchanged / 2 primary raised (32, 44) / 1 secondary raised (45 inbound) / 0 lowered / 1 split refined / D4 candidates audited 13: 2 justified, 11 not justified, 0 insufficient / D5–D7: no evidence in any repository / V5, gate review, code unchanged / V6 not created.
