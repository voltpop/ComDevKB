---
title: Organize ComDev's docs and policies — open items
type: Tasks
description: "Open items for organizing ComDev's docs and policies."
project: docs-and-policies
last_modified: 2026-11-20
---

- [x] Reconcile with `apache/www-site#725` (Rich Bowen's — confirmed
      ComDev PMC Chair — open PR consolidating ASF policies into one
      `/policy` page) — resolved 2026-08-19: use it as the starting
      baseline checklist rather than building an independent inventory.
      See [[docs-and-policies-policy-inventory]].
- [ ] Find what's missing from Rich's 11-category, ~40-link index. **First
      confirmed gap, 2026-08-19:** `community.apache.org/gsoc/` — not in
      the index, a hybrid how-to/policy page with real enforcement rules
      (hard deadlines, "no exceptions" rejection criteria). Still to check
      the same way: TAC's page, university-outreach guardrails.
- [x] **Verify the PolicyMCP gap list** — resolved 2026-08-19 via a real
      URL-by-URL cross-check (`list_policies` against every href in
      Rich's index), not just titles. Net result: 35 confirmed gaps (one
      title-based false positive removed — `privacy_project_websites`
      is the same doc as Rich's "ASF Website Privacy Policy" — and one
      new gap found — `incubator` itself, not just
      `incubator_ip_clearance`). Full detail in
      [[docs-and-policies-policy-inventory]]'s "Gap list — verified"
      section.
- [x] **Verify the reverse gap** (Rich's index → PolicyMCP) — resolved
      2026-08-19 via `search_policies` content checks, not just the
      absent-key list. Of the ~13 candidates, **12 confirmed genuinely
      absent** from PolicyMCP (Infra Team CoC, DMCA agent, Export
      Control page, Social Media Best Practices, Logo Usage Policy,
      Naming Policy, Trademark Reporting, Project Minimum Requirements,
      Board Escalation Guide, Conference Policy, Giveaway Rules,
      Officer Speaking Guide) and **1 corrected** — the mailing-list-naming
      anchor is already inside the `pmc` key, just not broken out.
      Confirms neither source is a superset of the other. Same section
      as above.
- [ ] Ask Justin McClean (VP Legal, PolicyMCP's author) whether he's the
      same "new VP Legal" already in direct contact per
      [[code-of-conduct]]'s "Questions for the VP Legal" section — not
      yet confirmed, that doc predates this KB's real-names policy.
- [ ] Enumerate what's actually in scope beyond the gap-hunt above
      (which docs, which policies, sourced from where).
- [ ] Decide how the three co-owners split the work, and whether one
      chairs it.
- [x] Check whether this should route through `wg-site`/`wg-website` —
      resolved 2026-08-19: yes, likely should. Andrew Wetmore (a
      co-owner here) is already a `wg-website` member alongside Rich
      Bowen, and that WG's own charter/WIP list already covers this
      exact de-duplication scope. Not yet formally coordinated — this
      is a finding, not an action taken.
- [ ] Actually reach out to `wg-website` (via Andrew, since he's already
      a member) to coordinate rather than run in parallel.
