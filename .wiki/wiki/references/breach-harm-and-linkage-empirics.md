---
title: "Breach Harm and Blockchain-Linkage Empirics"
category: reference
sources:
  - raw/papers/2026-09-19-abramova-breach-fulltext.md
  - raw/papers/2026-09-19-wang-rpc-linkage-ccs2025.md
  - raw/papers/2026-09-19-mikhed-vogan-breach-credit.md
created: 2026-09-19
updated: 2026-09-19
tags: [data-breach, blockchain, linkage, empirical-evidence, physical-security, adverse-evidence]
aliases: [Breach victim evidence, RPC linkage evidence]
confidence: medium
volatility: warm
verified: 2026-09-19
summary: "Three empirical studies distinguish reported breach harms, additional-data ledger linkage and limited credit-market effects; none establishes DAC8 attack incidence or annual-aggregate deanonymisation."
---

# Breach Harm and Blockchain-Linkage Empirics

Empirical support differs by endpoint. A victim survey can establish reported experiences, a controlled linkage experiment can demonstrate a technical mechanism, and a credit-panel study can identify changes in measured behaviour. None alone establishes the full chain from DAC8 collection through disclosure to identification and physical harm.

## Findings by endpoint

| Endpoint | Evidence | Limit for Austrian DAC8 assessment |
|---|---|---|
| Reported downstream harm | Abramova/Böhme surveyed 104 Ledger-breach respondents: two reported physical-security threats; 30 expressed moderate-to-extreme physical-safety concerns. | No verified completed assaults, representative incidence or forensic attribution of each event. |
| Additional-data linkage | Wang et al. experimentally linked observed RPC network traffic to blockchain pseudonyms, reporting 95.33% Ethereum-mainnet success under selected conditions. | Requires network visibility and precise timing; neither annual aggregates nor person identity were the tested input/output. |
| Observable financial consequences | Mikhed/Vogan found greater protective-service uptake after a US tax-data breach without corresponding deterioration in central measured credit outcomes. | US credit-market evidence, not Austrian crypto-risk evidence; does not exclude unmeasured harms. |

## What these studies add

The [Ledger full-text digest](../../raw/papers/2026-09-19-abramova-breach-fulltext.md) narrows the existing abstract evidence. About 31,632 invitations yielded 104 retained responses. Selection and reporting limits prohibit extrapolating the reported threats to exposed customers generally. Ten respondents reported financial losses after the breach, but only four themselves regarded a connection as likely or very likely. Chronology and self-attribution remain distinct from demonstrated causation.

The [RPC study](../../raw/papers/2026-09-19-wang-rpc-linkage-ccs2025.md) adds a contemporary mechanism beyond older web-payment research. Its controlled setup included 90 emulated users and 1,099 Ethereum-testnet transactions, plus 100 Ethereum-mainnet transactions. Its experimentally obtained percentages should not be transferred to Bitcoin/Solana mainnet, which were not experimentally tested, or to an attacker possessing only a tax report. An IP-to-pseudonym link still requires separate evidence before identifying a person or attributing ownership.

The [US tax-breach study](../../raw/papers/2026-09-19-mikhed-vogan-breach-credit.md) supplies a necessary counterweight: disclosure need not produce a detectable deterioration in every financial outcome. Its panel observations are not unique victims, and its outcome measures do not resolve physical-security or nonfinancial harms. US remedial institutions and credit practices cannot be presumed equivalent to Austria's.

## Remaining proof gaps

These studies provide no representative crypto-attack incidence, verified breach-caused physical assaults, DAC8-specific incremental risk or proof of annual-aggregate deanonymisation. They also do not quantify the long-term harm of a durable identity-to-ledger anchor. The actual annual tuple still needs a separate, ground-truthed test; additional provider or network data must be declared rather than silently included.

## See Also

- [[identity-to-public-ledger-linkage-evidence|Identity-to-Public-Ledger Linkage Evidence]] ([Linkage evidence](identity-to-public-ledger-linkage-evidence.md))
- [[dac8-physical-risk-causation|DAC8 Physical-Risk Causation and Evidence]] ([Physical-risk evidence](dac8-physical-risk-causation.md))
- [[dac8-blockchain-linkage-expert-evidence-protocol|DAC8 Blockchain-Linkage Expert-Evidence Protocol]] ([Expert-evidence protocol](dac8-blockchain-linkage-expert-evidence-protocol.md))

## Sources

- [Abramova/Böhme: full-text clarification](../../raw/papers/2026-09-19-abramova-breach-fulltext.md)
- [Wang et al.: controlled RPC linkage](../../raw/papers/2026-09-19-wang-rpc-linkage-ccs2025.md)
- [Mikhed/Vogan: US tax breach and credit outcomes](../../raw/papers/2026-09-19-mikhed-vogan-breach-credit.md)
