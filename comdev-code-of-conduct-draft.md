---
title: ASF Code of Conduct — enforcement framework (ComDev draft proposal)
compiled: 2026-07-30
status: draft — not yet adopted; not the Board's 2026-08-19 submission vehicle (see 2026-07-31 update below)
source: derived from comdev-code-of-conduct-revision.md
---

# ASF Code of Conduct — Enforcement Framework (Draft)

**Status:** this is ComDev's proposed addition to the existing ASF Code of
Conduct, prepared at the Board's direction that ComDev provide input into
the Board-owned CoC revision effort. It is not yet adopted. Targeted for
the ASF Board meeting on 2026-08-19. The Board retains ownership of this
policy; the ComDev Chair and VP Legal will jointly decide, and sign off
on, how it becomes official — either by the Board directly adopting this
text, or by directing the President to adopt and publish it under
existing presidential authority. Sections marked **[OPEN]** are not yet
resolved and should not be read as ComDev's final position on those
points.

**Update (2026-07-31):** the ComDev PMC Chair's actual resolution for the
2026-08-19 Board meeting instead proposes adopting a separate,
pre-existing document as the complete, replacement Code of Conduct text
(Exhibit A) — the cwiki "Apache Software Foundation Code of Conduct Draft
WIP," a Contributor Covenant v2.1 adaptation last revised 2025-09-09,
referred to elsewhere in this KB as "the September 2025 wiki draft" and
internally as v13. That document supersedes the existing CoC outright
rather than adding procedure to it, which is this framework's approach.
This framework is **not** currently the Board's submission vehicle. Its
most concrete near-term use is as the source of already-completed legal
research now applied directly against the cwiki draft in
[[comdev-coc-v13-proposed-changes]]; longer-term, the layer 1–4 mechanics
below remain a candidate for a companion "Enforcement Procedures"
document if the Board wants more operational detail than v13's ladder
provides on its own (see that file's "Structural suggestion" section).

---

## 1. Purpose

The Code of Conduct's existing principles and prohibited-conduct list
(below) describe *what* is expected of ASF participants. They do not
describe *how* a violation is investigated, who has authority to act, or
what happens next. This framework adds that missing procedure. It does
not change the values or prohibited-conduct list themselves.

## 2. Principles (carried forward, unchanged in substance)

Be open. Be empathetic and welcoming. Be collaborative. Be inquisitive.
Be careful with words. Be concise. Step down considerately. These are
the current Code of Conduct's seven principles, carried forward verbatim
into this document. Upon adoption, this document is the complete, sole
Code of Conduct text — it replaces the currently published version
rather than sitting alongside it as a separate add-on; nothing here
implies two co-existing documents.

## 3. Prohibited conduct (carried forward, unchanged in substance)

The current Code of Conduct's list of prohibited conduct — including
threats, discriminatory language, doxing, sexual harassment, and
personal insults — is carried forward verbatim. This framework changes
how a violation is investigated and enforced, not what counts as one.

**Conduct, not positions:** criticism of ASF decisions, policies,
project direction, or leadership is not itself a violation, however
sharply expressed within the principles above. Personal attacks,
harassment, or other prohibited conduct remain violations regardless of
the governance or technical disagreement they are wrapped in. This cuts
both ways: it cannot be used to silence dissent, and dissent cannot be
used to shield genuine misconduct.

## 4. Scope of enforcement

Enforcement actions are organized into four levels, distinguished by
what kind of authority is being exercised and who ultimately holds it:

| Level | What it covers | Who decides |
|---|---|---|
| 1. Space/access-level | Muting, event removal, temporary restriction from a list/channel/tool | A rotating CoC response team, operating within existing officer/committee discretion |
| 2. Project-role-level | Committer/PMC-member status, commit karma | The hosting PMC, by its own consensus vote — this framework can require the PMC to take up a matter, never decide it |
| 3. Officer-level | PMC chair or other Board-appointed officer titles | The Board |
| 4. ASF-Membership-level | Termination, involuntary emeritus conversion | The ASF membership, by two-thirds vote under Bylaws §4.7 |

Levels 1 and 2 require no legal dependency and can move independent of
anything below; officer- and membership-level actions are bound by
existing Bylaws mechanics this framework does not attempt to change.

**Scope of applicability — what spaces and conduct this reaches:**
ASF-managed spaces, plus conduct anywhere while representing the ASF.
Conduct in other spaces that is directed at an ASF project, community, or
participant may also be in scope. This framework does not claim
jurisdiction over participants' conduct in unaffiliated spaces generally
— it can only action ASF's own spaces, roles, events, and membership
status. **[OPEN]** whether a harm-triggered, case-by-case admissibility
test for edge cases (e.g., safety impact from an off-platform incident)
belongs in the enforcement procedures.

## 5. Reporting

**Before reporting:** ASF norms already expect good-faith assumptions,
and pointing a participant to this Code of Conduct directly is a
reasonable first response to a minor, one-off lapse. The channels below
are for when that doesn't resolve the concern, or the conduct doesn't
warrant an informal approach. A concern about specific documentation or
code content (e.g., inappropriate wording in a comment or doc) may go
through a project's normal review process instead of the CoC report
path, unless the conduct itself — not just the content — is what's at
issue.

Reports may go to a project's existing `private@` list, or to a new
`coc@` alias monitored by the rotating response team (Section 6.2).
Reports are acknowledged within 3 business days.

**Conflicted-recipient exception:** if the subject of a report is one of
the Code of Conduct's designated recipients (President, EVP, VP D&I),
the report should instead go directly to the Board (board@, or a
designated non-conflicted director) — the only body with authority over
those roles.

## 6. Layer 1: space/access-level actions

### 6.1 Escalation ladder

1. Informal private note — no formal record; first-line response to a
   one-off lapse.
2. Documented written warning.
3. Temporary moderation of one space (posts held for review), fixed
   window.
4. Temporary full restriction from one space, fixed duration.
5. Removal from a specific event.
6. Cross-space restriction — reserved for repeated or severe conduct.
7. Revocation of a non-merit tool privilege.

Steps 1–3 remain with whoever already holds that authority today (list
moderators, PMC members) — no escalation required. Step 4 and above
requires sign-off from two members of the rotating response team
(Section 6.2); never a single officer acting alone.

**Emergency exception:** for an active, ongoing safety situation, one
person may act immediately; the action must go to the full response
team for confirm/reverse/extend within 48–72 hours.

**Disposition — No Action:** a report investigated and found not to
constitute a violation closes with an explicit "No Action" disposition,
not silence. It is recorded with a closure reason — insufficient
evidence to conclude either way, or affirmatively found not a violation
— since the reporter-pattern flag (Section 6.3) depends on
distinguishing these. Both parties are notified of the outcome
(categorically, not narratively, mirroring interim-measure notice in
Section 6.3). No Action dispositions are included in the quarterly
aggregate counts (Section 6.4) alongside sanctioned outcomes, so the
aggregate reflects total caseload handled, not just actions taken.

**Appeal (final actions):** any step 2+ ladder action may be appealed
within 14 days of notice. Review is conducted by response-team members
not involved in the original decision, or by the Board-level backstop
group (Section 6.2) when fewer than two remain uninvolved. The action
stays in effect pending appeal unless the reviewers grant a stay. A
reversed action is lifted immediately and the log entry (Section 6.4) is
annotated to reflect the reversal, not silently corrected.

### 6.2 The rotating response team

A team of 3–5 people handles layer-1 sign-off and, where applicable,
layer-2 referral support. Starts at 3 seats, growing toward 5 as
volunteer capacity allows.

- **Selection is by nomination, not self-application.** Candidates are
  proposed by existing team members, `wg-code-of-conduct`, or the
  ComDev PMC — not by raising a hand. A self-nomination requires an
  existing PMC member to second it.
- **Confirmation and removal-for-cause both run by standard ASF lazy
  consensus:** posted to `wg-code-of-conduct`, stands unless a PMC
  member objects within 72 hours. This is deliberately the same
  lightweight mechanism ComDev decisions already use, not a heavier
  invented formal vote — the real safeguard against a bad seating is
  the checkable-fact triggers and two-person sign-off governing actual
  casework (Section 6.3), not the seating formality itself. A member
  facing a removal-for-cause proposal is recused from active casework
  for its duration; no-fault exit (below) remains available at any time
  in lieu of going through this.
- **Terms are 1 year**, coinciding with the team's own annual review
  point below rather than running on a separate clock. Renewal uses the
  same lazy-consensus mechanism as initial seating — a member continues
  unless a PMC member objects at the review point — so continuity in
  practice rests on that lazy-consensus inertia rather than a forced
  multi-year term or separate per-seat staggering.
- **Stepping down is always available, without stigma or process.**
- **The team does not renew or review itself.** Its continuation, and
  each member's 1-year term, is reviewed annually by the Board (or, for
  anything touching §4.7-adjacent territory, the membership). The team
  is expected to formalize to the nomination model above no later than
  this first annual review point, sooner if seats fill informally before
  then.
- **Transition note:** in practice, this team is expected to begin as a
  self-selected group of volunteers for a period before the
  nomination-based model above is fully in place. The trigger criteria
  and two-person sign-off in Section 6.3 apply regardless of how the
  team was seated, and are the actual safeguard against misuse during
  that transition.
- **Whole-team misconduct:** the Board's standing access to
  PII-obfuscated case records (Section 6.4) pairs with the power to act
  on what it sees — the Board can initiate the same lazy-consensus
  removal-for-cause mechanism against a team member directly, or in
  extremis vote to dissolve and reconstitute the team, under its
  ordinary existing oversight authority. No new authority is invented;
  not a separately invented escalation body.
- **Per-case recusal:** a team member with a personal tie to the
  reporter or the subject in a given matter recuses from sign-off on
  that case, mirroring the Layer 2 PMC-recusal norm (Section 7). If
  recusal leaves fewer than two available signers for a step 4+ action,
  the second signer is drawn from the Board-level backstop group
  (below).
- **Appeal quorum:** the primary reviewers are whichever response-team
  members were not involved in the original decision. When that leaves
  fewer than 2 uninvolved members, the appeal routes instead to a small
  **standing Board-level backstop group** (2–3 Board-designated
  members, rotating at the Board's own discretion) rather than
  concentrating repeat appellate load on one volunteer officer. This
  group draws on the Board's already-established standing case-record
  access (Section 6.4), so it needs no separate onboarding or
  disclosure step per appeal.

### 6.3 Interim measures

A provisional, non-punitive hold may be applied during an open
investigation, before notice-and-response is complete. It is not a
sanction and must not be presented as one.

**Triggers** (any one is sufficient; each is a checkable fact, not a
severity judgment):
1. Reporter and subject share a space, and the subject holds
   moderator/access authority over the reporter there.
2. The complaint concerns the subject's use of a privileged tool.
3. The conduct is verifiably still ongoing.
4. The subject has a prior interim measure or sanction on file within a
   defined window. **[OPEN — window not yet set.]**
5. The reporter has stated they will not continue participating while
   the subject retains access.

Authorization requires two-person sign-off, same as ladder step 4+ — no
single-person track beyond the emergency exception. Scope is limited to
same-space moderation or access-hold (ladder steps 3–4) only. Duration
is capped (proposed: 7 days), auto-expiring unless affirmatively
renewed, and lifted immediately if the matter resolves without
sanction. Notice is categorical, not narrative, and delivered
immediately. Appeal may be requested on an expedited basis (proposed:
72 hours).

**Reporter confidentiality:** a reporter's identity is shared only as
needed within the response team and, at referral, the minimum necessary
to the receiving PMC or officer (Section 7) — never disclosed to the
subject without the reporter's consent, absent a legal requirement to
do so.

**Bad-faith reporting is itself a violation:** a knowingly false or
malicious complaint is prohibited conduct under this framework, stated
here as a rule rather than left to the statistical pattern-flag below.
It is handled through this same process against the reporter,
independent of that pattern-flag.

**Reporting-system integrity:** because trigger 5 is self-attested, a
pattern of a single reporter's complaints repeatedly resulting in no
final sanction is tracked as a flag for human review — it never
triggers an action on its own, and a first-time use of trigger 5 is
never treated with added suspicion. **[OPEN — flagged as needing real
privacy/security review before implementation:]** any system that
tracks reports by reporter identity is itself a sensitive dataset
requiring access controls beyond an ordinary case log, and raises a
tension with anonymous reporting that has not yet been resolved.

### 6.4 Recordkeeping and reporting

Minimal, private logging: date, space, action, duration, category — not
full narrative — visible only to the response team and relevant
officers. Interim measures are logged distinctly from final ladder
actions. Quarterly aggregate counts, with no case detail, are reported
out. The Board additionally has standing access to the underlying case
records with PII obfuscated, so it can directly observe patterns or
complaints about the response team's own conduct.

## 7. Layer 2: project-role-level actions

Scope: committer/PMC-member status and commit karma within a hosting
PMC. Excludes PMC chair (Layer 3) and ASF Membership (Layer 4).

**This framework does not execute layer-2 actions.** It can require a
PMC to take up a substantiated matter and respond within a defined
window (proposed: 30 days) — it cannot compel a specific outcome. The
PMC's own consensus vote governs entirely.

A single severe incident may be referred directly to layer 2 without
first exhausting the layer-1 ladder. **[OPEN — criteria for "severe
enough to refer directly" not yet defined.]**

Any PMC member with a personal tie to the matter should recuse from
that PMC's vote.

**[OPEN]** the evidence-handoff format between layer-1's minimal log and
a fuller case file for PMC review; the notification protocol when a
pattern spans multiple projects; and what happens if a PMC declines to
act on a substantiated referral, are all undefined.

## 8. Layer 3: officer-level actions

Scope: PMC chair and other Board-appointed officer titles.

**Chair removal:** a PMC vote to remove its own chair requires separate,
explicit Board action to take effect. This is handled as part of the
Board's ordinary monthly business, not as an exceptional process.

Removal authority for any other Board-appointed officer (President, EVP,
VP D&I, VP Legal) already exists and is unconstrained: Bylaws §6.5 lets
the Board remove such an officer whenever it judges the org's best
interests served, no cause or process required. **[OPEN]** what's missing
is only the *path* from a complaint to the Board's agenda — who receives
it, who compiles the record, how it's calendared — not new authority.

## 9. Layer 4: ASF-Membership-level action

Scope: termination or involuntary emeritus conversion under Bylaws
§4.7, which requires a two-thirds membership vote. This framework does
not change that requirement. The most any body under this framework can
do is document a case and refer it to the membership.

A comparable mechanism already governs involuntary emeritus conversion
for long-term inactivity (confirmed practice: roughly five years,
through a members' vote) — any conduct-based conversion under this
framework would use that same voting mechanism, not a new one, though
the existing practice's purpose is quorum management, not conduct, so
this is an extension of that practice rather than a direct precedent for
it. Emeritus reactivation is not automatic: it requires the member's own
written request, a new membership application, and an affirmative
majority vote of the members.

Delegating any part of §4.7 authority to a committee is legally reachable
only through a Board bylaws amendment (not an ordinary resolution) and is
not recommended — it would strip the membership's own protection and
could simply be re-amended back. A document-and-refer committee that
never decides or binds raises no legal issue under DGCL §141(c). 501(c)(3)
status imposes no relevant obligation here. **[OPEN]** the conduct-action
log's discoverability, defamation, retention, and (for participants
outside the US) GDPR exposure has not been assessed against this
framework's recordkeeping design (Sections 6.4, 9) yet.

## 10. Governance of this framework

Two distinct reviews run on the same annual cadence but by different
bodies, and should not be conflated: the response **team's** own
continuation and membership is reviewed by the Board (Section 6.2). This
**framework's** operational mechanics (the ladder, triggers, recordkeeping,
etc.) are reviewed annually by `wg-code-of-conduct`, which may propose
amendments. Because this is a foundation-wide policy, formally amending
it beyond operational refinement requires Board (or, if adopted via
Path B, presidential) sign-off — `wg-code-of-conduct` alone cannot
amend the adopted policy text. It is not self-renewing.

## 11. Known gaps — not yet resolved

This framework is offered as ComDev's input, not a finished product. The
following are explicitly not settled, and should not be read into any
silence elsewhere in this document:

- **Severity rubric for routing between layers — top-priority remaining
  human-judgment work**, not a mechanical or legal gap. The base CoC's
  own Community Impact tier language (if it has one) may be a usable
  seed rather than starting from nothing.
- **A path to permanent exclusion for role-less participants.** Layer 2
  requires an existing PMC role, Layer 3 an officer title, Layer 4 ASF
  membership — a participant with none of those (e.g. a drive-by
  harasser with no project role) can only ever receive Layer 1's
  deliberately temporary measures. Needs either a new permanent-exclusion
  step with a named decider and appeal, or an explicit statement of who
  outside this framework holds that power.
- **Content-level actions.** The ladder restricts what a *person* can do
  (muting, access removal) but says nothing about removing the
  *offending content itself* — a harassing post, a slur in a commit
  message, doxxing on a wiki page. Who has authority to remove it, and
  how that action is logged, is undefined.
- **Person-based (cross-space) measures.** Every ladder measure attaches
  to a space ("muted on list X"); there is no "no contact with a named
  individual" condition that follows its target across spaces. Would
  likely need to be enforced indirectly — breach treated as new
  misconduct that escalates — rather than actively monitored.
- **The President's role once the rotating team is operational.** The
  published CoC currently routes reports to President/EVP/VP D&I; this
  framework substitutes the `coc@` alias and rotating team without
  saying what, if anything, the President's role becomes for routine
  (non-conflicted) reports.
- Non-chair officer removal *referral path* (Section 8) — authority
  itself is confirmed to already exist (Bylaws §6.5).
- Reporter-attribution privacy/security review, including an open GDPR
  question (Section 6.3).
- Conduct-action log discoverability/defamation/retention/GDPR exposure
  (Section 9).
- Off-platform / social-media scope — a harm-triggered admissibility test
  for edge cases still needs drafting (Section 4).
- Which adoption path the Board will use to make this official.
