# Proposed two-repository Git structure
Date: 8 October 2026
Status: proposed; no repositories created.

## Names and visibility
ai-engineering-portfolio: public when reviewed and ready; external showcase and reusable demonstrator code.
ai-engineering-workbench: private; working sessions, learning paths, decision history and private configuration references.
ContextLedger is the provisional project name, not a required third repository.

## Public repository
```text
ai-engineering-portfolio/
  README.md
  LICENSE                         # select explicitly; not assumed
  SECURITY.md
  CONTRIBUTING.md
  AGENTS.md
  .gitignore
  .env.example                    # placeholders only
  pyproject.toml
  src/context_ledger/             # single source of reusable product code
    ingest/
    records/
    search/
    context/
    cli/
  tests/
  examples/synthetic/
  schemas/
  evaluations/
    synthetic_cases/
    reports/
  docs/
    architecture/
    decisions/
    limitations.md
    case-studies/
    demo-guide.md
  .github/
    workflows/ci.yml
    pull_request_template.md
```
README documents problem, scope, setup, actual demo status, limitations and personal ownership. No actual private conversation in examples or CI fixtures.
Do not fabricate a public 'production' claim. A local CLI is a local CLI until deployment is demonstrated.

## Private repository
```text
ai-engineering-workbench/
  README.md
  AGENTS.md
  .gitignore
  protocol/
    existing-git-turn-protocol.md  # import actual protocol; do not invent it
    session-start.md
    session-end.md
    publication-checklist.md
  role-target/
    decision.md
    vacancy-matrix.csv
    gap-register.csv
    readiness-rubric.md
  teachers/
    chatgpt/
      proposal.md
      plan.md
      lessons/
      exercises/
      assessments/
    claude/
      proposal.md
      plan.md
      lessons/
      exercises/
      assessments/
    perplexity/
      proposal.md
      plan.md
      lessons/
      exercises/
      assessments/
  learner/
    attempts/
    reflections/
    time-log.csv
    evidence-index.csv
  conversations/
    manifests/
    raw/                          # only sensitivity-reviewed captures
    normalized/
  sessions/YYYY/MM/DD/
  context/
    current-state.md
    approved-decisions.md
    open-questions.md
    handovers/
  decisions/
  reviews/
  evidence/
  applications/                   # private CV/application drafts
  publications/                   # manifests, approvals, public commit links
  config/
    corpus.example.yaml           # no credentials or raw sensitive values
```
Runtime databases, indexes and caches are outside tracked paths. Public code reads a private corpus through an explicit local path or protected service; the public repository never embeds the private corpus.

## Code ownership boundary
Reusable product implementation lives once, in the public repository after safety review; develop private-first if necessary until safe publication. Workspace holds private records and configuration, not a second diverging copy of product code.
Record the exact product commit/release used for private runs. Two clones can be adjacent locally; do not silently mix their histories. If code is not safe for public release, keep a documented private staging area and publish selected clean snapshots only after approval.

## Proposed Git workflow extension
The existing user protocol governs. These are requirements to reconcile with it, not a claim that it was inspected.
1. Start: record repository, branch, HEAD, git status, task and files actually read.
2. Branch by task and assistant, for example docs/perplexity-role-review or feat/chatgpt-context-cli.
3. One writer for a given implementation task; other assistants can teach independent lessons and review.
4. Scoped changes; no destructive cleanup, force push, dependency churn or cross-repository copying without agreement.
5. Verify with actual commands. Distinguish not run, failed and passed.
6. Open review/PR with learner ownership and assistant assistance recorded.
7. Merge through the user's normal approval protocol.
8. End with status, commit, evidence, unresolved issues and handover.
Naming examples are conventions to approve, not mandatory replacements for existing branch rules.

## Session record template
session_id:
assistant:
project:
objective:
repository:
branch:
starting_commit:
files_actually_read:
context_pack_id:
learner_attempt:
assistance_received:
changes:
commands_run:
observed_results:
commands_not_run:
understanding_demonstrated:
unresolved_questions:
decisions_proposed:
decisions_approved_by_user:
ending_commit:
next_action:

## Context provenance rules
Original captures are retained where safe. Each normalised message has a stable ID, platform, role, timestamp status, capture method and original-source reference.
Summaries are derived records. They link to sources and do not overwrite originals.
Assistant statements remain claims until verified. Suggestions remain proposed until accepted. Corrections link to what they supersede.
A context pack identifies corpus version, relevant sources, decisions, conflicts, omissions and missing imports.
No assistant may say it has read another assistant's session unless it actually accessed that record.

## Public publication checklist
- Explicit allowlist of files; no whole-workspace synchronisation.
- Inspect content and history for secrets and personal information.
- Review synthetic fixtures for accidental real data.
- Confirm rights to publish any third-party or employer material.
- Preserve accurate attribution and test-status labels.
- Record private source references only in private publication manifest.
- Public case study links to safe public commits, not private sessions.
- Obtain approval for remote changes.

## Initial sequence
1. Approve the role-target recommendation and repository names separately.
2. Resolve GitHub account/organisation and inspect actual Git-turn protocol.
3. Agree visibility and initial files.
4. Request exact-action confirmation before remote creation/writes.
5. Import supplied conversation material with capture/completeness labels.
6. Start independent teacher proposals and a learner baseline.
7. Build the smallest searchable, source-linked context CLI.
