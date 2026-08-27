---
title: "MiCA, TFR, and the Krypto-MPfG Nexus"
category: topic
sources:
  - raw/articles/2026-08-27-eu-mica-regulation-2023-1114.md
  - raw/articles/2026-08-27-eu-tfr-regulation-2023-1113.md
  - raw/articles/2026-08-27-austria-mica-vvg-bgbl-111-2024.md
  - raw/articles/2026-08-27-austria-mica-vvg-amendment-bgbl-5-2026.md
  - raw/articles/2026-08-27-fma-mica-transition-2026.md
  - raw/articles/2026-08-27-fma-casp-applicant-guidance.md
  - raw/articles/2026-08-27-fma-tfr-guidance.md
  - raw/articles/2026-08-27-austria-fm-gwg-current-crypto.md
  - raw/articles/2026-08-27-eu-amlr-regulation-2024-1624.md
  - raw/articles/2026-08-27-austria-krypto-mpfg-bgbl-96-2025.md
  - raw/articles/2026-08-27-krypto-mpfg-section-20-retention.md
created: 2026-08-27
updated: 2026-08-27
tags: [mica, tfr, krypto-mpfg, casp, passporting, purpose-limitation, gold-plating]
aliases: [MiCA DAC8 overlap, CASP regulatory baseline]
confidence: high
volatility: hot
verified: 2026-08-27
summary: "MiCA and TFR create extensive CASP records and controls, but they do not erase the purpose, scope, and retention differences of Austria's all-customer Krypto-MPfG tax processing."
---

# MiCA, TFR, and the Krypto-MPfG Nexus

> MiCA and TFR explain why a CASP already holds extensive data. They do not by themselves authorise a second, universal tax-profile purpose.

## Three regimes, three purposes

| Regime | Core purpose | Relevant data duty | Ordinary period |
|---|---|---|---|
| MiCA | authorisation, supervision, market integrity, and client protection | records of services, activities, orders, and transactions under Article 68(9) | five years; up to seven on authority request |
| TFR | AML/CFT travel rule | originator and beneficiary information accompanying crypto transfers | five years; up to five more only after a national AML/CFT necessity/proportionality assessment |
| DAC8/Krypto-MPfG | tax transparency and automatic exchange | tax identity, residence, and annual reportable transaction aggregates | national implementation and Directive safeguards |

The same underlying transaction may touch all three systems. That operational overlap is not legal identity. Purpose limitation, data minimisation, access, storage, security, and deletion must be justified for each processing purpose.

## MiCA baseline

Articles 59–63 establish authorisation. A regulated financial entity can use the Article 60 notification route; another CASP applies in its home Member State. Article 65 then passports services across the Union through a notice to the home authority, which informs host authorities, ESMA, and EBA. A host-state physical presence is not generally required.

For Krypto-MPfG scope this means:

- an Austria-home Article 60/63 provider is the cleanest provider claimant under section 15(1)(1);
- a foreign-home provider should not be described as Austrian merely because it serves an Austrian customer;
- sections 16–17 must be checked before alleging duplicate reporting because they provide relief where another Member State or qualifying third country receives the report;
- a foreign-provider challenge needs an actual Austrian demand, refusal, or credible enforcement position, not a hypothetical passporting conflict.

MiCA Article 68(9) is the State's strongest overlap argument. It requires broad records that can already include the transaction material a tax pipeline needs. Article 73 also keeps the CASP responsible for outsourced functions and requires EU data-protection compliance. Article 94 gives authorities extensive information and enforcement powers.

The response is not that MiCA data do not exist. It is that Article 68(9) specifies supervisory, enforcement, client-protection, and market-integrity purposes; it does not automatically establish tax aggregation, all-customer tax classification, or tax-authority exchange as compatible secondary purposes.

## TFR baseline

TFR Articles 14–18 require defined originator and beneficiary data and relevant account, DLT-address, or transaction identifiers for transfers involving a covered intermediary. Transfers exceeding EUR 1,000 to or from a self-hosted address require an assessment of customer ownership or control.

That dataset can be much more granular than the annual DAC8 report. But Article 25 is correspondingly important: it confines TFR personal-data processing to AML/CFT and prohibits incompatible further processing. Article 26 starts with five years and permits a national extension only for the AML/CFT purpose after a necessity and proportionality assessment.

Public communication should therefore say:

- CASPs already collect sensitive transfer data under separate law;
- combining those records with tax identity and annual reporting can increase inference and breach consequences;
- the legal question is whether and how that combination is authorised and safeguarded.

It should not say that the DAC8 report itself transmits wallet addresses, transaction IDs, dates, or counterparties. It does not.

## Austrian MiCA implementation

The MiCA-VVG designates the FMA, creates Austrian supervision and sanctions, and supplies a BVwG appeal. Austria shortened the legacy transition to 31 December 2025. The FMA's June 2026 notice confirms that unauthorised providers cannot continue onboarding and should wind down. Any current claimant analysis must therefore use the provider's actual Article 60/63 status, not an expired VASP transition.

The MiCA-VVG and its 2026 amendment do not create section 20(1) Krypto-MPfG. They are useful mainly to establish:

- which authority and home state supervise the provider;
- what systems and records already exist;
- what authorisation and enforcement routes are available;
- which costs belong to MiCA rather than the tax-reporting increment.

## AML baseline

FM-GwG adds a third existing-cost baseline. Section 6 requires risk-based customer and beneficial-owner due diligence; section 11a adds controls for CASP transfers to or from self-hosted addresses; section 16 governs suspicious-transaction reports; and section 21 currently retains CDD and transaction records for ten years. Those duties can explain why a provider already has identity and transfer data, but they do not automatically authorise universal tax-purpose aggregation under section 20(1) Krypto-MPfG.

Future AMLR generally applies from 10 July 2027. Its five-year retention baseline plus a case-specific extension is a useful proportionality comparator, not current proof that Austrian FM-GwG retention is invalid. Provider evidence must subtract both present FM-GwG costs and future changes that have not yet occurred.

## Krypto-MPfG delta

The strongest distinct Austrian provision remains section 20(1): it requires the section 18 information to be determined, collected, stored, and processed for every customer, every transaction, and every crypto-asset irrespective of reportable-user status.

The best counterfactual is not “no regulation.” It is:

1. perform the identification and self-certification needed to decide reportability;
2. maintain MiCA and TFR records for their own legal purposes;
3. create the tax-specific section 18 aggregate only for a reportable user;
4. delete or cease tax-purpose processing when a reliably determined non-reportable status removes the need.

That counterfactual isolates the disputed increment and makes necessity testable.

Section 20(4) should not be overstated: its ten-year deletion rule is worded for information transmitted under the Act. Section 39 more clearly retains documentation of reporting and due-diligence steps for ten years. The retention rule for complete section 20(1) profiles that are never transmitted remains an interpretation, precision, and storage-limitation problem—not a proven universal ten-year raw-record command.

## Claimant and evidence consequences

An Austria-home CASP should quantify only the additional tax-purpose work:

- fields collected solely for non-reportable customers;
- tax-specific aggregation and historical reconstruction;
- storage, deletion, and access-control architecture beyond MiCA/TFR needs;
- TIN and tax-residence validation;
- DPIA, notices, legal review, vendors, and personnel attributable to that increment.

A non-reportable user should prove the provider relationship, valid self-certification, section 20 notice or actual processing, relevant transactions, and a concrete access/deletion response. A foreign-home CASP needs evidence that Austria demands duplicate or territorially excessive compliance despite passporting and sections 16–17.

## Red-team

The State can plausibly argue that universal collection is necessary to identify changing residence and reportability, that section 20(1) refers only to defined reportable fields rather than every raw event, and that MiCA already makes the marginal burden small. It can also seek a narrow, constitution-conforming interpretation rather than annulment.

The claimant must answer with a field-by-field and costed counterfactual, evidence that reportability has already been reliably determined, and a narrower workable design. Generic MiCA costs or generic claims of “total financial surveillance” are not enough.

## See Also

- [[austrian-dac8-implementation|Austrian DAC8 Implementation]] ([Austrian DAC8 Implementation](austrian-dac8-implementation.md))
- [[dac8-charter-proportionality|DAC8 Charter Proportionality]] ([DAC8 Charter Proportionality](dac8-charter-proportionality.md))
- [[vfgh-to-cjeu-dac8-route|VfGH-to-CJEU DAC8 Route]] ([VfGH-to-CJEU DAC8 Route](../theses/vfgh-to-cjeu-dac8-route.md))
- [[eu-aml-crypto-regulatory-stack|EU AML Crypto Regulatory Stack]] ([EU AML Crypto Regulatory Stack](eu-aml-crypto-regulatory-stack.md))
- [[austrian-aml-crypto-implementation|Austrian AML Crypto Implementation]] ([Austrian AML Crypto Implementation](austrian-aml-crypto-implementation.md))

## Sources

- [MiCA full official text](../../../legal-docs/supporting/eu-mica-pe-cons-54-2022-rev1-full.pdf)
- [TFR full official text](../../../legal-docs/supporting/eu-tfr-pe-cons-53-2022-rev1-full.pdf)
- [MiCA-VVG, BGBl. I No. 111/2024](../../../legal-docs/supporting/at-bgbl-i-111-2024-mica-vvg.pdf)
- [MiCA-VVG 2026 amendment](../../../legal-docs/supporting/at-bgbl-i-5-2026-mica-vvg-amendment.pdf)
