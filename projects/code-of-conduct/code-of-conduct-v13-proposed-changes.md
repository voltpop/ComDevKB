---
title: Proposed changes to the cwiki Code of Conduct draft (v13) before Board submission
compiled: 2026-07-31
status: draft — proposed edits, not yet raised with the wiki page's author or the Chair
source: reviewed against the actual v13 page text (last updated Sep 09 2025), pasted into conversation 2026-07-31
---

# Proposed changes to the cwiki CoC draft (v13)

## Framing

The Chair's resolution asks the Board to adopt this cwiki page (Exhibit A)
as the complete, replacement ASF Code of Conduct — a different move from
[[code-of-conduct-enforcement-draft]]'s approach of adding enforcement
procedure to the *existing* CoC's principles. These are surgical
proposed edits to v13 itself, on the working assumption that v13, not the
ComDev four-layer framework, is what actually goes to the Board on
2026-08-19. The goal is grounded, low-risk changes that reuse research
already done — not grafting the full ComDev design onto this page.

`Qn` below refers to a numbered question in
[[code-of-conduct-legal-questions-and-briefs]]; `item N` refers to a numbered
finding in [[code-of-conduct-external-gap-review]].

## Already solid — no change proposed

- **Recusal section.** Matches the design already worked through for the
  ComDev framework — conflict-of-interest handling and delegation to
  uninvolved parties is there and reads cleanly.
- **"No Action" disposition + frivolous/malicious-complaint clause.**
  Both already present — the page's own comment history shows they were
  added directly in response to a reviewer's "this reads as guilty until
  proven innocent" concern. This independently resolves gap-review item 1.
- **The five-tier Community-Impact-per-level language is a usable severity
  rubric on its own.** [[code-of-conduct]] flags a
  severity/routing rubric as the single top-priority remaining
  human-judgment item; v13 already has a working version of exactly that.
  That item can be closed against this text rather than drafted from
  scratch.
- **The ASF-Membership footnote** (Bylaw 4.7 vote required to terminate;
  a PMC/officer can only recommend temporary exclusion pending that vote)
  matches the document-and-refer conclusion from Q1/Q2 exactly.
- **The no-contact language in the Warning/Temporary Ban tiers** ("No
  interaction with the people involved... including avoiding community
  spaces and external channels like social media") already gives a
  cross-space "no contact" condition (gap-review item 7), correctly
  framed as a self-executing condition whose breach escalates — exactly
  the fix pattern Q11 recommends, not an actively-monitored measure.
- **The ladder restricts "public interaction with the community," not a
  specific role tier.** Because bans here aren't scoped to
  PMC-role/officer-title/ASF-membership status, v13 sidesteps what the
  ComDev framework had flagged as its single most structurally
  significant gap — a path to permanently excluding a participant who
  holds no formal role at all (gap-review item 8). Worth naming this
  explicitly as resolved-by-a-different-design, not left open. (One real
  gap remains underneath it, though — see proposed change 6 below on who
  actually executes a ban against a role-less participant.)

## Proposed changes, grounded in already-completed research

### 1. Narrow the Scope section — high priority

Current text: *"applies to all ASF projects, mailing lists, source code
repositories, issue trackers, events, chat services and community
spaces, whether official or unofficial, and also applies when
individuals are representing ASF..."*

Q11 finding: "official or unofficial" blanket scope is broader than
every surveyed peer CoC — Contributor Covenant, Linux kernel, Debian,
Rust all reach only their own venues; CNCF reaches external spaces only
when conduct is "directed at" a project/community/participant; PSF
enumerates its own spaces and keeps a harm-triggered case-by-case test in
its enforcement *procedures*, not its scope section. Undefined blanket
scope is the specific defect behind both the rare successful legal
challenges to association discipline and real community blowups (OpalGate
2015, Drupal/Garfield 2017, Linux kernel 2018) — risk here is political
and reputational as much as legal.

Proposed: drop "unofficial" as a scope category. Keep ASF-managed spaces
+ "representing the ASF" (the CC 2.1 baseline this document already
uses); add a CNCF-style clause reaching cross-platform harassment
"directed at" an ASF project/community/participant; move any broader
harm-triggered admissibility test ("if the incident occurred outside the
community, but a participant's safety may be affected, it may be in
scope") into the enforcement guidelines rather than the scope section.

### 2. Name the Board as the conflicted-recipient fallback — high priority

The Recusal section requires recusal but doesn't say where a report goes
when the conflicted party is one of the policy's own named recipients
(President, EVP, a designated volunteer).

Q9 finding: the Board is the only body with authority over the
President/EVP (bylaws §§6.2, 6.4, 6.5) — reporting directly to the Board
(board@apache.org, or a designated non-conflicted director) is the
structurally correct fallback, not just a reasonable one, and needs no
bylaws change.

Proposed addition (Recusal or Reporting Guidelines): *"If the subject of
a report is the President, the EVP, or another designated recipient
under this policy, the report should instead be sent directly to the
Board (board@apache.org) or a designated non-conflicted director."*

### 3. Don't route Foundation-wide backstop authority through one officer — high priority

Current text: *"the ASF President (or their designee) may investigate
and take appropriate action, or escalate to the ASF Board or an ASF
Officer if necessary."* A single named office carries the entire
cross-project/Foundation-wide backstop.

This is the one place v13 reintroduces the single-point-of-failure
problem the parallel ComDev design work was built specifically to avoid
— a single named officer, even a real willing one, was rejected as a
standing backstop in favor of a small 2–3 person group, precisely
because concentration is itself a risk regardless of who holds the
office.

Proposed: name a small Board-designated group (2–3 people) that the
President's office works alongside, or refers to, for Foundation-wide
matters — not sole discretion resting with one office. Doesn't need to
be elaborate; even one sentence naming a second reviewer removes the
single-person dependency.

### 4. Add a minimal appeal mechanism — medium-high priority

Gap-review item 3: no appeal path is defined anywhere in the current
enforcement process, for any ladder action.

Proposed: a short, fixed window (e.g. 14 days) to request review of a
Correction-or-above action, by someone not involved in the original
decision (falling back to the Board-level group in change 3 above when
too few uninvolved reviewers exist). Action stays in effect during
appeal absent an explicit stay.

### 5. Add a "conduct, not positions" clarification — medium priority

Gap-review item 9, not present anywhere in v13: one sentence stating
that criticism of ASF decisions, policy, or leadership is not itself a
violation, however sharply expressed, while personal attacks or
harassment remain violations regardless of the disagreement they're
wrapped in. Cuts both ways — protects dissent without shielding
misconduct behind it.

### 6. Fix the dangling contact references — medium priority (already flagged on the page itself)

Two of the page's own review comments independently raised this months
ago: (a) only the President has a stable email alias today
(president@apache.org) — the EVP and "designated volunteers" don't,
making the reference fragile across officer transitions; (b) "ASF's
designated volunteers" links to nothing — there's no actual roster.
Separately, this is also where the "role-less participant" gap actually
still bites (see the note in "Already solid" above): even though the
ladder's authority isn't role-gated, nothing says *who* executes a
permanent ban against someone with no PMC/committer/member status to
revoke — no Infra path is named.

Proposed: stand up a `coc@`-style alias (treated as a trivial,
non-blocking Infra ask in [[code-of-conduct]]), add or
link an actual roster for "designated volunteers," and name who holds
execution authority for actions against a participant with no existing
role (Infra? the President's office directly?).

### 7. Broaden the membership footnote beyond termination — low priority

Current footnote names only Bylaw 4.7 (termination). Q5/Q6 confirm
involuntary emeritus conversion (§4.4) is a separate, real,
lower-severity bylaws mechanism (also a two-thirds member vote) that
could serve as an intermediate consequence short of full termination.
Proposed: broaden the footnote to cover any change to ASF Membership
status, or name both §4.4 and §4.7 explicitly.

## Structural suggestion, not a text edit

Consider keeping this page scoped to what a Board vote should actually
cover — principles, ladder, scope, top-level responsibilities — and
moving deeper operational mechanics (interim/precautionary measures,
response-team composition and rotation, recordkeeping, cross-project
referral protocol — all substantially drafted already in
[[code-of-conduct]]) into a separate companion
"Enforcement Procedures" document, PSF-style. This keeps the Board's
actual vote scoped to something short enough to pass cleanly, while the
resolution's own "President may amend... substantive changes reported to
the Board" language gives that companion document room to evolve without
a fresh Board resolution every time.

## Out of scope for this file

- The retroactivity/"clean slate" clause described in the Chair's FAQ
  doesn't appear anywhere in the actual v13 text — it would need to be
  added either to the resolution's RESOLVED clauses or to this page
  directly if it's meant to be binding, not just an FAQ assurance.
- Whether a fresh legal review is actually needed, given the
  outside-counsel history already on record in
  [[code-of-conduct]], is a process question for the
  Chair/VP Legal conversation, not a v13 text edit.
