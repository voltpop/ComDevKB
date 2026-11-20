---
title: ASF social media platform — requirements
project: community-forum-platform
compiled: 2026-11-11
status: draft, requirements gathering started 2026-11-11 — every requirement below is a candidate awaiting the author's ruling; nothing raised with ComDev PMC yet
---

Widens [[community-forum-platform]] from "threaded forum" to a social
media platform with two halves. Platform shortlist (Discourse, Lemmy) and
the shape criterion live in that overview, not repeated here.

## Problem, as stated 2026-11-11

The ASF is a community-forward foundation, and it has no foundation-level
place for community. Project mailing lists serve projects; nothing serves
the people across them. This is the purpose the requirements below serve.
Success is measured by whether people find each other across PMCs, not by
traffic.

## Scope, as stated 2026-11-11

- **Owned community space:** a platform the ASF runs for its community.
- **Outbound presence:** ASF accounts on existing networks, with policy
  and tooling to run them.
- **Audiences:** committers/members, newcomers/students, general
  public/users. Three audiences with different needs; see Personas.

## Evaluated (2026-11-11)

- **forum.answers.apache.org (Apache Answer):** looked at, doesn't suit.
  Q&A-shaped, not community-shaped. Consistent with the earlier ruling in
  [[community-forum-platform]].
- **Reddit-style clone keeps coming up.** Hacker News uses a similar
  interface. The ASF is an online-native foundation (it built much of the
  internet), so its people are fluent in this shape and the pull is
  legitimate, not a quirk. The open point is the edges: newcomers,
  students and the public may not share that fluency, and the BBS-era
  members want a classic threaded view (see two-ended usability below). A
  Reddit/HN-shaped feed is a strong candidate for the modern front door,
  not proof it fits every audience. Lemmy's lean stands for that door, but
  it still has to pass the classic-door test.

## Personas (candidate)

| Persona | Wants | Ties to |
|---|---|---|
| Committer/member | cross-PMC conversation, knowledge sharing | [[contributor-role-promotion-language]] |
| Newcomer/student | safe place to ask, find mentors | [[university-outreach]], [[ambassador-program]] |
| Public/user | news, announcements, a way to reach projects | outbound presence |
| Moderator/admin | tools, audit trail, delegation | [[code-of-conduct]] |
| PMC / comms volunteer | post as the project, schedule, reuse content | outbound presence |

## Candidate requirements (all unconfirmed)

Marked `M` must, `S` should, `C` could. Author to rule on each.

### Owned community space

- M Threaded discussion with upvoting (from the original idea).
- M **ASF login (ruled 2026-11-11):** users sign in with their ASF identity. Mechanism (OAuth/OIDC against ASF's identity provider) and how non-committers get an identity are unconfirmed, ask Infra.
- M **Two-ended usability (ruled 2026-11-11):** must work for people who started on BBS/Usenet/mailing lists and for people who grew up on Facebook and newer apps. One community, two front doors:
  - Classic end: threaded view, plain text/Markdown, keyboard navigation, low bandwidth, reply and post by email.
  - Modern end: feed view, reactions, mentions, rich media, mobile-friendly or native apps, push/notification control.
  - Same content and identity behind both; neither is a second-class view.
- M Moderation tools that enforce the Code of Conduct, with an audit trail.
- M Public read access, no account needed to browse (open-by-default).
- S Federation (ActivityPub), the shared story with [[badgefed-credential-service]].
- S Search and indexing of knowledge; agent tooling from [[community-knowledge-agent-tooling]].
- M **Scoped, community-moderated spaces (author preference, 2026-11-11):** each space has its own scope, rules and moderators drawn from its own community. Replaces the earlier "per-PMC or per-topic spaces with delegated moderators" line.
  - Foundation floor: the Code of Conduct and ASF policy apply everywhere, enforced by a foundation-level escalation path above space moderators. (Mine, not stated by the author.)
- S **Spaces are free to create (author preference, 2026-11-11):** low friction to start one, as on Reddit. Guardrails are open: naming and trademark rules (ASF marks), who may create (any ASF login or a tier), and dormant-space cleanup.
- S Badge/credential display from BadgeFed.
- C Mailing-list bridge (feed into or out of dev@ lists).
- C **PyPubSub integration (author preference, optional, 2026-11-11):** the platform can publish its events (new post, reply, new space, moderation action) to an ASF PyPubSub stream, and optionally consume from one, so existing Infra-style tooling and bots work with it. Direction (publish, consume, both) and payload format unset. Must not be required to run the platform.

### Outbound presence

- M Inventory of which networks and which accounts (official, PMC, project).
- M Account ownership, credential custody and succession (no single-person lock).
- M Alignment with the ASF Social Media Best Practices page and trademark/logo policy.
- S Shared content calendar and approval flow for PMC posts.
- S Cross-posting from the owned space to outside networks.
- C Metrics per account/project.

### Non-functional

- M Open-source stack, Apache-2.0-compatible licensing (ASF principle).
- S ASF-first (candidate, from "we are the Apache Software Foundation", meaning unconfirmed): prefer, build on or contribute to ASF projects where one fits, and run under ASF governance, rather than adopt an outside product wholesale. Apache Answer was tried and didn't fit; the question is whether something else at the ASF does, or whether this is a new podling.
- M Privacy: GDPR-style data handling, retention, takedown path.
- M Accessibility, internationalization.
- M Clear hosting/ops owner (ComDev, Infra, or per-PMC). Currently unresolved.
- S Exportability of all content (no lock-in).
- S Spam and abuse resistance at public scale.

## Open questions (need the author or the PMC)

1. Does the owned space replace, supplement or feed the mailing lists? (Carried from the overview.)
2. Who runs it: ComDev, Infra, per-PMC? Does Infra have capacity?
3. Identity: ASF login is required (ruled). Open question is the non-committer path: ASF ID for everyone, or a guest/verified-contributor tier?
3a. Which platforms give both a threaded/email front door and a feed front door? Discourse has email reply and mailing-list mode (my recollection, verify). Lemmy has no email interface that I know of. Test both against the two-ended requirement before the shape criterion decides.
4. Public audience on an owned platform implies a moderation burden. Who staffs it?
5. Outbound: which networks are in scope, and do any ASF accounts already exist? Who owns them today?
6. Legal/brand: does the Social Media Best Practices page already constrain this? Needs reading (see [[docs-and-policies-policy-inventory]]).
7. Success measure: what makes this worth running after a year?
8. Budget and timeline, and whether this goes to the ComDev PMC and to office hours first.

## Next steps

- Author rules on the Must/Should/Could marks and answers 1 to 8.
- Read the ASF Social Media Best Practices page (PolicyMCP) and record constraints.
- Survey existing ASF accounts and platforms (outbound inventory).
- Then update [[community-forum-platform]] status and TODOs.
