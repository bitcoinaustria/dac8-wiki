---
title: "BIP 322: message challenges and bounded Proof of Funds"
source: "https://github.com/bitcoin/bips/blob/3a10b5b5f0a7586df8928d580a3009744ebb2079/bip-0322.mediawiki"
type: articles
ingested: 2026-09-30
fetched: 2026-09-30
assigned: 2018-09-10
authors: [Karl-Johan Alm, Oliver Gugger]
version: "2.0.0, dated 2026-06-04; Status Complete since version 1.0.0 dated 2026-04-15"
revision: "3a10b5b5f0a7586df8928d580a3009744ebb2079"
sha256: "0eb91c5093ef81c462cadffdbe02d4d1638cb270d3ccb47301a6d82860aa0454"
license: CC0-1.0
content_format: mediawiki
extraction_tool: curl-pinned-source
extraction_status: selective-source-digest
tags: [bitcoin, bip322, signed-message, proof-of-funds, identity-anchor, script-validation]
summary: "Message-bound script challenges can strengthen bounded attribution evidence but do not establish absolute control, legal ownership, prior sending or complete holdings."
quality: 4
credibility_score: 2
confidence: medium
normative_authority: canonical-protocol-specification
locators: "Header lines 1-19; Motivation lines 30-48; Terminology lines 52-57; Full lines 129-166; Full (Proof of Funds) lines 168-212; Verification lines 220-266; Changelog lines 492-502"
version_boundary: "Complete describes specification status, not universal wallet deployment. Version 1.0.0 changed signature prefixes and Proof-of-Funds encoding; version 2.0.0 makes its message_challenge explicitly mandatory."
---

## Source digest

BIP322 validates message-bound Script challenges through virtual transactions that cannot spend on a real network. A fresh verifier-issued challenge for a signing script can strengthen an address anchor without revealing private keys. Proof of Funds covers a signer-selected UTXO set; existence and unspent status require separate blockchain checks. It proves neither completeness nor past transaction authorship. Signing on another's behalf and subsequent key/state changes prevent absolute control or ownership conclusions. Verification can be inconclusive for unsupported scripts. Current smp/ful/pof formats require version-aware validation, not unqualified interchange with earlier drafts or legacy signatures.

Mechanical score 2: recent specification version +1, recognized authors +1. Normative method, not an empirical accuracy or deployment benchmark.
