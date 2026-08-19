---
title: BadgeFed-based verifiable credential service — ComDev-stewarded, foundation-wide
project: badgefed-credential-service
compiled: 2026-08-12
status: platform choice confirmed (2026-08-12) — ComDev-stewarded BadgeFed instance is the credential-service direction; ops details unresolved
---

Suggested 2026-08-12 by Gavin. Framed by the author as the technical
capstone tying together the recognition/credentialing thread that has been
running separately through [[university-outreach]],
[[outreach-identity]], and
[[contributor-role-promotion-language]] — this is a new,
foundation-wide project in its own right, not a feature of the campus
program specifically.

## What BadgeFed is

[BadgeFed](https://badgefed.org) is a decentralized digital-badge system:
cryptographically-signed credentials issued over ActivityPub (the same
federation protocol Mastodon uses), implementing W3C Open Badges
standards. Self-hosted, 100% open source, no central issuing authority —
any instance can issue and verify badges independently, and instances
federate with each other rather than reporting up to one server.

## Decision: ComDev stewards a BadgeFed instance on the foundation's behalf

ComDev runs the shared badge-issuing infrastructure; it does not become
the issuer. Each hosting PMC (or GSoC, TAC, a ComDev-affiliated event, a
university chapter) signs and issues its own badges through the shared
instance. This is the same split every other ComDev program already
uses — build/host the connective tissue, never hold the authority that
sits on top of it.

Why ComDev is the right steward, not Infra or an individual PMC: a
badge-issuing service is cross-PMC connective-tissue infrastructure —
closer to the mailing-list/wiki/GSoC-tracker category ComDev already
operates than to project-specific production data requiring a project's
own security boundary (the reasoning that puts the Pony Mail API
question in Infra's court instead, per [[outreach-identity]]).

## Why this is the capstone, not just a university-program feature

Each of the three companion docs independently ran into a version of the
same unresolved problem — how to represent a real, earned credential
without ComDev (or anyone) inventing a new authority to grant it:

- [[university-outreach]] flags, unresolved: "what to
  call the top-tier committer/PMC-adjacent recognition if it needs a name
  at all for messaging purposes — deliberately left open rather than
  inventing terminology." A badge sidesteps the naming problem entirely:
  it documents that a PMC vote happened, it doesn't invent a rank for it.
- [[contributor-role-promotion-language]]'s core conclusion —
  committer/PMC status is *individual technical trust*, never something
  ComDev itself grants — is exactly the constraint a badge satisfies by
  construction, since the PMC is the signer, not ComDev.
- [[outreach-identity]]'s recurring pattern across every ComDev
  program (GSoC, contributor ladder, TAC, the university pipeline) is
  "ComDev builds the on-ramp/template, the community you actually join
  grants the status." A shared badge-issuing instance is that same
  template layer, applied once, usable by every one of those programs
  instead of being designed separately per program.

So the service isn't scoped to the campus program — it's shared
infrastructure any current ComDev outreach channel can issue through:
GSoC completion badges, TAC volunteer-service badges, committer/PMC-vote
badges from any hosting PMC, university chapter milestones. One piece of
infrastructure resolving several separately-discovered gaps at once is
what makes it a capstone rather than a feature.

## What it's good for, concretely

Cryptographically-signed, portable, independently-verifiable records of
already-earned ASF-native events:
- First merged PR / first contribution attempt
- ICLA signed
- Committer vote passed (issued by the hosting PMC)
- PMC-member vote passed (issued by the hosting PMC)
- GSoC acceptance / completion
- TAC-funded event volunteer service
- University chapter milestones (chapter founding, chapter-lead
  succession, alumni-mentor transition)

These also feed the university pipeline's success-metrics framework
directly: badge-issuance events become independently verifiable,
portable data points instead of self-reported or ad hoc ASF-data pulls —
useful for the chapter-health Green/Yellow/Red rollup and, longer term, as
external evidence for the "structured OSS contribution as legitimate
experiential learning" argument in that doc's academic-legitimacy section.

## Explicitly out of scope

No new membership grades or titles distinct from real ASF/PMC status — a
badge documents an event that already happened under existing ASF
governance, it never creates a new one. ComDev does not sign or issue
badges on a PMC's behalf; it hosts the instance, PMCs (and GSoC/TAC) hold
their own signing identity and issuance decisions.

## Open / unresolved

- **Ops ownership within ComDev** — one PMC-run shared instance vs.
  per-project self-hosting on the shared BadgeFed codebase; who
  administers it day to day.
- **Whether this needs a PMC office-hours conversation before moving**,
  same as the still-unraised API-first advocacy question in
  [[outreach-identity]] — but this one has no Infra dependency, so
  it may not need to wait on that conversation to start.
- **Which program issues first** — a single pilot (e.g. one hosting PMC's
  committer badges, or one GSoC cohort) before wiring it into the broader
  university pipeline or TAC.
- **Federation exposure** — BadgeFed badges federate over ActivityPub to
  ~17M+ Fediverse accounts by design; whether ASF/PMC badge issuance
  should be publicly federated by default or scoped down hasn't been
  discussed.
