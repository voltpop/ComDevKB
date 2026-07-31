---
title: External gap review of the CoC enforcement draft
compiled: 2026-07-31
status: received and triaged — most items resolved same-day; see [[comdev-code-of-conduct-revision]]
source: received as an unformatted plain-text message (a flat list of dashed
  points, no headers or markdown); reformatted here into a numbered list for
  the KB, content otherwise unchanged from the original
---

# External gap review of the CoC enforcement draft

Feedback on [[comdev-code-of-conduct-draft]] from a reviewer with legal
context, sent directly rather than through the outside-counsel track. The
reviewer noted they weren't sure how the draft itself was generated, and
that their own separate CoC draft covers some of the same gaps.

1. **A "No Action" disposition** — no defined outcome for a report
   assessed and found not to be a violation: no closure-reason recording
   (insufficient-evidence vs. unfounded — which the framework's own
   reporter-pattern flag depends on), no notification to the parties, no
   place in the quarterly aggregates.
2. **A scope-of-application section** — §4 scopes authority; nothing
   says where the CoC applies (spaces, events, representing the ASF).
3. **An appeal path for final actions** — interim measures get a
   72-hour expedited appeal and the appeal-quorum [OPEN] presumes
   appeals exist, but no section defines the standard appeal: window,
   who reviews, effect.
4. **Per-case recusal** — the response team has removal-for-cause but
   no rule that a member recuses from a case they're personally
   connected to.
5. **Severity/routing criteria** — flagged [OPEN] by the doc itself; the
   Community Impact tier descriptions in the base CoC draft are a
   ready-made seed.
6. **Content-level actions** — the ladder restricts what a person can
   do, but nothing addresses offending content itself (a harassing
   post, a slur in a commit message, doxxing on a wiki page); who
   removes it, and how that's logged.
7. **Person-based measures** — every measure attaches to a space
   ("muted on list X"); there's no "no contact with A" condition for
   harassment that follows its target across spaces, enforced
   indirectly (breach = new misconduct that escalates).
8. **A path to permanent exclusion for role-less participants** — Layer
   2 requires a PMC role, Layer 3 an officer title, Layer 4 ASF
   membership; a drive-by harasser with none of these can only ever
   receive Layer 1's deliberately temporary measures. Add a permanent
   step with a named decider and appeal, or state who outside the
   framework holds that power.
9. **A conduct-not-positions clarification** — one line: criticism of
   decisions, policies, or leadership is never itself a violation, and
   personal attacks or harassment remain violations regardless of the
   governance context they're dressed in. Cuts both ways: can't be used
   to silence dissent, can't be hidden behind.
10. **Informal-resolution norms** — assume good faith, pointing out the
    CoC yourself as the expected first response, the docs/code-content
    reporting route.
11. **Reporter-side provisions** — an explicit confidentiality
    commitment to reporters, and "knowingly false or malicious
    complaints are themselves a violation" stated as a rule, not left
    to the quiet pattern-flag.
12. **Base-text assumption** — §§2–3 declare the current CoC's
    principles and prohibited-conduct list "unchanged," but the
    framework replaces that document.
13. **The President is absent from the operational path** — the
    published CoC routes foundation-wide reports to President/EVP; the
    framework substitutes the rotating team without saying what the
    President's role becomes.
14. **§10 ambiguity** — "reviewed annually by the body designated in
    Section 6.2" doesn't resolve to a body (6.2 designates the Board as
    the team's reviewer, not the framework's).

## Triage and resolution

Items 2 was already resolved before this review landed (Section 4's
scope-of-application language, added the same day). Items 1, 3, 4, 9,
10, 11, 12, and 14 were fixed same-day as clear-default, low-risk
additions/corrections. Items 6, 7, 8, and 13 remain open as genuine
judgment calls needing further design or Board/Infra input, not bugs.
Full triage detail: "External gap review of the draft policy text
(2026-07-31)" in [[comdev-code-of-conduct-revision]].
