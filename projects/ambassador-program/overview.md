---
title: Ambassador program — foundation-wide, ComDev-stewarded
project: ambassador-program
compiled: 2026-08-19
status: first draft exists (apache/comdev-working-groups proposed/ambassadors.md) — evaluated 2026-08-19 ahead of ComDev office hours; hybrid-funding refinement proposed, not yet raised with the draft's author or the PMC
---

Raised by the ASF President (also a ComDev PMC member) as a candidate
topic for the 2026-08-19 ComDev office hours. No prior thread in the KB —
this is a new project, not an extension of an existing one.

## Scope and ownership

Foundation-wide, ComDev-stewarded — the same split ComDev already uses for
[[badgefed-credential-service]]: build/host the connective tissue
across PMCs, don't hold authority that belongs to individual projects.
Not yet brought to the ComDev PMC as a formal proposal; this doc exists to
give office hours something concrete to react to.

## Starting shape, per the draft's author

The draft author's framing: the program starts as a place for ambassadors to compare
notes and share solutions — a peer knowledge-exchange venue, not (at
least initially) external evangelism, onboarding mentorship, or a formal
PMC-liaison structure. This is one person's opening framing, not a
decided scope — office hours may narrow, broaden, or contest it.

Open questions, deliberately unresolved:

- Who is an "ambassador" — self-selected per PMC, appointed, one per
  project, or something else? **Per the draft's author (2026-08-19):**
  visible community leads — people who already show up to events and do
  the work — rather than a formal appointment process. Consistent with
  the draft's own "recruit, don't assign" framing: ComDev identifies who
  a project already treats as its community champion, it doesn't select
  someone independently of that.
- What does "compare notes and share solutions" run on — a
  mailing list, recurring call, or the venue [[community-forum-platform]]
  is already exploring? Worth checking for overlap before standing up
  a separate channel.
- Does this stay a lightweight peer forum, or grow toward the
  outreach/liaison shapes considered and set aside for the office-hours
  discussion?

## First draft: [proposed/ambassadors.md](https://github.com/apache/comdev-working-groups/blob/main/proposed/ambassadors.md)

Confirms and fleshes out the framing above rather than diverging from it.
Core shape: **RECRUIT, EQUIP, CONNECT, RECOGNIZE** — ComDev never assigns
ambassadors from outside; each hosting PMC identifies its own community
champion, and ambassador responsibilities run "to their own PMC, not to
ComDev." The weekly office hour is explicitly "a peer network, not a
reporting structure" — matches the framing conveyed verbally above
exactly, not just a looser gloss on it.

Two-phase rollout: Phase 1 pilots direct outreach to five named TLPs
(Cassandra, Airflow, Iceberg, Kafka, Cloudstack); Phase 2 expands to the
Top 20 by activity plus a standing "graduation outreach" process — every
newly-graduated TLP gets a welcome email within a week of its board
resolution, run on a pull-model rotation of 3–5 ComDev PMC volunteers.
The toolkit ComDev commits to building: a per-project metrics dashboard,
a Good First Issues aggregator, onboarding/welcome-email templates, and
an escalation path — built once, applied across N projects.

## Evaluation (2026-08-19)

**Matches how ComDev already operates:**
- Authority model is correct — same tools/process/advice-not-authority
  pattern as GSoC, TAC, and the campus program in
  [[outreach-identity]]'s recurring-pattern table. No new
  authority ComDev doesn't actually have.
- Rotation/escalation design (pull-model, 3–5 person rotation, ambassadors
  report to their own PMC) matches [[feedback_coc_governance_design]]'s
  preference for distributed backstop authority over single-officer
  control.
- No invented rung in the committer/PMC/Member ladder — avoids the trap
  [[university-outreach]] flagged early with "Foundation
  Fellow/PMC treated as one terminal rung."

**Overlaps/gaps worth raising before endorsing Phase 1:**
1. **"Speaker Travel Program" vs. the existing Travel Assistance
   Committee.** The draft treats this as a separate not-yet-funded
   program. TAC already funds conference travel conditioned on
   volunteering at the event (per [[outreach-identity]]). The
   university-pipeline doc already flagged this exact duplication risk
   for travel/stipend mechanisms once — reuse, don't reinvent. See
   proposed resolution below.
2. **Metrics dashboard / Good First Issues aggregator — do these exist
   yet?** The draft's welcome-email template asserts the dashboard is
   already live at `community.apache.org/metrics/?project=X`; the
   toolkit section separately implies only some items are built.
   Resolved in part, 2026-08-19: the draft's author is already publishing
   weekly metrics, currently at <https://boxofclue.com/comdev-metrics/> —
   externally hosted, not on ASF/ComDev infrastructure, with a request to
   move it onto a ComDev-owned machine. So the dashboard is real, but
   the draft's `community.apache.org/metrics/` URL is aspirational, not
   current — the welcome-email template shouldn't point there until the
   migration actually happens. Still open: who provisions/maintains the
   ComDev machine, and whether "community.apache.org/metrics" is the
   intended eventual path or just a placeholder in the draft.
3. **Good First Issues aggregation is already scoped once**, in the
   campus program's template layer
   ([[university-outreach]]). Should be one build
   serving both threads, not two.
4. **Peer network vs. the forum-platform thread** — different medium
   (live weekly call vs. async threaded forum in
   [[community-forum-platform]]), not actually redundant. Natural
   sequencing: the ambassador cohort could seed the forum's founding
   community once it exists, rather than the two threads competing for
   "where does ComDev's knowledge-sharing happen."
5. **Scope/bandwidth risk** — Phase 1 alone asks ComDev to build four
   toolkit items, run weekly office hours, and staff a graduation-outreach
   rotation, on top of CoC revision, the campus program, BadgeFed, and the
   forum platform all already active. The draft itself flags the "equip"
   prerequisite without naming who builds it or by when.

## Proposed refinement: hybrid funding for the Speaker Travel Program

Author's framing (2026-08-19), not yet raised with the draft's author or
the PMC —
resolves overlap #1 above without reinventing TAC: **funding comes from
donors; outreach/selection stays volunteer-led.** Concretely:

- Donors fund a pool earmarked for speaker travel; volunteers (ambassadors
  plus existing TAC process) still decide who receives it, using the same
  merit/geography-weighted, volunteer-in-exchange model TAC already runs.
  New money, not new bureaucracy.
- **Selection must stay volunteer/merit-driven, never donor-driven** — the
  same vendor-neutrality guardrail [[university-outreach]]
  already worked out for corporate sponsorship of the campus program:
  *"sponsorship funds logistics/travel only, never project selection or
  governance influence (same principle as ApacheCon/GSoC sponsors)."*
  Applies directly: donors fund the pool, ambassadors/TAC pick who travels,
  never a sponsor's pick.
- Author's call (2026-08-19): this runs as its **own, separate effort**
  from TAC, not a donor-restricted line item folded into TAC's existing
  fund — narrower audience (accepted-CFP speakers specifically) and a
  distinct donor-funding source justify a program of its own, structurally
  parallel to TAC (same volunteer-led, same no-cash-for-influence rule)
  rather than a variant inside it. Either way the ambassador's job is the
  same — surface who deserves it, not who pays.
- Optics: probably can't be branded as sponsor-attributed ("brought to you
  by X Corp"), same vendor-neutrality concern as any ASF sponsor money.

## Status

First draft exists and has been evaluated. Purpose/shape is the draft
author's opening framing (peer knowledge-exchange), largely consistent
with how ComDev already runs its other programs. Remaining open items
above, plus the hybrid-funding refinement, are inputs for the 2026-08-19
office hours discussion — not yet raised with the draft's author or
decided by the PMC.
