---
title: "DAC8 Member-State Implementation Comparators"
category: reference
sources:
  - raw/articles/2026-08-27-eu-directive-2023-2226-dac8.md
  - raw/articles/2026-08-27-krypto-mpfg-section-20-retention.md
  - raw/articles/2026-09-04-krypto-mpfg-section-39-timing-correction.md
  - raw/articles/2026-09-04-germany-ksttg-reportability-notice-retention.md
  - raw/articles/2026-09-04-ireland-dac8-si-584-2025-retention-copy.md
  - raw/articles/2026-09-04-netherlands-dac8-decision-records-retention.md
  - raw/articles/2026-09-04-france-dac8-prefiling-copy-and-records.md
  - raw/articles/2026-09-04-eu-dac8-xml-correction-deletion.md
  - raw/articles/2026-09-04-finland-dac8-national-capital-gains-extension.md
created: 2026-09-04
updated: 2026-09-04
tags: [dac8, member-states, retention, notice, correction, data-minimisation, alternatives]
aliases: [DAC8 national alternatives, DAC8 comparative safeguards]
confidence: high
volatility: hot
verified: 2026-09-04
summary: "Comparison of enacted DAC8 choices showing shorter provider retention, staged reportability and concrete pre-filing transparency without overstating national privacy differences."
---

# DAC8 Member-State Implementation Comparators

> The useful comparison is feature-specific. It does not show that another Member State has a uniformly less intrusive DAC8 system. It shows that the Directive leaves concrete choices and that some narrower safeguards are already operational in enacted law.

## Comparative matrix

| Jurisdiction | Reportability and records | Provider retention | User information | Litigation use and limit |
|---|---|---:|---|---|
| EU baseline | Universal due diligence determines whether a user is reportable; transaction reporting is structured around reportable users. Annex VI V.B.1 permits a national record period within five to ten years. | 5–10 years permitted | Article 25(4) requires information sufficiently early to exercise data-protection rights. | Establishes discretion, not the unlawfulness of any option within the range. |
| Austria | Section 20(1) expressly requires section 18 information to be determined, collected, stored and processed for all customers, transactions and crypto-assets regardless of reportable-user status. Section 20(4) applies to transmitted information and section 39 to documented compliance steps; both use ten years after the end of the relevant reporting period. | 10 years | Section 20(2)–(3) transposes notice and timing duties but does not expressly require the concrete final dataset before filing. | The all-customer formulation and each ten-year provider category require their own field- and layer-specific justification. They are not unlawful merely because another drafting choice exists. |
| Germany | Self-certification applies to users; transaction reporting and the related statutory records are expressly framed around users already identified as reportable. | 10 years | Advance notice must be early enough for rights to be exercised, but the statute does not expressly require the final dataset before filing. | Strong drafting comparator for section 20(1); no proof of a different underlying provider system and no shorter-retention comparator. |
| Ireland | Return contains the reportable user's information. The provider must give that user a copy by the return deadline. | 6 years, unless an open enquiry requires longer | Copy of the information in the return by the filing date | Strong enacted shorter-period comparator. The simultaneous deadline does not guarantee pre-filing review or an automatic stop. |
| Netherlands | Self-certification precedes the reportability determination. Existing Common Reporting Standard due diligence and tax self-certifications may be reused. Supporting records include relevant external wallet addresses even though the routine report does not. | 7 years | No stronger concrete pre-filing right established in the reviewed measure | Strong shorter-period and staged-drafting comparator, but the wallet-address record is adverse evidence against treating the whole system as less intrusive. |
| France | Due diligence identifies users with covered transactions. Existing tax due diligence and self-certifications may be reused. | 10 years | The concrete information to be transmitted about the person must be provided before filing. | Strong proof that a pre-filing data view is practicable; it creates neither a veto nor an automatic suspension. |
| Finland | Finland publicly identifies an additional national report for Finnish tax residents intended to support calculation of gains and losses. | Not used here as a retention comparator | Not used here as a notice comparator | Adverse authority: national extensions are possible. It also shows that an extension can be expressly identified and tied to a defined extra tax purpose. |

## Propositions that survive the comparison

### Ten years is a choice, not an EU necessity

Ireland selected six years, subject to an open-enquiry extension, and the Netherlands seven for provider records. Austria selected ten years after the end of the relevant reporting period for both transmitted-information copies under section 20(4) and the different compliance documents under section 39. This gives a category-specific necessity question: why are ten years needed for each Austrian provider-held category, and why would six or seven years not serve the same defined Austrian task?

The comparison alone does not answer that question. Annex VI V.B.1 runs from the end of the period within which reporting is required, whereas section 39 runs from the end of the relevant reporting period. Duration and starting point must therefore be compared separately. Austrian assessment, audit, limitation and enforcement periods, open proceedings, backups and downstream files must be mapped before asserting equal effectiveness. Sections 20(4) and 39 do not set the retention period for every authority-held copy; those copies require a separate legal-basis and necessity analysis.

### Austria's all-customer wording was not textually inevitable

Germany and the Netherlands separate the universal residence self-certification from reportable-user treatment and transaction-related reporting records. That is strong evidence that DAC8 did not force Austria to use section 20(1)'s express all-customer, all-transaction and all-crypto-asset formulation.

The legal-text comparison does not establish what German or Dutch providers actually compute in temporary or operational systems. A claimant still needs provider evidence showing whether Austria causes an additional persistent annual profile for a non-reportable user.

### Concrete pre-filing review is practicable

France requires delivery of the information to be transmitted about the person before the report is filed. It therefore supplies an enacted accuracy safeguard against the contention that a concrete pre-filing view would be administratively impossible.

It does not prove a right to approve the report, a duty to wait while an objection is pending, or an existing EU-law right to a pre-transfer hearing. Those are separate remedial questions.

### Correction and deletion can propagate through the exchange format

The binding EU XML format includes corrected-data and deletion-of-data record types linked to the earlier message and record. A correction demand can therefore ask not only whether the provider changed its local database but whether a corresponding exchange message was sent to every holder of the earlier record.

Technical capability is not a substantive entitlement. The legal ground, controller, recipient, data copy and effect of a deletion remain to be established.

## Ranked less-intrusive alternatives

| Alternative | Evidence status | Proper use |
|---|---|---|
| Six- or seven-year provider period instead of ten | Enacted in Ireland and the Netherlands | Direct comparator; test against each Austrian statutory purpose and limitation period. |
| Materialise the full annual transaction aggregate only after reportability is determined | Supported by the EU reporting architecture and German and Dutch drafting | Strongest for a genuinely non-reportable user; provider architecture must show the actual incremental profile. |
| Give the user the concrete report before filing | Enacted in France | Demonstrates practicability of early error detection; does not itself establish a veto or stay. |
| Reuse compliant CRS due diligence or an existing tax self-certification | Expressly allowed in Germany, France and the Netherlands | Reduces duplicate collection; does not remove the final DAC8 fields. |
| Send correction or deletion messages to downstream recipients | Built into the EU exchange schema | Supports a traceable propagation remedy where the substantive right is established. |
| Use the reduced Identification Service identity tuple where its conditions are met | Expressly provided by DAC8 | Enacted conditional minimisation of what is reported and communicated; Recital 34 leaves due-diligence and collection duties untouched, and Austrian service availability and operational fitness remain unverified. |

## Arguments not established by the comparison

- Other Member States uniformly collect less data than Austria.
- DAC8 permits omission of mandatory annual fields for reportable users.
- The USD 50,000 retail-payment threshold is a general user or transaction de-minimis rule.
- Any examined Member State grants the user a veto over a required report.
- A six- or seven-year period is automatically constitutionally required in Austria.
- An Identification Service reduces the provider's underlying due-diligence or information-collection duties.
- Dutch provider retention of external wallet addresses makes those addresses part of the routine authority-to-authority DAC8 report.
- Zero-knowledge, risk-only or transaction-threshold systems are proven equally effective operational substitutes.

## Evidence needed for the Austrian comparison

1. Identify exactly when the provider creates a complete section 18 annual profile for a non-reportable user.
2. Separate ordinary transaction records from data duplicated or aggregated specifically for Krypto-MPfG compliance.
3. Identify the retention and deletion rule for a profile that is never transmitted.
4. Obtain the concrete notice and planned report view, including whether it arrives before filing.
5. Trace corrections through provider, BMF, exchange and recipient-state copies.
6. Determine whether an Austrian competent authority uses a qualifying Identification Service and whether Austrian providers can rely on it in practice.
7. Match every claimed ten-year need to a specific Austrian assessment, audit or enforcement period.

## See Also

- [[austrian-gold-plating-and-claimant-audit|Austrian DAC8 Gold-Plating and Claimant Audit]] ([Austrian DAC8 Gold-Plating and Claimant Audit](austrian-gold-plating-and-claimant-audit.md))
- [[dac8-data-lifecycle-access-retention-remedies|DAC8 Data Lifecycle: Access, Retention and Remedies]] ([DAC8 Data Lifecycle: Access, Retention and Remedies](dac8-data-lifecycle-access-retention-remedies.md))
- [[dac8-field-necessity-and-alternatives|DAC8 Field Necessity and Less-Intrusive Alternatives]] ([DAC8 Field Necessity and Less-Intrusive Alternatives](dac8-field-necessity-and-alternatives.md))

## Sources

- [Council Directive (EU) 2023/2226](../../raw/articles/2026-08-27-eu-directive-2023-2226-dac8.md)
- [Austria Krypto-MPfG section 20](../../raw/articles/2026-08-27-krypto-mpfg-section-20-retention.md)
- [Austria Krypto-MPfG section 39 timing correction](../../raw/articles/2026-09-04-krypto-mpfg-section-39-timing-correction.md)
- [Germany KStTG detail](../../raw/articles/2026-09-04-germany-ksttg-reportability-notice-retention.md)
- [Ireland SI 584/2025](../../raw/articles/2026-09-04-ireland-dac8-si-584-2025-retention-copy.md)
- [Netherlands implementing decision](../../raw/articles/2026-09-04-netherlands-dac8-decision-records-retention.md)
- [France pre-filing copy and records](../../raw/articles/2026-09-04-france-dac8-prefiling-copy-and-records.md)
- [EU XML correction and deletion](../../raw/articles/2026-09-04-eu-dac8-xml-correction-deletion.md)
- [Finland national gains-and-losses extension](../../raw/articles/2026-09-04-finland-dac8-national-capital-gains-extension.md)
