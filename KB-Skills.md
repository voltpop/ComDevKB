---
title: KB Skills — Function Reference
created: 2026-08-19
---

# KB Skills — Function Reference

This is the **one canonical place** the "how" for this KB's assistant
functions lives. `AGENTS.md` carries the *policy* — anonymization, the
Concepts (effort/project/sub-project/milestone), and layout — and points
here for the actual steps. Adapted from `infrastructure-aikb`'s
`KB-Skills.md`; several of its skills don't transfer as-is because
ComDevKB's situation is genuinely different (see "What's different from
infra-aikb" below) — read that before assuming a skill works the same way
here.

If a step here ever conflicts with policy stated in `AGENTS.md`,
`AGENTS.md` wins — flag the drift rather than picking one silently.

## Who this is for

ComDevKB has no project manager and no single centralized authority —
priority-setting happens through ComDev PMC consensus (office hours,
mailing-list lazy consensus), not one named "boss" the way
`infrastructure-aikb` has Fluxo. Every skill below assumes that: no
`kb-prioritize`-equivalent exists here (see below), and any skill that
would otherwise name a specific owner/recipient stays role-based instead,
per `AGENTS.md`'s anonymization rule.

## What's different from infra-aikb — don't copy these assumptions

- **Individual naming is fine, same as infra-aikb.** ComDevKB briefly ran
  a stricter role-only policy on 2026-08-19, then reopened it the same
  day — see `AGENTS.md`'s "Names and identifying information" for the
  full history and the public-repo/Apache-migration tradeoff that was
  weighed and set aside in favor of durable, name-based ownership
  tracking. `owner(s)`-style fields read like infra-aikb's own
  convention: "Brian Proffit (bkp)," not a role placeholder.
- **`main` is actually gated.** This repo has GitHub branch protection
  requiring changes to land via pull request — confirmed 2026-08-19 after
  a direct push to `main` was let through with an explicit "bypassed rule
  violations" warning. Unlike infra-aikb's flat "merge on your own
  judgment, no hard gate" model, `save-to-kb` here means **open a PR**,
  not push straight to `main`.
- **No Jira/Confluence sync skills** (`kb-ingest`, `kb-refresh`,
  `kb-close-loop` are omitted). Nothing in ComDevKB currently lives in
  Jira as trackable epics/issues. The CoC v13 draft *is* a Confluence
  (cwiki) page, so `kb-verify`'s `confluence` row is still real and
  useful — that's a spot-check against a live doc, not an ingestion
  pipeline, so it's kept.
- **No `kb-prioritize`.** Nobody here has Fluxo's role. If ComDev
  leadership ever does set an explicit priority, record it as a dated
  note in the project's `overview.md` rather than inventing a
  frontmatter field for a mechanism that doesn't exist yet.
- **"Live sync" means ComDev office hours (or a live PMC conversation)**,
  not a generic team call — several docs in this KB already say "intend
  to raise at next office hours"; `kb-agenda` below is built around that
  specific venue.

## Shared convention: hyperlink your citations

Whenever a function's output cites a specific place in the KB — a
heading, a table row, a PR — link it, don't just name it:
`[code-of-conduct/TODOs.md § severity rubric](./projects/code-of-conduct/TODOs.md)`,
not a bare filename or plain-text section name.

## Shared convention: land every write via `save-to-kb`

Any skill that edits the KB ends by landing through `save-to-kb` — see
below for what that means given this repo's actual branch protection.

## `kb-checkin` — start of session

1. Orient on which project/effort/reference topic this session concerns —
   check `Projects.md`/`Reference.md`/`strategy/README.md` if not already
   obvious from context.
2. Determine local vs. remote/cloud, same as infra-aikb: a real local
   clone gets full read/write; an ephemeral/hosted sandbox is read-only —
   answer from the KB's content, don't edit/commit/open a PR from there.
3. Defer sync, GitHub auth, and the open-PR queue until actually needed.

## `kb-start` — begin a new project

Minimal by design.

1. Create `projects/<name>/overview.md`: frontmatter (`title`, `project`,
   `compiled`, a free-text `status`), a role-based `owner(s)` line if
   ownership is already known, plus a one-line statement of what the
   project actually is.
2. Register a row in `Projects.md`.
3. Don't seed `TODOs.md` here — add it only once real open items exist;
   an empty `TODOs.md` is noise, not signal, in a KB this size.

## `save-to-kb` — landing any change

Never push straight to `main` — this repo enforces PR-required branch
protection (confirmed 2026-08-19).

1. Scan the diff for PII before committing — real names, emails, session
   IDs — per `AGENTS.md`'s anonymization rule. If in doubt, anonymize or
   leave it out rather than asking first.
2. Work in a branch, commit, push the branch, open a PR.
3. Don't merge your own PR by default — this isn't infra-aikb's flat,
   no-gate team; treat review as a real step unless explicitly told
   otherwise for a specific change.
4. If a real conflict comes up: never blanket-favor one side and never
   let a clean-looking auto-merge stand in for reading both sides.
   Reconcile so both edits survive.
5. After merge, run `kb-audit` (diff-scoped) — see below.

## `kb-audit` / weeding — integrity sweep

Full detail already lives in `AGENTS.md`'s "Weeding and staleness"
section — this entry just names it as a discrete, callable skill:

1. **Diff-scoped, after a merge:** dead `[[wikilink]]` references, a
   `TODOs.md` row with no corresponding project history, a `status` line
   that contradicts what the diff just changed elsewhere.
2. **Full-sweep, event-triggered, anyone, anytime:** run when something
   feels stale that a diff-scoped check wouldn't catch — an "open
   question" nobody's touched in months, a project that's quietly gone
   dormant.
3. Report findings; don't silently resolve them — filing something as
   superseded vs. still-relevant is a judgment call for whoever actually
   knows the current state.
4. Anything found but not immediately fixed goes in `Projects.md`'s or
   `Reference.md`'s staleness watchlist.

## `kb-verify` — spot-check a claim against its live source

Same mechanism as infra-aikb, minus the Jira-epic-tracking use case.

| `system` | typical `tool` | notes |
|---|---|---|
| `github` | `get_file`, `get_issue`, `get_pull_request` | e.g. checking whether a linked working-group proposal PR is still open |
| `confluence` | `get_page` | the CoC v13 draft is a real cwiki page — this is how its "last updated" claim gets re-checked |
| `ponymail` | `get_email` | dev@ mailing-list thread state, e.g. whether a discussion actually reached resolution |

1. Find every checkable claim's citation tag (adopt the same
   `<!-- kb-verify: system=... ref=... field=... value=... checked=...
   tool=... -->` format infra-aikb uses, prospectively — don't
   retrofit old claims).
2. Fetch, compare `field` to the recorded `value`.
3. Match → bump `checked:` in place. Drift → append new prose + a new
   tag with today's date; never edit the old tag or its surrounding
   prose (append-don't-erase, same as `AGENTS.md`'s weeding rule).

## `kb-close` / `kb-block` / `kb-unblock` / `kb-reopen`

Same shape as infra-aikb, adapted to this KB's free-text `status` line
instead of a fixed enum:

- **`kb-close`:** append a short retro (what shipped, what got reversed),
  move `projects/<name>/` to `archive/<name>/` in full, remove its
  `Projects.md` row.
- **`kb-block`:** update `status` to say what it's blocked on and why;
  reflect it in `Projects.md`.
- **`kb-unblock`:** update `status` back to active/current, with a dated
  note on what resolved it.
- **`kb-reopen`:** move `archive/<name>/` back to `projects/<name>/`,
  re-add the `Projects.md` row, append a dated note rather than editing
  the old close-out retro.

## `kb-catalog` — dedup check for reference material

Run before writing any new note into `reference/`.

1. Check `Reference.md`'s controlled `topics:` vocabulary and existing
   notes for overlapping coverage before writing a near-duplicate.
2. If it's genuinely new, add `topics:` frontmatter and a row in
   `Reference.md`.

## `kb-status` — cross-project rollup

Read-only, on-demand. Summarize what's active/blocked/stale by reading
`Projects.md` plus each project's `overview.md`/`TODOs.md` — pure
synthesis, not a new writing burden.

## `kb-prs` — PR queue visibility

More load-bearing here than in infra-aikb, since PRs are the *only* way
changes land (see "What's different" above, not just a courtesy review
step). List open PRs, flag staleness, and before calling anything "still
open," re-check its actual state (`gh pr view`/`gh pr list`) — see
`AGENTS.md`'s existing git-workflow note on this exact failure mode.

## `kb-followup` — deadline sweep

Scans every `projects/*/TODOs.md` for checkbox items carrying a due
date, classifies overdue/due-soon/no-date. Mostly latent today — few
`TODOs.md` items here carry due dates yet — but ready for when they do.

## `kb-agenda` — compile what needs raising at ComDev office hours

ComDevKB-specific adaptation of infra-aikb's "compile what needs a live
sync." Several docs already say "not yet raised with the PMC" or "intend
to raise at next office hours" — this turns that scattered state into an
actual pre-meeting checklist:

1. Pull together: every project/effort flagged "not yet raised with the
   PMC" in `Projects.md`, everything in the staleness watchlists, and any
   `kb-followup` overdue items.
2. Ephemeral by default — meeting prep, not a KB artifact. Only land
   something via `save-to-kb` if the meeting itself produces a decision
   worth recording (update the relevant project's `overview.md`/`status`
   instead of keeping a standalone "agenda" file).

## Escalation: async → live sync

Same as infra-aikb's version, except "live sync" concretely means the
next ComDev office hours or a direct PMC conversation, not a generic
team call. Anyone can call this. Triggers: a fixed round limit on the
same async point, a note getting reverted/re-edited, either side naming
it, or a third party flagging it from outside the disagreement.
