---
title: "DAC8 Blockchain-Linkage Expert-Evidence Protocol"
category: reference
sources:
  - raw/articles/2026-09-04-enfsi-evaluative-reporting-guideline.md
  - raw/articles/2026-09-04-nist-sp800-86-digital-forensics.md
  - raw/papers/2026-09-04-goldfeder-cookie-blockchain-popets-2018.md
  - raw/papers/2026-09-04-kappos-bitcoin-cluster-validation-usenix-2022.md
  - raw/papers/2026-09-04-moeser-narayanan-bitcoin-clustering-fc-2022.md
  - raw/papers/2026-09-04-ghost-clusters-usenix-2025.md
created: 2026-09-04
updated: 2026-09-19
tags: [dac8, blockchain, expert-evidence, reproducibility, false-positive, ground-truth, protocol]
aliases: [DAC8 linkage test, blockchain expert protocol]
confidence: high
volatility: warm
verified: 2026-09-04
summary: "Falsifiable protocol for measuring whether the actual DAC8 annual tuple or additional provider-held data can be linked to public-ledger activity without collapsing distinct attribution steps."
---

# DAC8 Blockchain-Linkage Expert-Evidence Protocol

> The expert question is not whether blockchain analysis exists. It is what the actual DAC8 fields add to identification risk, with what error, under which auxiliary-data assumptions. A result that fails to show material linkage is as important as one that succeeds.

## Competing propositions

The protocol should be fixed before inspecting the claimant's result. At minimum:

- **P1:** the actual annual DAC8 tuple materially narrows public-ledger candidates beyond public information alone;
- **P2:** it does not materially narrow them because annual aggregation, batching, fees, internal trades and common values leave many candidates or no valid mapping;
- **P3:** a verified provider-side MiCA or TFR address/transaction record creates a materially stronger anchor than the DAC8 tuple;
- **P4:** even with that anchor, cluster, entity and person attribution remain incomplete or too error-prone for the asserted conclusion.

ENFSI's framework supports competing propositions, pre-assessment, controlled methods, explicit limitations and reporting the strength of findings rather than the probability that a person owns or made a transaction.

## Ground-truth ladder

| Level | Evidence | Permissible conclusion |
|---|---|---|
| Own controlled account and addresses | provider export, own wallet records and public chain | whether the pipeline can recover a known mapping for that provider, asset and year |
| Provider-confirmed transaction record | source ledger, order and settlement data obtained lawfully | transaction-level validation, subject to batching and internal-book effects |
| Provider MiCA/TFR anchor | applicable Table 3/Table 4 or transfer record with identity and on-chain identifier | address or transaction seed, not beneficial ownership or whole-wallet attribution |
| Synthetic annual tuple | generated data with documented distribution | method behaviour only, not a rate for real users |
| Public labels without provider ground truth | published or vendor entity labels | exploratory entity attribution with label-coverage and staleness limits |

Own-account evidence can establish that a mechanism exists or fails in a defined case. It cannot estimate a population rate without an adequate independent sample.

## Ablation sequence

Each layer must be tested separately:

1. public ledger alone;
2. actual DAC8 fields only: year, asset, category, aggregate value, units and, where present, count;
3. provider identity and publicly known service clusters;
4. a short time window, only if legally available from a separate source;
5. a MiCA or TFR address or transaction identifier, only where the record exists and use is lawful;
6. cluster expansion;
7. entity attribution;
8. natural-person inference.

The incremental change at each step is the finding. Results from a later, stronger layer must not be attributed to DAC8.

## Negative controls

- provider-internal trades with no on-chain event;
- batched withdrawals and omnibus wallets;
- equal and round-valued transactions of other users;
- fees, spread and gross-versus-net differences;
- wrong year, wrong asset and wrong transaction category;
- own-account transfers;
- wrapping, bridges, collateral and loans;
- CoinJoin, PayJoin and chain-specific privacy mechanisms;
- stale labels and address reuse by a different controller.

The external-address aggregate requires special treatment because it contains no transaction count. A `count = 1` theory cannot be used for that field.

## Metrics and error separation

Report candidate-set size `k`, share of `k = 0`, share of `k = 1`, top-k recall, precision, recall, false-discovery rate, abstention rate and confidence intervals. Break results down by provider, asset, chain, category and year.

Four endpoints remain separate:

1. transaction candidate;
2. address cluster;
3. service or entity;
4. natural person.

Error compounds across those endpoints. A high transaction-match precision cannot be reported as high person-attribution precision.

## Reproducibility and preservation

- pre-register propositions, thresholds and metrics;
- freeze block height and block hash;
- hash provider exports, source records and parameter files;
- record code, dependencies, label sets and tool versions;
- preserve a complete transformation log;
- blind the analyst to truth labels where feasible;
- require an independent rerun;
- provide code and synthetic examples, while protecting personal records and addresses;
- reject an opaque commercial-tool conclusion without disclosed method, scope and measured error.

NIST SP 800-86 offers general preservation and process benchmarks. These are not substitutes for validation of the specific blockchain method.

## Stop rules

- no person-level claim without provider-specific ground truth;
- no transfer of results across chains, providers, wallet types or years not tested;
- no whole-portfolio or current-control claim from one historical address;
- no population-rate claim from one claimant's account;
- no unique-match claim if negative controls produce similar candidates;
- no result if the method was chosen or retuned after seeing the answer without clearly labelling that analysis exploratory;
- no unlawful acquisition or publication of third-party personal data to illustrate a risk;
- report a failed or non-discriminating test without reframing it as support.

## Procedural use

The protocol can be used in the DSB/BVwG fact-finding route to frame requests for the exact provider record, field map, valuation and classification method, legal basis for each auxiliary dataset and a neutral expert question. It can also falsify an overbroad public claim before it reaches a pleading.

It does not establish that the DSB or court must accept a particular methodology, that an expert result alone invalidates DAC8, or that a provider must disclose protected third-party or security material directly to the complainant.

## See Also

- [[breach-harm-and-linkage-empirics|Breach Harm and Linkage Empirics]] ([Breach Harm and Linkage Empirics](breach-harm-and-linkage-empirics.md)) — additional empirical endpoints and their input requirements.

- [[identity-to-public-ledger-linkage-evidence|Identity-to-Public-Ledger Linkage Evidence]] ([Identity-to-Public-Ledger Linkage Evidence](identity-to-public-ledger-linkage-evidence.md))
- [[dac8-inference-linkage-and-error-evidence|DAC8 Inference, Linkage and Error Evidence]] ([DAC8 Inference, Linkage and Error Evidence](dac8-inference-linkage-and-error-evidence.md))
- [[dsb-bvwg-evidence-and-interim-toolkit|DSB and BVwG Evidence and Interim-Protection Toolkit]] ([DSB and BVwG Evidence and Interim-Protection Toolkit](dsb-bvwg-evidence-and-interim-toolkit.md))

## Sources

- [ENFSI Guideline for Evaluative Reporting](https://enfsi.eu/wp-content/uploads/2016/09/m1_guideline.pdf)
- [NIST SP 800-86](https://csrc.nist.gov/pubs/sp/800/86/final)
- [When the Cookie Meets the Blockchain](https://petsymposium.org/popets/2018/popets-2018-0038.php)
- [How to Peel a Million](https://www.usenix.org/conference/usenixsecurity22/presentation/kappos)
- [Resurrecting Address Clustering in Bitcoin](https://arxiv.org/abs/2107.05749)
- [Ghost Clusters](https://www.usenix.org/system/files/usenixsecurity25-lubbertsen.pdf)
