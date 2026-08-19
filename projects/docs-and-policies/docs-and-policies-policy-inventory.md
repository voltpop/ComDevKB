---
title: Docs and policies — policy source inventory
project: docs-and-policies
compiled: 2026-08-19
status: three sources scraped, PolicyMCP gap list verified live against Rich's index — flags active overlapping work, not yet reconciled with the effort's three co-owners
last_modified: 2026-08-19
---

Sub-project note for [[docs-and-policies]] (`projects/docs-and-policies/overview.md`).
Started per Drew Foulks's request to cite these two sources; kept as a
standalone doc since it may graduate into `reference/` once the policy
landscape stabilizes rather than staying tied to this project's own
lifecycle.

## Source 1: ASF Board Project Policies & Services (apache.org/board/policies)

<!-- kb-verify: system=web ref=https://apache.org/board/policies field=section-count value=12 checked=2026-08-19 tool=WebFetch -->

Twelve policy sections, scraped 2026-08-19:

1. **Community & Project Oversight** — technical decisions on public,
   archived mailing lists; transparent async discussion unless a
   documented private reason exists.
2. **Operate Independently** — projects must govern themselves
   independently of undue commercial influence.
3. **Quarterly Board Reporting** — regular status reports to the Board.
4. **Software Release Policy** — compliance with the Release Policy,
   Apache Voting Process, and Release Distribution Policy.
5. **Security Notification Procedure** — collaborate with the Security
   Team; must follow notification procedures for security issues.
6. **Contributors & Licensing** — contributor CLAs, Apache
   licenses/headers, no unapproved restricted licenses in releases.
7. **Branding & Trademark Policy** — project websites comply with Apache
   Branding Requirements; PMCs manage trademarks.
8. **Infrastructure Policy** — primary repositories on ASF-maintained
   services; project homepages as static sites on ASF infrastructure.
9. **Press & Marketing** — formal press releases/media relations
   coordinated through the Marketing team.
10. **Fundraising Policies** — direct financial donations coordinated
    with VP, Fundraising.
11. **Privacy Policy** — compliance with the Foundation's Privacy Policy.
12. **Incubator Podling Policies** — podlings follow Incubator PMC
    policies before graduation.

## Source 2: apache/www-site PR #725 — "PROPOSED - /policy page"

<!-- kb-verify: system=github ref=apache/www-site#725 field=state value=OPEN checked=2026-08-19 tool=get_pull_request -->

- **Author: Rich Bowen** (`rbowen`) — same person as "the ComDev PMC
  Chair" in [[2-year-strategic-plan]] (confirmed via the HackMD source
  URL's `@rbowen` handle) and "Rich" throughout [[ambassador-program]].
- **Opened:** 2026-08-19. **State:** OPEN, unmerged.
- **What it does:** adds `content/policy/index.md` (80 lines, one new
  file) — Rich's own description: "Lists all policies I was able to find
  across the entire website, in one central place, for better
  findability."

### Full proposed index (scraped from the PR's file content, not just its metadata)

<!-- kb-verify: system=github ref=apache/www-site:content/policy/index.md field=content value="80-line index, 11 categories" checked=2026-08-19 tool=get_file (fetched at commit a94c0e4, the PR's head — this file doesn't exist on main yet) -->

Rich's page opens with: *"The Apache Software Foundation maintains
policies across several areas to ensure consistent governance, legal
compliance, and community standards across all Apache projects. This
page serves as a central index of all ASF policies."* It explicitly
points to the Board Policy Overview (Source 1 above) for the MUST/
SHOULD/MAY summary, rather than duplicating it — see "resolved" note
under Open questions below.

**Code of Conduct & Community Behaviour**
- [Code of Conduct](/foundation/policies/conduct.html) — all ASF-managed spaces
- [Anti-Harassment Policy](/foundation/policies/anti-harassment.html) — in-person events/conferences
- [Infrastructure Team Code of Conduct](/dev/infra-coc.html) — Infra-specific, references the general CoC

**Legal & Licensing**
- [Release Policy](/legal/release-policy.html)
- [Source Header and Copyright Notice Policy](/legal/src-headers.html)
- [3rd Party License Policy](/legal/resolved.html)
- [Generative Tooling Guidance](/legal/generative-tooling.html) — AI/ML-generated contributions
- [Applying the Apache License](/legal/apply-license.html)
- [DMCA Designated Agent](/legal/dmca.html)
- [Export Control / Encryption Policy](/licenses/exports/)

**Trademark & Branding**
- [Apache Trademark Policy](/foundation/marks/)
- [Project Branding Requirements](/foundation/marks/pmcs.html)
- [Third Party Event Branding Policy](/foundation/marks/events.html)
- [Domain Name Policy](/foundation/marks/domains.html)
- [Downstream Distribution Policy](/foundation/marks/downstream.html)
- [Social Media Best Practices](/foundation/marks/socialmedia.html)
- [Logo Usage Policy](/foundation/marks/logos.html)
- [Naming Policy](/foundation/marks/naming.html)
- [Linking Policy](/foundation/marks/linking.html)
- [Trademark Reporting](/foundation/marks/reporting.html)
- [Merchandise Policy](/foundation/marks/merchandise.html)

**Privacy**
- [ASF Privacy Policy](https://privacy.apache.org/policies/privacy-policy-public.html) (external)
- [ASF Website Privacy Policy](https://privacy.apache.org/policies/website-policy.html) (external)
- [Public Forum Archive Policy](/foundation/public-archives.html)

**Security**
- [Security Policy](/security/)
- [Security Policy for Committers](/security/committers.html)

**Governance & Project Requirements**
- [Board Policy Overview](/board/policies.html) — Source 1 above
- [Apache Project Minimum Requirements](/dev/project-requirements.html)
- [PMC Guide — Required Policies](/dev/pmc.html#policy)
- [Apache Voting Process](/foundation/voting.html)
- [Board Escalation Guide](/board/escalation.html)

**Sponsorship & Fundraising**
- [Sponsorship Policy](/foundation/sponsorship.html)
- [Targeted Sponsorship Policy](/foundation/docs/targeted-sponsorship-policy.html)

**Infrastructure** (all external: infra.apache.org)
- [Project Source Repository Policy](https://infra.apache.org/project-repo-policy.html)
- [Project Website Policy](https://infra.apache.org/project-site-policy.html)
- [Release Distribution Policy](https://infra.apache.org/release-distribution.html)

**Conferences & Events**
- [Conference Policy](/foundation/conferences.html)
- [Third Party Event Branding Policy](/foundation/marks/events.html) — listed twice in Rich's source (also under Trademark & Branding)
- [Giveaway Rules](/giveaway-rules/)

**Other Policies & Guidelines**
- [Press & Publicity Guidelines](/press/)
- [Officer Speaking Guide](/press/guides/officer-speaking-guide.html)
- [Mailing List Policy](/dev/pmc.html#mailing-list-naming-policy)
- [Contributor License Agreements](/licenses/#clas)
- [CLA FAQ](/licenses/cla-faq.html)

### Why this matters more than a citation

This is **active, in-flight work by the ComDev PMC Chair that directly
overlaps** with the docs-and-policies effort's stated goal (organize
ComDev's real docs and policies). It isn't prior art to study after the
fact — it's a live PR opened today, the same day this effort started.

Worth raising with the effort's three co-owners (Brian Proffit, Andrew
Wetmore, Drew Foulks) before doing independent scoping work: does
`docs-and-policies` fold into/support PR #725, review it, or is Rich's
page one input among several the effort organizes? Doing parallel,
uncoordinated inventory work risks duplicating exactly what PR #725
already did.

## A category to watch for: committer-only supplements to public policies

Checked the ASF committers-private SVN repo (2026-08-19) for anything
this effort should be aware of. Nothing there belongs in this KB or in
Rich's public index — most of it is superseded/historical or genuinely
sensitive (trademark-dispute case files, executed legal agreements,
vendor-donated licenses) — but one real pattern surfaced: **some public
policies have a committer-only operational supplement**, e.g. VP Brand
Management maintains private guidance for PMCs on evaluating third-party
trademark permission requests, layered on top of the public trademark
policy already in Rich's index. Don't reproduce that content here — the
point is just that "the public index is the complete picture" may not
always hold, so double-check with the relevant officer/VP before
assuming a gap in Rich's list means the policy doesn't exist anywhere.

## Open questions

- Has anyone on the docs-and-policies effort seen PR #725 yet?
- **Resolved 2026-08-19 — direction set:** the effort starts from Rich's
  index as the baseline checklist and hunts for what's missing from it,
  rather than building an independent inventory from scratch. Doesn't
  yet mean the effort formally coordinates with Rich or comments on the
  PR — just that his list is the starting point, not a competing one.
- **Resolved 2026-08-19 — Source 1 vs. Source 2 relationship:** not
  duplicative. Rich's page (Source 2) explicitly defers to the Board
  Policy Overview (Source 1) for the MUST/SHOULD/MAY summary and links
  to it directly rather than restating it — Source 1 is the
  obligation-level summary, Source 2 is the granular link index to every
  actual policy document. Both stay relevant.
- Still open: what's actually missing from Rich's 11-category, ~40-link
  index? Not yet checked against, e.g., ComDev's own program-specific
  policies (GSoC rules, TAC selection criteria, university-pipeline
  guardrails already documented in [[university-outreach]]) — none of
  which Rich's page appears to cover, since it's whole-of-website rather
  than ComDev-specific.

## First confirmed gap: community.apache.org/gsoc/

<!-- kb-verify: system=web ref=https://community.apache.org/gsoc/ field=policy-content value="hybrid: how-to guide with embedded binding rules" checked=2026-08-19 tool=WebFetch -->

Checked 2026-08-19 — confirms the hypothesis above with a concrete
example rather than leaving it speculative. The GSoC page is **not**
in Rich's `/policy` index, and it's a hybrid rather than a clean policy
doc:

- Mostly instructional (guidelines for students/mentors, an application
  template, a 2026 timeline).
- But embeds real binding rules with enforcement language: *"Proposals
  without a score will be rejected, no exceptions"*; proposals lacking a
  mentor get down-rated; hard deadline language ("must be completed")
  for scoring/application dates.

**Pattern this suggests:** ComDev's own program pages mix how-to content
with enforceable rules in the same page, at a level of granularity
Rich's whole-of-site index doesn't reach. Worth checking TAC's page and
the university-outreach guardrails the same way before generalizing
further — one confirmed example isn't yet a full pattern.

## Source 3: PolicyMCP (Justin McClean, VP Legal) — see [[policymcp]]

A third, far more granular source surfaced 2026-08-19: **73 distinct
policy documents**, vs. the Board Overview's 12 sections and Rich's
~40 links. Full detail (tools, install, complete list) in [[policymcp]]
— this section is just the gap comparison against Rich's index.

### Gap list — verified 2026-08-19 against live PolicyMCP

<!-- kb-verify: system=policymcp ref=list_policies field=url-cross-check value="see gap tables below" checked=2026-08-19 tool=list_policies -->

Superseded the title-based first pass below with a real URL-by-URL
comparison, now that [[policymcp]] is connected as a live MCP server:
pulled every PolicyMCP key's actual source URL via `list_policies` and
checked it against every href in Rich's index (Source 2 above). Two
corrections came out of doing this for real instead of by title:

- **False positive removed:** `privacy_project_websites` — its URL
  (`privacy.apache.org/policies/website-policy.html`) is *exactly*
  Rich's "ASF Website Privacy Policy" link. Same document, different
  title. Not a gap.
- **New gap the title pass missed:** `incubator` (Incubator Podling
  Policies, `incubator.apache.org/policy/incubation.html`) — Rich's
  index has no Incubator section at all, so even the top-level
  incubation-policy page is missing, not just `incubator_ip_clearance`.

**Confirmed gaps — PolicyMCP documents with no matching URL anywhere in
Rich's index (35 total):**

- **Governance/Reporting (4):** `bylaws`, `certificate_of_incorporation`,
  `project_independence`, `board_reporting`.
- **Release (4):** `docker_hub`, `release_download_pages`, `nightlies`,
  `crypto_policy`.
- **Branding (2):** `trademark_maintenance` (distinct page from Rich's
  "Trademark Reporting" — different URL, `responsibility.html` vs.
  `reporting.html`), `podling_branding`.
- **Events (1):** `event_code_of_conduct` — confirmed genuinely distinct
  from the Anti-Harassment Policy (different domain entirely:
  `apachecon.com/conduct.html` vs. `apache.org/foundation/policies/
  anti-harassment`). Resolves the "unclear if separate" flag from the
  first pass.
- **Infrastructure — still the largest gap, 17 documents (not ~15 as
  first estimated):** `infra_site_ban`, `committer_outreach`,
  `content_moderation`, `mail_rejection`, `spam_reporting`,
  `password_policy`, `third_party_services`, `slack_policy`,
  `sensitive_information`, `github_actions`, `content_security_policy`,
  `app_upgrade_policy`, `backup_policy`, `os_upgrade_policy`,
  `vm_policy`, `jira_account_approval`, `jira_account_retention`.
  Confirmed: Rich's Infrastructure section only lists 3 items
  (`repo_policy`, `website_policy`, `release_distribution` — all
  present in PolicyMCP too), everything else on `infra.apache.org`
  is absent from his index.
- **Privacy (5, not 6 — see false positive above):**
  `privacy_contributors`, `privacy_committers`,
  `privacy_downloadable_products_high`,
  `privacy_downloadable_products_medium`, `privacy_mailing_lists`.
  The last one is confirmed genuinely distinct from Rich's "Mailing
  List Policy" — that's `dev/pmc.html#mailing-list-naming-policy`
  (ML *naming* rules), while `privacy_mailing_lists` is
  `privacy.apache.org/policies/mailinglist-policy.html` (ML *privacy*
  policy). Resolves the ambiguity flagged in the first pass.
- **Incubator (2):** `incubator` (new finding, see above),
  `incubator_ip_clearance`.

**Confirmed theory:** every infra.apache.org-hosted document in
PolicyMCP's set is absent from Rich's index, and Rich's Infrastructure
section only covers the 3 items already cross-listed. The
docs-and-policies effort's real value-add over PR #725 is the
infra.apache.org layer plus the governance/privacy/incubator sub-policies
above — not a theory anymore, a direct URL-level diff.

**Reverse gap — verified by content, not just by key list:** ran
`search_policies` for each of the ~13 Rich-only items to check whether
their content actually exists somewhere inside PolicyMCP's 73 documents
under a different key, rather than trusting the URL list alone. Result:
**12 confirmed absent, 1 was not actually a gap.**

Confirmed genuinely absent from PolicyMCP — no matching content
anywhere in a search, not just missing as a standalone key:

- Infrastructure Team Code of Conduct (`/dev/infra-coc.html`)
- DMCA Designated Agent (`/legal/dmca.html`)
- Export Control / Encryption Policy (`/licenses/exports/`) — the
  *page itself* isn't indexed, though `crypto_policy` and `cla_faq`
  both reference it by name/link ("see the ASF Exports Classifications
  and Source Links page") without reproducing its content
- Social Media Best Practices (`/foundation/marks/socialmedia.html`)
- Logo Usage Policy (`/foundation/marks/logos.html`) — logo/graphics
  rules appear scattered inside `merchandise_branding` and
  `domain_name_branding`, but not this dedicated page
- Naming Policy (`/foundation/marks/naming.html`) — confirmed via
  `curl -I` this is a real, independently live page (HTTP 200, not a
  redirect to `marks/pmcs.html`), so it's a genuine separate document,
  not an alias of `branding`
- Trademark Reporting (`/foundation/marks/reporting.html`) — `trademark_maintenance`'s
  own content explicitly points to "the Apache Trademark Reporting
  Guidelines" as a separate document, corroborating the gap from
  inside PolicyMCP's own text
- Apache Project Minimum Requirements (`/dev/project-requirements.html`)
- Board Escalation Guide (`/board/escalation.html`) — same pattern as
  Trademark Reporting: `pmc`'s content names "the detailed Escalation
  Guide" as an external document rather than containing it
- Conference Policy (`/foundation/conferences.html`)
- Giveaway Rules (`/giveaway-rules/`)
- Officer Speaking Guide (`/press/guides/officer-speaking-guide.html`)

**Not actually a gap:** Mailing List (naming) Policy — Rich's link
(`/dev/pmc.html#mailing-list-naming-policy`) is an anchor *within* the
`pmc` document, and `search_policies` surfaced that exact anchor's
content directly. PolicyMCP does contain this — it's just not broken
out as its own key, same as the original inventory note predicted.

If `docs-and-policies` ends up building a merged index rather than just
patching PR #725, the 12 confirmed items belong in it too — PolicyMCP
isn't a full replacement for Rich's page, it's complementary.

One unresolved detail, not worth blocking on: `cla_faq`'s PolicyMCP URL
(`apache.org/foundation/license-faq.html`) differs from Rich's link
path (`/licenses/cla-faq.html`) — plausibly the same page via a
redirect, not independently confirmed.

<details>
<summary>Superseded first-pass (title-based only, kept for the record)</summary>

Original 2026-08-19 pass, before PolicyMCP was connected as a live MCP
server — comparison was by title/name only, not by URL:

- **Governance/Reporting, missing entirely from Rich's index:** `bylaws`,
  `certificate_of_incorporation`, `project_independence`,
  `board_reporting`.
- **Release, missing:** `docker_hub`, `release_download_pages`,
  `nightlies`, `crypto_policy`.
- **Branding, missing:** `trademark_maintenance`, `podling_branding`.
- **Events, missing:** `event_code_of_conduct` — distinct from the
  Anti-Harassment Policy already in Rich's index; unclear if this is a
  genuinely separate document or an overlap worth resolving.
- **Infrastructure — the largest gap by far, ~15 documents:**
  `infra_site_ban`, `committer_outreach`, `content_moderation`,
  `mail_rejection`, `spam_reporting`, `password_policy`,
  `third_party_services`, `slack_policy`, `sensitive_information`,
  `github_actions`, `content_security_policy`, `app_upgrade_policy`,
  `backup_policy`, `os_upgrade_policy`, `vm_policy`,
  `jira_account_approval`, `jira_account_retention`. Plausible
  explanation: Rich's index is scoped to `www.apache.org` content, and
  most of these live on `infra.apache.org` instead — same website-scope
  limitation as the GSoC gap above, different site.
- **Privacy, missing:** `privacy_contributors`, `privacy_committers`,
  `privacy_project_websites`, `privacy_downloadable_products_high`,
  `privacy_downloadable_products_medium` — Rich's index has the two
  top-level privacy policies but not these program-specific variants.
- **Incubator, missing:** `incubator_ip_clearance`.

**Working theory:** Rich's index and the Board Overview are both scoped
to `www.apache.org`; PolicyMCP additionally covers `infra.apache.org`
and several narrower sub-policies neither of the other two sources
reaches. If confirmed, the docs-and-policies effort's real value-add
over PR #725 may be exactly this: surfacing the infra.apache.org and
sub-policy layer that a website-content-focused index naturally misses.

</details>
