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
  - raw/articles/2026-09-19-gendarmerie-waltio-target-selection.md
  - raw/articles/2026-09-19-gendarmerie-haute-garonne-crypto-extortion.md
  - raw/articles/2026-09-19-doj-st-felix-crypto-home-invasions.md
  - raw/articles/2026-09-19-doj-ferro-crypto-burglary.md
  - raw/articles/2026-09-19-bobigny-tax-insider-le-parisien.md
  - raw/articles/2026-09-19-bobigny-tax-insider-protos.md
  - raw/articles/2026-09-19-coinbase-insider-social-engineering-disclosure.md
  - raw/papers/2026-09-19-abramova-boehme-wallet-breach-aftermath.md
  - raw/papers/2026-09-19-abramova-breach-fulltext.md
  - raw/articles/2026-09-19-saavedra-plea-location-abuse.md
  - raw/articles/2026-09-19-doj-iza-saavedra-location-attack.md
  - raw/articles/2026-09-19-doj-saavedra-plea-status.md
  - raw/articles/2026-09-19-france-dgfip-wallet-risk-debate.md
created: 2026-09-04
updated: 2026-09-19
tags: [dac8, krypto-mpfg, physical-security, causation, blockchain, evidence]
aliases: [DAC8 wrench-attack risk, crypto tax data physical risk]
confidence: medium
volatility: hot
verified: 2026-09-19
summary: "Causal-chain and evidence-gate analysis treating physical harm as a proportionality severity factor rather than an unsupported standalone Article 2 claim."
---

# DAC8 Physical-Risk Causation and Evidence

> Physical coercion against crypto holders is an established threat class. French police now expressly attribute criminal target selection to leaked Waltio data. That is evidence concerning a private crypto-tax service, not proof that a DAC8 dataset caused an attack. The legally usable point remains a concrete severity and security factor, not a proven causal consequence of the statute.

The 19 September update checks incident evidence. Existing legal-authority analysis retains its 4 September verification scope.

## What the reporting layer establishes

The routine DAC8 report links identity and address information to annual per-asset and per-category values, units and usually counts. It does not report a current holding or balance, wallet address, transaction identifier, transaction timestamp or counterparty. Activity values can suggest economic scale but do not establish current wealth, custody, key control or access to funds.

A provider may separately hold identity-to-ledger anchors under MiCA or TFR. Those records are not part of the DAC8 payload. Any enhanced physical-risk theory must prove their existence for the person, the legal and technical join, the persons able to access it and the inference actually made.

## Causal ladder

| Link | Current evidence status | Required proof |
|---|---|---|
| Crypto holders and relatives face physical coercion | AFT 2024 study and official DOJ accounts of convictions | No DAC8 inference follows from threat existence alone |
| Leaked crypto-service data aid criminal target selection | Express Gendarmerie attribution concerning Waltio, September 2026 | Case-level provenance and extent remain unpublished; private tax service is not a tax authority |
| Misused official location access can facilitate an armed crypto-targeted attack | Saavedra plea factual basis establishes location abuse; DOJ separately describes the subsequent attempted home invasion | Police powers and fraudulently procured GPS access, not a tax-database leak |
| DAC8 identity, address and activity fields could aid target selection | Security inference, strengthened but not proved by adjacent incidents | Exact report, address meaning, activity-to-wealth uncertainty and competing information |
| Provider-held ledger anchors increase persistence of disclosure | Institutionally supported by EDPB persistence and future-linkage analysis | Actual MiCA/TFR record, join path, access authority and expert test |
| Tax or provider systems can be breached | Supported as a general incident path | Concrete Austrian or relevant-controller architecture and control effectiveness |
| A DAC8 breach causes target selection or attack | Not established | Incident-specific provenance, attacker access, use of the data, victim selection and counterfactual causation |
| Authorities owe an Article 2 operational protection duty | Only claimant-specific under *Kurt* | Real and immediate risk to an identified person known or knowable to authorities and reasonable available measures |

Ordekian and co-authors identified public exposure, personal proximity, investigation and peer-to-peer encounters as observed targeting channels. Their 2024 study did not identify leaked tax data; that limit cannot negate later evidence.

## Incident evidence and misuse mechanisms

- **Waltio:** official police attribution includes mistakes about actual holdings. It is stronger than a hypothetical threat model, but not a published causal judgment. See the [source digest](../../raw/articles/2026-09-19-gendarmerie-waltio-target-selection.md).
- **Haute-Garonne:** an official armed-extortion investigation refers to apparently hacked personal data without identifying the originating leak. [Source](../../raw/articles/2026-09-19-gendarmerie-haute-garonne-crypto-extortion.md).
- **St Felix and Ferro:** official sentencing accounts establish physical attacks on holders and relatives, and an enterprise combining digital targeting with burglary. They do not identify DAC8 data. [St Felix](../../raw/articles/2026-09-19-doj-st-felix-crypto-home-invasions.md), [Ferro](../../raw/articles/2026-09-19-doj-ferro-crypto-burglary.md).
- **Bobigny:** original reporting concerns alleged tax-insider assistance to an attack on a prison officer. The derivative account adds the wife's involvement. Searches about crypto investors are not proof of attacks on those investors. Neither guilt nor a final disposition was verified. [Original-report limits](../../raw/articles/2026-09-19-bobigny-tax-insider-le-parisien.md), [derivative account](../../raw/articles/2026-09-19-bobigny-tax-insider-protos.md).
- **Saavedra/Iza:** the [plea factual basis](../../raw/articles/2026-09-19-saavedra-plea-location-abuse.md), Exhibit A paragraphs 21–27, admits fraudulent GPS access and locating the victim. The [DOJ announcement](../../raw/articles/2026-09-19-doj-iza-saavedra-location-attack.md) describes the subsequent armed attempt. A [September update](../../raw/articles/2026-09-19-doj-saavedra-plea-status.md) confirms Saavedra's February 2025 guilty plea. This is stronger insider evidence than the accessible Bobigny reporting, but no tax-data or DAC8 incident. General police-database misuse and the GPS-derived address must remain distinct.
- **Coinbase:** its disclosure acknowledges impersonation losses despite no stolen private keys. This supports indirect harm, not physical-attack causation. [Source](../../raw/articles/2026-09-19-coinbase-insider-social-engineering-disclosure.md).
- **Victim research:** a 104-person USENIX survey includes two reported physical threats and 30 respondents with moderate-to-extreme physical-safety concerns. The [full-text supplement](../../raw/papers/2026-09-19-abramova-breach-fulltext.md) establishes neither verified assaults nor a representative attack probability; the earlier [abstract extraction](../../raw/papers/2026-09-19-abramova-boehme-wallet-breach-aftermath.md) remains provenance.

Target selection and locating a victim do not require an exposed wallet address or private key. A later coerced transfer is a separate attack stage. Linking identity to public-ledger history, by contrast, requires an additional verified anchor; annual DAC8 aggregates alone do not establish it. Fraudulent impersonation, burglary and coercion should not be collapsed into one causal claim.

An offender's mistaken belief about accessible wealth can create danger even when the underlying data do not prove current holdings. This is not evidence that all reported users face equal risk, nor a measured incremental effect of DAC8. Incident counts without consistent definitions, exposed-population denominators and alternative explanations cannot provide that estimate.

## Institutional recognition and limits

The [[european-data-misuse-and-physical-risk|European evidence supplement]] ([European evidence supplement](european-data-misuse-and-physical-risk.md)) adds Dutch insider convictions, Finnish breach-related extortion, EDPB prospective risk guidance and pending C-609/26. It separates actual extortion from unproved attack connections and statutory access exceptions from confidential authority access. These additions do not establish DAC8-specific causation.

The [French parliamentary record](../../raw/articles/2026-09-19-france-dgfip-wallet-risk-debate.md) records Labaronne quoting a DGFiP warning about centralising identity and asset-value information. It concerns additional self-hosted-wallet declarations and fraud risk. The minister expressly favours DAC8. This supports scrutiny of specific data combinations, not a claim that the French administration rejected DAC8 or established physical harm.

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
- Waltio is a state tax database, or a DAC8 database has already been shown to cause crypto kidnappings;
- Bobigny establishes convictions, a verified price per data record, or attacks on the crypto investors whose records were reportedly searched;
- physical harm is inevitable or categorically greater than for every conventional asset record;
- the general threat class alone meets the *Kurt* Article 2 threshold.

## See Also

- [[data-risk-prevention-and-damages-thresholds|Data-Risk Prevention and Damages Thresholds]] ([Data-Risk Prevention and Damages Thresholds](data-risk-prevention-and-damages-thresholds.md))
- [[breach-harm-and-linkage-empirics|Breach Harm and Linkage Empirics]] ([Breach Harm and Linkage Empirics](breach-harm-and-linkage-empirics.md)) — full-text victim research and adverse economic evidence.

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
