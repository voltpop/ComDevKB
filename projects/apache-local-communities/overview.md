---
title: Apache Local Communities (ALC) — chapter program stewardship
type: Project
description: "Stewardship of the ALC chapter program and its stalled heartbeat mechanism."
project: apache-local-communities
compiled: 2026-09-09
status: draft
status_note: existing ComDev program (city/region chapters, running since ~2018-2020); revisited 2026-09-09 after two unanswered establishment requests surfaced a stalled heartbeat mechanism — not yet raised with the ComDev PMC as a fix proposal
---

## Context / motivation

Author reported (2026-09) two ALC establishment requests in the past
month that went unanswered, and a general sense that "the groups get
created and then we lose them" — chapters stand up and then drop off
ComDev's radar with no way to tell if they're still alive.

Investigation (2026-09-09) found this is **not a greenfield idea** —
ALC is a real, running ComDev program dating to at least 2018-2020,
originally driven by Swapnil M Mane. The process is real and mostly
still published; what's actually broken is narrower than "no process
exists."

**Sourcing note:** reconstructed entirely from public sources — the
`dev@community.apache.org` list archive (public) and the public
`cwiki.apache.org/confluence/display/COMDEV/*` pages. One process step
below (the PMC vote) happens on `private@community.apache.org`; that's
stated only as a procedural fact taken from the public wiki page
describing the process, not sourced from private@ content itself — per
`AGENTS.md`'s sourcing constraint.

## What exists today

- **Program shape**: city/region chapters modeled on things like Google
  Developer Groups or Mozilla Reps — one chapter per location, spreading
  awareness of Apache projects and The Apache Way, hosting local events.
- **Establishment process**: fully documented — see
  [[establishing-an-alc-chapter]] for the reconstructed step-by-step.
- **Roster**: ~21 chapters listed on the [ALC Chapters index](https://cwiki.apache.org/confluence/display/COMDEV/ALC+Chapters)
  (12 visible directly, "9 more child pages" not enumerated in the
  fetch). No status, lead, or contact info at the index level — you have
  to open each chapter's own page to know if it's alive.
- **A named owner role exists on paper**: "ALC Chair," responsible for
  ensuring quarterly reports are filed across all chapters and for
  reviewing pre-event materials with PMC assistance (per
  [Roles and Responsibilities in managing ALC initiative](https://cwiki.apache.org/confluence/display/COMDEV/Roles+and+Responsibilities+in+managing+ALC+initiative)).
  **Open question: who currently holds this role, if anyone** — this is
  the most likely explanation for both the unanswered requests and the
  stalled heartbeat below.
- **A heartbeat mechanism already exists on paper**: chapter leads file
  a status report to `dev@` every three months, and the main ALC
  overview page states inactive chapters (3+ months) face dissolution
  after a PMC vote.

## What's actually broken

Confirmed by reading the live wiki (2026-09-09), not assumed:

- The [Reports index](https://cwiki.apache.org/confluence/display/COMDEV/Reports)
  is stale — most tracked chapters show a "next report" date from
  2020–2022 that was never followed up on. Only 2 of 7 explicitly
  tracked chapters (Bangalore, Taipei) show a 2025 date. The
  3-month-inactivity dissolution rule does not appear to have been
  invoked despite years of missed reports.
- No one is currently visible running the `[ALC] Request to establish`
  intake pattern the way Swapnil M Mane did in 2020 (confirming
  members, calling the PMC vote, setting up chapter wiki pages,
  assigning a mentor) — consistent with the two requests this month
  going unanswered.
- No consolidated live-status view exists (active / stalled / dead)
  across the ~21 chapters — the only ground truth is each chapter's own
  report history, checked individually.

**Read together**: the gap isn't "ALC has no process" — it's that the
process has no visibly active owner right now, so both ends of it
(intake and the quarterly heartbeat) have gone quiet at the same time.

## Author's framing on scope (2026-09-09)

Explicitly **not** looking to design a heavier process: "we don't need
a lot of process, just a heartbeat." A strawman raised in conversation:
treat list traffic itself as the activity signal (did the chapter's
list see any activity this quarter?) rather than requiring a written
report to be chased down manually — cheaper than reviving the
chase-chapter-leads-for-reports cadence, and doesn't require a
volunteer rotation the way [[ambassador-program]]'s graduation-outreach
model does.

## Relation to other ComDev threads

- [[ambassador-program]] hit the identical "created, then goes cold"
  retention shape and solved it with a pull-model volunteer rotation
  doing periodic check-ins. ALC's problem is one level simpler — the
  reporting mechanism already exists, it just isn't running — so the
  fix may be "make the existing mechanism actually happen" rather than
  designing a new one.
- Both ALC and [[ambassador-program]] are ComDev-stewarded,
  advice/tools-not-authority programs, matching the same pattern
  [[outreach-identity]] documents for GSoC, TAC, and the campus program.

## Open / unresolved

- Who currently holds (or should hold) the ALC Chair role, and whether
  it's vacant.
- What to do with the two specific pending 2026 requests — route them
  now, separate from fixing the systemic gap.
- Whether to revive the quarterly-report-chasing cadence as-is, or
  replace it with the lighter list-activity-as-signal approach floated
  above — not yet decided.
- Whether/how to build a single consolidated status roster across all
  ~21 chapters.
- Not yet raised with the ComDev PMC.
