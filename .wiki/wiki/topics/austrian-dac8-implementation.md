---
title: "Austrian DAC8 Implementation"
category: topic
sources:
  - raw/articles/2026-08-27-eu-directive-2023-2226-dac8.md
  - raw/articles/2026-08-27-austria-krypto-mpfg-bgbl-96-2025.md
  - raw/articles/2026-08-27-austria-krypto-mpfg-section-18.md
  - raw/articles/2026-08-27-krypto-mpfg-section-20-retention.md
  - raw/articles/2026-08-27-austria-krypto-mpfg-user-facing-duties.md
  - raw/articles/2026-08-27-austrian-bmf-dac8-overview.md
  - raw/articles/2026-08-27-commission-implementing-regulation-2025-2263.md
  - raw/articles/2026-08-27-austria-krypto-mpfg-materials-rv306.md
  - raw/articles/2026-08-27-austria-krypto-mpfg-wfa-rv306.md
  - raw/articles/2026-08-27-commission-dac8-proposal-com-2022-707.md
  - raw/articles/2026-09-29-refreshat-commission-dac8-infringement-status.md
created: 2026-08-27
updated: 2026-09-29
tags: [austria, dac8-transposition, krypto-mpfg, tax-information-exchange]
aliases: [Krypto-MPfG, Austrian DAC8 transposition]
confidence: high
volatility: hot
verified: 2026-09-29
summary: "Austria implemented DAC8 through the Krypto-MPfG, effective 1 January 2026, with all-customer processing, annual reporting, user notice, self-certification, and enforcement rules."
---

# Austrian DAC8 Implementation

> Austria's DAC8 regime is enacted and operative. The first exchange is in 2027, but statutory collection and processing concern the 2026 reporting period.

## Legal instruments and timing

The core act is the Krypto-Meldepflichtgesetz in BGBl. I Nr. 96/2025. It entered into force on 1 January 2026 and is supplemented by a December 2025 implementing regulation. This met DAC8's formal transposition deadline. Austria was not among the twelve Member States sent letters of formal notice for DAC8 non-transposition on 30 January 2026.

At EU level, Commission Implementing Regulation (EU) 2025/2263 standardises technical forms, registration, identification, and computerised exchange formats.

Providers generally report the preceding calendar year by 31 July. Tax authorities exchange relevant 2026 information in 2027. The later exchange date does not mean that the statute is dormant during 2026.

## What the Austrian regime does

Section 18 requires identifying information and annual transaction aggregates by crypto-asset and category. The exact fields matter: the statute does not justify describing every reported record as a full raw transaction history.

Section 20 is broader at the provider-processing layer. It requires determination, collection, storage, and processing of the section 18 information for all customers with respect to all transactions and crypto-assets, regardless of final reportability. It also requires user notice before the first report. Section 20(4)'s ten-year deletion horizon applies only to information transmitted under the Act, not expressly to a never-reported customer's transaction-derived tax profile. The provision does not itself prove retention of every raw ledger field.

Section 39 separately retains documents evidencing reporting and due-diligence steps for ten years. Its enacted wording refers to documents; the explanatory materials speak of documents and information. The Act therefore leaves a significant interpretation and legal-certainty question about the retention and deletion rule for section 20(1) information that is never transmitted.

Sections 36 and 38 structure user self-certification and eventual transaction blocking where required information remains missing after statutory requests and reminders.

## Gold-plating seam

DAC8 Annex VI Section III requires due diligence and self-certification to identify reportable users. Section II frames transaction reporting around reportable users. Austria nevertheless expressly requires section 18 information to be processed for every customer with respect to every transaction. Germany and the Netherlands demonstrate that universal self-certification can coexist with reportable-user-specific transaction aggregation. The actual Austrian XML/WSDL or a submission example remains necessary to establish how the domestic portal segments the aggregate fields.

The textual excess is clear; illegality is not automatic because DAC8 contains no obvious maximum-harmonisation rule. The constitutional and EU-law question is whether the additional processing is strictly necessary, sufficiently precise, time-limited, and safeguarded under GDPR data minimisation and storage limitation, Charter Articles 7, 8, and 52(1), and section 1 DSG.

The official WFA estimates approximately EUR 500,000 implementation and EUR 425,000 annual cost per potentially affected provider. This supports current and material CASP standing but covers the whole regime; it does not quantify the disputed national increment.

The analysis must separate:

- mandatory DAC8 content, which may require a CJEU validity or interpretation ruling;
- Austrian implementation choices, which the VfGH can review directly;
- provider practice not actually required by the statute.

Section 22(2)'s annual re-arising registration duty concerns non-MiCA operators, not an ordinary Article 60/63 CASP, and is weak as a facial claim without actual cumulative sanctions. The implementing regulation should not be challenged merely because it exists; it contains the technical format and needs a concrete ultra-vires defect.

## See Also

- [[individualantrag-article-140|Individualantrag under Article 140 B-VG]] ([Individualantrag under Article 140 B-VG](../concepts/individualantrag-article-140.md)) — possible citizen entry route.
- [[dac8-charter-proportionality|DAC8 Charter Proportionality]] ([DAC8 Charter Proportionality](dac8-charter-proportionality.md)) — substantive rights analysis.
- [[vfgh-to-cjeu-dac8-route|VfGH-to-CJEU DAC8 Route]] ([VfGH-to-CJEU DAC8 Route](../theses/vfgh-to-cjeu-dac8-route.md)) — procedural thesis.
- [[mica-tfr-krypto-mpfg-nexus|MiCA, TFR, and the Krypto-MPfG Nexus]] ([MiCA, TFR, and the Krypto-MPfG Nexus](mica-tfr-krypto-mpfg-nexus.md)) — existing regulatory records versus the tax-purpose increment.
- [[dac8-fundamental-rights-and-public-risks|DAC8 Fundamental Rights and Public Risks]] ([DAC8 Fundamental Rights and Public Risks](dac8-fundamental-rights-and-public-risks.md)) — litigation and communications risk layers.

## Sources

- [Commission DAC8 infringement status](../../raw/articles/2026-09-29-refreshat-commission-dac8-infringement-status.md)
- [Council Directive (EU) 2023/2226](../../raw/articles/2026-08-27-eu-directive-2023-2226-dac8.md)
- [Krypto-MPfG enactment](../../raw/articles/2026-08-27-austria-krypto-mpfg-bgbl-96-2025.md)
- [Section 18 reporting fields](../../raw/articles/2026-08-27-austria-krypto-mpfg-section-18.md)
- [Section 20 processing and retention](../../raw/articles/2026-08-27-krypto-mpfg-section-20-retention.md)
- [User-facing operation](../../raw/articles/2026-08-27-austria-krypto-mpfg-user-facing-duties.md)
- [BMF implementation overview](../../raw/articles/2026-08-27-austrian-bmf-dac8-overview.md)
- [Commission Implementing Regulation (EU) 2025/2263](../../raw/articles/2026-08-27-commission-implementing-regulation-2025-2263.md)
- [Austrian explanatory materials](../../raw/articles/2026-08-27-austria-krypto-mpfg-materials-rv306.md)
- [Austrian WFA](../../raw/articles/2026-08-27-austria-krypto-mpfg-wfa-rv306.md)
- [Gold-plating and claimant audit](../references/austrian-gold-plating-and-claimant-audit.md)
