---
title: "DAC8 Physical-Risk Causation and Evidence"
category: reference
sources:
  - raw/articles/2026-09-04-ecthr-kurt-austria-physical-risk-threshold.md
  - raw/papers/2026-09-04-ordekian-wrench-attacks-aft-2024.md
  - raw/articles/2026-09-04-eu-delegated-regulation-2025-1140-mica-records.md
  - raw/articles/2026-08-27-edpb-blockchain-guidelines-02-2025-final.md
  - raw/articles/2026-09-04-cjeu-c340-21-tax-authority-breach-security.md
  - raw/articles/2026-09-04-coinbase-2025-data-theft-8k.md
  - raw/articles/2026-09-04-france-dgfip-tax-data-breach.md
  - raw/articles/2026-09-04-france-ficoba-account-register-breach.md
created: 2026-09-04
updated: 2026-09-04
tags: [dac8, krypto-mpfg, physical-security, causation, blockchain, evidence]
aliases: [DAC8 wrench-attack risk, crypto tax data physical risk]
confidence: medium
volatility: hot
verified: 2026-09-04
summary: "Causal-chain and evidence-gate analysis treating physical harm as a proportionality severity factor rather than an unsupported standalone Article 2 claim."
---

# DAC8 Physical-Risk Causation and Evidence

> Physical coercion against crypto holders is an established threat class. No located evidence shows that a DAC8 or tax-reporting dataset caused such an attack. The legally usable point is a concrete severity and security factor, not a proven causal consequence of the statute.

## What the reporting layer establishes

The routine DAC8 report links identity and address information to annual per-asset and per-category values, units and usually counts. It does not report a current holding or balance, wallet address, transaction identifier, transaction timestamp or counterparty. Activity values can suggest economic scale but do not establish current wealth, custody, key control or access to funds.

A provider may separately hold identity-to-ledger anchors under MiCA or TFR. Those records are not part of the DAC8 payload. Any enhanced physical-risk theory must prove their existence for the person, the legal and technical join, the persons able to access it and the inference actually made.

## Causal ladder

| Link | Current evidence status | Required proof |
|---|---|---|
| Crypto holders face physical coercion | Supported as a real threat class by the peer-reviewed AFT 2024 study | No DAC8 inference follows from threat existence alone |
| Identity plus address plus activity values can aid target selection | Plausible security inference | Exact report, meaning of address field, activity-to-wealth uncertainty, attacker utility and competing public information |
| Provider-held ledger anchors increase persistence of disclosure | Institutionally supported by EDPB persistence and future-linkage analysis | Actual MiCA/TFR record, join path, access authority and expert test |
| Tax or provider systems can be breached | Supported as a general incident path | Concrete Austrian or relevant-controller architecture and control effectiveness |
| A DAC8 breach causes target selection or attack | Not established | Incident-specific provenance, attacker access, use of the data, victim selection and counterfactual causation |
| Authorities owe an Article 2 operational protection duty | Only claimant-specific under *Kurt* | Real and immediate risk to an identified person known or knowable to authorities and reasonable available measures |

Ordekian and co-authors identified public exposure, personal proximity, investigation and peer-to-peer encounters as observed targeting channels. They did not identify leaked tax data. That negative finding must remain visible.

## Proper legal use

For a general Krypto-MPfG or DAC8 challenge, physical risk can increase the seriousness of identity-linked financial processing when assessing:

- field and address necessity under Charter Articles 7, 8 and 52(1) and section 1 DSG;
- access compartmentalisation, bulk-export rights, insider controls, monitoring and incident response under GDPR Article 32 and DAC Articles 21 and 25;
- provider and authority retention, because exposure duration affects the opportunity window;
- whether claimant-specific urgency and irreparability support a narrow interim restriction.

Article 2 ECHR should not be presented as a standalone facial-invalidity theory on generalized risk. *Kurt* requires a real and immediate risk to an identified individual before the operational positive duty arises. A documented threat record, police risk assessment, prior attack or exposure may be legally different from an ordinary user's generalized concern.

## Evidence file

1. The exact current or planned personal dataset and whether the recorded address is an actual residence or another contact address.
2. Provider-side MiCA, TFR or operational records linking identity to addresses, hashes or precise timestamps.
3. Access, export, contractor, administrator and recipient roles for each data copy.
4. Concrete threat intelligence or claimant-specific incidents, not sector-wide headlines alone.
5. A red-team assessment of what an attacker can infer from the DAC8 payload alone and after each additional verified data layer.
6. Control-effectiveness evidence: MFA, least privilege, segmentation, anomaly detection, immutable logs, incident response, deletion and backup testing.
7. Causal evidence for any alleged leak-to-harm sequence, with alternative target-selection explanations.

## Claims to exclude

- DAC8 reports wallets, hashes, individual transaction timestamps, counterparties or balances;
- annual activity values prove current accessible wealth;
- a verified ledger address proves current ownership or key control;
- any financial-data breach proves Austrian DAC8 controls are inadequate;
- a tax or DAC8 database has already been shown to cause crypto kidnappings;
- physical harm is inevitable or categorically greater than for every conventional asset record;
- the general threat class alone meets the *Kurt* Article 2 threshold.

## See Also

- [[identity-to-public-ledger-linkage-evidence|Identity-to-Public-Ledger Linkage Evidence]] ([Identity-to-Public-Ledger Linkage Evidence](identity-to-public-ledger-linkage-evidence.md))
- [[dac8-blockchain-linkage-expert-evidence-protocol|DAC8 Blockchain-Linkage Expert-Evidence Protocol]] ([DAC8 Blockchain-Linkage Expert-Evidence Protocol](dac8-blockchain-linkage-expert-evidence-protocol.md))
- [[financial-data-breach-and-security-authorities|Financial-Data Breach and Security Authorities]] ([Financial-Data Breach and Security Authorities](financial-data-breach-and-security-authorities.md))
- [[dac8-security-architecture-and-audit-evidence|DAC8 Security Architecture and Audit Evidence]] ([DAC8 Security Architecture and Audit Evidence](dac8-security-architecture-and-audit-evidence.md))

## Sources

- [ECtHR Kurt v Austria](../../raw/articles/2026-09-04-ecthr-kurt-austria-physical-risk-threshold.md)
- [Ordekian et al., Investigating Wrench Attacks](../../raw/papers/2026-09-04-ordekian-wrench-attacks-aft-2024.md)
- [CJEU C-340/21](../../raw/articles/2026-09-04-cjeu-c340-21-tax-authority-breach-security.md)
- [EDPB blockchain guidance](../../../legal-docs/supporting/eu-edpb-guidelines-02-2025-blockchain-v2.pdf)
- [MiCA provider records](../../raw/articles/2026-09-04-eu-delegated-regulation-2025-1140-mica-records.md)
