---
title: "Krypto-MPfG-DV Formality and Technical Specifications"
category: reference
sources:
  - raw/articles/2026-08-27-krypto-mpfg-dv-attackable-regulation.md
  - raw/articles/2026-09-04-austria-dsg-section-21-consultation-duty.md
  - raw/articles/2026-09-04-dsg-21-consultation-source-locator-correction.md
  - raw/articles/2026-09-04-vfgh-mandatory-consultation-formal-invalidity.md
  - raw/articles/2026-09-04-vfgh-external-technical-rules-publication.md
  - raw/articles/2026-09-10-bmf-carf-specification-publication-gap.md
created: 2026-09-04
updated: 2026-09-21
tags: [krypto-mpfg, regulation, article-139, consultation, publication, xml, wsdl]
aliases: [Krypto-MPfG implementing regulation challenge, Krypto-MPfG-DV consultation]
confidence: medium
volatility: hot
verified: 2026-09-04
summary: "Fact-gated analysis of the section 21 DSG consultation record and the legal status of external XML, XSD and WSDL requirements under the Krypto-MPfG-DV."
---

# Krypto-MPfG-DV Formality and Technical Specifications

> Two formal questions justify immediate evidence collection. Neither presently proves that the Krypto-MPfG-DV is unlawful.

## 1. Consultation of the Data Protection Authority

[Section 21(1) DSG](https://ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10001597&Artikel=2&Paragraf=21) requires consultation of the Data Protection Authority before federal regulations that directly concern data-protection questions are made. Section 4 Krypto-MPfG-DV specifies the compulsory electronic transmission of personal reporting data. This gives a substantial basis for treating the regulation as directly concerned with data protection, but the point remains open until the regulation file is obtained.

VfGH V 119/88, V 58/00 and V 531/2020 treat the proved omission of a mandatory consultation as a formal defect of the regulation. They concern different statutory consultation duties and therefore support an analogy, not a holding on section 21 DSG.

The required proof is:

1. the complete regulation file for BGBl II 331/2025;
2. the exact draft sent to the DSB;
3. the consultation request and delivery record;
4. the DSB response or documentation that the response period expired;
5. the chronology showing consultation occurred before the regulation was made.

No public DSB statement was located. That is not evidence that consultation was omitted.

## 2. External XML, XSD and WSDL specifications

Section 4 Krypto-MPfG-DV states that the organisational and technical specifications are available on the BMF website and in the provider portal. The regulation rests on express delegations in sections 17(4), 19(2) and 22(4) Krypto-MPfG and sections 86a and 97(3) BAO. A general claim that the regulation lacks any statutory authority is therefore weak.

The [10 September 2026 search record](../../raw/articles/2026-09-10-bmf-carf-specification-publication-gap.md) did not locate the CARF specifications on the inspected public BMF pages. It did not inspect the provider portal or establish that the specifications were unavailable there. This is a dated discovery gap, not proof of non-publication or invalidity. Obtain the applicable version, publication history and actual access conditions before drawing either conclusion. The archived search has not been repeated here.

The content of the external specifications controls the stronger question:

| Content | Preliminary legal character | Litigation value |
|---|---|---|
| XML encoding, data types, endpoint, transport and authentication | Technical implementation | Low without a separate defect |
| Fields and validation rules already determined by section 18 | Technical concretisation | Usually low |
| Additional compulsory data fields or substantive classifications | Possible generally binding norm | High enough for authority and publication analysis |
| New deadlines, retention duties or rejection consequences | Possible independent duty | High enough for authority, determinacy and publication analysis |
| Undated or mutable rules without version history | Legal-certainty concern | Depends on whether the rule changes legal duties |

VfGH V 69/2018 and V 23/06 condemn use of a website or other substitute medium where the external document itself contains the binding rule and the prescribed publication form was not used. G 174/06 is adverse authority: connection to recognised technical standards may be permissible where the standards are not themselves made binding normative content. The long-standing FinanzOnline and DAC7 implementations also make a categorical attack on external technical specifications unsafe.

## 3. Procedural reach

Section 4 Krypto-MPfG-DV directly obliges the reporting provider. A provider is therefore the more natural applicant for a direct Article 139 challenge to the transmission rule or a normative technical specification. A reporting user must separately establish direct legal effect or, in the DSB and BVwG route, that the challenged provision is applicable and prejudicial to the concrete decision.

A strong formal ground can still fail if brought by a person who is not directly affected, against a document that is not a regulation, or in a proceeding in which the rule is not prejudicial.

## 4. Evidence request

The immediate request should cover:

- the full regulation file, drafts, explanatory notes, approvals and distribution records;
- DSB and Data Protection Council consultation documents and chronology;
- all current and historic XML, XSD, WSDL, code and validation specifications;
- version identifiers, publication dates, effective dates and change logs;
- validation and rejection consequences;
- the legal basis assigned to each requirement.

The documents should then be diffed against section 18 Krypto-MPfG and the published regulation. The output should identify every requirement that is not merely technical or already determined by the published legislation.

## See Also

- [[austrian-gold-plating-and-claimant-audit|Austrian Gold-Plating and Claimant Audit]] ([Austrian Gold-Plating and Claimant Audit](austrian-gold-plating-and-claimant-audit.md))
- [[dac8-transaction-granularity-and-reporting-layers|DAC8 Transaction Granularity and Reporting Layers]] ([DAC8 Transaction Granularity and Reporting Layers](dac8-transaction-granularity-and-reporting-layers.md))
- [[g178-dsb-bvwg-subsidiarity-route|G 178/2024 and the DSB-BVwG Route]] ([G 178/2024 and the DSB-BVwG Route](g178-dsb-bvwg-subsidiarity-route.md))

## Sources

- [Krypto-MPfG-DV](../../raw/articles/2026-08-27-krypto-mpfg-dv-attackable-regulation.md)
- [Section 21 DSG consultation duty, original record](../../raw/articles/2026-09-04-austria-dsg-section-21-consultation-duty.md), with [correct official locator](../../raw/articles/2026-09-04-dsg-21-consultation-source-locator-correction.md).
- [Mandatory-consultation cases](../../raw/articles/2026-09-04-vfgh-mandatory-consultation-formal-invalidity.md)
- [External technical rules and publication](../../raw/articles/2026-09-04-vfgh-external-technical-rules-publication.md)
