---
type: Plan
title: ASFU launch plan — website, Discord, governance
description: "Consolidates the scattered ASFU notes into three workstreams (students.apache.org, Discord, chapter governance) with deliverables, status, dependencies and sequence."
project: university-outreach
status: draft
status_note: consolidation of existing notes, nothing new ruled; sources cited per row; AI-drafted, unreviewed until Drew reads it
owners: [Drew Foulks]
compiled: 2026-11-25
generated:
  by: claude-code/claude-sonnet-5-5
  at: 2026-11-25T15:42:52Z
---

# ASFU launch plan

Pulls together [[talk-2026-11-20-asfu-scaffold]] (the ideas),
[[overview]] (the 2026-07 target-state design), [[website-and-discord]]
(constraints), and the ALC and forum notes (precedent). "Agreed" below
means agreed in the scaffold talk, not ratified.

## What we're trying to do

Model government for tech kids, with a strong mentorship angle and a
semi-professional society behind it (Drew's pitch). The society is the
ASF itself, no invented grades ([[overview]]). Students join a campus
chapter, find a project mentor, and climb the real ASF ladder.
Incentive is employment. Culture comes first: social, rituals that flow
up to the foundation. Mentors are the bottleneck, not campuses.
Chapters mirror the foundation's governance, lazy consensus first.

Notes coalesced here: [[overview]] (design, July),
[[talk-2026-11-20-asfu-scaffold]] (ideas, November),
[[website-and-discord]] (constraints), [[TODOs]], plus precedent from
[[establishing-an-alc-chapter]] and the Ambassador and forum projects.
Not yet folded in: [[outreach-identity]] and the BadgeFed link
(badges were demoted from lead pitch, so deliberately left out).

**Shape:** the website informs, the Discord is where students go, and
the governance is what makes a chapter a chapter.

```
students.apache.org  -->  Discord server  -->  ALCU@school chapters
 (info only)              (the community)       (governance + mentors)
```

## 1. Website: students.apache.org

Information only. Its single job is to lead to the Discord.

| Item | Status | Source |
|---|---|---|
| Host on `*.apache.org` | Required by policy | [[website-and-discord]] |
| Content: what ASFU is, pilot campuses, "start a chapter" one-pager, mentor ask, Discord invite | Proposed | [[website-and-discord]] Q5 |
| Static site on Infra's standard path | Proposed, confirm with Infra | [[website-and-discord]] Q6 |
| Infra request filed | Not done | [[TODOs]] |
| Name on the page (ASFU, ALCU@school) | Open | scaffold Q1 |
| Brand Management sign-off for the @ lockup | Drew's report, no record linked | scaffold Q6 |

**Needs from others:** Infra (hostname, build path). Brand Management
(record of sign-off).

## 2. Discord: where students go

| Item | Status | Source |
|---|---|---|
| One ASF-wide server, open to university people | Drew's plan | scaffold |
| Moderation covered, President OK | Drew's report, unverified | scaffold |
| Discord is the social place; ASF Slack is for development, not a destination for groups | Ruled by Drew, 2026-11-25 | this note |
| Server owner and admins (3+, one an Infra contact) | Open | [[website-and-discord]] Q2 |
| Moderator guide + rules, CoC escalation path | Not written | [[website-and-discord]] Q3 |
| Under-18 handling | Open | [[website-and-discord]] Q4 |
| Decisions made in Discord get recorded publicly | Proposed | `pmc` policy by analogy |

**Ruled (Drew, 2026-11-25):** Discord is the social place. ASF Slack
is a development tool, not for socializing, so it is not a destination
for university groups and there is no Discord-to-Slack trigger.
Students may join Slack eventually, as developers on a project, on the
same terms as anyone else (`slack_policy`). Identity on Discord is a
Discord account, nothing official is decided there, and the forum's
ASF-login ruling ([[requirements]], 2026-11-11) doesn't conflict. Open:
whether [[community-forum-platform]] is also a destination.

**Needs from others:** Infra (hosting stance, a named admin). Whoever
moderates (Drew says covered, name them here).

## 3. Governance: chapters and the mentor supply

### Chapter charter, v0 (all from the scaffold unless noted)

| Concept | Rule |
|---|---|
| Name | Campus chapters are ALCUs, named for the school (ALCU@school). Program name ASFU is proposed. |
| Structure | The chapter picks by one question: does it want a president? Yes: board model (officers, board-style meetings). No, a management committee will do: PMC model. Drew expects most to choose board. (Drew, 2026-11-25. Supersedes the scaffold's "PMC-like first, board only when needed".) **Superseded 2026-11-25 by the proposed [[ADR-001-chapter-board-and-effort-pmcs]]: every chapter has a board and every effort a chapter PMC, no choice.** |
| Leadership | Chapter-led: students lead internally. Shepherds guide, they don't run the chapter. |
| Planning, i.e. how projects are executed (proposed) | Governance first: the structure mirrors the foundation's (Apache Way and university program in symmetry). Planning is how a chapter's efforts get planned and run. A board-model chapter runs the club through its board, and each effort is run the PMC way: a committee, a chair who reports to the board, lazy consensus, roles as written holes. Chapter is to its efforts as the foundation is to its PMCs. Gives students both models in one chapter. |
| Service framing (proposed) | Committing to or advocating for FOSS is community service, so chapter work counts as such. The apt kind of service is skilled work on a public project, e.g. a bug bash, not generic service like a roadside cleanup. Fits the existing event templates in [[overview]] (Issue Triage Night, Documentation Sprint). (Drew, 2026-11-25.) Open: whether ASFU verifies hours for a school's service requirement. That would sit near [[overview]]'s no-credit, no-grading line, so decide before promising it. |
| Efforts (proposed) | Starting set: Outreach, Partying, Education. Community is not a tracked effort. It is baked into all three (Drew, 2026-11-25). |
| Recycled concepts | Chapter structures reuse the foundation's own concepts and names, so what a student learns in a chapter is how the foundation works. Each chapter role or body should map to a real foundation one. (Drew, 2026-11-25.) |
| Emulation | Chapters run the foundation's real forms so students can do them for real later. PMC-model chapter: practice running a project. Board-model chapter: expected to hold board-style meetings (agenda, minutes, reports). Drew, 2026-11-25. |
| Decisions | Committee decides chapter business by lazy consensus. |
| Student path | Chapter, then mentor-guided entry to a project, then the real ASF ladder ([[overview]]). Committer on one project is the realistic promise. |
| Mentoring | Project-level, student-chosen by interest, language, availability. Not 1:1. |
| Heartbeat | Monthly: short report (3 to 5 lines) plus proof of a meeting. |
| Shepherds | ASF Members guiding a university group. |
| Quiet chapter | Friendly Roll Call from a Shepherd. Decide pause or retirement later. |
| Culture | Social first, "Community Over Code" taken literally. A welcome artifact per rung, modeled on the membership email (proposed). |
| Mentor roles | Written "holes" with explicit requirements, self-selected. Folded with the Ambassador program. |
| Pilots | VSU, UNCC, HU. VT is a planned approach. |

### What changes from the existing ALC process

Source: [[establishing-an-alc-chapter]], [[overview]] (ALC).

| | ALC (existing) | ALCU (proposed) |
|---|---|---|
| Founding team | 1 ASF Member + 2 PMC members | Not defined. Students lead, so this can't carry over. |
| Approval | 7-day confirmation, then 7-day ComDev PMC vote on private@ | Not defined. Drew's framing is announce, not ask. |
| Heartbeat | Quarterly report to dev@, enforced by an ALC Chair | Monthly short report. The ALC Chair role appears stalled, so the owner is open. |
| Dissolution | 3+ months inactive, PMC vote | Friendly Roll Call first, rest open. |

The ALC heartbeat exists on paper and isn't enforced
([[overview]] (ALC)). Don't copy it without naming a person who runs it.

### Shepherds (ruled by Drew, 2026-11-25)

A Shepherd is an ASF Member guiding a university group. The term is
borrowed from the Board, where a Shepherd is a Director assigned per
report, but the ASFU role is its own: Members, not Directors. This
supersedes the scaffold's Corrections bullet on Shepherds, which read
the word as the Board role. Still open: how many Shepherds per chapter,
and who the first ones are. Roll Call wording should be adapted, not
copied, since the Board's version needs three responsive PMC members.

### The real bottleneck: mentors

Campuses are not the constraint ([[overview]]: PMC supply is
elastic). Mentors are. The mentor hole and Ambassador fold are agreed
in the scaffold. The page for it is not written ([[TODOs]]).

## Sequence

Order follows dependencies, not importance.

1. **Settle the name** (ASFU / ALCU@school). Blocks the site, the
   Discord name, the Infra tickets, the brand record.
2. **Line up one or two mentors** before announcing campuses.
3. **Draft governance v0**: chapter charter, monthly report template,
   Roll Call wording, mentor hole. All pure documents, no Infra needed.
4. **File Infra requests**: site and Discord, once the name is set.
5. **Write Discord rules and moderator guide** while Infra works.
6. **Launch page and Discord opens**, pilot campuses invited.
7. **Ratify** the chapter structure (`makeadr`), after the pilots
   have run a cycle.

Steps 3 and 5 can start today.

## Open decisions (one owner each: Drew Foulks unless noted)

1. Program and chapter names.
2. Who the first Shepherds are, how many per chapter, and who collects
   the monthly reports (ComDev steward or the ALC Chair role).
3. Discord owner and admins, and Infra's stance on hosting it.
4. Whether the mentor ask goes to the ComDev PMC or to named
   projects directly.
5. Who is in the culture discussion first (scaffold Q8).
6. Whether the president question holds up. Drew expects board to
   win; the pilots (VSU, UNCC, HU) show what works. Open: can a chapter
   switch models later, and what the board model's officers and meeting
   cadence look like. Revisit after one cycle.

## Not covered

No verification of the pilot campuses' interest, the President's OK or
the Brand sign-off (all Drew's account). No Infra process check. No
review against Discord's terms. Rollout and metrics reporting remain
shelved as in [[overview]].
