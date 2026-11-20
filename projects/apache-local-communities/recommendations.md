---
title: Recommendations — better supporting ALC chapters
type: Proposal
description: "Recommendations for better supporting ALC chapters."
project: apache-local-communities
compiled: 2026-09-09
status: draft
status_note: author's own analysis, drafted 2026-09-09 conversationally; not yet raised with the ComDev PMC or ALC Chair (whoever/whether that role is currently staffed)
---

Author's recommendations (2026-09-09) on what the ASF/ComDev needs to
do differently, given the findings in [[overview]]. These are proposals,
not decisions — captured here so the reasoning survives until they're
actually raised.

## Immediate, low-effort

1. **Route the two pending 2026 requests now.** Whatever else changes,
   leaving a live request unanswered is the worst outcome — it signals
   the program is dead when the documented process (see
   [[establishing-an-alc-chapter]]) still actually works end to end.

## The core fix: ownership, not process redesign

2. **Confirm whether anyone currently holds the ALC Chair role, and
   staff it if not.** This is the single biggest lever. Per the wiki's
   own [Roles and Responsibilities](https://cwiki.apache.org/confluence/display/COMDEV/Roles+and+Responsibilities+in+managing+ALC+initiative)
   doc, the ALC Chair's job is literally "make sure intake happens and
   quarterly reports get filed" — both problems raised in this thread
   (unanswered requests, chapters going dark) are exactly what an
   unstaffed ALC Chair produces. Fixing this one thing plausibly fixes
   both symptoms without touching the documented process at all.

## Matches the author's "just a heartbeat, not more process" framing

3. **Replace chased quarterly reports with list-activity-as-signal.**
   Manually chasing ~21 chapter leads for a written report every three
   months has been effectively dead since 2020–2022 (see [[overview]]'s
   Reports-index finding) — too heavy to actually sustain. A cheap
   automated check (did the chapter's list see any traffic this
   quarter?) gives the same "still alive?" signal without a human
   having to chase anyone down.
4. **Either enforce or formally retire the 3-month-inactivity
   dissolution rule.** It exists on paper (main ALC overview page) and
   has apparently never been invoked despite years of missed reports.
   An unenforced rule is worse than no rule — it makes the roster look
   curated when it isn't, and undermines trust in the rest of the
   documented process.

## Visibility fix

5. **Build one consolidated status roster** (active / stalled / dead,
   at a glance) instead of requiring someone to open each of ~21
   individual chapter pages to find out. This is what makes #3 and #4
   actually actionable day to day, rather than theoretical.

## Concrete support a chapter actually needs (author's framing, 2026-09-09)

Distinct from the ownership/heartbeat fixes above, which keep the
*program* alive — this is what a chapter needs to run an actual event:

- **Food and drinks** (pizza-and-drinks-level, not lavish) — the
  standard low-friction way to get people to show up and stay.
- **A venue** — help finding or covering one, since this is often the
  actual blocker for a volunteer-run local group with no budget of its
  own.
- **Content** — speakers, talks, or material, so a chapter isn't
  solely dependent on its own local members to fill an agenda every
  time.
- **Swag** — stickers/shirts/similar, the usual give-away layer that
  makes a local event feel like it's actually backed by the ASF, not
  just a meetup with the Apache name on it.

None of this is decided or costed. If it involves outside money, the
same vendor-neutrality guardrail already established for
[[ambassador-program]]'s Speaker Travel Program should apply here too:
*sponsorship funds logistics (food, venue, travel) only, never event
content or chapter governance/selection* — same principle as
ApacheCon/GSoC sponsors. Whether this is ComDev's own budget, a
donor-funded pool (as ambassador-program is exploring), or something
chapters arrange themselves per-event is open.

## Worth deciding, not urgent

6. **Whether ALC should share infrastructure or thinking with
   [[ambassador-program]].** Both are ComDev-stewarded, chapter/
   peer-network-shaped, and hit the identical "created, then goes
   cold" failure mode — [[ambassador-program]] addressed it with a
   pull-model volunteer rotation for graduation outreach. They don't
   need to merge, but designing the retention fix twice, independently,
   would be wasted effort.

## Throughline

ALC doesn't need a new program design — the process in
[[establishing-an-alc-chapter]] already works when someone runs it. It
needs a live owner (the ALC Chair gap) and a lighter-weight heartbeat
than the one that already quietly stopped running.

## Open / unresolved

- Not yet raised with the ComDev PMC.
- Whether the ALC Chair role is actually vacant, or just quiet, hasn't
  been confirmed with anyone who'd know (e.g. Rich, or whoever
  originally succeeded Swapnil M Mane if anyone did).
- Whether #3's list-activity signal is technically easy to automate
  against the existing dev@/chapter list infrastructure, or would need
  Infra involvement.
- **No way to survey local ASF Members without asking directly.** There's
  no public or appropriate-to-mine dataset of Members by geographic
  location — ICLA records (`iclas.txt`, officer-restricted) hold real
  legal names/addresses and aren't an appropriate source to cross-reference
  for this, even in service of a legitimate ALC question. The only clean
  path to check a location against the "1 ASF Member + 2 PMC members"
  prerequisite (see [[establishing-an-alc-chapter]]) is to just ask on
  the relevant list and see who self-identifies.
