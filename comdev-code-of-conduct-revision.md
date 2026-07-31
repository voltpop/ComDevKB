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
  rotating CoC response team** (3–5 people, same rotation cadence the
  Chair's plan already uses for graduation outreach) — never a single
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
  out at once) rather than the Chair's monthly graduation-outreach
  cadence: CoC casework benefits from institutional memory of prior
  incidents/patterns in a way outreach emails don't, but the same
  anti-burnout, anti-capture logic still argues for guaranteed turnover.
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
- **Whole-team misconduct — resolved (2026-07-30).** Handled by the
  Board directly, not a newly-invented escalation body: the Board has
  standing access to the underlying case records with PII obfuscated
  (see Recordkeeping, below) — not just the quarterly aggregate counts —
  specifically so it can directly observe patterns or complaints about
  the team's own conduct, and act on its existing reserve authority over
  any PMC-adjacent body.
- **Still open:** appeal quorum is thin by construction on a 3–5 person
  team (if 2 acted, as few as 1 remain "uninvolved" to hear an appeal) —
  narrowing who's *on* the team doesn't fix this. Possible fix: route
  appeals to `wg-code-of-conduct` broadly if it's larger than the
  response team, or make VP D&I review the default rather than an
  alternative below some team size.

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
Quarterly aggregate counts (no case detail) reported out, matching the
Chair's plan's reporting rhythm. **Additionally (2026-07-30):** the Board
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

**Edge case, still unaddressed:** the current CoC's designated report
recipients (President, EVP, VP D&I) are themselves officer-level roles.
If one of them is the subject of a CoC complaint, the normal reporting
path is directly conflicted. Needs an explicit alternate path (e.g.
report to a different officer, or directly to the Board) — not
addressed anywhere in the current CoC or this draft yet.

## Layer 4 mechanics: ASF-Membership-level action (draft — deliberately
thin, enriched 2026-07-30 with existing-mechanism detail)

Scope: termination or involuntary emeritus conversion, locked to Bylaws
§4.7's two-thirds membership vote. Deliberately kept thin per the working
conclusion above — this doesn't invent new mechanics, it points at what
already exists.

**An analogous mechanism already runs today** (direct VP Legal
confirmation, 2026-07-30): the ASF already involuntarily converts members
to emeritus status after **2 years of inactivity**, believed (VP Legal's
own words: "I think") to require the same **two-thirds membership vote**
as any other §4.7 action. A CoC-driven involuntary emeritus conversion for
conduct reasons would piggyback on this same existing voting mechanism,
not invent a parallel one — consistent with the "reuse existing
processes" guardrail inferred from the Chair's strategic plan (see
below).

**Emeritus is not fully binary in practice:** emeritus status removes
membership rights, but reactivation happens **by the member's own
request** — softer than this doc previously assumed (a hard binary with
no described path back). Still unclear whether reactivation-by-request is
effectively automatic or itself requires an approval step; worth a direct
follow-up.

**Still fully open, pending further VP Legal review:** whether the Board
can delegate any part of this authority to a committee without a bylaws
amendment; whether 501(c)(3) status imposes a consistency/non-arbitrary-
enforcement obligation relevant here; whether a committee that only
documents-and-refers (never decides) raises any legal issue at all. See
"Questions for the VP Legal" below.

## Related: the Chair's own strategic plan retains a CoC working group

See [[comdev-2-year-strategic-plan]] — a ComDev strategic-plan draft
authored by the same ComDev PMC Chair this thread is with, which retains
a `wg-code-of-conduct` working group under its "governance reboot" of
ComDev working groups. Formal PMC adoption status is unconfirmed, and no
chair is currently known for that working group — but since the Chair
wrote the plan, that's a natural, easy thing to ask about directly, and
if the working group is live it's a more natural operational home for
turning this thread's layer-1/layer-2 mechanics into an actual proposal
than routing everything through the Chair informally.

## Potential guardrails, inferred from the Chair's own strategic plan (unconfirmed — validate directly)

The Chair hasn't stated explicit wishes or red lines for the CoC redraft
directly. In the absence of that, the following are inferred from
recurring design patterns in [[comdev-2-year-strategic-plan]] — the
Chair's own document — treated as **candidate guardrails to propose and
confirm**, not settled requirements:

- **No single-person dependency.** The plan explicitly diagnoses a prior
  ComDev initiative's collapse as caused by "single-person dependence,"
  and designs around it everywhere (graduation-email duty rotates across
  3–5 PMC members monthly; working-group ownership is distributed rather
  than centralized). Applied here: avoid concentrating CoC intake/response
  in one officer (today it's just the President/EVP/VP D&I) — prefer a
  small rotating group. This also happens to reduce the single-point
  burnout risk a real "committee with teeth" would otherwise create for
  whoever sits on it.
- **Named owner, clear deliverables, sunset/review clause — no indefinite
  standing bodies.** The plan's "governance reboot" requires this of every
  working group. Applied here: any CoC committee or process should have a
  named chair and a periodic review point (e.g., annual), not be chartered
  as permanent-and-unquestioned from day one.
- **Work inside the existing `wg-code-of-conduct` structure rather than
  inventing a new body.** The plan already retains this working group.
  Applied here: layer-1/layer-2 mechanics (see above) probably belong
  there rather than in a newly-invented committee — reinforces the
  cross-reference above.
- **No new budget outlay, volunteer-driven.** Every pillar in the plan is
  either $0 or modest and grant/event-specific; the Infrastructure &
  Tooling pillar explicitly leans on existing ASF Infra at no incremental
  cost. Applied here: prefer mechanics that reuse existing infra (mailing
  lists, existing officer roles, existing PMC processes) over anything
  implying new paid roles or tooling spend.
- **Concrete, templated, step-by-step process documents over principle
  statements.** The plan's graduation-outreach section is a literal
  numbered template, not a value statement — consistent with the Chair
  favoring exactly the kind of procedural specificity this whole CoC
  thread is trying to add. Weak evidence the Chair will be receptive to a
  templated "how" document, not just supportive of the goal in the
  abstract.
- **Defined reporting/review cadence.** The plan leans heavily on
  quarterly/monthly check-ins and board reporting rather than "set and
  forget" policy. Applied here: a CoC process revision might want a
  built-in periodic report (e.g., quarterly aggregate count of
  layer 1–3 actions taken, no case detail) rather than being silent on
  its own review cycle.

None of these are confirmed. Next real conversation with the Chair should
either validate or discard each one explicitly, rather than this list
quietly hardening into an assumed requirement.

## Open / unresolved — pick up here next

- **TOP PRIORITY — human judgment work still needed: severity rubric.**
  Still fully undrafted. Confirmed (2026-07-30) as still needed, not
  something to quietly drop — gates layer-1-vs-2 routing throughout this
  entire framework. Called out explicitly as the top item of remaining
  *human* (not legal, not mechanical) work.
- **Target: a proposal drawn from this doc is intended for submission at
  the ASF Board meeting on 2026-08-19** (confirmed 2026-07-30; confirmed
  to be the Board specifically, not just a ComDev PMC meeting).
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
  VP Legal), and the conflicted-reporting-path edge case when a report
  recipient is themself the subject.
- **New (2026-07-30): Layer 4 enriched, still thin by design** — an
  existing 2-year-inactivity involuntary-emeritus mechanism (believed
  two-thirds vote) is now documented as a procedural anchor, and emeritus
  status is confirmed reversible by the member's own request. Still fully
  open: bylaws delegation authority (Q4), 501(c)(3) consistency
  obligations (Q7), and whether a document-and-refer committee raises any
  legal issue at all (Q8) — see the new "Legal TODO" section below.
- **Adoption/publication mechanics documented; decision owner confirmed
  (2026-07-30).** Path A vs. Path B is not the author's call alone — **the
  ComDev Chair and the new VP Legal will jointly pick a path and sign
  off.** See "Adoption / publication mechanics" above and "Legal TODO"
  below.
- Interdependencies between layers, identified while drafting layer 2,
  still need resolving: the evidence-handoff format between layer 1's
  minimal log and a fuller layer-2/3 case file; the cross-project
  notification protocol when the layer-1 rotating team refers a pattern
  to a specific PMC; what happens if a PMC declines to act on a
  substantiated layer-2 referral.
- Rotating-team appointment/accountability drafted (2026-07-30) — see
  "Team composition, selection, and accountability" under Layer 1
  mechanics. **Reality check added (2026-07-30):** the nomination-based
  model is the target, but the team will likely start as a self-selected,
  ad hoc group of volunteers for a while in practice — the quantifiable,
  checkable-fact discipline in the triggers and two-person sign-off is
  the safeguard that holds regardless of how cleanly the team itself got
  seated. **Whole-team misconduct — resolved (2026-07-30):** handled by
  the Board directly via standing Board access to case records with PII
  obfuscated (not just quarterly aggregate counts) — no new escalation
  body needed. **Still open:** appeal quorum on a small team (if 2 acted,
  as few as 1 remain "uninvolved" to hear an appeal) — possible fix:
  route appeals to `wg-code-of-conduct` broadly if larger than the
  response team, or make VP D&I review the default below some team size.
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
  policy draft) and [[comdev-code-of-conduct-board-resolutions]] (draft
  Board resolutions for Path A and Path B). This working doc remains the
  fuller design-history record behind those artifacts.

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
   **Answer: still needs review** — not yet answered.
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
   **Answer: still needs review** — not yet answered.
8. Does a committee that only *documents a case and refers it* to a
   membership vote (never deciding anything itself) raise any legal issue
   at all, or is that clearly safe under current bylaws?
   **Answer: unclear at this point, needs further review** — not yet
   answered.
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

**Still outstanding, needs a follow-up conversation:** Q4, Q7, and Q8 —
all three gate how much Layer 4 (and possibly the document-and-refer
framing generally) can honestly claim. Worth prioritizing before
finalizing that language, not after.

## Legal TODO — concrete checklist for the VP Legal conversation

Consolidated, actionable version of what's still needed from Legal,
requested explicitly (2026-07-30) rather than leaving it scattered across
the Q&A above:

1. **Answer Q4** — can the Board delegate §4.7-adjacent authority to a
   committee by ordinary resolution, or does it require a bylaws
   amendment (and if so, Board-only or full membership vote)?
2. **Answer Q7** — does 501(c)(3) status impose a
   consistency/non-arbitrary-enforcement obligation relevant here?
3. **Answer Q8** — does a committee that only documents-and-refers (never
   decides) raise any legal issue at all?
4. **Review both draft Board resolutions** in
   [[comdev-code-of-conduct-board-resolutions]] — neither has been
   legal-reviewed; both are modeled on typical phrasing, not confirmed
   correct.
5. **Jointly pick Path A or Path B** with the ComDev Chair, and sign off —
   confirmed (2026-07-30) this is not the author's decision to make
   alone.
