---
title: "BMF Predictive Analytics Competence Center: official self-description and annual results 2022-2024"
source: "https://www.bmf.gv.at/themen/betrugsbekaempfung/einheiten-betrugsbekaempfung/Predictive-Analytics-Competence-Center.html"
type: articles
ingested: 2026-09-29
fetched: 2026-09-29
content_format: html
confidence: medium
tags: [austria, bmf, pacc, predictive-analytics, machine-learning, risk-scoring, audit-selection, human-review, art-22-gdpr, primary-institutional]
summary: "BMF and BRZ describe PACC as an ML risk-scoring unit covering millions of cases a year, including real-time scoring of new businesses and the persons behind them. They say only BMF auditors assess additional tax. None of the pages names CRS, DAC2 or DAC8 data as model inputs."
---

# BMF Predictive Analytics Competence Center: official self-description and annual results 2022-2024

**Sources read on 2026-09-29.** (1) BMF unit page (canonical URL above; undated). (2) BMF press release of 9 August 2024 on the 2023 results: https://www.bmf.gv.at/presse/pressemeldungen/2024/august/pacc-bilanz.html. (3) BMF press release of 13 August 2025 on the 2024 results: https://www.bmf.gv.at/presse/pressemeldungen/2025/august/pacc-ki.html. (4) BRZ page, undated but citing figures for the first half of 2023: https://www.brz.gv.at/was-wir-tun/services-produkte/mehr-gerechtigkeit-fuer-alle.html. BRZ is the federal IT provider that co-develops the algorithms.

**Function.** The unit page says PACC trains mathematical models, mainly supervised machine learning, on historical data and applies them to current data. Its stated main tasks are "Echtzeit-Risikobewertung" (real-time risk assessment), "die zentrale Prüfungsfallauswahl" (central selection of audit cases), automated audits, business start-ups, VAT carousel analysis, and support for data management and fraud-fighting. The 2024 release says new business registrations are checked in advance "um Unternehmen und die dahinterstehenden handelnden Personen mit einem höheren Risiko für Steuerbetrug zu identifizieren" (to identify businesses, and the persons acting behind them, with a higher tax-fraud risk). The same release says PACC also handles e-commerce platform data "und den internationalen Datenaustausch von Steuerinformationen" (and the international exchange of tax information). In both releases the PACC head lists crypto-currencies and "internationale Datenaustauschprogramme" among the topics PACC covers. The 2025 release says cases are proposed on the basis of "historischen Daten, Finanzdaten und anderen relevanten Informationen". BRZ quotes the PACC head as saying that the algorithms "diese Unregelmäßigkeiten automatisch zu erkennen und die relevanten Fälle einer gesonderten Prüfung zuzuführen" (detect irregularities automatically and route the relevant cases to a separate audit). The irregularities he lists include false statements about "Vermögensverhältnisse" (financial or asset circumstances). BRZ puts PACC at about 40 staff.

**Figures reported by the BMF and BRZ:**

| Year | Cases checked by risk models | Compliance checks | Additional tax attributed | Source |
|---|---|---|---|---|
| 2022 | about 6 million employee assessments; about 5,000 risk cases selected for audit each year | n/a | about EUR 600 million over three years | BRZ |
| 2023 | about 6.5 million | about 27.5 million | about EUR 185 million; 375,000 of 34 million cases flagged as implausible | BMF, 9 Aug 2024 |
| 2024 | about 6.6 million | about 23.4 million | about EUR 354 million | BMF, 13 Aug 2025 |

**Human review.** The unit page says: "die Festsetzung von Mehrergebnis an Steuerrückforderungen immer nur und ausschließlich durch die Prüforgane des BMF durchgeführt wird. Das PACC hat hier die Stellung einer Dienstleistungsabteilung, die Hinweise auf die risikoreichen Fälle zur Verfügung stellt." In English: additional tax is always and only assessed by BMF auditors, and PACC acts as a service unit that supplies indications of high-risk cases. The 2024 release says flagged cases "wurden in Folge von Sachbearbeiterinnen und Sachbearbeitern näher unter die Lupe genommen und im Bedarfsfall überprüft" (were then examined more closely by caseworkers and audited where necessary). BRZ also describes some favourable decisions that are automated: more than 100,000 family-allowance claims were extended automatically in one year. It lists planned uses: real-time scoring of goods shipments, and large language models to draft letters "oder Bescheide" (or administrative decisions).

**Evidence class and limits.** These are institutional self-descriptions and press statements, not audited results. The revenue figures are attributions by the BMF itself, and the sources give no method, error rate, false-positive rate or appeal outcome. The sources support these points:

- Austria operates large-scale automated risk scoring of identified taxpayers.
- Scores determine which cases are selected for audit or review.
- PACC's remit includes international data exchange.

They do not show that CRS/DAC2 or DAC8 data are model features. They also do not show that a score alone produces a decision with legal or similarly significant effect. The BMF's position, which a SCHUFA argument must engage with, is that the score only selects cases for review and a human official decides. Under CJEU C-634/21, the relevant question is whether a score "strongly" determines the outcome. Audit selection itself, and the extent to which officials depart from the score, are not documented. **Missing:** no source found stating whether Krypto-MPfG/DAC8 data feed PACC models.
