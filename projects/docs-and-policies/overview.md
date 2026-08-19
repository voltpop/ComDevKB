---
title: Organize ComDev's docs and policies
project: docs-and-policies
compiled: 2026-08-19
status: new — open-ended effort, no fixed end-state; three co-owners assigned, scope not yet broken down
owners: Brian Proffit (BKP), Andrew Wetmore, Drew Foulks (dfoulks)
last_modified: 2026-08-19
---

New effort raised 2026-08-19: organize ComDev's real, community-facing
documentation and policies — the actual `community.apache.org` content,
program policy pages, and similar artifacts, not this KB's own internal
structure (that work is already covered by this KB's own `AGENTS.md`
conventions, not tracked as a separate project).

Modeled here as a project (own directory, own overview) rather than a
directory-less effort, following the same reasoning as
[[code-of-conduct]]: it has real assigned owners and will accumulate
enough sub-notes to be worth grouping, even though — like an effort —
it has no fixed "done" state; ComDev's docs/policies need ongoing upkeep
indefinitely, not a one-time reorganization.

## Owners

Three co-owners assigned 2026-08-19: **Brian Proffit (BKP)**, **Andrew
Wetmore**, and **Drew Foulks (dfoulks)** — this KB's own author, and a
ComDev PMC member.

## Scope — not yet broken down

Raised at a high level only so far; no specific docs/policies have been
enumerated as in-scope, no priority order set, and no relationship to
this KB's own project-tracking conventions has been decided (e.g.
whether individual docs/policies each get their own sub-project note
here, or whether this stays a single overview until scope sharpens).

## Open / unresolved

- **Resolved 2026-08-19 — see [[docs-and-policies-policy-inventory]]:**
  Rich Bowen (confirmed ComDev PMC Chair) opened `apache/www-site#725`
  the same day, proposing a consolidated `/policy` page listing every
  policy found across the ASF website. Direction set: this effort uses
  Rich's index as its starting baseline and hunts for what's missing,
  rather than building an independent inventory from scratch.
- What's actually in scope — which docs, which policies, sourced from
  where (community.apache.org, cwiki, per-program pages)? Partial answer
  now in [[docs-and-policies-policy-inventory]] (the ASF Board policies
  page, 12 sections) — not yet reconciled against PR #725's coverage.
- How the three co-owners split the work, and whether one of them chairs
  it.
- **Resolved 2026-08-19 — wg-website connection found:** the strategic
  plan's `wg-site` is actually `wg-website` in the real
  `apache/comdev-working-groups` repo (naming slip, not a separate
  group) — the Website Working Group, charter: long-term
  community.apache.org maintenance plus explicit
  **de-duplication**, "work through the policy/best-practice dichotomy
  and ensure that we are not duplicating policy docs... which one is
  authoritative?" Its own current WIP list already has a de-duplication
  item worded almost identically to PR #725's goal. **Andrew Wetmore —
  one of this effort's three co-owners — is already a listed member of
  wg-website**, alongside Rich Bowen ("ComDev PMC Sponsor"). Given that,
  coordinating with wg-website rather than running docs-and-policies as
  a fully independent effort looks like the right call — not yet acted
  on, just the direction the evidence points.
- **Third source found 2026-08-19 — [[policymcp]]:** Justin McClean (VP
  Legal)'s independent MCP server indexes 73 distinct ASF policy
  documents plus the full Delaware GCL text — far more granular than
  either the Board Overview or Rich's index. First-pass gap comparison
  in [[docs-and-policies-policy-inventory]] surfaces ~25 candidate gaps,
  mostly `infra.apache.org` content. Working theory: this effort's real
  value-add over PR #725 may be exactly the infra/sub-policy layer a
  website-content-scoped index naturally misses. Not yet confirmed
  item-by-item.
