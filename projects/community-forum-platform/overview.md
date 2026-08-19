---
title: Threaded community forum with upvoting — knowledge organization and tooling
project: community-forum-platform
compiled: 2026-08-12
status: two platform options under consideration — Discourse and Lemmy (2026-08-12) — scope/hosting/audience still unresolved, not yet brought to ComDev PMC
---

Raised 2026-08-12, in the same conversation that produced
[[badgefed-credential-service]], while sorting ComDev's active
project threads into Social vs. Technical. Captured here, in the same
spirit as [[community-knowledge-agent-tooling]], so a thin idea
survives until it's worked through rather than being lost.

## The idea, as stated

Get a threaded forum solution with upvote functionality deployed; organize
ComDev's knowledge; build some tooling around it. That's the full scope
as raised — hosting owner and audience are still undecided.

## Platform: Discourse and Lemmy under consideration; Apache Answer ruled out

**Shape criterion, stated 2026-08-12:** author wants a *social-media-shaped*
platform — a feed/community feel, not a support-desk or Q&A feel. This is
the deciding criterion behind the ruling below, not just a stylistic
preference.

**Apache Answer — ruled out, 2026-08-12.** Raised as a dogfooding option
(a fellow ASF TLP — entered Incubator 2023-10-09, graduated
2024-12-18, [source](https://incubator.apache.org/projects/answer.html));
dropped once confirmed it's Stack-Overflow-shaped Q&A (one
accepted-answer-per-question, tags), not a discussion/social-feed shape —
fails the shape criterion above regardless of its dogfooding appeal.

**Discourse** — the option most commonly proposed for this kind of
community/knowledge forum. Mature admin/moderation tooling and plugin
ecosystem, strong fit for long-form knowledge organization. Weaker
against the shape criterion: built more for structured
categories/support-desk browsing than a social feed.

**Lemmy** — threaded, has upvoting, and runs on ActivityPub, the same
federation protocol [[badgefed-credential-service]] uses, which
would give one federated-infrastructure story across both projects
instead of two unrelated stacks. Reddit-like feed shape fits the
social-media criterion more directly than Discourse does. Tradeoff still
holds: much younger ecosystem, thinner admin/moderation tooling, and less
naturally suited to long-form knowledge organization than Discourse.

Neither is locked in, but the shape criterion now weighs toward Lemmy;
Discourse stays on the table for its knowledge-organization strength.
Still pending: scope, audience, and hosting, below.

## Likely relation to existing threads (not yet confirmed)

- [[community-knowledge-agent-tooling]] is adjacent but distinct:
  that doc is about agent-mediated *consumption* of the existing
  mailing-list substrate (summarizing dev@ threads). This idea is about
  standing up a *different* substrate entirely — a threaded, upvotable
  forum — which raises the question of whether it's meant to sit
  alongside mailing lists, feed into them, or eventually supersede them
  for some kinds of discussion. Not decided.
- Same stewardship-question shape as [[badgefed-credential-service]]
  and the Pony Mail API discussion in [[outreach-identity]]: who
  is positioned to safely run this — ComDev, Infra, or something
  self-hosted per-PMC — hasn't been worked through.
- "Organize our knowledge" could mean this KB specifically, ComDev's
  broader documentation, or ASF-wide community knowledge — scope not yet
  set.

## Open / unresolved (everything, this is a stub)

- Platform choice (e.g. Discourse, Discourse-alike, something custom).
- Audience: internal ComDev/PMC use, or a public ASF-wide forum.
- Relationship to existing mailing lists — replace, supplement, or feed.
- Hosting/ops ownership (ComDev vs. Infra vs. per-PMC).
- What "tooling around it" means concretely — search/indexing, the
  agent-summarization idea from
  [[community-knowledge-agent-tooling]], something else.
- Not yet raised with the ComDev PMC or any list.
