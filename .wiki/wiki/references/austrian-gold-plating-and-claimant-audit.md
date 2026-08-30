---
title: "Austrian DAC8 Gold-Plating and Claimant Audit"
category: reference
sources:
  - raw/articles/2026-08-27-eu-directive-2023-2226-dac8.md
  - raw/articles/2026-08-27-austria-krypto-mpfg-section-18.md
  - raw/articles/2026-08-27-krypto-mpfg-section-20-retention.md
  - raw/articles/2026-08-27-austria-krypto-mpfg-materials-rv306.md
  - raw/articles/2026-08-27-austria-krypto-mpfg-wfa-rv306.md
  - raw/articles/2026-08-27-commission-dac8-proposal-com-2022-707.md
  - raw/articles/2026-08-27-germany-ksttg.md
  - raw/articles/2026-08-27-netherlands-dac8-implementation-act.md
  - raw/articles/2026-08-27-vfgh-g105-2025-data-monitoring.md
  - raw/articles/2026-08-27-vfgh-g606-2015-registrierkasse.md
  - raw/articles/2026-08-30-austria-krypto-mpfg-section-39-records.md
  - raw/articles/2026-08-30-vfgh-g7-2012-retention-maximum.md
  - raw/articles/2026-08-30-vfgh-b1187-2013-financial-data-retention.md
  - raw/articles/2026-08-30-vfgh-e3249-2016-retention-necessity.md
created: 2026-08-27
updated: 2026-08-30
tags: [dac8, austria, gold-plating, krypto-mpfg, claimant, standing, proportionality]
aliases: [Krypto-MPfG overimplementation audit, DAC8 claimant matrix]
confidence: high
volatility: hot
verified: 2026-08-27
summary: "Primary-text audit identifying section 20(1) as the real Austrian excess, correcting the retention theory, and separating the best CASP and user proceedings."
---

# Austrian DAC8 Gold-Plating and Claimant Audit

> Textual result: section 20(1) clearly goes beyond the DAC8 reporting architecture. Litigation result: that excess is not automatically unlawful and must be tied to data-minimisation, strict necessity, and claimant-specific evidence.

## Ranked statutory points

| Point | Primary-text result | Litigation assessment |
|---|---|---|
| Section 20(1), section 18 information derived from every customer's transactions and assets | Clear Austrian all-customer processing language. DAC8 requires universal due diligence to identify status but structures transaction reporting around reportable users. The provision does not itself prove itemised reporting or retention of every raw ledger field. | Strongest national issue; medium merits until the actual processing scope, necessity, safeguards, and a less intrusive counterfactual are proved. |
| Section 39, ten-year compliance records | The enacted text omits Annex VI Section V.B.1's final reportability phrase, but Annex VI covers both reporting and due-diligence records and the phrase's scope is ambiguous. | Unresolved interpretation issue, not an established national excess. It matters only with a completed non-reportable determination and proved covered records. |
| Never-transmitted non-reportable-user data | Section 20(1) mandates storage and processing of the reportable information derived from all transactions, but the Act has no express deletion deadline for a never-transmitted section 18 aggregate profile outside records covered by section 39. The existence and content of that profile require provider evidence. | Storage-limitation issue requiring the actual provider dataset, legal basis, schedule and deletion response. GDPR Article 5(1)(e) is the main State answer. |
| Section 20(4), ten-year deletion date | Applies only to information transmitted under the Act. VfGH G 7/2012 supports construing a statutory deletion date as an outer limit with earlier necessity-based deletion. | A facial claim that section 20(4) mandates ten years of active storage is weak. Challenge an actual refusal or absence of necessity review instead. |
| Section 22(2), annual re-arising registration duty | Austrian enforcement device not stated verbatim in DAC8. It concerns non-MiCA operators, not an ordinary Article 60/63 CASP. | Weak facial claim because DAC8 leaves effective, proportionate, dissuasive enforcement to Member States. Reassess only after actual cumulative sanctions. |
| Section 15(1)(1), Article 60 nexus | Best read conformingly as Austrian home-state allocation; MiCA Article 65 governs ordinary passporting. | No present defect without an Austrian authority applying it to a foreign-home passported provider and creating duplicate reporting. Obtain a written authority position first. |
| Krypto-MPfG-DV | Requires transmission of the section 18 information through the FinanzOnline portal webservice and refers to separate BMF XML/WSDL specifications. | Do not challenge without obtaining the operative specification and identifying a concrete requirement outside statutory authorisation. |

## Why section 20(1) is the real excess

Annex VI Section III requires self-certification and due diligence so that providers can identify reportable users. Section II then specifies personal and annual transaction information with respect to reportable users and relevant controlling persons.

Section 20(1) instead requires the information defined by section 18 to be determined, collected, stored, and processed for all customers, all transactions, and all crypto-assets regardless of reportable-user status. The Austrian explanatory materials confirm that reading and say it implements Directive Article 25, even though Article 25 is a data-protection provision rather than an obvious standalone mandate for universal transaction-profile creation.

Germany and the Netherlands show a practically available implementation that takes self-certification from users but frames transaction aggregation and reporting around reportable users. This confirms that Austria's express universal rule was not textually compelled. It does not establish maximum harmonisation or invalidate the Austrian addition by itself.

The legal attack should therefore use:

- GDPR Articles 5(1)(b), (c), and (e), and 6(3);
- Charter Articles 7, 8, and 52(1);
- section 1 DSG and, for the provider, Article 6 StGG;
- CJEU C-175/20, *Valsts ieņēmumu dienests*, on relevance, strict necessity, objective limits, purpose, and time period.

The State will rely on changing tax residence, corrections, auditability, providers' existing MiCA/AML records, and broad legislative discretion in mass tax administration. The claimant must show why collecting self-certification universally but creating section 18 tax aggregates only after reportable status is established is equally effective and less intrusive.

## Retention: exact pleading

Section 20(4) says transmitted information must be deleted ten years after the reporting period. It is not the source of a ten-year mandate for a user whose transaction information is never reported.

Three distinct cases remain:

1. Section 39 requires ten-year retention of covered compliance records and omits DAC8 Annex VI's final reportability phrase. Because Annex VI also covers due-diligence records, determine the phrase's correct scope and which records the provider treats as covered before alleging an excess.
2. A never-transmitted section 18 aggregate profile outside section 39 has no clear Krypto-MPfG deletion period. Whether the provider creates that profile, and which transaction inputs it retains for this tax purpose, are factual questions. The issue is storage limitation, subject to the State's answer that directly applicable GDPR supplies the limit.
3. Section 20(4)'s ten-year deletion date for transmitted information can plausibly operate as a ceiling. The stronger case is an actual refusal to delete when necessity ends, not automatic facial invalidity.

VfGH B 1187/2013 upheld necessary automated retention and required destruction only for separate paper records; E 3249/2016 concerned an intimate paper file. They support an effective decision and current-necessity assessment only by analogy for routine electronic DAC8 data. Do not plead the different datasets and legal periods as one undifferentiated ten-year store. Obtain the CASP and authority retention schedules, backups/deletion logic, Article 15 answers and written legal bases.

## Claimant and route matrix

| Claimant | Best issue | Best route | Main weakness |
|---|---|---|---|
| Austria-home CASP | Section 20(1) incremental pipeline, storage, security, and compliance burden | Direct Article 140 application if section 15 status is undisputed and no ordinary determination route is available | Overall WFA costs do not isolate the Austrian excess; tax-compliance merits precedents are deferential. |
| Genuinely non-reportable user processed under section 20 | Universal creation/storage after the provider completed a non-reportable determination | Article 15/17/18 request → section 24 DSG complaint → BVwG → request Articles 267/140 review | Must prove the completed determination and actual processing/retention; direct Article 140 is likely blocked by this route. |
| Reportable Austrian user | DAC8's mandatory EU reporting and Charter validity | Same DSB/BVwG route | Closest DAC2 precedent is strongly adverse; cannot isolate the national non-reportable-user excess. |
| Foreign-home Article 60 entity passporting into Austria | Possible duplicate host-state reporting | Written BMF/FAG position first; litigate only if Austria asserts the duty | Conforming home-state interpretation likely eliminates the issue. |

Citizenship is irrelevant. A non-reportable user must have no tax residence in any participating state, together with a real Austrian statutory nexus and post-1 January 2026 processing. For existing users, section 28(3) permits self-certification acquisition until 1 January 2027 and section 33(2) permits due-diligence completion by the end of the reporting period. Treat status as final only after the provider has actually completed that determination. An Austrian tax resident is normally reportable.

The strongest overall design is coordinated but separate proceedings: a CASP Article 140 application on its own rights and costs, a non-reportable-user DSB case against the national excess, and, if desired, a reportable-user DSB case on DAC8 validity. A blended joint application risks mismatched standing, provisions, and routes.

## CASP evidence file

VfGH G 105/2025 and G 606/2015 make technical and administrative preparation costs powerful standing evidence. Both are adverse warnings on the merits: broad data or tax-compliance systems survived once a public interest and workable safeguards were accepted.

The official WFA estimates EUR 500,000 implementation and EUR 425,000 annual cost per provider, but only for the whole regime. A filing-ready CASP record should separate:

- the DAC8 minimum from section 20(1)'s non-reportable-user path;
- existing MiCA, transfer-of-funds, AML, accounting, and contractual records;
- classification, valuation, annual aggregation, tax-residence logic, storage, security, DPIA, Article 30, and data-subject-request work;
- invoices, contracts, engineering hours, FTEs, storage growth, and continuing support;
- customer counts and the share finally determined not reportable;
- a field-level, costed reportable-user-only counterfactual.

The WFA establishes materiality, not the incremental constitutional violation.

For downstream use, access and authority-side retention, see [[dac8-data-lifecycle-access-retention-remedies|DAC8 Data Lifecycle: Access, Retention and Remedies]] ([DAC8 Data Lifecycle: Access, Retention and Remedies](dac8-data-lifecycle-access-retention-remedies.md)).

## Candidate Article 267 interpretation question

> Do Article 8ad and Annex VI Sections II and III of Directive 2011/16/EU, as amended by Directive (EU) 2023/2226, read with Article 25 of that Directive, GDPR Articles 5(1)(b), (c), and (e), 6(3), and 23, and Charter Articles 7, 8 and 52, preclude national law from requiring a reporting crypto-asset service provider to determine, collect, store and process, for every customer regardless of reportable-user status, the transaction-derived inputs and annual aggregate information described in section 18 Krypto-MPfG?

This narrow interpretation question is more decision-relevant to the Austrian excess than a directive-wide surveillance question. The absence of an EU mandate or express authorisation would not itself invalidate Austria's Article 6(3) legal basis; the question is whether the combined EU data-protection rules preclude that additional processing.

## Sources

- [Krypto-MPfG consolidated snapshot](../../../legal-docs/core/at-krypto-mpfg-consolidated-2026.html)
- [DAC8 full text](../../../legal-docs/core/eu-dac8-directive-2023-2226.pdf)
- [Austrian explanatory materials](../../../legal-docs/supporting/at-krypto-mpfg-erlaeuterungen-rv-306.pdf)
- [Austrian WFA](../../../legal-docs/supporting/at-krypto-mpfg-wfa-rv-306.pdf)
- [Commission proposal COM(2022) 707](../../../legal-docs/supporting/eu-com-2022-707-dac8-proposal.pdf)
- [VfGH G 105/2025](../../../legal-docs/supporting/at-vfgh-g105-2025-corrected.pdf)
- [VfGH G 606/2015 ua](../../../legal-docs/supporting/at-vfgh-g606-2015-registrierkasse.pdf)
