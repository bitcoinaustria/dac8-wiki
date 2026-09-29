---
title: "Austrian Tax Risk Scoring and Actual Use of Financial Data"
category: reference
sources:
  - raw/articles/2026-09-29-atrisk-bmf-pacc-risk-scoring-self-description.md
  - raw/articles/2026-09-29-atrisk-ab-2592-pacc-ml-methods-and-data-basis.md
  - raw/articles/2026-09-29-atrisk-ab-2541-abb-fraud-data-and-account-openings.md
  - raw/articles/2026-09-29-atrisk-ab-4507-bbkg-2025-data-part-revenue.md
  - raw/articles/2026-09-29-atrisk-bao-automated-risk-management-legal-basis.md
  - raw/articles/2026-09-29-atrisk-kontenregister-query-statistics-2018-2022.md
  - raw/papers/2026-09-29-atrisk-rh-2019-33-international-exchange-matching.md
  - raw/papers/2026-09-29-atrisk-rh-2023-26-pacc-audit-selection.md
  - raw/papers/2026-09-29-atrisk-abb-annual-reports-2024-2025.md
  - raw/articles/2026-09-29-atrisk-ab-1948-crypto-tax-revenue-data.md
  - raw/articles/2026-09-29-profiling-cjeu-c634-21-schufa-scoring.md
created: 2026-09-29
updated: 2026-09-29
tags: [austria, bmf, pacc, risk-scoring, article-22-gdpr, bao, kontenregister, dac2, proportionality]
aliases: [PACC, Predictive Analytics Competence Center, Austrian tax scoring, § 114 Abs 4 BAO]
confidence: medium
volatility: hot
verified: 2026-09-29
summary: "The BMF's Predictive Analytics Competence Center scores about 6.6 million cases a year with machine-learning models under the broad § 114(4) BAO purpose clause, and its remit includes international data exchange; no source states that CRS, DAC2 or DAC8 data are model inputs, officials rather than models set tax, and the Kontenregister is queried only about 5,500 to 7,500 times a year."
---

# Austrian Tax Risk Scoring and Actual Use of Financial Data

Two questions matter for an Austrian DAC8 challenge. Does the tax administration score taxpayers automatically, which would open the CJEU *SCHUFA* (C-634/21) line under Article 22 GDPR? And how often does it actually use the financial data it already collects, which bears on necessity and proportionality?

## What PACC does

The BMF's Predictive Analytics Competence Center (PACC), with about 40 staff and IT from the federal provider BRZ, trains mainly supervised machine-learning models on the BMF's own historical data. Its stated tasks include "Echtzeit-Risikobewertung" (real-time risk assessment), "die zentrale Prüfungsfallauswahl" (central selection of audit cases), start-up checks and VAT-carousel analysis. New business registrations are checked to identify businesses "und die dahinterstehenden handelnden Personen" (and the persons acting behind them) with higher fraud risk.

| Year | Cases checked by risk models | Additional tax attributed by the BMF | Source |
|---|---|---|---|
| 2022 | about 6 million employee assessments; about 5,000 risk cases selected for audit a year | about EUR 600 million over three years | BRZ |
| 2023 | about 6.5 million; 375,000 of 34 million cases flagged as implausible | about EUR 185 million | BMF, 9 August 2024 |
| 2024 | about 6.6 million | about EUR 354 million | BMF, 13 August 2025 |

These figures are BMF self-attributions without published method, error or false-positive rates. A parliamentary answer (2592/AB) states that machine learning has been used since 2016 in customs audits, family allowance, employee and business assessment and start-up checks. It adds that data sources are used only where there is "eine eindeutige gesetzliche Grundlage" (a clear legal basis). The Rechnungshof (2023/26) confirms that "hochentwickelte IT–Analysen zur Fallauswahl" select tax audits and recommended extending PACC to criminal tax cases.

**Exchanged data.** PACC press releases list "internationale Datenaustauschprogramme" and crypto among its topics. The Rechnungshof (2019/33) found that about 86 percent of DAC1 records were matched to taxpayers automatically, while DAC2 matching of about 357,000 records received in September 2017 was still being tested. Promised worklists, including cases "von der automatisierten Risikobewertung ausgewählt" (selected by automated risk assessment), had not been delivered. The fraud office (ABB) reports that DAC reports arrive automatically but that criminal assessment is done by staff.

**Missing.** No source states that CRS, DAC2 or DAC8 data are PACC model features. No published data-source list, DPIA, override rate or current CRS matching rate was found.

**Conflicting answer.** Answer 2541/AB, given a day before 2592/AB, states "Es erfolgt keine KI-gestützte Mustererkennung" (no AI-based pattern recognition takes place) in detecting tax fraud. The likely reconciliation is that 2541/AB concerns the fraud office and criminal proceedings and 2592/AB concerns assessment and audit. That reading is an inference.

## Legal basis

- **§ 114(4) BAO** (Deregulierungsgesetz 2017; current wording since 25 May 2018) permits processing of personal and non-personal data "für Zwecke des automationsunterstützten Risikomanagements und der Betrugsbekämpfung" (for automated risk management and fraud-fighting), to the extent that it is suitable, necessary and appropriate. It names no data sources, model types or scoring-specific safeguards.
- **§ 48b BAO** is the general basis for automated processing, including Article 9(2)(g) GDPR special-category data.
- **§ 48e(1)(1)(b) and § 48f(1)(1) BAO** exclude information and access rights where disclosure could allow "Rückschlüsse auf die Ausgestaltung automationsunterstützter Risikomanagementsysteme" (inferences about how automated risk-management systems are designed).
- **§ 48i BAO** requires logs of queries and transmissions to be kept for at least three years.
- **§ 96(2) BAO** covers machine-generated documents without signature.
- A text search of the consolidated BAO found no reference to Article 22 GDPR and no express Article 22(2)(b) authorisation. Other tax statutes were not searched. The §§ 48e–48i numbering appears to date from a 2025 renumbering; older literature may cite different sections.

## The SCHUFA question

Under C-634/21 paras 43–50, an automated score is itself an Article 22 decision where a third party draws on it "strongly". A national authorisation must respect Articles 5 and 6 (paras 65–68).

- **For the argument:** mass automated scoring of identified persons exists. Audit selection follows the score, the legal basis is a broad purpose clause, and scoring logic can be withheld from data subjects.
- **Against it:** the BMF, the ABB and the Rechnungshof consistently describe officials as those who set tax or take investigative steps. The BMF says additional tax is assessed "immer nur und ausschließlich durch die Prüforgane" (always and only by auditors). § 114(4) contains an express necessity and proportionality test.
- **What would be needed:** evidence that audit or review selection is itself strongly determined by the score and produces significant effects, and that DAC8 data enter the models. Neither is documented. A request under the IFG or an Article 15 GDPR request would meet the § 48e/§ 48f restrictions. See [[austrian-security-evidence-access|Austrian Security-Evidence Access]] ([Austrian Security-Evidence Access](austrian-security-evidence-access.md)).

## Actual use of financial data

**Kontenregister queries**, from BMF and BMJ answers to parliamentary questions:

| Year | Prosecutors | Criminal-tax authorities | Tax authorities | Total |
|---|---|---|---|---|
| 2018 | 1,242 | 335 | 5,169 | 6,757 |
| 2019 | 1,680 | 260 | 5,498 | 7,454 |
| 2020 | 1,802 | 245 | 3,414 | 5,469 |
| 2021 | 1,993 | 213 | 3,841 | 6,061 |
| 2022 | 1,877 | 225 | 5,025 | 7,140 |

Totals include small numbers of court, BFG and § 4(5) queries. Account inspections approved by the BFG were at most two a year. The ABB's suspicion-based account openings numbered 75 to 417 a year from 2019 to 2025, with counting differences between sources. No figures for 2023 onwards and no VfGH decision on the Kontenregister were found.

These figures support an argument that universal collection outruns actual use: a register covering essentially all account relationships is queried a few thousand times a year, against millions of assessments. They equally support the State's comparator argument that central relationship metadata with logged, case-by-case access and judicial gating of substance is a minimising design. DAC8 data are transactional and arrive in bulk for all reportable users, so the comparison needs care.

## Benefit estimates

- The BMF plans EUR 110 million in total revenue for 2026–2029 from the data part of the 2025 fraud-fighting act (BGBl. I 96/2025, which includes the Krypto-MPfG), with no breakdown by measure.
- Declared crypto income was EUR 35.6 million (2022) and EUR 14.6 million (2023, incomplete). Crypto withholding tax (KESt) was EUR 33.8 million in 2024, 0.57 percent of all KESt.

These are baselines and plans, not a measured DAC8 yield.

## Claims to exclude

- "Austria's tax administration makes automated decisions about taxpayers based on DAC8 data."
- "PACC uses CRS or DAC8 data."
- "The Kontenregister is rarely used" without stating that about 6,000 to 7,500 queries a year were made.
- "The BMF's revenue attributions are audited results."

## See Also

- [[austrian-insider-database-misuse|Austrian Insider Database Misuse]] ([Austrian Insider Database Misuse](austrian-insider-database-misuse.md)) — insider misuse of the AIS tax system.
- [[transaction-profiling-and-sensitive-inference|Profiling and Sensitive Inference from Transaction Records]] ([Profiling and Sensitive Inference from Transaction Records](transaction-profiling-and-sensitive-inference.md)) — SCHUFA and Article 9 inference tests.
- [[dac8-and-the-wealth-register-risk|DAC8 and the Wealth-Register Risk]] ([DAC8 and the Wealth-Register Risk](../topics/dac8-and-the-wealth-register-risk.md)) — Kontenregister and register-combination context.
- [[dac8-aeoi-effectiveness-and-evidence-limits|DAC8, AEOI Effectiveness and Evidence Limits]] ([DAC8, AEOI Effectiveness and Evidence Limits](dac8-aeoi-effectiveness-and-evidence-limits.md)) — effectiveness evidence for exchanged data.
- [[austrian-security-evidence-access|Austrian Security-Evidence Access]] ([Austrian Security-Evidence Access](austrian-security-evidence-access.md)) — routes to obtain data-source and DPIA evidence.

## Sources

- [BMF PACC self-description and press releases](../../raw/articles/2026-09-29-atrisk-bmf-pacc-risk-scoring-self-description.md)
- [2592/AB: machine-learning methods and data basis](../../raw/articles/2026-09-29-atrisk-ab-2592-pacc-ml-methods-and-data-basis.md)
- [2541/AB: fraud-office data and account openings](../../raw/articles/2026-09-29-atrisk-ab-2541-abb-fraud-data-and-account-openings.md)
- [4507/AB: revenue from the data package](../../raw/articles/2026-09-29-atrisk-ab-4507-bbkg-2025-data-part-revenue.md)
- [BAO legal basis for automated risk management](../../raw/articles/2026-09-29-atrisk-bao-automated-risk-management-legal-basis.md)
- [Kontenregister query statistics 2018–2022](../../raw/articles/2026-09-29-atrisk-kontenregister-query-statistics-2018-2022.md)
- [Rechnungshof 2019/33](../../raw/papers/2026-09-29-atrisk-rh-2019-33-international-exchange-matching.md)
- [Rechnungshof 2023/26](../../raw/papers/2026-09-29-atrisk-rh-2023-26-pacc-audit-selection.md)
- [ABB annual reports 2024–2025](../../raw/papers/2026-09-29-atrisk-abb-annual-reports-2024-2025.md)
- [1948/AB: crypto tax revenue](../../raw/articles/2026-09-29-atrisk-ab-1948-crypto-tax-revenue-data.md)
- [CJEU C-634/21 SCHUFA](../../raw/articles/2026-09-29-profiling-cjeu-c634-21-schufa-scoring.md)
