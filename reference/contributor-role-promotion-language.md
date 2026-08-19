---
title: Is "promotion" the right word for committer/PMC roles? (dev@community.apache.org thread)
topics: [governance, terminology]
compiled: 2026-08-04
source: dev@community.apache.org thread, "Is the Committer/PMC member role a promotion for contributors?" (2026-07-22 to 2026-08-03)
status: notes — thread summary plus a first-pass synthesis (2026-08-04);
  no ComDev position taken yet, synthesis flagged for later refinement
---

## Context

A dev@community.apache.org thread questioned whether "promotion" is the
right word for becoming a committer or PMC member, after the thread
originator observed several (P)PMCs using that language informally (e.g.
"[DISCUSS] Promote X as a Y committer"). The core tension raised: a
committer gets commit access and a PMC member gets a binding vote, but
the ASF's "Community of Peers" principle (from The Apache Way) holds
that roles are equal in weight and volunteer contributions are not
ranked — so does calling the transition a "promotion" quietly contradict
that principle by importing a corporate-hierarchy framing?

No resolution was reached; the thread trails off (as of 2026-08-03) with
participants still holding different positions. It reads as a genuine
open question in ASF culture, not a settled norm ComDev could just cite.

## Positions raised, roughly in order

**Against "promotion" framing:**
- The word implies a hierarchy where one person's output/word is "of more
  value" and where the promoted person gets to "command and delegate" —
  incompatible with a peer/expertise model where people just do what
  they're good at.
- Committer/PMC roles are better framed as an added **burden or
  imposition** volunteers take on (extra responsibility, more expected
  care toward peers), not an elevation — "not a promotion at all."
- One participant framed this partly as a **cultural/translation**
  question: to a non-native English ear, "promotion" reads as "this
  person is now more/better," even if that's not the intended American
  usage.
- A later reply reframed the real distinguishing factor as **power**,
  not status: the PMC doesn't "call the shots" — decisions happen on
  dev@ — and if binding vs. non-binding votes are treated the same in
  practice, the distinction is largely formal.
- The most developed rejection (from a participant drawing on a security
  background) argued roles represent **responsibility, not power**, and
  proposed a "zero trust" framing over "trust" language: don't extend
  personal trust, verify (e.g., Apache Airflow's practice of 3 independent
  PMC members verifying each release build, as a safeguard against
  compromised accounts/coercion/crises rather than a trust signal).
  Concluded that PMC membership is closer to **servant leadership** — a
  "shared commitment" and expanded list of expectations (community
  decisions, resolving sensitive issues, branding stewardship, release
  verification, board reports/security response, project direction) —
  and that "promotion" language risks attracting people seeking power or
  control rather than people willing to serve.
- A subsequent reply (an OpenOffice PMC member) endorsed that
  responsibility-list framing without adding a competing view, plus a
  project-specific aside about ensuring PMC representation from each
  Native Language sub-project.

**For "promotion" framing:**
- Read literally, "promotion" just means more responsibility and work
  plus more trust/privilege — not a claim that the person is a "better"
  human being. Pushed back that the ASF's own community.apache.org site
  explicitly uses "ladder" language (the Contributor Ladder page), and
  that "ladder"/"promotion" terminology is standard across the wider
  open-source ecosystem (CNCF, OSPO glossary, other foundations).
  Argued committers *do* have more merit, because they've demonstrated
  and earned it — downplaying that is itself a distortion. Coined the
  framing "those who do the work get to make the decisions" /
  "do-ocracy."
- Later softened toward a practical compromise: consistency in naming
  *across* the ASF has value (so people don't have to re-learn what a
  role means per-project), but individual communities should feel free
  to use whatever word communicates most clearly to their own audience.
  Also noted "committer" itself has drifted — most projects now use
  Review-Then-Commit, so "commit access" means less than it did 20 years
  ago — and pointed to a related, separately contentious thread on
  adopting "maintainer" terminology.

**Middle/reframing:**
- The thread originator, after initial replies, proposed "community of
  peers" (Apache Way language) as the reference point and suggested a
  **"gravity model"** instead of a ladder: people dedicate more and are
  drawn toward more responsibility, rather than rising above others. Also
  noted concrete existing practice: some PMCs (cited: Apache ZooKeeper)
  already avoid "promote" in subject lines, using "[DISCUSS] New
  Committer: X" rather than "[DISCUSS] Promote X as committer."
  Ultimately suggested this may be a genuine cultural/language gap not
  worth forcing to hard consensus.

## Synthesis: what converged vs. what stayed split (2026-08-04)

Captured as a checkpoint for later refinement, not a resolved ComDev
position. Re-reading the positions above, they split into a narrow area
of real agreement and one genuine, unresolved fault line — not a full
consensus.

**What (almost) everyone converged on:** the value of committer/PMC
status is **trust and responsibility**, not command authority. Nearly
every participant reached for "trust" as the operative word
independently, several were explicit that the role does *not* grant the
ability to direct or command other volunteers, and what it concretely
grants is narrow and functional — commit access or a binding vote, not
general authority over people. Nobody argued the roles are valueless;
the disagreement was never "does this mean anything," only what kind of
thing it means.

**Where it genuinely split — the real fault line:** whether that
trust/responsibility increase should be described as the person now
*having more value* (the "for promotion" camp: committers "have more
merit," are "in fact, more" — earned and worth stating plainly,
consistent with community.apache.org's own "ladder" language) — or as
taking on *more service with no claim to added personal worth* (the
"against promotion" camp: "responsibility, not power," servant
leadership, a "zero trust" framing where the point is verification duty,
not personal elevation).

This lines up with the same distinction reached independently while
grounding committer-vs-PMC-member in the official ASF docs (see
[[outreach-identity]]'s "recurring pattern" table): committer
status is an individual, narrow, functional grant; PMC membership is
joining a collective governance/accountability body. The thread's fault
line is really about how to *narrate* that structural fact, not a
disagreement about the structure itself.

**Flagged for later refinement, not resolved here:** whether ComDev
should pick a side of that fault line for its own guidance/messaging, or
deliberately hold both (state the structural facts plainly, e.g. via
[[outreach-identity]], and leave the "is it a promotion"
narration question to individual PMCs/communities as the thread's own
"gravity model" reframing suggested).

## Open questions (unresolved as of thread's end)

- Whether ComDev should (a) recommend specific alternative language
  (e.g. discouraging "promote" in DISCUSS threads), (b) write something
  for community.apache.org clarifying "community of peers" against this
  specific recurring misreading, or (c) treat this as legitimately
  per-project/cultural and not standardize it.
- The thread's "gravity model" vs. "ladder" framings are in direct
  tension with each other, and community.apache.org's own Contributor
  Ladder page already commits to "ladder" — any ComDev guidance would
  need to either reconcile with or knowingly diverge from that existing
  page.
- Nobody in the thread proposed concrete replacement wording beyond the
  ZooKeeper DISCUSS-subject convention; "what should we actually write
  instead" is still open.
- Related, previously contentious naming thread on adopting "maintainer"
  terminology was referenced but not summarized here — may be worth
  pulling in if this topic proceeds, since it's the same underlying
  question (does changing a role's name change how it's understood) one
  layer up.
