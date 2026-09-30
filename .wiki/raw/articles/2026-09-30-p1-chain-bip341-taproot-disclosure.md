---
title: "BIP 341: Taproot reveals selected spending paths, not participant ownership"
source: "https://github.com/bitcoin/bips/blob/3a10b5b5f0a7586df8928d580a3009744ebb2079/bip-0341.mediawiki"
type: articles
ingested: 2026-09-30
fetched: 2026-09-30
assigned: 2020-01-19
authors: [Pieter Wuille, Jonas Nick, Anthony Towns]
version: "Status Deployed; repository revision 3a10b5b5f0a7586df8928d580a3009744ebb2079"
sha256: "463690d4c409587759c0ff6e8b8fc3a2bf6cb2cdda0c06ff193d317e0ed898ec"
content_format: mediawiki
extraction_tool: curl-pinned-source
extraction_status: selective-source-digest
tags: [bitcoin, taproot, key-path, script-path, multisig, privacy]
summary: "A Taproot key-path signature does not disclose participant count or optional scripts; script-path spending reveals a selected branch, while values and spend edges remain public."
quality: 4
credibility_score: 1
confidence: low
normative_authority: canonical-protocol-specification
locators: "Design lines 39-48; Script validation rules lines 58-83; Security lines 278-294; Deployment line 347"
---

## Source digest

Taproot outputs use a native witness-version-1, 32-byte program. A key-path spend presents a signature without exposing whether optional script paths or cooperative multi-party conditions exist. A script-path spend instead reveals the executed script and control information, including an internal key and Merkle authentication path, not every unused branch in full. Script-path selection and depth can still reveal information; key reuse is an additional privacy weakness. One visible signature must not be equated with one natural person, one sole owner or one simple wallet policy. Taproot does not encrypt output amounts or remove the references between spent and newly created outputs. Its mainnet activation is recorded at block 709632.

Mechanical score 1: recognized authors +1; no empirical peer-review or recency points. Unique consensus specification. Its privacy properties do not establish a population deanonymization rate, provider implementation, or attribution of beneficial ownership.
