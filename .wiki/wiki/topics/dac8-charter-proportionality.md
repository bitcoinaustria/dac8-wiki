---
title: "DAC8 Charter Proportionality"
category: topic
sources:
  - raw/articles/2026-08-27-eu-directive-2023-2226-dac8.md
  - raw/articles/2026-08-27-dac8-impact-assessment-swd-2022-401.md
  - raw/articles/2026-08-27-edps-opinion-9-2023-dac8.md
  - raw/articles/2026-08-27-cjeu-digital-rights-ireland.md
  - raw/articles/2026-08-27-cjeu-c-623-22-dac6.md
  - raw/articles/2026-08-27-cjeu-c175-20-sia-ss-tax-data.md
  - raw/articles/2026-08-27-vfgh-e-2097-2021-dac2.md
  - raw/articles/2026-08-27-ecthr-ferrieri-bonassisa-financial-data-remedy.md
  - raw/articles/2026-08-27-ecthr-gsb-v-switzerland.md
  - raw/articles/2026-08-30-austria-dsg-section-1-fundamental-right.md
  - raw/articles/2026-08-30-eu-charter-rights-review-framework.md
  - raw/articles/2026-08-30-vfgh-u466-2011-charter-review-standard.md
  - raw/articles/2026-08-30-dac8-impact-assessment-evidence-and-options.md
  - raw/articles/2026-08-30-edps-opinion-9-2023-dac8-detailed-extraction.md
  - raw/articles/2026-08-30-cjeu-c394-23-mousse-data-minimisation.md
  - raw/articles/2026-08-30-cjeu-c484-24-nth-haustechnik.md
  - raw/articles/2026-08-30-cjeu-c57-23-policejni-retention-review.md
  - raw/articles/2026-08-30-austria-eu-ahg-sections-15-19.md
  - raw/articles/2026-08-27-cjeu-etat-luxembourgeois-tax-information-remedy.md
  - raw/articles/2026-08-27-cjeu-la-quadrature-c-470-21.md
  - raw/articles/2026-09-04-cjeu-la-quadrature-bulk-data-categories.md
  - raw/articles/2026-09-04-cjeu-ligue-bulk-profiling-safeguards.md
  - raw/articles/2026-09-04-ecthr-big-brother-watch-end-to-end-safeguards.md
  - raw/articles/2026-09-04-ecthr-s-marper-data-lifecycle-effectiveness.md
created: 2026-08-27
updated: 2026-09-04
tags: [dac8, charter-articles-7-8, proportionality, data-protection, tax-information-exchange]
aliases: [DAC8 fundamental rights, DAC8 privacy challenge]
confidence: medium
volatility: warm
verified: 2026-08-30
summary: "DAC8 interferes with privacy and data protection, but a validity case must prove disproportionate inference, retention, access, or remedy effects while confronting strong tax-reporting counterauthority."
---

# DAC8 Charter Proportionality

> The interference is clear. Invalidity is not: the analysis turns on the exact fields, their inference value, pre-report processing, retention, authority access, safeguards, and remedies.

## Exact reporting profile

DAC8 links identification and tax-residence data to annual aggregates organized by crypto asset and transaction category. Depending on the category, the report includes fiat amounts, fair-market values, units, and counts for acquisitions, disposals, reportable retail payments, and transfers. It also includes aggregate value and units for transfers to DLT addresses not known by the provider to be associated with a virtual asset service provider or financial institution.

It does **not** report transaction dates, transaction identifiers, counterparties, wallet addresses, or DLT addresses. The external-address field contains annual aggregate value and units, not an address or transaction count. A blockchain-correlation theory needs separate evidence showing how a provider or authority obtains and links those additional facts.

## Claimant fit changes the claim

An ordinary natural person who is tax-resident in Austria is normally a reportable user. Removing Austria's all-customer language from section 20(1) would therefore not remove that person's DAC8-mandated section 18 processing. As to those fields, their claim reaches the EU baseline and must overcome the adverse DAC2 and DAC6 authorities; separate Austrian choices such as retention duration and safeguards remain reviewable.

A narrower national case is strongest for a genuinely non-reportable user whose provider creates or stores the complete section 18 annual aggregate tax profile, particularly after reportable status has been determined. Creation of that profile during an open status check may also be excessive if the provider could determine status with less data. Universal self-certification and status checks remain part of DAC8 and are not the same alleged excess.

## Strongest challenge theory

- for a reportable user, the challenged interference is DAC8 itself; for a non-reportable user, the distinct issue is Austria's additional section 18 aggregate-profile processing;
- coverage is routine and not based on individualized suspicion;
- due diligence and reportability decisions can require processing a broader customer population than the final transmitted set;
- identity, home address, per-asset values/units/counts, high-value payment use, and transfer categories may permit a materially richer annual profile than the bank-account facts considered in Austrian DAC2 litigation;
- Austria enacted a ten-year deletion date for transmitted information and a ten-year documentation duty; their scope and operation differ, and section 20(4) may operate as a ceiling rather than a mandatory minimum;
- Article 16 permits several tax, customs, AML/CFT and related uses plus conditional further use; every actual use still needs to remain within the statutory purpose and safeguards;
- cross-border authority access, correction propagation, security, and judicial remedies must operate effectively;
- targeted requests, risk-based selection, shorter retention, or narrower data categories matter only if shown to be equally effective.

## Counterauthority that must be answered

The legal intensity does not follow from calling DAC8 surveillance, bulk processing or a wealth register. The governing factors are the precise data categories, their demonstrated inference and linkage capacity, the purposes, access and onward use, duration, safeguards and effective review. The routine report is not a current-holdings register and contains no wallet address, transaction hash, transaction timestamp or counterparty.

- VfGH E 2097/2021 and VwGH Ro 2023/04/0021 upheld DAC2/CRS reporting and rejected no-threshold, all-customer processing, security-risk, and reference arguments.
- CJEU C-623/22 broadly upheld DAC6's precision and proportionality; C-694/20 is limited to lawyer-client confidentiality.
- C-623/22 treated DAC6 as early and targeted information about hallmarked potential-risk arrangements, which distinguishes but does not neutralise it. C-484/24 places the complete balance at the legislative-basis level; by analogy, its court-specific holding does not support a fresh full balance for every later CASP or authority operation.
- C-57/23 concerns biometric and genetic police data under Directive 2016/680. It rejects a categorical fixed-maximum rule only where legislation sets appropriate review intervals and every extension remains strictly necessary; it does not validate a default ten-year tax-retention practice.
- G.S.B. and Othymia accept tax-information transmission within a lawful, reviewable framework.
- Digital Rights Ireland, Tele2/Watson, La Quadrature C-511/18 and Others, SpaceNet, and Garda principally concern revealing communications traffic/location data used for security or law enforcement. La Quadrature C-470/21 is adverse nuance: it permits generalised retention of separated IP-address data that cannot generate a detailed profile and ties access safeguards to linkability.
- Schecke and Luxembourg Business Registers concern public disclosure; DAC8 exchange is not public.

## Better supporting authorities

Valsts ieņēmumu dienests, C-175/20, is useful for purpose specificity, minimization, time limits, and review in a tax-authority setting. Mousse, C-394/23, strengthens the analogy for objectively indispensable fields and equally effective alternatives. Ligue des droits humains and Opinion 1/15 supply rigorous safeguards for systematic profiling and automated analysis. Schrems I and Berlioz reinforce independent review where personal data cross borders or support tax enforcement.

These cases more naturally support narrowing interpretation and implementation safeguards than automatic facial invalidity.

## What a rights-based success could deliver

In a DSB/BVwG or GDPR judicial route, section 1 DSG, the GDPR and Charter Articles 7, 8 and 52 can support a narrow interpretation, processing restriction or deletion remedy. In Article 140 review, the VfGH can partially annul an unnecessary national extension but does not order individual deletion. Article 47 Charter and the procedural dimension of Article 8 ECHR support timely and effective review, not an automatic right to a direct Article 140 filing. Joined Cases C-245/19 and C-246/19 reject a categorical taxpayer right to direct pre-transfer review where effective later tax proceedings and GDPR Article 79 protection exist; a DAC8 claimant must show why no later route supplies comparable review. Directive-wide DAC8 invalidity remains the outer and materially weaker outcome.

## Evidence still needed

- an identifiable claimant, all tax residencies, an identifiable CASP, and proof of actual section 18 processing;
- real CASP notices, self-certification flows, access responses, and retention schedules;
- a field-by-field Austrian-to-EU schema map;
- proof of who can access which data, for how long, and with what logs/oversight;
- the actual Article 16/EU-AHG section 15 basis for every tax, customs, AML/CFT or other downstream use;
- the exact Article 25/EU-AHG section 19 basis and facts for any restriction of notice or access;
- a technically supported public-ledger correlation demonstration using the fields actually retained by the provider;
- evidence of physical-security threat pathways beyond general crypto-crime statistics;
- a quantified comparison with narrower tax-information tools.

## See Also

- [[non-eu-tax-resident-claimant-advantage|Drittstaaten-Steueransässigkeit als Klägerprofil]] ([Drittstaaten-Steueransässigkeit als Klägerprofil](../theses/non-eu-tax-resident-claimant-advantage.md))
- [[dac8-vs-dac2-distinguishing-arguments|DAC8 versus DAC2: Distinguishing Arguments]] ([DAC8 versus DAC2: Distinguishing Arguments](../references/dac8-vs-dac2-distinguishing-arguments.md))
- [[dac2-crs-austrian-litigation|Austrian DAC2/CRS Litigation]] ([Austrian DAC2/CRS Litigation](dac2-crs-austrian-litigation.md))
- [[dac8-com-argument-audit|DAC8.com and Bull Bitcoin Argument Audit]] ([DAC8.com and Bull Bitcoin Argument Audit](../references/dac8-com-argument-audit.md))
- [[austria-eu-precedent-matrix|Austria and EU Precedent Matrix]] ([Austria and EU Precedent Matrix](../references/austria-eu-precedent-matrix.md))
- [[dac8-fundamental-rights-and-public-risks|DAC8 Fundamental Rights and Public Risks]] ([DAC8 Fundamental Rights and Public Risks](dac8-fundamental-rights-and-public-risks.md))
- [[mica-tfr-krypto-mpfg-nexus|MiCA, TFR, and the Krypto-MPfG Nexus]] ([MiCA, TFR, and the Krypto-MPfG Nexus](mica-tfr-krypto-mpfg-nexus.md))
- [[dac8-field-necessity-and-alternatives|DAC8 Field Necessity and Less-Intrusive Alternatives]] ([DAC8 Field Necessity and Less-Intrusive Alternatives](../references/dac8-field-necessity-and-alternatives.md))
- [[dac8-inference-linkage-and-error-evidence|DAC8 Inference, Linkage and Error Evidence]] ([DAC8 Inference, Linkage and Error Evidence](../references/dac8-inference-linkage-and-error-evidence.md))
- [[dac8-data-lifecycle-access-retention-remedies|DAC8 Data Lifecycle: Access, Retention and Remedies]] ([DAC8 Data Lifecycle: Access, Retention and Remedies](../references/dac8-data-lifecycle-access-retention-remedies.md))
- [[dac8-bulk-data-case-transfer-matrix|DAC8 Bulk-Data Case Transfer Matrix]] ([DAC8 Bulk-Data Case Transfer Matrix](../references/dac8-bulk-data-case-transfer-matrix.md))

## Sources

- [DAC8](../../../legal-docs/core/eu-dac8-directive-2023-2226.pdf)
- [Austrian DAC2 VfGH decision](../../../legal-docs/core/at-vfgh-e-2097-2021-13.pdf)
- [CJEU C-623/22](../../../legal-docs/core/eu-cjeu-c623-22-belgian-tax-lawyers.pdf)
- [CJEU data and proportionality corpus](../../../legal-docs/_index.md)
