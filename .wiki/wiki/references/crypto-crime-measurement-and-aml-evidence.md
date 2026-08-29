---
title: "Crypto-Crime Measurement and AML Evidence"
category: reference
sources:
  - raw/papers/2026-08-29-fatf-va-vasp-targeted-update-2026.md
  - raw/papers/2026-08-29-europol-crypto-criminal-finances-2022.md
  - raw/papers/2026-08-29-us-treasury-nmlra-2024-virtual-assets.md
  - raw/papers/2026-08-29-nershi-crypto-threshold-avoidance.md
  - raw/papers/2026-08-29-foley-illegal-bitcoin-activity-2019.md
  - raw/papers/2026-08-29-makarov-schoar-bitcoin-market-2021.md
  - raw/articles/2026-08-29-chainalysis-crypto-crime-2026.md
  - raw/articles/2026-08-29-trm-crypto-crime-2026.md
  - raw/articles/2026-08-29-fatf-austria-mutual-evaluation-2026.md
created: 2026-08-29
updated: 2026-08-29
tags: [crypto-assets, crime, money-laundering, kyc, travel-rule, measurement, blockchain-analysis]
aliases: [Crypto crime statistics, Travel Rule effectiveness, illicit crypto measurement]
confidence: medium
volatility: hot
verified: 2026-08-29
summary: "Known illicit activity is a minority of attributed on-chain volume but a large absolute lower bound; estimates depend on labels, coverage and denominators, and evidence is stronger for investigative utility than aggregate crime reduction."
---

# Crypto-Crime Measurement and AML Evidence

## Core finding

Neither “crypto is mostly crime” nor “crypto crime is negligible” survives a method check.

Europol's 2022 EU assessment describes crypto as a limited part of the wider criminal economy, while the US Treasury's 2024 US assessment places virtual-asset laundering far below fiat and conventional methods. Neither supplies a current global percentage. Commercial on-chain series place known or attributed illicit activity around one percent of their respective denominators: below one percent for Chainalysis and 1.2 percent for TRM in their 2025 series. These are not directly comparable measures.

Known-address vendor estimates are lower bounds that omit unidentified activity. Model-based estimates such as Foley have two-sided uncertainty and can over- or under-estimate. Neither type covers every internal exchange ledger, privacy system, fiat leg or offence in which crypto is only one component.

## Minimum metadata for every crime percentage

| Field | Required question |
|---|---|
| numerator | known illicit addresses, attributed clusters, victim loss, stolen assets, proceeds received or layered volume? |
| denominator | raw on-chain transfers, adjusted economic activity, exchange activity, liquidity, payments, users or transaction value? |
| coverage | which chains, tokens, bridges, privacy systems and dates? |
| visibility | what internal-ledger, off-chain, cash and fiat activity is excluded? |
| attribution | conviction, official designation, victim report, vendor label or proprietary heuristic? |
| revision | initial estimate or later value after new address labels? |
| unit | transaction count, value, user share, proceeds, victim harm or repeated layering flows? |

A falling percentage can coexist with rising illicit dollars. A small transaction share is not a small share of offences or harm. A large share in an early Bitcoin or darknet sample is not an all-crypto market share.

## Evidence matrix

| Evidence | Narrow finding | What it does not establish |
|---|---|---|
| Europol 2022 | crypto use spans crime types but remains a limited part of the wider criminal economy; measurement is difficult | a current EU crime percentage |
| US Treasury NMLRA 2024 | virtual-asset laundering remains far below fiat and conventional methods in the US risk assessment | a global apples-to-apples transaction ratio |
| FATF 2026 targeted update | 91 of 109 responding jurisdictions reported Travel Rule legislation; 55 of those 91 reported no findings, directives, enforcement or other supervisory action focused on Travel Rule compliance | data quality, interoperability, investigative use or crime reduction; responses were self-reported and the question denominator was not the entire FATF network |
| Foley et al. 2019 | early Bitcoin through 2017: about 46 percent of transaction count, 23 percent of value and 26 percent of users associated with illegal activity | current all-crypto share; interchangeability of count, value and users |
| Makarov and Schoar 2021 | illegal, scam and gambling activity below three percent of measured Bitcoin volume in 2020, with exchange activity dominating the denominator | peer-reviewed current all-crypto crime rate |
| Nershi | increased activity just below a USD 1,000 screening threshold at BVI exchanges after implementation | avoidance of originator/beneficiary data transfer, criminal purpose, total compliance or aggregate crime effect |
| Chainalysis 2026 | at least USD 154 billion received by vendor-attributed illicit or sanctioned addresses/entities in 2025; attributed share below one percent | money-laundering volume, criminal proceeds, victim harm, unidentified addresses, full off-chain activity or an official total |
| TRM 2026 | approximately USD 158 billion incoming to attributed illicit wallets/entities in 2025; 1.2 percent of attributed on-chain volume and 2.7 percent of incoming VASP flows | money-laundering volume, criminal proceeds, direct comparability with another vendor or a final non-revisable value |
| FATF Austria 2026 | only moderate effectiveness for financial intelligence, investigation/prosecution and confiscation despite improved infrastructure | that a particular KYC or TFR field has no value |

The apparent conflict between Foley and Makarov/Schoar largely reflects time, attribution and denominator. Foley's 46 percent is transaction count while 23 percent is value; Makarov/Schoar include large exchange/service flows. Reporting one number without its unit creates a false comparison.

## KYC and Travel Rule effect chain

`identity or transfer data → investigative lead → freeze, seizure or disruption → deterrence → lower aggregate crime`

- Evidence exists separately for the first three stages, but the causal linkage from a particular KYC or Travel Rule field through that chain is generally not established. The evidence remains predominantly operational and case-based rather than causal.
- KYC can connect a customer record to on-chain activity and support attribution, but stolen identities, mules, nested accounts and weak verification limit reliability.
- The Travel Rule adds originator and beneficiary data only when covered intermediaries participate and implement interoperable, accurate systems.
- Centralised exchanges, banks and stablecoin issuers can provide identity, conversion, redemption, freeze and seizure points.
- Evidence that these controls cause a reduction in aggregate laundering or predicate crime remains limited.

Travel Rule legislation is therefore an implementation measure, not an outcome. FATF's 2026 adoption percentage must not be presented as a success rate.

## Displacement and friction

Control at regulated interfaces can shift activity toward offshore or no-KYC VASPs, OTC brokers, P2P transfers, DeFi, bridges, mixers, chain-hopping, mules, underground banking, cash and wires. The US Treasury and FATF reports document these channels; Nershi supplies direct evidence of transaction bunching around a screening threshold, without establishing criminal purpose or Travel Rule data-transfer avoidance.

Displacement is not automatically complete failure. Added cost, lower liquidity, loss of trusted intermediaries, traceable errors and seizure risk can create friction. The net effect is rarely measured against a credible counterfactual.

## Commercial-estimate rule

Chainalysis and TRM are useful current measurement series, not neutral official statistics. Similar headline amounts are not independent confirmation because both depend on proprietary attribution and may classify sanctioned or state-aligned entities without treating the amount as criminal proceeds. For every use record:

`vendor; as-of date; numerator; denominator; chain coverage; known/unknown boundary; initial or revised estimate`

Vendor labels can also feed FATF and official risk reports. That reuse does not independently validate the underlying attribution.

## Claims to avoid

- “Crypto is mainly used for crime.”
- “Less than one percent means crypto crime is negligible.”
- “Public blockchains reveal all criminal activity.”
- “Foley found that 46 percent of current crypto value is illegal.”
- “Travel Rule adoption proves effectiveness.”
- “KYC prevents identity abuse and mule accounts.”
- “Displacement proves no control has value.”
- “Vendor crime reports are official or directly comparable.”

## Relevance to the Austrian proceeding

Crypto-crime evidence can support a legitimate public interest and explain regulated chokepoints. It does not answer whether the incremental Krypto-MPfG tax processing of a particular person, field, transaction class or retention period is necessary and proportionate.

The correct comparison isolates what FM-GwG, TFR and MiCA already require before attributing an additional benefit or burden to DAC8 and section 20 Krypto-MPfG.

## See Also

- [[aml-kyc-effectiveness-evidence|AML and KYC Effectiveness Evidence]] ([AML and KYC Effectiveness Evidence](aml-kyc-effectiveness-evidence.md))
- [[eu-aml-crypto-regulatory-stack|EU AML Crypto Regulatory Stack]] ([EU AML Crypto Regulatory Stack](../topics/eu-aml-crypto-regulatory-stack.md))
- [[mica-tfr-krypto-mpfg-nexus|MiCA, TFR, and the Krypto-MPfG Nexus]] ([MiCA, TFR, and the Krypto-MPfG Nexus](../topics/mica-tfr-krypto-mpfg-nexus.md))

## Sources

- [FATF VA/VASP targeted update](../../raw/papers/2026-08-29-fatf-va-vasp-targeted-update-2026.md)
- [Europol crypto spotlight](../../raw/papers/2026-08-29-europol-crypto-criminal-finances-2022.md)
- [US Treasury NMLRA](../../raw/papers/2026-08-29-us-treasury-nmlra-2024-virtual-assets.md)
- [Nershi threshold study](../../raw/papers/2026-08-29-nershi-crypto-threshold-avoidance.md)
- [Foley et al.](../../raw/papers/2026-08-29-foley-illegal-bitcoin-activity-2019.md)
- [Makarov and Schoar](../../raw/papers/2026-08-29-makarov-schoar-bitcoin-market-2021.md)
- [Chainalysis 2026](../../raw/articles/2026-08-29-chainalysis-crypto-crime-2026.md)
- [TRM 2026](../../raw/articles/2026-08-29-trm-crypto-crime-2026.md)
- [FATF Austria Mutual Evaluation](../../raw/articles/2026-08-29-fatf-austria-mutual-evaluation-2026.md)
