# TalkProof — Authoritative Requirement & Sprint Recovery
**Session:** 2026-10-04 · **Role:** Product Owner / Architect / Requirements Engineer / Governance review · **Status:** PROPOSAL — NOTHING APPLIED. Awaiting Senthil's approval (Phase 7 gate).
**Intended location once approved:** `docs/92_planning/REQUIREMENT_RECOVERY_20261004.md`

Evidence labels used throughout: `[SOURCE]` (attached document, section cited) · `[INFERENCE]` (my conclusion from sources) · `[RESEARCH REQUIRED]` (needs fresh external research; not asserted as fact) · `[USER REQUIREMENT — THIS SESSION]` (the 2026-10-04 brief).

Sources read in full: `SPRINT_TRACKER.md` (2,043 lines), `TRACEABILITY.md`, `PRD.md` v1.0.1, `FRD.md` v1.0.1 (FR-001..082), `NFRD.md` v1.0.0 (NFR-001..067), `ARCHITECTURE.md` v1.1, `TELECOM_PROVIDER_POLICY.md`, `talkproof_competitors.md` (June 2026). **Not attached, referenced by sources:** BRD-001, `APRIL_PILOT_PROJECT_STATUS_20260420.md`, `DR_RUNBOOK.md`, `SOC2_CONTROL_MAP.md`, `DEPLOYMENT.md`, `_plan_S45_M27_pipeline_configurability.md`, `_plan_reslice_microsprints_S46plus.md`. Statements about them are `[SOURCE]` only to the extent the attached docs describe them.

---

## A. Executive finding

1. **The product definition is intact and broad.** PRD §1.2 defines three pillars (Certified Core, RTC Suite, SaaS Platform) with 21 modules; the tracker has grown that to 40 modules (M00–M40) without any formally approved reduction. `[SOURCE: PRD §1.2, §5; TRACEABILITY §1 BR-01..BR-19]` Nothing in the sources authorises shrinking it.

2. **"DONE" in S01–S23 means "application code + mocked tests", not product completion.** The tracker itself says so: "Spot-reads found DONE to mean happy-path code exists and self-tests pass" `[SOURCE: TRACKER S24 context note, line 994]`, and every S01–S23 completion note ends with a "Carried-forward … at deployment" clause deferring the live provider, the real transport, or the UI. By the D1–D7 scale in this brief, S01–S23 are mostly **D3** (implemented), a few **D2**, none **D6/D7**. Detail in §C/§D.

3. **The provider layer is where the requirement was misunderstood.** June built *isolation seams* (`_invoke_model`, `_dial`, `_stripe()`, `_send`, `_dispatch`, `_mint_sfu_token`, `_place`) that return deterministic fake IDs and called that "BYO-key by design". `[SOURCE: TRACKER S08/S13/S09/S34/S16/S15/S43 completion notes]` The brief's Requirement 3 says the opposite: the adapter must be written against the published API; only credentials and live execution are deferred. **Ironically, the April pilot (A03/A04) contains the only real provider adapters in the codebase** — Exotel, OpenAI/Anthropic/Gemini calls, Whisper, IOTA, Google Sheets — but hardcoded and reading `os.environ` `[SOURCE: TRACKER S45 evidence table]`. So TalkProof has two AI paths: a real-but-hardcoded April one and a governed-but-stubbed June one (M07/M22). They are not joined. This is the single most important structural gap.

4. **The planned S46–S51 pipeline work is the right spine, but as written it will reproduce the stub pattern** (e.g. S43's Twilio adapter is "sandbox-stubbed `_place`"). S47–S51 need the adapter standard applied before they close, and S51 (certification) conflicts with FR-054/NFR-023/NFR-024 by treating RFC3161 as an *alternative* to blockchain instead of a *required layer alongside* it.

5. **The competitor model is missing the category that already defeated the June plan once.** TalkProof's own history is the evidence: 22 modules / 122 tickets generated in ~16 hours (16–17 Jun) `[SOURCE: TRACKER index rows S01–S23, "AI-burst"]`. Any buyer with Claude Code can do what WET did. Defensibility must move to what AI cannot generate quickly: operated evidence corpus, carrier/regulatory onboarding, verification trust, independent-verifier ecosystem, compliance attestations, and configuration depth.

6. **Requirement IDs are not traced.** FR-001..082 and NFR-001..067 appear nowhere in the tracker or traceability matrix; both trace BR→US→ticket→test only `[SOURCE: TRACEABILITY §2–§5]`. Critical Requirement 10 (sprint rows carry requirement IDs) cannot be met until that mapping exists.

7. **Recommended path (one position):** keep S47 open and in sequence; add two docs-only governance sprints (completion levels + provider-adapter standard) immediately after S47 closes and before S48 starts, because S48–S51 will otherwise close at the wrong bar; then run the existing S48–S58 sequence under the new bar; then S60+ recovery sprints as laid out in §K. No history rewritten; every historical DONE stays as recorded with a separately dated recovery level.

---

## B. What the original product actually requires (authority map — Phase 1)

### B.1 Authority hierarchy as the sources present it
| Rank | Document | Status | Date | Notes |
|---|---|---|---|---|
| 0 | BRD-001 | referenced only | — | Not attached. PRD/FRD/NFRD cite it as parent. `[SOURCE: PRD header]` Treat PRD as top attached authority (decision §M-17). |
| 1 | PRD-001 v1.0.1 | Approved for Development | 2026-06-16 | Vision, 3 pillars, personas, journeys, epics E-01..E-16, MoSCoW, phases. |
| 2 | FRD-001 v1.0.1 | Approved | 2026-06-16 | FR-001..FR-082, modules M00–M21. |
| 3 | NFRD-001 v1.0.0 | Approved | 2026-06-16 | NFR-001..NFR-067. |
| 4 | ARCH-001 v1.1 | Baseline (stack-corrected) | 2026-06 | C4, pipeline, ADR-001..010. Contains code-reality details that PRD/FRD do not (Exotel primary, IOTA primary). |
| 5 | TELECOM_PROVIDER_POLICY | Active | S43 (2026-06-28) | Module-level policy; consistent with code. |
| 6 | SPRINT_TRACKER | live audit record | last 2026-06-29 | Canonical status source `[SOURCE: TRACEABILITY footers]`. |
| 7 | TRACEABILITY | live | last 2026-06-29 | BR/US/RT/ticket/test; §4/§5 "intentionally NOT extended" after S23 `[SOURCE: TRACEABILITY footer 2026-06-26]`. |
| 8 | talkproof_competitors | report | June 2026 | 85+ vendors, 7 categories, no AI-builder category. |

### B.2 Core requirement set (what must be true for TalkProof to be "the product")
| # | Requirement | Source | Tracker representation | Traceability | Contradiction / gap |
|---|---|---|---|---|---|
| R1 | Three pillars: Certified Core, RTC Suite, SaaS Platform | PRD §1.2 | M11/M06/M07/M12 · M12–M15 · M00–M10,M19–M21 | BR-02, BR-03, BR-01/06/07/08/10 | None — intact. |
| R2 | Human agent calls; **three independent AI models** verify; **HiL-signed** certificate; **tamper-proof blockchain-anchored PDF**; client-deliverable | PRD §1.1, §1.3 P1/P2; FR-040, FR-053, FR-054, FR-055; ARCH ADR-006/007/008 | S12 M11-T04..T07 | BR-02, BR-04 | FR-040 requires ≥2 distinct providers + all 3 respond; S48 M30-T05 proposes degrade to 2-of-2 → **conflict (§M-6)**. |
| R3 | Verdict vocabulary `confirmed/disputed/uncertain/insufficient` (FR-040) | FRD | Code uses `POSITIVE/NEGATIVE/NEUTRAL/INCONCLUSIVE` + `HUMAN_REVIEW` `[SOURCE: TRACKER S44-B, S45]` | — | Vocabulary mismatch; S44 genericised prompt but kept outcome labels. |
| R4 | Certification = canonical hash **+ RFC3161 from accredited TSA + blockchain anchor**, PDF with QR, S3 Object Lock | FR-054; NFR-023; NFR-024; NFR-045 | S12: `content_hash` + `issued_at` + optional `anchor_tx_id`; "external blockchain/RFC3161 anchoring populates at deployment via BYO provider" | — | **RFC3161 never implemented.** S51 M33-T04 frames RFC3161 as a "2nd adapter to prove abstraction" — contradicts FR-054 which needs both (§M-4). Blockchain named Hedera/Ethereum (FR/NFR) vs IOTA primary (ARCH §7, ADR-007, code) (§M-3). |
| R5 | HiL gate ordering | FR-054 "On HiL approval, the backend produces…"; ARCH §10 pipeline anchors + generates PDF **then** HiL gate | S12: draft → request_issue (HiL) → issue | — | ARCH and FRD disagree on whether anchoring precedes approval (§M-5). Matters for the evidence chain (what the TSA timestamps). |
| R6 | Transcription: BYO STT, **speaker-diarised**, word-level confidence, ≤2× realtime | FR-052 | S12 M11-T03 "already shipped operationally" = April whisper-1 literal | — | Diarisation / word-confidence not evidenced anywhere. S47 M29-T04 adds Google STT but not diarisation. |
| R7 | Telephony abstraction Twilio/Telnyx/Vonage + BYO; dual-channel recording; CallKit/ConnectionService dialer | FR-056, FR-057, FR-058, FR-073; PRD §9.1 | S13 (`_dial` stub), S43 (`_place` stub), S19 (NativeCallBridge abstraction, bindings deferred) | BR-03, BR-07, BR-16 | FRD does not list Exotel; ARCH/code make Exotel primary. Dual-channel recording not evidenced. Real Twilio/Telnyx/Vonage adapters absent. |
| R8 | Chat realtime WebSocket + presence; voice notes/media; E2E DMs | FR-059..061 | S14: models + REST; "WebSocket gateway … wire at deployment" | BR-03 | **Realtime transport not built**; app S30 polls REST. |
| R9 | Meetings via LiveKit + egress recording + live transcription + AI summary | FR-062..064 | S15: `_mint_sfu_token` stub; S30-C "media-plane SDK-deferred" | BR-03 | Media plane absent in app and backend. |
| R10 | Push FCM/APNs/WebPush + email | FR-065 | S16 `_dispatch` stub | BR-03 | No real push/email adapter. |
| R11 | BYO keys: KMS envelope, test-connection, router, fallback, metering, spend caps | FR-028..031, FR-079, NFR-020/022 | S06 Fernet (not KMS), `_probe` stub, router real; S23 platform keys | BR-07 | KMS adapter absent (Fernet derived from JWT secret in dev). Test-connection not real. |
| R12 | Billing: Stripe checkout/webhooks/dunning, metering, tiers | FR-041..043 | S09 `_stripe()` stub; webhook HMAC real | BR-08/10 | Stripe API adapter absent. |
| R13 | Multi-tenant Tier A/B/C | FR-005..010 | S02: Tier A RLS, Tier B schema, Tier C manifest; migration/routing "applied by deploy pipeline" | BR-06 | Tier B/C are D2/D3 only. |
| R14 | Identity: RS256 JWT (FRD/NFRD) | FR-012, NFR-014 | ARCH §7 HS256; S03 built HS256 | BR-08 | **Conflict (§M-2).** |
| R15 | Lockout 5 fails → 30 min (FR-011/NFR-017); impersonation ≤ 2 h (FR-045) | FRD/NFRD | S03: 15 min / 423; S10: 1–60 min, default 15 | — | Numeric drift (§M-9). |
| R16 | Audit: hash-chain, access_trail, auth_events, SIEM, WORM, GeoIP | FR-022..027, NFR-034..037 | S05 real; GeoIP coarse; WORM "provisioned by deploy" | BR-05 | Minor; hash formula differs between FR-022 and ARCH §10 (ip in ARCH, not FRD). |
| R17 | Observability: OTel tracing, Prometheus, SLOs, circuit breakers on all external calls | FR-074/075, NFR-046..049 | S20 primitives built, "adopted incrementally"; OTel/PagerDuty "at deployment" | BR-08 | Circuit breakers not wrapped around provider calls (NFR-046 unmet). |
| R18 | DR: RPO ≤15 min, RTO ≤4 h | NFR-042/043 | S20 runbook RPO 15m/RTO 60m; ARCH §15 RPO 1h/RTO 4–8h | — | Three different values (§M-8). |
| R19 | Coverage ≥80% backend (NFR-057, PRD §8.2) | NFRD/PRD | Tracker gate 100%; actual 99.3–99.5% `[SOURCE: S24, S31-E]` | BR-11 | Gate overstated; decision on official bar (§M-10). |
| R20 | Provider-neutral, config-selected, no hardcoding | ARCH AP-04; BR-16, BR-18 (added June) | S43 ✓(selection), S46 ✓(resolver), S47–S51 TODO | BR-18 | PRD/FRD have **no FR** for provider selection UI, capability discovery, health, fallback by provider, rotation (Req 4). |
| R21 | Won't-have: AI voice agents | PRD §6 Won't Have | — | — | Competitor doc treats as adjacent threat; brief Req 8 says evaluate by capability (§M-7). |
| R22 | Module M17 | PRD/FRD: Flutter **desktop** target (FR-070/071) | Tracker/Traceability RT-18: M17 = **React admin portal** | — | **Identity conflict (§M-1).** PRD maps admin portal to M09/M10/M04/M21 (Epic E-15). |
| R23 | Modules M22–M40 | not in PRD/FRD/NFRD | tracker + BR-11..BR-19 | — | 19 modules exist only in tracker/traceability; BR-14/15/16/17/18/19 have no FR rows. |
| R24 | Repo layout | ARCH §6 shows April app (`voter_list_screen.dart`), `voter.py`, `exotel_service.py`, `/api/v1/voters`, `/polls/{id}/certify` | S29 rebuilt app; S44 renamed voters→contacts, polls→certifications; S26 standalone repos | — | ARCH §6/§5 stale after S26/S29/S44. |
| R25 | Tracker header "22 modules · 122 tickets" | TRACKER line 6 | 40 modules, ~230 tickets | — | Stale header (cosmetic; do not rewrite history, add note). |

---

## C. Requirements misunderstood during previous development (Phase 2 — historical DONE semantics)

Scale: D1 specified · D2 designed · D3 implemented · D4 contract-verified · D5 live-integrated · D6 product-E2E · D7 production-ready. **Historical ☑ DONE is untouched; this is the recovery level as of the sources.**

| Sprint | Module | Historical status | What DONE actually meant (from the completion note) | Recovery level | Class |
|---|---|---|---|---|---|
| S01 | M00 | ☑ | CI + compose; minio not in compose; design system deferred | D3 | impl, not live |
| S02 | M01 | ☑ | Tier A RLS real; Tier B schema create only; Tier C manifest builder; data migration/provisioning "by deploy pipeline" | A: D3 · B: D3 · C: D2 | impl partial |
| S03 | M02 | ☑ | argon2/JWT/MFA real; OIDC/SAML "exercised in staging… unit-tested via stubs"; SCIM; HIBP fail-open | D3/D4 | impl; live unclear |
| S04 | M03 | ☑ | RBAC real; multi-role per user deferred | D3 | genuine (code) |
| S05 | M04 | ☑ | chain/trail/events real; GeoIP coarse; WORM by deploy | D3 | genuine (code) |
| S06 | M05 | ☑ | Fernet (derived key), `_probe` stub, router real; KMS "in prod" | D3 (router) · D2 (KMS, test-conn) | seam only |
| S07 | M06 | ☑ | state machine/SoD/provenance real; escalation delivery deferred | D3 | genuine (code) |
| S08 | M07 | ☑ | `_invoke_model()` sandbox stub returns neutral envelope conf 0.0 | D3 (envelope) · **D1/D2 (provider)** | **mock only** |
| S09 | M08 | ☑ | `_stripe()` stub; webhook HMAC real | D3 · D2 (Stripe) | seam only |
| S10 | M09 | ☑ | real cross-tenant service | D3 | genuine (code) |
| S11 | M10 | ☑ | real; IP-allowlist enforcement + webhook delivery deferred | D3 | impl partial |
| S12 | M11 | ☑ | consensus + hash cert + HiL issuance real; RFC3161/blockchain "at deployment"; console UI deferred | D3 · **D1 (TSA)** · D3 (IOTA via April) | impl partial |
| S13 | M12 | ☑ | `_dial`/`_provision_number` stubs; webhooks + S3 upload deferred | D3 (app) · D2 (carrier) | seam only |
| S14 | M13 | ☑ | models/REST real; **WebSocket gateway deferred** | D3 (REST) · D2 (realtime) | impl partial |
| S15 | M14 | ☑ | `_mint_sfu_token` stub; egress/STT deferred | D3 · D2 (LiveKit) | seam only |
| S16 | M15 | ☑ | `_dispatch` stub | D3 · D2 (push/email) | seam only |
| S17 | M16 | ☑ | 14 Dart files; SDK not in sandbox; superseded by S29/S30 rebuild on standalone | D2/D3 → superseded | superseded |
| S18 | M17 | ☑ | 8 Vitest; superseded by S28 | D3 → superseded | superseded |
| S19 | M18 | ☑ | abstractions only; native plugin bindings deferred | D2 | design only |
| S20 | M19 | ☑ | primitives built; "adopted incrementally"; OTel/PagerDuty at deployment | D3 (primitives) · D2 (wiring) | impl partial |
| S21 | M20 | ☑ | consent/GDPR/headers real; KMS rotation by deploy; DNC registry not evidenced | D3 · D2 (KMS, DNC) | impl partial |
| S22 | M21 | ☑ | branding + static packaging payload + ROI | D3 | genuine (code) |
| S23 | M22 | ☑ | ledger real; records neutral stub rows | D3 | genuine (code) |
| S24–S27, S37, S38, S40–S42, Q04–Q07 | quality/docs/tooling | ☑ | genuinely complete for their scope | n/a | genuine |
| S28–S36 | frontend | ☑ | functional+negative 100% **against typed mocks**; live Playwright/device runs "deferred to deploy" | D3/D4 | not D6 |
| S31, S59 | inbound + polymorphic pipeline | ☑ | real logic; Exotel inbound webhook HMAC real | D3/D4 | genuine (code) |
| S33 | M23 storage | ☑ | real Drive v3 + boto3 drivers behind `_client()` seam, tested with fake clients | **D4** | best-practice example |
| S34 | M24 WhatsApp | ☑ | `_send` stub (deterministic wamid); inbound webhook Meta signature real | D3 · D2 (Graph API send) | seam only |
| S43 | M25 carrier | ☑ | interface + resolver real; Twilio `_place` **stub** | D3 · D2 (Twilio) | seam only |
| S44 | M26 | ☑ | genuine refactor | D3 | genuine |
| S46 | M28 | ☑ | genuine | D3 | genuine |
| S47 | M29 | ◐ T01 only | interface only | D2 | open sprint |

**The misunderstanding, stated plainly** `[INFERENCE from the pattern above]`: "BYO key" was read as "the provider can be omitted because the customer supplies credentials later". The brief corrects this: BYO means *credentials are parameters*; the adapter is still the vendor's obligation. Only S33 (storage) got this right.

---

## D. Provider / stub implementation mismatch (against Requirement 3's 18-point adapter checklist)

| Provider (Req 2 list) | Where | Interface | Real adapter from spec | Runtime creds via vault | Auth/signing | Response parsing | Webhook | Error map | Retry/CB | Idempotency | Metering | Contract tests | Negative tests | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Exotel (campaign) | April `exotel_service.py`, S43 | ✓ | ✓ (real API, creds default "") | ✗ (`os.environ`/settings) | ✓ | ✓ | ✓ HMAC (S31-D) | partial | ✗ | ✓ idem key | ✗ (deferred to webhook) | ✗ | partial | **D3, keys wrong** |
| Twilio (campaign) | S43 | ✓ | ✗ stub `_place` | ✓ (router) | ✗ | ✗ | ✗ | ✗ | ✗ | – | ✗ | ✗ | ✗ | **stub** |
| Twilio/Telnyx/Vonage (M12) | S13 | ✓ | ✗ `_dial` stub | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | – | ✓ charge | ✗ | ✗ | **stub** |
| Telnyx/Vonage (campaign) | policy §3 | ✓ | ✗ "adapter pending" | – | – | – | – | – | – | – | – | – | – | **absent** |
| OpenAI/Anthropic/Gemini (pipeline) | April orchestrator | ✗ (S48 TODO) | ✓ real calls, model strings literal | ✗ `os.environ` (S49 TODO) | ✓ | ✓ | n/a | partial | partial (HUMAN_REVIEW on error) | – | ✓ per-token cost | ✗ | partial | **D3 hardcoded** |
| OpenAI/Anthropic/Gemini (M07 governed) | S08 | ✓ | ✗ `_invoke_model` stub | ✓ via vault | ✗ | ✗ | n/a | ✗ | ✗ | – | ✓ ledger | ✗ | ✗ | **stub — disconnected from April path** |
| Whisper STT | April | ✗ (S47 TODO) | ✓ real | ✗ env | ✓ | ✓ | n/a | partial | ✗ | – | partial | ✗ | ✗ | D3 hardcoded, no diarisation |
| Google STT / Deepgram / AssemblyAI | S47 M29-T04 | planned | – | – | – | – | – | – | – | – | – | – | – | **planned; must be real** |
| TTS | — | — | — | — | — | — | — | — | — | — | — | — | — | not required by PRD unless disclosure playback (FR-058) is TTS — `[INFERENCE]` |
| S3 / MinIO | S33 | ✓ | ✓ boto3 | config | ✓ | ✓ | n/a | ✓ 404 map | ✗ | ✓ | ✗ | ✓ fake client | ✓ | **D4 — model answer** |
| Google Drive | S33 | ✓ | ✓ Drive v3 | SA creds | ✓ | ✓ | n/a | ✓ | ✗ | ✓ | ✗ | ✓ | ✓ | **D4** |
| Google Sheets output | April | ✗ (S45 T08) | ✓ gspread | env | ✓ | ✓ | n/a | ✗ | ✗ | – | – | ✗ | ✗ | D3 hardcoded |
| Stripe | S09 | ✓ | ✗ `_stripe()` stub | ✓ | webhook sig ✓ | ✗ | ✓ | partial | ✗ | ✓ | n/a | ✗ | partial | **stub** |
| WhatsApp (Meta Graph) | S34 | ✓ | ✗ `_send` stub | ✓ | inbound sig ✓ | ✗ | ✓ | ✗ | ✗ | ✓ | ✓ charge | ✗ | partial | **stub (outbound)** |
| Telegram | S56 | planned | – | planned vault | – | – | planned | – | – | – | – | – | – | **planned; must be real** |
| Email (SMTP/SES) | S16 | ✓ | ✗ `_dispatch` stub | ✓ | ✗ | ✗ | n/a | ✗ | ✗ | – | – | ✗ | ✗ | **stub** |
| Push (FCM/APNs/WebPush) | S16, S19 | ✓ | ✗ stub + Flutter bindings deferred | ✓ | ✗ | ✗ | n/a | ✗ | ✗ | – | – | ✗ | ✗ | **stub** |
| LiveKit | S15, S30 | ✓ | ✗ `_mint_sfu_token` stub; no server SDK; no Flutter SDK | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | – | – | ✗ | ✗ | **stub** |
| IOTA | April `iota_service.py` | ✗ (S51 TODO) | ✓ real + `iota_stub_tx_id` fallback setting `[SOURCE: S01 note]` | ✗ env | ✓ | ✓ | n/a | "failure-no-block" | ✗ | – | – | ✗ | partial | D3 hardcoded |
| RFC3161 TSA | — | ✗ | **✗ none** | – | – | – | – | – | – | – | – | – | – | **absent (FR-054/NFR-024 MH)** |
| Hedera / Ethereum | — | ✗ | ✗ none | – | – | – | – | – | – | – | – | – | – | **absent (FR-054/NFR-023 MH)** |
| KMS (AWS/GCP/Vault) | S06/S21 | ✗ | ✗ Fernet only | – | – | – | – | – | – | – | – | – | – | **absent (FR-079 MH)** |
| OIDC / SAML IdP | S03 | ✓ | ✓ code; token exchange + xmlsec "via stubs" | config | ✓ | ✓ | n/a | partial | ✗ | – | – | partial | partial | D3/D4 |
| SIEM webhook | S05 | ✓ | ✓ HMAC | config | ✓ | ✓ | n/a | ✓ | retry? | ✓ delivery-id | – | ✓ | partial | D4 |
| HIBP | S03 | ✓ | ✓ k-anonymity | none | ✓ | ✓ | n/a | fail-open | – | – | – | ✓ | ✓ | D4 |
| Blockchain "BYO" at Tier C | FR-008 | ✗ | ✗ | – | – | – | – | – | – | – | – | – | – | D1 |

**Pattern** `[INFERENCE]`: 13 of 24 provider integrations are isolation seams with no provider code behind them; 6 are real but hardcoded April code; 5 are real-and-correct (S33 storage, SIEM, HIBP, Exotel webhook, Stripe/Meta inbound signature verification). The storage sprint (S33) is the template every provider sprint should follow, extended with retries, circuit breaker, metering, and spec-derived contract fixtures.

---

## E. Existing AI usage inside TalkProof

| Where | What | Real or stub | Source |
|---|---|---|---|
| Orchestrator `_ai_verify` | 3-model transcript-vs-script verification (Claude/GPT-4o/Gemini), `VERIFICATION_PROMPT` (genericised S44-B), per-token cost | **Real, hardcoded** | TRACKER S45 table; S44-B |
| `_majority_vote` / `compute_consensus` | 2-of-3 majority, agreement ratio, INCONCLUSIVE/HUMAN_REVIEW | deterministic | S12 T04, S57 |
| M07 `GovernedAIService.analyze()` | advisory envelope, confidence threshold 0.70, cache 60 min | **Stub provider** | S08 |
| M07 guardrails | PII redaction (regex email/phone/ssn/cc), injection detection | deterministic (FR-038 asks for NER/presidio — not evidenced) | S08 |
| M14 `summarize` | post-meeting summary via M07 | stub | S15 |
| M22 ledger | every AI call recorded (in/out/tokens/cost/latency) | real | S23 |
| M21 ROI calculator / competitor matrix | static payload, arithmetic | deterministic | S22 |
| S58 cost model | 3×AI "audit tax" rationale | docs only | S58 |
| **Build process** | S01–S23 generated by AI in ~16 h; S24+ by "Senthil+Claude" | process, not product | TRACKER index Owner/Repo |

**No AI is used today for**: onboarding, campaign/policy/disclosure creation, config validation, provider diagnostics, review prioritisation, anomaly/fraud detection, QA scoring beyond the certification verdict, root-cause, test generation, security review, observability, support, documentation, reporting. Everything in §F is new.

---

## F. Missing / future AI usage (Requirement 6) — each with problem · why AI · human control · evidence · failure risk · fallback

Priority order reflects proximity to the proof chain (the product's core). All advisory under FR-037 (never mutates state without HiL).

| ID | Capability | Problem | Why AI > rules | Human control | Evidence/audit | Failure risk | Fallback |
|---|---|---|---|---|---|---|---|
| AI-01 | **Policy → required/prohibited statement extraction** | Campaign managers type free-text scripts; verification needs structured must-say / must-not-say / must-do lists (Req 7) | Statements are paraphrased in speech; rules on exact text miss legitimate variants | Manager approves the extracted policy version before campaign activation | Policy version + extraction model/prompt recorded (FR-091/092 proposed) | Over-/under-extraction | Manual policy authoring (today's path) |
| AI-02 | **Transcript-vs-policy verification with evidence citations** (formalises today's 3-model check) | FR-040 asks for `evidence: [string]` per model; today's prompt outputs outcome labels | Semantic equivalence judgement | HiL approval (FR-053) | AIReview rows + ledger + prompt version | Hallucinated citations | Citation must quote a transcript span; non-matching citation → `uncertain` |
| AI-03 | **Human-review prioritisation** | Reviewer queue is FIFO; SLA 4 h (FR-035) | Rank by disagreement, confidence spread, risk words | Reviewer sees ranking reason; can reorder | Ranking stored on proposal | Mis-ranking delays a bad call | SLA escalation unchanged |
| AI-04 | **Anomaly / fraud flags** (agent reads script to voicemail, duplicate audio, silence ratio, speaker mismatch) | No detection today | Pattern recognition across calls | Flags only; HiL decides | Flag + features recorded | False positives | None required (advisory) |
| AI-05 | **AI QA scoring beyond certification** (tone, script adherence %, compliance phrases) | Competes with Observe.AI/CallMiner (competitor Cat 1/2) | Standard LLM task | Tenant enables per campaign | Ledger | Score drift between model versions | Pin model version per campaign (NFR-073 proposed) |
| AI-06 | **Configuration validation & provider diagnostics** (Req 4) | Tenant admin misconfigures carrier/keys; errors surface at call time | Explain provider error payloads, suggest fixes | Admin applies | Diagnostic recorded | Wrong advice | Deterministic test-connection (FR-029) remains the gate |
| AI-07 | **Onboarding assistant** (tenant setup, first campaign, disclosure template per jurisdiction) | PRD P-01 pain: manual onboarding | Generative drafting | Admin approves every artefact | Audit | Jurisdictional errors | Static templates |
| AI-08 | **Provider API change detection + migration suggestion** | Adapters rot (Twilio/Meta/OpenAI change APIs) | Diff official OpenAPI/changelog, propose adapter patch | Engineer approves PR | CI record | Missed change | Contract tests fail loudly (NFR-071 proposed) |
| AI-09 | **Test generation / regression analysis** for adapters & pipeline | 18-point checklist × 24 providers is large | Generate contract fixtures from docs; triage failures | Engineer | CI | Fixture drift | Hand-written fixtures |
| AI-10 | **Incident / root-cause assistant** over logs, traces, ledger, chain | M19 observability exists only as primitives | Correlate multi-service traces | Ops | Incident record | Confident wrong RCA | Manual runbook (DR_RUNBOOK) |
| AI-11 | **Customer-visible health & explainability** ("why was this call not certified?") | PRD P-07 pain: cannot trust record | Natural-language explanation from structured evidence | Read-only | Generated from ledger; never alters evidence | Mis-explanation | Show raw evidence |
| AI-12 | **Security review** (SAST triage, dependency CVE triage per NFR-026/028) | NFR-060 48 h patch SLA | Triage volume | Engineer | CI | — | Tooling only |
| AI-13 | **Cost optimisation** (provider/model selection by language/cost per S58) | S58 identifies 3×AI tax | Recommend roster per campaign | Admin selects | Config audit (S46) | Degraded accuracy | Platform default roster |
| AI-14 | **Reporting** (per-campaign certification report narrative) | FR-082 sales enablement; client reports | Summarisation | Reviewer approves | — | — | Tabular report |

Not proposed: autonomous AI callers (PRD Won't-Have; see §M-7).

---

## G. Competitive model gap — especially AI software builders (Phase 4)

### G.1 What the existing document covers `[SOURCE: competitors §1–§7]`
Seven categories, 85+ vendors, five "owned" gaps, pricing tiers. Category 6 ("AI Voice Agents") is the only AI-substitution category and it covers *AI replacing the agent*, not *AI replacing the vendor*.

### G.2 The missing category D — "build-it-yourself with AI coding agents"
**Evidence from TalkProof's own history** `[SOURCE: TRACKER]`:
- S01–S23: 22 modules, 122 tickets, 1,281 tests, ~16 h (16-Jun 13:52 → 17-Jun 05:53), Owner "AI-burst".
- April pilot A01–A04: real Exotel + 3-AI verification + IOTA + PDF + Flutter APK in ~5 days.
- S28–S36 (six frontend sprints, 8 admin screens + full Flutter app): ~5 calendar days, "Senthil+Claude".
- S44 (4 table-rename migrations, 16 commits): ~5 h.

**What that implies** `[INFERENCE]`:
| Question (Req 5) | Answer | Label |
|---|---|---|
| % of TalkProof reproducible today with AI coding agents | The **D3 code surface: ~80–90%** (tenancy, auth, RBAC, audit chain, HiL, billing scaffolding, chat/meetings models, dialer, single-LLM review, PDF, hash + anchor via a timestamping API). What is *not* quickly reproducible is **D5–D7**: live carrier onboarding (DLT/KYC "days-to-weeks" `[SOURCE: TELECOM_POLICY §4]`), SOC2 Type I needs 6 months evidence `[SOURCE: PRD §9.3]`, accredited TSA contracts, app-store review, an operated evidence archive, and the legal track record of certificates surviving challenge. | INFERENCE |
| Time/cost compression | Months → days for code; the June build is the datapoint. Live-integration and compliance timelines are **unchanged** by AI. | INFERENCE |
| Commodity features | Everything in Pillar 3 (SaaS platform) and most of Pillar 2 (RTC via LiveKit/Twilio/WhatsApp APIs). | INFERENCE |
| Copied quickly | Single-model verification, hash + OriginStamp/Woleet anchor, PDF certificate, client portal. | INFERENCE |
| Hard to reproduce | Multi-model consensus **calibration data** (thousands of reviewed calls), independent verifier ecosystem, neutral-third-party trust (the certificate is worth more when the issuer is not the campaign operator), carrier/regulatory onboarding per jurisdiction, HiL governance maturity, retained evidence with legal retention (NFR-035), white-label reseller network. | INFERENCE |
| Defensibility when code is cheap | Shifts from code to: (1) operated trust + evidence corpus, (2) configuration/extensibility depth (any provider, any policy, any jurisdiction without code), (3) integration surface (API-first, webhooks), (4) compliance attestations, (5) switching cost of archived evidence and verifiers in customers' hands. | INFERENCE |
| Does configuration/extensibility matter more? | Yes — it is the direct counter to "I'll just build it": a buyer's build is one configuration; TalkProof must be *every* configuration. | INFERENCE |
| How TalkProof uses AI internally to stay ahead | AI-08/09/10/12 in §F plus continuous AI-assisted adapter generation; the product must absorb provider churn faster than a self-builder can. | INFERENCE |

### G.3 Competitor matrix v2 (additive; dimensions from Req 9)
Rows = vendor categories A (direct), B (platform), C (AI-native substitutes for the human work), D (AI builders: Claude Code, Codex/ChatGPT, Cursor, Replit, Lovable, open-source call-centre stacks + CPaaS + LLM APIs — **names are `[RESEARCH REQUIRED]` for current capability/pricing**). Columns:

direct feature competition · platform competition · AI-agent substitution · AI-builder substitution · implementation time · implementation cost · customisability · provider neutrality · multi-tenancy · evidence ownership · original-evidence preservation · cryptographic integrity · independent verification · multi-model verification · human governance · policy conformance · auditability · compliance · explainability · self-diagnostics · observability · self-healing · extensibility · API-first · white-label · customer configuration · switching cost · data/network advantage · defensibility in an AI-cheap-code world.

Cells for categories A–C can be filled from the existing document for: pricing, compliance certs, tamper-proof, audit trail, multi-tenant/reseller `[SOURCE: master table]`. Everything else, and all of category D, is `[RESEARCH REQUIRED]`. The research must be **desk research only** (vendor docs, pricing pages, public repos) — no outreach, consistent with Senthil's stated working preference.

### G.4 Specific `[RESEARCH REQUIRED]` items
1. Current (Oct 2026) AI coding-agent capability benchmarks for full-stack SaaS generation; representative cost per module.
2. Open-source call-centre / compliance-recording stacks that a self-builder would start from.
3. Whether any vendor now offers multi-model consensus verification (the June doc said none; four months have passed).
4. AgentMint / LeadCompliant current state.
5. eIDAS/qualified-timestamp providers with APIs (Universign named in doc) — needed for S65.
6. Hedera Consensus Service / IOTA current fees and SDK status.
7. AI voice-agent vendors' certification features (Retell/Vapi/Bland) — do any now offer tamper-evident records?

---

## H. Evidence / proof-chain gaps (Requirement 7)

Reconciliation of the brief's binding list against FR-054 (canonicalised certificate = call metadata + transcript + consensus + approver + timestamp), NFR-023/024/030/045, S12 (`content_hash`, `issued_at`, `anchor_tx_id`, `verify_certificate`), S23 (ledger), S46 (config-resolution audit), TELECOM_POLICY §5 (carrier evidence parity).

| Element | In FR-054 today | In code (S12/S23/S31/S59) | Gap | Keep/Add/Remove |
|---|---|---|---|---|
| interaction ID, tenant, campaign | ✓ metadata | ✓ | — | Keep |
| participants (agent, contact — pseudonymised) | ✓ | ✓ | — | Keep |
| provider + provider call/session ID | implied | `telecom_call_sid` ✓ | not in canonical payload | **Add** to manifest |
| timestamps (initiation, connect, end) | ✓ | partial | — | Keep |
| consent evidence (NFR-030e: linked for retention) | ✗ in cert | ConsentRecord exists (S21) | **not bound** to certificate | **Add** |
| original recording + hash | ✗ hash | recording key only | **recording hash not in cert** | **Add** |
| transcript + hash + STT provider/version | transcript ✓; hash ✗; provider ✗ | Transcript row has `engine` (S47-A) | **Add** hash + engine/version |
| applicable policy/script/disclosure + version + required/prohibited statements/actions | script text ✓; version ✗; structured lists ✗ | Campaign.disclosure_script | **Add** policy versioning (FR-091 proposed) |
| each AI review + model/provider/version + prompt/policy version | consensus ✓; per-model ✓ (AIReview rows); versions ✗ | ledger has model/provider; prompt version ✗ | **Add** prompt/model version pin |
| consensus/voting result + strategy | ✓ | ✓ (S50 adds strategy) | strategy id not recorded | **Add** |
| human review/approval (who/when/IP/reason) | ✓ approver | ✓ decision_provenance | — | Keep |
| business outcome | partial | CallOutcome ✓ | — | Keep |
| evidence root hash (Merkle over the above) | single content_hash | ✓ single | no tree → cannot verify one artefact without all | **Add** root + leaf hashes (lets a client verify the PDF without the audio) |
| trusted timestamp (RFC3161) | ✓ required | **✗ absent** | **MH requirement unmet** | Build (S65) |
| external anchor (blockchain) | ✓ required | IOTA real (April), optional in S12 | provider-neutral + Hedera/Ethereum | Build (S51/S65) |
| certificate (PDF, QR, embedded tokens) | ✓ | pdf_service (April) | TSA token + anchor tx not embedded | Amend |
| later independent verification | ✓ portal in-browser hash | `verify_certificate` API | no offline verifier CLI; `openssl ts -verify` (NFR-024) impossible without TSA | Build (S71) |
| **Additions the brief did not list** `[INFERENCE]` | — | — | config resolution audit (S46) already records *which* provider/level produced each setting — bind the resolved provider config snapshot into the manifest; carrier evidence parity (policy §5); source_call_type (inbound vs campaign, S59) | **Add** |
| **Removals** | none justified | | | |

**Ordering decision needed (§M-5):** the TSA must timestamp the root hash *after* HiL approval if the approval is part of the evidence (FRD view), or *before* if the certificate is the thing being approved (ARCH view). Recommendation: two timestamps — evidence root (pre-approval, proves what the reviewer saw) and certificate (post-approval, proves issuance). `[INFERENCE]`

---

## I. Existing sprints that already cover discovered gaps (do not duplicate)

| Gap | Covered by | Clarification needed |
|---|---|---|
| Config resolver platform→tenant→campaign | S46 ✓ DONE | none |
| Transcription abstraction, 2nd engine, per-language | S47 (open) | T04 must be a **real** adapter; add diarisation + word confidence (FR-052) as T06 or note in S64 |
| AI reviewer adapters, roster, per-language, vendor-down | S48 | T02 must call real APIs via vault (depends S49); T05 conflicts with FR-040 (§M-6); must **replace** the M07 `_invoke_model` stub (one AI gateway) — add ticket |
| Keys → vault, remove `os.environ` | S49 | aligns with Req 2; add IOTA/Google SA (T02 already) |
| Voting strategies | S50 | record strategy id in evidence manifest (ties to S70) |
| Certification provider abstraction | S51 | **re-scope**: TSA is not an alternative provider; certification = hash → TSA → anchor; T04 becomes "RFC3161 real client" and a new T06 "Hedera adapter" |
| Carrier abstraction + 2nd adapter | S43 ✓ | Twilio `_place` is a stub → real adapter in S63 |
| Campaign metering at completion webhook | S43 honest seam, policy §6 | goes into S63 |
| Storage abstraction | S33 ✓ | live D5 run in S68 |
| WhatsApp outbound real send | S34 stub | S66 |
| Telegram | S56 | write real Bot API adapter (spec public); vault token |
| Consensus dedup | S57 | none |
| Cost model | S58 | add "build-vs-buy" line referencing §G |
| Multi-repo coordination + CROSS_TEAM_CONTRACT.md | S39 ◐ | execute; the contract file is also the provider-contract registry's home |
| Route coverage, edit-tool lesson, shell note | Q01–Q03 | none |
| Pipeline configurability E2E + `PIPELINE_CONFIGURABILITY.md` | S45 close | add D-level + adapter-standard conformance to the close gate |
| Inbound parity | S31/S59 ✓ | none |
| `LANGUAGE_AI_COMPATIBILITY.md` | named gap in policy §7 | fold into S48 T04 deliverable |

---

## J. Genuine new requirement gaps (not in any existing sprint)

| # | Gap | Source of requirement | Proposed FR/NFR |
|---|---|---|---|
| J1 | Completion levels D1–D7 as acceptance; recovery-level annex for S01–S23 | `[USER REQUIREMENT — THIS SESSION]` Req 1 | NFR-068 |
| J2 | Provider adapter standard (18-point) + contract-fixture discipline + registry | Req 3 | FR-083, FR-084, NFR-069, NFR-070 |
| J3 | Provider configuration **through the product**: platform default, tenant override, campaign override, encrypted creds UI, validation, capability discovery, fallback, health, usage/cost, runtime switch, rotation | Req 4; PRD J-03 partially (BYO keys) | FR-085, FR-086, FR-087 |
| J4 | Real adapters for: Twilio/Telnyx/Vonage, OpenAI/Anthropic/Gemini (governed path), Whisper/Google/Deepgram, Stripe, Meta Graph, Telegram, SMTP/SES, FCM/APNs/WebPush, LiveKit server, RFC3161 TSA, Hedera/Ethereum, KMS | Req 2/3; FR-028..031, FR-042, FR-054, FR-056, FR-062..065, FR-079 | existing FRs; D-level targets |
| J5 | Evidence package manifest (Merkle root, leaf hashes, bindings in §H) | Req 7; NFR-023/024/030/045 | FR-088, FR-089 |
| J6 | Policy/script versioning with required/prohibited statements/actions | Req 7 | FR-091 |
| J7 | AI model/provider/version + prompt version pinning and recording | Req 7 | FR-092, NFR-073 |
| J8 | Independent verifier (offline CLI + public endpoint + schema versioning) | FR-055 extension; NFR-024 | FR-090 |
| J9 | Realtime WebSocket gateway (FR-060 is specified but unbuilt — implementation gap, not a new FR) | FR-060 | — (sprint S72) |
| J10 | LiveKit media plane in Flutter + egress | FR-062/063 | — (sprint S73) |
| J11 | Native mobile bindings + store builds | FR-072/073 | — (sprint S74) |
| J12 | Circuit-breaker/retry wrapped around every provider call; OTel traces; SLO dashboards | NFR-046/048/049 | — (sprint S75) |
| J13 | KMS envelope encryption adapter + rotation; RS256 decision; IP allowlist enforcement | FR-079, NFR-022, NFR-014 | — (sprint S76) |
| J14 | AI inside TalkProof wave 1 (AI-01..04) and ops wave (AI-06, 08, 09, 10, 11) | Req 6 | FR-094..100 |
| J15 | Competitor framework v2 incl. category D, build-vs-buy model, research list | Req 5/9 | FR-082 amendment; new doc |
| J16 | Product E2E (D6) verification runbook + live staging E2E runs (the deferred Playwright/device suites) | Q07 precedent | NFR-068 |
| J17 | FR/NFR ↔ ticket traceability | Req 10 | TRACEABILITY §6 |
| J18 | FR rows for BR-14..BR-19 (WhatsApp, storage, carrier, vocabulary, pipeline config, Telegram) — currently BR with no FR | FRD gap | FR-101..106 |
| J19 | Document amendments (PRD/FRD/NFRD/ARCH/competitors) — version 1.1.0 | Phase 5 | — (sprint S81) |

---

## K. Proposed future sprint structure (Phase 6)

**Rules applied:** existing numbers untouched · S47 remains the open sprint · new sprints start at **S60** (S59 is the last used; the Q-series note reserves S43–S66, so S60 is next-free `[SOURCE: TRACKER Q-series header]`) · each substantial sprint gets `docs/92_planning/sprints/Sxx_<name>.md` · tracker rows carry: ID, title, objective, requirement IDs, dependencies, D-level target, acceptance gate, status, spec path.

### K.1 Sequence
```
S47 (open) → [S60, S61: governance docs — see §M-12] → S48 → S49 → S50 → S51 (re-scoped) → S45 close
→ S56 → S57 → S58 → S39 execute → Q01–Q03
→ S62 … S81 (below)
```

### K.2 New sprints
| ID | Title | Objective | Req IDs | Depends | D-target | Acceptance gate | Spec |
|---|---|---|---|---|---|---|---|
| S60 | G01 Completion-Level Standard + Recovery Annex | Define D1–D7; add `D-level` column to tracker index for S24+ (historical ☑ untouched); append a dated "Recovery level (2026-10)" annex table for S01–S59 (the §C table); add FR/NFR columns to traceability | NFR-068, J1, J17 | — | n/a (docs) | both files updated; no historical row text changed; encoding clean | `S60_completion_levels.md` |
| S61 | PV01 Provider Adapter Standard & Registry | `PROVIDER_ADAPTER_STANDARD.md` (18-point checklist, fixture rules, seam rules); provider registry with capability descriptors; conformance test harness; grandfather S33 as reference | FR-083, FR-084, NFR-069/070 | S60 | D3 | harness runs S33 drivers green; every S47+ adapter ticket references the standard | `S61_provider_adapter_standard.md` |
| S62 | PV02 LLM Gateway Unification | One AI gateway: S48 adapters become the real `_invoke_model`; M07/M22/orchestrator share it; real OpenAI/Anthropic/Gemini adapters from official APIs; model-version pinning | FR-037/040, FR-092, NFR-073 | S48, S49, S61 | D4 | contract fixtures from each vendor's documented response schema; negative tests (429/5xx/timeouts); ledger rows populated with real token fields | `S62_llm_gateway.md` |
| S63 | PV03 Telephony Real Adapters | Twilio Voice (campaign + M12), Exotel via vault, Telnyx, Vonage: initiate, status callbacks, recording fetch, dual-channel flag, completion-webhook metering (policy §6) | FR-056/057/058, BR-16 | S43, S49, S61 | D4 | per-carrier contract fixtures; evidence parity (policy §5) test; metering at completion | `S63_telephony_adapters.md` |
| S64 | PV04 STT Real Adapters + Diarisation | Whisper (API), Google STT, Deepgram/AssemblyAI; speaker diarisation; word-level confidence; per-language select | FR-052, S47 | S47, S61 | D4 | TranscriptionResult carries segments + confidences; ≤2× realtime test | `S64_stt_adapters.md` |
| S65 | PV05 Certification Layers | RFC3161 real client (DER request/response, `openssl ts -verify` passes), IOTA via vault, Hedera adapter, Ethereum optional; composite certification hash→TSA→anchor; failure-no-block preserved with explicit `partial` state | FR-054, FR-089, NFR-023/024 | S51, S49, S61 | D4 | TSA token verifies offline; anchor tx recorded; both embedded in PDF | `S65_certification_layers.md` |
| S66 | PV06 Messaging & Notification Adapters | Meta Graph send (templates, media), Telegram Bot API (aligns S56), SMTP/SES email, FCM/APNs/WebPush | FR-065, BR-14/19 | S56, S61 | D4 | contract fixtures; delivery status mapping | `S66_messaging_adapters.md` |
| S67 | PV07 Stripe Real Adapter | Customers, checkout sessions, subscriptions, metered usage records, invoices, dunning events | FR-041..043 | S61 | D4 | fixtures from Stripe docs; webhook replay tests | `S67_stripe_adapter.md` |
| S68 | PV08 Media & Storage Live | LiveKit server SDK token mint + egress; S3/Drive live D5 run; recording upload path end-to-end | FR-058/062/063, BR-15 | S33, S61 | D5 | live creds in staging; one real recording lands in configured backend | `S68_media_storage_live.md` |
| S69 | CFG01 Provider Configuration Through Product | Admin UI + API: provider selection per capability (platform/tenant/campaign), encrypted creds, test-connection (real), capability discovery, fallback chain, health, usage/cost, runtime switch, rotation | FR-085/086/087, FR-029, Req 4 | S46, S61, S62–S67 | D6 | admin configures a tenant to Twilio + Deepgram + Hedera with no code change; audit of resolution (S46) visible | `S69_provider_config_ui.md` |
| S70 | EV01 Evidence Package Manifest | Manifest schema, leaf hashes (recording, transcript, policy, each AI review, consensus, approval), Merkle root, provider/config snapshot, consent binding, policy versioning | FR-088/089/091, NFR-030 | S65, S50 | D4 | manifest reproducible; any single artefact verifiable against root | `S70_evidence_manifest.md` |
| S71 | EV02 Independent Verifier | Offline CLI + public verification endpoint + schema versioning; PDF embeds TSA token, anchor tx, root; portal verify uses the same library | FR-090, FR-055 | S70 | D6 | third party verifies a certificate with no TalkProof account | `S71_independent_verifier.md` |
| S72 | RT01 Realtime Gateway | WebSocket server + Redis pub/sub; presence deltas; Flutter `web_socket_channel` client; reconnect | FR-060, FR-066, NFR-003/009 | S14 | D6 | P95 < 500 ms in staging | `S72_realtime_gateway.md` |
| S73 | RT02 LiveKit Media Plane (Flutter) | `livekit_client` join/publish/subscribe, grid/speaker, screen share (desktop), recording badge | FR-062/063/071 | S68 | D6 | two participants exchange media in staging | `S73_livekit_media_flutter.md` |
| S74 | RT03 Native Mobile Bindings & Store Builds | CallKit/ConnectionService, `firebase_messaging`, `local_auth`, background presence, TestFlight/Play internal | FR-072/073, FR-065 | S66, S72 | D6 | push delivered; call appears natively | `S74_native_mobile.md` |
| S75 | OPS01 Observability & Resilience Wiring | Wrap every adapter call in retry/circuit-breaker/bulkhead; OTel traces across pipeline; Prometheus scrape; SLO dashboards; provider health feed for S69 | FR-075, NFR-046/048/049 | S61+ | D5 | chaos test per provider trips breaker; trace spans pipeline end-to-end | `S75_observability_wiring.md` |
| S76 | SEC01 KMS, Key Rotation, Auth Decisions | KMS adapter (AWS KMS / Vault), per-tenant DEK, rotation; RS256 (if §M-2 approves); IP allowlist enforcement middleware; impersonation/lockout numbers aligned | FR-079, FR-012, NFR-014/022, FR-045, FR-011 | S61 | D4 | rotation without downtime test | `S76_kms_auth.md` |
| S77 | AI01 AI in the Proof Chain | AI-01 policy extraction, AI-02 citation-grade verification, AI-03 review prioritisation, AI-04 anomaly flags — all advisory, HiL-gated | FR-094..097 | S62, S70 | D4 | citations resolve to transcript spans; prioritisation reason stored | `S77_ai_proof_chain.md` |
| S78 | AI02 AI Operations | AI-06 config validation, AI-08 provider API change detection, AI-09 test generation, AI-10 RCA assistant, AI-11 customer explainability | FR-098..100 | S69, S75 | D4 | change-detection flags a seeded spec diff | `S78_ai_operations.md` |
| S79 | CMP01 Competitor Framework v2 | Additive matrix (§G.3), category D, build-vs-buy model, research list executed by desk research; feed M21 packaging payload | FR-082 amendment | — | n/a | matrix with every cell labelled SOURCE/INFERENCE/RESEARCH REQUIRED | `S79_competitor_v2.md` |
| S80 | E2E01 Product E2E Verification (D6) | Staging runbook; execute the deferred live Playwright + device integration_test suites; per-pillar journey J-02/J-04 end-to-end | NFR-068, Q07 | S62–S74 | D6 | J-02 runs agent→call→transcript→3 AI→HiL→TSA+anchor→PDF→portal verify with real providers | `S80_product_e2e.md` |
| S81 | DOC01 Requirement Document Amendments | Apply approved §N changes: PRD/FRD/NFRD 1.1.0, ARCH 1.2, competitors v2, TELECOM policy update | all | §M approvals | n/a | version history rows added; nothing deleted | `S81_doc_amendments.md` |

**Cross-check against §I:** no new sprint duplicates S46–S58. S62 absorbs the "unify two AI paths" gap that S48 alone would leave open; S65 corrects S51's framing rather than replacing it.

---

## L. Documents that should eventually be amended (nothing applied)

| Document | Amendment type |
|---|---|
| PRD-001 → v1.1.0 | add §1.4 "AI-era positioning"; add Epics E-17 Evidence Package & Verification, E-18 Provider Adapters & Configuration, E-19 AI Inside TalkProof; extend module map M22–M40; resolve M17 (§M-1); decision on Won't-Have AI agents (§M-7); add D-levels to §7 gates |
| FRD-001 → v1.1.0 | FR-083..FR-106 (§J); amend FR-040 (verdict vocab, failure rule per §M-6), FR-052 (diarisation evidence), FR-054 (manifest + both TSA and anchor + ordering per §M-5), FR-056 (add Exotel), FR-012 (per §M-2), FR-011/045 numbers (per §M-9) |
| NFRD-001 → v1.1.0 | NFR-068..073; reconcile NFR-042/043 (§M-8); NFR-057 bar (§M-10); NFR-023 provider list (§M-3) |
| ARCH-001 → v1.2 | new §18 Provider Adapter Architecture (interface → adapter → config → vault → provider); §6 repo layout to standalone repos + post-S44 names; §5 route list (contacts/certifications); §7 JWT; §10 pipeline ordering; ADR-011 adapter standard, ADR-012 evidence manifest, ADR-013 AI gateway unification |
| talkproof_competitors → v2 | additive §8 "AI software builders & build-vs-buy"; matrix v2 appendix; research list |
| TELECOM_PROVIDER_POLICY | adapter status column → D-level; S63 reference |
| SPRINT_TRACKER | D-level column (S24+ only), recovery annex, S60–S81 rows, header note "40 modules as of 2026-10 (header totals historical)"; S17/S19 annotation "superseded by S29/S30/S32/S36" (annotation, not rewrite) |
| TRACEABILITY | §6 FR/NFR ↔ ticket map; BR-20 (completion/adapter governance), BR-21 (evidence package), BR-22 (AI inside), BR-23 (AI-builder competition); RT-60..RT-81 |
| New | `COMPLETION_LEVELS.md`, `PROVIDER_ADAPTER_STANDARD.md`, `EVIDENCE_PACKAGE_SPEC.md`, `LANGUAGE_AI_COMPATIBILITY.md`, `docs/92_planning/sprints/S60..S81_*.md` |

---

## M. Contradictions / questions requiring Senthil's decision

| # | Question | Sources in conflict | My recommendation |
|---|---|---|---|
| M-1 | M17 = Flutter desktop (PRD/FRD) or React admin portal (tracker/traceability)? | FR-070/071 vs RT-18 | Keep tracker (code reality); amend PRD/FRD: M17 = admin portal, desktop target becomes part of M16 (FR-070/071 re-homed). |
| M-2 | JWT RS256 (FRD/NFRD) or HS256 (ARCH/code)? | FR-012, NFR-014 vs ARCH §7, S03 | RS256 — multi-surface + Tier C verification without shared secret; schedule in S76. |
| M-3 | Primary anchor: IOTA (ARCH/code) or Hedera/Ethereum (PRD/FRD/NFRD)? | ADR-007 vs FR-054/NFR-023 | Provider-neutral: IOTA default (exists), Hedera second adapter (S65); amend FR/NFR to list all three. |
| M-4 | Is RFC3161 mandatory alongside the anchor (FR-054) or an alternative (S51)? | FR-054/NFR-024 vs S51 M33-T04 | Mandatory alongside. Re-scope S51 per §I. |
| M-5 | Evidence timestamp before or after HiL approval? | FR-054 vs ARCH §10 | Both: evidence-root timestamp pre-approval, certificate timestamp post-approval. |
| M-6 | On one AI vendor down: route to manual review (FR-040) or degrade to 2-of-2 (S48 T05)? | FR-040 vs M30-T05 | Keep FR-040 as default; make degrade-to-2-of-2 a tenant-configurable, evidence-recorded policy that still forces HiL (never silent). |
| M-7 | AI voice agents: keep PRD Won't-Have, or allow as a provider adapter for non-regulated tenants? | PRD §6 vs competitor Cat 6 + Req 8 | Keep Won't-Have for the certified pillar (human proof-bearer is the thesis); record "AI caller adapter" as an explicit future-option row, not a requirement. |
| M-8 | RPO/RTO official values? | NFR 15m/4h · ARCH 1h/4–8h · runbook 15m/60m | NFR values; amend ARCH; runbook stays stricter. |
| M-9 | Lockout 30 min (FRD) vs 15 min (code); impersonation ≤2 h (FRD) vs ≤60 min (code)? | FR-011/045 vs S03/S10 | Accept code values; amend FRD (tighter is fine). |
| M-10 | Coverage bar: 80% (NFRD/PRD) or 100% (tracker gate)? | NFR-057 vs CI gate | 90% branch-aware, with 100% on adapters and evidence code; amend both. |
| M-11 | New sprint numbering S60+ (continues series) vs new prefix (e.g. R-series)? | Q-series precedent | S60+ — the brief's own example uses S60. |
| M-12 | Run S60/S61 (docs-only) before S48 starts, or strictly after S58? | brief: "do not jump ahead of the open sprint" | After S47 closes, before S48 — S48–S51 are adapter sprints and must close at the new bar; S47's remaining tickets also adopt the standard retroactively at close. |
| M-13 | Google Sheets output: keep as an output adapter (S45 T08) or retire? | S45 | Keep as adapter (pilot dependency); not default for new tenants. |
| M-14 | Approve the `[RESEARCH REQUIRED]` list (§G.4) as desk-research-only tasks inside S79? | — | Yes. |
| M-15 | Annotate S17/S19 as "superseded by S29/S30/S32/S36"? | history rule | Yes, dated annotation only. |
| M-16 | ARCH stale paths/names (voters, polls, exotel_service, April app tree): fix in S81? | S26/S29/S44 | Yes. |
| M-17 | BRD-001 not attached — treat PRD as top authority for this recovery? | — | Yes, until BRD is supplied. |
| M-18 | TTS: out of scope unless FR-058 "recording disclosure playback" is meant to be synthesised? | FR-058 | Out of scope; pre-recorded audio satisfies FR-058. |

---

## N. Exact proposed changes — NOT YET APPLIED

### N.1 SPRINT_TRACKER.md
- Top-of-file: add a dated note under the header: "2026-10-04 Requirement recovery: completion levels D1–D7 adopted for S24+; recovery annex appended; S60–S81 added. Header totals are historical."
- Index table: add column `D-level` **for S24+ rows only** (S01–S23 cells "—/see annex"); add rows S60–S81 per §K.2 with status ☐ TODO and Planned = commit datetime.
- New section after S59 detail: "## Recovery Annex (2026-10-04) — completion level of historical sprints" = §C table verbatim, with the sentence "Historical ☑ DONE statuses above are unchanged; this annex records the independently assessed level."
- S47 detail: add note "T02–T05 close under PROVIDER_ADAPTER_STANDARD once S61 lands; T04 Google STT must be a real adapter; diarisation moved to S64."
- S48: add M30-T07 "replace M07 `_invoke_model` stub with the roster adapters (see S62)"; annotate T05 per §M-6.
- S51: re-title T04 "RFC3161 real TSA client (mandatory layer, not alternative)"; add T06 "Hedera adapter"; add note referencing S65.
- S56: annotate "Bot API adapter must be real (spec public); conforms to S61."
- S58: add M40-T05 "build-vs-buy cost line (see competitor v2 §8)".
- S17/S19 detail: append dated annotation "Superseded by S29/S30/S32/S36 (standalone rebuild); historical status unchanged."
- Enhancement Backlog: unchanged.

### N.2 TRACEABILITY.md
- §1: add BR-20 "Completion is measured on D1–D7; a sprint is not DONE below its declared level"; BR-21 "Evidence package is a verifiable manifest (root hash, TSA, anchor, independent verifier)"; BR-22 "AI performs defined advisory work inside TalkProof under HiL"; BR-23 "Competitive position accounts for AI-builder substitution".
- §2: RT-60..RT-81.
- New §6 "FR/NFR ↔ ticket map": FR-001..FR-106 and NFR-001..NFR-073 each mapped to tickets (existing + S60+). Initial fill from §B.2/§D of this document.
- Footer entry dated 2026-10-04.

### N.3 PRD.md → 1.1.0
- Revision row 1.1.0.
- §1.2: add row "Pillar 0 — Provider-neutral configuration layer (cross-cutting)" or fold into Pillar 3 text (decision at S81).
- §1.4 new: "AI-era positioning" (three sentences from §G.2).
- §5: Epics E-17/E-18/E-19 with feature rows from §J.
- §6: Won't-Have row per §M-7.
- §7.1: gate criteria restated in D-levels (Alpha = D4, Beta = D6, GA = D7).
- §2.1/§9.2: module map M22–M40; M17 per §M-1.

### N.4 FRD.md → 1.1.0
- Add FR-083..FR-106 (titles in §J); each in the FRD field format.
- Amend FR-040 Business Rules (vendor-down policy per §M-6; verdict vocabulary mapping to code labels), FR-052 (diarisation + word confidence are acceptance criteria, not description), FR-054 (manifest; TSA and anchor both; ordering per §M-5), FR-056 (add Exotel), FR-012 (per §M-2), FR-011/FR-045 (per §M-9).

### N.5 NFRD.md → 1.1.0
- NFR-068 Completion levels; NFR-069 Contract tests from official provider documentation for every adapter; NFR-070 No hard-coded tenant/provider values (lint-enforced); NFR-071 Provider specification drift monitoring; NFR-072 Evidence verifiable without platform access for full retention period; NFR-073 Model/prompt version pinning recorded per review.
- Reconcile NFR-042/043 (§M-8), NFR-057 (§M-10), NFR-023 provider list (§M-3).

### N.6 ARCHITECTURE.md → 1.2
- New §18 Provider Adapter Architecture (diagram: capability → interface → adapter → tenant/platform config → vault → provider; registry; health; fallback).
- New §19 Evidence Package (manifest, Merkle root, TSA, anchor, verifier).
- §5 component list: replace `voters`/`polls` with `contacts`/`certifications`; add config_resolver, storage, campaign_carrier, transcription packages.
- §6: repo layout = three standalone repos; remove April app tree.
- §7: JWT per §M-2; AI model names → "configured roster (default …)".
- §10: pipeline ordering per §M-5.
- §17: ADR-011 Adapter standard; ADR-012 Evidence manifest; ADR-013 Single AI gateway; ADR-014 Completion levels.

### N.7 talkproof_competitors.md → v2 (additive)
- New §8 "AI software builders & build-vs-buy substitution" (content of §G.2–G.4).
- Appendix: matrix v2 template (§G.3) with cells pre-labelled.
- No existing row removed.

### N.8 TELECOM_PROVIDER_POLICY.md
- §3 adapter status → D-level; §6 metering follow-up → S63; §7 `LANGUAGE_AI_COMPATIBILITY.md` → S48 T04 deliverable.

### N.9 New documents
`docs/03_architecture/COMPLETION_LEVELS.md` · `docs/03_architecture/PROVIDER_ADAPTER_STANDARD.md` · `docs/03_architecture/EVIDENCE_PACKAGE_SPEC.md` · `docs/03_architecture/LANGUAGE_AI_COMPATIBILITY.md` · `docs/92_planning/sprints/S60_completion_levels.md` … `S81_doc_amendments.md` (template per the brief's sprint-spec section list).

---

## Phase 7 — REVIEW GATE
STOP. Nothing above has been applied. Awaiting explicit approval on §M (decisions) and §N (changes). On "go ahead", the first execution is **S60 + S61 docs only** (no code), after which S47 resumes under the new bar.
