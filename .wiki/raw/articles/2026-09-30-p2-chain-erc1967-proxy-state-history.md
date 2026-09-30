---
title: "ERC-1967: proxy storage and historical implementation"
source: https://eips.ethereum.org/EIPS/eip-1967
source_type: protocol-specification
source_url: https://eips.ethereum.org/EIPS/eip-1967
type: articles
ingested: 2026-09-30
published: 2019-04-24
publication_date_status: "Created date; Final ERC specification"
retrieved: 2026-09-30
license: CC0
tags: [chain-data, ethereum, proxy, storage, upgrades, evidence]
credibility_score: 1
credibility: low
credibility_reason: "Recognized Ethereum specification +1; no recency point, peer review or independent measured attribution. Unique normative storage reference, not a universal proxy detector."
summary: "Proxy storage and balance persist while implementation code can change. Historical interpretation therefore needs historical implementation context."
---

# Historical semantics

Created 2019-04-24, Final. Locators: Abstract; Specification/Logic contract address, Beacon contract address, Admin address; Rationale. DELEGATECALL separates persistent proxy storage/balance from implementation code. Standard slots identify direct implementation, beacon or optional admin. A beacon's implementation() supplies logic when the direct implementation slot is empty. Upgrade/admin/beacon changes SHOULD emit events, not MUST. Function selectors use four bytes and can collide even between different names. Technical inference: current verified source/ABI is insufficient for historical token or wallet interpretation after upgrades; read historical slot values, relevant code and beacon results at the examined block. Missing upgrade logs do not establish absence of upgrades, and missing ERC-1967 slots do not establish absence of every possible proxy. Admin ability to replace logic is distinct from legal ownership of all assets recorded in the proxy's state.
