---
type: Meeting
title: ADR question record, ASFU chapter governance structure (2026-11-25)
description: Question record for the first ASFU ADR, chapter governance structure. Premises, rounds, defaults.
project: university-outreach
status: draft
generated:
  by: claude-code/claude-sonnet-5-5
  at: 2026-11-25T16:10:00Z
last_modified: 2026-11-25
---

# ADR question record: chapter governance structure

Mode: new. Questions: 12. Template: MADR. Folder: `asfu/decisions/`. Land: branch and PR.

## Premises

| Premise | Checked | Result |
|---|---|---|
| No decisions folder or ADRs existed | `ls` for docs, decisions, adr | None. Created `asfu/decisions/`. |
| Earlier "agreed" rulings are talk-only | scaffold header | "Agreed in talk is not ratified." Cited, not re-asked. |
| Overview says rollout is shelved | `asfu/overview.md` | Superseded in fact by active pilots (scaffold Corrections). |
| ALC heartbeat is not enforced | `projects/apache-local-communities/overview.md` | Stalled. Don't copy without a named owner. |
| Shepherd is an ASF Member guiding a group | Drew, this session | Ruled in conversation 2026-11-25. |

## Already ruled (cited, not asked)

- Chapters mirror the foundation's governance (scaffold, agreed).
- Chapter-led: students lead internally. Shepherds guide (Drew, 2026-11-25).
- A chapter that wants a president uses the board model, otherwise the PMC model (Drew, 2026-11-25).
- Each effort is run the PMC way (Planning). Starting efforts: Outreach, Partying, Education (Drew, 2026-11-25).
- Concepts and names are recycled from the foundation (Drew, 2026-11-25).
- Decisions by lazy consensus (scaffold, agreed).

## Defaulted

| Default | Who does it this way | |
|---|---|---|
| Monthly report is 3 to 5 lines plus proof of a meeting | scaffold, agreed | veto: |
| Chapter decisions get recorded publicly, not decided in Discord | `pmc` policy by analogy | veto: |

## Rounds

(Written round by round below.)

### Round 1 (Q1 to Q4)

| Q | Question | Answer | Note |
|---|---|---|---|
| 1 | Officer seats | Full foundation set including Treasurer | Overrules the recommendation (President, VP, Secretary). Treasurer holds no money, so the seat teaches the role without a budget. Keep the overruled option in Alternatives. |
| 2 | Term | One academic year, elected each fall | Recommended. |
| 3 | Electors | All chapter members vote | Recommended. |
| 4 | Scope | Chapters only | Recommended. Program-level governance is a later ADR. |

### Round 2 (Q5 to Q8)

| Q | Question | Answer | Note |
|---|---|---|---|
| 5 | Who is a chapter member | Joins the chapter's Discord and attends one meeting | Recommended. |
| 6 | Team name | PMC, the foundation's name | Recommended. Written "<School> chapter PMC" to avoid confusion with real PMCs. |
| 7 | Team chair term | Chosen per project, no fixed term | Overrules the recommendation (six months rotating). Chair seat has no clock, so the ADR names a Revisit-when: chairs that hold seats past a year. |
| 8 | Starting a new effort | Written proposal, board lazy consensus | Recommended. |

### Round 3 (Q9 to Q12)

| Q | Question | Answer | Note |
|---|---|---|---|
| 9 | Shepherds per chapter | One per chapter | Overrules the recommendation (two from a pool). Single point of failure, so the ADR names a Revisit-when: a chapter whose Shepherd goes quiet. |
| 10 | Switching models | Reframed: every chapter has a board, every effort has a PMC | No model choice at chapter level, so "can it switch" is moot. Supersedes the launch-plan Structure row (the "does it want a president" rule). Example efforts named: fundraising, outreach, education, development (maybe for metrics). Set is open, not fixed. |
| 11 | Heartbeat owner | The chapter's Shepherd | Recommended (with one Shepherd, not two). ComDev sees the count of missed reports. |
| 12 | Board cadence | Monthly, minutes on the chapter page | Recommended. |
