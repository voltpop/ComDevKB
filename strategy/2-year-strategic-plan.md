---
title: ComDev 2-year strategic plan — six pillars, budget, working-group governance reboot
compiled: 2026-07-30
status: Rich Bowen's (ComDev PMC Chair) own draft plan; formal PMC adoption status not yet confirmed
source: https://hackmd.io/@rbowen/SyglSEYrzl
last_modified: 2026-08-19
---

# ComDev 2-year strategic plan (ingested reference)

This is a ComDev strategic-plan draft authored by **Rich Bowen, the
ComDev PMC Chair** (confirmed via the `@rbowen` HackMD handle in the
source URL, and matching the same Rich Bowen who opened
`apache/www-site#725` and authored the [[ambassador-program]] draft) —
found on HackMD and pulled into this KB as reference material. It's
directly relevant to the Code of Conduct thread ([[code-of-conduct]]):
it retains a **`wg-code-of-conduct`** working group, a likely
operational home for the CoC enforcement-specificity work. Since it's
Rich's own plan rather than a third-party proposal, it's reasonable to
ask him directly about its status, rather than treating it as outside
material to independently vet. Whether/when the ComDev PMC has formally
adopted it is still unresolved — check before treating any of its
numbers or structure as current commitments.

**Ingestion-fidelity note:** repeated fetches of the source page returned
slightly inconsistent structural details (pillar count and exact ordering
varied between passes — one pass named six pillars including a separate
"Corporate Contributor Consortium" entry, another named five with
"Infrastructure & Tooling" as the fifth). The budget line items, working
group names, and named historical anecdotes were consistent across all
passes and are more trustworthy than the exact pillar numbering below.
Verify against the source directly before citing pillar structure
precisely.

## Overview

A two-year roadmap to strengthen community support across 320+ ASF
projects, centered on volunteer-driven working groups, a Year 1 budget of
**$96,718**, and an explicit "governance reboot" of how ComDev's working
groups are chartered — named chairs, clear deliverables, sunset clauses —
after past working groups reportedly failed from lack of accountability.

## Working groups (governance reboot)

- `wg-mentoring`
- `wg-events`
- `wg-ambassadors`
- `wg-site`
- `wg-corporate-engagement`
- `wg-code-of-conduct` (existing, retained as-is)

## Budget-bearing pillars

- **Mentoring Program Coordination — $6,000.** Amplifies third-party
  programs (GSoC, Outreachy, LFX Mentorship) rather than duplicating them;
  builds an Apache-specific curriculum (Apache Way, mailing-list culture,
  release mechanics, community governance). Covers ecosystem event
  attendance and mentor/mentee recognition swag.
- **Project Outreach & Activity — volunteer-run, no direct budget line.**
  A `comdev-metrics` dashboard surfaces project activity trends,
  declining-activity alerts, and cross-project contributor matching; feeds
  a Good-First-Issues aggregator.
- **Event Support & Speaker Travel — $79,600** (82% of Year 1 budget).
  Three funding tiers: evening meetups ($400 each), contributor sprints
  ($1,800 each), single-day project summits ($6,000 each); plus 10 Speaker
  Travel Grants at $3,000 each for contributors lacking employer support;
  event-materials reimbursement up to $200/event.
- **Project Ambassadors & Company Liaisons — $2,325.** Identifies existing
  community champions inside projects, gives them toolkit support and
  quarterly peer connection, recognizes their work; a parallel
  company-liaison track formalizes corporate engagement.
- **Infrastructure & Tooling — $0.** Entirely on existing ASF
  Infrastructure at no incremental cost; volunteer-built.
- **10% contingency — $8,793.**

**Year 1 total: $96,718.** Year 2 projection: ~$127,000 (expanded events,
mentoring partnerships, community-identity work completed).

**Optional add-on:** $5,500 to restore ASF Member T-shirts (discontinued
roughly 20 years ago) as a low-cost belonging/identity marker.

## Corporate Contributor Consortium

A no-cash, relationship-driven model (compared to CNCF's TAG approach):
companies with significant ASF involvement dedicate one person, one day a
week, to ComDev work. Projected yield: ~80 person-hours/week, equivalent
to 2 FTE, without ASF hiring — aimed at ComDev's chronic capacity
constraint.

## Communications strategy: "pull, not push"

Distributes outreach responsibility across working-group chairs instead
of concentrating it in one person (explicitly framed as a burnout
mitigation). Channels: the metrics dashboard (automatic/pull), monthly
board reports, quarterly ambassador check-ins, graduation welcome emails,
conference talks, and targeted 1:1 outreach triggered by metrics flags.

## Graduation outreach process (concrete "how," worth reusing as a model)

Step-by-step template for welcoming a newly-graduated TLP: identify a
community champion, add `good-first-issue` labels, check the metrics page,
join the quarterly ambassador call. Sending duty rotates across 3–5 ComDev
PMC members monthly, explicitly to prevent single-person bottleneck — the
same anti-bottleneck design principle shows up throughout the plan.

## Implementation phases

Phase 0 (foundations: deploy metrics, post working-group reboot proposal)
→ Phase 1 (pilot ambassadors, build tools/materials) → Phase 2 (outreach:
company emails, consortium kickoff) → Phase 3 (running programs:
quarterly/monthly calls, first speaker grants) → Phase 4 (scale: expand to
Top 20 projects, grow consortium, fund ALC expansion).

## Success metrics (Year 1)

12+ community events with outcome reports; 8+ speaker travel grants
awarded; events on 3+ continents; 50%+ of events organized by
non-ComDev-PMC members; 3+ new contributors onboarded through funded
events; declining-activity flagging system operational; quarterly board
reports on spend and outcomes.

## Historical context cited in the plan

The plan explicitly contrasts itself with a prior small-events initiative
(2011–2013) that ran 11 events across 4 continents at $0 cost but
collapsed from single-person dependence and no institutional backing.
Anecdotes cited in the source (attributed to named individuals there;
generalized here per this KB's anonymization convention — see
AGENTS.md):
- A contributor's proposal for a targeted-mentoring working group concept
  drew immediate enthusiasm.
- A contributor's request for travel-grant infrastructure for a project
  summit (Apache Iceberg) demonstrated clear real demand.
- A contributor's ~€1,250 ask for a project hackathon (June 2013) is
  cited alongside a past ComDev steward's reflection that "ComDev has no
  budget for this," and that the underwriting proposal on paper "was
  never really applied in practice" — the plan's stated rationale for
  budgeting real dollars up front rather than relying on ad hoc
  underwriting promises.
- A separate contributor's mention of "approaching sponsors" for a
  regional camp-style event is cited as evidence event organizers have
  long had to improvise funding themselves.

## Infrastructure & tooling

Everything hosted by ASF Infrastructure at no incremental cost:
`community.apache.org` (restructured July 1–2, 2026), `comdev-metrics`
dashboard, `projects.apache.org`, `reporter.apache.org`,
`events.apache.org`. No new hiring proposed anywhere in the plan;
sustainability rests on working-group distribution, the corporate
consortium, and volunteer automation.

## Open / unresolved — pick up here next

- Since this is the Chair's own draft, ask directly: is it formally
  adopted, still under discussion within the PMC, or superseded by a
  newer version?
- Confirm named chairs for each working group (plan states each group
  should have one; source didn't surface who, if anyone, the Chair
  intends to assign to `wg-code-of-conduct` — worth asking directly given
  the overlap with the CoC revision conversation).
- Resolve the pillar-structure ambiguity noted above by reading the
  source directly rather than relying on repeated fetch summaries.
- Connect back to [[code-of-conduct]]: if
  `wg-code-of-conduct` already exists and has (or needs) a chair, that's
  likely the right vehicle for turning the layer-1/layer-2 enforcement
  mechanics from that thread into an actual proposal, rather than routing
  everything through the Chair informally.
