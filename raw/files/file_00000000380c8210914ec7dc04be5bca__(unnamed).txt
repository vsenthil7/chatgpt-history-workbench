# Portfolio Audit Playbook

Derived from 39 defects found in OnCall Copilot across 28 releases on 13 September 2026 —
11 of them critical or live-blocking, and **nearly all invisible to a 100% coverage gate**.
Nine sibling products were built with the same patterns and have not had this applied.

Run `node audit.mjs <repo>` for the mechanical half, then work the judgement half below.
The script reports **suspects, not verdicts** — every expensive defect was a contract or
integration mismatch that no checker could have decided on its own.

---

## Why coverage missed all of this

Each defect below sat in a module with 100% coverage. Coverage measures whether a line
*executed during a test*, never whether a user can reach it, whether anything calls it, or
whether it matches the platform's real contract.

| Class | What it looked like | OnCall example |
| --- | --- | --- |
| Orphan module | Fully tested, nothing imports it | Five features unreachable; the live slash handler was a stub returning a string |
| Read/write split | Reads one store, writes another | Dashboard read from the repository; incidents were written to an in-process Map |
| Promise without a gate | State maintained, never enforced | Read-only on failed payment set everywhere, enforced nowhere; plan limits never counted |
| Claim without a caller | Module exists, no path calls it | "Encryption at rest" on the trust page; tokens stored in plaintext |
| Scope creep on "fixed" | Correct for one condition, not the deployed one | Id collision fixed for restarts, still live under two replicas |
| Circular evidence | Fake written to match your own code | A self-written Pg fake hid a foreign-key defect for six sprints |
| Platform contract | Your code is fine; the platform disagrees | 3-second slash-command ack; 12-hour token TTL; silent Block Kit truncation |

---

## The judgement half — eight checks, roughly 90 minutes per product

**1. Reachability.** For every story marked Done, name the user action that reaches it. If you
cannot, it is *module-complete*, not done. OnCall's Done count fell 77 → 70 on this check, then
earned its way back by building the missing surfaces.

**2. Read/write pairing.** For each store, list what writes to it and what reads from it. If a
read path has no matching write path, the feature is permanently empty in production.

**3. Promise tracing.** Open the trust page, pricing page and help centre. For each claim, name
the line of code that *refuses* what the claim forbids. A flag set is not a gate.

**4. Platform contract.** Read the platform's own docs for timing limits, retry behaviour,
token lifetimes and payload caps — then check your code against them, not against your memory.
This found a live-blocking defect (duplicate incident channels from a slow ack) that no test
could see.

**5. Restart and two-replica behaviour.** For every counter, cache and ledger: what happens on
restart, and what happens when a blue/green deploy runs two instances at once? Check id
generation and any scheduled job in particular.

**6. Real database.** Run the actual migrations against pg-mem or a real Postgres. Foreign keys,
NOT NULL columns and ON CONFLICT semantics are where hand-written fakes lie to you.

**7. Artifact accuracy.** Does the README describe the current directories? Does every route in
the manifest exist? Does the runbook's rollback claim survive a restart? These are read by
reviewers before anything else.

**8. Adversarial pass.** Forge a signature, replay a request, pass another tenant's id, call an
admin route as a member, submit junk. Roughly 18 cases; it found a 500-instead-of-400 that would
have paged someone on malformed input.

---

## Suggested order across the portfolio

Risk-first, because these classes hide the most damaging defects:

1. **Promise tracing** (check 3) — it is the shortest check and catches the ones with customer
   or legal consequences: retention, encryption, billing limits.
2. **Caller audit** (`audit.mjs` A1 + check 1) — mechanical, and it found the single largest
   problem in OnCall.
3. **Real database** (check 6) — fifteen minutes, and it found a critical foreign-key defect.
4. **Restart and replica** (check 5) — only matters if you deploy, which you will.
5. The rest as time allows.

---

## Honest notes on the tool

- It flags patterns, and some flags are correct-by-design. Run against OnCall Copilot after all
  39 fixes it still reports 4 areas: two genuine build-time libraries, in-memory state that is
  deliberate behind adapters, and five *optional* collaborators that are optional so tests can
  omit them but are required in practice at boot. That is the intended behaviour — it tells you
  where to look, and you decide.
- It cannot see contract mismatches with a platform, missing surfaces, or a promise phrased in
  words it does not match. Those need checks 1, 3 and 4.
- A clean run means nothing on its own. Every one of the 39 defects coexisted with a green suite.
