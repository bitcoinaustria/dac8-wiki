---
title: "Identity-to-Public-Ledger Linkage Evidence"
category: reference
sources:
  - raw/articles/2026-08-27-edpb-blockchain-guidelines-02-2025-final.md
  - raw/articles/2026-09-04-eu-delegated-regulation-2025-1140-mica-records.md
  - raw/papers/2026-09-04-goldfeder-cookie-blockchain-popets-2018.md
  - raw/papers/2026-09-04-kappos-bitcoin-cluster-validation-usenix-2022.md
  - raw/papers/2026-09-04-moeser-narayanan-bitcoin-clustering-fc-2022.md
  - raw/papers/2026-09-04-ghost-clusters-usenix-2025.md
  - raw/articles/2026-09-19-cjeu-c413-23p-identifiability.md
  - raw/articles/2026-09-19-edpb-anonymisation-consultation.md
  - raw/papers/2026-09-29-acctmodel-victor-ethereum-clustering-fc2020.md
  - raw/papers/2026-09-29-acctmodel-torres-web3-wallet-leaks-usenix2023.md
  - raw/articles/2026-09-29-acctmodel-stablecoin-issuer-freeze-terms.md
created: 2026-09-04
updated: 2026-09-29
tags: [blockchain, linkage, amount-matching, clustering, attribution, false-positive, expert-evidence]
aliases: [DLT linkage evidence, blockchain breach amplification]
confidence: high
volatility: warm
verified: 2026-09-04
summary: "Evidence map for transaction matching, cluster expansion and identity attribution, including the unproved status of DAC8 annual-aggregate matching."
---

# Identity-to-Public-Ledger Linkage Evidence

> A verified address, transaction identifier or precise amount-plus-time observation can create a durable entry point into a transparent public ledger. The DAC8 annual report provides none of those direct anchors. Whether its annual aggregates materially reduce the candidate set remains an open empirical question.

## Four separate steps

| Step | Required input | What the evidence supports | Failure mode |
|---|---|---|---|
| Transaction match | address or transaction ID, or exact amount plus a short time window | direct lookup or a candidate set; Goldfeder shows frequent unique matches in a web-payment setting | annual window, batching, fees, rounding, internal ledger entries and duplicate amounts |
| Address or wallet cluster | matched public transaction, or a provider deposit or withdrawal address, and chain-specific heuristics | practical cluster expansion on Bitcoin under validated conditions; on Ethereum, clustering relies mainly on exchange deposit-address reuse | CoinJoin, PayJoin, wallet changes, wrong change output and transitive cluster collapse |
| Entity attribution | provider label, controlled interaction, seizure data or another verified source | attribution for some services; Ghost Clusters reports low false positives but widely varying coverage in three seized-service cases | incomplete or stale labels, service-specific results, multiple users and custodial omnibus wallets |
| Natural-person conclusion | independent evidence connecting the entity or address to the person | a person-level conclusion only if separately corroborated | address control, legal ownership and beneficial ownership are not equivalent |

No later step follows automatically from an earlier one. A unique transaction candidate is not proof of who controlled the keys or economically owned the assets.

## DAC8-only boundary

The routine report supplies calendar year, provider, identity, crypto-asset, transaction category and aggregate value or fair-market value, aggregate units and usually transaction count. It does not supply the day, transaction hash, address or counterparty. The external-address category has no count.

No located peer-reviewed study tests whether `year + asset + category + value + units + count = 1` regularly identifies a public-ledger transaction. Existing high match rates use minutes or hours, exact amounts and often an API, known service or address seed. The Singleton argument is therefore a testable hypothesis, not a litigation fact.

## Why a direct ledger anchor is different

The final EDPB blockchain guidance provides the institutional basis for the distinct harm mechanism:

- paragraph 26 treats public keys or identifiers as personal data when reasonably likely means, including information exposed in a breach, can link them to a person;
- paragraph 50 notes that directly identifying data written on-chain may be practically impossible to delete or modify;
- paragraph 61 describes append-only ledgers as potentially persistent and widely replicated;
- paragraphs 63–64 emphasise storage limitation and preventing future linkage of existing and future transactions.

The better formulation is not that DLT data are absolutely immutable or that every address reveals a wallet. It is that a verified identity-to-ledger anchor may remain publicly queryable, may expose historical context and may become more informative when later labels or transactions appear.

## Identifiability is not the same as additional ledger inference

[C-413/23 P, EDPS v SRB](../../raw/articles/2026-09-19-cjeu-c413-23p-identifiability.md), paragraphs 73–87, requires a contextual assessment of a pseudonymised recipient's reasonably likely identification means. Effective controls can matter. Paragraphs 110–115 nevertheless preserve the controller's collection-stage information duty, assessed from its own perspective. The judgment applies Regulation 2018/1725, not DAC8.

An identified DAC8 report is already personal data. The separate evidentiary issue is how much additional public-ledger information its particular fields expose. Neither generic pseudonymity nor generic re-identification research answers that question.

The [EDPB's July 2026 anonymisation consultation draft](../../raw/articles/2026-09-19-edpb-anonymisation-consultation.md), paragraphs 29–31 and 88–90, adds a useful proposed method: identify realistically relevant actors, auxiliary information, access and changing capabilities; give effective controls weight. It expressly contemplates rogue employees and malicious actors where relevant. It is not final guidance and does not establish successful DAC8 aggregate matching. An expert test should state which extra data each actor can actually obtain.

## Chain-specific limits

| Model | Publicly visible | Necessary caution |
|---|---|---|
| Bitcoin and similar UTXO chains | transactions, inputs and outputs; graph structure | multi-input and change heuristics are probabilistic; batching and CoinJoin matter |
| Ethereum and account-based chains | addresses, calls, logs and token transfers; one persistent balance and sequential nonce per address | contract calls, internal operations, bridges, wrappers and token decimals require different methods; no multi-input heuristic exists, and Victor's substitute heuristics (exchange deposit addresses, airdrop consolidation) clustered 17.9 percent of active accounts in 2019 without ground truth; once one address is linked, its balance and history are directly readable |
| Issuer-controlled stablecoins on account chains | per-address token balances in the issuer's contract | issuers reserve address-level freeze powers; visibility and control differ from the native asset |
| Privacy-enhanced chains | visibility depends on protocol version and transaction type | historical Zcash or pre-RingCT Monero findings cannot be generalised to current shielded activity |
| Custodial provider ledger | customer trades and internal transfers | many customer events never map one-to-one to a public transaction; omnibus wallets break naive matching |

## Retrospective expansion and error propagation

Later transactions and new labels can make past public activity easier to interpret. Möser and Narayanan also show the adverse side: one wrong change-output inference can merge unrelated clusters, and small local error rates can propagate through transitive clustering. Kappos and co-authors caution that investigator output is not definitive evidence. The 2025 Ghost Clusters study reinforces both propositions: attribution can be strong for particular seeded services, yet coverage differs substantially between services and providers and changes over time.

## Expert test for DAC8 matching

1. Freeze the asset, chain, provider, transaction category and calendar year.
2. Test the actual DAC8 tuple first, without addresses, transaction IDs or hidden provider timestamps.
3. Measure candidate-set size `k`, unique-match rate, precision, recall, false-discovery rate and top-k recall.
4. Add auxiliary data one layer at a time: provider cluster, short time window, TFR or MiCA record, then address or transaction ID as a positive control.
5. Include negative controls: internal trades, batch withdrawals, equal values, round values, fees, wrong year and wrong category.
6. Keep transaction matching, address clustering, entity attribution and person attribution as separate reported endpoints.
7. Pre-register rules before unblinding and preserve chain snapshot, block height, code hash and parameters.
8. Report results by provider, wallet software, chain and time period; do not rely only on pooled accuracy.

## Claims to exclude

- DAC8 annual aggregates uniquely identify an on-chain transaction.
- A `count` of one identifies a transaction; the external-address field does not contain a count at all.
- Bitcoin clustering metrics transfer to Ethereum, Monero, Zcash or provider-internal ledgers.
- A matched address proves current control, current wealth or beneficial ownership.
- Cluster analysis is deterministic or court-ready without ground truth and error analysis.
- A public-ledger link necessarily exposes the complete portfolio or every future transaction.
- Account-based chains provide no privacy at all; see [[account-model-linkage-exposure|Account-Model Chains and Exposure After an Identity Link]] ([Account-Model Chains and Exposure After an Identity Link](../theses/account-model-linkage-exposure.md)).

## See Also

- [[account-model-linkage-exposure|Account-Model Chains and Exposure After an Identity Link]] ([Account-Model Chains and Exposure After an Identity Link](../theses/account-model-linkage-exposure.md)) — why one identity link exposes more on Ethereum-style chains, and the measured limits.

- [[bitcoin-payment-profile-retention|Bitcoin payment profiles and retention]] ([Bitcoin payment profiles and retention](../theses/bitcoin-payment-profile-retention.md)) — payment use, named recipients, sensitive inference and deletion are distinct evidentiary stages.

- [[breach-harm-and-linkage-empirics|Breach Harm and Linkage Empirics]] ([Breach Harm and Linkage Empirics](breach-harm-and-linkage-empirics.md)) — precise auxiliary-data requirements and non-representative victim research.

- [[dac8-inference-linkage-and-error-evidence|DAC8 Inference, Linkage and Error Evidence]] ([DAC8 Inference, Linkage and Error Evidence](dac8-inference-linkage-and-error-evidence.md))
- [[krypto-mpfg-provider-record-architecture|Krypto-MPfG Provider Record Architecture]] ([Krypto-MPfG Provider Record Architecture](krypto-mpfg-provider-record-architecture.md))
- [[financial-data-breach-and-security-authorities|Financial-Data Breach and Security Authorities]] ([Financial-Data Breach and Security Authorities](financial-data-breach-and-security-authorities.md))
- [[dac8-blockchain-linkage-expert-evidence-protocol|DAC8 Blockchain-Linkage Expert-Evidence Protocol]] ([DAC8 Blockchain-Linkage Expert-Evidence Protocol](dac8-blockchain-linkage-expert-evidence-protocol.md))

## Sources

- [Final EDPB blockchain guidance](../../../legal-docs/supporting/eu-edpb-guidelines-02-2025-blockchain-v2.pdf)
- [When the Cookie Meets the Blockchain](https://petsymposium.org/popets/2018/popets-2018-0038.php)
- [How to Peel a Million](https://www.usenix.org/conference/usenixsecurity22/presentation/kappos)
- [Resurrecting Address Clustering in Bitcoin](https://arxiv.org/abs/2107.05749)
- [Ghost Clusters](https://www.usenix.org/system/files/usenixsecurity25-lubbertsen.pdf)
- [Victor, Ethereum clustering heuristics](../../raw/papers/2026-09-29-acctmodel-victor-ethereum-clustering-fc2020.md)
- [Torres, Willi and Shinde, Web3 wallet leaks](../../raw/papers/2026-09-29-acctmodel-torres-web3-wallet-leaks-usenix2023.md)
- [Circle and Tether freeze terms](../../raw/articles/2026-09-29-acctmodel-stablecoin-issuer-freeze-terms.md)
