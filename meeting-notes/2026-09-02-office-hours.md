---
title: ComDev office hours — 2026-09-02
compiled: 2026-09-02
status: prep notes going into the meeting — outcomes/decisions section to be filled in live
---

# ComDev office hours — 2026-09-02

## Carried over: 2026-08-19 decisions/outcomes never recorded

That meeting's note
([[2026-08-19-office-hours]]) still has an empty "Decisions / outcomes"
section. Before diving into new material, worth confirming live what
was actually decided last time on the ambassador program and
docs-and-policies items below, so this KB isn't quietly relying on a
gap.

## Topic: Organize ComDev's docs and policies

**Owners:** Brian Proffit (BKP), Andrew Wetmore, Drew Foulks (dfoulks).

### Progress since last office hours

- **wg-website connection confirmed:** the strategic plan's `wg-site` is
  actually `wg-website` in `apache/comdev-working-groups` — Website
  Working Group, charter includes exactly this effort's
  de-duplication goal ("work through the policy/best-practice
  dichotomy... which one is authoritative?"). Andrew Wetmore (co-owner
  here) is already a wg-website member alongside Rich Bowen ("ComDev PMC
  Sponsor"). Direction: coordinate with wg-website rather than run this
  as a fully independent effort — not yet acted on.
- **Gap-hunt against Rich Bowen's `apache/www-site#725`** (his
  consolidated `/policy` page PR) is done in both directions, verified
  by content rather than just title/key matching:
  - Rich's index → PolicyMCP: 35 confirmed gaps (mostly
    `infra.apache.org` content), after removing one title-based false
    positive and adding one newly found gap (`incubator` itself).
  - PolicyMCP → Rich's index (reverse check): 12 of ~13 candidates
    confirmed genuinely absent from PolicyMCP (Infra Team CoC, DMCA
    agent, Export Control, Social Media Best Practices, Logo Usage,
    Naming Policy, Trademark Reporting, Project Minimum Requirements,
    Board Escalation Guide, Conference Policy, Giveaway Rules, Officer
    Speaking Guide); 1 corrected (mailing-list-naming anchor is already
    inside PolicyMCP's `pmc` key, just not broken out). Confirms neither
    source is a superset of the other.
  - Working theory holding up: this effort's real value-add over PR #725
    is the infra/sub-policy layer a website-content-scoped index misses.
  - Full detail: [[docs-and-policies-policy-inventory]],
    [[policymcp]].
- PolicyMCP (Justin McClean, VP Legal's independent MCP server indexing
  73 ASF policy docs + Delaware GCL) is now connected live for this
  effort's own use.

### Still open

- Ask Justin McClean whether he's the same "new VP Legal" already in
  direct contact per [[code-of-conduct]]'s "Questions for the VP Legal"
  section.
- Enumerate what's actually in scope beyond the gap-hunt (which docs,
  which policies, sourced from where).
- Decide how the three co-owners split the work, and whether one
  chairs it.
- Actually reach out to wg-website (via Andrew) to coordinate rather
  than run in parallel — this is the highest-value ask for this
  meeting, since the finding is a week old and unactioned.

## Topic: Ambassador program

**Raised by:** Ruth (ASF President, ComDev PMC member), 2026-08-19 —
status unchanged since, per [[project_ambassador_program]] and
[[ambassador-program]]/TODOs.md. Carrying these open items forward
since last meeting's outcomes weren't recorded:

- Fedora Ambassadors precedent (<https://fedoraproject.org/wiki/Ambassadors>)
  — not yet reviewed.
- Where "compare notes and share solutions" actually runs (list, call,
  or the [[community-forum-platform]] venue) — check for overlap before
  standing up a separate channel.
- Speaker Travel Program vs. TAC — **update from today:** Gavin
  McDonald, head of TAC, agrees ambassador travel is ComDev's own
  remit, not TAC's. TAC stays means-tested (under-financed
  volunteers). **Decided: ComDev's eligibility criterion is not
  funding-based** — what it actually is instead (role/ambassador-status
  or something else) is still open, worth resolving at this meeting if
  possible. Not yet formalized — no charter or funding mechanism
  decided, not yet confirmed whether this needs a dedicated committee,
  not yet raised with Rich or the PMC.
- Metrics dashboard: confirm `community.apache.org/metrics/` as the
  intended path vs. current external host
  (<https://boxofclue.com/comdev-metrics/>), and who provisions the
  ComDev-owned machine.
- De-duplicate the Good First Issues aggregator against
  [[university-outreach]]'s template layer.
- Name who builds the "equip" toolkit prerequisite and by when.

## Other active threads (no new material this cycle)

- [[code-of-conduct]] — living document, unchanged since 2026-07-31.
- [[badgefed-credential-service]] — platform choice confirmed
  2026-08-12, ops details still unresolved.
- [[community-forum-platform]] — still a stub, Discourse vs. Lemmy
  undecided, not yet brought to the PMC.

## Decisions / outcomes

*(fill in during/after the meeting)*
