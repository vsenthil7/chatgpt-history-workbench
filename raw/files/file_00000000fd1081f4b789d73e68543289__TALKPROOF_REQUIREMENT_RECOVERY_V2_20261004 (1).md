# TalkProof — Requirement Recovery V2 (corrected after independent review)
**Session:** 2026-10-04 · **Supersedes for review purposes:** `TALKPROOF_REQUIREMENT_RECOVERY_20261004.md` (V1, retained unchanged as historical evidence) · **Status:** NOTHING APPLIED. No tracker, PRD, FRD, NFRD, architecture, traceability, sprint-file or code changes.

**Approval status (2026-10-04 19:16, independent review; 19:18 Senthil):** Parts 2/2b approved as working gap register; Part 3 approved as provisional recovery baseline (tracker-attested, code verification pending); Part 5b unscheduled and unapproved. PO decisions recorded in Part 7. Correction pass 19:18 applied exactly four edits: G48 class, Part 7 annex, D-03/D-07 marked as new PO decisions, this status line.

**What changed from V1 after independent review (19:08):** roadmap S60–S81 removed · draft FR-083..106 / NFR-068..073 removed · code-vs-requirement conflicts reopened (M17, lockout/impersonation, coverage) · Merkle root and dual timestamps re-labelled NEW DESIGN PROPOSAL · every gap given one primary class · provider claims split into requirement evidence / tracker-attested state / code-verified state · D-levels moved to capability level · reviewer's ten missed areas entered the gap assessment · V1's "13/24" count restated as tracker-attested, not code-inspected.

**Evidence chain used in every row:** authoritative requirement → historical sprint intent → tracker-attested implementation → code verification → recovered D-level → gap classification → open decision / candidate work.

**Labels:** `[SOURCE]` quoted sentence + ID/section · `[TRACKER]` tracker/traceability completion-note text (the June–July team's own words) · `[CODE]` code inspected (none this session) · `CODE VERIFICATION PENDING` · `[USER REQUIREMENT — 2026-10-04]` · `[NEW DESIGN PROPOSAL]` · `[INFERENCE]` · `[RESEARCH REQUIRED]`.

**Important scope statement:** no source code was opened in this session. Every "implemented / stub / hardcoded" statement below is tracker-attested. Code verification is a required step before any of it is treated as fact.

**Numbering note (reviewer withdrawal accepted):** Q-series header: *"kept SEPARATE from feature/cleanup sprints and clear of the reserved S43–S66 planning range"* `[TRACKER Q-series header]`. S43–S59 are occupied; S60 is next free. Not used in this document (no numbered sprints by gate condition).

---

## Part 1 — Recovered requirements (verbatim, decisive sentence only)

| ID | Requirement (quote) | Source | Why decisive |
|---|---|---|---|
| R-01 | Pillars: *"1 — Certified Core … 2 — RTC Suite … 3 — SaaS Platform"* | PRD §1.2 | Scope baseline; no approved reduction found in any source. |
| R-02 | *"Three independent AI models verify exactly what was said. A tamper-proof, blockchain-anchored certified PDF — signed by a human reviewer — goes to the client"* | PRD §1.1 | Core proof thesis. |
| R-03 | *"All three models must respond for a valid consensus. If any model times out (> 60s) or errors, the call enters `needs_manual_review` and routes to HiL regardless of other results. Models must come from ≥ 2 distinct providers"* | FR-040 Business Rules | Fixes the vendor-down behaviour. |
| R-04 | Per-model verdict *"`{ verdict: confirmed \| disputed \| uncertain, confidence: float, evidence: [string] }`"* | FR-040 Processing | Fixes verdict vocabulary and evidence-citation requirement. |
| R-05 | *"(3) RFC3161 timestamp from accredited TSA. (4) Blockchain anchor: submit hash to Hedera/Ethereum/private network per tenant config; store `tx_id`."* | FR-054 Processing | Both layers, numbered sequentially, in one requirement. |
| R-06 | *"Every certificate must include an RFC3161 timestamp token issued by an accredited Timestamp Authority (TSA)… Timestamp verification must work offline using standard tools (e.g., `openssl ts`)."* | NFR-024 (MH) | TSA is mandatory and independently verifiable. |
| R-07 | *"Every issued certificate must have its SHA-256 hash anchored on an external blockchain (Hedera/Ethereum/private network) within 10 minutes"* | NFR-023 (MH) | Anchor mandatory; provider list named. |
| R-08 | *"ADR-007 \| RFC 3161 + IOTA dual timestamp \| TSA = legally recognised; IOTA = public immutability"* | ARCH §17 | Architecture also treats both as required; names IOTA, not Hedera. |
| R-09 | *"On HiL approval, the backend produces a tamper-proof, blockchain-anchored certified PDF."* | FR-054 Description | Approval precedes certification. |
| R-10 | Pipeline: *"I → J (IOTA/blockchain anchor) → K (PDF generation) → L (HiL gate: Proposal created → reviewer queue)"* | ARCH §10 flowchart | Anchor + PDF precede the HiL gate. Conflicts with R-09. |
| R-11 | *"receive speaker-diarised transcript (agent / contact)… Outputs: … speaker-labelled segments, timestamps, word-level confidence scores"* | FR-052 | Diarisation + word confidence are outputs, not options. |
| R-12 | *"PSTN telephony must be abstracted behind a provider-agnostic interface supporting Twilio, Telnyx, and Vonage"* | FR-056 | Exotel absent from FRD. |
| R-13 | *"RTC — PSTN \| Exotel (primary) + Twilio/Telnyx/Vonage (BYO)"* | ARCH §7 | Exotel primary in architecture. |
| R-14 | *"All campaign PSTN calls must be dual-channel recorded"* | FR-058 | Recording channel requirement. |
| R-15 | *"Chat messages must be delivered in real time via WebSocket."* | FR-060 | Realtime transport is a requirement. |
| R-16 | *"Multi-party audio/video meetings must use LiveKit SFU. The Flutter app uses the official `livekit_client` Dart package"* | FR-062 | Media plane is a requirement. |
| R-17 | *"The backend must deliver push notifications to Flutter mobile (FCM/APNs) and Flutter Web (Web Push API)."* | FR-065 | Push is a requirement. |
| R-18 | *"Per-tenant AES-256-GCM DEK generated and wrapped by platform CMK (AWS KMS / GCP KMS / HashiCorp Vault)"* | FR-079 | KMS envelope, not symmetric app key. |
| R-19 | *"Before saving a key, the backend must execute a minimal test call to the provider"* | FR-029 | Test-connection must hit the provider. |
| R-20 | *"Stripe webhook signature verified… Create Stripe Customer + Subscription."* | FR-042 | Stripe API calls required. |
| R-21 | *"All external service calls (LLM, CPaaS, STT, blockchain, RFC3161 TSA) must be wrapped in circuit breakers."* | NFR-046 (MH) | Wrapping, not primitives. |
| R-22 | *"Short-lived JWT access tokens (RS256, 15-minute TTL)"* | FR-012; also NFR-014 | RS256. |
| R-23 | *"JWT (HS256) + Argon2id + TOTP"* | ARCH §7 | HS256. Conflicts with R-22. |
| R-24 | *"enforce lockout after 5 failures in 15 minutes (30-minute lockout)"* | FR-011 | 30-min lockout. |
| R-25 | *"requested duration (max 2 hours)"* | FR-045 | Impersonation ceiling. |
| R-26 | *"FR-070 — Flutter Desktop Build \| Module \| M17"* and *"FR-071 — Screen Share for Desktop Meetings \| Module \| M17"* | FRD §19 | M17 = Flutter desktop target. |
| R-27 | *"S18 \| M17 Admin Portal (talkproof-admin, React 19/Vite)"* | TRACKER index; TRACEABILITY RT-18 | M17 = React admin portal. Conflicts with R-26. |
| R-28 | *"Won't Have \| AI voice agents (automated calls without human) \| — \| Out of scope"* | PRD §6 | Explicit exclusion. |
| R-29 | *"RPO: ≤ 15 minutes for Tier A/B"*; *"RTO: ≤ 4 hours for full platform restore"* | NFR-042/043 | DR targets. |
| R-30 | *"RPO: 1 hour… RTO: 4 hours (Tier A/B), 8 hours (Tier C)"* | ARCH §15 | Conflicts with R-29. |
| R-31 | *"≥ 80% for `talkproof-backend`"* | NFR-057; PRD §8.2 | Coverage bar. |
| R-32 | *"`.coveragerc`/`setup.cfg` `fail_under` set to 100"* | TRACKER S01 note | Implemented gate differs. |
| R-33 | *"Check DNC list (national registry integration + platform DNC list). Block if consent absent or DNC listed."* | FR-078 | DNC registry integration required. |
| R-34 | *"Apply `presidio-analyzer` (or equivalent) to detect: names, phone numbers, email addresses, SSNs, DOBs, payment card numbers, national IDs"* | FR-038 | NER-grade PII redaction. |
| R-35 | *"call recording and transcript must be linked to the consent record for the entire retention period"* | NFR-030(e) | Consent is part of the evidence chain. |
| R-36 | *"'Verify Now' recomputes SHA-256 of downloaded PDF content in-browser… Offline verification works without network access after PDF download."* | FR-055 | Independent verification scope as specified. |
| R-37 | *"Certified call records within legally mandated retention cannot be erased."* | FR-077 | Redaction-vs-integrity rule already exists. |
| R-38 | *"Offboard: generates GDPR-compliant data export ZIP"* | FR-009 | Tenant-exit export exists; verification after exit not specified. |
| R-39 | *"Once any tenant is live on v1, no breaking changes… under `/api/v2/`"* | NFR-059 | API versioning; no evidence-schema versioning. |
| R-40 | *"DEK rotation without downtime… Annual CMK rotation."* | FR-079; NFR-022 | Key rotation; no hash/signature-algorithm agility. |
| R-41 | *"the campaign-voice calling path is carrier-abstracted… Switching carrier is a config change, not a code deploy."* | TELECOM_POLICY §2 | Runtime switching; no provider-exit/evidence-interpretation rule. |
| R-42 | *"§4 reverse-trace + §5 test-table intentionally NOT extended (consistent with S24+ pattern)"* | TRACEABILITY footer 2026-06-26 | FR/NFR IDs are not traced anywhere in tracker/traceability (confirmed by reading both files: no `FR-`/`NFR-` references). |
| R-43 | *"Spot-reads found "DONE" to mean "happy-path code exists and self-tests pass at 100% coverage" — not "feature works end-to-end.""* | TRACKER S24 context (line 994) | The team itself established the completion-semantics problem. |
| R-44 | Owner/Repo *"AI-burst/backend"*, Started *"Jun-burst"*, S01 Ended 2026-06-16 15:41 … S23 Ended 2026-06-17 05:53 | TRACKER index rows | 22 modules generated in ~16 h — primary evidence for the AI-builder competition category. |

**Requirements from this session's brief (not in any June document)** `[USER REQUIREMENT — 2026-10-04]`: completion levels D1–D7 (Req 1) · provider-neutral with real adapters (Req 2/3) · configuration through product (Req 4) · AI-builder competitor category (Req 5) · AI inside TalkProof assessment (Req 6) · proof-chain binding list (Req 7) · sprint-spec documents (Req 10).

---

## Part 2 — Gap register (one primary class per row)

Classes: **ORIG** original requirement already specified · **COVERED** existing sprint fully covers · **CORRECT** existing sprint covers but needs correction · **IMPL** implementation gap on an existing requirement, no open sprint · **CONFLICT** contradiction left open · **NEWREQ** genuinely new, from this session's brief only · **DESIGN** my design proposal · **RESEARCH** external research required.

| # | Gap | Requirement evidence | Tracker-attested state | Code | Primary class | Secondary note |
|---|---|---|---|---|---|---|
| G01 | Historical DONE ≠ product completion | R-43; brief Req 1 | S01–S23 notes each end "Carried-forward … at deployment" | — | **NEWREQ** (completion levels) | Governance, not product feature. |
| G02 | FR/NFR not traced to tickets/tests | R-42; brief Req 10 | confirmed absent | — | **NEWREQ** (traceability extension) | Prerequisite for requirement-ID columns. |
| G03 | LLM provider adapters in governed path are a stub | R-03/R-04; FR-037 | S08: *"`_invoke_model()` is the single provider isolation point… sandbox stub returns a neutral envelope (conf 0.0)"* | PENDING | **CORRECT** → S48 | S48 M30-T02 builds Claude/GPT-4o/Gemini adapters; add ticket "wire M07 `_invoke_model` to the roster adapters" (see Part 5 note). |
| G04 | April orchestrator LLM calls bypass vault, model strings literal | FR-030; BR-18 | S45 table: *"Keys \| `os.environ.get(...KEY)` direct … ❌ bypasses M05 BYO vault"* | PENDING | **COVERED** → S49 | S49 M31-T01/T04 explicit. |
| G05 | Vendor-down behaviour: S48 proposes 2-of-2 degrade | R-03 | S48 M30-T05: *"vendor-down fallback (degrade to 2-of-2, never silent)"* | — | **CONFLICT** | R-03 says route to HiL. Open decision D-04. |
| G06 | Verdict vocabulary: FR says confirmed/disputed/uncertain; code uses POSITIVE/NEGATIVE/NEUTRAL/INCONCLUSIVE | R-04 | S44-B: *"outcome labels (POSITIVE/NEGATIVE/NEUTRAL/INCONCLUSIVE) + JSON contract unchanged"* | PENDING | **CONFLICT** | Open decision D-05 (mapping vs rename). |
| G07 | RFC3161 TSA never implemented | R-05, R-06, R-08 | S12: *"external blockchain/RFC3161 anchoring populates `anchor_tx_id` at deployment via BYO provider"*; S45 table lists IOTA only | PENDING | **IMPL** (MH requirement, no open sprint builds a TSA client) | S51 names RFC3161 only as a "2nd adapter" (G08). |
| G08 | S51 frames TSA as alternative certification provider | R-05/R-06/R-08 (both required) | S51 M33-T04: *"Depth: 2nd adapter (RFC3161 trusted-timestamp) to prove abstraction"* | — | **CORRECT** → S51 | Sources establish precedence here (FR-054 numbers TSA and anchor as steps 3 and 4; ADR-007 "dual"). Not a conflict: S51 must treat TSA and anchor as two mandatory layers. |
| G09 | Anchor provider named inconsistently (Hedera/Ethereum vs IOTA) | R-05/R-07 vs R-08/R-13 ARCH | code = IOTA (S45) | PENDING | **CONFLICT** | Open decision D-03. |
| G10 | HiL before or after anchoring/PDF | R-09 vs R-10 | S12: draft → request_issue(HiL) → issue | PENDING | **CONFLICT** | Open decision D-06. |
| G11 | Diarisation + word-level confidence not evidenced | R-11 | S12 M11-T03 "already shipped operationally" = whisper-1 literal (S45) | PENDING | **CORRECT** → S47 | S47 owns transcription; its tickets omit diarisation/confidence. |
| G12 | Google STT second adapter must be real | R-11; brief Req 3 | S47 M29-T04 planned | — | **CORRECT** → S47 | Specify real adapter, not seam. |
| G13 | Campaign Twilio adapter is a seam | R-12; brief Req 3 | S43-D: *"carrier I/O isolated to one `_place` seam, sandbox-stubbed (deterministic SID, BYO key by design"* | PENDING | **IMPL** | S43 is DONE; no open sprint owns real carrier adapters. |
| G14 | M12 PSTN carriers are seams; carrier webhooks deferred | R-12 | S13: *"`_dial` / `_provision_number` (BYO-key by design, sandbox stubs — no live carrier key needed)"*; *"live carrier webhooks … wire at deployment"* | PENDING | **IMPL** | — |
| G15 | Telnyx/Vonage adapters absent | R-12 | TELECOM_POLICY §3 "Adapter pending" | — | **IMPL** | — |
| G16 | Exotel absent from FRD; primary in ARCH/code | R-12 vs R-13 | S43 default exotel | — | **CONFLICT** | Open decision D-07 (document-level; does not block build). |
| G17 | Dual-channel recording not evidenced | R-14 | no tracker mention of dual-channel | PENDING | **IMPL** | Attach to carrier adapter work. |
| G18 | Campaign metering at completion webhook | FR-031; FR-043 | S43 honest seam; POLICY §6 *"not wired at initiation"* | — | **IMPL** | — |
| G19 | WebSocket gateway not built | R-15 | S14: *"the WebSocket gateway + real S3 media upload + push fan-out wire at deployment"*; S30 app uses REST | PENDING | **IMPL** | — |
| G20 | LiveKit server/media plane absent | R-16 | S15: *"`_mint_sfu_token` isolation point (BYO LiveKit key, sandbox stub)"*; S30-C: *"WebRTC media-plane SDK-deferred"* | PENDING | **IMPL** | — |
| G21 | Push/email adapters are a seam | R-17 | S16: *"actual send is the single `_dispatch` isolation point (BYO FCM/APNs/web-push/SMTP keys, sandbox stub)"* | PENDING | **IMPL** | — |
| G22 | Native mobile bindings deferred | FR-072/073 | S19: *"native plugin bindings (flutter_callkit_incoming, firebase_messaging, local_auth) + store signing wire at build-out"* | PENDING | **IMPL** | — |
| G23 | KMS envelope absent (Fernet derived key) | R-18 | S06: *"`byo_encryption_key` setting (derives from JWT secret in dev/test, dedicated KMS key in prod)"*; S21: *"KMS/per-tenant key rotation handled by the deploy KMS path (carried-forward)"* | PENDING | **IMPL** | — |
| G24 | Test-connection does not call providers | R-19 | S06: *"`test_connection` (isolated `_probe`)"*; *"live provider connectivity probe … in staging"* | PENDING | **IMPL** | — |
| G25 | Stripe API adapter is a seam | R-20 | S09: *"single `_stripe()` isolation point (BYO Stripe key by design, sandbox stub — no live key needed)"* | PENDING | **IMPL** | Webhook signature verification attested real. |
| G26 | WhatsApp outbound send is a seam | BR-14 | S34-A: *"`_send` BYO-key isolation seam (sandbox stub, deterministic `wamid`, no live key)"* | PENDING | **IMPL** | Inbound Meta signature attested real. |
| G27 | Telegram adapter must be real | BR-19; brief Req 3 | S56 planned | — | **CORRECT** → S56 | Specify Bot API adapter from spec. |
| G28 | Circuit breakers not wrapped around provider calls | R-21 | S20: *"resilience primitives are adopted incrementally around external provider calls"*; OTel/PagerDuty "at deployment" | PENDING | **IMPL** | — |
| G29 | JWT algorithm | R-22 vs R-23 | S03 built HS256 (ARCH) | PENDING | **CONFLICT** | Open decision D-01. |
| G30 | Lockout duration | R-24 | S03: *"5-failure lockout -> 15 min (HTTP 423)"* | PENDING | **CONFLICT** | Open decision D-08 (drift or approved change?). |
| G31 | Impersonation ceiling | R-25 | S10: *"time-box (1–60 min, default 15)"* | PENDING | **CONFLICT** | Open decision D-08. |
| G32 | M17 identity | R-26 vs R-27 | tracker/traceability consistently React admin | — | **CONFLICT** | Open decision D-02. Note: PRD Epic E-15 maps admin portal to M09/M10/M04/M21, not M17, so PRD and FRD agree with each other and disagree with the tracker. |
| G33 | AI voice agents | R-28; competitor Cat 6; brief Req 8 | — | — | **CONFLICT** (product intent) | Open decision D-09. Reviewer's split adopted: "proof subject is human" vs "platform may handle AI-originated interactions" are separate questions. |
| G34 | RPO/RTO values | R-29 vs R-30; tracker S20 "RPO ≤ 15m / RTO ≤ 60m" | — | — | **CONFLICT** | Open decision D-10. |
| G35 | Coverage bar | R-31 vs R-32; actual 99.3–99.5% (S24, S31-E) | — | — | **CONFLICT** | Open decision D-11. |
| G36 | DNC national registry integration | R-33 | S21 lists ConsentRecord only; no DNC mention | PENDING | **IMPL** | — |
| G37 | PII redaction is regex, not NER | R-34 | S08: *"`redact_pii()` (email/phone/ssn/cc)"* | PENDING | **IMPL** | FR allows "or equivalent"; regex on 4 types is not equivalent to 7 named entity classes. |
| G38 | Consent record not bound to certificate | R-35 | S21 consent ledger exists; S12 canonical payload = metadata+transcript+consensus+approver+timestamp (FR-054) | PENDING | **IMPL** | Binding mechanism is open (G41). |
| G39 | Recording hash, transcript hash, STT engine/version not in certificate | FR-054 payload list; brief Req 7 | S12 `content_hash` over canonical JSON; Transcript row gains `engine` (S47-A) | PENDING | **NEWREQ** (evidence binding beyond FR-054's list) | Brief Req 7 extends FR-054; needs PO acceptance. |
| G40 | Policy/script version, required/prohibited statements, prompt version, model version pinning | brief Req 7 | Campaign.disclosure_script (text); M22 records model/provider per call | PENDING | **NEWREQ** | — |
| G41 | Binding mechanism (Merkle root + leaf hashes) | — | — | — | **DESIGN** | Not a recovered requirement. Evaluated only if G39/G40 accepted. |
| G42 | Two timestamps (evidence-root pre-HiL, certificate post-HiL) | — | — | — | **DESIGN** | Candidate resolution for D-06 only. |
| G43 | Independent verifier beyond in-browser hash | R-36; R-06 (`openssl ts`) | FR-055 portal + `verify_certificate` API (S12) | PENDING | **IMPL** on R-06 once TSA exists | Offline CLI is not required by FR-055 as written → any CLI is DESIGN. |
| G44 | Provider selection/config through product (capability discovery, fallback by provider, health, runtime switch, rotation UI) | brief Req 4; PRD J-03 covers BYO key add/test/spend-cap only | S35 tenant-config page (storage/WhatsApp keys); S28-T05 notes platform-key admin screen is "candidate backlog screen"; S46 resolver | PENDING | **NEWREQ** | Partially overlaps FR-028..031 (keys); selection/health/discovery are new. |
| G45 | Provider adapter completion standard (18-point) | brief Req 3 | S33 storage drivers are the attested best example: *"real Google Drive v3 upload… All Drive I/O isolated to the single `_client()` seam"* | PENDING | **NEWREQ** (engineering standard) | — |
| G46 | AI-builder competitor category | brief Req 5; R-44 | competitors doc has no such category | — | **RESEARCH** | Framework is NEWREQ at strategy level; market facts RESEARCH. |
| G47 | % reproducible / commodity classification | — | — | — | **RESEARCH** | V1's 80–90% withdrawn as fact; hypothesis only. |
| G48 | AI inside TalkProof (14 opportunities) | brief Req 6 | existing: 3-model verify (real, hardcoded), M07 advisory (stub), M14 summary, M22 ledger | — | **RESEARCH** | Secondary: opportunity assessment — each passes the 7-step test (problem → AI advantage → deterministic alternative → human authority → audit evidence → failure mode → fallback) before any becomes a requirement. |
| G49 | Tier B data migration / Tier C live provisioning | FR-007/008 | S02: *"applied by the deploy pipeline"* | PENDING | **IMPL** | — |
| G50 | Live E2E runs deferred (Playwright staging, device integration_test) | Q07 standard | all six frontend sprints: *"deferred to deploy"* | — | **IMPL** (D6 evidence) | — |
| G51 | ARCH stale (April app tree, `voters`/`polls` routes, `exotel_service` only) | S26/S29/S44 | — | — | **IMPL** (documentation) | Doc-only fix after decisions. |
| G52 | Tracker header "22 modules · 122 tickets" | — | 40 modules | — | **IMPL** (documentation) | Add dated note; do not rewrite. |

### Part 2b — Reviewer's ten missed areas, assessed against sources first

| Area | Existing coverage | Primary class |
|---|---|---|
| Evidence schema evolution (v1 cert verifiable after v7) | R-39 covers API, not evidence schema; FR-055 signed link 30 days re-issuable | **NEWREQ candidate** — not covered |
| Cryptographic agility | R-40 covers key rotation; SHA-256/AES-256 fixed in FR-054/NFR-020 | **NEWREQ candidate** — not covered |
| Provider exit (historic evidence interpretable after provider disappears) | R-41 covers runtime switching only | **NEWREQ candidate** — not covered |
| Model reproducibility (hosted model drift) | M22 ledger records model name; no version pin | **NEWREQ candidate** — partial |
| Legal/regulatory version at decision time | NFR-030(a) *"exact consent text version"* only | **NEWREQ candidate** — partial |
| Clock/time trust beyond TSA | NFR-056 timezone notation; NFR-024 TSA | **NEWREQ candidate** — partial |
| Redaction vs integrity | R-37 (FR-077) + crypto-shred erase (S21) | **ORIG** — covered at rule level; verification of a redacted record unspecified |
| Tenant export/exit with continued verification | R-38 export exists; verification after exit unspecified | **NEWREQ candidate** — partial |
| Verifier longevity (independent of TalkProof's existence) | R-36 offline hash; NFR-064 on-prem; TSA/anchor by design external | **ORIG partial** — PDF-level only |
| AI supply-chain provenance (what generated deployed behaviour) | M22 runtime ledger; build-time none | **NEWREQ candidate** — not covered |

None become requirements in this document.

---

## Part 3 — Capability-level D-assessment

Target = level the requirement implies as written · Actual = recovered level from tracker · Confidence: **T** tracker-attested only · **S** source-document only.

| Capability | Requirement | Target | Recovered actual | Evidence basis | Missing / deferred components | Conf. |
|---|---|---|---|---|---|---|
| Tenancy Tier A (RLS) | FR-005/006 | D7 | D3 | S02 note | live RLS verification in staging | T |
| Tenancy Tier B / C | FR-007/008 | D7 / D6 | D3 / D2 | S02 "deploy pipeline" | migration, routing, IaC provisioning | T |
| Auth core (argon2, JWT, MFA, sessions) | FR-011..013 | D7 | D3 | S03 | algorithm conflict (G29); lockout drift (G30) | T |
| SSO OIDC/SAML, SCIM | FR-015..017 | D5 | D3/D4 | S03 "unit-tested via stubs… exercised in staging" | live IdP confirmation unattested | T |
| RBAC | FR-019..021 | D7 | D3 | S04 | multi-role per user deferred | T |
| Audit chain / access trail / auth events | FR-022..025 | D7 | D3 | S05 | GeoIP real lookup; WORM provisioning | T |
| SIEM export | FR-027 | D5 | D4 | S05 HMAC + tests | live delivery | T |
| BYO key store + router + metering | FR-028, FR-030, FR-031 | D7 | D3 | S06 | KMS (G23) | T |
| Test-connection | FR-029 | D5 | D2 | S06 `_probe` | provider calls | T |
| HiL engine | FR-032..036 | D7 | D3 | S07 | escalation push delivery | T |
| Governed AI envelope | FR-037 | D7 | D3 | S08 | — | T |
| Governed AI provider calls | FR-037/040 | D5 | D2 | S08 stub | adapters (G03) | T |
| Guardrails PII/injection | FR-038/039 | D5 | D3 (regex) | S08 | NER (G37) | T |
| 3-model consensus (orchestrator) | FR-040/053 | D5 | D3 hardcoded | S45 table | vault keys, roster config, vocabulary (G04–G06) | T |
| Transcription | FR-052 | D5 | D3 hardcoded | S45; S47-A interface | diarisation, confidence, engine select (G11/G12) | T |
| Hash + canonical certificate + offline hash verify | FR-054(1–2), FR-055 | D6 | D3 | S12 | — | T |
| RFC3161 TSA | FR-054(3), NFR-024 | D5 | **D1** | S12 "at deployment" | everything (G07) | T |
| Blockchain anchor | FR-054(4), NFR-023 | D5 | D3 (IOTA, hardcoded, stub-tx fallback) | S45; S01 `iota_stub_tx_id` | vault keys, provider abstraction (S51), Hedera | T |
| Certified PDF | FR-054(5) | D6 | D3 | S12 reuses April pdf_service | TSA token/anchor embedding | T |
| S3 Object Lock immutability | FR-054(6), NFR-045 | D5 | D2 | S05/S12 "provisioned by deploy" | — | T |
| Client portal | FR-055 | D6 | D3 | S29/S36 app; portal route unattested | signed-link portal page | T |
| Campaign carrier abstraction + selection | BR-16 | D4 | D3 (Exotel real April; Twilio seam) | S43 | real Twilio/Telnyx/Vonage (G13/G15) | T |
| M12 PSTN out/in + numbers | FR-056/057 | D6 | D3 | S13; S31 inbound real HMAC webhook | carriers (G14), webhooks | T |
| Recording dual-channel + storage | FR-058 | D5 | D3 (storage D4) | S33 drivers; S29-E carrier-side | dual-channel (G17), live upload | T |
| Chat models/REST | FR-059 | D6 | D3 | S14/S30 | — | T |
| Chat realtime WebSocket + presence | FR-060/066 | D6 | **D2** | S14 "at deployment" | gateway (G19) | T |
| E2E DMs | FR-061 | D5 | D3 server-side | S14 | client-side X3DH in Dart unattested | T |
| Meetings scheduling/rooms | FR-062 | D6 | D3 | S15/S30 | LiveKit (G20) | T |
| Meeting recording / transcription / summary | FR-063/064 | D5 | D3 logic | S15 | egress, live STT, real summary model | T |
| Push + email | FR-065 | D5 | D2 | S16 seam | adapters (G21) | T |
| Flutter app (web/desktop) | FR-067..069 | D6 | D3/D4 vs mocks | S29–S36 "flutter test green; device/web run deferred" | PWA, live E2E (G50) | T |
| Flutter mobile native | FR-072/073 | D6 | D2 | S19 | bindings, store builds (G22) | T |
| Admin portal | PRD E-15 | D6 | D3/D4 vs mocks | S28/S35 Vitest; Playwright deferred | live E2E; provider-key screens | T |
| Observability endpoints | FR-074 | D5 | D3 | S20 | scrape, tracing export | T |
| Resilience wrapping | FR-075/NFR-046 | D5 | D2 | S20 "adopted incrementally" | wrapping (G28) | T |
| DR | FR-076 | D5 | D2 (runbook) | S20 | tested restore | T |
| GDPR export/erase | FR-077 | D5 | D3 | S21 | — | T |
| TCPA consent | FR-078 | D5 | D3 | S21 | DNC registry (G36) | T |
| KMS envelope | FR-079 | D5 | D2 | S06/S21 | adapter (G23) | T |
| Security headers / rate limit | FR-080 | D5 | D3 | S21 | — | T |
| White-label / packaging | FR-081/082 | D6 | D3 | S22/S28-T07 | — | T |
| AI ledger | M22 | D5 | D3 | S23 "sandbox stub records neutral rows" | real values after G03 | T |
| Storage abstraction | BR-15 | D5 | **D4** | S33 fake-client contract tests | live run | T |
| WhatsApp channel | BR-14 | D5 | D3 (inbound D4) | S34 | outbound send (G26) | T |
| Config resolver | BR-18 | D4 | D4 | S46 tests | — | T |
| Inbound calling + polymorphic pipeline | BR-03/05 | D5 | D3/D4 | S31/S59 | live carrier inbound | T |

**Provider inventory restated** (V1 said "13 seams / 6 hardcoded real / 5 correct"): that tally is derived from tracker completion notes quoted in G03–G26 and S33/S05/S03; it is **tracker-attested, CODE VERIFICATION PENDING** for every row.

---

## Part 4 — Open decisions (options only; no recommendation that amends an approved document)

| ID | Decision | Options | What the sources establish |
|---|---|---|---|
| D-01 | JWT algorithm | (a) RS256 per FR-012/NFR-014 and refactor; (b) PO formally changes requirement to HS256 | Approved FRD/NFRD say RS256; ARCH + build say HS256. Precedence not established by the sources (ARCH is "Baseline", FRD is "Approved"). |
| D-02 | M17 identity | (a) FRD stands: M17 = Flutter desktop; tracker/traceability RT-18 re-labelled (e.g. admin portal gets a new module ID) with dated note; (b) PO changes PRD/FRD so M17 = admin portal | PRD and FRD agree with each other (desktop); tracker/traceability agree with each other (admin). No source grants the tracker precedence over approved requirement documents. |
| D-03 | Anchor provider list | (a) FRD/NFRD list (Hedera/Ethereum/private) is binding → IOTA is non-conforming; (b) PO extends list to include IOTA; (c) provider-neutral with no named default | ARCH ADR-007 and code say IOTA; FR-054/NFR-023 say Hedera/Ethereum/private. |
| D-04 | Vendor-down (G05) | (a) FR-040 as written: any failure → manual review; (b) PO amends FR-040 to allow configured degrade with recorded evidence and HiL | FR-040 is explicit. S48 T05 as written contradicts it. |
| D-05 | Verdict vocabulary (G06) | (a) rename code labels to FR-040 terms; (b) define a recorded mapping; (c) PO amends FR-040 | FR-040 is explicit. |
| D-06 | HiL ordering (G10) | (a) FRD: approval → anchor → PDF; (b) ARCH: anchor → PDF → approval; (c) design proposal G42 | FRD "Approved" vs ARCH "Baseline"; both dated June 2026. |
| D-07 | Exotel in FRD (G16) | (a) PO adds Exotel to FR-056 list; (b) treat ARCH as the carrier list of record | Documentation-level. |
| D-08 | Lockout 30→15 min; impersonation 2 h→60 min (G30/G31) | (a) drift → correct code to FRD; (b) PO records an approved change | Nothing in the tracker records a requirement-change decision for either value. |
| D-09 | AI-originated interactions (G33) | (a) keep Won't-Have entirely; (b) keep "proof subject is a human" and allow the platform to record/verify AI-originated interactions as a separate capability; (c) reopen | PRD §6 explicit; brief Req 8 asks for capability-based evaluation. |
| D-10 | RPO/RTO (G34) | (a) NFR values bind; (b) PO reconciles | NFRD "Approved" vs ARCH "Baseline". |
| D-11 | Coverage bar (G35) | (a) NFR-057 80% binds and the CI gate is a stricter engineering policy; (b) PO sets a new bar | Two different artefacts; no decision recorded. |
| D-12 | Accept brief Req 7 extensions (G39/G40) as requirements? | yes / no / partially | These are new user requirements, not recovered ones. |
| D-13 | Accept brief Req 4 (G44) as requirements beyond FR-028..031? | yes / no / partially | New user requirements. |
| D-14 | Which of Part 2b's ten areas enter the requirement process? | per-row | Assessment above. |
| D-15 | BRD-001 availability | supply it / treat PRD as top authority | PRD cites BRD-001 as parent. |

---

## Part 5 — Candidate work packages (unnumbered; each answers "why can't an existing sprint absorb this?")

Rule applied: if an open or TODO sprint already owns the requirement, the work goes back into that sprint as a correction, and is listed in 5a, not 5b.

### 5a — Returned to existing sprints (not new packages)
| Existing sprint | Correction required | Gap |
|---|---|---|
| S47 | T04 = real Google STT adapter; add tickets for diarisation + word-level confidence (FR-052 outputs) | G11, G12 |
| S48 | T02 adapters are real API clients via vault (after S49); add ticket to replace M07 `_invoke_model` stub with the roster adapters so there is one AI invocation path; T05 held until D-04; add `LANGUAGE_AI_COMPATIBILITY.md` as T04 deliverable (POLICY §7 gap) | G03, G05 |
| S49 | unchanged (already explicit) | G04 |
| S50 | record strategy id in the certified payload (needed whatever D-12 decides) | — |
| S51 | TSA and anchor are two mandatory layers (FR-054 steps 3–4, ADR-007); T04 becomes "RFC3161 TSA client"; anchor provider list per D-03 | G07, G08 |
| S56 | Bot API adapter is real, from spec | G27 |
| S45 close | add conformance gate: no `os.environ` key reads, each stage behind a real adapter | — |
| S58 | add a build-vs-buy cost line once G46 research exists | G46 |

### 5b — Candidate packages
| Package (name only) | Gaps | Class basis | Why existing sprint cannot absorb this |
|---|---|---|---|
| Completion-level governance + FR/NFR traceability | G01, G02 | NEWREQ (brief Req 1/10) | No open sprint is a governance/traceability sprint; S40/S41 (docs standards) are DONE. Must exist before any adapter sprint can state a D-level honestly. |
| Provider adapter standard + conformance harness | G45 | NEWREQ (brief Req 3) | S45 close could host a pipeline-only version, but the standard also governs M08/M12/M14/M15/M24 adapters outside the pipeline. If the PO prefers, it can be scoped into S45 close and the harness reused — flagged as an option. |
| Telephony carrier completion (M12 `_dial`, campaign Twilio `_place`, Telnyx, Vonage, status webhooks, dual-channel, completion metering) | G13–G18 | IMPL on FR-056/057/058 | S13 and S43 are DONE; no TODO sprint owns carrier adapters. |
| Payment/notification/messaging adapter completion (Stripe, FCM/APNs/WebPush, SMTP/SES, Meta Graph send) | G21, G25, G26 | IMPL on FR-042/065, BR-14 | S09/S16/S34 are DONE; S56 covers Telegram only. |
| Key management (KMS envelope, rotation, real test-connection) | G23, G24 | IMPL on FR-029/079 | S06/S21 are DONE; S49 moves keys into the vault but does not replace Fernet with KMS. |
| Trusted-time and anchoring completion (TSA client; anchor provider per D-03; embedding in PDF; `openssl ts` verification) | G07, G43 | IMPL on FR-054/NFR-023/024 | S51 abstracts the *provider*; it does not build the TSA client or the PDF embedding. Could be absorbed into S51 if the PO widens S51 — flagged as an option. |
| Evidence binding (consent, recording hash, transcript hash, engine/model/prompt versions) | G38, G39, G40 | IMPL (G38) + NEWREQ (G39/G40, pending D-12) | S12 is DONE; S50/S51 touch voting/certification provider, not the certified payload. Mechanism (G41) stays DESIGN. |
| Realtime gateway | G19 | IMPL on FR-060/066 | S14 DONE; no TODO sprint. |
| Media plane (LiveKit server + Flutter SDK, egress, screen share) | G20 | IMPL on FR-062/063/071 | S15/S30 DONE; no TODO sprint. |
| Native mobile completion | G22 | IMPL on FR-072/073 | S19 DONE. |
| Resilience/observability wiring | G28 | IMPL on NFR-046/048 | S20 DONE. |
| Compliance completion (DNC registry, NER redaction, Tier B/C provisioning, Object Lock) | G36, G37, G49 | IMPL | S21/S02 DONE. |
| Provider configuration through product | G44 | NEWREQ (pending D-13) | S35 built a key/value tenant-config editor; selection/discovery/health/switch/rotation UI has no owner. |
| Product E2E (D6) evidence runs | G50 | IMPL (evidence) | Every frontend sprint deferred the live run "to deploy"; no sprint owns the deploy-time run. |
| AI-builder competitive framework (desk research only) | G46, G47 | RESEARCH | Competitor doc is a static report; S58 is cost-model only. |
| AI-inside opportunity assessment | G48 | RESEARCH/assessment | No existing sprint; produces candidate requirements, not features. |
| Document amendments after decisions D-01..D-15 | G16, G51, G52 + decided items | documentation | Depends on Part 4 outcomes; cannot precede them. |

Nothing above is scheduled, numbered, or approved.

---

## Part 6 — Reviewer's ten areas: disposition summary
Entered the gap process in Part 2b. Covered already: redaction-vs-integrity (FR-077), verifier longevity at PDF level (FR-055). Partially covered: model reproducibility (M22), regulatory version (NFR-030a), clock trust (NFR-024/056), tenant exit (FR-009). Not covered: schema evolution, cryptographic agility, provider exit, AI supply-chain provenance. All await D-14 before any becomes a requirement.

---

## Part 7 — PO Decision Annex (dated 2026-10-04 19:16, independent review; confirmed by Senthil 19:18)

Part 4 is unchanged above and remains the record of each contradiction as the sources left it. This annex records the Product Owner's dated resolution separately. Where a decision is marked **NEW PO DECISION**, it is not recovered from any June document; it is a product decision taken on 2026-10-04.

| Decision | PO decision | Reason (as given) | Nature |
|---|---|---|---|
| D-01 JWT | **RS256** | Approved FR/NFR requirement wins unless deliberately changed. | Recovered requirement upheld |
| D-02 M17 | **Flutter Desktop remains M17** | PRD+FRD agree; tracker naming is historical drift. Preserve history and correct forward mapping. | Recovered requirement upheld |
| D-03 Anchor providers | **Provider-neutral; no hard-coded default.** Existing named providers (Hedera/Ethereum/private per FR-054/NFR-023; IOTA per ADR-007/code) become supported, configurable adapters rather than product identity. | Best fit with the product's provider-neutral direction. | **NEW PO DECISION** — supersedes both document lists; historical contradiction G09 preserved in Part 2/Part 4 |
| D-04 Vendor-down | **FR-040 stands** — any required model failure → `needs_manual_review`. | Do not weaken proof integrity for availability. S48 M30-T05 must conform. | Recovered requirement upheld |
| D-05 Verdict vocabulary | **FR-040 vocabulary is canonical** (`confirmed/disputed/uncertain`). Internal mappings may exist; persisted/audited contract uses requirement terminology. | — | Recovered requirement upheld |
| D-06 HiL ordering | **OPEN — deferred** | Touches the fundamental proof/evidence lifecycle; resolve during evidence-chain architecture, not by picking the stronger-looking document. | Open |
| D-07 Exotel in FRD | **Provider-neutral requirement.** No carrier is special in the product requirement; Exotel is another supported adapter. | — | **NEW PO DECISION** — historical contradiction G16 (FR-056 vs ARCH §7) preserved in Part 2/Part 4 |
| D-08 Security values | **Requirements stand** — 30-minute lockout (FR-011), max 2-hour impersonation (FR-045). Code values are drift. | Until an explicit security decision changes them. | Recovered requirement upheld |
| D-09 AI-originated interactions | **Option B** — certified proof subject remains human; AI-originated interactions may be captured/verified as a distinct capability. TalkProof does not become an autonomous-calling product. | — | Recovered requirement (PRD §6) upheld with scoped clarification |
| D-10 RPO/RTO | **NFR values bind** — ≤15 min RPO / ≤4 h RTO. Architecture must conform. | — | Recovered requirement upheld |
| D-11 Coverage | **Option A** — 80% (NFR-057) is the requirement floor; 100% remains a stricter engineering policy. Not contradictory once distinguished. | — | Recovered requirement upheld |
| D-12 Evidence extensions (G39/G40) | **Accepted in principle; architecture deferred.** What must be bound (recording, transcript, STT, model, prompt, policy provenance) is accepted; Merkle or any other mechanism (G41) is not. | Belongs in the proof proposition. | New user requirement accepted (scope only) |
| D-13 Product provider configuration (G44) | **Accepted.** Keys alone are insufficient. | Central to the configurable, provider-neutral product. | New user requirement accepted |
| D-14 Ten missed areas (Part 2b) | **All 10 accepted into requirements analysis.** Not automatically requirements; each needs wording, threat/use case and acceptance criteria before approval. | — | Analysis scope accepted |
| D-15 BRD-001 | **OPEN — deferred pending BRD-001.** PRD remains highest available product source. | Do not invent its authority. | Open |

Consequences recorded, not actioned: S48 T05, S51 T04, S47 T04 corrections in Part 5a now have their governing decisions (D-04, D-03, D-05); G29/G30/G31/G32/G34/G35 are closed as drift-to-be-corrected, not as requirement changes. No document or code has been modified as a result of this annex.

## Gate
Parts 2/2b, 3 and 7 constitute the frozen recovery baseline on approval of this correction pass. D-06 and D-15 remain open. Part 5b remains unscheduled. No architecture, sprint planning, requirement-document amendment or code work begins from this document.
