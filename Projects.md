# Projects — status index

Ground truth for which projects *exist* is `ls projects/` itself; this
file adds status, and whether an idea has actually been raised with the
ComDev PMC yet, which a directory listing can't show. Update the table
whenever a project's `overview.md` `status:` line changes — it doesn't
self-maintain.

| Project | Status | Raised with PMC? | Last touched |
|---|---|---|---|
| [code-of-conduct](projects/code-of-conduct/overview.md) | Living document — in progress, more sessions to be folded in | Ongoing Board-owned process, ComDev input | 2026-07-31 |
| [university-outreach](projects/university-outreach/overview.md) | Target-state design; rollout deliberately shelved pending inventory reconciliation | No — rollout explicitly not on the table yet | 2026-07-29 |
| [badgefed-credential-service](projects/badgefed-credential-service/overview.md) | Platform choice confirmed; ops details unresolved | No | 2026-08-12 |
| [community-forum-platform](projects/community-forum-platform/overview.md) | Stub — two platforms under consideration (Discourse vs. Lemmy) | No | 2026-08-12 |
| [ambassador-program](projects/ambassador-program/overview.md) | First draft evaluated; hybrid-funding refinement proposed | Being raised at 2026-08-19 office hours | 2026-08-19 |

"Last touched" is each project's `overview.md` frontmatter `compiled`
date — a proxy for recency, not a guarantee nothing in the directory
changed since (check `git log projects/<name>/` for the real answer when
it matters).

## Staleness watchlist

Flagged here, not fixed automatically — see `AGENTS.md`'s weeding
convention. An item leaves this list when someone actually acts on it
(raises it, supersedes it, or explicitly confirms it's still fine to sit).

- Several projects above say "not yet raised with the PMC/Chair/wiki
  author" — worth checking at each office hours whether that's still true
  or just never got revisited.
- [[community-knowledge-agent-tooling]] and the outreach-identity API-first
  advocacy section have both been "intend to raise at next office hours"
  since early August — confirm whether either actually happened.
