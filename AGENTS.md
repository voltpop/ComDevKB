# AGENTS.md — instructions for AI agents working in this repo

ComDevKB is a Markdown knowledge base of ideas, designs, and decisions
arising from Apache Community Development (ComDev) work. Its job is
project/effort management and keeping async discussions in sync — each
file documents one topic or workstream in enough depth that a future
reader — human or AI, and not necessarily the original author — can pick
up where things left off without replaying the original conversation.

This is a **project knowledge base**, not a chat log. Write for a future
reader, not as a transcript.

For the "how" behind the conventions below — the actual skill functions
(`kb-start`, `save-to-kb`, `kb-audit`, `kb-agenda`, etc.) — see
`KB-Skills.md`.

## Names and identifying information

Real names (and ASF handles, where known) are fine to use — for
ownership/attribution specifically, they're more durable than roles,
since roles drift ("the ComDev PMC Chair" today may not be the same
person next year) in a way a name doesn't.

**History on this:** this repo briefly ran a stricter role-only
anonymization policy (adopted, then reconsidered, all within
2026-08-19) on the reasoning that this repo is public today and expected
to move into the Apache org. That tradeoff is real and was explicitly
discussed — the call was made to use names anyway, favoring durability
and ease of ownership-tracking. Revisit if the repo's visibility or the
migration timeline changes. Docs written under the earlier policy (e.g.
early Code of Conduct notes) may still read role-only; that's fine as a
historical artifact, not something to mass-migrate.

Still avoid regardless of the above:
- **No session/system metadata.** Session IDs, conversation IDs,
  working-directory paths, hostnames, or other machine/tool-generated
  identifiers. If a template includes a field like `source_session`,
  remove it.
- **No email addresses or contact details** — a name is fine, a way to
  reach that person directly isn't.
- When editing an existing file, scrub any session metadata you find in
  it as part of the edit, even if that wasn't the primary request.

## Structure

- Frontmatter: `title`, `compiled` (date — set once, a point-in-time
  record; doesn't get bumped just because the doc was edited later),
  `status` (free text — this KB favors an informative status line over a
  rigid enum, since ComDev threads carry more nuance than
  active/blocked/done). `project: <name>` on any note inside
  `projects/<name>/`, matching the directory. `topics: [tag, tag]` on any
  note inside `reference/` — check `Reference.md`'s controlled vocabulary
  before inventing a new tag. `owners:` is fine wherever ownership is
  actually known (real names/handles, per "Names and identifying
  information" above). `last_modified:` (date) is CI-maintained — see
  `.github/workflows/update-frontmatter.yml` — don't hand-edit it; it
  gets stamped automatically on any PR that touches the file. Still no
  session/cwd fields (`source_session` and similar).
- Body should capture: context/motivation, decisions made and why,
  explicit rejections (what was considered and ruled out, and why — this
  is often more valuable than the decision itself), and open/unresolved
  items so later work doesn't retread the same ground.
- Prefer compressed, decision-dense prose over verbatim transcript. Drop
  back-and-forth that didn't change the outcome.
- Cross-reference other notes inline with `[[note-name]]` (the filename
  stem, not a path — these are citation tags, not clickable links).

## Concepts: effort, project, sub-project, milestone

Adapted from `infrastructure-aikb`'s layout. Which one something is
decides whether it gets its own `projects/<name>/` directory or not:

- **Effort** — an open-ended initiative with no concrete end (e.g. an
  ongoing advisory function). Never reaches a "done" state. Doesn't need
  its own directory — a mention inside a related project/reference note
  is enough.
- **Project** — an effort **with** a concrete deliverable, even if that
  deliverable is far off or the work is genuinely ongoing in the
  meantime (e.g. `code-of-conduct` — Board adoption is the real
  deliverable, even though revision is a continuous process until then).
  Gets a `projects/<name>/` directory, an `overview.md`, and a row in
  `Projects.md`.
- **Sub-project** — a project nested inside a parent project's scope
  rather than promoted to its own top-level directory. Lives as a note
  inside the *parent's* existing directory (e.g. `code-of-conduct`'s
  `v13-proposed-changes.md` sibling notes). Cross-link it to its parent
  via `[[wikilink]]`; no separate `Projects.md` row.
- **Milestone** — a real but small deliverable: a dated checkpoint inside
  a project's notes, not big enough to need its own file. Written as a
  heading: `## <subject> — milestone (<date>)`.

## Layout

- `projects/<name>/` — active initiatives with a real (even if distant)
  deliverable: one `overview.md`, an optional `TODOs.md` for open
  checklist items, and any sibling/sub-project notes.
- `archive/<name>/` — closed projects, moved here in full once done. Not
  deleted — a closed project is still a valid historical record.
- `reference/` — enduring, non-lifecycle knowledge: standing synthesis
  or analysis true independent of any one project's status. Flat, no
  subdirectories — tag with `topics:` instead (see `Reference.md`).
- `strategy/` — leadership-owned strategic thinking: mission, vision,
  priority-setting, open-ended wishlists. **Subjective, top-down
  material** — opinion, taste, and judgment calls about direction, not
  verified facts about how something works. Not held to `reference/`'s
  or `projects/`'s fact-checking bar. No lifecycle, no `Projects.md` row.
  Matters more here than it does in `infrastructure-aikb`: ComDev's own
  strategic plan (budget, working groups, priorities) directly shapes
  which of this KB's projects and efforts are worth pursuing, in a way a
  purely technical Infra team's roadmap doesn't for its own KB.
- `meeting-notes/` — one file per live meeting (e.g. ComDev office
  hours), named `YYYY-MM-DD-<meeting>.md`. Meeting-facing summaries, not
  duplicates of the full project docs they draw from — link out to the
  relevant `projects/`/`reference/` notes rather than restating them.
  Includes a "Decisions / outcomes" section left for after the meeting.
  Flat, no lifecycle, no index file — chronological by filename is
  enough to browse.
- `Projects.md` — status index for `projects/`, including whether each
  has actually been raised with the ComDev PMC yet.
- `Reference.md` — subject catalog for `reference/`, keyed by its
  controlled `topics:` vocabulary.

New material goes into whichever bucket fits; if it's genuinely both a
project deliverable and a standing reference fact, split it rather than
forcing one file to serve both purposes.

## Weeding and staleness

This KB has no single maintainer and no calendar-driven review cadence,
so staleness has to be caught deliberately rather than assumed away:

- **Never silently rewrite or delete a doc to reflect new information.**
  If something is superseded, say so explicitly in the doc (new section
  or updated `status` line) and point to whatever replaced it, rather
  than editing the old conclusion out. Point-in-time records stay
  readable as what was true when they were written; other docs may
  already `[[link]]` to them.
- **Mark stale, don't guess-fix.** If a doc reads outdated or a `[[wikilink]]`
  target no longer exists, flag it in place (or in `Projects.md`'s/
  `Reference.md`'s staleness watchlist) rather than silently resolving
  it — filing something as superseded vs. still-relevant is a judgment
  call for whoever actually knows the current state, not something to
  auto-fix.
- **Check for drift before treating a doc as current.** A `status` line
  that says "not yet raised with the PMC" or "pending X" may be stale by
  the time it's read again — verify against the actual current situation
  (ask, check a PR/thread, check office-hours notes) before building on
  it, rather than trusting the frontmatter forever.
- Anything flagged this way but not yet resolved belongs in `Projects.md`'s
  staleness watchlist, so it doesn't just disappear back into the file
  list.

## Git workflow

- **`main` has GitHub branch protection requiring changes via pull
  request** (confirmed 2026-08-19 — a direct push was let through with an
  explicit "bypassed rule violations" warning, meaning it's enforced but
  currently bypassable, not that it's optional). Default to a branch + PR
  rather than pushing straight to `main`; only push directly when the
  user explicitly asks for that specific action.
- Before pushing a new commit onto an existing branch that backs an open
  PR, verify the PR still exists and is still open (e.g. `gh pr view`).
  It may have already been merged since you last checked — pushing more
  commits to an already-merged branch either silently reopens it or
  lands the commit somewhere nobody's looking for it.
- Only commit or push when the user explicitly asks. Don't take it upon
  yourself to commit "while you're at it."
- Never force-push, skip hooks (`--no-verify`), bypass signing, or amend
  a commit that's already been pushed/shared — create a new commit
  instead.
- Run `git status` before any command that could discard uncommitted
  work (`checkout`/`restore`/`reset --hard`/`clean`), and prefer a
  reversible step (stash, rename, move aside) over a destructive one
  when you're not sure whether something is safe to lose.
- Deleting a branch, force-pushing, or other hard-to-reverse/shared-state
  actions need explicit confirmation in the moment — an earlier approval
  for a similar action doesn't carry forward automatically.
- Never edit git config.
