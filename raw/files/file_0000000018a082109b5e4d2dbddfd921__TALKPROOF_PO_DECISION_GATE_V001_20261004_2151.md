# TalkProof — Product Owner Decision Gate V001
**Session:** 2026-10-04 21:51 · **Role:** independent Product Owner decision analyst and evidence auditor · **Type:** analysis / recommendation record only

> ## NO PRODUCT OWNER DECISION HAS BEEN APPLIED BY THIS ARTIFACT.
> Every "Recommendation" below is the analyst's. Nothing is approved, closed, created or changed until the Product Owner says so in a dated record. V6 is unmodified and remains the frozen decision baseline.

**Inputs used:** `TALKPROOF_REQUIREMENT_RECOVERY_V6_20261004_2155.md` (authoritative current state) · `TALKPROOF_V5_GATE_REVIEW_V001_20261004_2115.md` · `TALKPROOF_DSCALE_RECONCILIATION_V001_20261004_2135.md` · `TALKPROOF_CONFIG_RESOLVER_TESTRUN_20261004_2150.md` · **`BRD-001` — SUPPLIED** (`TALKPROOF_BRD.md`, Document ID BRD-001, version 1.0.1, dated 2026-06-16, status "Approved for Development", owner WET).

**Frozen V6 facts honoured without re-litigation:** 46 rows · D1 3 / D2 20 / D3 22 / D4 1 / D5–D7 0 · 25 CONFIRMED / 20 LOWERED / 0 RAISED / 1 UNABLE TO VERIFY (row 41) · Flutter native D2 · Config Resolver D4 component, not D5 · WhatsApp inbound D3 · S3 D3 · Google Drive D3 · D-26 open · no FR/NFR IDs · no sprint · no implementation authorised.

**Contradiction check (required before any decision is called safe):** no internal V6 contradiction was found that makes a PO decision unsafe. Two evidence observations arising from BRD-001 are recorded under D-15 (they concern requirement-authority labels, not D-levels, and do not reopen the D-scale).

---

## PHASE 1 — DECISION INVENTORY (from V6 Part 46; exactly 13)

| # | Decision | Exact question (V6 wording) | Why open | Evidence already available | Missing evidence | Scope impact if decided | Dependency on another decision |
|---|---|---|---|---|---|---|---|
| 1 | **D-06** | Order of HiL approval vs anchor vs PDF — (a) FRD approval→anchor→PDF · (b) ARCH anchor→PDF→HiL · (c) two timestamps | PO deferred it 19:16: "resolve during evidence-chain architecture, not by picking the stronger-looking document" (Part 7) | R-09 (FR-054, Approved), R-10 (ARCH §10, Baseline), G42 (DESIGN), Part 29.1 option analysis, Part 41 (neither ordering exists in code; CD-13), **BRD-001 BR-02 / AC-02.5** (new) | A defined certificate lifecycle (reject / modify path; proof that approved content = anchored content); E-02 result if (c) | Fixes wording of every proof-chain requirement (FR-054 steps 3–5) | D-16 (option (c) presupposes an ERS-style record); E-02 |
| 2 | **D-15** | BRD-001 availability — supply it / treat PRD as top authority | BRD-001 was not among the V2 recovery sources | **BRD-001 v1.0.1 is now supplied** | None for the availability question; reconciliation of BR-01..BR-10 against R-01..R-44 is follow-on documentation work | Changes the top of the requirement-authority order (BRD above PRD) | None; it feeds D-06 and D-21 as evidence |
| 3 | **D-16** | Adopt RFC 4998 ERS / ETSI LTV as the evidence-record substrate (CR-07) — yes / no / investigate (E-02) | New in V3; never put to the PO | Part 13.5 item 1, 29.1, 29.2, CR-07, Part 31 H1 — all research finding / architecture proposal / candidate; Part 41: chain stops at SHA-256, no TSA, no anchor | E-02 (ERS record vs existing canonical-JSON `content_hash` + PDF embedding, read-only); R-C primary-source revalidation of RFC 4998 / ETSI refs (currently secondary S-56/S-57) | "yes" fixes the long-term evidence format for all proof-chain requirements; "investigate" commits only research | D-06 (c) depends on it; CR-07/CR-08 selection in D-22 depends on it |
| 4 | **D-17** | Accept the Part 26 autonomy-ceiling table as policy — accept / amend per row | New in V3 | Part 26 (ARCHITECTURE PROPOSAL); code: no autonomy code exists; nothing at A3 is near | None for a policy acceptance; research basis (S-14, S-18, S-27) is secondary pending R-C | Governs any future agent/automation work; no requirement until CR-18 | None (CR-18 depends on it, via D-22) |
| 5 | **D-18** | Decision Ledger on OTel GenAI with persisted rows and UNKNOWN default (CR-15) — yes / amend | New in V3 | M22 scope (recovered: every AI provider call ledgered); code-verified: only M07 ledgered, model name only, real calls bypass ledger (CD-11); Part 21 (ARCHITECTURE PROPOSAL); OTel GenAI semconv "Development, no stable release" (research finding S-52) | CR-15 expanded to 19 fields (only after D-22 selects it); R-C on OTel GenAI status | Either option is a requirement change (new ledger schema or M22 extension) | D-22 (CR-15 must be selected and analysed before it can be approved) |
| 6 | **D-19** | Cross-tenant knowledge aggregation boundary — none / anonymised operational knowledge only / per-tenant opt-in | New in V3 | Code-verified: tenancy is app-layer scoping only, RLS is D2 (row 1, EV-04); no learning code exists; Part 23 (ARCHITECTURE PROPOSAL); BRD-001 R-04 names RLS as the Tier-A mitigation | None for "none"; data-handling/legal analysis for either other option | "none" adds no requirement and blocks cross-tenant learning; others create new data-handling requirements | CR-22 (via D-22) depends on it |
| 7 | **D-20** | CLM / model-portfolio gate (Part 19.2) accepted as the condition for any fine-tune — accept / set N / reject CLM entirely | New in V3 | Part 19.2 gate (ARCHITECTURE PROPOSAL); code-verified: zero attested traffic, no Decision Ledger → gate cannot pass today | E-04 (break-even N) requires Cost Ledger data | "accept" commits nothing now; "set N" needs data; "reject" is a product decision with no evidence either way | D-18 (ledger) before the gate can ever be evaluated |
| 8 | **D-21** | Standalone published verifier (CR-12) becomes a requirement (changes V2's "any CLI is DESIGN") — yes / no | New in V3 | R-06 (NFR-024 `openssl ts` offline), R-36 (FR-055 in-browser hash, offline after download) — recovered; **BRD-001 AC-02.6** "verifiable offline … without platform access" (new); code-verified: no artefact leaves the server (Part 41, offline verification D1); Part 15/31 (hypothesis) | R-D relying-party model (Part 29.4 states no verifier candidate is drafted until R-D is done); CR-12 19-field expansion | "yes" creates a new verification requirement | D-22 (CR-12 selection); R-D |
| 9 | **D-22** | Which of CR-01..CR-23 are **selected for requirements analysis** (not approval of CR text) — per row | New in V3; Part 46 recommends CR-01, CR-03, CR-07, CR-12, CR-15, CR-23 first | Part 32 (all 23, candidate-grade only, C05); E-01/Part 38/39/41 code facts; D-14 (all ten Part 2b areas already accepted into analysis); D-12, D-13 | None for selection into analysis; each selected CR then needs independent 19-field expansion | Selection commits analysis effort only; no requirement, no ID | D-26 (precondition); D-16 (CR-07/08); D-21 (CR-11/12); D-24 (CR-14); R-D/R-E (CR-04, CR-23) |
| 10 | **D-23** | Scorecard (CR-20) as customer-facing — yes / internal only | New in V3 | Part 13.5 item 9, Part 27 (research finding / proposal); code-verified: no scorecard exists; D5–D7 = 0 | None for "internal only" | "yes" would make D-levels a customer artefact while nothing is above D4 | CR-01/CR-20 (via D-22) |
| 11 | **D-24** | PSM storage position: Postgres-first, graph only after E-03 — accept / direct otherwise | New in V3 | Part 16.3 (ARCHITECTURE PROPOSAL); code-verified: Postgres + Alembic is the existing stack | None for "accept"; E-03 only if graph is ever proposed | Constrains CR-14 design; adds no DB category | CR-14 (via D-22) |
| 12 | **D-25** | Procure continuous AI pentest rather than build (Part 27) — buy / build / defer | New in V3 | Part 27/13.2 (research finding); code-verified: no deployment or staging artefact exists (EV-04, Part 44) | None for "defer"; vendor desk research for "buy" when a deployment exists | None now | None |
| 13 | **D-26** | Code-verification pass (E-01) scheduled before any CR work begins — close as satisfied / keep open | V5 silently closed it; R-D26 re-listed it open; PO has not closed it | E-01 artefact; Part 38 (46 rows, each with E-01 ref and disposition); Part 44 (tests executed; Config Resolver 24/0/0; 1,465/0 reproduced); gate review + D-scale reconciliation corrected E-01's errors; Part 48: no CR work has begun | None | Closing it unblocks D-22; it does not authorise any CR work | None (D-22 depends on it) |

**Count check: 13 decisions — D-06, D-15, D-16, D-17, D-18, D-19, D-20, D-21, D-22, D-23, D-24, D-25, D-26. ✔** D-01/04/05/08 appear in Part 46 only as "restated" conformance items; they are decided and are not part of this gate.

---

## PHASE 2 — SOURCE / EVIDENCE REVIEW (classification per decision)

| Decision | RECOVERED REQUIREMENT | EXISTING PO DECISION | USER/PO REQUIREMENT | CODE-VERIFIED FACT | TRACKER-ATTESTED FACT | EXTERNAL VERIFICATION GAP | NEW REQUIREMENT CANDIDATE | DESIGN PROPOSAL | RESEARCH FINDING | INFERENCE |
|---|---|---|---|---|---|---|---|---|---|---|
| D-06 | R-09 (FR-054); R-06 (NFR-024); R-36 (FR-055); **BRD-001 BR-02, AC-02.5** | D-12 (binding scope accepted; mechanism not); D-03 (provider-neutral anchor) | brief Req 7 (G39/G40) | Part 41: issue flow has no anchor/PDF step; anchor is campaign-level; `anchor_tx_id` dead (CD-13); payload has 7 fields, no approver/timestamp | S12 draft→request→issue | EV-04 (no deployment) | CR-07 (via D-16) | G42 two timestamps; Part 29.1 (c) ERS-style mechanism; R-10 ARCH ordering | RFC 4998 / ERS pattern (S-56, S-57; secondary, R-C pending) | "(c) proves both" is the analyst's reasoning in Part 29.1, not a verified property |
| D-15 | PRD cites BRD-001 as parent | Part 7: open, "do not invent its authority" | — | — | — | — | — | — | — | — |
| D-16 | R-05/R-06/R-08 (TSA, offline verification, SHA-256/AES fixed) | D-12 (scope); Part 35.1 "bespoke formats REJECTED" is the **reviewer's** bucket, not a PO decision | brief Req 7 | Part 41: no TSA, no anchor, no algorithm identifier on `content_hash` | — | EV-04 | CR-07, CR-08 | Part 29.1 (c) mechanism; Part 32-D | Part 13.5 item 1; 29.2; Part 31 H1 scoring (hypothesis C06) | Headroom "first" position is a FORECAST |
| D-17 | — | — | brief §8/§21 (user brief) | No autonomy/agent code exists | — | — | CR-18 | Part 26 ceiling table | S-14 (~14% autonomous-remediation benchmark), S-18, S-27 (secondary) | "a self-modifying proof product has a trust problem" — analyst position |
| D-18 | M22 scope (every AI provider call ledgered) | — | brief §13/§15 | M22 ledgers M07 only; model name, no version; orchestrator calls not ledgered (CD-11) | M22 DONE | — | CR-15, CR-16 | Part 21 schema | OTel GenAI semconv status "Development" (S-50..S-52) | — |
| D-19 | NFR tenancy (FR-005/006) | D-13 (provider config) | brief §17–19 | App-layer isolation only; RLS helpers never called, no policies/migration (row 1 D2) | row 1 tracker D3 | EV-04 | CR-22 | Part 23 | — | "none is safest while RLS is D2" — inference, but one grounded on the code fact |
| D-20 | — | D-04 (FR-040 verdicts excluded from any gate) | brief §10–§11 | Zero attested traffic; no ledger | — | — | — | Part 19.2 gate | S-41..S-43 cost ranges (MARKET FACT, secondary) | "gate cannot pass today" follows directly from zero traffic |
| D-21 | R-06 (NFR-024 `openssl ts`); R-36 (FR-055 offline after download); **BRD-001 AC-02.6** | V2 Part 2b: "any CLI is DESIGN" (V2 baseline position) | brief Req 7 | Part 41: nothing a third party can hash leaves the server; offline verification D1 | S12 `verify_certificate` | — | CR-12, CR-11 | Part 29.2 verifier longevity | Part 15 "independent verification" moat row; Part 33.2 item 15 (open-source ERS/TSA verifiers exist) | Part 29.4: relying-party model (R-D) must precede any "proof" claim — RESEARCH REQUIRED |
| D-22 | G01, G02, G36, G40, G45 (gap register) | D-12, D-13, D-14 (ten areas into analysis) | brief Req 1, 3, 7 | Part 38/39: 20 rows lowered; no adapter integrated; consent never enforced; real AI calls not ledgered | — | EV-01..EV-07 | CR-01..CR-23 (all candidate-grade, C05) | Parts 16–29 | Parts 13–15, 31 | Part 46's "first six" list is the reconciler's ordering |
| D-23 | — | — | brief §35 | No scorecard; D5–D7 = 0 | — | — | CR-20 | Part 27 | Part 13.5 item 9 (procurement driver) | "sales collateral" is a forecast |
| D-24 | — | — | brief §6, §10, §37 | Postgres/Alembic is the existing stack | — | — | CR-14 | Part 16.3 | S-49 (secondary) | — |
| D-25 | NFR security scope (M20) | — | brief §34 | No deployment, no staging (EV-04; Part 44 "none in any repo") | — | EV-04 | — | Part 27 "buy" position | Part 13.2 | — |
| D-26 | — | Gate order accepted 20:21 (E-01 before CR work) | V2 scope statement | E-01: 46 rows inspected, tests executed; Part 44 figures reproduced; corrections R-36, rows 32/45 applied through reviewed lineage; row 41 UNABLE beyond D3 (bounded) | — | EV-05 (Flutter/Playwright not run — runtime, not code inspection) | — | — | — | — |

**Insufficient-evidence verdicts from this phase:** D-06 (lifecycle not defined in V6) · D-18 (CR-15 not yet analysed) · D-21 (R-D not done; CR-12 not yet analysed). All three are kept open in Phase 4 with the exact missing items.

---

## PHASE 3 — DEPENDENCY ORDER

**Dependency graph (A → B means B needs A first):**

```
D-15 (BRD-001 authority) ──► evidence for D-06, D-21
D-26 (E-01 satisfied) ─────► D-22 (CR selection)
D-24 (Postgres-first) ─────► CR-14 (in D-22)
D-16 (ERS: investigate) ───► CR-07/CR-08 conditionality (in D-22) ──► E-02 ──► D-06 option (c)
D-17 (ceilings policy) ────► CR-18 (in D-22, deferred)
D-19 (boundary: none) ─────► CR-22 (in D-22, deferred)
D-22 (selection) ──────────► CR-15 analysis ──► D-18 (approval)
D-22 (selection) + R-D ───► CR-12 analysis ──► D-21 (approval)
D-18 (ledger) ─────────────► D-20 gate can ever be evaluated (D-20 itself decidable now)
D-23, D-25 ────────────────► independent
```

**Classification:**

1. **Decidable independently now:** D-15, D-26, D-17, D-19, D-20, D-23, D-24, D-25.
2. **Decidable now but ordered after another decision:** D-16 (after D-15, for completeness of evidence); D-22 (after D-26 closes and D-16/D-24 are known, so conditional rows are tagged correctly).
3. **Require missing source material:** none remaining (BRD-001 is supplied).
4. **Require research / revalidation:** D-16 "yes" (E-02, R-C); D-21 (R-D); D-18 "yes" (R-C on OTel GenAI status).
5. **Remain open until architecture work:** D-06 (certificate lifecycle definition).
6. **Remain open until external / runtime evidence:** none of the 13 directly; D-23 and D-25 have reopen triggers tied to EV-04 / D5.

**Safest decision order (not numerical):**

| Step | Decision | Why here |
|---|---|---|
| 1 | D-15 | Settles the authority base first; BRD-001 supplies evidence used by D-06 and D-21. |
| 2 | D-26 | Precondition for D-22; closing it costs nothing and authorises nothing. |
| 3 | D-24, D-19, D-20, D-23, D-25, D-17 | Independent, conservative-default decisions; each commits no requirement. |
| 4 | D-16 | Determines whether CR-07/CR-08 are conditional in D-22 and whether (c) is live for D-06. |
| 5 | D-22 | Per-row selection into analysis, with conditional rows tagged from steps 3–4. |
| — | D-18, D-21 | Open until the selected CR-15 / CR-12 analyses exist (and R-D for D-21). |
| — | D-06 | Open until certificate-lifecycle architecture and E-02. |

---
## PHASE 4 — DECISION ANALYSIS

### D-06 — HiL approval / anchor / PDF ordering

**Decision question**
Order of HiL approval vs anchor vs PDF: (a) FRD approval → anchor → PDF · (b) ARCH anchor → PDF → approval · (c) two timestamps (evidence-root at T0, certificate at T1).

**Evidence**
- (a): R-09, FR-054 Description (Approved): "On HiL approval, the backend produces a tamper-proof, blockchain-anchored certified PDF." **BRD-001 BR-02** (Approved for Development): certified PDF "gated by Human-in-the-Loop reviewer approval before issuance"; **AC-02.5**: "A reviewer approves the certificate; the system issues a … PDF with embedded hash, RFC3161 timestamp, and blockchain anchor reference."
- (b): R-10, ARCH §10 flowchart (Baseline): I → J (anchor) → K (PDF) → L (HiL gate). No approved requirement document supports this ordering.
- (c): G42 (DESIGN, V2); Part 29.1 (analyst's option table; "subject to E-02 validation"; "ERS … does not by itself decide TalkProof's semantic lifecycle").
- Code (Part 41, CD-13): per-call issue flow has no anchor or PDF step; the only anchor is campaign-level, HiL-independent; `anchor_tx_id` is a dead column; payload has no approver, timestamp, transcript or recording hash. Neither (a) nor (b) exists in code.
- PO's own reason for deferral (Part 7): resolve during evidence-chain architecture, not by picking the stronger-looking document.

**Options** — (a), (b), (c) as in V6. No fourth option is introduced.

**Proof-proposition test (special control)**

| Test | (a) approval first | (b) anchor/PDF first | (c) two timestamps |
|---|---|---|---|
| What exists before human approval | Unanchored evidence + draft | Anchored evidence + PDF | Anchored evidence-root (T0) |
| What exactly the human approves | Draft certificate content | An already-anchored PDF | The evidence-root (by hash) + verdict |
| What is timestamped/anchored | Approved certificate (T1) | Pre-review PDF (T0) | Evidence-root (T0) and certificate incl. approval record (T1) |
| What becomes immutable | Approved content | Pre-review content | Both |
| If the human rejects or modifies the evidence | Nothing anchored yet — no orphan; **but** V6 does not define the modify path (is a modified draft a new draft? is the rejection recorded as evidence?) | Anchored artefact must be superseded/revoked — V6 has no status model (CR-23 is candidate only) | T0 root stands as "what was reviewed"; rejection/modification path **not defined in V6** |
| Can the certificate prove approved content = anchored content | Yes for the approved artefact; cannot prove the reviewer saw unchanged evidence | No — approval is not in the anchored artefact unless re-anchored | Yes for both, **if** the T1 record binds the T0 root and the approval record — mechanism unvalidated (E-02) |

**Consequences**
- *Product meaning:* (a) "the approved certificate existed at T1"; (b) "the pre-review evidence existed at T0"; (c) "what was reviewed, and when it was approved".
- *Proof/evidence integrity:* (a) leaves the capture→review custody gap unproven; (b) leaves the approval unproven; (c) closes both only with a defined binding.
- *Security/compliance:* (b) anchors content a reviewer may reject — creates revoked-but-anchored artefacts with no status model. (a)/(c) avoid that. TCPA/AC-02.7 verbatim-disclosure proof favours an evidence-root commitment (c) but is not decided by it.
- *Architecture:* (a) one TSA/anchor call post-approval; (b) same, pre-approval, plus re-anchor to prove approval; (c) two timestamps and an evidence-record structure (ERS-style if D-16 → yes).
- *Requirement impact:* FR-054 steps 3–5 wording; FR-055 verification scope; D-12 bindings land in whichever artefact is anchored.
- *Existing code:* none of the three exists; CD-13 must be fixed under any option. (a) is closest to the existing S12 state machine.
- *Migration/back-compat:* no issued anchored certificates exist in evidence → N/A today.
- *Provider neutrality:* all options are anchor-provider-neutral per D-03. N/A as a differentiator.
- *Future D5/D6/D7 verification:* (c) requires two independent timestamp verifications per certificate at D6; (a) one.

**Recommendation**
`RECOMMEND KEEP OPEN — the certificate lifecycle (reject / modify path; how the approval record is bound to the anchored content) is not defined anywhere in V6, and Part 29.1 says the ERS mechanism does not decide it. Choosing an ordering now would be inventing that architecture.`

Evidence finding recorded for the PO, not a recommendation to narrow: (b) is supported by no approved requirement or business document (FRD R-09 and BRD-001 BR-02/AC-02.5 both put approval before issuance) and fails two of the six proof tests. Whether to strike (b) is the PO's call.

**Confidence** HIGH that it must stay open (the lifecycle gap is explicit in V6 Part 29.1 and Part 7).

**Evidence required before approval**
1. A certificate-lifecycle definition covering: evidence captured → reviewer sees → approve / reject / modify → issue → (later) supersede/revoke — stating, for each transition, what is hashed, what is timestamped/anchored and what the verifier must show. This is architecture work; not performed here.
2. D-16 outcome and, if (c) is live, E-02 result (ERS record vs existing `content_hash` + PDF embedding).
3. R-D relying-party model (what the certificate claims), because the ordering determines the claim set.

---

### D-15 — BRD-001 availability

**Decision question**
BRD-001: supply it / treat PRD as top authority.

**Evidence**
- BRD-001 is supplied with this gate: Document ID BRD-001, version 1.0.1, 2026-06-16, "Approved for Development", owner WET, related PRD-001 / FRD-001 / NFRD-001; BR-01..BR-10 with acceptance criteria, assumptions A-01.., constraints C-01..C-08, risks, out-of-scope OOS-01..08.
- Part 7: "PRD remains highest available product source. Do not invent its authority."

**Options** — supply it / treat PRD as top (V6). Supplying it resolves the question as posed.

**Consequences**
- *Product meaning:* BRD-001 becomes the parent authority above PRD-001 for business intent.
- *Proof/evidence integrity:* N/A.
- *Security/compliance:* N/A.
- *Architecture:* N/A.
- *Requirement impact:* authority order changes; no recovered requirement changes by this decision. A follow-on documentation pass must reconcile BR-01..BR-10, AC-nn, A-nn, C-nn, OOS-nn against R-01..R-44 / G01..G52 (this belongs to the existing Part 5 "Document amendments after decisions" package; no new work item is created here).
- *Existing code / migration / provider neutrality / D5–D7:* N/A.

**Two evidence observations (recorded, not resolved; neither reopens the D-scale):**
1. BRD-001 as supplied contains **BR-01..BR-10 only**. V6 Part 38 cites **BR-14** (row 44 WhatsApp), **BR-15** (row 43 storage), **BR-18** (row 45 Config resolver) and **BR-03/05** (row 46 inbound calling) in its "Authoritative requirement" column. Those identifiers are not in BRD-001 v1.0.1 (in BRD-001, BR-03 is the real-time communications suite and BR-05 is the forensic audit trail). The D-levels of rows 43–46 do not depend on these labels (row 45's D4 rests on the S46 plan contract plus the execution record), so no frozen fact is contradicted; but the source of "BR-14/15/18" must be identified in the BRD-001 reconciliation pass before those labels are relied on as authority.
2. BRD-001 internal inconsistency: header says v1.0.1; footer reads "End of BRD-001 v1.0.0". Clerical; note for the owner.
3. For the PO's awareness (already governed, no action here): BRD-001 A-03 names Hedera/Ethereum/private anchoring — superseded by D-03 (provider-neutral, NEW PO DECISION); BRD-001 OOS-02 puts native WhatsApp Business API out of scope for v1.0 — row 44 WhatsApp is in the tracker at D2/D3; BRD-001 OOS-01 is consistent with D-09 Option B.

**Recommendation**
`RECOMMEND OPTION "supply it" — accept BRD-001 v1.0.1 as the supplied parent authority above PRD-001, with the reconciliation of its contents against the recovered baseline recorded as follow-on documentation work.`

**Confidence** HIGH for the availability question; the reconciliation itself is not done and is not claimed.

**Evidence required before approval** NONE.

---

### D-16 — RFC 4998 ERS / ETSI LTV as evidence-record substrate (CR-07)

**Decision question**
Adopt RFC 4998 ERS / ETSI LTV as the evidence-record substrate (CR-07): yes / no / investigate (E-02).

**Evidence**
- Recovered: R-05/R-06/R-08 require SHA-256, TSA tokens verifiable with `openssl ts`, AES-256 — algorithms fixed in FR-054/NFR-020 (Part 2b notes this as the agility problem).
- Code-verified (Part 41): chain stops at SHA-256 over a 7-field JSON; no algorithm identifier; no TSA; no anchor.
- Research finding / proposal: Part 13.5 item 1 ("biggest omission"), 29.1, 29.2, CR-07, Part 31 H1 — ERS references S-56/S-57 are secondary; R-C primary-source revalidation is still RESEARCH REQUIRED. Part 33.2 item 17(e): mechanism is a standards-adoption problem; operational/legal longevity is open (R-E).
- E-02 (does an ERS record integrate with existing `content_hash` and PDF embedding without re-issuing?) — not done.
- Part 35.1 lists "bespoke long-term evidence formats" as REJECTED — reviewer's classification, not a PO decision.

**Options** — yes / no / investigate (E-02), as in V6.

**Consequences**
- *Product meaning:* yes = evidence verifiable decades out, renewal before algorithm deprecation; no = bespoke format (needs its own longevity answer); investigate = decide after E-02/R-C.
- *Proof/evidence integrity:* yes/investigate strengthen; no leaves G41 DESIGN with no standard.
- *Security/compliance:* yes aligns with eIDAS/ETSI (per research, unrevalidated); introduces TSA-key-compromise handling and renewal operations (R-E).
- *Architecture:* yes commits the evidence-record structure before D-06 is resolved; investigate commits a read-only prototype only.
- *Requirement impact:* yes converts CR-07 direction into an approved direction before 19-field expansion — the exact move this gate must not make; investigate creates none.
- *Existing code:* none of it conforms; E-02 is read-only against the S12 payload.
- *Migration:* no issued certificates in evidence → N/A today; E-02 asks precisely the re-issue question for the future.
- *Provider neutrality:* ERS is TSA-neutral (RFC 3161 layer); positive.
- *D5–D7:* yes defines the D6 verification artefacts (ERS chain verifies).

**Recommendation**
`RECOMMEND OPTION "investigate (E-02)" — the direction is well supported, but "yes" would approve a research finding as a product direction before R-C revalidation and before E-02 shows it fits the existing payload. Part 46's "with yes as default direction" wording is not carried: no default is pre-loaded.`

**Confidence** HIGH that "no" is unsupported and "yes" is premature; MEDIUM on how long E-02/R-C take.

**Evidence required before approval** NONE for "investigate". For a later "yes": E-02 result; R-C primary-source read of RFC 4998 / ETSI EN 319 102-1 / ETSI TS 119 312.

---

### D-17 — Part 26 autonomy-ceiling table as policy

**Decision question**
Accept the Part 26 autonomy-ceiling table as policy: accept / amend per row.

**Evidence**
- Part 26 table: A5 for worker restart/queue/cache/rollback and provider failover within configured adapters; A4 for dependency bumps and code changes to adapters/pipeline/UI; **A2** for auth/RBAC/keys, certificate crypto/TSA/anchoring/evidence schema/verifier, consent/DNC/retention/redaction, FR-040 verdict logic/prompts, tenant configuration; A4 for knowledge promotion (promotion human).
- Code-verified: no autonomy or agent code exists; Part 46: "nothing at A3 is near".
- Research basis S-14/S-18/S-27 is secondary (R-C pending). ARCHITECTURE PROPOSAL label.
- D-04 (FR-040 integrity over availability) is consistent with the A2 ceiling on verdict logic.

**Options** — accept / amend per row.

**Consequences**
- *Product meaning:* TalkProof does not self-modify its proof machinery, security or consent logic; operational self-healing is bounded.
- *Proof/evidence integrity:* positive — A2 on evidence/crypto.
- *Security/compliance:* positive — default-deny posture; agent identity/budget rules follow only if CR-18 is later approved.
- *Architecture:* none now; constrains Parts 24–26 design when built.
- *Requirement impact:* none — the table becomes a requirement only through CR-18 (D-22, deferred).
- *Existing code:* none affected.
- *Migration / provider neutrality:* N/A.
- *D5–D7:* N/A.

**Recommendation**
`RECOMMEND OPTION "accept" — as a governing policy for any future automation work, explicitly not as a requirement; the table is conservative, so accepting it adds no risk, while amending upward would need evidence that does not exist.`

**Confidence** MEDIUM — the research citations are unrevalidated, but the policy direction is defensive and reversible per row.

**Evidence required before approval** NONE.

---

### D-18 — Decision Ledger on OTel GenAI (CR-15)

**Decision question**
Decision Ledger on OTel GenAI with persisted rows and UNKNOWN default (CR-15): yes / amend (keep M22 and extend).

**Evidence**
- Recovered scope: M22 — every AI provider call ledgered. Code-verified: M22 ledgers M07 only; model name only, no version; orchestrator's real Anthropic/OpenAI/Gemini calls bypass it (CD-11). **CD-11 is a conformance defect against existing M22 scope regardless of D-18.**
- Part 21: ARCHITECTURE PROPOSAL; OTel GenAI semantic conventions are "Development, no stable release as of Aug 2026" (S-52, secondary); DERIVED REQUIREMENT (certified-verdict provenance in payload) is CR-04, not approved.
- CR-15 is candidate-grade only (C05); not expanded; not selected (D-22 pending).

**Options** — yes / amend, as in V6.

**Consequences**
- *Product meaning:* yes = one persisted decision ledger across M07 and the orchestrator, UNKNOWN-default outcomes; amend = M22 extended in place.
- *Proof/evidence integrity:* both improve verdict reproducibility; neither is needed to fix CD-11.
- *Security/compliance:* content capture per tenant policy; no secrets in rows (CR-15 fields).
- *Architecture:* yes introduces a new schema pinned to an unstable convention version; amend keeps the existing table.
- *Requirement impact:* **both options are requirement changes** — approving either here converts a candidate into a requirement before analysis.
- *Existing code:* `AIInteractionLedger` exists (M07); CD-11 fix is independent.
- *Migration:* yes requires M22 rows to map to the new schema; amend does not.
- *Provider neutrality:* OTel is provider-neutral; positive for either.
- *D5–D7:* a persisted ledger is the evidence source for D6 verdict reproducibility.

**Recommendation**
`RECOMMEND KEEP OPEN — dependent on D-22: CR-15 must first be selected for analysis and expanded to its 19 fields; D-18 is then the approval of that analysed requirement. Part 46's "fold CD-11 fix into it" is not carried: CD-11 is a conformance item against existing M22 scope and must not wait on D-18.`

**Confidence** HIGH that it cannot be approved at this gate; MEDIUM on which option will survive analysis (the unstable OTel status may favour "amend").

**Evidence required before approval** CR-15 19-field expansion (after D-22); R-C on OTel GenAI semconv status; a stated mapping from existing M22 rows.

---

### D-19 — Cross-tenant knowledge aggregation boundary

**Decision question**
Cross-tenant knowledge aggregation boundary: none / anonymised operational knowledge only / per-tenant opt-in.

**Evidence**
- Code-verified: tenancy is application-layer scoping; RLS helpers exist but are never called, no policies/migration (row 1 D2, EV-04). No learning, promotion or aggregation code exists.
- BRD-001 R-04 names PostgreSQL RLS as the Tier-A cross-contamination mitigation (business intent, not code).
- Part 23 (ARCHITECTURE PROPOSAL) makes cross-tenant promotion contingent on this decision; CR-22 candidate.

**Options** — none / anonymised operational only / per-tenant opt-in.

**Consequences**
- *Product meaning:* none = no tenant's data informs another tenant, in any form, until lifted; the others create a shared-learning capability.
- *Proof/evidence integrity:* N/A (learning is outside the certified path per D-04/D-20).
- *Security/compliance:* none is the only option with no new data-protection analysis; "anonymised" requires a defined anonymisation standard and GDPR basis; "opt-in" requires consent/contract wording.
- *Architecture:* none constrains Part 23 to per-tenant scope.
- *Requirement impact:* none creates no requirement; the other two create new data-handling requirements.
- *Existing code:* none affected.
- *Migration:* N/A.
- *Provider neutrality:* N/A.
- *D5–D7:* a lift of "none" should not be considered before row 1 (RLS) is at D5 — otherwise isolation cannot be evidenced.

**Recommendation**
`RECOMMEND OPTION "none" — until row 1 (Tier-A RLS) reaches D5 and CR-22 has been analysed; reopen trigger recorded, not scheduled.`

**Confidence** HIGH.

**Evidence required before approval** NONE.

---

### D-20 — CLM / model-portfolio gate (Part 19.2)

**Decision question**
CLM / model-portfolio gate accepted as the condition for any fine-tune: accept / set N / reject CLM entirely.

**Evidence**
- Part 19.2 gate (five conditions; N to be set by PO; E-04 computes a starting point; FR-040 verdicts excluded per D-04). Code-verified: zero attested traffic, no Decision Ledger → the gate cannot pass today. V3 position: DEFERRED with reopen trigger, not rejected; "Company Language Model" as a goal is in the reviewer's REJECTED bucket.

**Options** — accept / set N / reject entirely.

**Consequences**
- *Product meaning:* accept = no fine-tune is proposed until the gate holds; set N = same plus a number; reject = TalkProof never trains.
- *Proof/evidence integrity:* all options keep FR-040 verdicts outside training (D-04).
- *Security/compliance:* N/A now.
- *Architecture:* accept constrains Part 19 to a gate; nothing is built.
- *Requirement impact:* none for accept; "set N" with no data would be a number without evidence; "reject" is a product decision V6 gives no evidence for.
- *Existing code / migration / provider neutrality:* N/A.
- *D5–D7:* N/A.

**Recommendation**
`RECOMMEND OPTION "accept" — the gate as the condition, with N left unset until E-04 has Cost Ledger data.`

**Confidence** HIGH — accepting commits nothing and preserves the reopen path.

**Evidence required before approval** NONE (for "set N" later: E-04).

---

### D-21 — Standalone published verifier (CR-12) becomes a requirement

**Decision question**
Standalone published verifier (CR-12) becomes a requirement, changing V2's "any CLI is DESIGN": yes / no.

**Evidence**
- Recovered: R-06 (NFR-024, Must Have) — TSA verification "must work offline using standard tools (e.g., `openssl ts`)"; R-36 (FR-055) — in-browser SHA-256 of downloaded PDF, offline after download. **BRD-001 AC-02.6**: "verifiable offline (hash + timestamp verify without platform access)". V2 Part 2b: any offline CLI is DESIGN because FR-055 does not require it.
- Code-verified (Part 41): no artefact leaves the server that a third party can hash; client verification is an authenticated endpoint recomputing from its own DB; offline verification D1.
- Part 29.4 (C08): "No candidate requirement is drafted until R-D is done" — the relying-party model precedes CR-12 and any "proof" claim.
- Part 33.2 item 15: open-source ERS/TSA verifiers already exist; TalkProof's edge is operating, not authoring.

**Options** — yes / no.

**Consequences**
- *Product meaning:* yes = a published, versioned verifier that works without TalkProof; no = verification stays at PDF hash + `openssl ts` as already required.
- *Proof/evidence integrity:* the already-required offline verification (R-06, R-36, AC-02.6) is at D1 — that gap exists under either option. CR-12 adds publication, versioning and ERS/anchor/chunk validation beyond it.
- *Security/compliance:* verifier supply chain (signed releases, CR-13) becomes a surface.
- *Architecture:* depends on D-06 and D-16 (what the verifier must validate).
- *Requirement impact:* yes creates a requirement — not permitted at this gate before selection and 19-field expansion.
- *Existing code:* none.
- *Migration:* verifier version must be recorded in every certificate from first issue.
- *Provider neutrality:* positive — removes the live-provider dependency (CR-09).
- *D5–D7:* a standalone verifier is how D6 "independently verifiable" would be evidenced.

**Recommendation**
`RECOMMEND KEEP OPEN — dependent on D-22 (selection of CR-12 for analysis) and on R-D (relying-party model), which V6 itself places before any verifier requirement is drafted.`

**Confidence** HIGH that it cannot be approved here; MEDIUM–HIGH that the analysis will support "yes", given three existing sources already require offline verifiability.

**Evidence required before approval** R-D output; CR-12 19-field expansion; D-06 and D-16 outcomes (verifier scope).

---

### D-22 — Which CR-01..CR-23 are selected for requirements analysis

**Decision question**
Which of CR-01..CR-23 are selected for requirements analysis (not approval of CR text as written): per row.

**Evidence**
- Part 32: all 23 are NEW REQUIREMENT CANDIDATE, candidate-grade only (C05); several are compressed ("Rest: as CR-09"); CR-23 has no requirement text yet.
- Code-verified anchors: G01 code-corroborated at scale (20 rows below tracker); no adapter integrated, S33 "best example" unintegrated (G45); consent never enforced (G36/CD-08); real AI calls not ledgered (G40/CD-11); no FR/NFR traced to a check (G02).
- Existing PO decisions: D-14 accepted all ten Part 2b areas into analysis — CR-05/06/07/08/09/10/11/12/13 are those areas; D-12 accepted binding scope (CR-04); D-13 accepted provider configuration (CR-03, CR-21).
- Research gates: Part 29.4 — no CR-04/CR-12 drafting until R-D; CR-23 after R-D/R-E; CR-10 depends on a mechanism D-12 did not accept and on E-09.
- Part 46's "first six" (CR-01, 03, 07, 12, 15, 23) is the reconciler's ordering, unapproved.

**Options** — per row (select for analysis / not now), as in V6.

**Per-row recommendation (selection into analysis only; no CR is approved; no ID is issued):**

| CR | Candidate | Grounding | Recommendation |
|---|---|---|---|
| CR-01 | Completion-level governance | G01 code-corroborated; brief Req 1 | **SELECT** |
| CR-02 | FR/NFR → executable checks | G02; R-42 | **SELECT** |
| CR-03 | Adapter standard + conformance harness | G45; brief Req 3; D-13 | **SELECT** |
| CR-04 | Verdict provenance in certificate | D-12 scope accepted; Part 21 derived | **SELECT — expansion gated on R-D** |
| CR-05 | Regulation/policy version provenance | D-14 area | **SELECT** |
| CR-06 | Trusted-time provenance classes | D-14 area; NFR-024/056 | **SELECT** |
| CR-07 | ERS evidence records | D-14 area | **CONDITIONAL on D-16** (select if D-16 ≠ "no"; expansion after E-02) |
| CR-08 | Crypto agility / PQ | D-14 area; depends CR-07 | **CONDITIONAL on D-16**; E-07 input |
| CR-09 | Provider-exit verifiability | D-14 area; R-41 | **SELECT** |
| CR-10 | Chunk-level commitments | D-14 area; mechanism not accepted by D-12; E-09 | **DEFER** until D-06/D-16 fix the mechanism and E-09 runs |
| CR-11 | Tenant exit with continued verification | D-14 area; depends CR-09, CR-12 | **CONDITIONAL on D-21** |
| CR-12 | Standalone published verifier | D-14 area; R-06/R-36/AC-02.6 | **CONDITIONAL on R-D** (feeds D-21) |
| CR-13 | SBOM/AIBOM/SLSA | D-14 area | **SELECT** |
| CR-14 | Product State Model | brief §6; CR-01/17/20 depend on it | **SELECT — under D-24 constraint** |
| CR-15 | Decision Ledger | M22 scope + CD-11; brief §13 | **SELECT** (feeds D-18) |
| CR-16 | Quality/Cost ledgers | depends CR-15; no data | **DEFER** until CR-15 analysed |
| CR-17 | Gap-detection comparators | brief §7; depends CR-14 | **DEFER** to second wave |
| CR-18 | Autonomy ceilings as requirement | D-17 policy suffices; nothing near A3 | **DEFER** |
| CR-19 | External awareness | depends CR-14, CR-17 | **DEFER** |
| CR-20 | Scorecard | depends CR-01/14/16/17; D-23 internal | **DEFER** |
| CR-21 | Tenant intelligence policy | extends D-13; depends CR-15 | **DEFER** to second wave |
| CR-22 | Knowledge promotion governance | D-19 "none"; no learning | **DEFER** |
| CR-23 | Certificate status/correction lifecycle | Part 29.5; no text; R-D/R-E | **SELECT — expansion gated on R-D and R-E** (and informs D-06) |

Wave summary: **SELECT now = 10** (CR-01, 02, 03, 04*, 05, 06, 09, 13, 14, 15, 23* — *gated expansion); **CONDITIONAL = 4** (CR-07, 08 on D-16; CR-11 on D-21; CR-12 on R-D); **DEFER = 8** (CR-10, 16, 17, 18, 19, 20, 21, 22). The PO may trim the first wave; every selection is analysis effort only.

**Consequences**
- *Product meaning:* none until analysed requirements are approved.
- *Proof/evidence integrity:* the selected set covers every Part 41 "missing binding" except the ordering (D-06).
- *Security/compliance:* CR-13 adds supply-chain attestation to analysis.
- *Architecture:* none changed; CR-14 is constrained by D-24.
- *Requirement impact:* **zero** — selection is not approval; IDs are issued only by the governance process after 19-field expansion.
- *Existing code:* none.
- *Migration / provider neutrality:* N/A at selection.
- *D5–D7:* CR-01/CR-03 define how D5+ will later be evidenced.

**Recommendation**
`RECOMMEND OPTION "per row, as tabled above".`

**Confidence** MEDIUM — the grounding of each SELECT row is HIGH; the size of the first wave is a PO capacity judgement.

**Evidence required before approval** NONE for selection; D-16 and D-24 outcomes determine the CONDITIONAL tags.

---

### D-23 — Scorecard (CR-20) customer-facing

**Decision question**
Scorecard as customer-facing: yes / internal only.

**Evidence**
- Part 13.5 item 9 and Part 27 (research finding / proposal; "sales collateral" is a forecast). Code-verified: no scorecard exists; D5–D7 = 0 across all 46 rows; Part 41: TalkProof "may not be described as tamper-proof, blockchain-certified, independently verifiable or production-certified on this evidence".

**Options** — yes / internal only.

**Consequences**
- *Product meaning:* yes = customers see per-capability D-levels; internal = governance artefact only.
- *Proof/evidence integrity:* a customer-facing scorecard with no D5+ rows would publish the Part 41 statement as product fact.
- *Security/compliance:* exposure of security posture rows to customers needs its own analysis.
- *Architecture:* none now.
- *Requirement impact:* none for internal; yes adds a customer-facing requirement to CR-20.
- *Existing code / migration / provider neutrality / D5–D7:* N/A.

**Recommendation**
`RECOMMEND OPTION "internal only" — reopen when at least one capability reaches D5 with recorded evidence.`

**Confidence** HIGH.

**Evidence required before approval** NONE.

---

### D-24 — PSM storage position: Postgres-first

**Decision question**
PSM storage position: Postgres-first, graph only after E-03 — accept / direct otherwise.

**Evidence**
- Part 16.3 (ARCHITECTURE PROPOSAL): relational versioned rows; append-only event table; graph as a projection via recursive SQL; graph DB only if E-03 proves traversal cost. Code-verified: PostgreSQL + Alembic is the existing backend stack. Brief §37: no graph merely because fashionable.

**Options** — accept / direct otherwise.

**Consequences**
- *Product meaning:* N/A (internal).
- *Proof/evidence integrity:* N/A.
- *Security/compliance:* fewer stores to secure.
- *Architecture:* constrains CR-14 to the existing stack; no new database category.
- *Requirement impact:* none; CR-14 is still a candidate.
- *Existing code:* consistent with it.
- *Migration:* none.
- *Provider neutrality:* N/A.
- *D5–D7:* N/A.

**Recommendation**
`RECOMMEND OPTION "accept".`

**Confidence** HIGH — it is the conservative, reversible default on the stack already in use.

**Evidence required before approval** NONE.

---

### D-25 — Procure continuous AI pentest vs build

**Decision question**
Procure continuous AI pentest rather than build (Part 27): buy / build / defer.

**Evidence**
- Part 27 / 13.2 (research finding: buy; building pentest tooling in-house is in the reviewer's REJECTED bucket). Code-verified: no deployment, staging or E2E artefact exists in any repo (Part 44; EV-04). There is nothing to pentest.

**Options** — buy / build / defer.

**Consequences**
- *Product meaning:* N/A now.
- *Proof/evidence integrity:* N/A.
- *Security/compliance:* buying now spends budget on an undeployed system; deferring postpones nothing real.
- *Architecture:* none.
- *Requirement impact:* none for defer.
- *Existing code / migration / provider neutrality:* N/A.
- *D5–D7:* a pentest record will be D7 evidence when a deployment exists.

**Recommendation**
`RECOMMEND OPTION "defer" — until a deployed staging/production environment exists (EV-04 evidence); the buy-not-build direction is noted as the reviewer's position, not decided.`

**Confidence** HIGH.

**Evidence required before approval** NONE.

---

### D-26 — E-01 before any CR work

**Decision question**
Code-verification pass (E-01) scheduled before any CR work begins: close as satisfied / keep open.

**Evidence (tested, not assumed)**
- Required evidence per Part 33.1 E-01: inspect the repositories for all 46 Part 3 capability rows (brief §46, Part 12 plan).
- Delivered: `TALKPROOF_E01_CODE_VERIFICATION_V001_20261004_1945.md` against the three supplied ZIPs (backend / admin / Flutter); Part 38 carries 46 rows, each with an E-01 sheet reference, a code classification, a confidence and a disposition; Part 40 CD-01..CD-17; Part 41 fourteen stages; Part 43 D4 audit; Part 44 test execution (1,465/0 backend, 239/0 admin; Config Resolver 24/0/0 reproduced on PostgreSQL 16.15; the 1,465 figure reproduced in the same environment).
- E-01's own errors were caught and corrected through the reviewed lineage (R-36; rows 32 and 45 under the authoritative scale) — the verified state the PO decides on is V6, not raw E-01.
- Bounded limits, labelled: row 41 UNABLE TO VERIFY beyond D3 (custom-domain provisioning — a limit of the supplied repositories, not an uninspected row); Flutter `flutter test` and admin Playwright not run (runtime, recorded as EV-05 — outside a code-inspection pass).
- No CR work has begun (Part 48 "Not done in V6"; V6 Gate).
- V5 Gate Review R-D26: E-01 being done satisfies the decision; the PO has not said so. That is a recommendation only.

**Options** — close as satisfied / keep open.

**Consequences**
- *Product meaning:* N/A.
- *Proof/evidence integrity:* closing records that CR work starts from a code-verified baseline, which is what the decision asked for.
- *Security/compliance / architecture:* N/A.
- *Requirement impact:* none; closing D-26 does not authorise any CR — D-22 does.
- *Existing code / migration / provider neutrality:* N/A.
- *D5–D7:* N/A.

**Recommendation**
`RECOMMEND CLOSE AS SATISFIED — E-01 was executed on all 46 rows before any CR work, its results were independently reviewed and corrected into V6, and its remaining limits are bounded and labelled (row 41; EV-05).`

**Confidence** HIGH.

**Evidence required before approval** NONE.

---
## PHASE 5 — PO DECISION SHEET

| Decision | Recommendation | Confidence | Can PO decide now? | Dependency / missing evidence | Scope effect | Requirement change? |
|---|---|---|---|---|---|---|
| D-06 | KEEP OPEN — lifecycle architecture required | HIGH | No | Certificate-lifecycle definition; D-16; E-02; R-D | Proof-chain wording | No (none yet) |
| D-15 | OPTION "supply it" — BRD-001 v1.0.1 accepted as parent authority | HIGH | Yes | None (reconciliation is follow-on documentation) | Authority order only | No |
| D-16 | OPTION "investigate (E-02)" | HIGH | Yes | None for investigate | Research only | No |
| D-17 | OPTION "accept" (policy, not requirement) | MEDIUM | Yes | None | Governance | No |
| D-18 | KEEP OPEN — dependent on D-22 (CR-15 analysis) | HIGH | No | CR-15 19-field expansion; R-C | Ledger requirement | Would be — later |
| D-19 | OPTION "none" | HIGH | Yes | None | Constraint | No |
| D-20 | OPTION "accept" (N unset) | HIGH | Yes | None | Constraint | No |
| D-21 | KEEP OPEN — dependent on D-22 and R-D | HIGH | No | R-D; CR-12 expansion; D-06/D-16 | Verification requirement | Would be — later |
| D-22 | OPTION "per row as tabled" (10 select / 4 conditional / 8 defer) | MEDIUM | Yes | D-16, D-24 set the conditional tags | Analysis effort only | No |
| D-23 | OPTION "internal only" | HIGH | Yes | None | None | No |
| D-24 | OPTION "accept" | HIGH | Yes | None | Design constraint | No |
| D-25 | OPTION "defer" | HIGH | Yes | None | None | No |
| D-26 | CLOSE AS SATISFIED | HIGH | Yes | None | Unblocks D-22 only | No |

### A — READY FOR PO DECISION NOW (10)
D-15 · D-26 · D-16 · D-17 · D-19 · D-20 · D-22 · D-23 · D-24 · D-25

### B — KEEP OPEN — MISSING EVIDENCE (0)
None. BRD-001 was the only missing source material and it is now supplied.

### C — KEEP OPEN — DEPENDENT ON ANOTHER DECISION (2)
- **D-18** — depends on D-22 selecting CR-15 and on its 19-field expansion; also R-C on OTel GenAI status. CD-11 proceeds independently as an M22 conformance item.
- **D-21** — depends on D-22 selecting CR-12, on R-D (relying-party model), and on D-06/D-16 for verifier scope.

### D — KEEP OPEN — ARCHITECTURE / RESEARCH REQUIRED (1)
- **D-06** — work required (not performed here, not authorised by this artifact): (1) a certificate-lifecycle definition covering capture → review → approve/reject/modify → issue → supersede/revoke, stating per transition what is hashed, timestamped, anchored and shown by the verifier; (2) E-02 if option (c) is live; (3) R-D relying-party claim set. The ordering is decided after that, against the proof-proposition test in Phase 4, not by document seniority.

---

## PHASE 6 — ASK THE PRODUCT OWNER

For each item in **A**, please approve / reject / change the recommended option. Nothing is applied until you answer.

| # | Decision | Recommended option | Your answer |
|---|---|---|---|
| 1 | D-15 | Accept BRD-001 v1.0.1 as parent authority; reconciliation against R-01..R-44 is follow-on documentation work; BR-14/15/18 label source to be identified in that pass | |
| 2 | D-26 | Close as satisfied by E-01 (as corrected into V6) | |
| 3 | D-24 | Accept Postgres-first; graph only after E-03 | |
| 4 | D-19 | None — no cross-tenant aggregation until row 1 RLS reaches D5 and CR-22 is analysed | |
| 5 | D-20 | Accept the Part 19.2 gate; N unset until E-04 | |
| 6 | D-23 | Internal only; reopen at first D5 | |
| 7 | D-25 | Defer until a deployment exists | |
| 8 | D-17 | Accept the Part 26 ceiling table as policy (not as a requirement) | |
| 9 | D-16 | Investigate — authorise E-02 (read-only prototype against the S12 payload) and R-C primary-source read; no default direction pre-loaded | |
| 10 | D-22 | Per row as tabled: SELECT CR-01, 02, 03, 04*, 05, 06, 09, 13, 14, 15, 23* (*expansion gated on R-D/R-E); CONDITIONAL CR-07, 08 (D-16), CR-11 (D-21), CR-12 (R-D); DEFER CR-10, 16, 17, 18, 19, 20, 21, 22 — trim as you see fit | |

D-06, D-18 and D-21 stay open. No decision is requested on them.

---

## CLOSING COUNTS

- 13 decisions accounted for: **YES** (D-06, D-15, D-16, D-17, D-18, D-19, D-20, D-21, D-22, D-23, D-24, D-25, D-26)
- READY FOR PO DECISION NOW: **10**
- KEEP OPEN — MISSING EVIDENCE: **0**
- KEEP OPEN — DEPENDENCY: **2**
- KEEP OPEN — ARCHITECTURE/RESEARCH: **1**
- New requirements created = **0**
- FR/NFR IDs issued = **0**
- Sprints created = **0**
- Architecture changed = **NO**
- Code changed = **NO**
- V6 changed = **NO**
- V7 created = **NO**

**STOP. Waiting for Product Owner decisions.**
