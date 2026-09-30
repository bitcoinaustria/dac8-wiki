---
title: "ZIP 316: unified address/viewing-key scope and revision boundaries"
source: "https://zips.z.cash/zip-0316"
type: articles
ingested: 2026-09-30
fetched: 2026-09-30
created: 2021-04-07
version: "Revision 0 Active; Revision 1 Withdrawn; Revision 2 Draft"
content_format: html
extraction_tool: web-html-text
extraction_status: selected-standard-sections
tags: [zcash, zip316, unified-addresses, viewing-keys, xpub, revision-status]
summary: "Unified addresses select among receiver types; unified viewing keys can expand visibility across included components without granting spending authority."
quality: 4
credibility_score: 1
confidence: low
---

# Verified scope

**Locators:** header/status; Terminology, Viewing Key and Unified Address; Requirements, Overview and Viewing Keys; Open Issues and Known Concerns; Specification, Revisions. Score: recognized protocol authors +1; current fetch is not proof of a recent publication date. Unique normative role/revision evidence.

## Source digest

A Unified Address combines receiver types; it is not evidence that every transfer to that wallet uses a shielded pool. A single transaction may contain different transfer protocols. Unified Full Viewing Keys and Incoming Viewing Keys combine corresponding viewing components; included transparent account visibility can use an extended public key. An address, incoming viewing key, full viewing key and spending credential therefore require separate leak classifications. A larger bundle may reveal more than a single address, but its scope is bounded by included accounts/components and actual key derivation. The page explicitly distinguishes active Revision 0 from withdrawn Revision 1 and draft Revision 2. New Revision 2 prefixes and transparent-only/P2SH extensions must not be presented as already deployed merely because they appear on this live page. Transparent/cross-pool privacy concerns are acknowledged, not quantified. This standard gives no proof that CASPs routinely hold full viewing keys, no attack success rate, and no assurance against application-side identity or metadata disclosure.
