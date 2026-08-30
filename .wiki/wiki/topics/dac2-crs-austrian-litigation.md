---
title: "Austrian DAC2/CRS Litigation"
category: topic
sources:
  - raw/articles/2026-08-27-bvwg-w211-2232955-dac2.md
  - raw/articles/2026-08-27-vfgh-e-2097-2021-dac2.md
  - raw/articles/2026-08-27-vwgh-ro-2023-04-0021-dac2.md
  - raw/articles/2026-08-27-dac2-directive-2014-107.md
  - raw/articles/2026-08-27-eu-directive-2023-2226-dac8.md
  - raw/articles/2026-08-27-dac8-impact-assessment-swd-2022-401.md
  - raw/articles/2026-08-27-krypto-mpfg-section-20-retention.md
created: 2026-08-27
updated: 2026-08-30
tags: [dac2, crs, austria, automatic-exchange, vfgh, adverse-authority]
aliases: [Austrian CRS lawsuit, E 2097/2021]
confidence: high
volatility: cold
verified: 2026-08-30
summary: "The Austrian DAC2 case used the practical DSB-to-BVwG route but failed on Charter validity and non-referral, making it the closest adverse procedural and merits authority for DAC8."
---

# Austrian DAC2/CRS Litigation

> DAC2 is the closest Austrian precedent, and it is adverse: the ordinary data-protection route worked procedurally, while the privacy, proportionality, and Article 267 arguments failed.

## Procedural chain

1. An individual complained to the Austrian Data Protection Authority about automatic exchange of a German bank account holding approximately EUR 40.
2. The DSB rejected the complaint in a partial decision of 18 May 2020.
3. The BVwG dismissed the appeal in W211 2232955-1/7E on 12 April 2021.
4. The VfGH dismissed the constitutional complaint in E 2097/2021 on 9 March 2023 and found no genuine doubt requiring an Article 267 reference.
5. The VwGH rejected the revision and proposed references in Ro 2023/04/0021 on 10 December 2025.

The public full-text record begins with the BVwG decision; no separate public full text of the DSB partial decision was located.

## Adverse holdings already on the table

The courts rejected or neutralized arguments that:

- suspicionless reporting of all covered accounts is inherently disproportionate;
- a de minimis account requires a minimum threshold;
- generic cybersecurity or hacking risks invalidate the regime;
- all-customer pre-processing is unlawful merely because most customers are tax-compliant;
- the tax-information regime is equivalent to communications metadata retention;
- the Austrian courts were obliged to refer broad validity questions to the CJEU.

The VfGH stressed that ordinary account information did not reveal movements, daily habits, or social relationships in the way the traffic and location data did in Digital Rights Ireland.

## What can distinguish DAC8

DAC8 does not report a year-end crypto-asset balance. It instead reports a richer annual activity profile than the bank-account facts described in the DAC2 case: per-asset category aggregates for fiat and crypto acquisitions and disposals, high-value retail payments, and transfers. Most categories include value, units and count; the separate outward-transfer field contains value and units for DLT addresses not known by the provider to be associated with a VASP or financial institution, but no address or transaction count. The Commission deliberately preferred a transaction-derived annual category-aggregate model to balance-only reporting because it expected more precise risk assessment, stronger deterrence and fewer follow-up requests.

The distinction must remain exact. DAC8 does **not** require reporting transaction dates, transaction identifiers, counterparties, or wallet/DLT addresses. Public-ledger correlation is a separate evidentiary step and cannot be assumed from the reporting fields alone.

Austria's retention text also differs. The GMSG provision quoted in E 2097/2021 required deletion of transmitted information after five years; section 20(4) Krypto-MPfG sets a ten-year deletion date. Austrian authority suggests such a date can operate as an outer limit rather than a mandatory minimum. Its concrete operation remains separable from the validity of DAC8's reporting fields.

## Strategic consequence

The DAC2 chain is the strongest default route for an individual DAC8 claimant: section 24 DSG complaint, BVwG appeal, Article 267 request at the deciding court, then constitutional/administrative supreme-court review. At the same time, DAC2 means the merits theory must confront existing Austrian rejection of generalized tax-reporting objections and explain why DAC8's exact profile materially changes the Charter analysis.

## See Also

- [[dac8-vs-dac2-distinguishing-arguments|DAC8 versus DAC2: Distinguishing Arguments]] ([DAC8 versus DAC2: Distinguishing Arguments](../references/dac8-vs-dac2-distinguishing-arguments.md))
- [[dac8-charter-proportionality|DAC8 Charter Proportionality]] ([DAC8 Charter Proportionality](dac8-charter-proportionality.md))
- [[dac8-field-necessity-and-alternatives|DAC8 Field Necessity and Less-Intrusive Alternatives]] ([DAC8 Field Necessity and Less-Intrusive Alternatives](../references/dac8-field-necessity-and-alternatives.md))
- [[dac8-inference-linkage-and-error-evidence|DAC8 Inference, Linkage and Error Evidence]] ([DAC8 Inference, Linkage and Error Evidence](../references/dac8-inference-linkage-and-error-evidence.md))

## Sources

- [BVwG W211 2232955-1/7E](../../../legal-docs/core/at-bvwg-w211-2232955-1-7e.pdf)
- [VfGH E 2097/2021-13](../../../legal-docs/core/at-vfgh-e-2097-2021-13.pdf)
- [VwGH Ro 2023/04/0021-12](../../../legal-docs/core/at-vwgh-ro-2023-04-0021-12.pdf)
- [Directive 2014/107/EU (DAC2)](../../../legal-docs/core/eu-dac2-directive-2014-107.pdf)
- [Directive (EU) 2023/2226 (DAC8)](../../../legal-docs/core/eu-dac8-directive-2023-2226.pdf)
- [Commission impact assessment SWD(2022) 401](../../../legal-docs/supporting/eu-swd-2022-401-dac8-impact-assessment.pdf)
- [Krypto-MPfG, BGBl I 96/2025](../../../legal-docs/core/at-bgbl-i-96-2025-krypto-mpfg.pdf)
- [Austrian GMSG, consolidated snapshot](../../../legal-docs/core/at-gmsg-consolidated-2026.html)
