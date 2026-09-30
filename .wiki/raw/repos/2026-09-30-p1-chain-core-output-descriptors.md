---
title: "Bitcoin Core output descriptors: script-set observation and its limits"
source: "https://github.com/bitcoin/bitcoin/blob/4b612c6bf8cfa319a9df130d4b3d0523fddb6579/doc/descriptors.md"
type: repos
ingested: 2026-09-30
fetched: 2026-09-30
revision: "4b612c6bf8cfa319a9df130d4b3d0523fddb6579"
revision_date: "2026-09-30T14:30:40Z"
sha256: "48d462a1e281714026301618894ac7b327aa88428ada666e7bd6843dbabe4550"
content_format: markdown
extraction_tool: curl-pinned-source
extraction_status: selective-source-digest
tags: [bitcoin, descriptors, xpub, watch-only, multisig, script-policy]
summary: "A public descriptor can deterministically describe script sets, including receiving/change branches and multisig policies, but does not establish a person's complete wallets or beneficial ownership."
quality: 4
credibility_score: 1
confidence: low
normative_authority: canonical-implementation-documentation
locators: "Introduction lines 3-6; KEY expressions lines 74-90; multisig lines 121-139; BIP32 derived keys and chains lines 190-204; Key origin identification lines 206-235; Public and private keys lines 237-253; Multipath descriptors lines 256-278; Checksums lines 288-303"
---

## Source digest

Descriptors describe collections of output scripts rather than a civil owner. Combining an xpub with derivation paths and script functions can identify receiving/change outputs or multisig scripts without heuristic clustering. Wildcard scans have configured finite ranges; unscanned indices, different derivation branches or additional wallets remain outside the result. Public descriptors permit observation without necessarily enabling spending; private descriptors can contain secret keys, so these categories must not be conflated. Hardened derivation requires private material. Key-origin fingerprints and paths are metadata and do not independently authenticate identity or beneficial ownership. Multipath syntax can express receiving and change branches together. Descriptor checksums protect against transcription errors, not hostile alteration or false person attribution.

Mechanical score 1: recognized project +1; no peer-review or publication-recency points. Unique implementation documentation. This pinned development snapshot establishes syntax and scope, not universal provider possession, deployed version distribution, or scan completeness.
