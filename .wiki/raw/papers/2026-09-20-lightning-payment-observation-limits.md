---
title: "Kappos et al.: Lightning payment observation limits"
source: "https://arxiv.org/pdf/2003.12470"
type: papers
ingested: 2026-09-20
fetched: 2026-09-20
content_format: pdf
extraction_tool: web-pdf-text
tags: [bitcoin, lightning, privacy, observation-model, peer-reviewed]
summary: "Lightning privacy research separates public funding records from payment inference requiring additional routing or active probing capabilities."
---

# An Empirical Analysis of Privacy in the Lightning Network

Kappos et al., Financial Cryptography 2021; inspected 26-page arXiv version. Page 2 explains that routed payments are not broadcast to all peers or recorded in a public ledger. Sections 4–6 examine active balance discovery and inference by routing participants or from repeated balance snapshots. Section 1.1, p. 3, distinguishes testnet experiments from simulations.

A provider's on-chain funding anchor alone therefore does not expose the full Lightning payment history. Other observation models can weaken privacy, but the paper does not establish retrospective reconstruction of arbitrary purchases from a CASP's address records. Historical experimental conditions are not present-day success rates.
