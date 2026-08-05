---
title: ComDev Code of Conduct revision — adding enforcement specificity within Delaware nonstock/501(c)(3) constraints
compiled: 2026-07-30
status: living document — in progress, more sessions to be folded in
---

# ComDev Code of Conduct revision

Started as a conversation between a ComDev PMC member and the ComDev PMC
Chair. Shared diagnosis: the current ASF Code of Conduct
([apache.org/foundation/policies/conduct](https://www.apache.org/foundation/policies/conduct))
reads as a **"what," not a "how"** — seven behavioral principles, a list
of prohibited conduct, a reporting address — with no defined investigation
process, no defined consequences, and no defined authority for who can
impose what. The goal of this thread is to add that missing procedural
specificity. This is explicitly a living document; expect more sessions
appended over time as the conversation with the Chair develops.

## Baseline: what exists today

- **Code of Conduct** (apache.org/foundation/policies/conduct): 7
  principles (be open, be empathetic/welcoming, be collaborative, be
  inquisitive, be careful with words, be concise, step down considerately)
  + a prohibited-conduct list (threats, discriminatory language, doxing,
  sexual harassment, personal insults, etc.) + reporting contacts
  (President, EVP, VP Diversity & Inclusion, or a project's `private@`
  list for doc/code-specific issues). No defined process past "report it."
- **Anti-Harassment Policy** (apache.org/foundation/policies/anti-harassment.html):
  narrower, event-scoped. Reporting goes to event organizers/security;
  resolution language is just "organizers may take any action they deem
  appropriate, including warning the offender or expulsion from the event
  without a refund." Also thin on actual investigation mechanics.
- Neither document links its enforcement path to the ASF Bylaws' actual
  membership-governance mechanics (see below) — that gap is a large part
  of why both currently read as toothless.

## This was already a live board-level effort — now clarified by direct VP Legal input

Board minutes show this exact gap has been under active board discussion
for roughly a year, independent of this ComDev conversation:

- **2025-09-24** ([minutes](https://apache.org/foundation/records/minutes/2025/board_minutes_2025_09_24.txt)):
  board reviewed a draft/WIP CoC. One director's objection: *"a committee
  with teeth is needed before approval"* — nearly identical framing to
  this conversation's starting complaint. Another director asked whether
  an enforcement committee is even needed. Board voted to task the EVP
  with driving the process forward.
- **2026-01-21** ([minutes](https://apache.org/foundation/records/minutes/2026/board_minutes_2026_01_21.txt)):
  EVP reports the "Code of Conduct email to outside counsel delayed from
  December to January due to concerns with pro-bono limit." The Board
  Chair names the CoC as a personal focus for the month, alongside the
  Members Meeting. VP Legal sends a clarification to board@ and is
  "awaiting further instructions."
- **2026-05-20** ([minutes](https://apache.org/foundation/records/minutes/2026/board_minutes_2026_05_20.txt)):
  VP Legal announces intent to resign; a successor process kicks off.
  Legal Affairs Committee report otherwise minimal that month.
- **2026-06-17** ([minutes](https://apache.org/foundation/records/minutes/2026/board_minutes_2026_06_17.txt)):
  no CoC content at all — the effort appears to have gone quiet during
  the VP Legal transition.

**Update (2026-07-30, direct conversation with the current VP Legal):** the
outside-counsel review referenced in the January 2026 minutes **did
complete** — it wasn't merely delayed or gone quiet, as the board minutes
alone suggest. It was **found insufficient**. That's very likely why the
Board's posture, per the same conversation, is now **Board ownership with
ComDev input** — not full board ownership excluding ComDev, and not
ComDev independently drafting-and-proposing either. Full answer set below
under "Questions for the VP Legal."

**Implication, carried forward:** ComDev's role is confirmed as input into
a Board-owned process, not independent authorship. The CoC remains a
**foundation-wide, board-owned policy** — ComDev doesn't own it, even
though community-health expertise is squarely ComDev's remit. ComDev's job
is producing well-scoped, well-reasoned input (this document) for that
Board-owned process to use — not producing a competing draft to route
around it.

## The Delaware / 501(c)(3) legal tension — plain-language grounding

Two distinct legal layers get conflated here; worth keeping separate when
talking to outside counsel:

- **501(c)(3)** is *federal tax law* (IRS). It constrains things like
  private inurement, private benefit, and the dissolution clause. It has
  essentially nothing to say about how an individual member gets
  disciplined.
- **Delaware nonstock corporation law** (Title 8, applied to nonstock
  corporations via §114) is the actual operative constraint. The ASF is a
  Delaware nonstock membership corporation, and **ASF Members are
  literally "members" in the Title 8 sense** — the body that elects the
  Board and votes on corporate matters. That's the "ownership" analog:
  no equity/residual claim (nonprofits can't distribute surplus), but
  real governance control.

The [ASF Bylaws](https://www.apache.org/foundation/bylaws.html) already
lock down how that status can be touched, and it's a high bar:

- **Termination** of a Member requires "an affirmative vote of a
  two-thirds majority of the members of the corporation" (§4.7) — not the
  Board, not an officer, not a committee.
- **Involuntary conversion to emeritus** (benching voting rights) requires
  the same two-thirds membership vote.
- Delaware's Title 8 doesn't spell out a specific due-process statute
  (notice/hearing) for nonstock member expulsion. That gap gets filled by
  (a) whatever procedure the corporation's own bylaws commit to — which
  becomes legally enforceable once written — and (b) general common-law
  expectations courts apply to membership associations disciplining a
  member with substantial governance rights (roughly: meaningful notice
  of the charge, real opportunity to respond, before any vote). **Open
  item for actual outside counsel to confirm**, not settled here.

**Consequence:** a CoC "committee with teeth" cannot itself expel or
suspend someone's ASF Membership without either (a) working through the
existing §4.7 membership-vote mechanism, or (b) the Board pursuing a
bylaws amendment to delegate that power elsewhere — a materially bigger,
slower lift than a CoC revision normally implies. This is very likely a
large part of why outside counsel and the board have been stuck for a
year.

## The layered model — how to get real teeth without waiting on the stalled legal track

Originally scoped as three layers. Working through layer 2 in detail
surfaced a real split: **removing someone as PMC chair is not the same
kind of action as removing them as a committer/PMC member** — a chair
also holds a Board-appointed corporate officer title, so it doesn't
belong in pure PMC self-governance territory. That split promotes it to
its own layer. Now four:

1. **Space/access-level actions** — muting a list, removing someone from
   an event, revoking a role account, temporary cool-down from a channel.
   Pure officer/committee operational discretion today; no bylaws
   implication. This is where most of the "toothless" complaint can be
   fixed immediately, with no legal dependency.
2. **Project-role-level actions** — pulling commit karma, removing someone
   from a PMC's committer/PMC-member roster. Already governed by each
   PMC's own merit process; the CoC can *require* a PMC to take up a
   finding and respond within a defined window, but cannot dictate the
   outcome — 100% stays the PMC's own consensus vote.
3. **Officer-level actions** — removing someone as PMC chair, or any other
   Board-appointed officer title (President, EVP, VP D&I, VP Legal, etc.).
   Even when a PMC vote initiates a chair removal, the chair title itself
   is a corporate officer appointment — likely needs actual Board action,
   not just a PMC's internal vote. Almost entirely unresolved; needs
   Board/VP Legal input on the actual mechanics.
4. **ASF-Membership-level action** — termination or involuntary emeritus
   conversion. Locked to Bylaws §4.7's two-thirds membership vote. The
   most any committee can do here is build a documented case and *refer*
   it to the membership — not execute it itself.

**Working conclusion:** write concrete "how" mechanics for layers 1–3 as
they become tractable — layers 1 and 2 are legally unblocked and can move
independent of the stalled Delaware question; layer 3 needs the VP Legal
conversation before it can be drafted at all. Keep layer-4 language
deliberately thin ("consistent with Bylaws §4.7") and let that piece ride
on the board's outside-counsel track rather than inventing new mechanics
in parallel.

## Adoption / publication mechanics — how any of this actually becomes policy

Per direct VP Legal input (2026-07-30), there are two possible paths for
formally adopting a CoC revision, independent of what the content ends up
saying:

- **Path A — the Board directly adopts the policy.** The Board itself
  reviews and votes on the actual text. Carries more institutional
  weight — the same body that raised "a committee with teeth is needed
  before approval" would be voting on the specific language, not
  delegating that judgment elsewhere.
- **Path B — the Board directs the President to adopt and publish it
  under existing presidential authority.** A single Board resolution
  authorizes the President to act, rather than the Board reviewing and
  blessing exact document language. Lighter-weight, and decouples
  *getting authorization to proceed* from *having fully finished,
  legally-vetted text* — meaningful given how much of this document is
  still draft (Layer 3's non-chair officer mechanics, the
  reporter-attribution tension, the severity rubric). Also keeps the
  document genuinely living: future refinements could be folded in under
  ongoing presidential publishing authority without a fresh Board
  resolution each time.

**Not yet decided which path to pursue** — genuinely more a political read
on this specific Board's posture (given the CoC's history and the
"committee with teeth" objection) than a legal question, and the author
is better positioned to judge that than this document. Whichever path is
chosen shapes how the August submission itself should be framed: Path A
implies asking the Board to review specific language (a heavier, likely
premature ask given how much is still open); Path B implies asking the
Board to authorize forward motion now, with content following.

## Layer 1 mechanics: space/access-level actions (draft, for later review)

First detailed pass at the layer-1 "how." Scope: temporary, reversible
restrictions on access to a *specific space* — a mailing list, chat
channel, issue tracker, wiki, event, or a non-merit tool privilege (e.g.
wiki edit rights). Explicitly excludes PMC roles/committer status (layer
2), officer titles (layer 3), and ASF Membership itself (layer 4).

**An escalation ladder, not a binary:**
1. Informal private note — no formal record, first-line response for a
   one-off lapse.
2. Documented written warning — formal, logged.
3. Temporary moderation of one space (posts held for review), fixed
   window.
4. Temporary full restriction from one space, fixed duration.
5. Removal from a specific event — already has precedent in the
   Anti-Harassment Policy; this generalizes it.
6. Cross-space restriction — reserved for repeated or severe conduct.
7. Revocation of a non-merit tool privilege.

**Who can act — solving the single-person-dependency problem:**
- Steps 1–3 (single space) stay with whoever already has that authority
  today — list moderators, PMC members. Nothing new needed; the CoC
  should just say explicitly this is expected first-line behavior, not
  something requiring escalation.
- Step 4 and above requires sign-off from **two members of a small
  rotating CoC response team** (3–5 people) — never a single
  officer acting alone, never permanently the same two people.
- **Emergency exception:** for an active, ongoing safety situation, one
  person can act immediately, but it must go to the full rotating team
  for confirm/reverse/extend within 48–72 hours. Mirrors what the
  Anti-Harassment Policy already allows event organizers to do in the
  moment.

**Team composition, selection, and accountability (draft — resolves
"who watches the watchers"):**
- **Selection is by nomination, not self-application.** Self-selection
  into a role with power to sanction others is a known adverse-selection
  risk — the people most drawn to volunteer for that kind of authority
  are not reliably the people best suited to hold it. Candidates should
  be proposed by existing rotating-team members, `wg-code-of-conduct`,
  or the ComDev PMC broadly — someone with an existing track record
  vouching for them — rather than raising a hand. Self-nomination isn't
  banned (a volunteer org can't afford to turn away genuine volunteers)
  but should require an existing PMC member to second it, not be
  accepted on its own strength. Same underlying pattern as ASF's
  Security Team: invitation into a vetted group, not open application —
  already the model proposed below for the `coc-response-team` ACL
  group; worth applying to the humans, not just the tooling.
- **Screen for absence of the wrong signal, not just presence of the
  right one.** Recent involvement as the subject of a complaint, an
  active dispute with someone in the nominating pool, or a visible
  pattern of seeking authority over others are reasons to slow-walk or
  decline a nomination.
- **Volunteer constraint shapes rotation.** All roles here are unpaid.
  Terms should be staggered (like board classes — not everyone rotating
  out at once) rather than a short, uniform monthly rotation: CoC
  casework benefits from institutional memory of prior incidents/patterns
  in a way a faster handoff wouldn't, but the same anti-burnout,
  anti-capture logic still argues for guaranteed turnover.
- **No-fault exit, explicitly.** Nobody can be compelled to keep doing
  unpaid, emotionally heavy, confidentiality-bound work. Stepping down
  must be trivial and stigma-free, same principle as the no-fault PMC
  hosting exit in [[comdev-university-membership-pipeline]] — the
  alternative is the team silently re-concentrating into whoever's
  still willing, recreating the single-person-dependence failure mode
  this design exists to avoid.
- **Removal-for-cause uses the same mechanism that seated them** —
  PMC/`wg-code-of-conduct` consensus, not internal team self-policing. A
  team member who is themself the subject of a substantiated complaint
  is handled through this same CoC process, recursively, like anyone
  else.
- **Confirmation and removal-for-cause mechanism, specified
  (2026-07-31):** standard ASF lazy consensus — proposal posted to
  `wg-code-of-conduct`, stands absent a PMC-member objection within 72
  hours — rather than a heavier invented formal-vote process. Reality
  check from this same conversation: whatever gets written down, actual
  seating decisions in a volunteer org like this will run on lazy
  consensus among a self-selected pool regardless, so the design should
  describe what will actually happen rather than an idealized process
  nobody follows. The real safeguard against a bad seating is the
  checkable-fact interim-measure triggers and two-person sign-off
  governing actual casework, not the seating formality itself. A member
  facing a removal-for-cause proposal is recused from active casework
  for its duration; no-fault exit remains available at any time instead.
- **Term length, specified (2026-07-31, revised same day):** 1 year,
  coinciding with the team's own annual review point rather than running
  on a separate clock — since that annual review already exists, a
  longer staggered term would just be a second, redundant schedule.
  Renewal runs on the same lazy-consensus mechanism as initial seating
  (continues unless a PMC member objects at the review point), so
  continuity in practice rests on lazy-consensus inertia rather than a
  forced multi-year term or separate per-seat staggering. (3 seats to
  start, growing toward 5 as capacity allows.)
- **The team does not review or renew itself.** The annual sunset/review
  point (governance hooks, below) is conducted by the Board or, where it
  touches §4.7-adjacent territory, the Membership — not
  `wg-code-of-conduct` or the response team assessing its own
  continuation. This also likely answers the top-level adoption
  question: ComDev can draft and pilot the layer-1/2 operational
  mechanics under existing PMC/working-group discretion, but the CoC
  document itself, as a foundation-wide policy, still needs Board (or
  Membership) ratification to formally supersede the current text —
  **working assumption, not confirmed.**
- **Recruitment cost, named honestly.** Nomination-based selection
  (above) narrows an already-thin volunteer pool further, in an org with
  a chronic capacity constraint. This is an accepted trade-off for
  adverse-selection safety, not a problem assumed away.
- **Reality check (2026-07-30):** in practice, this team will likely
  start as a self-selected, ad hoc group of volunteers for a while,
  rather than the nomination model above taking hold immediately —
  named explicitly rather than assumed away. The quantifiable,
  checkable-fact discipline built into the interim-measures triggers and
  the two-person sign-off (below) is the safeguard that holds regardless
  of how cleanly the team itself got seated — it doesn't depend on
  selection being clean to still constrain subjectivity and abuse.
  Nomination-based selection remains the target to work toward, not a
  precondition for the rest of this design to function.
- **Whole-team misconduct — resolved (2026-07-30), made actionable
  (2026-07-31).** Handled by the Board directly, not a newly-invented
  escalation body: the Board has standing access to the underlying case
  records with PII obfuscated (see Recordkeeping, below) — not just the
  quarterly aggregate counts — specifically so it can directly observe
  patterns or complaints about the team's own conduct. That visibility
  now pairs with an explicit action: the Board can initiate the same
  lazy-consensus removal-for-cause mechanism above against a team member
  directly, or in extremis vote to dissolve and reconstitute the team,
  under its ordinary existing oversight authority — no new authority
  invented, just applied here explicitly.
- **Appeal quorum — resolved (2026-07-31).** Thin by construction on a
  3–5 person team (if 2 acted, as few as 1 remain "uninvolved" to hear
  an appeal) — narrowing who's *on* the team doesn't fix this. Rejected
  both originally-floated fixes as insufficient alone (VP D&I alone
  concentrates repeat appellate load on one volunteer officer;
  `wg-code-of-conduct` broadly has its own undefined size/quorum).
  **Design:** primary reviewers are uninvolved response-team members;
  when fewer than 2 remain, the appeal routes to a small standing
  **Board-level backstop group** (2–3 Board-designated members, rotating
  at the Board's own discretion) — reuses the Board's already-
  established standing case-record access, so no separate
  onboarding/disclosure step is needed per appeal.
- **Ad hoc → nomination transition trigger, specified (2026-07-31):**
  tied to the existing annual review point rather than a separate
  deadline — the team formalizes to the nomination model no later than
  its first annual review, sooner if seats fill informally before then.

**Process and timeline:**
1. Report comes in (existing `private@` addresses, or a new low-effort
   `coc@` alias monitored by the rotating team).
2. Acknowledged within a fixed window (e.g. 3 business days).
3. Triaged: layer 1, or does it actually belong at layer 2/3/4? If so,
   escalate immediately — outside this team's authority.
4. The person reported gets notice of the specific conduct at issue and a
   chance to respond, except under the emergency exception above.
5. Decision + a short written rationale, communicated to both sides.
6. Every temporary action gets an explicit expiry date — nothing
   open-ended.
7. **Appeal:** request review within a fixed window (e.g. 14 days) by
   rotating-team members not involved in the original decision, or by the
   VP D&I for an independent look.

**Recordkeeping and reporting:** minimal, private logging — date, space,
action, duration, general category (not full narrative) — visible only to
the rotating team and relevant officers. Same minimal-data-footprint
principle as guardrail #7 in [[comdev-university-membership-pipeline]].
Quarterly aggregate counts (no case detail) reported out. **Additionally (2026-07-30):** the Board
has standing access to the underlying case records with PII obfuscated —
not just the aggregate counts — specifically so it can directly observe
patterns or complaints about the team's own conduct, rather than relying
solely on the team's own self-reporting.

**Governance hooks:** a named point of *contact* for questions, never
sole decision authority (satisfies "no single-person dependency" without
leaving the process ownerless); a sunset/review clause where
`wg-code-of-conduct` reviews and can amend the process after a fixed
period (e.g. one year).

**Interim/precautionary measures (draft — distinct from the ladder
above):** Provisional, non-punitive holds applied *during* an open
investigation, before the notice-and-response step of the process
timeline completes — distinct from a final ladder sanction. Must be
framed explicitly as protective risk mitigation, not a pre-judgment of
guilt, to stay consistent with the common-law "meaningful notice +
opportunity to respond before any vote" expectation flagged in the
legal-tension section above.

*Trigger criteria — checkable facts, not a severity judgment (deliberately
scoped this way; the qualitative severity rubric that would otherwise gate
layer-1-vs-2 routing is a separate, harder, not-yet-drafted piece):*
1. Reporter and subject are both active in the same space, and the
   subject holds tool/access power over the reporter there (moderator,
   list owner).
2. The complaint is specifically about the subject's use of a privileged
   tool — leaving that access in place risks interference with the
   investigation itself.
3. The conduct at issue is verifiably still live/ongoing, not a
   completed past incident.
4. Prior record on file — a checkable count of the subject's own prior
   interim measures/sanctions within a window.
5. Reporter's stated unwillingness to continue participating while the
   subject retains access — a declared fact, not an assessment of
   whether the concern is "reasonable." **Flagged as the most
   abuse-prone trigger** (see below) since it's the only one that's
   purely self-attested with no independent corroboration.

*Authorization:* two-person sign-off, same threshold as ladder step 4+ —
no new single-person track. The existing emergency exception already
covers genuinely urgent action; a second single-person path here would
quietly recreate the single-point-authority problem this whole design
works against.

*Scope cap:* limited to the narrowest tools on the ladder — same-space
moderation or access-hold (steps 3–4) only. Cross-space restriction
(step 6) is never available as an interim measure, only as a final
sanction for severe/repeated conduct. **Open tension, not resolved:**
this assumes the conduct stays put during the investigation window; if
it visibly spreads to a second space mid-investigation, the cap as
written doesn't let the interim measure follow it there without
escalating to a step reserved for final sanctions.

*Duration:* hard cap (e.g. 7 days), auto-expiring unless affirmatively
renewed — never silently rolls over. Immediately lifted, with no
residual restriction, if the case resolves without a sanction.

*Notice:* categorical, not narrative, delivered immediately rather than
deferred to the final-decision stage — e.g. "temporary hold pending
review of a complaint in [space], category [X]."

*Appeal:* expedited track (e.g. 72 hours to request review), shorter
than the standard 14-day appeal window for final decisions, given the
provisional and time-sensitive nature of the measure.

*Recordkeeping:* logged distinctly as "interim" vs. "final action" so
quarterly aggregate reporting doesn't conflate provisional holds with
actual sanctions.

*Trigger list is reviewable, not closed* — worth a standing note that
it's appendable at the same cadence as the annual sunset review rather
than presented as exhaustive-by-construction.

**Report-system abuse resistance:** Trigger #5's self-attested nature is
the system's most exploitable point. Mitigation follows the same
checkable-fact discipline as everything else here, and surfaces a
general design principle worth stating explicitly and carrying forward
into future sections: **a quantifiable signal decides when a human
looks, never what they conclude.**
- Symmetric prior-record tracking on the *reporter* side, mirroring the
  subject-side tracker: how often has this reporter's report led to an
  interim measure later lifted with no final sanction? This is a flag
  that routes to human review — it never fires an action on its own.
- First invocation of trigger #5 is taken at face value, no extra
  scrutiny — consistent with everything else on this list being
  judgment-free to invoke. Only once a reporter's own prior-record flag
  shows a pattern (e.g., 2+ priors with no resulting sanction) does
  trigger #5 require the two-person sign-off to explicitly weigh that
  history before acting.
- When a flagged reporter pattern does get human review, the two people
  should weigh context the raw count can't carry: same subject reported
  repeatedly (reads as sustained victimization) vs. different subjects
  across unrelated incidents (more ambiguous either way); and *why*
  prior cases closed without sanction — "insufficient evidence to act"
  is not the same as "affirmatively found meritless," and the log needs
  to capture which, for this review to mean anything.
- The existing bounds (7-day cap, auto-expiry, reversibility, explicitly
  non-punitive framing) already limit the damage of a single gamed
  invocation; the tracker exists to catch *repeated* gaming, not first
  instances.
- A demonstrated pattern of bad-faith reporting is itself CoC-covered
  conduct — routes back through this same process as a complaint
  against the reporter, rather than needing a separate mechanism.

**Open, high-abuse-potential tension — flagged, not resolved:** the
reporter-side tracker requires reports to be attributable to a stable
identity (even privately/pseudonymously), which is in direct tension
with any aspiration toward anonymous reporting the base CoC or
Anti-Harassment Policy might otherwise want to support. Two distinct
risks follow, worse than the subject-side equivalent: (a) a
reporter-attribution dataset is itself a high-value target — if
compromised or accessed outside the narrow rotating team, it's a map of
who reports CoC violations, more sensitive than an ordinary
disciplinary log; (b) even with the "flag, not verdict" discipline
above, the review step depends on case-closure reasons being recorded
accurately and honestly — a rotating team that gets this wrong (or is
pressured to) could still discredit a genuine repeat victim. Needs real
review before this goes anywhere near implementation, not just the
mitigation sketch above.

### Infra requirements to support this (open — needs an actual Infra conversation)

Split into what's likely already possible vs. genuine new asks; none of
this has been confirmed with Infra yet.

**Likely already exists — confirm, don't build:**
- Per-address mailing list moderation (ezmlm-based lists generally
  support moderating a single subscriber, not just the whole list) —
  confirm whether it's self-service for list owners or Infra-only.
- GitHub org-level "block from organization."
- Slack/chat channel removal or mute via existing workspace admin
  controls.
- JIRA/Confluence per-account restriction on commenting/editing.

**Genuine new asks:**
1. A private, access-controlled record space (private JIRA project or
   repo) for the rotating team's logs, with ACLs kept in sync as team
   membership rotates.
2. A trusted requesting-authority group (e.g. an LDAP/ACL group like
   `coc-response-team`) that Infra treats as authorized to request these
   specific actions — same pattern as other trusted groups (e.g.
   Security Team) — so the general ticket queue can't be abused to
   silence someone under false CoC pretense.
3. An expedited, private ticket queue, separate from the public Infra
   queue — time-sensitive, and shouldn't be visible to the person being
   actioned.
4. Expiry/auto-reversal handling — every layer-1 action has a fixed
   expiry by design; unclear whether anything auto-reverses a ban/mute on
   a date or whether that's entirely manual today. If manual, needs
   either a small volunteer-buildable script or an explicit owner to
   track it by hand.
5. Emergency-path latency — the single-person emergency exception is
   only honest if the relevant actions are genuinely self-service/instant
   (e.g. a list moderator flipping a flag) rather than "file an Infra
   ticket and wait." Needs a per-action answer, not an assumption.
6. **Structured, queryable storage, not just narrative logs** — the
   prior-record trackers (subject-side and reporter-side, see
   Interim/precautionary measures above) need per-identity counts within
   a time window. That's a small structured store, closer to a
   lightweight database than a JIRA project full of free-text tickets —
   ask #1 above needs to accommodate this, not just narrative case
   entries.
7. **An interim-vs-final field in the log schema** — otherwise quarterly
   aggregate reporting conflates provisional holds with real sanctions.
8. **Active auto-expiry for interim measures specifically** — stricter
   and shorter (e.g. 7 days) than ordinary ladder-action expiry (ask #4),
   and must not silently persist past its cap; needs an active alert,
   not passive manual tracking.
9. **An audit trail for the two-person sign-off itself** — who signed
   off, when — so "never a single officer acting alone" is verifiable
   after the fact, not just asserted.
10. **Reporter-attribution storage, if built at all, needs tighter
    access control than the general record space (ask #1)** — see the
    open tension flagged above; this is a higher-sensitivity dataset
    than an ordinary case log and shouldn't inherit the same ACL model
    by default.

**Bigger open question:** is there value in a more centralized flag on
the LDAP identity itself, or does every tool (GitHub, Slack, JIRA,
Confluence, mailing lists) stay independently actioned regardless? That
answer determines how painful ladder step 6 (cross-space restriction) is
in practice — worth resolving before the doc promises something that's
actually five separate manual tickets every time.

## Layer 2 mechanics: project-role-level actions (draft, for later review)

Scope: removing someone from a PMC's committer/PMC-member roster, or
pulling commit karma. Explicitly **excludes PMC chair** (moved to layer 3
— see above) and anything touching ASF Membership (layer 4).

**Core principle — referral, not execution.** Carries over directly from
the existing guardrail in [[comdev-university-membership-pipeline]] ("all
committer/PMC-member nomination decisions stay 100% with the hosting
PMC... the program has zero authority there"). The CoC process cannot
execute a layer-2 action. It can only **require the PMC to take the
matter up and respond within a defined window** (e.g. 30 days) — never
compel a specific outcome. The PMC's own consensus vote stays fully
intact.

**Sequencing:** selectable by severity, not a mandatory escalation chain.
A single severe incident can go straight to a layer-2 referral without
first exhausting the layer-1 ladder.

**Conflict of interest / recusal:** any PMC member with a personal tie to
the situation should recuse from that PMC's vote on the matter — informal
Apache norm already, worth stating explicitly here.

**Interdependencies with layer 1:**
- **Evidence handoff.** Layer 1's logging is deliberately minimal
  (category, not narrative) for privacy. A PMC asked to vote on removing
  someone needs more than that to decide responsibly. Implies a
  bifurcated record: thin aggregate log for routine reporting, plus a
  fuller confidential case file compiled only at the moment of referral
  upward. Not yet designed.
- **Cross-project pattern detection.** If conduct spans multiple ASF
  spaces/projects, the layer-1 rotating team may be the only party
  positioned to see the pattern, but layer-1's privacy design means no
  single PMC sees it automatically. Needs a defined minimal-disclosure
  protocol for notifying a specific PMC's `private@` at referral time,
  without over-sharing.

**Open: what if the PMC declines to act?** No defined escalation yet for
a PMC that receives a substantiated referral and simply doesn't act — the
same shape of unresolved problem as the "chapter failure modes / off-ramps"
gap in [[comdev-university-membership-pipeline]]. Likely traces back to
the Board's reserve authority over any PMC, but unconfirmed.

**Infra angle — lighter than layer 1.** Unlike layer 1, this likely needs
**no new Infra capability** — PMCs already have self-service tooling for
managing their own committer/PMC roster (existing committee-info/roster
mechanism, Whimsy tooling). The CoC's job is creating the *obligation to
use* that existing power when warranted, not building anything new.
Worth confirming this assumption with Infra alongside the layer-1
questions, but it's a much lighter ask.

## Layer 3 mechanics: officer-level actions (draft — chair removal now
confirmed, other officer titles still open)

Scope: removing someone as PMC chair, or any other Board-appointed
officer title (President, EVP, VP D&I, VP Legal, etc.). Split out from
layer 2 because a chair title is a corporate officer appointment, not
pure project self-governance — even though a PMC vote is usually what
triggers it.

**Chair removal, confirmed (2026-07-30, direct VP Legal input):** a PMC
vote to remove its own chair **does** require separate, explicit Board
action to take effect — the Board's normal ratify-what-the-PMC-nominates
practice does *not* cover removal informally. This is not a special or
rare event: it's **handled routinely, monthly**, as part of ordinary
Board business. That materially de-risks this piece of layer 3 — the
mechanics are simply: PMC votes to remove chair → referred to the Board's
existing monthly ratification process → takes effect on Board
confirmation. No new mechanism needs inventing; the CoC's job is
documenting this existing path clearly and pointing a PMC at it, the same
"obligation to use existing power" framing as layer 2's infra angle.

**Still open:** the equivalent mechanics for removing any *other*
Board-appointed officer (President, EVP, VP D&I, VP Legal) — the chair
question is answered, but those roles don't have an initiating "PMC vote"
to point to, so what triggers a review of *their* conduct, and by whom,
is undefined.

**Edge case, resolved 2026-07-31 (briefs Q9):** the current CoC's
designated report recipients (President, EVP, VP D&I) are themselves
officer-level roles. If one of them is the subject of a CoC complaint,
the normal reporting path is directly conflicted. **Answer: report
directly to the Board (board@, or a designated non-conflicted
director).** This follows structurally from §8's own §6.5/§6.2 analysis —
the Board is the only body with authority over the President/EVP — so
this is a two-sentence CoC addition, no bylaws dependency. Non-chair
officer *removal* mechanics (§6.5: total Board discretion, no defined
process) remain the separate, still-open piece — see
[[comdev-coc-legal-questions-and-briefs]] Q8.

## Layer 4 mechanics: ASF-Membership-level action (draft — enriched
2026-07-30 with existing-mechanism detail; corrected and substantially
resolved 2026-07-31 by research briefs in
[[comdev-coc-legal-questions-and-briefs]])

Scope: termination or involuntary emeritus conversion, locked to Bylaws
§4.7's two-thirds membership vote. Deliberately kept thin per the working
conclusion above — this doesn't invent new mechanics, it points at what
already exists.

**Correction (2026-07-31, briefs Q5):** the "2 years of inactivity"
precedent stated below did not hold up under closer bylaws review — there
is **no fixed inactivity horizon in the bylaws at all**, and the confirmed
practice figure is **~5 years**, not 2. The bylaws' actual mechanism is
either §4.3 (voluntary, requires the member's own signed notice — silence
doesn't satisfy this) or §4.4 (involuntary, two-thirds vote, no stated
trigger); which door the existing practice actually runs through is still
unconfirmed. Also important: the practice's **recorded purpose is quorum
management**, not conduct — extending it to CoC cases is a genuine
purpose extension, not "we already do this," and the framework should say
so plainly rather than lean on it as a clean precedent.

**Correction (2026-07-31, briefs Q6):** reactivation from emeritus is
**not** simple request-based, as previously assumed here. §4.5 requires
the member's written request **plus a new membership application plus an
affirmative majority vote of the members** — effectively re-election, at
a lower (majority, not two-thirds) bar than the vote that converted them
out, but a real gate, not an automatic reversal.

**Resolved (2026-07-31) — see
[[comdev-coc-legal-questions-and-briefs]] Q1, Q2, Q7:**
- The Board *can* reach delegation of §4.7-adjacent authority, but only
  via its unilateral bylaws-amendment power (Art. X), not an ordinary
  resolution — and doing so would be politically explosive (stripping the
  membership's own §4.4/§4.7 protection) and reversible by the membership
  re-amending. **Document-and-refer remains the sound design on both
  legal and political grounds**, not just as a stopgap pending a slower
  legal track.
- A document-and-refer committee that only investigates and recommends —
  never decides or binds — raises no legal issue: DGCL §141(c)'s
  board-power formality doesn't reach purely advisory bodies.
- 501(c)(3) status imposes essentially no obligation here; member
  discipline is a state-law (Delaware nonstock corporation) matter, not a
  federal tax-exemption one.

**Still open:** the common-law procedural floor for a §4.7 vote (notice +
opportunity to be heard + following the org's own rules — briefs Q4)
confirms the "conservative assumption" this framework already uses is the
right one, but isn't itself a bylaws requirement to point to. The
conduct-action log's legal exposure (discoverability, defamation,
retention, and an open GDPR question for any org with EU participants —
briefs Q10) hasn't been addressed anywhere in this framework yet and
should be before the reporter-attribution tracker design goes further.

## Scope of enforcement: off-platform / social-media conduct (new,
2026-07-31, from [[comdev-coc-legal-questions-and-briefs]] Q11)

Not previously flagged anywhere in this document — a real gap, not just
an unresolved detail. The September 2025 wiki draft's scope language
("official or unofficial" spaces) is legally actionable — association
discipline is contractual; an org can reach conduct outside its own
spaces if its adopted rules clearly say so and it follows its own
procedure (*Dawkins v Antrobus*, no First Amendment bar) — but it is
**broader than every surveyed peer CoC** (Contributor Covenant, Linux
kernel, Debian, Rust: own venues only; CNCF: external spaces only when
"directed at" a CNCF project/community/participant; PSF: enumerated
spaces plus a harm-triggered case-by-case test in enforcement
procedures, not the scope section). Undefined blanket scope is exactly
the vagueness that produced both the rare successful legal challenges and
the real governance blowups (OpalGate 2015, Drupal/Garfield 2017, Linux
kernel 2018) — the risk is political/reputational as much as legal.

**Recommended fix, to land before the August submission:** drop
"unofficial" as a scope category. Scope = ASF-managed spaces + conduct
"representing the ASF" (Contributor Covenant 2.1 baseline), plus a
CNCF-style clause reaching cross-platform harassment *directed at* an ASF
project/community/participant, with a PSF-style harm-triggered
admissibility test (safety-impact, not blanket jurisdiction) living in
the enforcement procedures rather than the scope section. This also
matches the framework's existing checkable-fact discipline (interim
measures, etc.): ASF can only action its own spaces, roles, events, and
membership status — it should only *claim* jurisdiction it can actually
exercise.

## Editorial note: attribution of recurring design principles

Several design principles recur throughout this document: avoiding
single-person dependency in CoC intake/response, staggered/rotating
terms, a named point of contact without sole decision authority, a
sunset/review clause rather than an indefinite standing body, working
inside the existing `wg-code-of-conduct` structure rather than inventing
a new one, minimizing new budget/tooling asks, and preferring concrete,
templated process documents over principle statements. These reflect the
current ComDev PMC Chair's own stated governance preferences and design
opinions, expressed directly in conversation with the author — they are
not confirmed ComDev PMC or Board requirements, and should be treated as
candidate guardrails to validate with the Chair (and, where relevant, the
wider PMC or Board) rather than as settled constraints.

## External gap review of the draft policy text (2026-07-31)

A reviewer with legal context sent a 14-point gap analysis of
[[comdev-code-of-conduct-draft]] directly (their own separate CoC draft
apparently covers some of the same ground) — full list preserved in
[[comdev-coc-draft-external-gap-review]]. Triaged:

**Already resolved before this review landed:** the scope-of-application
gap they flagged was already added the same day (Section 4's "Scope of
applicability" paragraph) — likely reviewed against an earlier copy.

**Fixed same-day, low-risk/clear-default items:** a "No Action"
disposition (closure-reason recording, notification, quarterly-aggregate
inclusion); a base 14-day appeal window for final (non-interim) ladder
actions, reusing the Board-level backstop group already designed for
appeal quorum; per-case recusal for the response team (mirroring the
Layer 2 PMC-recusal norm); reporter confidentiality and an explicit
bad-faith-reporting rule (previously only an implicit statistical
pattern-flag); a conduct-not-positions clarification; informal-
resolution norms before the formal report path; two internal-consistency
bugs (§10 pointed at "the body designated in Section 6.2" for reviewing
the *framework*, when 6.2 only designates a reviewer for the *team* —
now split explicitly into team-review-by-Board vs.
framework-review-by-`wg-code-of-conduct`; and Sections 2–3's "unchanged"
framing read as two documents coexisting when adoption is meant to fully
replace the current CoC text — reworded to "carried forward, unchanged
in substance").

**Flagged, not designed — genuine judgment calls, not bugs:**
- **A path to permanent exclusion for role-less participants** — the
  most structurally significant gap found. Layers 2–4 all require an
  existing role/title/membership to attach to; a participant with none
  of those can only ever receive Layer 1's deliberately *temporary*
  measures. Needs either a new permanent-exclusion step with a named
  decider and appeal, or an explicit statement of who outside this
  framework holds that power (Infra? a new Board-delegated authority?).
- **Content-level actions** — the ladder governs access to spaces, not
  removal of the offending content itself (a slur in a commit message, a
  doxxing wiki edit). Undefined who acts and how it's logged.
- **Person-based (cross-space) "no contact" measures** — every ladder
  measure is space-scoped today; no mechanism follows a target's
  specific harasser across spaces. Likely needs indirect enforcement
  (breach = new, escalating misconduct) rather than active monitoring.
- **The President's residual role** — the published CoC currently names
  President/EVP/VP D&I as report recipients; this framework substitutes
  the rotating team without saying what's left for the President to do
  in the routine (non-conflicted) case.

Severity-rubric note from the same review: the base CoC (or the
reviewer's own draft) may have Community-Impact-tier language usable as
a seed, rather than drafting the rubric from nothing.

## Open / unresolved — pick up here next

- **TOP PRIORITY — human judgment work still needed: severity rubric.**
  Still fully undrafted. Confirmed (2026-07-30) as still needed, not
  something to quietly drop — gates layer-1-vs-2 routing throughout this
  entire framework. Called out explicitly as the top item of remaining
  *human* (not legal, not mechanical) work.
- ~~**Target: a proposal drawn from this doc is intended for submission at
  the ASF Board meeting on 2026-08-19**~~ **Superseded (2026-07-31):** the
  Chair's actual resolution text instead adopts the pre-existing cwiki
  draft ("the September 2025 wiki draft" / v13, Contributor Covenant
  v2.1-adapted) as the complete, replacement CoC — not a text drawn from
  this document. See [[comdev-coc-v13-proposed-changes]] for the
  resulting near-term work: proposed edits to that draft, reusing this
  document's already-completed legal research, rather than continued
  drafting here toward its own submission.
- ~~Whether a new VP Legal has been seated yet~~ **Resolved (2026-07-30)
  — yes,** and a direct conversation has now happened — see "Questions
  for the VP Legal" below for the full answer set.
- ~~What ComDev's actual role should be framed as~~ **Resolved
  (2026-07-30) — Board ownership, with ComDev input.** Not full board
  exclusivity, not independent ComDev authorship. Shapes the whole
  document's framing going forward: this is input into a Board-owned
  process, not a competing proposal.
- ~~Concrete mechanics for layers 1 and 2 not yet drafted~~ **Drafted
  (2026-07-30)** — see the Layer 1 and Layer 2 mechanics sections above.
  Both still need real review, not yet validated with the Chair, Infra, or
  affected PMCs.
- ~~Layer 3 (officer-level actions) is still almost entirely undrafted~~
  **Partially drafted (2026-07-30)** — chair-removal mechanics are now
  confirmed (PMC vote → routine monthly Board ratification).
  **Confirmed still needing work (2026-07-30):** equivalent mechanics for
  removing any *other* Board-appointed officer (President, EVP, VP D&I,
  VP Legal) — briefs Q8 confirms §6.5 gives the Board unconstrained
  removal authority already, so what's missing is only the
  complaint→Board referral path, not new authority.
  ~~the conflicted-reporting-path edge case when a report recipient is
  themself the subject~~ **Resolved 2026-07-31 (briefs Q9):** report
  directly to the Board (board@ or a designated non-conflicted
  director).
- ~~**New (2026-07-30): Layer 4 enriched, still thin by design** — an
  existing 2-year-inactivity involuntary-emeritus mechanism (believed
  two-thirds vote)~~ **Corrected 2026-07-31:** no fixed inactivity
  horizon exists in the bylaws; confirmed practice is ~5 years, purpose
  is quorum management not conduct, and the mechanism (§4.3 vs. §4.4) is
  still unconfirmed. Emeritus reactivation is **not** simple request —
  §4.5 requires a new membership application plus an affirmative
  majority member vote. Bylaws delegation authority (Q4), 501(c)(3)
  consistency obligations (Q7), and the document-and-refer committee's
  legal standing (Q8) are now all answered — see
  [[comdev-coc-legal-questions-and-briefs]] and the updated Layer 4
  section above. Still genuinely open: the conduct-action log's
  discoverability/defamation/retention/GDPR exposure (Q10), and the
  off-platform scope gap (Q11, new section above).
- **Adoption/publication mechanics documented; decision owner confirmed
  (2026-07-30).** Path A vs. Path B is not the author's call alone — **the
  ComDev Chair and the new VP Legal will jointly pick a path and sign
  off.** See "Adoption / publication mechanics" above and "Legal TODO"
  below. **New supporting fact (2026-07-31, briefs Q3):** the current CoC
  was never Board-adopted in the first place (2014 officer action, no
  board resolution or discussion in the minutes) — strengthens the case
  for Path B.
- Interdependencies between layers, identified while drafting layer 2,
  still need resolving: the evidence-handoff format between layer 1's
  minimal log and a fuller layer-2/3 case file; the cross-project
  notification protocol when the layer-1 rotating team refers a pattern
  to a specific PMC; what happens if a PMC declines to act on a
  substantiated layer-2 referral.
- Rotating-team appointment/accountability drafted (2026-07-30), **fully
  specified (2026-07-31)** — see "Team composition, selection, and
  accountability" under Layer 1 mechanics. Nomination-based selection is
  the target; the team will likely start as a self-selected, ad hoc
  group in practice, formalizing no later than its first annual review.
  Confirmation and removal-for-cause both run by standard ASF lazy
  consensus (72-hour objection window on `wg-code-of-conduct`) rather
  than an invented formal vote — named as the honest expectation for how
  a volunteer org actually seats people, not an idealized process.
  1-year terms coinciding with the team's own annual review point, 3
  seats to start. Whole-team misconduct: the
  Board's existing standing record access now pairs with the power to
  act on it directly (removal-for-cause, or in extremis dissolve/
  reconstitute). Appeal quorum: uninvolved response-team members first,
  falling back to a small Board-designated backstop group (2–3 members)
  rather than a single volunteer officer when too few remain uninvolved.
- Interim/precautionary measures drafted (2026-07-30) — see the
  subsection under Layer 1 mechanics, including trigger criteria, scope
  cap, duration, notice, appeal, and a report-system abuse-resistance
  design built on the principle "a quantifiable signal decides when a
  human looks, never what they conclude." Open within it: the cross-space
  scope-cap edge case, and a high-abuse-potential tension around the
  reporter-attribution data the abuse tracker requires (map-of-reporters
  risk if the dataset leaks; review-step reliability risk if closure
  reasons aren't recorded honestly) — flagged, not resolved.
- ~~Document format itself still needs translation~~ **Addressed
  (2026-07-30)** — see [[comdev-code-of-conduct-draft]] (standalone
  policy draft). This working doc remains the fuller design-history
  record behind that artifact.

## Questions for the VP Legal (2026-07-30) — asked, partially answered

The author has a personal channel directly to the new VP Legal. Original
question list, now annotated with answers from that direct conversation.

**Process/status — where things actually stand**
1. Where did the outside-counsel review actually stall — what specifically
   did counsel flag, beyond the pro-bono capacity issue mentioned in the
   January 2026 board minutes?
   **Answer: unknown — no notes available.** Probably not answerable
   further; not worth continuing to chase.
2. Is that review still active, or does it need to effectively restart?
   **Answer: it was completed, but found insufficient.** Not "stalled" as
   the board minutes alone suggested — it finished and didn't produce an
   adoptable result. Framing updated above.
3. Does the Board still want ComDev's input on this, or has it decided to
   keep full ownership at the board level?
   **Answer: the Board wants Board ownership, with ComDev input** — not
   full exclusive board ownership, and not ComDev independent authorship.
   Resolves the "ComDev's role" open question.

**Bylaws / Delaware mechanics — the core legal tension**
4. Can the Board delegate any part of §4.7's membership-discipline
   authority to a committee by ordinary Board resolution, or does that
   require a bylaws amendment — and if so, does *amending the bylaws*
   itself need a full membership vote, or just the Board?
   **Answered 2026-07-31, [[comdev-coc-legal-questions-and-briefs]] Q1:**
   not by ordinary resolution — but the Board *can* reach it via its own
   unilateral bylaws-amendment power (Art. X), no membership vote required
   for the amendment itself. Politically, though, the Board using that
   power to move the membership's own §4.4/§4.7 protection away from them
   would be explosive and reversible by the membership re-amending — so
   document-and-refer remains the right design, now on political as well
   as legal-speed grounds.
5. Is there any recognized status between "full active Member" and
   "terminated/emeritus" — e.g., a temporary suspension of voting rights
   short of full emeritus conversion — or do the bylaws only recognize
   that binary today?
   **Answer: no formal in-between status — but emeritus members have no
   membership rights until reactivated by their own request.** Softer in
   practice than a hard binary; see Layer 4 mechanics above.
6. What actually has to happen procedurally (notice, opportunity to
   respond, documentation) before a §4.7 termination or
   involuntary-emeritus vote, for it to hold up if challenged? Is there
   real case law/precedent here, or is the ASF building this from
   scratch?
   **Partial answer:** there's already a live, working precedent — 2
   years of inactivity triggers involuntary emeritus conversion today,
   believed (VP Legal: "I think") to require a two-thirds membership
   vote. The specific procedural due-process question (notice, hearing,
   case law) remains open.
7. Does 501(c)(3) status impose any obligations relevant here — e.g.,
   around consistent, non-arbitrary enforcement — even though it's not
   the primary constraint?
   **Answered 2026-07-31, [[comdev-coc-legal-questions-and-briefs]] Q7:**
   confirmed — essentially nothing. Member discipline is a state-law
   matter; none of the federal exemption tests (private inurement,
   private benefit, §4958, lobbying/campaign limits) touch it.
8. Does a committee that only *documents a case and refers it* to a
   membership vote (never deciding anything itself) raise any legal issue
   at all, or is that clearly safe under current bylaws?
   **Answered 2026-07-31, [[comdev-coc-legal-questions-and-briefs]] Q2:**
   clearly safe — DGCL §141(c)'s committee formality only reaches
   committees exercising board power (deciding, binding, approving); a
   purely advisory investigate-and-refer body exercises none of that.
9. **(Layer 3)** if a PMC votes to remove its own chair, does that
   require separate, explicit Board action to actually take effect —
   given the chair title is a Board-appointed corporate officer position —
   or does the Board's normal ratify-what-the-PMC-nominates practice cover
   removal too, informally, without a formal vote?
   **Answer: yes, separate explicit Board action is required — and it's
   routine, handled monthly.** See Layer 3 mechanics above.

**ComDev's standing — does this even need the board track**
10. Are the layer 1–2 actions scoped above (space/access-level: muting,
    event removal, role revocation; project-role-level: PMC-managed
    committer/PMC-member removals) actually fully outside bylaws/Board
    territory, as assumed — or is there a legal reason even those need
    board sign-off?
    **Answer: confirmed outside Board territory** — these are primarily
    under the purview of PMCs (as officers of the foundation) and
    Infrastructure (as stewards of the foundation's resources).
11. Does ComDev (or its `wg-code-of-conduct` working group) have any
    standing to draft and propose foundation-wide CoC changes, or does
    anything beyond layer 1–2 need to originate from the Board/EVP to be
    legitimate?
    **Answer: resolved by Q3** — ComDev's standing is as an input
    provider under Board ownership, not an independent originator.

~~**Still outstanding, needs a follow-up conversation:** Q4, Q7, and Q8~~
**Resolved 2026-07-31** — full research briefs received and folded in
above; see [[comdev-coc-legal-questions-and-briefs]] for the complete
answer set (Q1–Q11), including two items not originally asked: the
2-year-inactivity precedent corrected to ~5 years with an ambiguous
bylaws mechanism (Q5), and a new off-platform/social-media scope concern
not previously flagged in this document at all (Q11 — see new section
below). These are research briefs, not formal outside-counsel legal
advice — still worth a confirming pass with the VP Legal before the
August submission finalizes language that leans on them.

## Legal TODO — concrete checklist for the VP Legal conversation

Consolidated, actionable version of what's still needed from Legal,
requested explicitly (2026-07-30), now mostly resolved 2026-07-31:

1. ~~**Answer Q4**~~ **Answered** — Board *can* delegate via unilateral
   bylaws amendment (no membership vote needed for the amendment), but
   shouldn't; document-and-refer stays the design.
2. ~~**Answer Q7**~~ **Answered** — no relevant 501(c)(3) obligation.
3. ~~**Answer Q8**~~ **Answered** — document-and-refer raises no legal
   issue.
4. **Jointly pick Path A or Path B** with the ComDev Chair, and sign off —
   confirmed (2026-07-30) this is not the author's decision to make
   alone. **Now has a supporting fact (briefs Q3):** the current CoC was
   never Board-adopted in the first place (2014 officer action, no board
   resolution) — Path B has real precedent, including the Board's own
   2025-09-24 use of a light discussion-item vote on this exact topic.
5. **New, not on the original list (briefs Q11):** narrow the draft's
   scope language before submission — see new section below. This is a
   drafting fix, not something that needs further legal input.
