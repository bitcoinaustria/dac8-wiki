---
title: "Off-chain and privacy-ledger observer limits"
category: reference
sources:
  - raw/articles/2026-09-30-p3-chain-bip324-observer-limits.md
  - raw/articles/2026-09-30-p3-chain-bitcoin-core31-broadcast.md
  - raw/articles/2026-09-30-p3-chain-bitcoin-core31-ip-leak-supplement.md
  - raw/articles/2026-09-30-p3-chain-monero-privacy-primitives.md
  - raw/articles/2026-09-30-p3-chain-monero-view-key-limits.md
  - raw/articles/2026-09-30-p3-chain-zcash-unified-viewing-keys.md
  - raw/papers/2026-09-30-p3-chain-zcash-shielded-spec.md
  - raw/repos/2026-09-30-p3-chain-lightning-bolts-observers.md
  - raw/papers/2026-09-19-wang-rpc-linkage-ccs2025.md
  - raw/papers/2026-09-29-acctmodel-torres-web3-wallet-leaks-usenix2023.md
created: 2026-09-30
updated: 2026-09-30
verified: 2026-09-30
volatility: hot
confidence: medium
tags: [lightning, monero, zcash, viewing-keys, rpc, metadata, observer-model, technical-evidence]
summary: "Public readers, peers, routing nodes, viewing-key holders and identified providers possess different information; privacy claims need version and field scope."
---

# Off-chain and privacy-ledger observer limits

Public verification is not universal transaction transparency, while privacy mechanisms do not erase provider/application knowledge. Specify the observer and the fields it actually has before testing inference.

## Additional observers

A node's local receipt time or relaying peer is not a global transaction-origin fact. BIP324 protects particular passive transport observations, not every active peer or traffic-analysis endpoint. Core31.0's optional private broadcast had an officially disclosed configuration-specific IP leak; 31.1 documents a correction. Read the original release digest with the controlling supplement. Neither is a universal anonymity guarantee.

External RPC/wallet/explorer services can observe requests at their application boundary despite transport encryption. Address interest is not ownership. Torres documents address leakage in an older Web3 sample; Wang's controlled RPC-timing experiment requires network visibility and temporal data. Neither measures annual-tax-only matching or economic ownership.

## Lightning

Public channel gossip can bind node keys to funding outputs, not reveal every off-chain payment or current participant balance. Local HTLC observations and onion routing have distinct scopes; traffic analysis is not categorically excluded. Custodial customer ledgers can contain more than public funding data. BOLT2/4 were pinned; BOLT7 was checked at contemporaneous master, not a successfully fetched pinned copy. Deployed support was not tested.

## Privacy-chain keys

Monero separates real-input ambiguity, amount privacy and one-time recipient outputs. The private view key together with the relevant address reveals incoming observations; key images add spending information. View-only incoming totals alone are not a correct remaining balance or spend authority. Older glossary signature details are not asserted as a complete current protocol specification.

Zcash transparent components differ from shielded notes and public double-spend verification material. Incoming/full viewing authority and spend credentials differ. The fetched NU6.2-labelled specification does not itself prove mainnet activation. ZIP316's active, withdrawn and draft revisions must not be conflated. Unified address usage is not necessarily entirely shielded.

## Leak amplification and alternatives

An identity anchor or additional viewing material can expand the accessible ledger context without breaking cryptography or requiring another provider query. The actual leaked field set and derivation scope control that expansion. No routine Austrian provider collection of viewing keys is established.

Restricted operational access can reduce one leak path without deleting retained data or withdrawing previously stolen copies. Measure actual reachable fields, derived information, task utility and privileged residual access separately; do not infer risk reduction merely from a crypto/privacy label.

## See Also

- [Identity-to-ledger evidence](identity-to-public-ledger-linkage-evidence.md)
- [Bitcoin UTXO evidence](bitcoin-utxo-observation-and-attribution.md)
- [Account and contract evidence](account-contract-chain-data-evidence.md)
- [Provider breach/security evidence](financial-data-breach-and-security-authorities.md)
- [Concentration proof and alternatives](financial-data-concentration-proof-and-alternatives.md)

## Sources

Raw records preserve each public primary URL, normative/first-party evidence class, exact locators and version/measurement limits. Low mechanical scores do not convert unique protocol documentation into measured operational privacy guarantees.
