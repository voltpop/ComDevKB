---
title: ComDev university membership pipeline — IEEE-inspired campus program, ASF-native governance mapping, university institutional guardrails, and success metrics
project: university-outreach
compiled: 2026-07-29
status: target-state design — rollout deliberately not yet started, pending reconciliation against a separate inventory of current university interactions
---

# ComDev university membership pipeline

Compiled while a ComDev PMC member worked through the design of a
university/campus engagement program. Explicit framing from the author:
this is a **target-state design** — "what we think our university
presence should look like across the board, regardless of what it is
right now." The author is separately, in parallel, conducting an
inventory of current/ongoing university interactions; that inventory is
not part of this document and reconciling the target state against it is
future work, not yet started.

Two things the author ruled out explicitly and early, both worth holding
onto if this gets revisited:
- **Not an academic-credit or grading program.** No course credit, no
  grades, no faculty-graded participation. Stated twice, treated as a hard
  constraint.
- **Not a parallel membership/credentialing system.** See below — the
  "professional society" is the ASF itself, not something built alongside
  it.

## Starting point: what was wrong with the initial draft

The author brought an LLM-generated blueprint proposing an IEEE-campus-chapter
model adapted for a "small open-source foundation." The draft's core flaw:
it implicitly assumed a single-project foundation — one codebase, one set
of "core maintainers," "the Foundation's technology" as a singular thing.
The ASF isn't that; it's a legal umbrella over roughly 350 independently
governed PMCs, each with its own culture, committers, and merit process.
ComDev itself has no code, no maintainers, no projects to triage.

Other specific problems flagged in the original draft:
- "2+ merged PRs earns voting rights for Contributor Representative seats"
  — contradicts how ASF actually grants any authority (PMC consensus vote,
  not a numeric threshold). Automatic entitlement gates were rejected
  throughout the redesign.
- "Foundation Fellow / PMC" treated as one terminal rung — these are
  actually two unrelated axes at ASF (PMC membership is per-project;
  ASF Member is foundation-wide, granted by nomination/vote of the existing
  Members body). ASF has no "Fellow" grade.
- Travel/micro-grants and structured stipends largely duplicate mechanisms
  that already exist (Travel Assistance Committee for conference travel,
  Google Summer of Code for funded student contribution) — reuse these
  rather than inventing parallel ones.
- ICLA friction and ASF trademark/Brand Management sign-off were both
  missing from the original draft entirely; both are ASF-specific gates a
  generic "software foundation" wouldn't have.

## Core structural correction: the Society *is* the ASF

Midway through the redesign, the author corrected the direction explicitly: the
goal is a membership pipeline / professional society, not an
academic-credit program — and, crucially, **the society is the Apache
Software Foundation itself**, not a new parallel credentialing system
bolted onto it. There are no invented grades. The pipeline is the real ASF
ladder:

**Prospect (campus chapter participant) → Contributor → Committer → PMC
Member → ASF Member**

This resolves what had looked like a hard problem (brand-collision risk
between invented "Society grades" and real ASF terms, plus a dues/revenue
question) by dissolving it — there's no separate entity to name or fund.

IEEE's own structure maps onto this once matched at the right levels
(better than initially given credit for):

| IEEE | ASF |
|---|---|
| Student Branch / Student Member | Campus chapter participant — pre-ICLA, pre-first-patch, pure prospect |
| Joining a Technical Society (e.g. IEEE Computer Society) | Becoming an active contributor on a specific project |
| Senior Member (peer-endorsed, sustained record) | Committer / PMC Member — peer-nominated, real authority, project-scoped |
| Fellow (rare, capstone, invitation-only) | ASF Member — foundation-wide, elected by the existing ~1,000 Members |

Calibration note for messaging: ASF Membership is a rare, career-later,
cross-project honor — it should never be sold as the program's target
outcome. **Committer status on one project** is the realistic, genuinely
portable credential to promise students.

## Two-layer structure

- **Template layer** (built once, by ComDev): Apache Way + ICLA +
  mailing-list-culture training module, pre-cleared trademark/branding
  packet (one-time Brand Management sign-off, not renegotiated per
  chapter), wiki chapter registry, aggregated good-first-issue list pulled
  from opted-in PMCs, event templates (Issue Triage Night, Documentation
  Sprint, GSoC-prep workshop), a one-page "How to Start a Chapter" doc.
- **Instance layer** (per campus): Chapter Lead (student, single point of
  contact), Faculty Advisor (**optional**, logistics/legitimacy only — room
  bookings, student-org registration — explicitly no grading and no
  research obligation), matched Hosting PMC + one liaison committer,
  Alumni/Regional Mentor (a graduated chapter lead who stays on remotely).

## PMC opt-in — the actual bottleneck

A project becomes a pilot host by its own choice, never by ComDev
assignment. The ask has to be framed as low-cost to the PMC — *"pre-oriented
newcomers who already understand the Apache Way and have ICLA sorted"* —
not *"donate mentor time to an unproven outside program."* A no-fault exit
(stepping back from hosting for a term, no process drama) is part of the
design, not an afterthought. All committer/PMC-member nomination decisions
stay 100% with the hosting PMC; the program has zero authority there.

## Annual cadence (tied to the academic calendar)

Fall: recruitment, Apache Way training, first contributions, chapter
registration/renewal. Winter: sustained contribution. Spring: GSoC-prep
workshops timed to Google's application window (the existing funded on-ramp
— reused, not duplicated). Summer: GSoC participants work under that
program's own mentor/stipend structure. Following fall: chapter-lead
succession, outgoing lead optionally becomes remote alumni mentor — the
graduate-bridge mechanism, same rhythm every year.

## University institutional guardrails — and why each is also a feature

Working through "what happens when a university's own research/business
goals interact with this program" surfaced seven concrete tensions. Each
gets a guardrail *and* a reframe, because the author asked explicitly not to
leave these as pure risk-mitigation — they should read as selling points
where possible:

1. **University IP/tech-transfer claims** (Bayh-Dole, grant-funded
   research, RA positions) can conflict with the Apache License's patent
   grant — a student may not actually hold the rights their ICLA
   represents. *Guardrail:* chapters are explicitly extracurricular,
   unaffiliated with funded research or coursework; onboarding flags
   "check with your PI/tech-transfer office if this came out of grant
   work." *Feature:* "own your work" — a clean personal ICLA is faster to a
   public credential than any funded-research path requiring IP assignment.
   This is also the reason the earlier "no credit, no grades" decision
   matters beyond avoiding academic bureaucracy — it's doing double duty as
   IP hygiene.
2. **University commercialization goals** conflict with giving away
   patentable IP for free. *Guardrail:* match students to non-core,
   non-patentable work (docs, testing, tooling, community infra) around a
   lab, never its commercializable core. *Feature:* pitch to research
   offices as a free pipeline for the open infrastructure surrounding their
   research, not competition for the same IP.
3. **Corporate sponsorship** pressure toward exclusivity/branding rights
   conflicts with ASF vendor neutrality. *Guardrail:* sponsorship funds
   logistics/travel only, never project selection or governance influence
   (same principle as ApacheCon/GSoC sponsors). *Feature:* the credential is
   trusted specifically because it isn't for sale.
4. **Faculty incentives** run on grants/publications, not community
   service. *Guardrail:* advisor role stays logistics-only, zero
   grading/research obligation — resist future scope creep here.
   *Feature:* zero-workload institutional affiliation ("our students are
   Apache committers") is the easiest kind of faculty buy-in to get,
   precisely because it asks for nothing.
5. **Formal university-ASF MOU / legal review** would stall a chapter
   launch for months. *Guardrail:* never require an institutional
   partnership agreement to start a chapter; ordinary student-org
   registration is fine, a bilateral ASF-university MOU is not needed.
   *Feature:* same-week launch capability and resilience to administration
   turnover is a real competitive advantage.
6. **Trademark use implying exclusivity/endorsement** between the ASF and
   one university. *Guardrail:* chapter materials read "an ASF-affiliated
   student chapter at [University]," never partnership language.
   *Feature:* the anti-exclusivity constraint is exactly what allows
   parallel chapters at many, even competing, universities without
   conflict-of-interest overhead.
7. **Faculty wanting to study the chapter** as a research subject (surveys,
   contribution-pattern analysis) is their own IRB matter. *Guardrail:*
   program doesn't grant special data access beyond what's public; keeps
   its own data footprint to aggregate-only chapter metrics. *Feature:*
   minimal data collection is a trust/privacy signal to prospective student
   contributors, not just defensive posture.

## Success metrics framework

Split by audience — each level acts on different signals, so one combined
scorecard doesn't work:

**Leading indicators (semester-scale, actionable):**
- Time from chapter-join to first contribution attempt, net of ICLA lag —
  owned by the chapter lead, diagnoses onboarding friction.
- % of prospects making at least one contribution attempt per semester —
  chapter lead, diagnoses recruiting→engagement conversion.
- PMC liaison median response time on a student's first PR — ComDev
  steward, diagnoses whether the hosting PMC is actually delivering; a
  slow/absent liaison is the most common way a promising student silently
  disengages.
- Cadence adherence (did planned events actually happen) — chapter lead,
  basic operational health.

**Outcome indicators (year-plus, track but too slow to act on alone):**
GSoC application/acceptance rate among chapter participants; Contributor →
Committer conversion rate aggregated across hosting PMCs; chapter
succession survival rate (did the chapter outlive its founding lead's
graduation); alumni mentor participation rate among graduating leads;
18-month post-graduation retention as an active contributor.

**Threshold-setting:** no absolute numeric targets yet — no baseline data
exists and the author's inventory hasn't landed. First real cohort establishes
baseline; later cohorts get evaluated by trend against that baseline, not
against an invented number.

**Sustainable collection:** split each metric into "free" (already-public
ASF data — committer status changes, GSoC results, mailing-list activity —
pullable without asking anyone) vs. "costs someone effort"
(self-reported). Keep the self-reported burden to one short quarterly note
per chapter lead.

**Operational synthesis tool:** roll the leading indicators into a single
Green/Yellow/Red chapter-health status (contribution attempt this quarter +
liaison responded within a to-be-calibrated window + quarterly note filed)
so a ComDev steward can triage at a glance.

## Relationship to the broader "OSS as academic output" movement

The author brought a second document for review — this one considerably more
grounded than the original IEEE blueprint — arguing for systemic university
reform to recognize open-source software as a first-class academic output
equivalent to journal publications for promotion & tenure (P&T): CITATION.cff
adoption, Software Heritage/Zenodo persistent identifiers, funder mandates
(NSF/NIH/ERC), university-ranking criteria, Research Software Engineer (RSE)
career tracks, and academic Open Source Program Offices (OSPOs, the kind
Sloan-funded initiatives are standing up). Real movement, real
organizations, not invented.

**Decoupling conclusion (the author's, confirmed):** this reform agenda is a
separate, parallel initiative from the campus program — different
timescale (multi-year, top-down: deans, provosts, funders, ranking bodies),
different actors, different mechanism (funding/prestige/accreditation
pressure rather than bottom-up grassroots adoption). The campus program's
design strength is specifically that it doesn't need this reform to
succeed first (no MOU, no institutional sign-off, faculty kept
logistics-only). Making the program dependent on P&T reform would undercut
that strength. Stays background awareness, not a workstream ComDev takes
ownership of.

**Does the program still move the needle on it?** Mostly not on the
specific axis that document cares about — P&T reform is about *faculty*
research-output recognition, and the campus program is a *student*
pipeline; most participants head into industry, not academic faculty
careers. The program has no direct leverage over funder mandates or
ranking criteria.

It does advance a different, more tractable, adjacent legitimacy question:
not "does OSS count as faculty research output" but **"does structured OSS
contribution count as legitimate experiential learning for students"** —
the same category internships and research assistantships already occupy.
The success-metrics framework above (time to first contribution, GSoC
conversion, committer conversion rate, 18-month retention) is exactly the
kind of longitudinal cohort data that movement currently lacks — most of
its case is built on anecdote and career-track proposals, not real outcome
data. Several years of disciplined measurement makes the program a genuine
evidence supplier for that broader legitimacy argument, as a byproduct of
running it well, not because ComDev set out to advocate for anything.
Slower/indirect mechanism in the same direction: some fraction of
participating students eventually become faculty themselves, carrying
forward a lived conviction that OSS contribution is real work — real, but
decade-scale and diffuse.

**Framing caution for whenever outcome data is ever shared publicly**:
because the program is deliberately designed to succeed *without* any
formal academic recognition (the right call, for the IP-hygiene and
fast-launch reasons above), its own success is double-edged as evidence — a
skeptical administrator could point at it as proof that no formal
recognition is needed, rather than proof that structured investment pays
off. If/when results get shared outside ComDev, frame as the latter
("structured mentorship investment produces strong outcomes") not the
former ("students already do this for free, no change needed") — the
second framing would actually undercut the reform case rather than support
it.

**The author's stated broader motivation** (2026-07-29): paving the way for open
source, as an engineering discipline, to follow the same legitimizing path
open science has been cutting for the hard sciences — i.e., this campus
program is one piece of a larger personal effort to establish OSS
contribution as a recognized, credentialed form of technical/professional
development, parallel to how open science practices (preregistration, open
data, open methods) have been gaining institutional legitimacy in
research-science fields.

## Campus program vs. academic/university OSPO — how they differ, and how to align without merging

Prompted by the author asking directly how the campus program differs from a
university/academic Open Source Program Office (OSPOs, e.g. the
Sloan-funded academic cohort referenced above), and then how to align goals
between the two under a "playing nice" framing.

**Core difference:** an OSPO manages a university's *own* research software
as an institutional asset; the campus program connects students to
*somebody else's* software (ASF projects) as a career pipeline. Different
customer, different authority structure, different organizational weight.

| Dimension | Academic/University OSPO | Campus program |
|---|---|---|
| What it manages | The university's own research software output — licensing, compliance, sustainability | Third-party software (ASF projects) the university has no ownership stake in |
| Who it serves | The university itself — faculty, IP/compliance posture, funder-mandate obligations, institutional reputation | Individual students, plus opted-in hosting PMCs — the university is a logistical host, not a customer |
| Relationship to IP/TTO | Actively engages the TTO, advocates open licensing over patenting the university's own inventions | Deliberately avoids TTO entanglement — stays extracurricular so student contributions never touch university-owned IP |
| Organizational position | Official university office — funded, staffed, reporting into research administration | Not an official university function — student-led, faculty role optional/logistics-only, no dean/provost sign-off |
| Where real authority lives | Internal to the university — its own P&T committees, its own licensing decisions | External — ASF PMCs grant committer/PMC/Member status, never the university or the program |
| Investment bar to exist | Heavyweight — real staff/budget/institutional buy-in, typically one per well-resourced university | Lightweight — one motivated student, zero university money, replicates across many campuses at once |
| Disciplinary scope | University-wide, any department | Scoped to specific hosting projects/PMCs |

**Framing:** these are two different organs of the same broader OSS-legitimacy
question, not competitors. An OSPO, where one exists, is faculty/
institution-facing; the campus program is student/community-facing. A
campus with both would have the OSPO handling faculty-software legitimacy
and the chapter handling the student pipeline, with no real overlap.

**Alignment mechanisms ("playing nice"), free to do:**
- OSPO as first-stop referral for IP/TTO questions (ties into guardrail #1/
  #2 above) — chapter gets expert guidance for free, OSPO reaches a
  population it might not otherwise engage.
- Shared metric vocabulary (what counts as "a contribution," what
  "sustained" means) so datasets are comparable later, without either
  party changing how it operates.
- Co-marketing / joint events for visibility, no shared budget or charter.
- One informal point of contact per side — no joint committee.

**The one place alignment needs a boundary, not just goodwill:** an OSPO's
job includes finding contributors to sustain faculty's *own* research
software. A natural-feeling ask — "can your chapter students help maintain
Professor X's lab code?" — has to be declined or routed carefully, because
it would reopen exactly the IP-entanglement risk guardrail #1 exists to
prevent. The only legitimate bridge: if a professor's research software is
deliberately released under a permissive license and becomes a genuine ASF
Incubator candidate, it enters through the normal Incubator/PMC process
like anything else — not through a chapter-OSPO side channel. Noted as a
real edge case, not a mechanism to build now.

**Standing rule:** alignment mechanisms are fine as long as none of them
require a formal university-level MOU to function (breaks the fast-launch
design) and none of them expand the chapter's mandate into managing the
university's own software/IP (reopens exactly what guardrail #1 prevents).
Referral and visibility, yes; shared responsibility for each other's actual
constituency, no.

## Explicitly out of scope

No dues, no academic credit or grading, no membership grades/titles
distinct from real ASF status, no program or ComDev authority over any
PMC's committer/PMC nomination decisions, and — per the author, 2026-07-29 —
**no rollout/community-buy-in work yet**. That question (how to socialize
this beyond pilot PMCs without it reading as ComDev overreach into project
autonomy) was explored in the same conversation and shelved deliberately:
rollout isn't on the table until the target-state design is further along
and reconciled against the author's separate inventory of current university
interactions.

## Open / unresolved — pick up here next

Three target-state design gaps identified but not yet worked through, in
the order the author was tackling them:

1. **Liability posture for chapter events** — what the standard *should*
   be (independent of what any current ad hoc chapter is actually doing)
   for physical meetups/hackathons run under Apache branding. Trademark/
   endorsement optics are covered (see guardrail #6 above); actual legal
   exposure is not. Likely needs disclaimer language along the lines of
   "chapters are independent student organizations responsible for their
   own event logistics and insurance; the ASF is not the organizing entity
   of record" — reviewed by whoever handles this for the ASF, not
   improvised in this design conversation.
2. **Chapter failure modes / off-ramps** — no mechanism yet for ComDev to
   pull a chapter's registration or branding rights if it goes dormant,
   misrepresents its affiliation, or produces low-quality activity that
   annoys a hosting PMC. PMCs have a no-fault hosting exit; chapters
   themselves don't yet have an equivalent off-ramp defined.
3. ~~Demand/supply scaling mechanism~~ **Resolved (2026-07-30) — no formal
   mechanism needed.** The author's conclusion: with ~350 independently governed
   PMCs/PPMCs plus continuous Incubator ingress of new projects,
   hosting-PMC supply is structurally abundant and elastic relative to any
   realistic campus-chapter demand curve. A formal waitlist/queuing plan
   and a PMC-recruiting-pace plan would be solving a problem that doesn't
   arise at this program's scale — retired as a design gap rather than
   worked through.
   Initial framing raised Apache Airavata as precedent for the ASF
   spinning up a TLP ad hoc specifically to teach open source; checked and
   found **inaccurate** — Airavata incubated on a normal timeline (May 2011
   → TLP Sept 2012), originating as genuine Indiana University research
   infrastructure (science-gateway workflow tooling); no teaching motive
   appears in the actual incubator proposal. A real adjacent precedent
   exists instead: IU's own "Applied Distributed Systems" course
   (courses.airavata.org, taught by Airavata's founders) already uses the
   *existing* Airavata project as a hands-on vehicle that produces real ASF
   committers/PMC members — evidence the underlying pattern (student →
   real ASF contributor) works, though it's for-credit, in tension with
   this program's own no-academic-credit rule, so treat it as evidence for
   the concept, not a template to copy. If a genuinely dedicated
   teach-open-source vehicle is ever wanted as a reference point, ComDev
   itself (board-chartered 2009 specifically to grow OSS practice, not ship
   a product) is the accurate example of that pattern — not an ad hoc TLP.

Lower-priority items noted along the way, not yet revisited: international
considerations (non-US IP regimes, export control, GDPR on the
alumni/talent directory — deferred, pilot can be US-campus-first); overlap
with existing corporate-sponsored community programs at specific large
projects (check before matching a chapter to, e.g., Kafka or Airflow);
Code of Conduct escalation path at the local chapter/event level (small
addition to the existing ASF-wide CoC process, not a redesign);
good-first-issue quality bootstrapping for PMCs that don't already
maintain a curated newcomer backlog; and naming/ownership of who actually
builds the chapter-in-a-box materials (currently implicit ComDev
ownership, no named volunteer or deadline).

Also unresolved, flagged during the IEEE-mapping discussion: what to call
the top-tier committer/PMC-adjacent recognition if it needs a name at all
for messaging purposes — deliberately left open rather than inventing
terminology that might collide with something the wider ASF community
already uses.
