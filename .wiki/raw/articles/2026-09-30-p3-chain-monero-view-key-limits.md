---
title: "Monero view-only wallets: incoming visibility and key-image limits"
source: "https://www.getmonero.org/resources/user-guides/view_only.html"
type: articles
ingested: 2026-09-30
fetched: 2026-09-30
content_format: html
extraction_tool: web-html-text
extraction_status: selective-source-digest-without-operational-steps
tags: [monero, viewing-key, key-images, data-leak, spend-authority, observer-model]
summary: "A private view key and address reveal incoming wallet activity but do not alone authorize spending or give a correct balance after outgoing activity."
quality: 4
credibility_score: 0
confidence: low
---

# Verified scope

**Locators:** introductory paragraphs before CLI instructions, especially the accompanying-key-images paragraph. Corroborating project documentation: [Offline Transaction Signing](https://docs.getmonero.org/cold-storage/offline-transaction-signing/), “Restoring view-only wallet”. No operating instructions reproduced. Publication date unspecified. Score: recognized project +1, first-party implementation account -1. Unique role/visibility evidence, not a measured leak incident.

## Source digest

The guide distinguishes a view-only wallet from possession of the mnemonic seed or private spend key. With the wallet's main address and private view key, its incoming transactions can be recognized; the view-only role cannot sign transactions or independently spend funds. Outgoing activity and the correct remaining balance require additional information, notably the corresponding key images. The official instructions also specify limitations for hardware-wallet-derived view-only wallets. A leaked public receive address and a leaked private view key therefore create different observer capabilities. A leaked view-only dataset is not necessarily a complete, reliable balance record, and neither a key image nor a view key should silently be described as a spend key. Local wallet metadata or already signed transactions can add further facts, so the actual leaked fields must be inventoried. This documents a technical information-expansion mechanism; it does not establish that Austrian CASPs collect these keys, that tax reporting transmits them, or that any specific historical breach exposed them.
