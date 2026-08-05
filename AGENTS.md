# AGENTS.md — instructions for AI agents working in this repo

ComDevKB is a Markdown knowledge base of ideas, designs, and decisions
arising from Apache Community Development (ComDev) work. Each file
documents one topic or workstream in enough depth that a future reader —
human or AI, and not necessarily the original author — can pick up where
things left off without replaying the original conversation.

This is a **project knowledge base**, not a chat log. Write for a future
reader, not as a transcript.

## Anonymization — required before any content lands here

Files in this repo may end up shared or published beyond the original
conversation. Before writing or committing content:

- **No session/system metadata.** Don't include session IDs, conversation
  IDs, working-directory paths, hostnames, or other machine/tool-generated
  identifiers. If a template includes a field like `source_session`,
  remove it.
- **No personal PII.** Don't use full personal names, email addresses, or
  other identifying details. Refer to people by role instead — "the
  author," "a ComDev PMC member," "the requester," "the hosting PMC's
  liaison" — even when the identity is obvious from context (e.g., a
  single-author doc). Public ASF role/committee names (PMC, ComDev, TAC,
  Brand Management) are fine; individual names are not.
- **Dates are fine, identities are not.** Keep absolute dates (helps later
  readers judge how stale something is) but don't pair them with a named
  individual — "decided 2026-07-30" not "Drew decided on 2026-07-30."
- When editing an existing file, scrub any PII/session metadata you find
  in it as part of the edit, even if that wasn't the primary request.

## Structure

- Frontmatter: `title`, `compiled` (date). No session/cwd/author-identity
  fields.
- Body should capture: context/motivation, decisions made and why,
  explicit rejections (what was considered and ruled out, and why — this
  is often more valuable than the decision itself), and open/unresolved
  items so later work doesn't retread the same ground.
- Prefer compressed, decision-dense prose over verbatim transcript. Drop
  back-and-forth that didn't change the outcome.

## Adding a new doc

One file per topic/workstream, `kebab-case-name.md`, at the repo root
unless a clear subdirectory grouping emerges.

## Git workflow

- Before pushing a new commit onto an existing branch that backs an open
  PR, verify the PR still exists and is still open (e.g. `gh pr view`).
  It may have already been merged since you last checked — pushing more
  commits to an already-merged branch either silently reopens it or
  lands the commit somewhere nobody's looking for it.
