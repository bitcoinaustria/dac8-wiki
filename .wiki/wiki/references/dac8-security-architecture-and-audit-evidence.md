---
title: "DAC8 Security Architecture and Audit Evidence"
category: reference
sources:
  - raw/articles/2026-09-04-dac8-security-controller-breach-architecture.md
  - raw/articles/2026-09-04-austria-eu-ahg-section-19a-breach-response.md
  - raw/articles/2026-09-04-mica-dora-casp-security-baseline.md
  - raw/articles/2026-09-04-austria-rechnungshof-bmf-it-security-audit.md
  - raw/articles/2026-09-04-cjeu-c340-21-tax-authority-breach-security.md
created: 2026-09-04
updated: 2026-09-19
tags: [dac8, security, audit, bmf, brz, ccn, dora, evidence, adverse-authority]
aliases: [DAC8 security safeguards, BMF security evidence]
confidence: high
volatility: hot
verified: 2026-09-04
summary: "Separates binding DAC8, MiCA and DORA safeguards from the still-unproved implementation facts needed for a concrete security challenge."
---

# DAC8 Security Architecture and Audit Evidence

> The useful security claim is not that safeguards are absent. Binding safeguards exist, and the Austrian Court of Audit records a substantial BMF control environment. The open issue is whether the concrete DAC8 data chain implements adequate, necessary and effective controls for its particular data combination, users, copies and retention.

## Control map

| Layer | Established safeguard | Fact still to prove |
|---|---|---|
| Provider | GDPR Articles 25 and 32; MiCA Article 68; DORA monitoring, segmentation, detection, response and testing | DAC8 data flow, privileges, joins, bulk-export capability, subcontractors, logs, backup retention and tested effectiveness |
| Austrian authority | GDPR, DAC Article 21 national-system security, DAC Article 25 controller status and EU-AHG section 19a response | production architecture, data classification, role matrix, interface and export controls, anomaly detection, audit results and deletion propagation |
| CCN | Commission responsibility for network security and limited accredited technical access | operating controls and relevant audit or incident evidence |
| Central directory | residence-gated Member-State access; Commission statistics-only access; breach suspension and remediation | operational readiness, field-level access, logging, exceptional access and copy lifecycle |
| Recipient authority | GDPR controller duties and Member-State security responsibility | identity and permissions of recipients, onward use, joins, retention, correction, deletion and breach history |

## Austrian audit evidence

The 2024 Court of Audit report is important adverse authority. It records BMF ISO 27001 and ISO 27701 certification, standardised reporting, installed IDS/IPS and SIEM, 255 reviews over 2018 to 2022, monthly BRZ vulnerability scans and a conclusion that the BMF could detect, analyse and reduce security risks to a high degree.

Its limits are precise:

- the review principally covers 2018 to 2022, before the Krypto-MPfG;
- it examined selected security-management aspects, not the later DAC8 system;
- service-provider security management, including BRZ, was outside scope;
- no DAC8 field, access, export, retention or deletion design was reviewed;
- the BMF had no social-engineering audit during the period, although it said operational risk management covered the risk;
- a dedicated BRZ SOC was only in preparation in June 2023, with CERT performing the function.

Those limits justify targeted evidence requests. They do not prove a control defect. The absence of social-engineering testing in that historical audit cannot be used as the cause of any later incident.

## Breach response is not prevention

DAC Article 25 and EU-AHG section 19a provide notification, containment, exchange suspension, CCN suspension and remediation. Those mechanisms reduce systemic harm and must be acknowledged. They are reactive. A necessity and security review still asks whether the dataset, access population and retention were minimised before any breach.

The Directive's affected-person notification rule should not be turned into a pleaded Austrian transposition defect without checking its exact DAC8 personal scope and all implementing law. The terminology does not line up cleanly between `Reportable Person` and `Reportable User`.

## Proof package

A security limb becomes concrete only if the proceedings obtain and test:

1. the controller and processor chain at every copy;
2. data-flow and trust-boundary diagrams from provider to recipient authority;
3. a field-level role and export matrix, including administrator and contractor access;
4. logging coverage, retention and alert thresholds for consultation and bulk extraction;
5. segmentation of tax identity, contact/address, transaction aggregate and address-bearing MiCA/TFR records;
6. the DAC8-specific risk assessment, DPIA or Article 35(10) legislative assessment relied on;
7. security-test scope, findings, remediation and residual-risk acceptance;
8. backup, correction, deletion and breach-notification propagation across all copies.

CJEU C-340/21 supplies the discipline: the assessment concerns the nature, content, implementation and practical effect of the measures against the concrete processing risks. A breach alone is not proof of inadequate measures.

## Claims to exclude

- the BMF or BRZ has inadequate security merely because a future breach is possible;
- the Court of Audit found a defect in a DAC8 system it did not examine;
- certification proves that every later DAC8 control is adequate;
- DORA or MiCA authorises tax-purpose reuse of separate records;
- DAC breach-response rules erase the need for prevention and minimisation;
- an unverified terminology or implementation gap establishes a breach-notification violation.

## See Also

- [[tax-exchange-confidentiality-and-suspension|Tax-Exchange Confidentiality, Review and Suspension]] ([Tax-Exchange Confidentiality, Review and Suspension](tax-exchange-confidentiality-and-suspension.md)) — actual suspension, restored exchange and current review benchmarks.
- [[insider-risk-controls-and-proof|Insider-Risk Controls and Proof]] ([Insider-Risk Controls and Proof](insider-risk-controls-and-proof.md)) — detailed DORA duties and their evidentiary limits.
- [[austrian-security-evidence-access|Austrian Security-Evidence Access]] ([Austrian Security-Evidence Access](austrian-security-evidence-access.md)) — public information, own data and supervisory evidence channels.

- [[dac8-dpia-accountability-and-security-evidence|DAC8 DPIA, Accountability and Security Evidence]] ([DAC8 DPIA, Accountability and Security Evidence](dac8-dpia-accountability-and-security-evidence.md))

- [[financial-data-breach-and-security-authorities|Financial-Data Breach and Security Authorities]] ([Financial-Data Breach and Security Authorities](financial-data-breach-and-security-authorities.md))
- [[krypto-mpfg-provider-record-architecture|Krypto-MPfG Provider Record Architecture]] ([Krypto-MPfG Provider Record Architecture](krypto-mpfg-provider-record-architecture.md))
- [[dsb-bvwg-evidence-and-interim-toolkit|DSB and BVwG Evidence and Interim-Protection Toolkit]] ([DSB and BVwG Evidence and Interim-Protection Toolkit](dsb-bvwg-evidence-and-interim-toolkit.md))

## Sources

- [Directive 2011/16/EU, consolidated 1 January 2026](https://eur-lex.europa.eu/eli/dir/2011/16/2026-01-01/eng)
- [Austrian Court of Audit, Bund 2024/16](https://www.rechnungshof.gv.at/rh/home/home/2024_16_IT-Sicherheit_BM.pdf)
- [DORA](https://eur-lex.europa.eu/eli/reg/2022/2554/oj/eng)
- [MiCA](https://eur-lex.europa.eu/eli/reg/2023/1114/oj/eng)
- [EU-AHG section 19a](https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20008121&Paragraf=19a)
- [CJEU C-340/21](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62021CJ0340)
