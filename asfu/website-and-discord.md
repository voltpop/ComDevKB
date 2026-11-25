---
type: Design
title: ASFU website and Discord — scoping notes
description: "Scoping notes for the ASFU website (students.apache.org) and an ASF-wide Discord open to university people: constraints, open questions, next steps."
project: university-outreach
status: draft
status_note: scoping only, nothing requested or built; Infra tickets not yet filed
owners: [Drew Foulks]
compiled: 2026-11-25
generated:
  by: claude-code/claude-sonnet-5-5
  at: 2026-11-25T15:42:52Z
---

# ASFU website and Discord — scoping notes

AI-drafted, unreviewed until Drew reads it. Builds on
[[talk-2026-11-20-asfu-scaffold]] (infrastructure needs) and the open
TODO in [[TODOs]]. Nothing here is ruled.

## What's wanted

- **Website:** `students.apache.org`, the front door for ASFU. (Drew's
  account in the scaffold talk.)
- **Discord:** one ASF-wide server open to university people, not a
  per-chapter server. Drew reports moderation is covered and the ASF
  President is OK with it (unverified, no thread cited).

## Constraints (checked against PolicyMCP, 2026-11-25)

- **Domain:** official content lives on `*.apache.org`. A third-party
  domain can't host it, and third parties can't use "Apache" or "Community
  Over Code" in domain names (`branding`, `domain_name_branding`). So
  `students.apache.org` is in bounds; an `asfu.org`-style fallback is not.
- **Chat:** the only chat policy PolicyMCP returns is for Slack
  (`slack_policy`): CoC applies, private channels only for security or
  sensitive matters, decisions made in DMs go back to the email thread.
  **No Discord policy found.** Not checked: Infra's own pages beyond
  PolicyMCP. Ask Infra whether Slack-style rules carry over.
- **CoC:** covers "chat services and community spaces, whether official or
  unofficial" (`code_of_conduct`). A Discord with students is in scope.
- **Decisions off-list:** PMC rule is that decisions SHALL NOT be made in
  Slack/IRC/in person (`pmc`). Chapters aren't PMCs, but the scaffold has
  chapter committees deciding by lazy consensus. Same habit is cheap to
  adopt: Discord is for talk, decisions get recorded somewhere public.
- **Linking:** pages must not imply an exclusive relationship with one
  school (`website_linking`, and the "@ implies location" lockup in the
  scaffold). Chapter pages list schools equitably.

## Open questions

1. **Discord vs ASF Slack:** answered by Drew, 2026-11-25. Discord is
   the social place. ASF Slack is a development tool, not for
   socializing, and there is no Discord-to-Slack trigger. Still ask
   Infra whether it hosts the server or ComDev owns it.
2. **Who owns the server?** A personal account owning an ASF community
   space is a bus-factor risk. Recommend: at least three admins, one an
   Infra contact, named in this KB.
3. **Moderation:** who, and under what escalation path to the CoC
   process? Recommend: write a one-page moderator guide before opening
   the doors.
4. **Under-18s:** university people are adults, but high-school students
   find open servers. Recommend: Discord verification level plus an
   18+ line in the rules. Not checked against Discord's terms.
5. **Site content for launch:** smallest useful set. Recommend: what
   ASFU is, the pilot campuses, "how to start a chapter" one-pager, the
   mentor ask, a Discord invite. Everything else later.
6. **Site tech and hosting:** Infra's standard static-site path (Pelican
   or similar) is the default; confirm with Infra. Don't build custom.
7. **Name on the page:** ASFU vs ALCU@school still open (see scaffold).
   Recommend: don't register or announce a name-dependent URL until it
   settles.
8. **Brand sign-off:** the @ lockup clearance is Drew's report. Link the
   public record here before the logo ships on the site.

## Next steps

- [ ] File the Infra requests: `students.apache.org` and the Discord
      (owner: Drew Foulks). Check Infra's current process first.
- [ ] Draft the Discord rules and moderator guide.
- [ ] Sketch the launch page (see question 5).
- [ ] Record the Brand Management sign-off (question 8).

## Not covered

No trademark review of "ASFU", no Discord terms review, no look at how
other ASF communities run Discord. Training-data similarity: this is a
scoping list, not reproduced text.
