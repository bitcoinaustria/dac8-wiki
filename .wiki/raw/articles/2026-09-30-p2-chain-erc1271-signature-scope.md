---
title: "ERC-1271: signature validity is contextual authorization"
source: https://eips.ethereum.org/EIPS/eip-1271
source_type: protocol-specification
source_url: https://eips.ethereum.org/EIPS/eip-1271
type: articles
ingested: 2026-09-30
published: 2018-07-25
publication_date_status: "Created date; Final ERC specification"
retrieved: 2026-09-30
license: CC0
tags: [chain-data, ethereum, smart-wallets, signatures, multisig, ownership, evidence]
credibility_score: 1
credibility: low
credibility_reason: "Recognized Ethereum standard +1; no recency point or measured economic-ownership validation. Unique normative authorization interface; not a human-identity study."
summary: "A smart account can accept signatures under state-, time- and authorization-dependent rules; acceptance does not prove sole economic ownership."
---

# What signature acceptance proves

Created 2018-07-25, Final. Locators: Specification, Rationale and Security Considerations. isValidSignature(hash, signature) returns magic value 0x1626ba7e on acceptance and must not change state. Validation may depend on time, state, signer permission, multisignature or another signature scheme. The rationale frames validity as authorization to perform the particular action for a smart wallet. Technical inference: acceptance is evidence about that challenge under that contract's rules, not automatically one natural person's exclusive key control, beneficial ownership or authority for every asset. A reproducible historical challenge must record chain, block, challenge domain/purpose, code/configuration and validation outcome. Do not replace smart-account validation with EOA address recovery or treat one partial signer as the entire multisig. The illustrative single-owner reference implementation is not a universal wallet implementation or evidence of operational Austrian practice.
