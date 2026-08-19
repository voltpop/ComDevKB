# ComDevKB

A knowledge base for Apache Community Development (ComDev) work: ideas,
designs, and decisions written up in enough depth that anyone — not just
whoever was in the original conversation — can pick up where things left
off. Its job is project/effort management and keeping async discussions
in sync, not archiving chat transcripts.

If you're an AI agent working in this repo, read `AGENTS.md` first — it
has the required conventions (anonymization, frontmatter, git workflow).
This README is the human-facing "how do I find/use things" guide.

## Where to start

- **[Projects.md](Projects.md)** — every active project, its current
  status, and whether it's actually been raised with the ComDev PMC yet.
  Start here if you want "what's ComDev working on right now."
- **[Reference.md](Reference.md)** — standing analysis/synthesis docs,
  catalogued by topic. Start here if you want "what do we already know
  about X."
- **[strategy/README.md](strategy/README.md)** — the ComDev PMC Chair's
  2-year plan and an open-ended wishlist of ideas nobody's scoped yet.
  Start here if you want "what's the direction, not just the backlog."

## How it's organized

```
projects/<name>/     one directory per active project
  overview.md           what it is, decisions made, why, what was rejected
  TODOs.md              open items, as a checklist (only exists once there's something to track)
  <name>-*.md           sibling/sub-project notes, prefixed with the project name

reference/<name>.md  standing knowledge, independent of any project's status
strategy/            leadership-owned direction: the Chair's plan, the wishlist
archive/<name>/      closed projects, moved here whole, never deleted
```

A **project** has a real (even if distant or ongoing) deliverable — the
Code of Conduct revision counts, even though it's a continuous process,
because Board adoption is the actual target. An **effort** is more
open-ended than that and usually doesn't need its own directory; see
`AGENTS.md`'s Concepts section if you're deciding where something new
belongs.

## Reading a project

Open `overview.md` first — it's written to capture *why*, including
what was considered and explicitly rejected, not just the final
decision. The `status:` line at the top is the fastest way to tell if
something is live, stalled, or already resolved. If a `TODOs.md` exists
alongside it, that's the concrete open-items list; check it before
assuming a project needs re-scoping from scratch.

Notes cross-reference each other with `[[double-bracket]]` tags — these
are citations by name, not clickable links, so search/grep for the
bracketed name to find the file (e.g. `[[ambassador-program]]` →
`projects/ambassador-program/overview.md`).

## What you won't find here

No individual names. Every doc refers to people by role ("the ComDev
PMC Chair," "the draft's author," "a hosting PMC's liaison") instead —
this KB is public today and headed into the Apache org, so that's a
hard rule, not a style preference. See `AGENTS.md`'s Anonymization
section for the full policy, including what to do if you're editing a
doc that predates it.

## Contributing a change

`main` requires changes via pull request (GitHub branch protection).
Work in a branch, open a PR — see `KB-Skills.md`'s `save-to-kb` for the
full mechanics, including the PII scan every diff should get before it
lands. If you're not sure whether something is a new project, an
addition to an existing one, or reference material, `AGENTS.md`'s
Concepts/Layout sections walk through the distinction.

## Full conventions and skills reference

- **[AGENTS.md](AGENTS.md)** — required policy: anonymization, frontmatter,
  the project/effort/sub-project/milestone concepts, git workflow.
- **[KB-Skills.md](KB-Skills.md)** — the "how": starting a project, landing
  a change, auditing for staleness, compiling an office-hours agenda, and
  what's deliberately different here from where these conventions were
  adapted from (`infrastructure-aikb`).
