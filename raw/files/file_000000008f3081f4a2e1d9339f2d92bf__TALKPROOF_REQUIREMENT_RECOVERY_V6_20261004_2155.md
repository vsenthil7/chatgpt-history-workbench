# TalkProof — Requirement Recovery V6 (V5 + accepted gate corrections + authoritative D1–D7 reconciliation)
**Session:** 2026-10-04 21:55 · **Lineage:** V2 (frozen recovery baseline) → V3 (first frontier/recovery expansion, historical review evidence) → V4 (`…_V4_20261004_2021.md`, V3 + corrections C01–C10) → **E-01 code verification** (`TALKPROOF_E01_CODE_VERIFICATION_V001_20261004_1945.md`, 46 rows inspected, tests executed) → V5 (`…_V5_20261004_2058.md`, reconciled candidate baseline) → **V5 Gate Review** (`TALKPROOF_V5_GATE_REVIEW_V001_20261004_2115.md`, five accepted corrections R-36, R-44/45, R-D26, R-EV7, R-SCALE) → **D-scale reconciliation** (`TALKPROOF_DSCALE_RECONCILIATION_V001_20261004_2135.md`, independently reviewed and closed 2026-10-04 21:44 "ACCEPT WITH CORRECTIONS — CLOSED") → **V6 (this file): corrected reconciliation baseline**.

> **V6 is a RECONCILIATION-ONLY SUCCESSOR TO V5.** It applies exactly (1) the five corrections accepted by the independent V5 gate review and (2) the final authoritative D1–D7 reconciliation as closed by independent review, and nothing else. It makes no Product Owner decision (D-01..D-26 remain unapproved; D-26 is listed open), issues no FR/NFR ID, numbers no sprint, changes no source code, redesigns no architecture and neither expands nor shrinks scope. V2, V3, V4, E-01, V5, the V5 gate review, the D-scale reconciliation and the Config Resolver test-run record remain immutable. V4 is reproduced verbatim as Parts 1–36 (unchanged from V5). Parts 37–47 are V5's content with only the edits listed in Part 48; Parts 48–49 are new. Every V6 edit is traceable in Part 49.

**Status:** NOTHING APPLIED. Code-verified state is populated (E-01) and D-levels are now **authoritative** (D-scale reconciliation, closed 21:44). Tracker-attested state is preserved **separately** from code-verified state in every row — the two are never merged. V6 is to be frozen before Product Owner decisions.

**Labels added in V5 (retained in V6):** `CODE-VERIFIED (E-01)` · `CODE VERIFICATION INCOMPLETE` · `EXTERNAL RUNTIME VERIFICATION REQUIRED` · `UNABLE TO VERIFY FROM SUPPLIED REPOSITORIES` · `CODE-DISCOVERED IMPLEMENTATION DEFECT` (CD-nn). All V2/V3/V4 labels are unchanged.

**D-scale used in this file: the AUTHORITATIVE D1–D7 Definition of Done** — D1 SPECIFIED · D2 DESIGNED · D3 IMPLEMENTED · D4 CONTRACT VERIFIED · D5 LIVE INTEGRATED · D6 PRODUCT E2E VERIFIED · D7 PRODUCTION READY (supplied 2026-10-04 21:18; reconciled against all 46 rows in `TALKPROOF_DSCALE_RECONCILIATION_V001_20261004_2135.md` §A.2, independently reviewed and closed). Interpretation applied uniformly: D1 = requirement only, nothing designed or implemented; D2 = design artefact exists (interface/seam/stub/config-only/documented design) but the capability is not implemented; D3 = capability actually implemented in production code, whether hard-coded, unintegrated, defective at integration or only mock-tested; D4 = an independently defined, sufficiently precise contract exists (external-provider or internal) **and** evidence shows the production implementation satisfies it (tests exercise the production implementation, inputs/outputs and error/edge behaviour are asserted against that contract, execution is evidenced); D5/D6/D7 require recorded live, product-E2E or production-operation artefacts. Interface existence, mocked implementation, fake-ID stubs, unit coverage alone and tests that mock the adapter away cannot establish D4 and do not by themselves fix the D1/D2/D3 level. The E-01 working scale that V5 used is superseded; EV-08 is closed. No row carries a provisional label.

**How to read this file:** Parts 1–36 = V4 verbatim (which contains V2 verbatim as Parts 1–7 and V3 as Parts 8–36). Part 37 = V5 change log (unchanged). Part 38 = the 46-row reconciled capability table in V4 Part 3 order, now with authoritative D-levels (Part 3 is **not** edited; Part 38 supersedes it as the working table). Parts 39–47 = V5's gap reconciliation, defect register, proof-chain table, preserved conflicts, D-level discipline, test evidence, external verification register, PO decision pack and V4→V5 delta ledger, edited only where Part 48 says so. Part 48 = V6 change log. Part 49 = V5→V6 delta ledger. Final gate block at the end.

---

# V4 — PRESERVED VERBATIM (PARTS 1–36)

# TalkProof — Requirement Recovery V4 (V3 + ten accepted independent-review corrections)
**Session:** 2026-10-04 20:21 · **Lineage:** V2 (frozen recovery baseline) → V3 (`TALKPROOF_REQUIREMENT_RECOVERY_V3_20261004_1954.md`, first frontier/recovery expansion, retained unchanged as historical review evidence) → **V4 (this file)**.

> **V4 supersedes V3 as the candidate working document. V3 is retained unchanged as historical review evidence. V2 remains the frozen recovery baseline embedded/preserved through the lineage. V4 applies only the ten accepted independent-review corrections C01–C10 (independent review of 2026-10-04 20:16, accepted by Senthil 20:21); it does not retrospectively alter V3.** V4 change log: Part 8A. Gate sequence: V4 correction → verify V2 preservation + V3→V4 controlled delta → code-verify all 46 capabilities → PO decisions → requirements/sprint work.

**V3 session line (preserved):** 2026-10-04 19:54 · **Extends:** `TALKPROOF_REQUIREMENT_RECOVERY_V2_20261004.md` (V2, preserved below as Parts 1–7, unchanged except one clerical correction recorded in Part 9) · **Supersedes nothing** — V1 and V2 remain immutable historical evidence · **Status:** NOTHING APPLIED. No tracker, PRD, FRD, NFRD, architecture, traceability, sprint-file or code changes. No FR/NFR IDs issued. No sprint numbers issued.

**Inputs actually supplied for V3:** (1) the V2 recovery baseline; (2) the V3 master brief (Senthil's message of 2026-10-04 19:51/19:54); (3) external web research performed 2026-10-04. **Not supplied:** PRD, FRD, NFRD, ARCH/ADRs, SPRINT_TRACKER.md, TRACEABILITY.md, competitor/Build-It analysis, repository ZIPs, V1. Every statement that depends on those is marked `SOURCE REVALIDATION PENDING — INPUT NOT SUPPLIED` or `CODE VERIFICATION PENDING — REPOSITORY NOT SUPPLIED`. Nothing in Parts 8+ infers missing evidence.

**Labels used in Parts 8+ (V3 brief §0):** `SOURCE` · `TRACKER-ATTESTED` · `CODE-VERIFIED` (none in V3) · `CODE VERIFICATION PENDING` · `PRODUCT OWNER DECISION` · `USER/PO REQUIREMENT` · `DERIVED REQUIREMENT` · `MARKET FACT` · `FRONTIER RESEARCH FINDING` · `FORECAST` · `ARCHITECTURE PROPOSAL` · `HYPOTHESIS` · `EXPERIMENT REQUIRED` · `DEFERRED` · `REJECTED`. V2's own labels (`[SOURCE]`, `[TRACKER]`, `[NEW DESIGN PROPOSAL]`, etc.) are preserved unchanged inside Parts 1–7.

**Evidence chain (unchanged from V2):** authoritative requirement → historical sprint intent → tracker-attested implementation → code verification → recovered D-level → gap classification → PO decision / candidate work. V3 adds, after that chain and never in place of it: frontier research finding → competitor pressure → moat test → architecture proposal → candidate requirement → PO decision gate.

**How to read this file:** Parts 1–7 are V2 verbatim (the V2 header, status lines and gate are kept inside them). Part 8 is the V3 change log. Part 9 is the clerical correction. Parts 10–34 are the V3 extension, ordered to match the brief's required output A–AC (cross-reference table in Part 8). Part 35 is the final governance split required by brief §50. Sources are listed in Part 36.

---

# V2 BASELINE — PARTS 1–7 (PRESERVED VERBATIM; ONE CLERICAL CORRECTION IN PART 7, SEE PART 9)

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

Consequences recorded, not actioned: S48 T05 and S51 T04 corrections in Part 5a now have their governing decisions (D-04 and D-03 respectively); the S47 T04 correction (real Google STT adapter, G11/G12) is governed by brief Req 3, not by any Part 4 decision — D-05 governs the verdict-vocabulary conflict G06, which has no S47 ticket. *[V3 clerical correction 2026-10-04: the V2 text read "S48 T05, S51 T04, S47 T04 … (D-04, D-03, D-05)"; see Part 9.]* G29/G30/G31/G32/G34/G35 are closed as drift-to-be-corrected, not as requirement changes. No document or code has been modified as a result of this annex.

## Gate (V2, preserved)
Parts 2/2b, 3 and 7 constitute the frozen recovery baseline on approval of this correction pass. D-06 and D-15 remain open. Part 5b remains unscheduled. No architecture, sprint planning, requirement-document amendment or code work begins from this document.

---

# V3 EXTENSION

## Part 8 — V3 change log from V2 (brief output AB)

| # | Change | Nature | Touches Parts 1–7? |
|---|---|---|---|
| C-01 | Part 7 consequence sentence corrected: S47 T04 is not governed by D-05 | Clerical correction (brief §2) | Yes — one sentence, old text retained in brackets |
| C-02 | Gate heading retitled "Gate (V2, preserved)" so the V3 gate in Part 35 is distinguishable | Editorial | Heading only |
| C-03 | Parts 8–36 added | Extension | No |
| C-04 | Everything else in Parts 1–7 | Unchanged | — |

### Part 8A — V4 change log from V3 (independent review 2026-10-04 20:16; all ten corrections accepted)

| Review # | Sev. | V4 edit | Type |
|---|---|---|---|
| C01 | P1 | "44 Part 3 rows/capabilities" → **46** at every occurrence (Parts 11, 12, 33.1 E-01). 44 = recovered requirements R-01..R-44; 46 = Part 3 capability rows | CORRECT |
| C02 | P1 | Part 14: "cannot certify its own calls" replaced by the reliance/trust-advantage framing | CORRECT |
| C03 | P2 | Part 29.1: "Exactly the RFC 4998 ERS pattern" → ERS-style candidate architecture subject to E-02 | CORRECT |
| C04 | P2 | Parts 13.5 item 1 and 33.2 item 17(e): standardised preservation mechanism distinguished from operational/legal longevity | CORRECT |
| C05 | P1 | Part 32 preamble and D-22 reworded: CR text is candidate-grade; compressed CRs (e.g. CR-11) must be expanded to the full 19 fields after D-22 and before any FR/NFR ID | CORRECT |
| C06 | P2 | Part 31: 6–12-month headroom relabelled `FORECAST / HYPOTHESIS`, validated through R-A | RECLASSIFY |
| C07 | P2 | Part 36 note and new R-C: primary-source revalidation of standards/legal/high-impact market claims before any becomes a requirement | RESEARCH |
| C08 | P1 | New Part 29.4 and R-D: relying-party model (what a certificate proves vs does not) | ADD |
| C09 | P1 | New Part 29.5 and CR-23 candidate: certificate status / correction / supersession / revocation lifecycle | ADD |
| C10 | P2 | New R-E: trust-root governance, liability, indemnity, longevity obligations | RESEARCH |
| V4-meta | — | Header block, this Part 8A, Part 35 gate sequence; Part 36 note. No other text changed; Parts 1–7 untouched | METADATA |

**Brief output A–AC → V3 Part map:** A→10 · B→11 · C→12 · D→13 · E→14 · F→15 · G→16 · H→17 · I→18 · J→19 · K→20 · L→21 · M→22 · N→23 · O→24 · P→25 · Q→26 · R→27 · S→28 · T→29 · U→26 (autonomy ladder) · V→30 · W→31 · X→32 · Y→33 · Z→34 · AA→Part 32-D (diagrams) · AB→8 · AC→Part 33 (self-critique).

---

## Part 9 — Clerical correction (brief §2)

**Verified from V2 text (line 296 of the supplied file):** *"S48 T05, S51 T04, S47 T04 corrections in Part 5a now have their governing decisions (D-04, D-03, D-05)"*.

**Check against V2 itself:** Part 5a row S47 = *"T04 = real Google STT adapter; add tickets for diarisation + word-level confidence"* (gaps G11, G12). Part 4 D-05 = *"Verdict vocabulary (G06)"*. Part 7 D-05 = *"FR-040 vocabulary is canonical"*. G06's secondary note names D-05; G12's secondary note names S47 and brief Req 3, not any D-number. No Part 4 decision governs G11/G12.

**Correction applied:** the mapping S47 T04 → D-05 is removed. S48 T05 → D-04 and S51 T04 → D-03 stand. The S47 T04 correction is governed by brief Req 3 (real adapters), which is a `[USER REQUIREMENT — 2026-10-04]`, not a Part 4 decision. D-05 is left attached to G06 only. Nothing else in Parts 1–7 changed. `SOURCE REVALIDATION PENDING — INPUT NOT SUPPLIED` applies to whether the underlying tracker rows S47-T04 / S48-T05 / S51-T04 read as V2 quotes them; V3 has only the V2 text.

---

## Part 10 — Executive conclusion (brief output A)

One position, stated plainly:

1. **The V2 baseline stands.** Nothing in the October-2026 frontier changes a single recovered requirement, D-level, gap class or PO decision in Parts 1–7. What the frontier changes is *which of TalkProof's remaining work is worth doing first* and *what TalkProof must become to still be worth buying in 12–36 months*.

2. **Code generation is no longer the scarce thing; verified behaviour is.** `FRONTIER RESEARCH FINDING`: industry and academic sources in 2026 converge on "the bottleneck moved from writing to verification" (DORA 2026 as summarised in arXiv:2603.25773; InfoQ Sept 2026; Augment Code; Tessl Sept 2026). Frontier agents score 80–97% on single-issue benchmarks but under 30% on release-sized, multi-file evolution tasks (SWE-EVO best 25%; SWE-Marathon <30%; SWE-bench Pro top confirmed 81%). TalkProof's June-2026 build (22 modules in ~16 h, R-44) is exactly the kind of output that is now commodity. Its *verification* — D4–D7 evidence per capability — is not.

3. **The moat hypothesis survives only in a narrower form than the brief states.** "Verified organisational intelligence" is defensible *where it is bound to evidence a third party must trust* (certificates, provider behaviour under regulation, decision provenance that an auditor or court can replay). It is **not** defensible as a general "we learn and get cheaper" flywheel — RouteLLM/cascades, semantic caching, SLM distillation and agent memory are all commodity or ≤6 months from it (Part 15). The defensible core is: **evidence + regulation + provider history + decision provenance, kept verifiable after TalkProof, its providers, its models and its cryptography have all changed.** That is a trust-longevity moat, not an AI moat.

4. **The single most important thing the brief did not name:** long-term evidence preservation standards already exist and TalkProof's evidence thesis should be built on them rather than invented. RFC 4998 Evidence Record Syntax (archive-timestamp chains with hash-tree renewal), ETSI EN 319 102-1 long-term validation, and ETSI TS 119 312 V2.1.1 (June 2026) which now names a post-quantum timestamping suite, directly answer V2's four uncovered Part 2b areas (schema evolution, cryptographic agility, provider exit, verifier longevity) — see Part 29. Adopting them is `DIFFICULT TO REPRODUCE` for AI builders because it requires operating history, not code.

5. **The intelligence architecture in the brief (Parts 9–32 of the brief) is sound as an *execution discipline* and over-specified as a *product*.** Recommendation: build the Decision Ledger and the expected-vs-observed gap detector as *first-class product capabilities* (they are evidence); build the router, CRAG and learning loop as *internal platform modules with stable contracts* (they are cost control); do **not** build a Company Language Model until the ledger shows ≥ a measured volume of repeated semantic reasoning that deterministic rules and retrieval cannot absorb (Part 19 gives the gate).

6. **Autonomy ladder: A0–A4 are appropriate now across most capabilities; A5+ is appropriate for nothing that touches evidence, cryptography, authentication, consent or provider credentials.** Published AI-SRE benchmarks resolve ~14% of production-style failures (Augment Code 2026 guide citing the most rigorous published benchmark); vendor claims of 70–82% autonomous resolution are unverified. TalkProof should not be an early adopter of autonomous remediation on a proof product.

7. **What to decide next:** eleven new PO decisions (Part 34) and twenty-two candidate requirements (Part 32), none of which enters the baseline from this document.

---

## Part 11 — What V2 established and what remains historically unchanged (brief output B)

- Parts 1–7 are the frozen recovery baseline as approved 2026-10-04 19:18: Parts 2/2b and 3 approved; Part 7 PO decisions D-01..D-15 recorded; D-06 (HiL ordering) and D-15 (BRD-001) open; Part 5b unscheduled.
- V3 inherits unchanged: R-01..R-44; G01..G52; Part 2b's ten areas; the 46-row capability D-assessment (all rows `T`, tracker-attested, `CODE VERIFICATION PENDING`); D-01..D-15; the provider-neutral direction (D-03, D-07, D-13); the proof thesis (R-02, D-09 Option B); the evidence-binding scope (D-12).
- V3 does **not** reopen any of G29/G30/G31/G32/G34/G35 (closed as drift-to-be-corrected).
- V3 does **not** resolve D-06. Part 29 gives the evidence-chain analysis the PO asked for ("resolve during evidence-chain architecture") and presents the options with their consequences; the decision stays with the PO (Part 34, D-06 restated).
- V3 adds nothing to Part 5b and numbers no sprint. S60 remains the next free number (V2 numbering note); it is not used.

---

## Part 12 — Current code-verified state (brief output C)

`CODE VERIFICATION PENDING — REPOSITORY NOT SUPPLIED`

No repository was supplied with the V3 brief. V3 therefore has **zero** `CODE-VERIFIED` rows. The current state of record remains V2 Part 3 (46 capability rows, every row tracker-attested; not to be confused with the 44 recovered requirements) and the V2 provider inventory restatement ("13 seams / 6 hardcoded real / 5 correct", tracker-attested).

What V3 can add without repositories is the **verification plan** the brief's §46 requires, so that when the ZIPs arrive the inspection is mechanical rather than interpretive. For each of the 46 Part 3 rows the inspection must record one of: implemented-and-wired · implemented-not-integrated · partial · hard-coded · stub/mock · interface/seam only · test-only · configuration-only · absent · externally dependent · unable to verify; with file/module evidence; and must examine actual call path, configuration, provider invocation, error handling, persistence, tests, tenant isolation, security and telemetry. Rows where the tracker words themselves say "seam", "sandbox stub", "at deployment" or "carried-forward" (G03, G07, G13–G15, G19–G26, G28, G36, G49, G50) are the ones most likely to be *below* their V2 recovered level once code is read, because V2 took the team's own completion notes at face value; V3 does not pre-judge that.

Three specific checks the code pass must perform because V3 research makes them material (all `CODE VERIFICATION PENDING`):
- Whether any `os.environ` key read survives outside the S45 close conformance gate (V2 Part 5a S45 row).
- Whether M22's AI ledger records a model *version string* or only a model *name* (Part 2b "model reproducibility": V2 says name only; Part 21's Decision Ledger depends on this).
- Whether the certified payload `content_hash` is computed over a canonical serialisation with a declared algorithm identifier (needed for cryptographic agility, Part 29).

---

## Part 13 — October-2026 frontier research (brief output D)

All rows are `FRONTIER RESEARCH FINDING` unless marked `FORECAST`. Sources are numbered [S-nn] and listed in Part 36. Maturity scale: **Research** · **Early product** · **Production (vendor-claimed)** · **Production (independently evidenced)** · **Commodity**. "Advantage?" answers the brief's question: does adopting it create genuine advantage for TalkProof, or merely follow the market.

### 13.1 Software engineering frontier

| Area | What exists now (Oct 2026) | Maturity | Limitation | 6 / 12 / 24 / 36-month direction (`FORECAST`) | Relevance to TalkProof | Commoditisation | Advantage? |
|---|---|---|---|---|---|---|---|
| Coding agents | Frontier models 81–97% on single-issue benchmarks (SWE-bench Pro 81.2% Fable 5.1; Verified 97% Opus 5, now archived as saturated) [S-01][S-02] | Commodity for single-issue work | Release-sized evolution tasks: best 25% on SWE-EVO [S-03]; <30% on SWE-Marathon multi-hour tasks [S-04]; agents degrade over long iterative horizons [S-05] | 6m: long-horizon scores rise but stay well below single-issue; 12m: reliable multi-file feature work with spec + tests; 24m: release-scale evolution common with human gates; 36m: unknown | Explains R-44 (22 modules in 16 h) and G01 (DONE ≠ complete). Rebuilding TalkProof's code is cheap for any competitor | COMMODITY NOW | No. Follow the market; use them as the builder, as already done |
| Spec-driven development / executable specs | GitHub Spec Kit, Specmatic, OpenSpec, BMAD; executable specs as CI gates [S-06][S-07]; SDAD framework (May 2026) [S-08] | Early product → production | Specs as prose still need human intent; non-deterministic generation from spec [S-09] | 6m: standard practice in AI-first teams; 12m: spec conformance gates in mainstream CI; 24m: machine-readable requirement standards consolidate | Directly answers G02 (FR/NFR untraced) and G01: requirements must become executable conformance checks, not prose | ≤12 MONTHS | Partial. The *tooling* is commodity; the *content* (TalkProof's FR/NFR as executable checks) is TalkProof's own work and compounds |
| Verification-first engineering | "Verification is the new bottleneck" — DORA 2026 via [S-10]; InfoQ Sept 2026 [S-11]; Tessl Sept 2026 [S-12]; Augment [S-13] | Production (consensus) | Human review still the gate; AI reviewers inflate PR volume | 6–12m: AI verifiers (agent-as-judge) widely used but not trusted alone; 24m: verification evidence becomes a procurement artefact | Core to the whole V3 thesis | Tooling commodity; evidence not | Yes, if TalkProof *ships* its verification evidence to customers (Part 27) |
| Autonomous testing / mutation / fuzzing / property tests | Mature OSS; AI-generated tests mainstream; adversarial benchmark strengthening exposes inflated pass rates [S-05] | Commodity | AI-written tests that pass AI-written code prove little without independent oracles | 12m: adversarial/metamorphic testing by default | Needed for D4–D5 evidence on every adapter | COMMODITY NOW | No |

### 13.2 Operations, security, supply chain

| Area | What exists now | Maturity | Limitation | Direction (`FORECAST`) | Relevance | Commoditisation | Advantage? |
|---|---|---|---|---|---|---|---|
| AI SRE / AIOps / self-healing | Gartner Market Guide Jan 2026 treats AI SRE as a category; Resolve AI, Azure SRE Agent, AWS DevOps Agent, Datadog Bits, PagerDuty AI, NudgeBee, Komodor [S-14][S-15][S-16] | Production (vendor-claimed) | Most rigorous published benchmark: ~14% of production-style failures resolved [S-14]; vendor claims 70–82% unverified [S-17]; "self-healing → self-harming" guardrail problem [S-15]; telemetry manipulation attacks on AIOps [S-18] | 6m: approval-gated remediation normal; 12m: bounded autonomous actions on routine incidents; 24m: trust-scored agents with revocable authority common [S-16] | A0–A4 now; A5 only for restart/scale/rollback-class actions | Platform commodity ≤12 months | No for the agent; yes for the *incident/correction history bound to evidence* |
| AI AppSec / autonomous pentest / red-teaming | XBOW, Intruder, Escape, FireCompass, Horizon3, Wiz Red Agent, AWS security agent (GA Mar 2026) [S-19][S-20][S-21]; AI agents beat in-house researchers 60–70% on vendor benchmarks with <2% FP when exploit-validated [S-21] | Production | Hallucinated PoCs without deterministic validators; agents over-trust environment evidence (ATOBench) [S-22]; repair agents can be tricked into malicious patches that pass tests [S-23] | 6m: continuous AI pentest as a subscription norm; 12m: remediation PRs with proof-of-exploit standard | TalkProof should *buy* continuous pentest, not build it | COMMODITY ≤6 MONTHS | No |
| Software + AI supply chain | SLSA v1.1, in-toto, Sigstore/Rekor, CycloneDX ML-BOM, OWASP AIBOM, LF Model Signing [S-24][S-25]; EU CRA reporting from 11 Sept 2026, SBOM by Dec 2027 [S-26]; OWASP Agentic ASI04 mandates AIBOM [S-27] | Production | Signing proves publisher, not distribution path [S-28]; AIBOM tooling immature for agent skills [S-29] | 12m: AIBOM expected by auditors; 24m: CRA makes SBOM legally mandatory | Answers Part 2b "AI supply-chain provenance": build-time attestation of what generated deployed behaviour | Tooling commodity | Partial — the attestation *content* for a proof product is differentiating |
| Agent governance / runtime containment | OWASP Top 10 for Agentic Applications 2026 (ASI01–ASI10) [S-27][S-30]; Microsoft Agent Governance Toolkit (Apr 2026); NIST CAISI AI Agent Standards Initiative and agent identity draft (Feb 2026) [S-31]; policy-as-code runtime frameworks (MI9, Policy Cards, deontic policies) [S-32][S-33] | Early product → production | Standards still drafts; per-agent identity and short-lived credentials not yet universal | 6m: OWASP ASI mapping expected in security questionnaires; 12m: NIST agent identity guidance final; 24m: ISO 42001 audits routinely cover agents [S-34] | Mandatory for any A3+ capability | Frameworks commodity | No; non-compliance is a disqualifier |
| Continuous compliance / evidence-as-code | Vanta, Drata, Secureframe: hourly/daily automated control tests, ISO 42001 mapped, auditor portals [S-34][S-35]; AICPA Mar 2026 FAQ calls them efficiency aids, not auditors [S-36] | Commodity | Software cannot issue the opinion; collects configuration evidence, not product-level evidence | 12m: agent-governance evidence (ISO 42001) routine | TalkProof's *product* must emit control evidence (consent, DNC, retention, model provenance) that these platforms can ingest | COMMODITY NOW for infra evidence; not for product evidence | Partial |

### 13.3 Intelligence, retrieval, models, cost

| Area | What exists now | Maturity | Limitation | Direction (`FORECAST`) | Relevance | Commoditisation | Advantage? |
|---|---|---|---|---|---|---|---|
| Model routing / cascades | RouteLLM, FrugalGPT, AutoMix, RLCascadeRouter, LLMRouterBench (ACL 2026); surveys Mar 2026 [S-37][S-38]; practitioner reports 45–85% cost cut at ~95% quality [S-39] | Production | Confidence estimation unreliable; high-risk queries mis-routed by price; batch/capacity constraints [S-40] | 6m: gateway-native routing default; 12m: built into every AI gateway | Brief Part 12 router is a commodity component | COMMODITY NOW | No |
| Semantic caching / AI gateways | Portkey, TrueFoundry, LiteLLM, etc.; semantic cache 60%+ savings on repetitive workloads [S-39] | Commodity | Cache staleness vs policy/version changes — exactly brief Part 19's invalidation list | — | Use, don't build | COMMODITY NOW | No |
| SLM fine-tuning / distillation | 7B fine-tune < $5 compute, hours [S-41]; 10–30× cheaper serving [S-42]; distil-frontier-into-SLM is the strongest 2026 fine-tune case [S-43] | Production | Needs labelled verified data; modality collapse with poor data [S-44]; RAG remains default for ~80% of apps [S-43] | 12m: per-task SLMs routine where volume justifies | Only justified after Decision Ledger shows repeated semantic reasoning (Part 19 gate) | Commodity technique | No as a technique; data is the only edge |
| RAG / GraphRAG / temporal graphs / agent memory | Microsoft GraphRAG v3.1 (May 2026); Zep/Graphiti bi-temporal graphs; temporal RAG (STAR-RAG, MemoTime WWW'26) [S-45][S-46][S-47]; KG-RAG on regulations +70% accuracy over vector RAG [S-48]; 2026 academic turn toward determinism, provenance, keeping contradictions live [S-49] | Production (graph memory early) | LLM-extracted graphs are lossy and non-reproducible; auto-invalidation of facts by an LLM is contested [S-49]; cost of extraction at corpus scale | 12m: bi-temporal provenance graphs standard for agent memory; 24m: deterministic traversal preferred for audit | Validates brief Part 10's "don't put everything in embeddings" and Part 37's temporal-provenance question | Tooling commodity | Partial — regulatory/provider history with validity intervals is TalkProof-specific |
| Agent observability / decision tracing | OpenTelemetry GenAI semantic conventions (gen_ai.* spans: invoke_agent, chat, execute_tool; token usage; MCP conventions v1.39) [S-50][S-51]; moved to own repo June 2026, still Development, no release as of Aug 2026 [S-52]; OpenInference competing | Production (conventions evolving) | Gateway sees model traffic, not planning/retrieval; content capture is a privacy decision | 6–12m: first stable release | **The Decision Ledger schema should extend OTel GenAI, not invent fields** (Part 21) | Commodity transport | No as transport; yes as bound evidence |
| Verifiable inference (zkML, re-execution, TEEs) | Full GPT-2 proof (DeepProve-1, Aug 2025); layerwise/sampled proofs to 70B-scale traces (NanoZK Jul 2026; Seal-Then-Sample Sept 2026) [S-53][S-54]; restaking re-execution (EigenAI, VeriLLM) [S-55] | Research → early product | Orders of magnitude above inference cost; model architecture disclosed; hosted frontier providers do not offer it | 12m: sampled audits practical for small open models; 24m: possibly for a verification SLM; 36m: unknown for frontier APIs | Answers "model reproducibility" only if TalkProof's *verification* model is open-weight and self-hosted | Not commodity | `EXPERIMENT REQUIRED` — potentially a genuine differentiator for certified verdicts |

### 13.4 Evidence, trust, regulation (the areas the brief under-weighted)

| Area | What exists now | Maturity | Limitation | Direction (`FORECAST`) | Relevance | Commoditisation | Advantage? |
|---|---|---|---|---|---|---|---|
| Long-term evidence preservation | RFC 4998 Evidence Record Syntax (archive-timestamp chains, hash-tree renewal before algorithms weaken); RFC 6283 XMLERS; ETSI EN 319 102-1 LTV with proofs of existence [S-56][S-57] | Standard, decades old, under-used | Needs a qualified TSA and operational renewal discipline | Unchanged standards; renewal cycles become PQ-driven | **Resolves V2 Part 2b: schema evolution, crypto agility, provider exit, verifier longevity** (Part 29) | Not commodity (operational) | **Yes — compounding** |
| Post-quantum timestamping / signatures | ETSI TS 119 312 V2.1.1 (June 2026) names hybrid and PQ timestamping suites (ECDSA/EdDSA + SLH-DSA); hybrid ML-DSA-65 in PAdES demonstrated [S-58]; EU PQC roadmap: inventories by end-2026, high-risk migration by 2030 [S-59]; Google/Cloudflare 2029 deadlines [S-59] | Standards final; qualified PQ TSAs not yet operating [S-58] | No qualified PQ TSA in production | 12m: first PQ TSAs; 24m: hybrid tokens expected for long-lived evidence; 36m: classical-only tokens questioned | Every TalkProof certificate is long-lived evidence; crypto agility is not optional | Not commodity | Yes |
| Media provenance (C2PA / Content Credentials) | C2PA 2.3 (Jan 2026); CAWG 1.2; 6,000+ members; Pixel 10 native; Microsoft 365 signing (Feb 2026); audio in scope [S-60][S-61]; Android C2PA forgery demonstrated Aug 2026; no desktop app conformant as of mid-2026 [S-62]; MerkleSpeech chunk-localised speech provenance (Feb 2026) [S-63] | Production, uneven | Implementation vulnerabilities; absence of credential proves nothing; telephony audio is not captured by C2PA devices | 12m: EU Code of Practice pushes C2PA for AI-generated audio; 24m: provenance at capture becomes expected for recordings | TalkProof should *emit* C2PA manifests for recordings/transcripts it certifies and *verify* incoming ones; chunk-level commitments answer redaction-vs-integrity | Format commodity | Partial — interoperability, not moat |
| EU AI Act Article 50 | Applies from 2 Aug 2026; Commission guidelines (20 Jul 2026) and Transparency Code of Practice (June 2026) confirmed adequate; extraterritorial; deployers of AI interacting with people must disclose; machine-readable marking of AI-generated audio; fines to €15m/3% [S-64][S-65][S-66] | Enforceable now | Deployer vs provider roles depend on tenant set-up | Dec 2026: Art 50(2) grace ends; 2027: high-risk obligations | D-09 Option B capability (AI-originated interactions) is now a regulated capability; evidence must bind the disclosure | Compliance commodity | Regulatory-history value compounds |
| US TCPA / FCC on AI voice | FCC Feb 2024: AI voice = artificial voice; $500–$1,500/call; consent must be linked to number and retrievable at call time; Fifth Circuit Feb 2026 narrowed written-consent requirement for some states; FCC AI-disclosure NPRM pending; KYUP vetting rules May 2026; 12 all-party-consent states; consent records retained ≥5 years [S-67][S-68][S-69] | Enforceable, moving | Circuit split; state patchwork | 12m: FCC AI disclosure rule likely final (`FORECAST`) | Validates FR-078/G36 and the consent-binding thesis (R-35); regulation-version provenance (Part 2b) is now unavoidable | — | Regulatory-history value compounds |
| STT diarisation / word confidence | AssemblyAI Universal-3.5/3.6 Pro lead published cpWER (30–35 avg on DiPCo/NOTSOFAR) and 5.19% realtime WER; Deepgram Nova-3/Flux; Google Gemini 3.5 Transcribe Live; ElevenLabs Scribe v2; Voxtral; GPT-4o Transcribe [S-70][S-71][S-72] | Commodity, fast-moving | Benchmarks vendor-run; accented/noisy audio 75–90%; diarisation remains the weakest metric | 6–12m: provider rankings reorder repeatedly | Confirms R-11 (diarisation + confidence are outputs) and D-13: provider selection must be configurable, and *provider-version provenance per transcript* is evidence | COMMODITY NOW | No for STT; yes for recorded provider-behaviour history |

### 13.5 Important 2026 approaches the brief did not name (brief §3 "search for what we have not thought of")

1. **Evidence Record Syntax / archive-timestamp renewal (RFC 4998, ETSI EN 319 102-1).** The brief treats "evidence longevity" and "cryptographic agility" as research questions; the *preservation mechanisms* are standardised. What is not solved by a standard is operational and legal longevity — who operates renewal for decades, under what obligations and liability (C04; see R-E). This is the biggest omission.
2. **Chunk-localised media commitments (MerkleSpeech-style perceptual-fingerprint Merkle commitments; C2PA/CAWG for audio).** Lets a redacted recording remain partially verifiable — the concrete answer to "redaction vs integrity".
3. **Executable-specification conformance gates as the bridge between FR/NFR and tests (G02).** Spec-driven tooling has matured enough that "requirement conformance" in brief §6 can be a CI artefact, not a document.
4. **OpenTelemetry GenAI semantic conventions as the base schema for the Decision Ledger.** Avoids inventing a proprietary trace format and makes the ledger exportable to any observability backend.
5. **OWASP Agentic ASI01–ASI10 as the threat model for brief Parts 8/21.** "Memory & context poisoning (ASI06)" is precisely the risk in the knowledge-promotion loop (Part 23); "cascading failures (ASI08)" is the risk in self-correction.
6. **EU CRA SBOM mandate (Dec 2027) and EU AI Act Art 50 (Aug 2026) as external-awareness triggers already dated.** External awareness (brief §33) has concrete first targets.
7. **Sampled layerwise verifiable inference** as a 24–36-month path to "the verdict was produced by the model we say it was" — only meaningful if the verification model is open-weight and self-hosted (links to D-13 and the CLM decision).
8. **Bi-temporal provenance graphs that keep contradictions live** (2026 academic direction) — the correct model for TalkProof's own requirement contradictions (G09, G10, G16, G29…): record both, with validity intervals, never auto-resolve.
9. **The verification bottleneck as the procurement artefact.** If buyers increasingly ask "show me the evidence it works", a continuously generated capability scorecard (brief §35) is sales collateral, not only governance.

---

## Part 14 — The competitor TalkProof will face (brief output E)

`MARKET FACT` where cited; otherwise `HYPOTHESIS`. V2 G46/G47 remain RESEARCH; this Part gives the model the brief asked for and does not restate V1's withdrawn "80–90% reproducible" figure as fact.

| Competitor | Who they are in 2026 | What they can reproduce of TalkProof | What they cannot easily reproduce | Time to a credible TalkProof-like product (`FORECAST`) |
|---|---|---|---|---|
| C1 Traditional SaaS vendor (CCaaS / call-recording / compliance recording) | Incumbents adding AI summaries, QA scoring, consent capture | UI, workflows, dashboards, carrier integrations, STT, summaries | Three-model consensus bound into a certificate with TSA+anchor; independent verification; evidence longevity | Already partially there; 6–12 months to add "certified" marketing claims without the evidence depth |
| C2 AI-native startup | Voice-agent and conversation-intelligence startups on frontier APIs | Everything C1 can plus multi-model voting, RAG, routing, agent workflows | Regulatory and provider operating history; human-reviewer provenance at scale; long-term evidence operations | 3–6 months to feature parity on paper |
| C3 Enterprise internal engineering + AI | Retool report: 35% of enterprise teams have replaced at least one SaaS tool with a custom build; 78% expect to build more in 2026 [S-73]; Klarna-style replacements [S-74] | Internal recording + transcript + LLM check tool for their own compliance team | Independent reliance: evidence an enterprise creates and controls about its own conduct carries less weight with a counterparty or regulator than independently operated, independently verifiable evidence; qualified TSA relationships; third-party verifier | 2–8 weeks for an internal tool; independent-operator trust is not something it can build for itself |
| C4 Consultancy + coding agents | SI/consultancy delivering "built for you" with agents | A bespoke TalkProof clone per client | Multi-tenant operating history; continuous assurance after hand-over | 2–4 months per clone; maintenance decays |
| C5 Solo / small expert team + AI | Exactly TalkProof's own origin (R-44) | The whole codebase at the D3 level TalkProof itself reached in June 2026 | D5–D7 evidence; provider conformance; evidence operations | Weeks to D3; months–years to D7 |
| C6 AI-generated custom software | "Describe it, get it" platforms (Lovable, Vercel, enterprise AppGen) [S-73][S-75] | Prototype-grade proof tool | Counter-evidence: "shipping v1 is 2% of the work" [S-76]; systems of record and regulated workflows resist [S-77] | Days to a demo; not a substitute for a system of record |
| C7 Continuously maintained autonomous software | The brief's full loop (idea → requirements → … → continuous evolution) | In principle everything | In practice, 2026 evidence: long-horizon autonomy <30% [S-03][S-04]; AI SRE ~14% on hard benchmark [S-14]; spec fidelity loss over long horizons [S-05]; governance frameworks still drafts [S-31] | 24–36 months before C7 is an unsupervised reality for regulated software (`FORECAST`, low confidence) |

**"If customers can obtain this capability cheaply, why should TalkProof still exist?"** — one answer, not "more features":

> Because **independent operation and independently verifiable evidence can carry more trust with relying parties than evidence controlled solely by the party whose conduct is being proved** (C02 wording; the earlier V3 phrasing "cannot certify its own calls" was too absolute — an enterprise can create and retain evidence about its own interactions). Certification is a relationship between the certified party, the relying party and an independent operator who holds the keys, the TSA/anchor relationships, the reviewer provenance, the regulation-version history and the renewal obligations for as long as the evidence must stand. Code is the cheapest part of that. C3–C6 can build the tool; what they cannot build for themselves is the independent-operator standing that gives a relying party reason to prefer the evidence (see Part 29.4, relying-party model — `RESEARCH REQUIRED` R-D). C1–C2 can be independent operators but have not accumulated the evidence operations; the window is the time it takes them to do so, which the frontier shortens for code and does not shorten for operating history.

That answer is only valid if TalkProof actually operates evidence (TSA, anchoring, renewal, verifier) — all of which V2 recorded at **D1–D3** (G07, G43, R-06). It is a thesis TalkProof has not yet earned. This is why Part 31 puts trusted-time and evidence-record completion at the top of headroom, ahead of every intelligence feature.

---

## Part 15 — Commodity vs moat assessment (brief output F, brief §5)

Classes: `COMMODITY NOW` · `COMMODITY ≤6 MONTHS` · `COMMODITY ≤12 MONTHS` · `DIFFICULT TO REPRODUCE` · `COMPOUNDING ADVANTAGE`. "Basis" cites Part 13 rows. Where the class depends on TalkProof first doing something it has not done, the condition is stated.

| Area | Class | Basis / condition |
|---|---|---|
| Code | COMMODITY NOW | 13.1 coding agents; R-44 |
| UI | COMMODITY NOW | 13.1 |
| Ordinary workflows | COMMODITY NOW | 13.1; C1–C6 |
| Dashboards | COMMODITY NOW | — |
| Provider adapters | COMMODITY ≤6 MONTHS | Writing them is cheap; *conformance-tested* adapters with recorded provider behaviour move to the "provider behaviour history" row |
| Integrations | COMMODITY NOW | — |
| AI summaries | COMMODITY NOW | 13.3 |
| Multi-model voting | COMMODITY NOW | Cascades/ensembles are standard; the *binding of the vote into a certificate* is not |
| RAG | COMMODITY NOW | 13.3 |
| Configuration (tenant/provider config through product, D-13) | COMMODITY ≤12 MONTHS | Product work, reproducible; necessary, not differentiating |
| Operational history | DIFFICULT TO REPRODUCE | Only once accumulated; TalkProof has little today (no live tenants attested) |
| Verified decision history | COMPOUNDING ADVANTAGE — *conditional* | Requires the Decision Ledger (Part 21) and outcome verification; without outcome labels it is just logs |
| Evidence provenance | COMPOUNDING ADVANTAGE — *conditional* | Requires D-12 bindings implemented and ERS-style preservation (Part 29) |
| Cryptographic trust (TSA + anchor + agility) | DIFFICULT TO REPRODUCE | Operational relationships, renewal cycles, PQ migration; currently D1 (G07) |
| Independent verification | DIFFICULT TO REPRODUCE | Verifier that outlives TalkProof (FR-055 is PDF-level only, Part 2b) |
| Compliance intelligence | COMMODITY ≤12 MONTHS for *checks*; COMPOUNDING for *regulation-version history bound to decisions* | 13.2, 13.4 |
| Regulatory history | COMPOUNDING ADVANTAGE | Each certified decision records the regulation/policy version in force (Part 2b partial) |
| Incident / failure knowledge | DIFFICULT TO REPRODUCE | Only from real operation |
| Provider behaviour history | COMPOUNDING ADVANTAGE | Per-provider, per-version latency/error/drift under real traffic is unavailable to new entrants and is itself evidence for certificates (which STT version transcribed this call) |
| Interoperability (C2PA, OTel GenAI, CycloneDX) | COMMODITY ≤12 MONTHS | Adopt standards; no edge in inventing |
| Migration capability | COMMODITY ≤12 MONTHS | Runtime switching exists (R-41); evidence-preserving migration is the hard part (next row) |
| Evidence longevity | DIFFICULT TO REPRODUCE | RFC 4998 operations; renewal obligations |
| Customer policy history | COMPOUNDING ADVANTAGE | Tenant policy versions bound to decisions |
| Continuous assurance | COMMODITY ≤12 MONTHS for infra; DIFFICULT for product-level | 13.2 compliance automation |
| Self-awareness (expected vs observed) | COMMODITY ≤12 MONTHS as pattern; DIFFICULT as *populated* model | Pattern is drift detection; the populated requirement→code→test→runtime graph is TalkProof's own |
| Governed self-correction | COMMODITY ≤12 MONTHS (AI SRE platforms) | 13.2 |
| Verified organisational intelligence | **Defensible only as the union of the rows marked COMPOUNDING above** | See verdict |

**Verdict on the moat hypothesis** (brief §5: "Do not assume it is"):

- As stated in the brief — *"accumulates verified organisational intelligence … and moves verified learning into a cheaper/faster intelligence layer"* — the hypothesis **fails** as a moat. The "moving learning into cheaper layers" half is routing + caching + distillation, all commodity (Part 13.3). Any competitor with traffic gets the same cost curve.
- Restated — *"accumulates evidence-bound, independently verifiable decision history under recorded regulatory, provider and model conditions, and keeps it verifiable through cryptographic, provider and model change"* — the hypothesis **holds**, because (a) it needs operating time that frontier tooling does not compress, (b) it needs an independent operator role that self-builders cannot occupy, and (c) it accrues per certified interaction.
- Fragility: this moat disappears if TalkProof never reaches D5+ on TSA/anchor/verifier, or if tenants never go live. It is a moat that must be *earned by operating*, and the brief's intelligence architecture is justified only insofar as it feeds it.

---

## Part 16 — Product State Model (brief output G, brief §6 and §37)

`ARCHITECTURE PROPOSAL` throughout; nothing here is a requirement.

### 16.1 Name research (brief §6 last line)
Established names for "a machine-readable model of what a product should be, is, and has been":
- **Digital twin** (engineering; software/system digital twins are an active 2026 research area) — accurate for the *runtime* half, misleading for the *intent* half.
- **Ontology / operational ontology** (Palantir-style) — accurate for the relationship model, carries vendor connotations.
- **Model-based systems engineering (SysML v2)** — accurate for intent→architecture→verification traceability; heavy for a SaaS.
- **Software catalog / service catalog (Backstage)** — covers implementation inventory only.
- **System of record for engineering intent / "spec as system of record"** (2026 SDD literature, Jama) [S-07][S-13] — closest to the intent half.
- **Provenance graph / bi-temporal knowledge graph** (Zep/Graphiti; 2026 academic turn) — the storage pattern, not the model.

**Position:** keep the working name **Product State Model (PSM)** internally; describe it externally as *"a bi-temporal provenance model of product intent, implementation, verification, runtime and evidence"*. No single established name covers all nine of the brief's domains; inventing a marketing name is unnecessary.

### 16.2 Minimal entity model (relationships from brief §37)

```text
Requirement(id, text, version, source_doc, source_version, status, valid_from, valid_to)
  └─governs→ Policy(id, version, jurisdiction?, tenant?)
  └─realised_by→ Capability(id, D_target, D_actual, D_evidence_ref)
       └─implemented_in→ Component(repo, module, version, commit)
            └─covered_by→ Verification(kind: unit|integration|contract|e2e|property|mutation|fuzz|perf|security|provider|compliance|evidence-integrity, result, evidence_ref, run_at)
            └─deployed_as→ Deployment(env, version, config_hash, iac_ref, at)
                 └─uses→ ProviderBinding(provider, api_version, capability_set, status, tenant_config_version)
                      └─observed_in→ RuntimeObservation(metric|log|trace|health, window)
Decision(id = Decision Ledger row, see Part 21)
  ├─made_under→ Requirement/Policy versions in force
  ├─used→ KnowledgeVersion(kind: rule|crag-doc|clm-model|frontier-model, version, provenance)
  ├─cost→ CostRecord · latency→ LatencyRecord
  ├─produced→ Outcome(correct|wrong|partial|missed|uncertain|unknown, verified_by, at)
  ├─linked_to→ Incident(id) ─caused→ Correction(id, attempted|succeeded|failed|rolled_back)
  └─yields→ LearningCandidate(id) ─promoted_to→ KnowledgeVersion
EvidenceRecord(cert_id, hashes[], algorithm_ids[], tsa_tokens[], anchors[], ers_chain[], schema_version, verifier_version)
```

Every entity is **bi-temporal** (valid-time + record-time) so that "what was true when this certificate was issued" is a query, not a reconstruction. Contradictions (G09, G10, G16, G29…) are stored as two Requirement rows with overlapping validity and a `Conflict` edge, never collapsed (Part 13.5 item 8).

### 16.3 Storage decision (brief §10 "determine what belongs where")

| Data | Store | Why |
|---|---|---|
| Requirements, policies, capabilities, components, deployments, provider bindings, tenant config, decisions, outcomes, costs | **Relational (Postgres), versioned rows** | Deterministic, auditable, already TalkProof's stack (Alembic-managed) |
| Deployments, incidents, corrections, promotions, provider status changes | **Append-only event store** (Postgres table or dedicated) | Immutable history; replayable |
| Runtime metrics/traces | **Time-series + OTel backend** (existing FR-074 endpoints) | Not the PSM's job to store raw telemetry; PSM stores *summaries and links* |
| Relationship traversal (requirement → test → deployment → decision) | **Graph *projection* over the relational tables** (recursive SQL first; a graph DB only if traversal cost proves it, `EXPERIMENT REQUIRED`) | Brief §37: "do not use a graph merely because graphs are fashionable"; 2026 evidence favours deterministic traversal for audit [S-49] |
| Documents (ADRs, provider docs, regulations, runbooks) | **Document store + vector index with provenance metadata** (CRAG, Part 19) | Retrieval, not truth |
| Evidence artefacts (recordings, transcripts, PDFs, tokens) | **Object store with Object Lock** (FR-054(6)) | Existing requirement |

**Position:** the PSM is Postgres-first. No new database categories are introduced until a measured need exists. This directly serves brief §37 ("do not build disconnected databases for each idea").

---

## Part 17 — Expected state ↔ observed state (brief output H, brief §7) and self-awareness

`ARCHITECTURE PROPOSAL`.

```text
EXPECTED (from PSM)                          OBSERVED (from the world)
 Requirement/Policy versions                  Code: repo state, SBOM, AIBOM, commit
 Capability D-targets                         Verification: last run results per kind
 Architecture invariants (ADRs)               Deployment: running versions, config hash
 SLOs (NFR latency/availability)              Runtime: OTel metrics/traces/health
 Security baseline (CVE policy, headers)      Security: scanner/pentest findings, CVE feed
 Compliance rules (consent, DNC, retention)   Compliance: per-tenant evidence counters
 Evidence rules (FR-054 steps, D-12 bindings) Evidence: certificate integrity re-checks
 Cost expectations (per-call/per-tenant)      Cost: ledgers (Part 21)
 Provider contracts (capabilities, versions)  Providers: health, version headers, deprecations
            │                                            │
            └──────────────► GAP DETECTOR ◄──────────────┘
                 (deterministic comparators per gap type; no LLM in the comparator)
                                   │
                    Gap(id, type, severity, affected capabilities/tenants/evidence,
                        expected_ref, observed_ref, detected_at, detector_version)
```

**Gap types** (brief §7 list) and the comparator that detects each — all deterministic:

| Gap type | Comparator |
|---|---|
| Requirement drift | Executable-spec conformance check fails for a requirement (G02 resolved via Part 13.5 item 3) |
| Implementation defect | Verification result ≠ pass for a capability whose D-actual claims it |
| Configuration drift | Deployed config hash ≠ declared config hash |
| Documentation drift | ARCH/ADR version referenced by a component older than component's commit (G51 is an instance) |
| Architecture drift | Dependency/call graph violates a declared invariant (e.g., a provider call outside an adapter — S45 close gate) |
| Provider degradation / API drift | Provider conformance test fails; version header changes; deprecation notice |
| Performance / reliability regression | SLO comparator over OTel metrics |
| Security vulnerability | CVE feed ∩ SBOM; scanner finding above policy |
| Compliance drift | Per-tenant counter (e.g., calls without linked consent) > 0 |
| AI/model drift | Evaluation-set score drop per model version; verdict distribution shift |
| Evidence-chain failure | Scheduled re-verification of certificates fails (hash/TSA/anchor) |
| Cost anomaly | Ledger cost per capability outside expected band |
| Knowledge staleness | CRAG document validity_to < now; regulation version superseded |
| Quality regression | Quality Ledger (Part 21) wrong/missed rate rises for a route |

**Self-awareness** is nothing more than: the PSM is populated, the comparators run on an execution policy (Part 24), and every Gap is itself a ledger row. No LLM is required to *detect*; LLMs enter only at *diagnose* (Part 26, A1+).

---

## Part 18 — Company Intelligence architecture (brief output I, brief §9)

`ARCHITECTURE PROPOSAL`. The brief's initial hypothesis (deterministic → cache → CRAG → verified history → CLM → frontier → verification) was tested against Part 13.3.

**What research changes in the order:**
- "Verified historical decisions" belongs **inside** the deterministic layer when the match is exact (same tenant, same policy version, same provider version, same input fingerprint) and **inside** CRAG when it is semantic. It is not a separate rung.
- "Cache" splits: exact cache is deterministic; semantic cache is a retrieval technique with the same invalidation rules as CRAG (brief §19). Treating semantic cache as "safe" is where production systems leak stale answers [S-39].
- "CLM" is **not a rung by default** (Part 19): the layer is "task model portfolio", which may contain zero fine-tuned models.
- A **risk-class gate** must sit *before* the ladder, not after: high-assurance capabilities (verdicts, consent, certification) skip to the policy-mandated route regardless of cost (brief §12, §14).

**Resulting hierarchy:**

```text
REQUEST / EVENT  ──► RISK-CLASS GATE (deterministic: capability × tenant policy × evidence sensitivity)
                              │
            ┌─────────────────┴──────────────────┐
     LOW/MEDIUM RISK                       HIGH ASSURANCE / REGULATED
            │                                     │
 0 DETERMINISTIC (rules, SQL, PSM, exact          0 DETERMINISTIC
   cache, exact verified-decision reuse)          │
            │ miss                                 │ miss
 1 RETRIEVAL (CRAG; semantic cache; semantic      1 RETRIEVAL (citations mandatory)
   verified-decision reuse) ─► small generic      │
   model to compose IF needed                     │
            │ miss / low confidence                │
 2 TASK MODEL PORTFOLIO (classifiers, SLMs,       2 POLICY-MANDATED MODEL SET
   fine-tuned only where Part 19 gate passed)       (e.g. FR-040: 3 models, ≥2 providers)
            │ miss / low confidence                │
 3 FRONTIER LLM                                   3 FRONTIER LLM (as one of the mandated set)
            │                                     │
            └─────────────► VERIFICATION ◄────────┘
                   (deterministic checks; schema; citation presence; HiL where policy says)
                              │
                       DECISION LEDGER ROW (Part 21)
```

**Principle preserved from the brief:** use deterministic truth whenever it exists. **Principle added:** the FR-040 verdict path is *not* a cost-optimised cascade and must never become one — D-04 and R-03 fix it as a policy-mandated set with HiL fallback. Cost optimisation applies to TalkProof's *own* operational intelligence (support, diagnosis, routing, classification, summaries), not to the certified verdict.

---

## Part 19 — CRAG, CLM and model-portfolio recommendation (brief output J, brief §10–§11)

### 19.1 CRAG (Company RAG) — what goes where
Already decided in Part 16.3: structured truth stays relational; documents go to a document store with provenance metadata and a vector index; nothing enters CRAG without `source, source_version, valid_from, valid_to, tenant_scope, authority_level, ingested_at, content_hash`. Regulatory material gets a **validity interval and supersession edge** (temporal RAG, [S-48]) so that "the rule in force on date X" is answerable. Retrieval audit: every retrieval writes `(decision_id, doc_ids[], versions[], scores[])` to the Decision Ledger. Tenant isolation: tenant-scoped documents are in tenant-partitioned indexes; cross-tenant retrieval is structurally impossible, not policy-filtered.

**Position on GraphRAG:** not now. Start with relational + vector + supersession edges in SQL. `EXPERIMENT REQUIRED` E-03 (Part 33) tests whether multi-hop questions over requirements/provider/regulation history exceed what recursive SQL answers.

### 19.2 CLM / model portfolio — the economic gate
The brief asks for `training + fine-tuning + inference + hosting + hardware + evaluation + refresh + operations` versus frontier savings and quality effect. Without a Decision Ledger there is **no data** to fill the left side; the honest answer today is a gate, not a number.

**Gate (all must hold before any fine-tune is proposed):**
1. Decision Ledger shows ≥ N decisions/month in one capability routed to frontier **after** deterministic and retrieval misses (N to be set by PO; suggested starting point: the volume at which frontier cost for that capability exceeds one month of a hosted 7B serving cost — `EXPERIMENT REQUIRED` E-04 computes it).
2. ≥ 80% of those decisions have **verified outcomes** (not AI-labelled) — otherwise there is no training set, only guesses.
3. The capability is **not** certification-critical (FR-040 verdicts are excluded; D-04).
4. A held-out evaluation set with regression tests exists before training starts.
5. Rollback to the previous route is a configuration change.

**Portfolio shape when the gate passes (`FORECAST` of what will pass first):** small classifiers (incident type, support intent, provider-error class) → a routing classifier → at most one distilled SLM for operational troubleshooting/summarisation. A single "Company Language Model" is `REJECTED` as a goal: 2026 evidence favours per-task small models plus retrieval over one domain model [S-43][S-42], and continued pre-training is "rarely justified" [S-43].

**Cost sketch (illustrative, `MARKET FACT` ranges from Part 13.3):** 7B fine-tune compute < $5/hour-scale [S-41]; serving 10–30× cheaper than frontier [S-42]; the real costs are evaluation, refresh and operations, which are people-time. For TalkProof's current volume (no live tenants attested in V2) the gate cannot pass. The CLM question is therefore `DEFERRED` with a reopen trigger, not rejected.

---

## Part 20 — Intelligence Router (brief output K, brief §12)

`ARCHITECTURE PROPOSAL`. The router is a **deterministic policy function**, versioned, with inputs exactly as the brief lists (deterministic solvability, cache validity, freshness, complexity, uncertainty, risk, tenant, privacy, latency, required accuracy, budget, provider/model capability, regulatory sensitivity, evidence sensitivity) and output `(route_plan, policy_version, reasons[])`. Complexity/uncertainty scoring may use a small classifier; the *decision* is rule-based so it is replayable.

Rules the router enforces that no tenant policy can relax (brief §14): FR-040 model set and vendor-down behaviour (D-04); consent/DNC checks (FR-078); evidence bindings (D-12); any A5+ action gate (Part 26). Rules it will follow from tenant policy: economy/balanced/premium ordering; freshness tolerance; latency budget; permitted model list; monthly budget with governed fallback (brief §21).

Research position: build on an AI gateway's routing primitives (commodity, Part 13.3) and keep the policy function in TalkProof. Do not train a learned router (RouteLLM-style) until the ledger supplies preference data; even then, learned routing is confined to low-risk capabilities.

---

## Part 21 — Decision, Quality and Cost Ledgers (brief output L, brief §13, §15, §16, §20)

`ARCHITECTURE PROPOSAL`, with one `DERIVED REQUIREMENT` flagged below.

**Schema base:** OpenTelemetry GenAI semantic conventions (gen_ai.* attributes; `invoke_agent`, `chat`, `execute_tool` spans; token usage; MCP conventions) [S-50][S-51]. Status: Development, no stable release as of Aug 2026 [S-52] — so TalkProof pins a convention version in the ledger row (`otel_genai_semconv_version`) and maps forward. The Decision Ledger row is **an OTel trace + TalkProof extension attributes**, persisted (not sampled) for every `decision_id`, with content capture governed by tenant policy and privacy (span events, not attributes [S-50]).

**TalkProof extension attributes (brief §13, grouped):**
- identity: `decision_id, tenant, workflow, capability, agent, request_fingerprint, risk_class`
- route: `routing_policy_version, tenant_policy_version, route_plan[], deterministic.{attempted,result}, cache.{attempted,kind,result}, crag.{attempted,doc_ids,versions,scores,confidence}, history.{reused_decision_id}, portfolio.{model,version,confidence}, frontier.{provider,model,version,prompt_version}`
- cost: `tokens.{input,output,cached}, cost.{retrieval,embedding,rerank,portfolio,frontier,tool,infra_attributed}, latency.{per_stage[],total}, retries`
- result: `decision, confidence, verification.{checks[],passed}, human.{intervened,who_role,at}`
- outcome (written later): `outcome ∈ {correct, wrong, partial, missed, uncertain, UNKNOWN}, outcome_verified_by, false_positive|false_negative, severity, correction_id, learning_class`
- provenance: `knowledge_versions_used[], regulation_versions_in_force[], policy_versions_in_force[], provider_versions[]`

**UNKNOWN is the default outcome** and remains until a verified signal arrives (brief §15). An AI judge can propose an outcome; it is recorded as `outcome_proposed_by_ai` and does not change `outcome`.

**Quality Ledger** = materialised views over Decision Ledger outcomes by route × provider/model/version × agent × tenant × capability × risk class (brief §16). **Cost Ledger** = materialised views over cost attributes **plus** non-AI cost sources the brief lists (telephony, numbers, SIP, SMS, WhatsApp, email, media, DB, storage, vector, graph, backups, bandwidth, TSA, anchoring, certificates, verification, compute, queues, buses, monitoring, coding/test/security agents, CI/CD, HiL and human approvals where measurable). Unit outputs: cost per interaction / call / certified proof / tenant / workflow / provider / agent / capability / user / month / correction / incident (brief §20).

**`DERIVED REQUIREMENT` (from R-02, D-12 and Part 2b "model reproducibility"):** the subset of the Decision Ledger row that concerns a *certified* verdict (models, versions, prompt versions, provider versions, policy/regulation versions, reviewer identity-role, timestamps) must be part of the certified payload or hash-bound to it. This is CR-04 in Part 32 and needs PO approval; it is not a requirement until then.

---

## Part 22 — Tenant intelligence policy (brief output M, brief §14)

`ARCHITECTURE PROPOSAL`. Policies as named, versioned bundles: `DETERMINISTIC_ONLY · RAG_MAX · PORTFOLIO_MAX (no frontier) · ECONOMY · BALANCED · PREMIUM · HIGH_ASSURANCE · REGULATED · CUSTOM_PER_CAPABILITY`. Each bundle sets, per capability: permitted routes, permitted providers/models (intersecting with tenant BYO keys, FR-028), freshness tolerance, latency budget, monthly budget and fallback, content-capture level, HiL thresholds.

**Non-negotiable floor (cannot be lowered by any bundle):** FR-040 verdict model set and vendor-down behaviour (D-04); FR-054 steps 1–6; D-12 bindings; FR-078 consent/DNC; FR-077 retention; FR-079 KMS; any A5+ gate; EU AI Act Art 50 disclosure where applicable (Part 13.4); OWASP ASI controls for agents acting on the tenant's behalf.

Interaction with D-13 (provider configuration through product): the intelligence policy is one more thing the product must let a tenant select, inspect and switch — same UI surface, same audit trail.

---

## Part 23 — Learning and knowledge-promotion architecture (brief output N, brief §17–§19)

`ARCHITECTURE PROPOSAL`.

```text
Decision (any route) ──► Outcome verified? ──no──► stays UNKNOWN; no learning
        │ yes
        ▼
KnowledgeLearningCandidate(id, decision_ids[], class_hypothesis, provenance, tenant_scope)
        │
        ▼ classify (deterministic first):
   solvable by rule/SQL?        → RULE/POLICY candidate
   stable fact with authority?  → STRUCTURED/CRAG candidate
   repeated semantic reasoning? → PORTFOLIO candidate (subject to Part 19 gate)
   temporary/current?           → TIME-BOUNDED CACHE/RAG (valid_to mandatory)
   rare complex reasoning?      → KEEP FRONTIER
   high-risk?                   → HIGH ASSURANCE / HUMAN (never auto-promoted)
        │
        ▼ promotion checks: source authority · verification record · evaluation on held-out set ·
          regression tests · security review (ASI06 memory-poisoning threat model [S-27]) ·
          tenant isolation (tenant-derived knowledge never leaves the tenant without an explicit,
          recorded anonymisation decision) · freshness/expiry · versioning · rollback · human approval
          where class requires
        ▼
KnowledgeVersion(kind, version, provenance, promoted_from_candidate, approved_by, valid_from, valid_to)
```

**Frontier output is never company truth** (brief §17): a frontier answer creates a candidate; only a verified outcome promotes it. **Duplicate expensive-request detection** (brief §19) is the deterministic layer's exact-match plus CRAG's semantic match **with the invalidation key** `(tenant, policy_version, requirement_version, provider_version, regulation_version, knowledge_valid_to, security_context)`; any component differing → no reuse.

**Learning economics** (brief §23): priority = `expected_reuse × avoided_cost × value_or_risk_weight ÷ promotion_cost`, with `value_or_risk_weight` dominating for compliance/security knowledge (promote immediately even if reuse is low). Research note: this is a standard value-of-information prioritisation; no better established formula was found that adds anything for this use.

**Cross-tenant flywheel** (brief §36): what may compound across tenants is *provider behaviour, regulation versions, incident patterns and TalkProof's own operational knowledge*. What may **not** cross tenants: transcripts, verdict content, customer scripts, tenant policies, anything identifying. This split must be a PO decision (D-19, Part 34) before any aggregation exists.

---

## Part 24 — Modular execution architecture (brief output O, brief §24–§26, §29–§30)

`ARCHITECTURE PROPOSAL`. This is the one area where the brief's design is accepted almost unchanged, because it is ordinary good engineering and the research adds nothing that contradicts it.

**Rule:** one domain module per intelligence capability (Decision Ledger ingestion, outcome evaluation, quality scoring, cost calculation, RAG-miss analysis, portfolio-miss analysis, frontier-escalation analysis, duplicate detection, clustering, knowledge consolidation, rule-candidate generation, CRAG promotion, portfolio training preparation, model evaluation, provider-health analysis, security analysis, compliance analysis, performance analysis, self-diagnosis, correction proposal, simulation, verification, promotion, gap detection). Each module is a pure function over inputs with a **contract** (`input schema, output schema, event schema, version, idempotency key, retry semantics, timeout, failure behaviour, checkpoint/resume, provenance, tenant context, security context, resource needs, cost telemetry`). No `nightly_X` / `realtime_X` pairs: one implementation, bound at deployment to an **execution policy** `DISABLED · ON_DEMAND · BATCH(cron) · THRESHOLD(n decisions | £x spend | n misses | error rate) · EVENT · NEAR_REAL_TIME · REAL_TIME`.

**Execution substrates** (same module, deployment-selected): in-process sync/async → queue + worker (same host / separate host / container / serverless job / scheduled batch / continuous service). Hidden coupling forbidden: local filesystem, single-machine assumptions, specific DB/queue/cloud/LLM/vector implementations — all behind the existing adapter pattern (D-13 direction extended inward).

**Checkpoint/resume** (brief §30): job record `(job_id, module, version, input_range, checkpoint_cursor, processed, remaining, provider/model, tokens, accumulated_cost, failures, retries)`; idempotent re-run from cursor. **Default policies at launch:** everything BATCH nightly except gap detection for security/compliance/evidence (EVENT) and ledger ingestion (NEAR_REAL_TIME). Real-time is used for nothing in the intelligence runtime at launch (brief §26).

Relationship to TalkProof's current state: V2 Part 3 shows the resilience/observability layer at D2 (G28) and no live deployment; this runtime therefore has **no substrate to run on yet**. It is designed now so that adapters, ledgers and gap detectors are written to the contract from the start — not so that it is built now.

---

## Part 25 — Cost-aware execution and workload placement (brief output P, brief §27, §28, §31, §32)

`ARCHITECTURE PROPOSAL`. The scheduler is a deterministic policy over `(tenant policy, risk, urgency, backlog, compute availability, infra price, AI/API price, expected savings, SLA, freshness, volume)` producing `(run_now | defer_to(batch_window) | escalate_to(NRT))`. Placement tiers HOT/WARM/COLD map to execution policies, not to code. Research findings that matter: frontier providers' batch APIs and spot/preemptible compute are commodity and cheap; local inference is cost-effective only for the portfolio models (Part 19) — and only if the gate passes. **Do not optimise infrastructure now** (brief §31): record the cost of the learning system itself (queue, bus, compute, storage, embeddings, retrieval, rerank, portfolio inference/training, frontier, verification) in the Cost Ledger from day one so that the two questions in brief §32 ("would hourly be cheaper?", "has this batch become valuable enough for NRT?") are answerable from data later.

---

## Part 26 — Governed self-correction and autonomy (brief outputs Q and U, brief §8, §21)

`ARCHITECTURE PROPOSAL` with one strong position.

**Loop (brief §8, accepted):** observe → detect (Part 17) → diagnose → retrieve evidence/context → root cause → generate options → risk score → simulate → test → security verify → compliance verify → performance verify → evidence verify → human/automatic gate → canary → deploy → observe → verify outcome → learn → update PSM. Each step is a Part 24 module. The gate is a Part 20 router decision with the correction's **risk class** as input.

**Autonomy ladder per capability** (brief §8): A0 Observe · A1 Diagnose · A2 Recommend · A3 Generate change · A4 Auto-test · A5 Auto-remediate bounded low-risk · A6 Controlled autonomous deploy · A7 Governed closed-loop optimisation.

**Position (one clear line):**

| Capability class | Max autonomy now | Reopen trigger |
|---|---|---|
| Worker restart, queue scaling, cache clear, retry storms, rollback to last known-good deployment | **A5** | — |
| Provider failover within a tenant's configured adapter set | **A5** (because R-41 already makes it a config change) | — |
| Dependency bumps with passing conformance + security tests | **A4** (PR only) | Six months of A4 with zero post-merge incidents → consider A6 for patch-level |
| Code changes to adapters, pipeline, UI | **A4** | Same |
| Authentication, authorisation, RBAC, session, KMS, keys | **A2** | None in 36 months (`FORECAST`) |
| Certificate cryptography, TSA, anchoring, evidence schema, verifier | **A2** | None in 36 months |
| Consent, DNC, retention, redaction rules | **A2** | None |
| FR-040 verdict logic, model roster, prompts used for verdicts | **A2** (prompt/model changes are requirement changes) | None |
| Tenant configuration | **A2** (the tenant acts, not the agent) | — |
| Knowledge promotion to CRAG/rules | **A4** (candidate + tests auto; promotion human) | After ledger shows AI-proposed outcomes agree with verified outcomes > a PO-set threshold for 3 months |

Rationale: published autonomous-remediation performance on hard benchmarks is ~14% [S-14]; AIOps is attackable via telemetry manipulation [S-18]; OWASP ASI08 cascading failures and ASI10 rogue agents are live categories [S-27]. A proof product that self-modifies its proof machinery has a trust problem no customer will accept in 2026.

**Agent cost governance** (brief §21): per-agent run budget `(cost, tokens, model calls, tool calls, retries, wall time, permitted models, escalation rules, tenant daily/monthly caps)`; budget exhaustion → governed fallback (recommend-only, defer, or HiL) recorded in the ledger; hard loop limits; every agent has its own identity and short-lived credentials (NIST agent-identity draft, OWASP ASI03 [S-31][S-27]).

---

## Part 27 — Continuous assurance and verification-first engineering (brief output R, brief §34–§35)

**Research position (brief §34):** yes — in 2026 verification is the principal bottleneck [S-10][S-11][S-12], and for a *proof* product it is also the principal product. "Generate cheaply, verify aggressively" is accepted as a core principle with one correction: *AI-generated verification of AI-generated code is not verification* unless the oracle is independent (spec-derived, property-based, adversarial, or human). Adversarial benchmark work shows test-based pass rates inflate [S-05].

**Automate where justified** (brief §34 list → position): requirement conformance (executable specs, G02), unit, integration, contract, E2E, property, mutation, fuzzing, load/performance, provider conformance, evidence-integrity re-verification, prompt/model evaluation → automate. Chaos → automate once a staging environment exists (none attested). Security/pentest/AI red-teaming → **buy** continuous AI pentest (Part 13.2), keep deterministic exploit validation. Compliance → automate control evidence; keep legal interpretation human.

**Where human verification remains necessary:** acceptance of any requirement wording; D-level sign-off per capability (D6/D7 live runs, G50); HiL on verdicts (FR-032..036); legal/regulatory interpretation; promotion of knowledge into rules/CRAG for high-assurance capabilities; any change at A2 ceilings above.

**Continuous assurance outputs (brief §35, accepted as `ARCHITECTURE PROPOSAL`):** capability scorecard with D1–D7 and evidence refs · requirement conformance · provider health · model quality · security posture · compliance posture · evidence-chain health (scheduled re-verification of a sample of certificates) · performance/regression/reliability baselines · cost baseline · architecture drift · technical debt · test adequacy (mutation score) · release readiness · tenant risk. All are Part 24 modules writing to the PSM; the scorecard is **also a customer-facing artefact** (Part 13.5 item 9).

---

## Part 28 — External-awareness architecture (brief output S, brief §33)

`ARCHITECTURE PROPOSAL`. Sources to watch, each an adapter with a schema: provider changelogs/deprecation feeds (telephony, STT, LLM, messaging, storage, TSA, anchoring, payments), provider status pages, model release/retirement feeds, pricing pages, CVE/NVD + OSV against SBOM/AIBOM, browser/iOS/Android release notes, regulatory trackers (EU AI Act implementing acts, FCC dockets, Ofcom/ICO, TRAI), evidence/crypto standards (ETSI TS 119 312 revisions, NIST PQC, C2PA releases). Process (brief §33): detect → relevance (deterministic match against PSM provider bindings, SBOM, jurisdictions) → affected capabilities/tenants/evidence (PSM traversal) → urgency → proposed response (A2) → verification → governed deployment (per Part 26 ceilings).

**Already-dated first targets** (`MARKET FACT`): EU AI Act Art 50 in force 2 Aug 2026 with Art 50(2) grace to 2 Dec 2026 [S-64]; EU CRA reporting 11 Sept 2026, SBOM Dec 2027 [S-26]; EU PQC inventories by end-2026 [S-59]; FCC AI-disclosure NPRM pending [S-69]; OTel GenAI first stable release pending [S-52]; ETSI TS 119 312 V2.1.1 (June 2026) [S-58].

---

## Part 29 — Evidence and trust evolution (brief output T, brief §38)

This Part does the work D-06 and D-14 asked for. Nothing here changes a decision; it gives the PO the analysis to make them.

### 29.1 Evidence-chain ordering (D-06, left OPEN by PO) — options with consequences, no selection
R-09/FR-054: approval → anchor → PDF. R-10/ARCH §10: anchor → PDF → approval. G42: two timestamps.

| Option | What is proven | What is not proven | Standards fit |
|---|---|---|---|
| (a) FRD: HiL approval first, then TSA + anchor over the approved certificate | The *approved* content existed at time T | That the evidence the reviewer saw was unchanged between capture and review | Simple; one archive timestamp |
| (b) ARCH: anchor + PDF before HiL | The *pre-review* evidence existed at T0 | The approval itself is not timestamped unless re-anchored | Needs a second anchor to prove the approval |
| (c) G42 two timestamps: evidence-root (recording, transcript, STT provenance, model outputs, prompts, policies) timestamped at T0; certificate (evidence-root hash + approval record) timestamped at T1 | Both: what was reviewed and when it was approved; chain of custody across the HiL gap | — | Can be modelled using an RFC 4998/ERS-style evidence-record and renewal approach (initial archive timestamp over the evidence hash tree, subsequent timestamps chained [S-56][S-57]), **subject to E-02 validation**. ERS provides the preservation mechanism; it does not by itself decide TalkProof's semantic lifecycle (evidence captured → reviewer sees evidence → reviewer approves → certificate issued). D-06 stays open. |

`ARCHITECTURE PROPOSAL`: if the PO chooses (c), the mechanism should be ERS-conformant rather than a bespoke Merkle scheme (G41 stays DESIGN but has a standard to conform to). The ordering decision itself remains **D-06 OPEN — PO DECISION REQUIRED** (Part 34).

### 29.2 Part 2b's ten areas — what the frontier answers

| Area (V2 Part 2b) | V2 status | V3 position | Class |
|---|---|---|---|
| Evidence schema evolution | not covered | Evidence records carry `schema_version` and `algorithm_ids`; ERS renewal re-timestamps old records under new schemas without rewriting them ("algorithm migration does not reinterpret historical bytes" [S-57]) | CR-07 candidate |
| Cryptographic agility | not covered | Algorithm identifiers in every hash/signature; hash-tree renewal before deprecation; hybrid classical+PQ timestamps when a qualified PQ TSA exists (ETSI TS 119 312 V2.1.1) [S-58]; PQ inventory by end-2026 to match EU roadmap [S-59] | CR-08 candidate |
| Provider exit | runtime switching only | Evidence must be verifiable with *only* the evidence record + public verifier + TSA/anchor public material — no provider API call. Provider-version provenance recorded per artefact. | CR-09 candidate |
| Model reproducibility | name only | Record model + version + prompt version + provider; where the verification model is open-weight and self-hosted, sampled verifiable inference is a 24–36-month option [S-54] (`EXPERIMENT REQUIRED` E-06) | CR-04 / E-06 |
| Legal/regulatory version at decision time | consent text only | Regulation/policy version IDs in the Decision Ledger and bound into the certificate (TCPA/FCC, EU AI Act Art 50, PECR as first catalogue entries) | CR-05 candidate |
| Clock/time trust beyond TSA | TSA + tz notation | TSA is the trust anchor; local clocks are informative; recording-provider timestamps recorded as a *separate* claim with provenance | CR-06 candidate |
| Redaction vs integrity | rule-level | Chunk-level commitments (MerkleSpeech-style / C2PA assertions over segments) so a redacted recording verifies for the unredacted chunks [S-63][S-60] | CR-10 candidate |
| Tenant exit with continued verification | export only | Export = evidence records + verifier + public trust material; verification must succeed offline after export (extends R-36) | CR-11 candidate |
| Verifier longevity | PDF-level | Standalone open-source verifier (CLI/library) that validates ERS chains, TSA tokens (`openssl ts` as R-06 already requires) and anchors; versioned; published | CR-12 candidate |
| AI supply-chain provenance | none | AIBOM (CycloneDX ML-BOM) + SLSA provenance for TalkProof's own builds; models and prompts as attested components [S-24][S-25] | CR-13 candidate |

### 29.3 Other items from brief §38
- Recording/transcript/STT provenance, speaker/timestamp confidence, model/prompt/policy provenance, human-review provenance → all are D-12 "accepted in principle" bindings; Part 21 gives the fields.
- C2PA/Content Credentials: emit manifests for certified recordings and transcripts; verify incoming manifests; treat absence as no signal [S-61]. Interoperability only.
- EU AI Act Art 50: where a tenant uses D-09 Option B (AI-originated interactions), the disclosure event becomes part of the evidence chain.

### 29.4 Relying-party model (C08 — `RESEARCH REQUIRED` R-D)
A certificate proves integrity and existence-at-a-time of bound artefacts; it does not by itself prove that the underlying statement (what was said, agreed, consented) is true. TalkProof needs a formal answer to: **who relies on a certificate, for what decision, under what contractual/legal basis, and what exactly are they entitled to infer from it?** Minimum analysis: (a) relying-party classes (counterparty, regulator, court, auditor, the tenant itself); (b) for each, the claim set a certificate makes (integrity, time, provenance, reviewer attestation, model-verdict attestation) and the claim set it explicitly does not make (truth of content, speaker identity beyond diarisation confidence, legal effect); (c) the verifier output must state both sets in plain language. This precedes any marketing use of the word "proof" and feeds CR-12 (verifier) and CR-04 (provenance). No candidate requirement is drafted until R-D is done.

### 29.5 Certificate status, correction, supersession and revocation (C09 — candidate CR-23)
Long-term immutability without a correction model preserves mistakes perfectly. Lifecycle to analyse: `valid certificate → later discovered error (wrong verdict, wrong consent link, reviewer error, compromised key, provider mis-transcription) → correction / supersession / revocation → relying party can discover the new status`. Requirements to analyse: a certificate status record (valid, superseded-by, revoked, under-review) that is itself evidence (timestamped, anchored, ERS-preserved); a superseding certificate that references the original; a status-discovery path that works for an offline verifier (status list embedded at renewal, or a signed status response cached in the export); who may revoke (links to R-E trust-root governance); and whether revocation of an anchored certificate is itself anchored. Interaction with FR-077 (cannot erase within retention) and FR-055 (30-day re-issuable links) must be stated.

---

## Part 30 — Complete economics (brief output V)

What V3 can say without data: the cost model's **structure** (Part 21 Cost Ledger, all categories) and the **ordering of likely cost drivers** for a certified call (`HYPOTHESIS`): telephony minutes + recording storage > STT > three-model verdict (bounded by policy, not optimisable) > TSA + anchoring per certificate > HiL reviewer time (human, dominant if HiL rate is high) > TalkProof's own intelligence runtime (should be a small fraction if Part 24–25 are followed). Everything in the brief's "AI FinOps" scope (routing, caching, distillation) acts only on the *last* line. The economically important lever is therefore **HiL rate and reviewer time**, which depends on verdict quality — which is why the Quality Ledger matters more than the Cost Ledger for margin. `EXPERIMENT REQUIRED` E-05: instrument the first live tenant to replace this hypothesis with numbers. S58 (cost model) remains the owner of the build-vs-buy cost line (V2 Part 5a).

---

## Part 31 — Competitive-headroom assessment (brief output W, brief §43)

Scoring 1–5 (5 = best for TalkProof). Columns: customer value (CV) · reproducibility by AI builders (RP, 5 = hard to reproduce) · time to reproduce (TR, 5 = long) · data/history compounding (DC) · regulatory value (RV) · operational value (OV) · trust value (TV) · implementation cost (IC, 5 = cheap) · ongoing cost (OC, 5 = cheap) · maintenance (MT, 5 = light) · dependency risk (DR, 5 = low) · commoditisation risk (CR, 5 = low).

| Capability (smallest set) | CV | RP | TR | DC | RV | OV | TV | IC | OC | MT | DR | CR | Total /60 | Position |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| H1 Trusted-time + anchoring completion with ERS-style renewal and a standalone verifier (G07, G43, CR-07/08/09/12) | 5 | 5 | 5 | 4 | 5 | 3 | 5 | 2 | 3 | 3 | 3 | 5 | 48 | **First** |
| H2 Evidence bindings per D-12 + regulation/policy/model-version provenance in the certificate (CR-04/05/06) | 5 | 4 | 4 | 5 | 5 | 3 | 5 | 3 | 4 | 4 | 4 | 5 | 51 | **First (with H1)** |
| H3 Decision Ledger on OTel GenAI with UNKNOWN-default outcomes (Part 21) | 3 | 3 | 3 | 5 | 4 | 5 | 4 | 3 | 4 | 4 | 4 | 4 | 46 | Second |
| H4 Expected-vs-observed gap detection + continuous capability scorecard (Parts 17, 27) | 4 | 3 | 3 | 4 | 4 | 5 | 4 | 3 | 4 | 3 | 4 | 3 | 44 | Second |
| H5 Real provider adapters + conformance harness + provider-version provenance (G13–G26, G45) | 5 | 2 | 2 | 4 | 3 | 5 | 3 | 2 | 3 | 3 | 2 | 2 | 36 | Necessary, not headroom |
| H6 Intelligence router / CRAG / portfolio / learning loop (Parts 18–23) | 2 | 1 | 1 | 3 | 1 | 4 | 2 | 2 | 3 | 2 | 3 | 1 | 25 | Later; cost control only |
| H7 Governed self-correction A5+ (Part 26) | 2 | 1 | 1 | 2 | 1 | 4 | 1 | 1 | 2 | 2 | 2 | 1 | 20 | Defer |

**Position (`FORECAST / HYPOTHESIS` — C06):** H1 + H2 are the strongest *current headroom hypothesis*; the "6–12 months" is a forecast that requires R-A named-vendor validation (how many competitors already have RFC 3161, evidence renewal, published verification, model/prompt provenance, regulation-version provenance, provider-exit verification). As a hypothesis the headroom is **H1 + H2** (trust that outlives providers, models and cryptography), supported by H3 + H4 (evidence that TalkProof knows what it is and does). H5 is table stakes. H6 is cost control to be built on the ledgers once there is traffic. H7 is not headroom in 2026.

---

## Part 32 — Candidate new requirements (brief output X, brief §45)

Every item is `NEW REQUIREMENT CANDIDATE`. No FR/NFR IDs are assigned (brief §45). **Candidate-grade only (C05):** the blocks below are compressed; several later CRs (e.g. CR-11 "Rest: as CR-09") do not independently state every field. No CR is requirement-grade as written. After D-22 selects a CR, it must be expanded to all 19 fields independently before any FR/NFR ID is issued. Each block gives the 19 fields the brief requires in compressed form: **P** problem · **S** source/reason · **CP** competitor pressure · **CV** customer value · **R** requirement statement · **AC** acceptance criteria · **EV** evidence required · **D** dependencies · **SI/CI/OI/£** security / compliance / operational / cost impact · **FM** failure mode · **FB** fallback · **A** autonomy level · **DvA** deterministic vs AI · **EM** execution mode · **TC** tenant configurable · **PO** PO approval required (always yes).

**CR-01 Completion-level governance made executable.** P: G01 (DONE ≠ complete). S: brief Req 1; Part 13.1 SDD. CP: C5/C6 ship D3 and call it done. CV: buyers can see D-level per capability. R: every capability has a D-target, a D-actual and machine-checkable evidence refs in the PSM; D-level cannot be raised without the evidence kind for that level. AC: scorecard regenerates from evidence; a capability with failing D5 evidence drops to D4 automatically. EV: PSM rows + CI artefacts. D: PSM (CR-14). SI: none. CI: supports ISO 42001 lifecycle documentation. OI: changes definition of done. £: low. FM: evidence refs stale. FB: manual override logged. A: A0. DvA: deterministic. EM: EVENT on CI. TC: no. PO: yes.

**CR-02 FR/NFR → executable conformance checks.** P: G02 (no FR/NFR traced). S: R-42; Part 13.5 item 3. CP: spec-driven tooling commodity. CV: conformance is demonstrable. R: each approved FR/NFR has ≥1 executable check (contract/property/E2E/compliance) referencing its ID and version; CI fails on conformance regression. AC: coverage report FR/NFR → checks ≥ an agreed floor. EV: CI artefacts in PSM. D: CR-14. SI: none. CI: positive. OI: adds check authoring to requirement approval. £: medium (authoring). FM: checks that test the wrong thing. FB: human review of check-to-requirement mapping. A: A4 (checks may be AI-drafted, human-approved). DvA: deterministic execution. EM: EVENT on CI. TC: no. PO: yes.

**CR-03 Provider adapter standard + conformance harness (restates G45 with V3 content).** P: G13–G28 seams. S: brief Req 3; V2 G45. CP: adapters are commodity; conformance history is not. CV: real integrations. R: every provider adapter passes a conformance suite against the provider's API (sandbox or live) covering the common contract, declared capabilities, error mapping, circuit-breaker wrapping (NFR-046), version detection and telemetry; the suite result and provider version are recorded per deployment. AC: no adapter reaches D5 without a passing conformance run recorded in the PSM. EV: conformance run artefacts. D: CR-14; S45 close gate. SI: credentials via vault only. CI: n/a. OI: harness maintenance per provider. £: medium. FM: sandbox ≠ production behaviour. FB: staging live run (G50). A: A4. DvA: deterministic. EM: EVENT on deploy + BATCH weekly. TC: no (tenant selects providers under D-13; standard is platform). PO: yes.

**CR-04 Verdict provenance bound into the certificate.** P: Part 2b model reproducibility; M22 records name only. S: R-02, D-12; Part 21 derived requirement. CP: C1/C2 can claim "AI-verified" without provenance. CV: a disputed certificate can be audited to the models, versions, prompts and policies used. R: the certified payload includes or hash-binds: model identifiers and versions, prompt versions, provider versions, routing policy version, regulation/policy versions in force, reviewer role and approval record, Decision Ledger ids. AC: verifier displays these fields; changing any invalidates the hash. EV: certificate + ledger. D: CR-07, Decision Ledger (CR-15). SI: no secrets in payload. CI: supports Art 50 and TCPA evidence. OI: payload schema change (versioned). £: low. FM: provider does not expose version → record "unversioned" explicitly. FB: HiL note. A: A0. DvA: deterministic. EM: inline. TC: no. PO: yes.

**CR-05 Regulation and policy version provenance.** P: Part 2b partial (NFR-030a consent text only). S: Part 13.4 (TCPA, FCC rulings, Art 50 dates). CP: regulatory-history compounding (Part 15). CV: proves which rule was applied. R: a versioned regulation/policy catalogue (jurisdiction, instrument, version, valid interval, source) exists; every consent, DNC, disclosure and verdict decision records the catalogue versions in force. AC: "which rules applied on date X in jurisdiction Y" is a query. EV: catalogue + ledger. D: CR-15, CRAG supersession edges. SI: none. CI: core. OI: catalogue curation is human. £: low tech / ongoing human. FM: stale catalogue. FB: external-awareness alert (CR-19). A: A2 for proposals, human for catalogue changes. DvA: deterministic. EM: EVENT. TC: jurisdiction selection yes; catalogue no. PO: yes.

**CR-06 Trusted-time claims separated by provenance.** P: Part 2b clock trust partial. S: NFR-024/056; Part 29.2. R: every timestamp in evidence carries a provenance class (TSA, anchor, platform clock, provider clock, device clock); only TSA/anchor are trust anchors; others are informative. AC: verifier shows provenance per timestamp. EV: evidence schema. D: CR-07. SI/CI: positive. OI: minimal. £: low. FM: none material. FB: n/a. A: A0. DvA: deterministic. EM: inline. TC: no. PO: yes.

**CR-07 Evidence records conform to a long-term preservation standard (RFC 4998 ERS / ETSI EN 319 102-1 LTV).** P: Part 2b schema evolution, verifier longevity; G41 DESIGN has no standard. S: Part 13.4, 13.5 item 1; R-05/R-06/R-08. CP: `DIFFICULT TO REPRODUCE`. CV: evidence verifiable decades later. R: certificate evidence is stored as an evidence record with archive-timestamp chain; renewal (re-timestamp / hash-tree renewal) is performed before any used algorithm is deprecated; schema version and algorithm identifiers are explicit. AC: `openssl ts`-class verification of each timestamp in the chain; a renewed record verifies old and new chain. EV: ERS artefacts. D: TSA client (G07), anchor adapter (S51/D-03). SI: TSA key compromise handling. CI: eIDAS/ETSI alignment. OI: renewal operations calendar. £: TSA fees per token + renewal batches. FM: missed renewal window. FB: external-awareness + scheduled job alarms. A: A0 (renewal is scheduled, not autonomous judgement). DvA: deterministic. EM: BATCH. TC: no. PO: yes — **also informs D-06**.

**CR-08 Cryptographic agility and PQ readiness.** P: Part 2b. S: ETSI TS 119 312 V2.1.1; EU PQC roadmap; Part 13.4. R: algorithm identifiers everywhere; a cryptographic inventory (CBOM) is maintained; hybrid classical+PQ timestamps adopted when a qualified PQ TSA is available; a documented migration runbook exists. AC: inventory complete by a PO-set date; hash/sig algorithm change is a configuration + renewal, not a code rewrite. EV: CBOM; renewal records. D: CR-07. SI: core. CI: EU PQC roadmap. OI: renewal cycles. £: low until PQ TSAs exist. FM: hard-coded algorithms (V2 Part 2b notes SHA-256/AES-256 fixed in FR-054/NFR-020). FB: n/a. A: A2. DvA: deterministic. EM: BATCH. TC: no. PO: yes.

**CR-09 Provider-exit verifiability.** P: Part 2b. S: R-41; Part 29.2. R: verifying any certificate requires no live call to any provider; all provider-derived artefacts (transcripts, verdicts, tokens, tx ids) are stored with provider + version provenance and public verification material is cached. AC: verifier runs with network disabled (extends R-36). EV: offline verification test. D: CR-07, CR-12. SI/CI: positive. OI: cache public material. £: low. FM: anchor chain unavailable → anchor marked unverifiable, TSA still verifies. FB: multi-anchor policy (D-03). A: A0. DvA: deterministic. EM: inline + BATCH re-verification. TC: no. PO: yes.

**CR-10 Chunk-level evidence commitments (redaction-preserving integrity).** P: Part 2b redaction vs integrity verification unspecified. S: FR-077; Part 13.5 item 2. R: recordings and transcripts are committed as segment hash trees so that a redacted artefact verifies for all unredacted segments and declares redacted ranges. AC: redact a segment → verifier reports "valid, N segments redacted". EV: commitment + verifier output. D: CR-07, G41 mechanism (ERS-conformant). SI: redaction cannot hide tampering. CI: GDPR erasure vs FR-077 retention reconciled. OI: none. £: low. FM: segment granularity too coarse. FB: policy-set granularity. A: A0. DvA: deterministic. EM: inline. TC: granularity yes. PO: yes — depends on D-12 mechanism acceptance.

**CR-11 Tenant exit with continued verification.** P: Part 2b. S: FR-009. R: tenant export includes evidence records, the standalone verifier, public trust material and a verification report; exported certificates verify offline after export. AC: offline verification of export passes. D: CR-09, CR-12. Rest: as CR-09. PO: yes.

**CR-12 Standalone, published verifier.** P: Part 2b verifier longevity (PDF-level only). S: R-36, R-06. R: an open, versioned verifier (library + CLI) validates evidence records, TSA tokens, anchors and chunk commitments without TalkProof services; verifier version is recorded in every certificate. AC: third party verifies a certificate using only the verifier and public material. EV: published artefact + conformance tests. D: CR-07–CR-10. SI: verifier supply chain (signed releases, CR-13). CI: positive. OI: release discipline. £: medium. FM: verifier bug invalidates valid certs → versioning. FB: previous verifier version. A: A4. DvA: deterministic. EM: n/a. TC: no. PO: yes. Note: V2 recorded any offline CLI as DESIGN because FR-055 does not require it; CR-12 is the candidate requirement that would change that.

**CR-13 Build and AI supply-chain provenance (SBOM/AIBOM/SLSA).** P: Part 2b AI supply-chain provenance (none). S: Part 13.2; OWASP ASI04; EU CRA. R: every deployment has a signed SBOM and AIBOM (models, prompts, agents, tools) and SLSA provenance; the PSM links deployment → attestations; CVE matching runs against them. AC: attestation present and verified before deploy. D: CR-14. SI: core. CI: CRA (Dec 2027), ISO 42001. OI: CI changes. £: low (commodity tooling). FM: unsigned artefact → block. FB: none. A: A4. DvA: deterministic. EM: EVENT on build. TC: no. PO: yes.

**CR-14 Product State Model (bi-temporal).** P: brief §6; no single record of intent/implementation/verification/runtime/evidence. S: Part 16. R: a versioned, bi-temporal relational model links requirements, policies, capabilities, components, verification, deployments, provider bindings, decisions, outcomes, costs, incidents, corrections and knowledge versions; contradictions are stored, not resolved. AC: the queries in Part 17 comparators run against it. D: none (Postgres). SI: access control on PSM. CI: n/a. OI: ingestion modules. £: medium. FM: PSM diverges from reality → it is the observed side that is authoritative for runtime, the PSM for intent. FB: n/a. A: A0. DvA: deterministic. EM: NRT ingestion. TC: no. PO: yes.

**CR-15 Intelligence Decision Ledger on OTel GenAI with UNKNOWN-default outcomes.** P: brief §13/§15. S: Part 21. R: every automated intelligence decision has a persisted ledger row with the Part 21 attributes; outcome defaults to UNKNOWN; AI-proposed outcomes are recorded separately and never set outcome. AC: the six questions in brief §13 are answerable for any decision_id. D: CR-14. SI: content capture per tenant policy; no secrets. CI: supports Art 50/ISO 42001 traceability. OI: storage growth → retention policy. £: low–medium. FM: sampling drops rows → persistence is mandatory, not sampled. FB: none. A: A0. DvA: deterministic. EM: NRT. TC: content-capture level yes. PO: yes.

**CR-16 Quality and Cost Ledgers.** P: brief §15/§16/§20. S: Part 21. R: materialised views as specified; cost sources beyond AI tokens ingested; unit costs per the brief's list; frontier-dependency ratio reported only alongside quality and severe-error rates. AC: Intelligence Control Centre (brief §22) renders QUALITY/COST/SPEED/RISK from these views. D: CR-15. £: low. A: A0. EM: BATCH hourly. TC: view only. PO: yes.

**CR-17 Expected-vs-observed gap detection (deterministic comparators).** P: brief §7. S: Part 17. R: the fourteen gap types have deterministic comparators that write Gap rows to the PSM; no LLM in detection. AC: each comparator has a positive and negative test. D: CR-14. A: A0. EM: EVENT for security/compliance/evidence; BATCH otherwise. TC: no. PO: yes.

**CR-18 Governed self-correction with per-capability autonomy ceilings.** P: brief §8. S: Part 26. R: the ceilings table in Part 26 is a versioned policy; any agent action above its capability's ceiling is blocked and logged; every agent has its own identity, short-lived credentials and run budget; budget exhaustion yields governed fallback. AC: attempted over-ceiling action → blocked + ledger row; OWASP ASI01–10 control mapping documented. D: CR-15. SI: core. CI: ISO 42001 agent governance. OI: policy ownership. £: low. FM: ceiling misconfiguration → default deny. A: policy itself A2. DvA: deterministic. EM: inline. TC: no. PO: yes.

**CR-19 External awareness.** P: brief §33. S: Part 28. R: adapters for provider changelogs, status, pricing, model lifecycle, CVE/OSV, platform release notes, regulatory trackers and crypto standards feed Gap rows with affected capabilities/tenants/evidence via PSM traversal. AC: the dated events in Part 28 are detected and attributed. D: CR-14, CR-17. A: A2. EM: BATCH daily; EVENT where feeds push. TC: jurisdiction subscription yes. PO: yes.

**CR-20 Continuous assurance scorecard as a customer-facing artefact.** P: brief §35; Part 13.5 item 9. S: Part 27. R: a per-tenant, evidence-linked scorecard (D-levels, conformance, provider health, model quality, security/compliance posture, evidence-chain health, cost baseline) is generated continuously and exportable. AC: scorecard regenerates from PSM; no manual edits. D: CR-01, CR-14, CR-16, CR-17. A: A0. EM: BATCH daily. TC: visibility yes. PO: yes.

**CR-21 Tenant intelligence policy with a non-negotiable floor.** P: brief §14. S: Part 22. R: named policy bundles selectable through the product (extends D-13); the floor in Part 22 cannot be lowered by any bundle; policy version is recorded in every ledger row. AC: attempt to disable a floor control → rejected + audited. D: CR-15, D-13 work. A: A0. EM: inline. TC: yes (that is the requirement). PO: yes.

**CR-22 Knowledge promotion governance.** P: brief §17/§18. S: Part 23. R: no knowledge enters rules, CRAG or any model except via a LearningCandidate → verification → promotion → KnowledgeVersion path with provenance, isolation, expiry, rollback and human approval for high-assurance classes; cross-tenant promotion requires the D-19 anonymisation decision. AC: every KnowledgeVersion traces to candidates and verified outcomes. D: CR-15. SI: ASI06 memory-poisoning controls. A: A4. EM: BATCH nightly. TC: opt-out of cross-tenant contribution yes. PO: yes.

**CR-23 Certificate status and correction lifecycle (C09; candidate only, from Part 29.5).** P: no status/correction/revocation model for issued certificates. S: independent review 2026-10-04 C09; FR-077/FR-055 interaction. CP: an immutable-but-wrong certificate is a liability, not a moat. CV: relying parties can discover supersession/revocation. R: to be written after D-22 selection and R-D/R-E; fields not independently specified here (C05 applies). PO: yes.

---

## Part 32-D — Architecture and evolution diagrams (brief output AA, brief §40–§42)

### Diagram 1 — TalkProof today (from V2 Part 3; every box `TRACKER-ATTESTED`, `CODE VERIFICATION PENDING`)

```text
Legend: [T] tracker-attested real · [S] seam/stub · [P] partial · [A] absent · [X] external/deploy-dependent

CLIENTS                 BACKEND (FastAPI)                       PROVIDERS
Flutter web/desk [P] ─► Auth HS256 argon2 TOTP [T] (G29)        Exotel [T April] / Twilio [S] / Telnyx [A] / Vonage [A]
Flutter mobile [S]      RBAC / audit chain [T]                   whisper-1 literal [T] / Google STT [A]
React admin [P]         BYO key store (Fernet) [T] KMS [A]       Claude/GPT/Gemini adapters [S] (M07 stub)
                        Test-connection _probe [S]               IOTA anchor [T hardcoded, stub-tx fallback]
                        Campaign/pipeline, ConfigResolver [T]    RFC3161 TSA [A]  (D1)
                        3-model consensus, hardcoded [T]         Stripe _stripe() [S] · FCM/APNs/SMTP _dispatch [S]
                        Transcription iface [T] whisper [T]      Meta WhatsApp send [S] (inbound real) · Telegram [planned]
                        Cert hash + canonical JSON + PDF [T]     LiveKit SFU [S] · WebSocket gateway [A]
                        HiL engine [T]                           S3 Object Lock [X] · OTel/PagerDuty [X]
                        Consent ledger [T] DNC registry [A]      KMS [X]
                        Regex PII [T] NER [A]
                        AI ledger M22 (neutral rows) [P]
```

### Diagram 2 — Recovery target (what V2 Parts 5a/5b require; unchanged by V3)

```text
Every [S]/[A]/[X] above becomes a REAL ADAPTER behind the common contract (brief Req 3, G45):
telephony ×4 · STT ×2 (diarisation + confidence) · LLM ×3 via vault (S48/S49) · TSA client + anchor adapters (S51, D-03)
payments · push/email · WhatsApp send · Telegram · LiveKit · WebSocket · KMS envelope · DNC registry · NER redaction
+ provider configuration through product (D-13) · + evidence bindings per D-12 · + D6 live E2E runs (G50)
+ completion-level governance and FR/NFR traceability (G01/G02)
D-levels: every row in V2 Part 3 moved to its Target column, evidenced, code-verified.
```

### Diagram 3 — Frontier TalkProof (`ARCHITECTURE PROPOSAL`; nothing below is implemented)

```text
                         ┌──────────── SECURITY · COMPLIANCE · EVIDENCE · COST · AGENT CONTROL · TENANT ISOLATION · OBSERVABILITY ────────────┐
                         │                                          TALKPROOF                                                                   │
                         │                                    PRODUCT STATE MODEL (bi-temporal, Postgres)                                       │
                         │          Requirements/Architecture/Policies   ·   Runtime/Evidence/Performance   ·   Providers/APIs/Regulation/CVEs   │
                         │                                              │                                                                         │
                         │                               SELF-AWARENESS: EXPECTED ↔ OBSERVED (deterministic comparators)                        │
                         │                                              │  Gap / Opportunity rows                                                │
                         │                       RISK-CLASS GATE ──► INTELLIGENCE ROUTER (versioned policy function)                             │
                         │        ┌──────────────┬──────────────┬──────────────┬──────────────────┐                                              │
                         │   Deterministic   Exact/semantic   CRAG (prov.)   Task-model     Frontier LLM                                         │
                         │   rules/SQL/PSM   cache            + history      portfolio      (policy-mandated set for verdicts: FR-040)            │
                         │        └──────────────┴──────────────┴──────────────┴──────────────────┘                                              │
                         │                                   VERIFICATION (deterministic / HiL per policy)                                       │
                         │                                   DECISION LEDGER (OTel GenAI + TalkProof attrs; outcome=UNKNOWN by default)          │
                         │                                              │ DECISION → OUTCOME (verified later)                                    │
                         │                              QUALITY LEDGER ◄─┴─► COST LEDGER                                                          │
                         │                                     LEARNING QUEUE → KNOWLEDGE CONSOLIDATION (candidate → verify → promote → version)  │
                         │                       rule/policy  ·  CRAG update (valid_to)  ·  portfolio training (gate, Part 19)                   │
                         │                                            CHEAPER NEXT DECISION (operational capabilities only)                       │
                         │  SELF-CORRECTION: diagnose → propose → simulate → test → security/compliance/perf/evidence verify →                    │
                         │                   human/auto gate (per-capability ceiling, Part 26) → canary → deploy → observe → learn               │
                         │  EVIDENCE CORE (unchanged thesis): recording/transcript/STT/model/prompt/policy/HiL provenance → ERS evidence record   │
                         │                   → TSA (+PQ hybrid when available) + anchor → certificate → standalone verifier → renewal            │
                         └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### Diagram 4 — Modular execution (brief §41)

```text
DOMAIN INTELLIGENCE MODULE (one implementation)
          │  Stable contract: in/out/event schema · version · idempotency · retry · timeout · failure · checkpoint · provenance · tenant/security ctx · resources · cost telemetry
 ┌────────┼─────────┬───────────┬───────────┐
 Sync    Async     Batch       Event       NRT        ← EXECUTION POLICY (DISABLED / ON-DEMAND / BATCH / THRESHOLD / EVENT / NRT / REAL-TIME)
          │
          ▼  PLACEMENT POLICY (HOT / WARM / COLD via cost-aware scheduler, Part 25)
 ┌────────┼────────┬──────────┬─────────────┐
 Local   Worker   Container  Serverless   Cheap batch / local model
Batch, event and NRT are policies. There is one KnowledgeConsolidationEngine, not nightly_X and realtime_X.
```

### Diagram 5 — Evolution (brief §42; no later stage is implemented; stages 1–2 are V2's scope)

```text
TODAY (V2 Part 3: mostly D2–D3, seams, TSA D1)
  ↓  recovery work (V2 Parts 5a/5b; code verification first)
RECOVERED (every capability at its Target D-level, real adapters, D-13 configuration, D-12 bindings)
  ↓  CR-07/08/09/12 (ERS, agility, provider-exit, standalone verifier) + CR-01/02 (executable completion & conformance)
VERIFIABLE (evidence that outlives providers/models/crypto; verification evidence per capability)
  ↓  CR-14/17 (PSM + gap detection)
SELF-AWARE
  ↓  CR-15/16 (ledgers)
COST-AWARE
  ↓  A1–A2 modules on ledgers
SELF-DIAGNOSING
  ↓  CR-18 ceilings; A4–A5 for bounded ops only
GOVERNED SELF-CORRECTING
  ↓  CR-20 scorecard
CONTINUOUSLY ASSURED
  ↓  CR-22 promotion loop; Part 19 gate for any model training
CONTINUOUSLY LEARNING
  ↓  (36-month `FORECAST`; depends on C7 maturity, Part 14)
CONTINUOUSLY EVOLVING TALKPROOF
```

---

## Part 33 — Experiments and research still required (brief output Y) and self-critique (brief output AC, brief §48)

### 33.1 Experiments / research (`EXPERIMENT REQUIRED` / `RESEARCH REQUIRED`)

| ID | Question | Method | Blocks |
|---|---|---|---|
| E-01 | Code verification of all 46 Part 3 capability rows | Inspect repos per brief §46 and Part 12 plan | Everything that claims a D-level |
| E-02 | Does an ERS-conformant evidence record integrate with the existing canonical-JSON `content_hash` and PDF embedding without re-issuing old certificates? | Prototype against S12 payload (read-only) | CR-07 |
| E-03 | Do multi-hop questions over requirement/provider/regulation history exceed recursive SQL? | Benchmark on PSM sample | Part 16.3 graph decision |
| E-04 | At what monthly frontier volume per capability does a hosted SLM break even, including evaluation/refresh labour? | Model from Cost Ledger once data exists | Part 19 gate |
| E-05 | Actual cost structure of a certified call (telephony/STT/verdict/TSA/anchor/HiL) | First live tenant instrumentation | Part 30 |
| E-06 | Is sampled verifiable inference feasible for an open-weight verification model at TalkProof's verdict volume? | Literature + prototype (NanoZK / deep-prove class tooling) | CR-04 future extension |
| E-07 | Which qualified TSAs offer (or plan) hybrid PQ tokens per ETSI TS 119 312 V2.1.1? | Desk research, vendor enquiry (no calls required) | CR-08 |
| E-08 | Diarisation/word-confidence quality of candidate STT providers on TalkProof-like telephony audio | Offline benchmark on sample recordings | S47 T04, R-11 |
| E-09 | Does chunk-level commitment granularity (CR-10) survive the recording codecs TalkProof's carriers deliver? | Prototype | CR-10 |
| E-10 | Which Art 50 role (provider/deployer) applies per TalkProof tenant configuration for D-09 Option B interactions? | Legal desk research | CR-05, D-09 follow-on |
| R-A | Competitor category C1–C7 evidence refresh (V2 G46/G47 remain RESEARCH) | Desk research against named vendors | Part 14 |
| R-B | AI-inside opportunity assessment (V2 G48, 14 opportunities) against the 7-step test | Desk analysis using Parts 18–23 | Part 32 additions |
| R-C | Primary-source revalidation of standards/legal/high-impact market claims in Parts 13, 28, 29 (C07) | Read RFC 4998/6283, ETSI EN 319 102-1, ETSI TS 119 312 V2.1.1, EU AI Act Art 50 + guidelines, FCC dockets, OTel GenAI repo, OWASP ASI; replace S-nn secondary refs | Any CR drawing on those claims |
| R-D | Relying-party model: what a certificate proves vs does not, per relying-party class (C08; Part 29.4) | Legal/evidential desk research; no calls required | CR-04, CR-12, any "proof" claim |
| R-E | Trust-root governance and independent-operator obligations: signing keys, TSA relationships, reviewer authority, verifier releases, revocation, compromised/erroneous certificates, liability, professional indemnity, verification-longevity SLA, TSA/anchor/provider disappearance, multi-year retention/verification cost (C10) | Desk research + cost model once E-05 data exists | CR-07, CR-12, CR-23, Part 15 moat verdict |

### 33.2 Attack on the proposal (brief §48 — eighteen questions, one answer each)

1. **Fashionable rather than useful:** "Company Language Model"; graph database as a first-class store; real-time intelligence processing; A6–A7 autonomy. All rejected or deferred above.
2. **Commodity within six months:** routing, semantic caching, AI pentest, AI summaries, provider adapters as code.
3. **Commodity within twelve months:** executable-spec tooling, continuous compliance for infra, agent governance frameworks, AI SRE platforms, C2PA emission.
4. **Unnecessary complexity:** separating "verified historical decisions" as its own ladder rung (merged into deterministic/CRAG); nine PSM domains as nine stores (one Postgres); a learned router (deferred).
5. **Reproducible quickly by AI-native competitors:** the whole intelligence runtime (Parts 18–25) and everything in Diagram 1. Not reproducible quickly: operated trust (H1/H2) and operating history.
6. **Requires data/history we do not possess:** the CLM gate, learning economics, cost model, learned routing, cross-tenant flywheel — all of Parts 19, 23, 25, 30. V3 designs them so the data is captured; it does not pretend they are useful today.
7. **Dangerous autonomous authority:** any A5+ on evidence, crypto, auth, consent, verdict logic, knowledge promotion for high-assurance classes. Capped at A2 (Part 26).
8. **Economically irrational:** training any model at current (zero attested) traffic; real-time execution for learning jobs; graph DB before SQL is shown insufficient; building pentest or compliance-monitoring tooling.
9. **Deterministic software superior:** gap detection, router policy, duplicate detection, invalidation, promotion checks, PSM traversal, consent/DNC, cost calculation — all deterministic by design.
10. **RAG overused:** if CRAG is used for anything with a deterministic source of truth (tenant config, provider versions, policy versions). Rule: structured truth never goes through retrieval.
11. **CLM unjustified:** today, entirely. Gate in Part 19.
12. **Real-time unjustified:** everywhere in the intelligence runtime at launch. Only ledger ingestion and security/compliance/evidence gaps are NRT/EVENT.
13. **Batch better:** knowledge consolidation, quality/cost views, scorecards, re-verification of certificates, external-awareness polling.
14. **Provider neutrality impractical:** LiveKit (FR-016 names it; R-16 is specific); Flutter packages; the TSA *protocol* (RFC 3161 is the neutral layer, TSAs are interchangeable); anchoring across chains with different finality semantics — "provider-neutral" must mean "evidence interpretable per anchor type", not "identical semantics".
15. **Moats that disappear with better open source:** everything in Part 15 marked COMMODITY; also "independent verification" *if* TalkProof does not publish its verifier first (open-source verifiers for ERS/TSA already exist — TalkProof's edge is being the operator, not the author).
16. **Genuine compounding advantage:** evidence-bound decision history under recorded regulatory/provider/model conditions, kept verifiable through change; provider-behaviour history; regulation-version history; incident/correction history bound to evidence.
17. **Assumptions in the brief that are wrong or over-stated:** (a) that "accumulated verified intelligence that teaches cheaper layers" is a moat — it is cost control; (b) that CLM is a rung — it is a gated option; (c) that seven competitor classes are distinct — C3/C4/C5/C6 collapse into "self-built proof tool", and the decisive distinction is operator independence, not builder type; (d) that "self-awareness" needs intelligence — it needs comparators; (e) that evidence longevity is a research problem — the mechanism is a standards-adoption problem; the operational/legal longevity (renewal operations, obligations, liability) remains open research (R-E).
18. **Important October-2026 development missed by the brief:** RFC 4998 / ETSI LTV as the evidence substrate; ETSI TS 119 312 V2.1.1 PQ timestamping suites; EU AI Act Art 50 already in force; C2PA/CAWG audio provenance; OTel GenAI as ledger schema; OWASP Agentic Top 10 as the agent threat model; the verification-bottleneck consensus as a *procurement* driver.

### 33.3 Core principles (brief end) — tested

| Principle | Verdict |
|---|---|
| Immutable history + versioned living requirements | Holds; implemented as bi-temporal PSM with stored contradictions |
| Expected ↔ observed continuously compared | Holds; comparators deterministic |
| Generate cheaply; verify aggressively | Holds with the correction: independent oracles only |
| Deterministic truth where it exists | Holds; strengthened to "structured truth never via retrieval" |
| Expensive intelligence teaches cheaper layers via verified promotion | Holds as cost control; **not** a moat |
| Lower AI cost ≠ better quality | Holds; UNKNOWN default, quality alongside dependency ratio |
| Every important decision reconstructable | Holds; OTel-based persisted ledger |
| Build once; configure execution | Holds unchanged |
| Batch/event/NRT are policies | Holds unchanged |
| Move workloads by economic/risk value without rewriting logic | Holds; design now, optimise later |
| Tenant economics never configure away mandatory controls | Holds; floor in Part 22 |
| Moat = accumulated verified organisational intelligence and evidence | **Partly wrong as stated**; holds only as evidence-bound, independently verifiable history (Part 15 verdict) |

---

## Part 34 — Product Owner decisions still required (brief output Z)

Restated open decisions from V2 and new ones from V3. None is taken here.

| ID | Decision | Options | What V3 adds |
|---|---|---|---|
| D-06 (open) | HiL ordering | (a) FRD · (b) ARCH · (c) two timestamps | Part 29.1: (c) is the RFC 4998 pattern; (a)/(b) each leave one fact unproven |
| D-15 (open) | BRD-001 | supply / treat PRD as top | unchanged |
| **D-16** | Adopt RFC 4998 ERS / ETSI LTV as the evidence-record substrate (CR-07) | yes / no / investigate (E-02) | Highest-scoring headroom (Part 31) |
| **D-17** | Accept the Part 26 autonomy-ceiling table as policy | accept / amend per row | Blocks any A3+ work |
| **D-18** | Decision Ledger on OTel GenAI with persisted rows and UNKNOWN default (CR-15) | yes / amend | Blocks Quality/Cost ledgers, learning, CLM gate |
| **D-19** | Cross-tenant knowledge aggregation boundary | none / anonymised operational knowledge only / per-tenant opt-in | Blocks any cross-tenant learning (Part 23) |
| **D-20** | CLM/model-portfolio gate (Part 19) accepted as the condition for any fine-tune | accept / set N / reject CLM entirely | — |
| **D-21** | Standalone published verifier (CR-12) becomes a requirement (changes V2's "any CLI is DESIGN") | yes / no | Part 15 independent-verification row depends on it |
| **D-22** | Which of CR-01..CR-23 are **selected for requirements analysis** (not approval of CR text as written) | per row | Selected CRs are expanded to all 19 fields; governance process then issues IDs, not this document |
| **D-23** | Scorecard (CR-20) as customer-facing | yes / internal only | Part 13.5 item 9 |
| **D-24** | PSM storage position: Postgres-first, graph only after E-03 | accept / direct otherwise | Part 16.3 |
| **D-25** | Procure continuous AI pentest rather than build (Part 27) | buy / build / defer | Budget |
| **D-26** | Code-verification pass (E-01) scheduled before any CR work begins | yes (recommended) / parallel | V2 scope statement |

---

## Part 35 — Final governance split (brief §50) and the seven buckets requested on 2026-10-04 19:54

### 35.1 Brief §50 classification

| Bucket | Contents |
|---|---|
| HISTORICAL / ALREADY REQUIRED | Parts 1–7 entire: R-01..R-44; G01..G52; Part 2b; Part 3 D-assessment; D-01..D-15; Parts 5a/5b |
| CODE-VERIFIED CURRENT | **None** — `CODE VERIFICATION PENDING — REPOSITORY NOT SUPPLIED` |
| PO-APPROVED DIRECTION | Provider-neutral adapters (D-03, D-07, D-13); FR-040 integrity (D-04, D-05); proof subject human (D-09 B); evidence binding scope (D-12); Part 2b analysis scope (D-14) |
| NEW REQUIREMENT CANDIDATE | CR-01..CR-23 (Part 32); all candidate-grade only (C05) |
| ARCHITECTURE PROPOSAL | Parts 16–29 designs; Diagrams 3–5; Part 29.1 option (c) mechanism (ERS-conformant) |
| RESEARCH REQUIRED | R-A (competitors, G46/G47), R-B (AI-inside, G48), R-C (primary-source revalidation), R-D (relying-party model), R-E (trust-root governance/liability), E-07, E-10 |
| EXPERIMENT REQUIRED | E-01..E-06, E-08, E-09 |
| PO DECISION REQUIRED | D-06, D-15, D-16..D-26 |
| DEFERRED | CLM / model portfolio training (reopen trigger: Part 19 gate); learned router; graph database (after E-03); A5+ beyond the Part 26 bounded list; verifiable inference (E-06); workload-placement optimisation (Part 25) |
| REJECTED | A single "Company Language Model" as a goal; A5+ on evidence/crypto/auth/consent/verdict/knowledge-promotion-high-assurance; real-time execution for learning modules at launch; LLM-based gap detection; building pentest/compliance-monitoring tooling in-house; bespoke (non-standard) long-term evidence formats; treating semantic cache as "safe" without the Part 23 invalidation key; using AI-proposed outcomes as ledger outcomes |

### 35.2 Seven buckets requested in the 19:54 instruction

| Bucket | Where |
|---|---|
| Completed from supplied evidence (V2 + brief) | Parts 8, 9, 10 items 1 and 6–7, 11, 12 (plan only), 14 column "what they can reproduce" where it cites V2 rows, 29.1, 32-D Diagrams 1–2, 34 restated rows |
| Completed from cited external research | Parts 13, 14 (`MARKET FACT` rows), 15 bases, 19.2 cost ranges, 26 rationale, 27 research position, 28 dated targets, 29.2 standards, 33.2 items 2–3 and 18 |
| Architecture proposals | Parts 16–25, 26 loop and ceilings, 27 outputs, 28 process, 29.2 "V3 position" column, 32-D Diagrams 3–5 |
| Forecasts / hypotheses | Every `FORECAST` cell in Part 13; Part 14 time-to-reproduce column; Part 15 "conditional" rows; Part 30 ordering; Part 19.2 "what will pass first" |
| Source revalidation pending — input not supplied | All V2 quotations of PRD/FRD/NFRD/ARCH/tracker/traceability (R-01..R-44, G-rows); Part 9 underlying tracker rows; Part 12 three checks' premises; Diagram 1 provenance |
| Code verification pending — repository not supplied | Part 12 entire; every D-level in Part 3; Diagram 1; the "today" stage of Diagram 5 |
| PO decisions required | Part 34 |

### Gate (V4)
**Sequence (accepted 2026-10-04 20:21):** V4 correction → verify V2 preservation + V3→V4 controlled delta (Part 8A) → code-verify all 46 Part 3 capability rows (E-01) → PO decisions D-06, D-15, D-16..D-26 → requirements/sprint work. D-16..D-26 are **not** approved by the existence of this document.

Parts 1–7 remain the frozen recovery baseline (one clerical correction, Part 9). Parts 8–36 add candidate requirements, architecture proposals, research findings and decisions; **none enters the active requirement baseline, no FR/NFR ID is issued, no sprint is numbered, and no implementation begins from this document.** The next action is the Product Owner's: D-16..D-26 and D-22 (which CRs proceed to wording), with E-01 code verification recommended before any CR work.

---

## Part 36 — Sources (external research performed 2026-10-04; `FRONTIER RESEARCH FINDING` / `MARKET FACT` provenance)

| Ref | Source |
|---|---|
| S-01 | morphllm.com — "Best AI Coding Agents (September 2026)": Fable 5.1 81.2% SWE-bench Pro; Opus 5 97.0% SWE-bench Verified (archived Sep 1 2026); Terminal-Bench 4.0 |
| S-02 | openhands.dev — "AI Coding Benchmarks Explained" (2026): SWE-bench Verified saturating; SWE-bench Pro design |
| S-03 | arXiv 2512.18470v6 — SWE-EVO: best model 25%; gpt-5.2 72.8%→22.9% |
| S-04 | arXiv 2606.07682 — SWE-Marathon: <30% on multi-hour tasks; 27.2M tokens avg |
| S-05 | arXiv 2603.24755 — SlopCodeBench (degradation over long-horizon iteration); cites SWE-abs on inflated pass rates and spec-fidelity loss |
| S-06 | augmentcode.com — "What Is Spec-Driven Development?" (Spec Kit, Specmatic; Jan 2026 preprint) |
| S-07 | jamasoftware.com — SDD for AI-powered engineering (two new bottlenecks: specification and verification) |
| S-08 | arXiv 2608.20341 — SDAD: Spec-Driven Agentic Development (May 2026) |
| S-09 | augmentcode.com — "Spec + TDD" (Thoughtworks on non-deterministic generation; conformance gates) |
| S-10 | arXiv 2603.25773 — "The Specification as Quality Gate" (cites DORA 2026: bottleneck shifts to specification and verification) |
| S-11 | infoq.com — "When Spec-Driven Development Pays off" (Sept 2026) |
| S-12 | tessl.io — "AI Agent Evaluation Needs Executable Specs" (17 Sept 2026) |
| S-13 | augmentcode.com — "How AI Enhances Spec-Driven Development Workflows" |
| S-14 | augmentcode.com — "AI SRE: The 2026 Guide" (Gartner Jan 2026 Market Guide; ~14% on most rigorous published benchmark) |
| S-15 | anhtu.dev — "AI SRE 2026" (autonomy curve; self-healing vs self-harming guardrails) |
| S-16 | novaaiops.com — "AI SRE 2026" (trust-scored agents, revocable authority; most teams not fully autonomous) |
| S-17 | neuralwired.com — AIOps self-healing 2026 (vendor/analyst claims 65% MTTR, 82% autonomous resolution — unverified) |
| S-18 | arXiv 2606.24496 — "Red-Teaming the Agentic Red-Team" (cites telemetry-manipulation attacks on LLM-driven IT ops) |
| S-19 | intruder.io — "8 best AI pentesting tools for 2026" |
| S-20 | arXiv 2607.20255 — Ethics of autonomous offensive agents (AWS security agent GA Mar 2026; XBOW 84.6%) |
| S-21 | firecompass.com — Web app pentesting 2026 (<2% FP with validation; 60–70% vs humans, vendor benchmark) |
| S-22 | arXiv 2608.12996 — ATOBench (agents over-trust target evidence) |
| S-23 | arXiv 2510.06445 — Survey on agentic security (repair agents tricked into malicious patches) |
| S-24 | dev.to — KubeCon Amsterdam 2026: securing the agentic supply chain (SLSA, in-toto, Sigstore, aiBOM, CRA) |
| S-25 | appscale.blog — AI supply chain security 2026 (CycloneDX ML-BOM, LF Model Signing) |
| S-26 | github.com/pulseengine/rivet #107 — EU CRA dates (reporting 11 Sept 2026; SBOM Dec 2027); EU AI Act Aug 2 2026 |
| S-27 | cycode.com — OWASP Top 10 for Agentic Applications 2026 (ASI01–ASI10; AIBOM under ASI04) |
| S-28 | arXiv 2605.03309 — Cryptographic registry provenance (Sigstore proves publisher, not distribution path) |
| S-29 | arXiv 2603.00195 — Supply-chain security for agent skills (ASBoM) |
| S-30 | goteleport.com — OWASP Agentic Top 10 (per-agent identity, short-lived credentials) |
| S-31 | arXiv 2604.05229 — Governance norms → runtime guardrails (cites NIST CAISI AI Agent Standards Initiative Feb 2026; NIST agent identity IPD Feb 2026) |
| S-32 | arXiv 2606.19464 — Deontic policies for runtime governance (Microsoft Agent Governance Toolkit Apr 2026) |
| S-33 | github.com/systempromptio/awesome-ai-agent-governance |
| S-34 | vanta.com — "9 things your auditor will want to see about your AI agents" (ISO 42001; EU AI Act Aug 2026) |
| S-35 | soc2auditors.org — ISO 42001 software for AI startups (Drata ISO 42001 certified) |
| S-36 | soc2auditors.org — Vanta review 2026 (AICPA Mar 2026 FAQ: efficiency aid) |
| S-37 | arXiv 2608.15817 — RLCascadeRouter (cites LLMRouterBench ACL 2026; routing survey 2603.04445) |
| S-38 | arXiv 2605.06350 — Decision-theoretic characterisation of LLM cascades |
| S-39 | tianpan.co — LLM routing and cascades (RouteLLM 95% quality at 85% routed; semantic cache 60%+) |
| S-40 | neuraltrust.ai — LLM model routing (cascade 50–98%, classifier 45–85%) |
| S-41 | ainewsnest.com — SLMs vs LLMs 2026 (7B fine-tune < $5; 80/20 routing pattern) |
| S-42 | innoflexion.com — SLM vs LLM inference cost (10–30× cheaper serving) |
| S-43 | winder.ai — RAG vs fine-tuning 2026 decision framework (RAG default ~80%; distillation strongest case; continued pre-training rarely justified) |
| S-44 | arXiv 2410.09699 — Honest AI (RAG alone insufficient on CRAG benchmark; fine-tune risks) |
| S-45 | arXiv 2501.13956 — Zep: temporal knowledge graph for agent memory |
| S-46 | neo4j.com — Graphiti knowledge-graph memory (Sept 2026) |
| S-47 | arXiv 2510.16715 (STAR-RAG); arXiv 2510.13614 (MemoTime, WWW'26) |
| S-48 | arXiv 2604.14220 — KG-RAG on CFR regulations (+70% over vector RAG; temporal precedence) |
| S-49 | mnemoverse.com — Knowledge-graph memory for agents (Jul 2026; GraphRAG v3.1 May 2026; keep contradictions live; determinism) |
| S-50 | uptrace.dev — OpenTelemetry for AI systems 2026 (gen_ai.* attributes; content in span events) |
| S-51 | greptime.com — OTel GenAI conventions evolution (MCP conventions v1.39; v1.41) |
| S-52 | truefoundry.com — OTel GenAI conventions (moved to own repo June 2026; Development; no release as of 21 Aug 2026) |
| S-53 | arXiv 2603.18046 — NanoZK (Jul 2026 v2); lagrange.dev — DeepProve-1 (Aug 2025, full GPT-2 proof) |
| S-54 | arXiv 2609.27367 — Seal, Then Sample: sampled layerwise proofs to 70B (22 Sept 2026) |
| S-55 | arXiv 2608.09055 — Restaking-based verifiable inference (EigenAI, VeriLLM) |
| S-56 | ejbca.org — Evolution of timestamping (RFC 3161, RFC 4998 ERS, hash-tree renewal, PQ) |
| S-57 | github.com/Luminous-Dynamics/mycelix #1354 — Long-term validation contract (RFC 4998/6283, ETSI EN 319 102-1; "algorithm migration does not reinterpret historical bytes") |
| S-58 | mdpi.com Cryptography 10(5):70 — Hybrid PQ qualified signatures (ETSI TS 119 312 V2.1.1 June 2026 PQ timestamping suite; no qualified PQ TSA yet) |
| S-59 | thequantuminsider.com (Aug 2026) — PQC timelines (EU inventories end-2026, high-risk 2030; Google/Cloudflare 2029) |
| S-60 | c2pa.org news — Content Credentials 2.3 (Jan 2026); TikTok steering (Jul 2026) |
| S-61 | contentauthenticity.org — State of Content Authenticity 2026 (CAWG 1.2; Pixel 10) |
| S-62 | en.wikipedia.org/wiki/Content_Credentials — Android forgery Aug 2026; no conformant desktop app mid-2026 |
| S-63 | arXiv 2602.10166 — MerkleSpeech (chunk-localised speech provenance) |
| S-64 | knowledge.dlapiper.com — Deployer obligations from 2 Aug 2026 (Art 50; Dec 2 2026 grace) |
| S-65 | digital-strategy.ec.europa.eu — Art 50 guidelines; Transparency Code of Practice |
| S-66 | shibolet.com — Art 50 (guidelines finalised 20 Jul 2026; fines) |
| S-67 | retellai.com — 2026 TCPA playbook (FCC Feb 2024; Fifth Circuit Feb 2026; UK PECR/Ofcom) |
| S-68 | henson-legal.com — AI voice agent compliance (call-by-call consent logging) |
| S-69 | bitbytes.io — AI voice calls legal 2026 (NPRM pending; KYUP May 2026; 12 all-party states; 5-year consent retention) |
| S-70 | assemblyai.com — "How accurate is speech-to-text in 2026" (cpWER; Universal-3.6 Pro RT 5.19%) |
| S-71 | assemblyai.com/benchmarks — Universal-3.6 Pro Realtime benchmark tables (vendor-run) |
| S-72 | deepgram.com — Best STT APIs 2026 (Nova-3 5.26% WER; Google Chirp 2/3 diarisation) |
| S-73 | businesswire.com — Retool 2026 Build vs Buy report (35% replaced a SaaS tool; 78% building more) |
| S-74 | nocodesaas.io — Build vs buy (Klarna replacements) |
| S-75 | appdirect.com — Build vs buy and vibe coding 2026 |
| S-76 | saastr.com — "The 2026 SaaS crash" (v1 is 2% of the work; systems of record resist) |
| S-77 | visioninvesting.substack.com — "Software is dead, long live software" (vertical/regulated SaaS resists) |

All S-nn items were read as search excerpts on 2026-10-04; figures are as reported by those sources, several of which are vendor-authored. Vendor-authored figures are marked as such in Part 13. **C07:** the list mixes standards/research with vendor blogs, commercial benchmarks, GitHub issues, secondary legal articles, Wikipedia and opinion. Acceptable for exploratory V3/V4 analysis; **not sufficient for requirements or product-strategy decisions**. R-C requires primary-source revalidation (RFC/ETSI texts, Official Journal, FCC dockets, OTel repo, OWASP, vendor primary docs) of every standards, legal and high-impact market claim before it informs a requirement.

---

# V5 RECONCILIATION (PARTS 37–47) — CARRIED INTO V6 WITH THE PART 48 EDITS ONLY

## Part 37 — V5 change log from V4 (controlled delta)

| # | Change | Nature | Touches Parts 1–36? |
|---|---|---|---|
| V5-01 | Header block, lineage, D-scale flag | Metadata | No |
| V5-02 | Part 38 added: 46-row reconciled capability table carrying tracker-attested and code-verified columns separately | Reconciliation (E-01 §C/§D/§K) | No — Part 3 untouched; Part 38 supersedes it as the working table |
| V5-03 | Part 39 added: gap-register reconciliation for every V4 gap E-01 touched | Reconciliation (E-01 §C/§I) | No — Part 2 untouched |
| V5-04 | Part 40 added: `CODE-DISCOVERED IMPLEMENTATION DEFECT` register CD-01..CD-17 from E-01 §I | Add (E-01 §I) | No |
| V5-05 | Part 41 added: 14-stage proof-chain evidence table | Reconciliation (E-01 §H/§D) | No |
| V5-06 | Part 42 added: conflicts preserved, with code reality attached as evidence only | Preserve (E-01 §G) | No — Parts 4/7/34 untouched |
| V5-07 | Part 43 added: D-level discipline and D4 audit (no V4 D4 survives) — *V6 note: superseded; one V4 D4 survives under the authoritative scale (Part 43, Part 48 V6-11)* | Reconciliation (E-01 §A/§K) | No |
| V5-08 | Part 44 added: test evidence carried exactly | Carry (E-01 §J) | No |
| V5-09 | Part 45 added: external verification register EV-01..EV-08 | Carry (E-01 §L) | No |
| V5-10 | Part 46 added: PO Decision Pack — NOT YET DECIDED (D-06, D-15, D-16..D-26; D-01/04/05/08 restated with code facts because code contradicts the approved decision) | Add | No |
| V5-11 | Part 47 added: V4→V5 delta ledger (row/defect/test trace per change) | Change control | No |
| V5-12 | Part 12 "Current code-verified state" is **superseded** by Part 38; Part 12's three specific checks are answered in Part 43 | Supersession noted, text unchanged | No |
| V5-13 | Part 35.1 bucket "CODE-VERIFIED CURRENT: None" is superseded by Part 38 (46 rows) | Supersession noted, text unchanged | No |
| V5-meta | Everything else in Parts 1–36 | Unchanged | — |

---

## Part 38 — Reconciled capability table (46 rows, V4 Part 3 order; supersedes Part 3 as the working table; D-levels authoritative as of V6)

Columns: **Req** = authoritative requirement (V4 Part 3) · **Tracker** = V4 "Recovered actual" (tracker-attested, preserved) · **Code** = E-01 classification (IW implemented-and-wired · INI implemented-not-integrated · P partial · HC hard-coded · ST stub/mock · SEAM interface-only · TO test-only · CO configuration-only · AB absent · ED externally-dependent · UV unable-to-verify) · **V6 D** = authoritative D-level (split preserved where E-01 or the D-scale reconciliation split it; first value of a split is the primary used for counts) · **Conf.** = E-01 confidence · **ERVR** = external runtime verification required (EV-ids, Part 45) · **Disp.** = CONFIRMED / LOWERED / RAISED / UNABLE TO VERIFY. E-01 evidence sheet reference in the last column.

| # | Capability | Req | Target | Tracker (V4) | Code (E-01) | V6 D | Conf. | ERVR | Disp. | E-01 ref |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Tenancy Tier A (RLS) | FR-005/006 | D7 | D3 | app-layer scoping IW; RLS SEAM (helpers never called, no policies/migration) | **D2** (RLS) · D3 (app scoping) | HIGH | EV-04 | LOWERED | D-1 |
| 2 | Tenancy Tier B / C | FR-007/008 | D7/D6 | D3/D2 | B: P (`CREATE SCHEMA` only, no routing); C: CO (dict manifest) | D3 / D2 | HIGH | EV-04 | CONFIRMED | D-2 |
| 3 | Auth core (argon2, JWT, MFA, sessions) | FR-011..013 | D7 | D3 | IW, HC values (HS256, 15-min lockout, 15-min TTL) | D3 | HIGH | — | CONFIRMED | D-3 |
| 4 | SSO OIDC/SAML, SCIM | FR-015..017 | D5 | D3/D4 | OIDC P (token response treated as claims; no id_token/JWKS); SAML SEAM (no ACS); SCIM IW | **D2 / D2 / D3** | HIGH | EV-04 | LOWERED | D-4 |
| 5 | RBAC | FR-019..021 | D7 | D3 | IW (server-side, DB grants) | D3 | HIGH | — | CONFIRMED | D-5 |
| 6 | Audit chain / access trail / auth events | FR-022..025 | D7 | D3 | IW; GeoIP ST; WORM AB; chain global + unlocked (CD-07) | D3 | HIGH | — | CONFIRMED | D-6 |
| 7 | SIEM export | FR-027 | D5 | D4 | INI (exporter has no caller) | **D3** | HIGH | EV-04 | LOWERED | D-7 |
| 8 | BYO key store + router + metering | FR-028/030/031 | D7 | D3 | store IW; router INI (`decrypt_secret` never called; resolve result discarded) | **D2** (router) · D3 (store) | HIGH | — | LOWERED | D-8 |
| 9 | Test-connection | FR-029 | D5 | D2 | ST (length check) | D2 | HIGH | — | CONFIRMED | D-9 |
| 10 | HiL engine | FR-032..036 | D7 | D3 | IW; escalation INI (no scheduler) | D3 | HIGH | — | CONFIRMED | D-10 |
| 11 | Governed AI envelope | FR-037 | D7 | D3 | IW around ST | D3 | HIGH | — | CONFIRMED | D-11 |
| 12 | Governed AI provider calls | FR-037/040 | D5 | D2 | ST (constant envelope) | D2 | HIGH | — | CONFIRMED | D-11 |
| 13 | Guardrails PII/injection | FR-038/039 | D5 | D3 (regex) | IW regex/substring | D3 | HIGH | — | CONFIRMED | D-11 |
| 14 | 3-model consensus (orchestrator) | FR-040/053 | D5 | D3 hardcoded | IW+HC (real SDK calls, env keys, literal models; single-model failure tolerated; not ledgered) | D3 | HIGH | EV-01 | CONFIRMED (FR-040 non-conformance recorded, Part 42) | D-14 |
| 15 | Transcription | FR-052 | D5 | D3 hardcoded | inline HC (whisper-1, env key); abstraction SEAM (interface only, no adapters, not imported) | D3 (inline) / **D2** (abstraction) | HIGH | EV-01 | LOWERED | D-15 |
| 16 | Hash + canonical certificate + offline verify | FR-054(1–2)/FR-055 | D6 | D3 | IW but 7-field payload, no algorithm id, server-side self-check only, no in-browser/offline | **D2** | HIGH | — | LOWERED | D-16 |
| 17 | RFC3161 TSA | FR-054(3)/NFR-024 | D5 | D1 | AB | D1 | HIGH | — | CONFIRMED | D-17 |
| 18 | Blockchain anchor | FR-054(4)/NFR-023 | D5 | D3 (IOTA hardcoded, stub-tx fallback) | ST+CO (`iota_client` undeclared → ImportError; env stub only; campaign-level; `anchor_tx_id` never written) | **D2** | HIGH | — | LOWERED | D-18 |
| 19 | Certified PDF | FR-054(5) | D6 | D3 | IW campaign report (reportlab); no per-call cert, no hash/TSA/anchor embedding | D3 | HIGH | — | CONFIRMED | D-19 |
| 20 | S3 Object Lock immutability | FR-054(6)/NFR-045 | D5 | D2 | AB | **D1** | HIGH | — | LOWERED | D-20 |
| 21 | Client portal | FR-055 | D6 | D3 | AB (portal/signed link); verify API IW (authenticated) | **D2** | HIGH | — | LOWERED | D-21 |
| 22 | Campaign carrier abstraction + selection | BR-16 | D4 | D3 (Exotel real; Twilio seam) | resolver IW; Exotel HC + **broken** (CD-01); Twilio ST; Telnyx/Vonage AB | **D2** | HIGH | EV-02 | LOWERED | D-22 |
| 23 | M12 PSTN out/in + numbers | FR-056/057 | D6 | D3 | ST dial/provision; inbound webhook IW-to-DB; no carrier adapters | **D2** | HIGH | EV-02 | LOWERED | D-23 |
| 24 | Recording dual-channel + storage | FR-058 | D5 | D3 (storage D4) | dual-channel AB; storage drivers real but INI (no production writer) | **D1** (dual) / **D3** (storage) | HIGH | EV-02 | LOWERED | D-24 |
| 25 | Chat models/REST | FR-059 | D6 | D3 | IW | D3 | HIGH | — | CONFIRMED | D-25 |
| 26 | Chat realtime WebSocket + presence | FR-060/066 | D6 | D2 | WS AB; presence REST IW | D2 | HIGH | — | CONFIRMED | D-25 |
| 27 | E2E DMs | FR-061 | D5 | D3 server-side | P (flag + ciphertext-required; no keys, no client crypto) | **D2** | HIGH | — | LOWERED | D-25 |
| 28 | Meetings scheduling/rooms | FR-062 | D6 | D3 | IW DB + ST SFU token | D3 | HIGH | — | CONFIRMED | D-28 |
| 29 | Meeting recording / transcription / summary | FR-063/064 | D5 | D3 logic | DB state rows; client-posted transcript; summary via M07 stub | **D2** | HIGH | — | LOWERED | D-28 |
| 30 | Push + email | FR-065 | D5 | D2 | ST `_dispatch` | D2 | HIGH | — | CONFIRMED | D-30 |
| 31 | Flutter app (web/desktop) | FR-067..069 | D6 | D3/D4 vs mocks | IW REST client; no web/desktop targets; tests MockClient; integration_test not run | **D3** | HIGH (code) / UV (test run) | EV-05 | LOWERED | D-31 |
| 32 | Flutter mobile native | FR-072/073 | D6 | D2 | SEAM (Noop/Fake bridges, no plugins, no iOS) — designed interfaces present: `lib/src/mobile/biometric_gate.dart` (`abstract class BiometricAuthenticator`, `FakeBiometricAuthenticator`), `lib/src/mobile/call_controller.dart` (`abstract class NativeCallBridge`, `NoopCallBridge`); no platform plugin in `pubspec.yaml`; no `ios/` | **D2** (V6: raised from V5 D1 — a designed interface is D2 DESIGNED under the authoritative scale) | HIGH | EV-05 | CONFIRMED | D-31 |
| 33 | Admin portal | PRD E-15 | D6 | D3/D4 vs mocks | IW to 42 real routes; Vitest mocks hooks; Playwright not run | **D3** | HIGH | EV-05 | LOWERED | D-33 |
| 34 | Observability endpoints | FR-074 | D5 | D3 | IW minimal (health/ready/prometheus text) | D3 | HIGH | — | CONFIRMED | D-34 |
| 35 | Resilience wrapping | FR-075/NFR-046 | D5 | D2 | INI (primitives exist, wrap nothing) | D2 | HIGH | — | CONFIRMED | D-34 |
| 36 | DR | FR-076 | D5 | D2 (runbook) | Documentation-only: `docs/40_operations/DR_RUNBOOK.md` (RPO ≤15 min / RTO ≤60 min, backup set, PITR restore, failover) and `docs/15_deployment/DEPLOYMENT.md §11 Backup & Restore`; referenced `deploy/scripts/backup.sh` **absent**; no restore-test record (R-36 — E-01 "AB in repo" was wrong, its grep was truncated) | **D2** (V6 per R-36) | MEDIUM | EV-07 | CONFIRMED | D-34 (superseded on this point by R-36) |
| 37 | GDPR export/erase | FR-077 | D5 | D3 | IW narrow (user fields only; field overwrite; no retention rule) | D3 | HIGH | — | CONFIRMED | D-37 |
| 38 | TCPA consent | FR-078 | D5 | D3 | INI (`require_consent` never called; DNC AB) | **D2** | HIGH | — | LOWERED | D-37 |
| 39 | KMS envelope | FR-079 | D5 | D2 | AB (Fernet app key from JWT secret) | D2 | HIGH | — | CONFIRMED | D-39 |
| 40 | Security headers / rate limit | FR-080 | D5 | D3 | headers IW; rate limiter INI (not registered) | D3 (headers) / D2 (rate limit) — split added by V5 from E-01 D-39/40 text | HIGH | — | CONFIRMED | D-39 |
| 41 | White-label / packaging | FR-081/082 | D6 | D3 | IW branding/packaging; no custom-domain provisioning | D3 | MEDIUM | — | UNABLE TO VERIFY (beyond D3; held) | D-41 |
| 42 | AI ledger | M22 | D5 | D3 | IW for M07 only; model name, no version; real AI calls not ledgered | D3 | HIGH | — | CONFIRMED | D-42 |
| 43 | Storage abstraction | BR-15 | D5 | D4 | real adapters (S3/Drive) INI — no production writer, no live run | **D3** | HIGH | EV-04 | LOWERED | D-24/43 |
| 44 | WhatsApp channel | BR-14 | D5 | D3 (inbound D4) | outbound `_send` ST returning deterministic fake `wamid` (`whatsapp_service.py:143-150`), no Graph API adapter; outbound governance/scheduling/persistence IW (`send_outbound`, `_enforce_send_policy`, `dispatch_due`); inbound `POST /webhooks/whatsapp` IW (`routes/webhooks.py:53-63,215-290`: `X-Hub-Signature-256` HMAC-SHA256 over raw body, constant-time compare; **accepts a bare digest as well as `sha256=<hex>`**, `:57`), tested through the real route into the real DB (`tests/integration/test_s34c_whatsapp_webhook.py`, 6 tests); fixture is hand-authored with no Meta API reference or sample payload in the repository; Meta GET verification handshake (`hub.mode`/`hub.verify_token`/`hub.challenge`) **absent**; secret is process-wide env with `dev-secret` default (CD-05) | **D2** (outbound send) / **D3** (outbound governance, scheduling, persistence) / **D3** (inbound webhook + signature verification — contract provenance not independently established in repo; same standard as S3) / **D2** (provider adapter) | HIGH | EV-03 | LOWERED | D-45 (V5 row 45; renumbered to V4 order per R-44/45) |
| 45 | Config resolver | BR-18 | D4 | D4 | Production class `services/config_resolver.py` (campaign > tenant > platform > default; present-row-with-NULL wins; request-scoped cache, `invalidate`, `resolve_with_source`, opt-in audit); contract stated independently of the code in `docs/92_planning/_plan_S46_M28_config_resolver.md:4-7` and BR-18; 22 unit + 2 integration tests (`tests/unit/test_config_resolver.py`, `tests/integration/test_config_resolver_acceptance.py`) run the production class against a real PostgreSQL test database with no substitution of the resolver or repository behaviour (three cache tests attach delegating spies to `_repo.find_tenant_config`); execution evidenced: 24 passed / 0 failed / 0 skipped on PostgreSQL 16.15 with pinned requirements (`TALKPROOF_CONFIG_RESOLVER_TESTRUN_20261004_2150.md`), consistent with the 1,465-pass E-01 run (Part 44). **No production importer** outside its own module (CD-08) | **D4** (component — CONTRACT VERIFIED) / **not runtime-integrated — D5 not reached** | HIGH | — | CONFIRMED (V6: raised from V5 D3 / UNABLE TO VERIFY; non-integration is a D5 question, not a D4 bar) | D-44 (V5 row 44; renumbered to V4 order per R-44/45) |
| 46 | Inbound calling + polymorphic pipeline | BR-03/05 | D5 | D3/D4 | IW logic over ST carrier; recording key never written | **D3** | HIGH | EV-02 | LOWERED | D-46 |

**Row-count invariant:** 46 rows = V4 Part 3 rows (V4 lines 174–219), in V4 Part 3 order (rows 44/45 restored to V4 order per R-44/45: 44 = WhatsApp, 45 = Config resolver). **Disposition tally (V6, authoritative):** CONFIRMED 25 · LOWERED 20 · RAISED 0 · UNABLE TO VERIFY 1 — V5 recorded 22/22/0/2 under the E-01 working scale; R-36 moved row 36 to CONFIRMED, the D-scale reconciliation moved row 32 to CONFIRMED and row 45 (Config resolver) from UNABLE TO VERIFY to CONFIRMED; the remaining UNABLE row is 41 (white-label custom-domain part beyond D3). One V5 refinement retained: row 40 split (headers D3 / rate limiter D2), disposition CONFIRMED. One V6 refinement: row 44 (WhatsApp) split into four sub-capabilities, primary value and disposition unchanged. **V6 D distribution (first value of split rows):** D1 × 3 (rows 17, 20, 24) · D2 × 20 · D3 × 22 · D4 × 1 (row 45 Config resolver, component level) · D5–D7 × 0. **One V4 D4 claim survives under the authoritative scale** (row 45 Config resolver, component level, not runtime-integrated); the other V4 D4 claims (rows 4, 7, 24, 31, 33, 43, 44 inbound, 46) do not — Part 43.

---

## Part 39 — Gap-register reconciliation (every V4 gap touched by E-01)

Format: V4 gap → V4 evidence (tracker-attested) → E-01 code fact → V5 status. Gap classes are V4's (ORIG/COVERED/CORRECT/IMPL/CONFLICT/NEWREQ/DESIGN/RESEARCH) and are **not** changed; V5 adds the code-verified qualifier. No gap is closed in this pass.

| Gap | V4 evidence | E-01 code fact | V5 status |
|---|---|---|---|
| G01 DONE ≠ complete | tracker "carried-forward at deployment" | Confirmed at scale: 22/46 rows below tracker level; no row above D3 | NEWREQ — **code-corroborated**; strengthened |
| G02 FR/NFR untraced | confirmed absent | Not re-checked in E-01 (tracker text not revalidated, EV-06) | NEWREQ — unchanged |
| G03 LLM adapters in governed path stub | S08 stub | `ai_service._invoke_model` returns constant (stub/mock) | CORRECT→S48 — **code-confirmed stub** |
| G04 April orchestrator bypasses vault, literal models | S45 table | `orchestrator_service.py:56-60,454,476,500` env keys + literal models; vault never decrypted anywhere (CD-04) | COVERED→S49 — **code-confirmed; wider than V4** (no path uses the vault, not only the orchestrator) |
| G05 vendor-down 2-of-2 degrade | S48 T05 proposal | Code already tolerates one failed model (`qa_flag` only if `<2` valid) — current behaviour is the S48 proposal, not FR-040 | CONFLICT — unchanged; code reality attached to D-04 (Part 46) |
| G06 verdict vocabulary | S44-B | POSITIVE/NEGATIVE/NEUTRAL/INCONCLUSIVE in prompt, reviews, certificate payload | CONFLICT — unchanged; attached to D-05 |
| G07 TSA never implemented | S12 "at deployment" | Absent in all repos | IMPL — **code-confirmed D1** |
| G08 S51 frames TSA as alternative | S51 T04 | n/a (planning) | CORRECT→S51 — unchanged |
| G09 anchor provider IOTA vs Hedera | S45 | IOTA only, and only via env stub (`iota_client` undeclared) | CONFLICT — unchanged; attached to D-03 with code fact "no working anchor of any provider" |
| G10 HiL before/after anchor | S12 draft→request→issue | Per-call issue has **no** anchor/PDF step; anchor is campaign-level and HiL-independent | CONFLICT — unchanged; D-06 open, noted as moot-in-code (Part 46) |
| G11 diarisation/confidence | S12 whisper-1 literal | `verbose_json` segments discarded; `Transcript` has no segment/confidence columns | CORRECT→S47 — **code-confirmed absent** |
| G12 Google STT must be real | S47 planned | No STT adapter of any kind; package is interface-only | CORRECT→S47 — **less built than V4 assumed** (S47-T02 Whisper adapter not in repo) |
| G13 campaign Twilio seam | S43-D | `_place` deterministic SID | IMPL — **code-confirmed stub** |
| G14 M12 carriers seams, webhooks deferred | S13 | `_dial`/`_provision_number` fake; Exotel webhook HMAC present (semantics EV-02) | IMPL — code-confirmed |
| G15 Telnyx/Vonage absent | POLICY §3 | Absent (strings in `PROVIDERS` only) | IMPL — code-confirmed |
| G16 Exotel absent from FRD | — | Exotel adapter exists and is **broken** (CD-01) | CONFLICT (doc) — unchanged; CD-01 attached |
| G17 dual-channel | no mention | `Record:"true"` single flag | IMPL — **code-confirmed D1** |
| G18 metering at completion webhook | POLICY §6 | No campaign metering at initiation or webhook | IMPL — code-confirmed |
| G19 WebSocket gateway | S14 | Zero WebSocket code in backend or Flutter | IMPL — code-confirmed |
| G20 LiveKit absent | S15/S30-C | `_mint_sfu_token` fake; no `livekit_client` | IMPL — code-confirmed |
| G21 push/email seam | S16 | `_dispatch` logs+True | IMPL — code-confirmed |
| G22 native bindings deferred | S19 | No plugins, no `ios/` | IMPL — **code-confirmed D1** (lower than V4 D2) |
| G23 KMS absent (Fernet) | S06/S21 | Fernet; key derived from JWT secret when unset | IMPL — code-confirmed |
| G24 test-connection no provider call | S06 | `_probe` length check; platform keys no probe | IMPL — code-confirmed |
| G25 Stripe seam; "signature verification attested real" | S09 | `_stripe` stub; **signature scheme is not Stripe's** (CD-02) | IMPL — seam confirmed; **V4's "attested real" for the webhook signature is contradicted by code** |
| G26 WhatsApp outbound seam; inbound Meta signature real | S34-A | `_send` fake; inbound `X-Hub-Signature-256` sha256= HMAC correct; secret defaults `dev-secret` (CD-05) | IMPL — confirmed; inbound not live-verified (EV-03) |
| G27 Telegram | S56 planned | No Telegram code | CORRECT→S56 — unchanged |
| G28 circuit breakers not wrapped | S20 | `core/resilience.py` imported only by ops route; no call wrapped | IMPL — **code-confirmed D2** |
| G29 JWT algorithm | S03 HS256 | `jwt_algorithm="HS256"` | CONFLICT closed-as-drift (V2) — code-confirmed drift; D-01 unchanged |
| G30 lockout 15 min | S03 | `LOCKOUT_MINUTES=15` | drift — code-confirmed; D-08 unchanged |
| G31 impersonation 60 min | S10 | `IMPERSONATION_MAX_MINUTES=60` | drift — code-confirmed; D-08 unchanged |
| G32 M17 identity | tracker | Flutter has no desktop targets; admin is React | CONFLICT (D-02 decided) — code adds: neither M17 reading is built |
| G35 coverage bar | S24/S31-E 99.3–99.5% | Gate red at HEAD: 99.74% vs `fail_under=100` (CD-17) | CONFLICT (D-11 decided) — code fact attached |
| G36 DNC registry | S21 | Absent; consent itself never enforced (CD-08) | IMPL — **wider than V4**: consent enforcement is also missing |
| G37 PII regex not NER | S08 | 4 regexes + 11 substrings | IMPL — code-confirmed |
| G38 consent not bound to certificate | S21/S12 | Payload has 7 fields; no consent, transcript, approver, timestamp, recording hash | IMPL — **code-confirmed; payload smaller than V4's S12 description** (metadata+transcript+consensus+approver+timestamp is **not** what code hashes) |
| G39 recording/transcript hash, STT version not in cert | S12 | Confirmed absent; `Transcript.engine` literal string | NEWREQ (pending D-12) — code-confirmed |
| G40 model version pinning | M22 name only | `AIInteractionLedger.model` String(64) name; orchestrator calls not ledgered (CD-11) | NEWREQ — code-confirmed; **worse than V4**: the only real model calls are outside the ledger |
| G41/G42 Merkle / two timestamps | DESIGN | No code | DESIGN — unchanged |
| G43 independent verifier | FR-055 portal + verify API | Authenticated API recomputes from own DB; no portal, no artefact | IMPL — code-confirmed D2 |
| G44 provider config through product | S35/S46 | Resolver unused in production; admin has no provider-selection screens | NEWREQ (D-13 accepted) — code-confirmed gap larger than V4 |
| G45 adapter completion standard | S33 "best example" | S3/Drive adapters real but no writer | NEWREQ — code fact: the best example is unintegrated |
| G49 Tier B/C provisioning | S02 | empty schema / dict manifest | IMPL — code-confirmed |
| G50 live E2E deferred | all frontend sprints | No live-run artefact in any repo; Playwright/integration_test not run (EV-05) | IMPL (D6 evidence) — code-confirmed |
| G51 ARCH stale | — | README also stale (Next.js/Tauri/RN layout absent) (CD-14) | IMPL (doc) — extended |
| G48 AI inside TalkProof (existing: 3-model verify real-hardcoded, M07 stub, M14 summary, M22) | V2 | Verify: real-hardcoded confirmed; M07: stub confirmed; M14 summary: stub via M07; M22: M07-only | RESEARCH — premises code-confirmed |

Gaps not touched by E-01 (G33, G34, G46, G47, G52, Part 2b areas): unchanged.

---

## Part 40 — `CODE-DISCOVERED IMPLEMENTATION DEFECT` register (from E-01 §I)

These are code facts. A CD entry becomes a requirement **only** where the "Existing requirement" column names one; otherwise it is recorded for engineering correction after PO decisions, without a new FR/NFR ID.

| CD | Defect | E-01 evidence | Maps to V4 gap / row | Existing requirement already requiring the behaviour? |
|---|---|---|---|---|
| CD-01 | Exotel adapter reads non-existent `settings.exotel_account_sid` (real attr `exotel_sid`) → empty account in URL; `status_callback_url` is relative | I-01; `campaign_carrier/resolver.py:109-112`, `config.py:46`, `call_service.py:122` | G13/G16, row 22 | Yes — FR-056 (working PSTN carrier path) |
| CD-02 | Stripe webhook verification uses HMAC(body) vs header, not Stripe's `t=…,v1=` scheme | I-02; `routes/billing.py:253-259` | G25, (no Part 3 row — billing is outside Part 3) | Yes — FR-042 "Stripe webhook signature verified" |
| CD-03 | OIDC callback treats token response as claims; no id_token/JWKS validation; SAML has no ACS | I-03; `sso_service.py:84-125`, `routes/sso.py` | row 4 | Yes — FR-015/016 |
| CD-04 | BYO vault write-only: `decrypt_secret` has no callers; router results discarded | I-04; `core/crypto.py:37` | G04, row 8 | Yes — FR-030 (router uses tenant keys) |
| CD-05 | Webhook secrets default to `"dev-secret"`/`"dev-stripe-secret"` when env unset | I-05; `routes/webhooks.py:30,32`, `routes/billing.py:37` | rows 23, 45; G25/G26 | Partially — NFR secret-handling (NFR-020 class); recorded as defect |
| CD-06 | `iota_client` not a declared dependency; runtime anchor = ImportError → FAILED | I-06; `requirements.txt`, `iota_service.py:188` | G09, row 18 | Yes — NFR-023 (anchor within 10 min) |
| CD-07 | Audit chain global and race-prone (no lock on `prev_hash`) | I-07; `audit_repo.py:29-39` | row 6 | Yes — FR-022 (tamper-evident chain) |
| CD-08 | No production caller for: consent enforcement, rate limiter, HiL SLA escalation, SIEM exporter, ConfigResolver, resilience primitives | I-08 | G36, G28, rows 7, 10, 38, 40, 45 (Config resolver; V5 row 44 before R-44/45) | Yes — FR-078, FR-080, FR-034, FR-027, BR-18, NFR-046 |
| CD-09 | Transcription abstraction interface-only; orchestrator inline | I-09 | G11/G12, row 15 | Yes — FR-052 |
| CD-10 | Storage drivers have no writer | I-10 | G45, rows 24/43 | Yes — FR-058 (recording storage) |
| CD-11 | Orchestrator AI calls bypass M22 ledger | I-11 | G40, rows 14/42 | Yes — M22 scope (every AI provider call ledgered) |
| CD-12 | Blocking `time.sleep` 30/60/90 s retries inside HTTP request | I-12 | row 18 | No new requirement; operational defect |
| CD-13 | Certificate issue flow has no anchor/PDF step; `anchor_tx_id` dead column | I-13 | G10, rows 16/18/19 | Yes — FR-054 (steps 3–5 after approval) |
| CD-14 | Flutter `android/` only; README describes non-existent apps | I-14 | G22/G51, rows 31/32 | Yes — FR-067..073 |
| CD-15 | Celery/Redis declared, unused; worker is 60-s poll | I-15 | row 10 (escalation), 18 | No new requirement; documentation drift |
| CD-16 | Gemini path records no tokens/cost; JSON parse has no fence stripping (formatting counts as vendor failure) | I-16 | row 14, G05 | Yes — FR-040 (per-model result capture) |
| CD-17 | Coverage gate `fail_under=100` red at HEAD (99.74%) | I-17; E-01 §J-2 | G35 | D-11 decided (80% floor); engineering policy gate is red — recorded |

---

## Part 41 — Proof-chain evidence table (14 stages)

"Real E2E today?" = whether the stage is part of a chain that actually executes from carrier webhook to a third-party-checkable artefact. **Current answer for the chain as a whole: NO.** The real, code-verified chain is: carrier webhook → Whisper (real, env key) → 3-model vote (real, env keys) → DB rows → HiL approve → `status=issued` + SHA-256 of a seven-field summary → server-side self-check. TalkProof may not be described as tamper-proof, blockchain-certified, independently verifiable or production-certified on this evidence.

| Stage | Authoritative requirement | Tracker claim (V4) | Code reality (E-01) | Current D | Missing binding | Real E2E today? |
|---|---|---|---|---|---|---|
| Recording | FR-058 dual-channel; NFR-030(e) linkage | S33 drivers; S29-E carrier-side | Campaign: carrier URL fetched, discarded after STT, never stored, no hash. Inbound: client-supplied key, nothing writes | D1 (dual) / D3 (drivers) | recording bytes, recording hash, storage location | Partial (fetch only) |
| Consent | FR-078; NFR-030(e) | S21 consent ledger | `ConsentRecord` + check endpoint; never enforced on call/message paths; not in payload | D2 | consent id/version in payload; enforcement | No |
| Transcription | FR-052 | whisper-1 "shipped operationally" | Real Whisper call; text/duration/language only | D3 | engine version, segments | Yes (real call) |
| Transcript metadata | FR-052 outputs | S47-A `engine` | `engine="openai_whisper"` literal; no timestamps/speakers/confidence; no transcript hash | D2 | diarisation, word confidence, transcript hash | No |
| 3-model consensus | FR-040/053 | S45 real hardcoded | Real 3-provider calls; 2-of-3; one failure tolerated; vocabulary differs; no evidence citations; not ledgered | D3 | FR-040 rules; vault keys; model version; ledger row | Yes (real calls) |
| Human review | FR-032..036, FR-054 "on HiL approval" | S12 draft→request→issue | Draft cert → proposal → approve → `issue` flips status; approver recorded on row, not in hash | D3 | approver/time in payload | Yes (state machine) |
| Canonical evidence payload | FR-054(1) metadata+transcript+consensus+approver+timestamp | S12 "canonical payload" | 7 fields: call_id, campaign_id, tenant_id, verdict, agreement, model_count, per_model | D2 | transcript, approver, timestamp, recording/transcript hashes, consent, algorithm id | Yes (but under-specified) |
| SHA-256 | FR-054(2) | S12 `content_hash` | SHA-256 over sorted compact JSON; stored beside payload; no algorithm identifier | D2 | algorithm id; detached storage | Yes |
| RFC3161 | FR-054(3), NFR-024 | "at deployment" | Absent | D1 | everything | No |
| Blockchain anchor | FR-054(4), NFR-023 | S45 IOTA stub-tx fallback | IOTA via env stub only; undeclared SDK; campaign-level outcome hash, not the certificate; per-call `anchor_tx_id` never set | D2 | real transaction; certificate-level anchoring; provider per D-03 | No |
| Certified PDF | FR-054(5) | S12 reuses pdf_service | Campaign summary PDF with counts + stub tx; no per-call certificate; no hash/TSA/anchor embedding | D3 | hash, TSA token, anchor, approver | Partial (PDF renders) |
| Immutable storage | FR-054(6), NFR-045 | "provisioned by deploy" | Absent | D1 | Object Lock/WORM | No |
| Client verification | FR-055 portal, signed link, "Verify Now" | S29/S36; portal unattested | Authenticated JSON endpoint recomputes from own DB | D2 | portal, signed link, downloadable artefact | No |
| Offline verification | FR-055 in-browser hash; NFR-024 `openssl ts` | S12 `verify_certificate` | None — no artefact leaves the server that a third party can hash | D1 | everything | No |

---

## Part 42 — Conflicts preserved (nothing resolved in V5)

| Decision | V4 state | E-01 code reality (evidence only) | V5 action |
|---|---|---|---|
| D-01 JWT | RS256 approved (Part 7) | HS256 (`config.py:37`) | Preserved; code = drift to correct, per Part 7 |
| D-02 M17 | Flutter desktop (Part 7) | Neither reading built (no desktop target; admin is React) | Preserved |
| D-03 Anchor providers | provider-neutral (Part 7) | No working anchor of any provider | Preserved |
| D-04 Vendor-down | FR-040 stands (Part 7) | Code tolerates one failed model; S48 T05 behaviour is already what ships | Preserved; **code contradicts approved decision** — restated in Part 46 as a conformance item, not reopened |
| D-05 Vocabulary | FR-040 canonical (Part 7) | POSITIVE/… persisted in reviews and certificate payload | Preserved; conformance item |
| D-06 HiL ordering | OPEN | Neither R-09 nor R-10 ordering exists; per-call issue has no anchor/PDF (CD-13) | Preserved OPEN; Part 46 |
| D-07 Exotel | provider-neutral | Exotel adapter broken (CD-01) | Preserved |
| D-08 Security values | 30 min / 2 h stand | 15 min / 60 min in code | Preserved; conformance item |
| D-09 AI-originated | Option B | No code either way | Preserved |
| D-10 RPO/RTO | NFR binds | No DR artefact (row 36 D1) | Preserved |
| D-11 Coverage | 80% floor / 100% policy | Policy gate red at 99.74% (CD-17) | Preserved |
| D-12 Evidence extensions | accepted in scope | Payload has none of them | Preserved |
| D-13 Provider config via product | accepted | Resolver unused; no UI | Preserved |
| D-14 Ten areas | accepted into analysis | — | Preserved |
| D-15 BRD-001 | OPEN | — | Preserved OPEN |
| D-16..D-26 | NOT DECIDED | — | Preserved NOT DECIDED; Part 46 |

---

## Part 43 — D-level discipline, D4 audit, and the three Part 12 checks (V6: re-stated under the authoritative scale)

**D4 audit (authoritative scale; row numbers in V4 order).** V4 Part 3 carried D4 (primary or secondary) on rows 4, 7, 24, 31, 33, 43, 44 (WhatsApp inbound), 45 (Config resolver), 46. Under the authoritative scale D4 = CONTRACT VERIFIED and is reachable without credentials or a live run when an independently defined, sufficiently precise contract exists and evidence shows the production implementation satisfies it (externality of the contract is not the criterion; independence and precision are). Every candidate was audited in `TALKPROOF_DSCALE_RECONCILIATION_V001_20261004_2135.md` §C and the result was independently reviewed and closed. **One V4 D4 survives:** row 45 Config resolver — D4 at component level (contract in the S46 plan/BR-18; 24 tests on the production class against real PostgreSQL; execution evidenced in `TALKPROOF_CONFIG_RESOLVER_TESTRUN_20261004_2150.md`); it is not runtime-integrated, so D5 is not reached. **Eight do not:** 4 (SSO defects; SCIM subset not verified against RFC 7643/7644), 7 (TalkProof-proprietary signing contract, transport patched), 24/43 (S3: hand-authored fake, no AWS reference/sample provenance, `_client()` construction/auth untested, bucket never asserted; Drive: additionally substitutes `MediaIoBaseUpload`/`MediaIoBaseDownload`), 31/33 (mock clients of TalkProof's own API; live E2E not run), 44 inbound WhatsApp (hand-authored fixture with no Meta reference/sample provenance in the repository — the same standard applied to S3; implementation also accepts a bare digest as well as `sha256=<hex>`; GET verification handshake absent), 46 (logic over stubs). Rows 14/15 (real AI/Whisper calls, MagicMock SDK fixtures) and 22/23 (Exotel: whole `httpx` module patched, no request assertions, undocumented inbound signature header) are D3, not D4. No row is lowered by the authoritative scale; raised: 32 (D1→D2, designed interfaces) and 45 (D3→D4 component).

**Prohibited bases checked:** no row in Part 38 is scored on unit tests passing, mocks passing, SDK import, adapter class existence, a provider call appearing in code, or tracker DONE. Rows 14/15 are D3 because real calls exist and are hard-coded, which is the D3 definition — not because the calls are proven to work (EV-01). The single D4 (row 45) rests on contract evidence plus a retained execution record, not on any prohibited basis.

**Part 12's three checks, answered from code:**
1. `os.environ` key reads outside the S45 gate — **present**: `orchestrator_service.py` (4 provider keys + Sheets), `iota_service.py`, `storage/drivers/*`, `call_service.py`, `pdf_service.py`, `routes/billing.py`, `routes/webhooks.py`, `core/logging.py` (E-01 inventory). 
2. M22 model **name only, no version** — confirmed; and the only real model calls are not ledgered (CD-11).
3. `content_hash` canonical serialisation **has no declared algorithm identifier** — confirmed (Part 41).

---

## Part 44 — Test evidence (carried exactly from E-01 §J; V6 adds the retained Config Resolver execution record)

| Item | Result |
|---|---|
| Backend unit (`pytest tests/unit --no-cov -x`) | 990 passed |
| Backend unit + integration with repo config (`--cov-fail-under=100`) | **1,465 passed, 0 failed, 0 skipped** · coverage **99.74%** · **gate FAILED** (23 uncovered lines, listed in E-01 §J) |
| **V6 — Config Resolver execution record** (`TALKPROOF_CONFIG_RESOLVER_TESTRUN_20261004_2150.md`) | `pytest tests/unit/test_config_resolver.py tests/integration/test_config_resolver_acceptance.py --no-cov -o addopts="" -v -rA` on the supplied backend ZIP, pinned `requirements.txt`, PostgreSQL 16.15 local server: **24 passed / 0 failed / 0 skipped** (verbatim pytest output retained). Same environment, `pytest tests/unit tests/integration --no-cov -o addopts=""`: **1,465 passed / 0 failed**, reproducing the E-01 figure above. This record is the execution evidence for row 45 D4; it does not change any other row. |
| Backend `tests/api` (Playwright API) | 64 **skipped** — requires live server |
| Admin Vitest | 30 files, **239 passed, 0 failed** — hooks mocked (`vi.spyOn`) |
| Admin Playwright E2E (12 specs) | **not run** — needs live backend + Vite + seeded super-admin |
| Flutter `flutter test` (19 files) / `integration_test` (4 journeys) | **not run** — no Flutter SDK in verification environment |
| Provider boundaries mocked | all: `_call_claude/_call_gpt4o/_call_gemini`, `openai`, `httpx`, `_place`, `_dial`, `_stripe`, `_send`, `_dispatch`, `_submit_to_iota`, `_exchange_code`, `_probe`, storage `_client` (95 patch/mock references in the integration tier) |
| Real external-provider tests | **none** in any repo |
| End-to-end / staging / deployment evidence | **none** in any repo |

The correct statement is: "all 1,465 backend tests and 239 admin tests pass; the repository's own 100% coverage gate is red; nothing beyond mocked boundaries has been executed." It is **not** "100% tests pass".

---

## Part 45 — External verification register (E-01 §L preserved)

| ID | Verification required | Why code cannot prove it | Evidence needed | Max D before evidence |
|---|---|---|---|---|
| EV-01 | Live Anthropic/OpenAI/Gemini/Whisper responses (JSON robustness, latency, 60-s rule) | Calls are real but keys/network absent; parse path untested on real output (CD-16) | Recorded live run with keys; response samples; latency log | D3 |
| EV-02 | Exotel API behaviour after CD-01 fix; actual signature header; recording URL/retention | Carrier-specific semantics not in repo; HMAC header is an assumption | Carrier docs + recorded webhook capture from staging | D3 (campaign carrier), D2 (M12) |
| EV-03 | Meta WhatsApp inbound signature with real app secret; Graph send | Outbound absent; inbound never exercised; no Meta API reference or sample payload in the repository; **GET verification handshake (`hub.verify_token`) absent — must exist before any live inbound test is possible**; implementation accepts a bare digest as well as `sha256=<hex>` | Meta reference/sample payload with provenance; recorded webhook + send with real app | D3 inbound / D2 outbound |
| EV-04 | Staging/deployment logs from the Vultr host in `docker-compose.prod.yml` (RLS, Tier B, SIEM, storage) | No deployment artefact in repos | Deployment logs, DB policy dump, bucket listing | D3 |
| EV-05 | Admin Playwright and Flutter `integration_test` against a live stack | Not executable in verification environment | Run logs + artefacts | D3 |
| EV-06 | Tracker/traceability quotations in V4 R-/G- rows revalidated line-by-line | E-01 verified code, not tracker wording | Line-cited revalidation pass | n/a (document evidence) |
| EV-07 | DR: tested restore evidence (R-EV7) | Runbook **exists** (`docs/40_operations/DR_RUNBOOK.md`, `docs/15_deployment/DEPLOYMENT.md §11`); `deploy/scripts/backup.sh` referenced but absent; what is missing is a restore test record | Restore test record (and the backup script) | D2 |
| EV-08 | Brief Req 1 authoritative D1–D7 definitions | **CLOSED in V6** — supplied 21:18 and reconciled (`TALKPROOF_DSCALE_RECONCILIATION_V001_20261004_2135.md`); actual movement was D1→D2 (row 32) and D3→D4 (row 45), not D2↔D3 as E-01 predicted | — | — |

---

## Part 46 — PRODUCT OWNER DECISION PACK — NOT YET DECIDED

Recommendations below are the reconciler's and are **not approved**. "Blocks?" = whether requirements/sprint creation must wait for this decision.

| ID | Conflict / question | Authoritative req. | Tracker | E-01 code reality | Market/frontier (V4) | Options | Consequences | Recommendation (unapproved) | Blocks? |
|---|---|---|---|---|---|---|---|---|---|
| D-06 (open) | Order of HiL approval vs anchor vs PDF | FR-054 approval→anchor→PDF (R-09) vs ARCH anchor→PDF→HiL (R-10) | S12 draft→request→issue | Neither exists: per-call issue has no anchor/PDF; anchor is campaign-level (CD-13) | Part 29.1: option (c) two timestamps = RFC 4998 pattern | (a) FRD · (b) ARCH · (c) two timestamps | (a) single post-approval timestamp, simplest; (b) proves pre-review state only; (c) proves both, needs ERS-style record (D-16) | (c), conditional on D-16; if D-16 is "no", (a) | Yes — proof-chain requirements cannot be worded |
| D-15 (open) | BRD-001 availability | PRD cites BRD-001 | — | — | — | supply / treat PRD as top | without it PRD stays top authority | treat PRD as top until supplied | No |
| D-01 restated | RS256 approved; code HS256 | FR-012/NFR-014 | S03 | HS256 | — | (decided) | conformance work item | no change | No |
| D-04 restated | FR-040 stands; code tolerates one failed model | FR-040 (R-03) | S48 T05 | 2-of-3 with silent single failure; 30-s not 60-s; fenced JSON = failure (CD-16) | — | (decided) | conformance work item for S48 | no change; add CD-16 to S48 scope | No |
| D-05 restated | canonical vocabulary; code uses POSITIVE/… in persisted cert | FR-040 (R-04) | S44-B | persisted in reviews + certificate payload | — | (decided) | mapping must be in payload if labels retained internally | no change | No |
| D-08 restated | 30 min / 2 h stand; code 15 / 60 | FR-011, FR-045 | S03/S10 | confirmed | — | (decided) | conformance | no change | No |
| D-16 | Adopt RFC 4998 ERS / ETSI LTV as evidence-record substrate (CR-07) | FR-054, NFR-023/024 (both layers mandatory) | none | chain stops at SHA-256; no TSA/anchor (Part 41) | Part 29.2 standards; Part 31 highest headroom | yes / no / investigate (E-02) | yes: standard long-term format, hash-tree renewal, PQ path; no: bespoke format (rejected in Part 35.1); investigate: delays proof-chain spec | investigate (E-02) now, with yes as default direction | Yes for proof-chain sprints |
| D-17 | Accept Part 26 autonomy-ceiling table | — | — | no autonomy code exists | Part 26 | accept / amend | blocks any A3+ work | accept | No (nothing at A3 is near) |
| D-18 | Decision Ledger on OTel GenAI with persisted rows, UNKNOWN default (CR-15) | M22 scope | M22 M07-only | real AI calls not ledgered (CD-11); name-only model | Part 21 | yes / amend | yes: one ledger schema for M07 + orchestrator; amend: keep M22 and extend | yes, and fold CD-11 fix into it | Partially — blocks ledger-dependent CRs only |
| D-19 | Cross-tenant knowledge aggregation boundary | NFR tenancy | — | app-layer isolation only; no RLS | Part 23 | none / anonymised ops only / per-tenant opt-in | none is safest while RLS is D2 | none until row 1 reaches D5 | No |
| D-20 | CLM / model-portfolio gate (Part 19) | — | — | zero traffic | Part 19 | accept / set N / reject | — | accept gate (defers all training) | No |
| D-21 | Standalone published verifier (CR-12) becomes requirement | FR-055 (in-browser), NFR-024 (`openssl ts`) | S12 verify API | no artefact leaves server (Part 41) | Part 15 | yes / no | yes changes V2's "CLI is DESIGN"; without it independent verification cannot be claimed | yes | Yes for verification requirements |
| D-22 | Which CR-01..CR-23 go to requirements analysis | — | — | E-01 shows CR-01 (completion governance) and CR-03 (adapter conformance) are already the two things the code most lacks | Part 32 | per row | selected CRs get 19-field expansion, no IDs | CR-01, CR-03, CR-07 (via D-16), CR-12 (via D-21), CR-15 (via D-18), CR-23 first | Yes |
| D-23 | Scorecard customer-facing | — | — | — | Part 13.5 | yes / internal | — | internal until D-levels ≥ D5 exist | No |
| D-24 | PSM Postgres-first | — | — | — | Part 16.3 | accept / direct | — | accept | No |
| D-25 | Procure AI pentest vs build | — | — | — | Part 27 | buy / build / defer | — | defer until deployed | No |
| D-26 (open) | E-01 before any CR work | — | — | **E-01 is complete** | — | close as satisfied / keep open | — | close as satisfied by E-01 (R-D26: listed open — the PO has not closed it; not closed by this document) | No |

---

## Part 47 — V4 → V5 delta ledger (change control)

| Δ | V5 location | Change | Trace |
|---|---|---|---|
| Δ01 | Part 38 rows 1,4,7,8,15,16,18,20,21,22,23,24,27,29,31,32,33,36,38,43,45,46 (V5 numbering; 45 = WhatsApp) | D-level lowered (22 rows) — *V6 note: rows 32 and 36 later CONFIRMED (Part 49)* | E-01 §C matrix rows of the same number; §K |
| Δ02 | Part 38 rows 2,3,5,6,9–14,17,19,25,26,28,30,34,35,37,39,40,42 | D-level confirmed (22 rows) | E-01 §C/§K |
| Δ03 | Part 38 rows 41,44 (V5 numbering; 44 = Config resolver, now row 45) | UNABLE TO VERIFY beyond stated level — *V6 note: Config resolver resolved to D4 component / CONFIRMED (Part 49)* | E-01 §C rows 41, 44 |
| Δ04 | Part 38 row 40 | Split added: headers D3 / rate limiter D2; disposition unchanged | E-01 sheet D-39/40 text; explicit reconciliation refinement |
| Δ05 | Part 38 "ERVR" column | EV-ids attached to rows 1,2,4,7,14,15,22,23,24,31,32,33,36,43,45,46 | E-01 §L |
| Δ06 | Part 39 | 48 gap rows annotated with code facts; none closed; G04, G12, G25, G36, G38, G40, G44, G45 marked wider/contradicted | E-01 §C/§D/§I |
| Δ07 | Part 40 CD-01..CD-17 | Defect register added | E-01 §I I-01..I-17 (1:1) |
| Δ08 | Part 41 | Proof-chain table, 14 stages | E-01 §H + sheets D-14..D-21, D-24, D-37 |
| Δ09 | Part 42 | Code reality attached to D-01..D-26 as evidence only | E-01 §G |
| Δ10 | Part 43 | D4 audit: 9 D4 values removed with reasons; Part 12 checks answered | E-01 §A, §K, inventory |
| Δ11 | Part 44 | Test evidence | E-01 §J J-1..J-6 |
| Δ12 | Part 45 | EV-01..EV-08 | E-01 §L 1–8 |
| Δ13 | Part 46 | Decision pack; D-26 recorded as moot (E-01 done) — *V6 note: superseded by R-D26; D-26 is listed open in Part 46* | E-01 completion |
| Δ14 | Part 37 V5-12/13 | Part 12 and Part 35.1 "CODE-VERIFIED CURRENT: None" superseded, text unchanged | reconciliation logic |
| Δ15 | Header | D-scale flag — *V6 note: replaced by the authoritative scale (Part 49)* | E-01 header; EV-08 |

No other change in V5. Parts 1–36 are byte-identical to V4 (MD5 of the V4 source file: `0a519fc9cdc54a5f4a0ca463069eaf90`). V6 edits to Parts 37–47 are listed in Part 49.

---

## Part 48 — V6 change log from V5 (controlled delta)

| # | Change | Source | Nature |
|---|---|---|---|
| V6-01 | Header: title, lineage, status, D-scale paragraph replaced by the authoritative D1–D7 scale; "How to read" updated | R-SCALE + D-scale reconciliation §A | Metadata |
| V6-02 | Part 38 row 36 DR: D1 → **D2**, LOWERED → **CONFIRMED**; evidence added; `backup.sh` absent noted | **R-36** | Correction of an E-01 error |
| V6-03 | Part 38 rows 44/45 restored to V4 Part 3 order (44 = WhatsApp, 45 = Config resolver); CD-08 and Part 47 Δ01/Δ03 annotated for the renumbering | **R-44/45** | Numbering only |
| V6-04 | Part 46 D-26 listed **open** with recommendation "close as satisfied by E-01" (unapproved); open-decision count 13; Part 39 G10 and Part 47 Δ13 wording aligned | **R-D26** | Governance (no decision taken) |
| V6-05 | Part 45 EV-07 reworded: runbook exists; missing item is a restore test record; max D before evidence D2 | **R-EV7** | Register wording |
| V6-06 | Every "provisional (E-01 working scale)" qualifier removed; D-levels labelled authoritative | **R-SCALE** (as resolved by the D-scale reconciliation) | Labels |
| V6-07 | Part 38 row 32 Flutter mobile native: D1 → **D2**, LOWERED → **CONFIRMED**; designed-interface evidence added | D-scale reconciliation (reviewed, accepted) | D-level |
| V6-08 | Part 38 row 45 Config resolver: D3 / UNABLE TO VERIFY → **D4 (component) / not runtime-integrated (D5 not reached)**, CONFIRMED; "zero mocks" wording replaced by "no substitution of the resolver or repository behaviour" (delegating spies exist in three cache tests) | D-scale reconciliation + independent review + `TALKPROOF_CONFIG_RESOLVER_TESTRUN_20261004_2150.md` | D-level |
| V6-09 | Part 38 row 44 WhatsApp: split refined to outbound send D2 / outbound governance D3 / **inbound D3** / adapter D2; primary D2 and LOWERED unchanged; facts added: no Meta reference/sample provenance in repo, bare-digest acceptance (`routes/webhooks.py:57`), GET verification handshake absent | Independent review correction (inbound is **D3, not D4**) | Split refinement + evidence facts |
| V6-10 | Part 38 tally/distribution: 25 CONFIRMED / 20 LOWERED / 0 RAISED / 1 UNABLE; D1 3 · D2 20 · D3 22 · D4 1 · D5–D7 0; "No V4 D4 survives" replaced | D-scale reconciliation (final) | Totals |
| V6-11 | Part 43 D4 audit re-stated under the authoritative scale ("Zero D4+ survives" removed); corrected D4 principle recorded (independence and precision of the contract, not externality) | D-scale reconciliation §C + independent review | D-level discipline |
| V6-12 | Part 44: Config Resolver execution record row added (24/0/0 on PostgreSQL 16.15; 1,465-pass reproduction) | Test-run record | Evidence |
| V6-13 | Part 45: EV-03 narrowed (provenance, handshake, bare digest); EV-08 closed | D-scale reconciliation §H/§I + review | Register |
| V6-14 | Parts 48, 49 and Gate (V6) added; Gate (V5) superseded | Change control | Structure |
| V6-meta | Everything else in Parts 1–47 | Unchanged — the other 43 capability rows are not altered | — |

**Not done in V6 (by instruction):** no new FR/NFR ID; no new requirement; no PO decision approved; D-26 not closed; no sprint scope; no architecture change; no code change; no scope change; no reinterpretation of unrelated V5 evidence; no new CD entry (the WhatsApp handshake absence, bare-digest acceptance and the S3 `_client()` coverage gap are recorded as evidence facts in Part 38/43/45 only).

---

## Part 49 — V5 → V6 delta ledger (change control)

| Δ | V6 location | Before (V5 / gate-corrected) | After (V6) | Trace |
|---|---|---|---|---|
| Δ16 | Part 38 row 32 | D1, LOWERED | D2, CONFIRMED | D-scale reconciliation §B/§E; independent review "D2 JUSTIFIED" |
| Δ17 | Part 38 row 36 | D1, LOWERED (E-01 "AB in repo") | D2, CONFIRMED; runbook evidence; `backup.sh` absent | R-36 |
| Δ18 | Part 38 rows 44/45 | 44 = Config resolver, 45 = WhatsApp (E-01/V5 swap) | 44 = WhatsApp, 45 = Config resolver (V4 order) | R-44/45 |
| Δ19 | Part 38 row 45 (Config resolver) | D3, UNABLE TO VERIFY (as integrated) | D4 component / not runtime-integrated (D5 not reached), CONFIRMED | D-scale reconciliation §C.2; execution record 24/0/0 (PostgreSQL 16.15); independent review closed 21:44 |
| Δ20 | Part 38 row 44 (WhatsApp) | D2 (outbound) / D3 (inbound), LOWERED | D2 send / D3 governance / D3 inbound / D2 adapter, LOWERED; provenance, bare-digest and handshake facts added | D-scale reconciliation §C.3 as corrected by independent review (inbound D3) |
| Δ21 | Part 38 tally line | 22/22/0/2; D1 5 · D2 18 · D3 23 · D4 0; "No V4 D4 survives" | 25/20/0/1; D1 3 · D2 20 · D3 22 · D4 1; one V4 D4 survives (row 45) | Part 48 V6-10 |
| Δ22 | Part 40 CD-08 | rows … 44 | rows … 45 (renumbered) | R-44/45 |
| Δ23 | Part 43 | "Zero D4+ survives"; E-01 "no live run ⇒ no D4" logic | Authoritative D4 audit; one D4; corrected D4 principle | D-scale reconciliation §C; review |
| Δ24 | Part 44 | E-01 §J only | + Config Resolver execution record row | Test-run record |
| Δ25 | Part 45 EV-03 | "inbound never exercised" | + no Meta provenance in repo; handshake absent; bare digest accepted | D-scale reconciliation §H item 7; review |
| Δ26 | Part 45 EV-07 | "Grepped, not read; no artefact found", max D1 | Runbook exists; restore test record missing; max D2 | R-EV7 |
| Δ27 | Part 45 EV-08 | open, "may move D2↔D3 only" | CLOSED; actual movement D1→D2 and D3→D4 | D-scale reconciliation §G |
| Δ28 | Part 46 D-26 | "record as satisfied; decision is now moot" (silent closure) | listed open; recommendation "close as satisfied by E-01" (unapproved); open count 13 | R-D26 |
| Δ29 | Part 39 G10; Part 47 Δ01/Δ03/Δ13/Δ15; Part 47 closing line | — | annotation notes only (no content change to the V5 record) | cross-reference integrity |
| Δ30 | Header; Part 37 title line; Part 38 title/columns; Part 43/44 titles | V5 wording; E-01 working scale; "provisional" | V6 wording; authoritative scale; no provisional label | R-SCALE |

No other change. Parts 1–36 remain byte-identical to V4 (MD5 of the V4 source file: `0a519fc9cdc54a5f4a0ca463069eaf90`); V5 source MD5 `6f339478bc5c7f84b0943e0a740af8f8` is retained unmodified alongside this file.

---

## Gate (V6)

**Sequence:** V4 → E-01 (complete) → V5 (complete) → V5 Gate Review (complete; R-36, R-44/45, R-D26, R-EV7, R-SCALE accepted) → D-scale reconciliation (complete; independently reviewed and closed 2026-10-04 21:44) → **V6 corrected reconciliation baseline (this file) — to be FROZEN** → PO decisions D-06, D-15, D-16..D-26 → requirements/sprint work. Nothing in Parts 37–49 enters the active requirement baseline; no FR/NFR ID is issued; no sprint is numbered; no implementation begins from this document.

**Final invariants checked (mechanical, see validation report):** Part 38 = 46 rows in V4 Part 3 order · all 46 have a disposition · row 32 = D2 · row 36 = D2 · row 44 WhatsApp inbound = D3 · row 45 Config resolver = D4 component / not D5 · distribution D1 3 · D2 20 · D3 22 · D4 1 · D5–D7 0 · disposition 25 / 20 / 0 / 1 · CD-01..CD-17 all present · EV-01..EV-07 open, EV-08 closed · no PO decision approved · D-26 open · V2/V3/V4/E-01/V5/gate review/D-scale reconciliation/test-run record unchanged · code unchanged.

V6 status:
46 capability rows reconciled under the authoritative D1–D7 scale / 25 confirmed / 20 lowered / 0 raised / 1 unable to verify
D distribution (primary values): D1 3 · D2 20 · D3 22 · D4 1 · D5 0 · D6 0 · D7 0
Open PO decisions: 13 (D-06, D-15, D-16..D-26)
External verification categories open: 7 (EV-01..EV-07); EV-08 closed
New FR/NFR IDs issued: 0
New sprints created: 0
Source code changed: NO
V7: NOT created
