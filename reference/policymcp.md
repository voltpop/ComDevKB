---
title: PolicyMCP — Justin McClean's MCP server for ASF policy Q&A
topics: [tooling, ai-agents, governance]
compiled: 2026-08-19
last_modified: 2026-08-19
---

<https://github.com/justinmclean/PolicyMCP> — an independent MCP server
by Justin McClean (currently ASF VP Legal) for answering questions about
ASF policies. **Explicitly not an ASF project** — the README states this
directly, and Apache/related marks remain ASF trademarks regardless.

Possibly (not yet confirmed) the same VP Legal referenced in
[[code-of-conduct]]'s "Questions for the VP Legal" section — that doc
predates this KB's real-names policy, so it never named him. Worth
confirming directly rather than assuming.

## What it covers

Two source sets:
- The full policy set at apache.org/board/policies — releases,
  licensing, branding, security, infrastructure, incubator, and more —
  **73 distinct policy documents**, far more granular than either the
  Board Policy Overview (12 sections) or Rich Bowen's `/policy` index
  (~40 links) already catalogued in
  [[docs-and-policies-policy-inventory]].
- The **Delaware General Corporation Law** (Title 8, Chapter 1 of the
  Delaware Code) — the ASF's actual state of incorporation, and the same
  body of law [[code-of-conduct-legal-questions-and-briefs]] researched
  for CoC enforcement work. Delaware sources only enter search results
  when a query mentions Delaware; always retrievable directly by key.

Policy pages are cached locally for 30 days (`force_refresh=true` bypasses
per-call).

## Tools exposed

- `list_policies` — all available policy documents by section, with cache status.
- `get_policy` — full text of one policy document by key.
- `search_policies` — keyword search with ranked excerpts; Delaware law
  only searched when the query mentions Delaware.
- `refresh_cache` — force re-fetch of one or all documents.

## Full policy document list (73 keys, by section)

**Community And Project Oversight:** `pmc` (PMC Guide), `code_of_conduct`,
`anti_harassment`, `public_archives` (Public Forum Archive Policy)

**Governance:** `bylaws` (Bylaws of the ASF), `certificate_of_incorporation`

**Independence:** `project_independence`

**Reporting:** `board_reporting` (Board Reporting Requirements)

**Release:** `release_policy`, `voting` (Apache Voting Process),
`release_distribution`, `docker_hub` (Docker Hub Policy),
`release_download_pages`, `nightlies` (Project Use of nightlies.apache.org)

**Security:** `security` (Security Team Guidance),
`security_committers` (Vulnerability Handling for Committers)

**Licensing:** `licenses` (CLAs), `apply_license`, `cla_faq`,
`source_headers`, `resolved_licenses` (Approved/Resolved Third-Party
Licenses), `crypto_policy` (Handling Cryptography within an ASF Release),
`generative_tooling`

**Branding:** `branding` (Project Branding Requirements),
`trademark_maintenance`, `website_linking`, `event_branding`,
`merchandise_branding`, `domain_name_branding`, `downstream_distribution`,
`podling_branding` (Incubator Podling Branding Guide), `trademark_policy`
(ASF Trademark Policy)

**Events:** `event_code_of_conduct`

**Infrastructure:** `repo_policy`, `infra_site_ban` (Site-Wide Ban),
`committer_outreach`, `content_moderation`, `mail_rejection`,
`spam_reporting`, `password_policy`, `third_party_services`,
`slack_policy`, `sensitive_information`, `github_actions`,
`website_policy`, `content_security_policy`, `app_upgrade_policy`,
`backup_policy`, `os_upgrade_policy`, `vm_policy`,
`jira_account_approval`, `jira_account_retention`

**Press:** `press`

**Fundraising:** `sponsorship`, `targeted_sponsorship`

**Privacy:** `privacy`, `privacy_contributors`, `privacy_committers`,
`privacy_project_websites`, `privacy_downloadable_products_high`,
`privacy_downloadable_products_medium`, `privacy_mailing_lists`

**Incubator:** `incubator` (Incubator Podling Policies),
`incubator_ip_clearance`

**Delaware Law:** 18 subchapters of Delaware GCL Title 8 (Formation,
Powers, Registered Office/Agent, Directors and Officers, Stock and
Dividends, Stock Transfers, Meetings/Elections/Voting, Amendment of
Certificate of Incorporation, Merger/Consolidation/Conversion, Sale of
Assets/Dissolution/Winding Up, Insolvency, Renewal/Revival/Extension,
Close Corporations, Public Benefit Corporations, Foreign Corporations,
Domestication and Transfer, Miscellaneous Provisions)

## Relevance to ComDevKB

- **[[docs-and-policies-policy-inventory]]:** this is now the most
  granular of the three sources found so far (Board overview, Rich's
  index, this). See that doc for a first-pass gap comparison against
  Rich's index.
- **[[code-of-conduct-legal-questions-and-briefs]]:** the Delaware GCL
  coverage here could serve as a live, queryable cross-check for that
  doc's Delaware nonstock/501(c)(3) research, rather than relying on
  manually-sourced citations.
- **Potential `kb-verify` system**, per `KB-Skills.md`'s table — a
  `policymcp` system/tool row alongside `github`/`confluence`/`ponymail`,
  if this KB ever gets MCP access to it.
