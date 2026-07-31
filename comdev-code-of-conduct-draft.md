---
title: ASF Code of Conduct — enforcement framework (ComDev draft proposal)
compiled: 2026-07-30
status: draft — ComDev input prepared for Board consideration; not yet adopted
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

---

## 1. Purpose

The Code of Conduct's existing principles and prohibited-conduct list
(below) describe *what* is expected of ASF participants. They do not
describe *how* a violation is investigated, who has authority to act, or
what happens next. This framework adds that missing procedure. It does
not change the values or prohibited-conduct list themselves.

## 2. Principles (unchanged)

Be open. Be empathetic and welcoming. Be collaborative. Be inquisitive.
Be careful with words. Be concise. Step down considerately. These
principles remain as stated in the current Code of Conduct.

## 3. Prohibited conduct (unchanged)

The current Code of Conduct's list of prohibited conduct — including
threats, discriminatory language, doxing, sexual harassment, and
personal insults — remains in force and is not modified by this
framework.

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

## 5. Reporting

Reports may go to a project's existing `private@` list, or to a new
`coc@` alias monitored by the rotating response team (Section 6.2).
Reports are acknowledged within 3 business days.

**Conflicted-recipient exception:** if the subject of a report is one of
the Code of Conduct's designated recipients (President, EVP, VP D&I),
the report should instead go to an alternate officer, or directly to the
Board. **[OPEN — no alternate path defined yet.]**

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

### 6.2 The rotating response team

A team of 3–5 people handles layer-1 sign-off and, where applicable,
layer-2 referral support.

- **Selection is by nomination, not self-application.** Candidates are
  proposed by existing team members, `wg-code-of-conduct`, or the
  ComDev PMC — not by raising a hand. A self-nomination requires an
  existing PMC member to second it.
- **Terms are staggered**, not all rotating out simultaneously, to
  preserve case continuity while guaranteeing turnover.
- **Stepping down is always available, without stigma or process.**
- **Removal for cause** uses the same nomination/consensus mechanism
  that seated the member.
- **The team does not renew or review itself.** Its continuation is
  reviewed annually by the Board (or, for anything touching
  §4.7-adjacent territory, the membership).
- **Transition note:** in practice, this team is expected to begin as a
  self-selected group of volunteers for a period before the
  nomination-based model above is fully in place. The trigger criteria
  and two-person sign-off in Section 6.3 apply regardless of how the
  team was seated, and are the actual safeguard against misuse during
  that transition.
- **Whole-team misconduct** is addressed through standing Board access
  to case records with PII obfuscated (Section 6.4) — not a separately
  invented escalation body.
- **[OPEN]** Appeal quorum on a small team is not yet resolved.

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

**[OPEN]** equivalent mechanics for removing any other Board-appointed
officer (President, EVP, VP D&I, VP Legal) are not yet defined.

## 9. Layer 4: ASF-Membership-level action

Scope: termination or involuntary emeritus conversion under Bylaws
§4.7, which requires a two-thirds membership vote. This framework does
not change that requirement. The most any body under this framework can
do is document a case and refer it to the membership.

An existing, comparable mechanism already governs involuntary emeritus
conversion for inactivity (two years without activity, believed to
require the same two-thirds vote) — any conduct-based conversion under
this framework would use that same voting mechanism, not a new one.
Emeritus status is reversible by the member's own request.

**[OPEN, pending legal review:]** whether the Board can delegate any
part of this authority to a committee without a bylaws amendment;
whether 501(c)(3) status imposes a consistency/non-arbitrary-enforcement
obligation; whether a document-and-refer committee raises any legal
issue at all.

## 10. Governance of this framework

This framework is reviewed annually by the body designated in Section
6.2 and may be amended at that point. It is not self-renewing.

## 11. Known gaps — not yet resolved

This framework is offered as ComDev's input, not a finished product. The
following are explicitly not settled, and should not be read into any
silence elsewhere in this document:

- **Severity rubric for routing between layers — top-priority remaining
  human-judgment work**, not a mechanical or legal gap.
- Non-chair officer removal mechanics (Section 8).
- Conflicted-reporting-path alternate recipient (Section 5).
- Appeal quorum on a small response team (Section 6.2).
- Reporter-attribution privacy/security review (Section 6.3).
- Bylaws delegation authority, 501(c)(3) obligations, and the legal
  standing of a document-and-refer committee (Section 9).
- Which adoption path the Board will use to make this official.
