---
title: "EU AML Crypto Regulatory Stack"
category: topic
sources:
  - raw/articles/2026-08-29-fatf-history-and-mandate.md
  - raw/articles/2026-08-29-fatf-virtual-assets-standard-2019.md
  - raw/papers/2026-08-29-fatf-va-vasp-targeted-update-2026.md
  - raw/articles/2026-08-29-oecd-carf-2022.md
  - raw/articles/2026-08-27-eu-directive-2023-2226-dac8.md
  - raw/articles/2026-08-27-eu-amlr-regulation-2024-1624.md
  - raw/articles/2026-08-27-eu-amla-regulation-2024-1620.md
  - raw/articles/2026-08-27-eu-amld4-amld5-transition.md
  - raw/articles/2026-08-27-eu-criminal-amld6-2018-1673.md
  - raw/articles/2026-08-27-eu-amld6-2024-1640-system.md
  - raw/articles/2026-08-27-eu-tfr-regulation-2023-1113.md
  - raw/articles/2026-08-27-eu-directive-2019-1153-financial-info.md
  - raw/articles/2026-08-27-eu-asset-recovery-directive-2024-1260.md
  - raw/articles/2026-08-27-eu-directive-2026-799-insolvency-baris-access.md
created: 2026-08-27
updated: 2026-08-29
tags: [eu, aml, amlr, amla, casp, self-hosted-address, baris, crypto-assets]
aliases: [EU AML package for crypto, AMLD6 crypto, AMLR CASPs]
confidence: high
volatility: hot
verified: 2026-08-27
summary: "The EU crypto AML stack is a staged system: current AMLD4/5 national law and TFR, future direct AMLR duties, AMLA supervision, national AMLD6 mechanisms, BARIS, and separate criminal asset-recovery powers."
---

# EU AML Crypto Regulatory Stack

> In 2026, the mistake is to describe the entire 2024 AML package as already applicable. TFR and national AMLD4/5 implementations operate now; most AMLR and recast AMLD6 rules arrive in 2027, while BARIS interconnection follows in 2029.

## Where the crypto layer came from

AMLD5 brought limited fiat/crypto exchange and custody activity into EU AML law in May 2018, before FATF completed its October 2018 and June 2019 virtual-asset revisions. TFR recital 6 is the clearest express EU translation of FATF's June 2019 Recommendations 15 and 16 framework. The resulting provider duty comes from EU law, not directly from the FATF standard.

CARF and DAC8 have a separate OECD tax-transparency lineage. Reuse of AML customer data does not convert DAC8 due diligence or reporting into AML law. See [[international-aml-cdd-crypto-genealogy|International AML, CDD and Crypto-Regime Genealogy]] ([article](../references/international-aml-cdd-crypto-genealogy.md)).

## Which instrument does what?

| Instrument | Function | Status on 27 August 2026 |
|---|---|---|
| AMLD4, Directive 2015/849 as amended | national CDD, FIU, reporting, beneficial-ownership, and account-mechanism framework | operative until repeal on 10 July 2027 |
| AMLD5, Directive 2018/843 | brought exchange and custody providers into AML and expanded registers and FIU access | embedded in the current AMLD4 framework |
| Criminal AMLD6, Directive 2018/1673 | harmonised money-laundering offences and legal-person liability | operative criminal-law instrument |
| TFR, Regulation 2023/1113 | identity and traceability information for CASP-involved crypto transfers | directly applicable since 30 December 2024 |
| AMLA, Regulation 2024/1620 | EU supervision, convergence, FIU support, joint analysis, and a supervisory database | generally applicable since 1 July 2025 |
| AMLR, Regulation 2024/1624 | single directly applicable private-sector AML rulebook | in force; generally applies from 10 July 2027 |
| Recast AMLD6, Directive 2024/1640 | national FIUs, supervisors, ownership registers, account mechanisms, and sanctions | staged transposition; general deadline 10 July 2027 |
| Directive 2019/1153 as amended | designated criminal-authority access to account and financial information | operative; cross-border BARIS changes staged to 2029 |
| Asset Recovery Directive 2024/1260 | tracing, freezing, and confiscation, including crypto-assets | transposition due 23 November 2026 |

The two instruments commonly called “AMLD6” are different. Directive 2018/1673 is criminal law. Directive 2024/1640 is the institutional and national-mechanisms companion to AMLR.

## What applies to a CASP now?

TFR applies whenever at least one CASP participates in the transfer. It requires defined originator and beneficiary information, risk-based handling of missing information, five-year retention, and assessment of ownership or control for transfers above EUR 1,000 to or from a self-hosted address.

Three limits matter:

1. Article 2 excludes a person-to-person transfer with no CASP.
2. “Self-hosted address” describes an address not linked to a CASP or equivalent non-Union intermediary. It is not a legal category of prohibited wallet.
3. Originator and beneficiary information is required for a CASP-involved self-hosted transfer regardless of value. The EUR 1,000 rule is only the additional ownership-or-control assessment trigger; it is not a travel-rule threshold, automatic suspicious report, or one mandatory technical proof method.

Current AMLD4 Article 19a and future AMLR Article 40 add risk-based controls for self-hosted transfers. AMLR Article 79 prohibits anonymous or anonymising accounts maintained by obliged entities. It does not prohibit private self-custody.

## The 2027 AMLR baseline

For CASPs, AMLR Article 19 requires full CDD for occasional transactions at or above EUR 1,000 and at least identity verification below that threshold. Article 20 adds beneficial-owner identification, relationship purpose, customer business and risk profile, sanctions checks, and ongoing monitoring.

Article 76 permits special-category and conviction data only where strictly necessary and supplies accuracy, security, human-intervention, explanation, and challenge safeguards for covered processing and profiling. Article 77 fixes five years for CDD, risk, transaction, suspicious-report, and partnership records. A competent authority can require up to five additional years only case by case where necessary for AML/CFT; other GDPR-compliant retention bases and pending-proceeding rules remain relevant.

That future five-year baseline is a useful comparator for national ten-year rules. It does not itself invalidate those rules before 2027 or where another valid legal basis applies.

## BARIS and crypto-account discovery

Recast AMLD6 Article 16 requires national central mechanisms that identify bank, payment, securities, crypto-asset account, and safe-deposit relationships held by credit or financial institutions. Mandatory fields include holder, proxy, and beneficial-owner identity, a unique account identifier, and opening and closing dates. Article 16(6) requires interconnection through BARIS by 10 July 2029. National extra fields under Article 16(5) do not enter BARIS. Article 16(8) uses five years after closure plus a specific necessary and proportionate extension of up to five years.

This is account discovery, not an EU register of every blockchain address. The legal text leaves an implementation seam: TFR defines a crypto-asset account as an account held by a CASP, while Article 16 is framed through accounts held by credit or financial institutions. National transposition and technical standards will determine the practical perimeter.

Article 21 gives FIUs immediate and direct access to the central mechanisms and defined administrative, tax, transfer, law-enforcement, and obliged-entity information. Directive 2019/1153 as amended creates case-specific serious-crime access by designated criminal authorities. Directive 2026/799 adds a future case-specific insolvency route through designated courts or administrative authorities on an insolvency practitioner's request. Those channels have different purposes and safeguards and must not be collapsed.

Recast AMLD6 Article 18 separately requires national real-estate access points by 10 July 2029, exposing ownership, acquisition price, encumbrances, and ownership/price history to competent authorities. This expands asset discovery but still does not create one unified EU net-worth register.

## AMLA is not universal direct supervision

AMLA can directly supervise selected high-risk, cross-border financial entities. Selection is not automatic for every CASP. National supervisors remain responsible for non-selected entities.

AMLA also maintains a central database of supervisory information and supports FIU cooperation and joint analysis. Those functions increase interoperability risk, but the Regulation confines sharing to statutory tasks, need-to-know use, and confidentiality. A rights challenge needs the actual information, recipient, access, retention, and remedy path—not the word “database” alone.

## Separate purposes that can touch the same person

| Layer | Main legal purpose | Typical record |
|---|---|---|
| MiCA | authorisation, supervision, market integrity, client protection | services, activities, orders, and transactions |
| TFR | AML/CFT traceability | originator, beneficiary, account/address, and transfer identifiers |
| AMLR/FM-GwG | customer risk and suspicious-activity prevention | CDD, beneficial ownership, risk profile, monitoring, STR record |
| DAC8/Krypto-MPfG | tax transparency and exchange | tax identity and annual reportable crypto aggregates |
| BARIS/account mechanisms | relationship discovery | institution, account holder, type, and opening/closing metadata |
| Asset recovery | criminal tracing, freezing, and confiscation | case-specific asset and transfer information |

Operational reuse does not erase purpose, access, retention, and remedy boundaries. Conversely, the campaign must acknowledge that Directive 2011/16/EU Article 16 expressly permits defined DAC information reuse for AML/CFT. The legally testable question is whether each additional access or linkage stays within its enacted purpose and safeguards.

## Litigation implications

For the current Austrian Krypto-MPfG challenge, AML is mostly a baseline and counterfactual problem:

- subtract records and costs that the provider already needs for FM-GwG, TFR, and MiCA;
- isolate tax-specific processing of section 18 fields for reliably non-reportable users;
- do not attack future AMLR or BARIS rules before their national implementation creates a direct effect;
- use different retention baselines to demand a field-by-field legal basis, not to claim automatic invalidity.

Future AML implementation becomes separately reviewable where Austria enacts concrete account fields, users, access tiers, retention, sanctions, or remedies that exceed the EU floor.

FATF reported Travel Rule legislation in 91 of 109 responding jurisdictions in 2026, but 55 of those 91 reported no findings, directives, enforcement or other supervisory action focused on Travel Rule compliance. The data were self-reported and the question did not cover the entire FATF network. This is an implementation gap, not an estimate of prevention or crime reduction. The measurement limits are collected in [[crypto-crime-measurement-and-aml-evidence|Crypto-Crime Measurement and AML Evidence]] ([article](../references/crypto-crime-measurement-and-aml-evidence.md)).

## Claims to avoid

- “The EU has banned self-hosted wallets.”
- “Every P2P transaction carries identity data.”
- “AMLR has applied in full since 2024.”
- “BARIS is an EU database of all wallet addresses and balances.”
- “AMLA directly supervises every exchange.”
- “All AML, MiCA, TFR, and DAC8 data are freely interchangeable.”

## See Also

- [[international-aml-cdd-crypto-genealogy|International AML, CDD and Crypto-Regime Genealogy]] ([International AML, CDD and Crypto-Regime Genealogy](../references/international-aml-cdd-crypto-genealogy.md))
- [[crypto-crime-measurement-and-aml-evidence|Crypto-Crime Measurement and AML Evidence]] ([Crypto-Crime Measurement and AML Evidence](../references/crypto-crime-measurement-and-aml-evidence.md))
- [[austrian-aml-crypto-implementation|Austrian AML Crypto Implementation]] ([Austrian AML Crypto Implementation](austrian-aml-crypto-implementation.md))
- [[aml-financial-intelligence-and-fundamental-rights|AML Financial Intelligence and Fundamental Rights]] ([AML Financial Intelligence and Fundamental Rights](aml-financial-intelligence-and-fundamental-rights.md))
- [[mica-tfr-krypto-mpfg-nexus|MiCA, TFR, and the Krypto-MPfG Nexus]] ([MiCA, TFR, and the Krypto-MPfG Nexus](mica-tfr-krypto-mpfg-nexus.md))
- [[aml-directives-regulations-timeline|AML Directives and Regulations Timeline]] ([AML Directives and Regulations Timeline](../references/aml-directives-regulations-timeline.md))

## Sources

- [FATF institutional history](../../raw/articles/2026-08-29-fatf-history-and-mandate.md)
- [FATF virtual-assets standard 2019](../../raw/articles/2026-08-29-fatf-virtual-assets-standard-2019.md)
- [FATF targeted update 2026](../../raw/papers/2026-08-29-fatf-va-vasp-targeted-update-2026.md)
- [OECD CARF](../../raw/articles/2026-08-29-oecd-carf-2022.md)
- [DAC8](../../raw/articles/2026-08-27-eu-directive-2023-2226-dac8.md)
- [AMLR official source record](../../raw/articles/2026-08-27-eu-amlr-regulation-2024-1624.md)
- [AMLA official source record](../../raw/articles/2026-08-27-eu-amla-regulation-2024-1620.md)
- [AMLD4 and AMLD5 transition](../../raw/articles/2026-08-27-eu-amld4-amld5-transition.md)
- [Criminal AMLD6](../../raw/articles/2026-08-27-eu-criminal-amld6-2018-1673.md)
- [Recast AMLD6](../../raw/articles/2026-08-27-eu-amld6-2024-1640-system.md)
- [TFR](../../raw/articles/2026-08-27-eu-tfr-regulation-2023-1113.md)
- [Financial-information access](../../raw/articles/2026-08-27-eu-directive-2019-1153-financial-info.md)
- [Asset recovery](../../raw/articles/2026-08-27-eu-asset-recovery-directive-2024-1260.md)
- [Insolvency BARIS access](../../raw/articles/2026-08-27-eu-directive-2026-799-insolvency-baris-access.md)
