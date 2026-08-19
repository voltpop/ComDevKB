---
title: ComDev outreach identity — what we offer as a collective, and how current efforts express it
topics: [outreach, identity, governance]
compiled: 2026-08-04
status: draft — first pass, grounded in ComDev's real charter/programs
---

Companion to [[university-outreach]] (the campus
program, one channel this doc situates) and
[[contributor-role-promotion-language]] (the mailing-list thread
whose conclusion — committer/PMC status as *individual technical trust*
vs. *collective governance accountability*, never something ComDev
itself grants — turned out to be one small, concrete instance of a
pattern that recurs across all of ComDev's outreach channels; see
"The recurring pattern" below).

Supersedes an earlier draft of this file that framed this as a
university-recruitment pitch. Reframed per direction: this should be
about ComDev's outreach efforts and collective identity as a whole, not
a sales document for one audience.

## Grounding: what ComDev actually is

Pulled from community.apache.org rather than reconstructed from memory,
since getting this wrong would undercut everything built on top of it.

ComDev's own stated mission: **"create and provide tools, processes, and
advice to help open-source projects improve their own community
health."** Chartered by Board resolution in November 2009.

Two things that follow directly from that wording, and matter a lot for
how ComDev should talk about itself:
- **ComDev doesn't ship code and has no projects of its own to grow.**
  It's a meta-layer over roughly 350 independently governed PMCs, not a
  single community with its own contributors in the normal sense.
- **ComDev's offering is consistently *tools/processes/advice* — the
  connective tissue — never authority.** It builds things other projects
  use; it does not itself decide who becomes a committer, who gets
  funded, or who gets to attend an event. That's not a limitation stated
  once — it's the same shape every current program takes (below).

## The recurring pattern

Looking across ComDev's actual current programs, the same structure shows
up every time:

| Program | What ComDev provides | Who holds real authority/status |
|---|---|---|
| GSoC | Coordination: Jira tracking, mentor guides, proposal-review admin, Google liaison | The hosting project mentors and community — ComDev's own docs say it "facilitates connections... rather than managing mentoring relationships directly" |
| Contributor Ladder / committer & PMC guidance | The documented pathway and process templates | The hosting PMC's own vote (3 +1s, no vetoes) — see [[contributor-role-promotion-language]] |
| Travel Assistance Committee (TAC) | Funds/arranges travel and lodging | Not a subsidy — recipients must **volunteer at the event** (setup, registration desk, speaker intros, teardown) in exchange; merit- and geography-weighted selection |
| University/campus program (in design) | Template layer: Apache Way training, pre-cleared trademark packet, event templates, aggregated good-first-issues | The **hosting PMC**, opt-in only, retains 100% of committer/PMC nomination authority — see [[university-outreach]] |
| API-first community data access (e.g. mail-archive tooling) | Articulates cross-community demand for structured data access, and mobilizes volunteers (GSoC, working groups) to build interfaces once one exists | **Infra** — the only party positioned to safely expose the API (production data, access control, security boundary); see "A sharper edge" below |

The throughline: **ComDev's offer is never "join us and we'll grant you
something." It's "here's the on-ramp; the community you actually join
grants it, and you earn it."** TAC is the cleanest illustration —
funding is conditioned on volunteering, not given freely — but it's the
same idea as a hosting PMC's committer vote, just at a different scale.

This is also why "promotion" language kept causing trouble in the
mailing-list thread ([[contributor-role-promotion-language]]): a
"promotion" implies a single body doing the elevating. Nothing in
ComDev's actual structure works that way — there's no central authority
positioned to "promote" anyone into anything. Status is always earned
from the specific community you contributed to, not conferred from
above. That's not just a wording preference; it's structurally accurate
to how the ASF works.

### A sharper edge: ComDev also shapes other bodies' day-to-day priorities, not just its own tools

Everything above reads as reactive — ComDev builds a template layer on
top of a gate someone else already opened. There's a proactive version
of the same pattern worth naming explicitly, raised in a 2026-08-04
conversation about mail-archive (Pony Mail) tooling: an Infra committer
with prior ComDev PMC service argued that if Infra focuses on shipping
*just an API* — its actual, non-delegable job, since only Infra can
safely expose production data behind the right access controls — rather
than also trying to build every interface on top of it, then ComDev (or
anyone) can build the interface that actually fits their need. His
framing: unblock people on the API, and they'll build the rest
themselves.

The important part isn't the API itself — it's that **ComDev doesn't
hold any authority over Infra's roadmap, but can still shape what Infra
prioritizes day to day**, by articulating concrete downstream demand
(dashboards, contributor/mentoring visibility, chapter-health tracking —
recurring needs across [[university-outreach]] and
this doc) and by having the volunteer pipeline (GSoC, working groups,
the university program) ready to actually build against an API the
moment it exists. That's a distinct mechanism from "build a template
after a gate opens" — it's ComDev acting as demand-side advocate for
*how another ASF body should shape its own priorities*, purely through
demonstrated need and follow-through capacity, not delegated authority.

Concrete proof this already works, independent of any new advocacy: a
Pony Mail Foal-style API already exists and was used directly, live, in
the 2026-08-04 conversation that produced
[[contributor-role-promotion-language]] — a working research tool
built entirely outside Infra, on data Infra was never asked to design a
UI for. The mechanism isn't hypothetical; it already happened once,
by accident, the moment the API was available to query.

**Not yet done:** this hasn't actually been raised with the current
ComDev PMC as a concrete question or proposal — it's analysis captured
here so the reasoning survives until that conversation happens.

## Current outreach channels (scoped per direction — not exhaustive)

Per direction, this covers the channels actually in focus right now:
university presence (the new, primary effort), GSoC/mentoring (the
existing on-ramp it plugs into), and TAC (the event-side pull-in
mechanism). PMC-level community-health advising and Community Over
Code/event presence are real ComDev functions too, but are ancillary to
current focus and not elaborated here.

**University / campus program** — the new flagship effort. Full
target-state design in [[university-outreach]]: a
template layer ComDev builds once, an instance layer per campus, PMC
hosting as opt-in, GSoC as the natural summer bridge. Its core identity
claim, sharpened by the committer/PMC breakdown: what it offers a student
isn't a manufactured credential, it's a *real, externally-earned* one —
see that doc's IEEE-mapping table and messaging calibration
(committer status is the realistic promise; ASF Membership is not).

**GSoC / mentoring** — the existing, funded, well-known on-ramp the
university program deliberately reuses rather than duplicates. ComDev's
role here is explicitly administrative/connective (tracker, mentor
guides, Google liaison), not the mentoring relationship itself, which
belongs to the hosting project — same pattern as above.

**Travel Assistance Committee (TAC)** — the mechanism most likely to pull
university-program participants into in-person community (Community Over
Code and other events), per direction. Worth noting structurally: TAC
doesn't just fund attendance, it converts attendance into volunteer labor
at the event (registration desk, speaker intros, setup/teardown) —
selection favors merit and geographic proximity over pure need. That's a
second concrete example of "earn it, don't just receive it" showing up
in a completely different program, independently of the committer/PMC
or university-program design work.

## Open / unresolved

- Whether/how the university program and TAC should be explicitly linked
  operationally (e.g., pointing graduating chapter leads or active
  contributors toward TAC applications) hasn't been designed — currently
  just an observed structural resonance, not a mechanism.
- The broader "what ComDev offers as a collective" identity statement
  above is a first pass from public docs, not something checked against
  how the current ComDev PMC or Chair would describe it themselves.
- PMC-level community-health advising and Community Over Code/event
  presence are real, currently-ancillary parts of ComDev's identity that
  this doc deliberately doesn't develop — revisit if focus broadens.
- The API-first advocacy question ("A sharper edge" above) hasn't been
  raised with the current ComDev PMC yet. The author is a current ComDev
  PMC member and intends to raise it at the next ComDev office hours,
  rather than as a mailing-list thread — captured here so the reasoning
  survives until that meeting happens. See
  [[community-knowledge-agent-tooling]] for a 2026-08-05 external
  data point (an AWS precedent) supporting the same push.
