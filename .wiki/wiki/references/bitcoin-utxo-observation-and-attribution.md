---
title: "Bitcoin UTXO observation, wallet scope and attribution"
category: reference
sources:
  - raw/repos/2026-09-30-p1-chain-bitcoin-core-transaction-model.md
  - raw/articles/2026-09-30-p1-chain-bip141-witness-identifiers.md
  - raw/articles/2026-09-30-p1-chain-bip32-xpub-observation.md
  - raw/articles/2026-09-30-p1-chain-bip78-payjoin-heuristics.md
  - raw/articles/2026-09-30-p1-chain-bip341-taproot-disclosure.md
  - raw/repos/2026-09-30-p1-chain-core-output-descriptors.md
  - raw/papers/2026-09-30-p1-chain-risk-scoring-taint-models.md
  - raw/articles/2026-09-30-p4-chain-core-observation-context.md
  - raw/articles/2026-09-30-p4-chain-core-release-date-correction.md
  - raw/articles/2026-09-30-p1-chain-bip322-challenge-proof-limits.md
created: 2026-09-30
updated: 2026-09-30
verified: 2026-09-30
volatility: warm
confidence: medium
tags: [bitcoin, utxo, chain-data, xpub, scripts, clustering, technical-evidence]
summary: "Outpoints and script sets support reproducible observation; wallet expansion and ownership require distinct evidence and correction provenance."
---

# Bitcoin UTXO observation, wallet scope and attribution

This is a protocol/source-level evidence map, not a population attribution benchmark. Normative specifications have unique authority despite mechanical low credibility tiers caused by age and lack of peer review. Their empirical claims are not upgraded by that authority.

## Data versus interpretation

Inputs reference previous outputs; amounts require enrichment. Outputs carry values and scripts. Ordinary fees are the difference, with coinbase separately handled. An address is a representation of particular script conditions, not a human-owner field. Distinguish txid/wtxid, full outpoints and contextual block/local-mempool times. Core development revision is not deployed-version evidence. The immutable RPC digest's release date is controlled by its separate correction record: 10 October 2025.

The graph supplies spend/create relationships, not a unique value allocation from each input to each output. Poison reachability and proportional Haircut allocation answer different questions; neither is an ownership proof. The 2014 risk pilot explicitly lacked calibration-quality data.

## Three very different expansion routes

1. Address/script observation covers a defined output set, subject to snapshot and historical coverage.
2. Heuristic clustering adds probabilistic common-input/change relationships. PayJoin is a constructive counterexample; transitive false edges can merge unrelated groups. Unsolicited outputs do not establish recipient consent.
3. A supplied public descriptor/xpub with appropriate non-hardened paths can derive a script set without common-input inference. Hardened other accounts, independent wallets and unscanned ranges remain outside scope. These fields are not mandatory ordinary on-chain data or tax-report fields.

Taproot changes disclosed spending conditions, not visibility of all values. One visible signature is not a count of natural persons. Public and private descriptors are different leak classes; viewing capability must not be mistaken for spend authority.

## Technical application to financial-data concentration

BIP322 v2 message-bound script validation can strengthen a defined anchor without spending real outputs when the checked script conditions actually require signatures. A generally satisfiable script is not a key-authorization proof. Proof of Funds covers a signer-selected set and requires separate chain-state checks; neither completeness nor prior sending is proved. Third-party signing and immediate state/key changes prevent absolute control or legal-ownership conclusions. Complete specification status is not universal deployed wallet support.

A customer-linked final outpoint is a more precise anchor than a withdrawal transaction hash alone. Public derivation data can expand the observation scope beyond a single receive address. Neither route automatically establishes sole control or beneficial ownership. Challenge evidence, provenance, relevant dates and independent economic records must be specified separately. Provider collection of xpubs/descriptors has not been established.

The output project's offline chain countermodels distinguish arithmetic, stipulated ownership worlds, taint policies and transitive cluster correction. They are not Bitcoin serialization, signature validation or an empirical classifier.

## See Also

- [Identity-to-ledger evidence](identity-to-public-ledger-linkage-evidence.md)
- [Account and contract data](account-contract-chain-data-evidence.md)
- [Off-chain and privacy observers](offchain-private-ledger-observation-limits.md)
- [Concentration proof and alternatives](financial-data-concentration-proof-and-alternatives.md)

## Sources

Pinned implementation/specification URLs, individual locators, versions and mechanical assessments are preserved in the source records above. The distinction between normative authority and empirical accuracy is controlling.
