---
title: "EIP-1898: coherent state queries by block hash"
source_type: protocol-specification
source_url: https://eips.ethereum.org/EIPS/eip-1898
source: https://eips.ethereum.org/EIPS/eip-1898
type: articles
ingested: 2026-09-30
published: 2019-04-01
retrieved: 2026-09-30
tags: [chain-data, ethereum, rpc, reorg, snapshots, evidence]
credibility_score: 1
credibility: low
credibility_reason: "Official Ethereum specification +1; foundational 2019 design receives no recency point. Final normative interface, not an empirical study or proof every endpoint implements it."
summary: "Final specification separates a particular block hash from height and optionally requires canonical-chain membership."
---

# Coherent snapshots

EIP-1898, Created 2019-04-01, Final; Specification and Rationale. State methods including getBalance, getStorageAt, getCode, eth_call and getProof can identify a block by hash; requireCanonical optionally rejects a known noncanonical block. Sequential block-number or latest queries can otherwise mix states across reorganisation. Logs are not sufficient to reconstruct arbitrary contract state without appropriate contract semantics. Actual endpoint support and returned errors need separate testing. The specification is about consistent observation, not human ownership or statistical linkage.
