---
title: "Monero documentation: ring signatures, RingCT and stealth outputs"
source: "https://www.getmonero.org/get-started/faq/"
type: articles
ingested: 2026-09-30
fetched: 2026-09-30
content_format: html
extraction_tool: web-html-text
extraction_status: selected-official-documentation
software_snapshot: "Official downloads list GUI 0.18.5.2 and CLI 0.18.5.1"
tags: [monero, ringct, ring-signatures, stealth-addresses, observer-model, version-boundary]
summary: "Official documentation describes distinct input, amount and recipient privacy mechanisms while warning that disclosed identity or keys survive protocol privacy."
quality: 4
credibility_score: 0
confidence: low
---

# Verified scope

**Locators:** FAQ, Privacy questions; Moneropedia [Ring Signature](https://www.getmonero.org/resources/moneropedia/ringsignatures.html), “Application to Monero”; [Stealth Address](https://www.getmonero.org/resources/moneropedia/stealthaddress.html), “The Basics”; [Ring CT](https://www.getmonero.org/resources/moneropedia/ringCT.html), “The Basics”; [downloads](https://www.getmonero.org/downloads/), GUI/CLI headings. Undated pages. Score: recognized project +1, first-party privacy framing -1. Unique specification-context evidence, not an independent attack evaluation.

## Source digest

The documentation separates ring signatures obscuring the true spent input among candidate outputs, RingCT hiding transaction amounts, and one-time stealth outputs concealing linkage to the recipient's published address. Public keys/outputs and verification material still exist; “not transparently attributable” is not “no public transaction data.” The FAQ expressly warns that revealing identity or secret keys to another party is not undone by protocol privacy. The RingCT glossary gives its 2017 introduction and historically describes MLSAG; it is not a complete current signature-version specification. Accordingly, no ring size, current attack probability, FCMP++ activation or permanent untraceability is inferred here. The observed download versions bound the software snapshot but are not an independent consensus audit. Earlier zero-decoy or selection-heuristic results would require the exact transaction era, proof/signature scheme and additional observer information before transfer to another version. A provider's own deposit, withdrawal or customer records remain information outside the public-chain privacy boundary.
