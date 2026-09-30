---
title: "BIP 78: PayJoin as a constructive counterexample to ownership heuristics"
source: "https://github.com/bitcoin/bips/blob/3a10b5b5f0a7586df8928d580a3009744ebb2079/bip-0078.mediawiki"
type: articles
ingested: 2026-09-30
fetched: 2026-09-30
assigned: 2019-05-01
authors: [Nicolas Dorier]
version: "Status Deployed; repository revision 3a10b5b5f0a7586df8928d580a3009744ebb2079"
sha256: "1888ea3529a77477820045358e4ff4ce1085020ecc3e1d7e47b39bfd3f0eada2"
content_format: mediawiki
extraction_tool: curl-pinned-source
extraction_status: selective-source-digest
tags: [bitcoin, payjoin, common-input-heuristic, change, psbt, privacy]
summary: "A jointly constructed payment can contain sender and receiver inputs, invalidating a categorical common-input ownership rule; final output mappings and off-chain PSBT metadata matter."
quality: 4
credibility_score: 1
confidence: low
normative_authority: canonical-protocol-specification
locators: "Motivation lines 24-45; Protocol lines 63-68; Original PSBT lines 98-102; sender checks lines 274-275; Output substitution lines 329-334; Impacted heuristics lines 343-362; Probing attack lines 364-377"
---

## Source digest

PayJoin negotiates a transaction in which a receiver can contribute inputs to a sender's payment. Consequently, inputs in one transaction need not belong to one owner. The specification expressly targets common-input, script-type change and round-amount heuristics. Output substitution can replace the originally supplied payment script; the original invoice address is therefore not always the final output anchor without retained transaction mapping. Original PSBTs must exclude unnecessary global xpubs and key paths, recognizing off-chain metadata exposure distinct from the public ledger. A proposal without additional receiver inputs is possible and should not be counted as an actual PayJoin. Counterparties can learn contributed UTXOs, and protocol probing/fingerprinting limits privacy.

Mechanical score 1: recognized author +1; no empirical peer-review or recency points. Unique constructive protocol counterexample, not a measured prevalence or universal immunity to clustering. Historical relay-fee assumptions in the text are not current network-wide constants.
