---
title: "Austrian Insider Database Misuse"
category: reference
sources:
  - raw/articles/2026-09-29-atinsider-ogh-database-query-rechtssaetze.md
  - raw/articles/2026-09-29-atinsider-ogh-17os10-15x-ais-tax-queries.md
  - raw/articles/2026-09-29-atinsider-bmf-dk-2016-ais-thousands-queries.md
  - raw/articles/2026-09-29-atinsider-bmf-dk-2019-ais-logfile-controls.md
  - raw/papers/2026-09-29-atinsider-bak-annual-reports-data-query-cases.md
  - raw/articles/2026-09-29-atinsider-bmi-ekis-logging-parliamentary-answers.md
  - raw/articles/2026-09-29-atinsider-rh-2011-pad-log-review-gap.md
  - raw/articles/2026-09-29-atinsider-bvwg-zmr-log-reconstruction-limits.md
  - raw/articles/2026-09-29-atinsider-ogh-14os26-24s-informant-data-leak.md
  - raw/articles/2026-09-29-atinsider-ott-verdict-intelligence-data-queries.md
  - raw/articles/2026-09-29-atinsider-media-tax-official-query-convictions.md
  - raw/articles/2026-09-29-atrisk-bao-automated-risk-management-legal-basis.md
created: 2026-09-29
updated: 2026-09-29
tags: [austria, insider-threat, amtsmissbrauch, ais, ekis, zmr, logging, bak, tax-secrecy]
aliases: [Amtsmissbrauch Datenabfrage, unbefugte EKIS-Abfrage, AIS Abfrage Finanzbeamter]
confidence: high
volatility: warm
verified: 2026-09-29
summary: "Austrian officials, including tax officials using the AIS tax system, are repeatedly prosecuted for private-purpose database queries under § 302 StGB, and the anti-corruption office registers about 100 to 116 such cases a year; detection in documented cases was mostly reactive and misuse ran for years, but logging, prosecution and sanctions exist and no case of tax-data misuse leading to violence was found."
---

# Austrian Insider Database Misuse

European insider cases are covered in [[insider-risk-controls-and-proof|Insider-Risk Controls and Proof]] ([Insider-Risk Controls and Proof](insider-risk-controls-and-proof.md)) and [[european-data-misuse-and-physical-risk|European Data Misuse and Physical-Risk Evidence]] ([European Data Misuse and Physical-Risk Evidence](european-data-misuse-and-physical-risk.md)). This reference adds the Austrian evidence: authorised officials querying state databases for private purposes, how they were detected and how they were sanctioned. Police, register and tax evidence are kept separate below.

## Legal treatment

OGH case law treats a query in EKIS (police information system), ZMR (central population register), court registers, social-insurance data or PAD (police case files) made "ohne dienstliche Veranlassung" (without official reason) as an official act. Such a query can amount to *Missbrauch der Amtsgewalt* (§ 302 StGB) where the required intent to harm is found (Rechtssätze RS0095301, RS0114637, RS0114317; for example 12 Os 2/09z, 11 Os 105/11t, 17 Os 20/12p, 14 Os 140/20z).

**Limits (adverse authority):**

- Querying data that are public or already known to the official falls outside § 302 (17 Os 1/12v).
- A conviction requires specific findings on which secret data were targeted. In 17 Os 10/15x (14 September 2015), a tax official had browsed AIS data on 27 colleagues out of curiosity; the conviction was set aside for want of such findings. The retrial outcome is unknown.

All tax cases found were prosecuted under §§ 302 and 310 StGB. The current FinStrG tax-secrecy offence was not verified.

## Tax-administration cases

| Case | Facts | Detection | Outcome | Evidence class |
|---|---|---|---|---|
| BMF Disziplinarkommission, 30 September 2016 | "mehrere tausend" (several thousand) AIS accesses in 2008–2014, including over 1,000 residents of the official's hometown | investigated by the BMF internal-affairs unit (BIA) and the anti-corruption office (BAK) for the prosecutor | final criminal sentence of six months suspended plus EUR 4,800; disciplinary fine EUR 5,000, not dismissal | disciplinary decision reciting a final judgment |
| BMF Disziplinarkommission, 6 August 2019 | 319 queries on the official's own relatives; querying continued after charges | a request about a different taxpayer triggered a log analysis | disciplinary fine EUR 15,000 | disciplinary decision |
| OGH 17 Os 10/15x (2015) | curiosity queries on 27 colleagues, 2008–2013 | not stated | conviction set aside | Supreme Court decision |
| Innsbruck, 2026, and four other press-reported cases (2015–2026) | private-purpose queries by tax officials | Innsbruck came to light "durch eine anonyme Anzeige" (through an anonymous report) | Innsbruck final (dismissal; six months conditional plus EUR 5,400); others unverified | media, labelled as such |

No case was found of an Austrian tax official passing taxpayer data to criminals, and none in which tax-data misuse led to threats or violence.

## Police and register cases

- **OGH 14 Os 26/24s (8 October 2024).** A Vorarlberg police officer's convictions stand for retrieving a police note containing an informant's name, date of birth and address and passing it to unknown persons. The informant had reported on extortion and violent clashes between criminal groups. The decision finds no resulting harm.
- **Egisto Ott (Landesgericht für Strafsachen Wien).** A jury found numerous personal-data queries without official reason, with the data passed to a Russian intelligence service in 2017–2022. The sentence was four years and one month. The verdict is not final, and the date is from secondary reports.

These show paid or state-actor tasking of authorised access. They concern police systems, not tax data.

## Scale

The Federal Anti-Corruption Office (BAK) categorised 116 of 852 new cases in 2024 (13.62 percent) and 98 of 754 in 2023 as "unbefugte Datenabfrage und Datenweitergabe" (unauthorised data query and disclosure). These are case registrations across the whole public sector, not convictions, and the pages read give no breakdown by ministry or database. No parliamentary answer from 2020 to 2026 with BMI or BMF counts of unauthorised-query cases was found.

## Logging is not detection

| System | Control documented | Gap documented |
|---|---|---|
| AIS (tax) | login warning that access is logged; BIA monitors lawfulness of access under a 2004 directive on occasion-driven log analysis ("Anlassbezogene Logfile-Auswertungen") | documented misuse ran for years (2008–2014); detection in the 2019 case was triggered by another matter; current 2026 review practice unknown |
| EKIS (police) | queries logged with mandatory purpose field and three-year retention; random-generator checks ordered in 2004 | in 2001 the BMI kept "keine Statistiken" (no statistics) on log reviews; about 29,500 users and 51 million accesses in 1999 |
| PAD (police files) | every query logged | Rechnungshof 2011: no random control routines; recommendation accepted |
| ZMR (register) | data-protection logs | BVwG 2016: logs could not show whether a historical-address query had occurred; technical logs deleted after 60 days |

The EKIS, PAD and ZMR descriptions date from 2001 to 2016 and are historical. § 48i BAO now requires tax-authority logs of queries and transmissions to be kept for at least three years; see [[austrian-tax-risk-scoring-and-financial-data-use|Austrian Tax Risk Scoring and Actual Use of Financial Data]] ([Austrian Tax Risk Scoring and Actual Use of Financial Data](austrian-tax-risk-scoring-and-financial-data-use.md)).

## Adverse evidence

- Logging, per-user traceability, purpose fields, login warnings, BIA oversight and random checks exist. A Rechnungshof recommendation on PAD was accepted.
- Detected cases are prosecuted and sanctioned.
- The OGH narrows criminal liability through the public-data and specificity requirements.
- Case numbers are small relative to the volume of authorised access.
- No Austrian case links tax-data misuse to physical harm.

## Transfer to the Austrian DAC8 proceeding

- DAC8 data will sit in tax-administration systems accessed by many authorised officials. Austrian evidence shows that private-purpose queries in the AIS tax system have occurred, sometimes at scale and over years, and were found mainly reactively.
- This supports asking concretely how DAC8 data will be accessed, logged and proactively reviewed. It does not show that DAC8 data will be misused or that Austrian tax data have caused harm.
- The strongest request would be for current AIS access-review practice and any DAC8-specific access design, through the routes in [[austrian-security-evidence-access|Austrian Security-Evidence Access]] ([Austrian Security-Evidence Access](austrian-security-evidence-access.md)).

## Claims to exclude

- "Austrian tax officials sell taxpayer data to criminals."
- "Tax-data misuse has led to attacks in Austria."
- "Austrian authorities do not log database access."
- "BAK figures are conviction counts."

## See Also

- [[insider-risk-controls-and-proof|Insider-Risk Controls and Proof]] ([Insider-Risk Controls and Proof](insider-risk-controls-and-proof.md)) — European controls and evidence classes.
- [[european-data-misuse-and-physical-risk|European Data Misuse and Physical-Risk Evidence]] ([European Data Misuse and Physical-Risk Evidence](european-data-misuse-and-physical-risk.md)) — Dutch, Finnish and French insider cases.
- [[austrian-tax-risk-scoring-and-financial-data-use|Austrian Tax Risk Scoring and Actual Use of Financial Data]] ([Austrian Tax Risk Scoring and Actual Use of Financial Data](austrian-tax-risk-scoring-and-financial-data-use.md)) — BAO logging and access-right restrictions.
- [[austrian-security-evidence-access|Austrian Security-Evidence Access]] ([Austrian Security-Evidence Access](austrian-security-evidence-access.md)) — routes to obtain access-review evidence.

## Sources

- [OGH Rechtssätze on database queries](../../raw/articles/2026-09-29-atinsider-ogh-database-query-rechtssaetze.md)
- [OGH 17 Os 10/15x](../../raw/articles/2026-09-29-atinsider-ogh-17os10-15x-ais-tax-queries.md)
- [BMF Disziplinarkommission 2016](../../raw/articles/2026-09-29-atinsider-bmf-dk-2016-ais-thousands-queries.md)
- [BMF Disziplinarkommission 2019](../../raw/articles/2026-09-29-atinsider-bmf-dk-2019-ais-logfile-controls.md)
- [BAK annual reports 2023–2024](../../raw/papers/2026-09-29-atinsider-bak-annual-reports-data-query-cases.md)
- [BMI EKIS logging answers](../../raw/articles/2026-09-29-atinsider-bmi-ekis-logging-parliamentary-answers.md)
- [Rechnungshof 2011 PAD review gap](../../raw/articles/2026-09-29-atinsider-rh-2011-pad-log-review-gap.md)
- [BVwG ZMR log limits](../../raw/articles/2026-09-29-atinsider-bvwg-zmr-log-reconstruction-limits.md)
- [OGH 14 Os 26/24s](../../raw/articles/2026-09-29-atinsider-ogh-14os26-24s-informant-data-leak.md)
- [Ott verdict](../../raw/articles/2026-09-29-atinsider-ott-verdict-intelligence-data-queries.md)
- [Media reports on tax-official convictions](../../raw/articles/2026-09-29-atinsider-media-tax-official-query-convictions.md)
- [BAO legal basis digest](../../raw/articles/2026-09-29-atrisk-bao-automated-risk-management-legal-basis.md)
