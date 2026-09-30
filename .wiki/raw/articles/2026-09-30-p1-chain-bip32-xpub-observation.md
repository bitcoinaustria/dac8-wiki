---
title: "BIP 32: extended public keys as deterministic observation anchors"
source: "https://github.com/bitcoin/bips/blob/3a10b5b5f0a7586df8928d580a3009744ebb2079/bip-0032.mediawiki"
type: articles
ingested: 2026-09-30
fetched: 2026-09-30
assigned: 2012-02-11
authors: [Pieter Wuille]
version: "Status Deployed; repository revision 3a10b5b5f0a7586df8928d580a3009744ebb2079"
sha256: "e5e00a8289db2f681052cf24a745320afc225e66b25d1e489a7c884d2fc7f11f"
content_format: mediawiki
extraction_tool: curl-pinned-source
extraction_status: selective-source-digest
tags: [bitcoin, bip32, xpub, hardened-derivation, wallet-observation]
summary: "An xpub supports deterministic non-hardened descendant-key derivation without signing authority, while hardened account boundaries and script/range scope constrain completeness."
quality: 4
credibility_score: 1
confidence: low
normative_authority: canonical-protocol-specification
locators: "Extended keys lines 60-66; CKDpub lines 85-105; The key tree line 120; Key identifiers/serialization lines 124-140; Audits lines 174-176; Security/Implications lines 195-213"
---

## Source digest

An extended public key contains a public key and chain code. It permits non-hardened public-child derivation, recursively, without private keys; hardened derivation from an xpub fails. Thus a disclosed account xpub can identify many freshly derived keys without common-input clustering. The audit use case explicitly describes public observation of a wallet tree. Correct script policy, paths and scan range are additional requirements; neither other hardened accounts nor independent wallets are thereby revealed. A 32-bit key fingerprint is collision-prone bookkeeping, not a unique person identifier. An xpub alone cannot authorize spending. The separate security warning requires an additional non-hardened descendant private key: together these can compromise the parent private branch. Ordinary transaction serialization does not mandate disclosure of an xpub.

Mechanical score 1: recognized author +1; foundational specification exempted from age penalty; no empirical peer-review points. Unique derivation specification, not evidence that tax-report payloads contain xpubs or that providers universally possess them.
