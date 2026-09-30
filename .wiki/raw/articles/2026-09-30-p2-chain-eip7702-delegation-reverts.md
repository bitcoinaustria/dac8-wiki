---
title: "EIP-7702: delegated EOAs and authorization effects surviving failure"
source: https://eips.ethereum.org/EIPS/eip-7702
source_type: protocol-specification
source_url: https://eips.ethereum.org/EIPS/eip-7702
type: articles
ingested: 2026-09-30
published: 2024-05-07
publication_date_status: "Created date; Final Core specification"
retrieved: 2026-09-30
license: CC0
tags: [chain-data, ethereum, eip7702, delegation, accounts, nonces, reverts, evidence]
credibility_score: 2
credibility: medium
credibility_reason: "Recognized Ethereum specification/authors +1 and creation within three years +1. Normative activated-fork behavior, not independent empirical attribution or a deployment audit."
summary: "EOAs can retain delegated code; processed delegations survive later execution failure. A nonzero code field or failed receipt cannot alone classify account/control effects."
---

# Exact failure boundary

Created 2024-05-07, Final. Locators: Motivation; Specification/Set code transaction, Behavior, Delegation indicator, Transaction origination; Rationale/Persistence; Backwards Compatibility. Type 0x04 carries signed authorization tuples processed before execution, after the outer sender nonce increment. Valid tuples set or clear persistent delegation code and increment authority nonce. Invalid tuple processing continues with later tuples. The Behavior note expressly says processed delegation indicators are not rolled back when subsequent execution fails or reverts. This does not mean ordinary reverted call/storage/value effects persist. Delegated EOAs may originate transactions; nonempty code no longer uniquely identifies a classic contract account. Sponsorship separates outer fee payer from authorizing account. Backwards Compatibility warns balances can decrease without that EOA originating the transaction and nonces can increase through other mechanisms. Apply these statements only on chains/forks implementing EIP-7702; Final status alone is not a deployment check.
