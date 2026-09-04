---
title: "DAC8 DPIA, Accountability and Security Evidence"
category: reference
sources:
  - raw/articles/2026-09-04-gdpr-articles-35-36-dpia-conditions.md
  - raw/articles/2026-09-04-austria-krypto-mpfg-wfa-privacy-assessment-record.md
  - raw/articles/2026-09-04-austria-dpia-required-and-exempt-lists.md
  - raw/articles/2026-09-04-cjeu-c60-22-accountability-documentation-limit.md
  - raw/articles/2026-09-04-cjeu-c61-22-legislative-dpia-limit.md
  - raw/articles/2026-09-04-cjeu-c340-21-tax-authority-breach-security.md
  - raw/articles/2026-09-04-mica-dora-casp-security-baseline.md
  - raw/articles/2026-09-04-mica-dora-casp-evidence-generators.md
  - raw/articles/2026-09-04-dac8-security-controller-breach-architecture.md
  - raw/articles/2026-08-30-edps-opinion-9-2023-dac8-detailed-extraction.md
  - raw/articles/2026-09-04-austria-dsg-section-21-consultation-duty.md
  - raw/articles/2026-09-04-dsg-21-consultation-source-locator-correction.md
created: 2026-09-04
updated: 2026-09-04
tags: [dac8, krypto-mpfg, gdpr, dpia, accountability, security, evidence]
aliases: [DAC8 DPIA, Krypto-MPfG security evidence]
confidence: high
volatility: hot
verified: 2026-09-04
summary: "Operational DPIA and security evidence map that preserves the statutory-processing and Austrian exemption defences while identifying records capable of proving concrete necessity or control defects."
---

# DAC8 DPIA, Accountability and Security Evidence

> A missing or weak DPIA is an investigation and accountability issue, not an automatic invalidity theory. The stronger merits case tests the actual processing, risks, controls and effects under GDPR Articles 5, 24, 25 and 32 and DAC Articles 21 and 25.

## Trigger and defence matrix

| Proposition | Supporting basis | Limiting authority or fact |
|---|---|---|
| High-risk provider or authority processing may require an operational DPIA | GDPR Article 35(1); Austrian required list; actual automation, matching, scale and consequence | Trigger must be proved operation by operation. Routine crypto financial data are not Article 9 data merely because they are financial. |
| A legislative assessment can remove the operational Article 35(1)–(7) duty | Article 35(10), but only where its three cumulative conditions are met | The applicable law must regulate the specific operation and the adoption-stage assessment must satisfy the relevant content. A Member State may still require a DPIA. |
| The public Austrian WFA appears not to contain a structured privacy-risk assessment | WFA identifies only financial, administrative-cost and macroeconomic material effects and describes system resources | The public record does not prove the absence of a separate or non-public assessment. |
| Legislative consultation is a distinct duty | Article 36(4) | The Parliament file proves that DSB and Datenschutzrat were invited, not whether advice was delivered or considered. |
| Section 21(1) DSG makes DSB consultation mandatory before a federal regulation directly concerning data protection | Austrian statutory text | For the Krypto-MPfG regulation, non-consultation and its relevance under Article 139 must be proved. The statutory-process invitation does not answer the regulation process. |
| Authority processing may fall within the Austrian DSFA-A17 exemption for public tax assessment, collection, accounting and control | DSFA-AV A17 | Scope must be tested for additional joins or materially different reuse; the exemption does not remove Articles 5, 24, 25, 30 or 32. |
| Provider processing may invoke DSFA-A01 customer/accounting or DSFA-A06 statutory-register categories | DSFA-AV | Neither category decides without facts whether section 20 classification, aggregation, transmission and cross-system joins remain within it. |
| A breach or third-party access proves inadequate security | No: C-340/21 expressly rejects that inference | Test identified risks and the nature, implementation and practical effect of the controls. |
| Missing Article 26 or 30 documentation makes the processing unlawful and requires deletion | No: C-60/22 rejects automatic unlawfulness from those defects | Documentation can support investigation and corrective orders but must be connected to the substantive defect. |
| No legislative DPIA means the statute is invalid | No: C-61/22 rejects treating law adoption itself as the Article 4(2) processing operation | Later provider and authority processing remains fully subject to GDPR duties. |

## Public legislative-record questions

The Austrian WFA can be used as a controlled evidence request, not as a conclusive merits claim:

1. If Article 35(10) is invoked, identify the assessment and map it to Article 35(7): processing description, necessity, proportionality, risks and safeguards.
2. Produce the Article 36(4) consultation record: invitation, delivery, response or non-response, meeting record and treatment of advice.
3. Identify separate operational DPIAs, exemption analyses, change reviews and DPO advice for provider, BMF and recipient processing.
4. Explain how the public WFA's quantified revenue and system assumptions support each additional field and the ten-year choice.
5. For the Krypto-MPfG implementing regulation, identify the section 21(1) DSG consultation record and any treatment of DSB advice.

CJEU C-61/22 is a hard limit: failure to perform a legislative DPIA does not automatically invalidate the legal act because adoption is not itself the processing operation. The stronger operational consequence runs in the other direction. Unless a qualifying assessment satisfied Article 35(10)'s conditions, provider and authority processing remains subject to the ordinary Article 35 analysis; Article 35(11) review and Articles 5, 24, 25, 30 and 32 remain applicable in any event.

EDPS Opinion 9/2023 is evidence that purpose, controller-role and retention concerns were raised during the EU process. It is an institutional recommendation, not a holding of unlawfulness.

## Provider evidence file

| Issue | Documents to identify or seek |
|---|---|
| DPIA trigger and governance | trigger or exemption memorandum; DPIA versions and change log; DPO advice; Article 35(9) consultation decision; any Article 36 file |
| Data necessity and minimisation | Article 30 record; Article 25 design decisions; field schema; derivation and lineage; reportable/non-reportable separation; aggregation and deletion logic |
| Access and security | role and export matrix; access logs; encryption and key architecture; testing and penetration findings; incident log and root-cause analysis; remediation evidence |
| Third parties and recovery | Article 28 agreements; DORA third-party register and contract terms; system and data locations; backup, recovery, return and deletion tests |
| DAC8-specific execution | section 20 notice; section 39 records; report preview; correction/deletion propagation; provider-to-BMF interface controls |
| MiCA and DORA corroboration | authorisation ICT dossier; continuity plan; risk-framework review report; asset/dependency inventory; incident and resilience-testing records |

MiCA and DORA create valuable documentary trails for an authorised CASP. They are adverse to any claim that providers operate without binding controls. Their existence does not prove that the separate DAC8 data path was properly scoped or that every reporting operator falls within DORA.

## Authority evidence file

- legislative assessment and Article 36(4) consultation records;
- provider, BMF, CCN, directory and data-warehouse flow maps and schemas;
- controller, joint-controller and processor allocations under DAC Article 25(3);
- purpose, recipient, role, export and access-log catalogues;
- data-quality, correction and downstream-propagation workflows;
- active, archival, backup and legal-hold retention schedules and tested deletion;
- security accreditation, audit, penetration-test, incident and DAC Article 25(6) suspension/remediation records;
- actual risk-selection or downstream model inputs, human review and consequences.

Article 15 gives the person an intelligible copy of personal data, purposes, categories, recipients, sources and retention information, including access-log information relating to that person where applicable. It does not grant a general right to the full DPIA, Article 30 record, security test or contract. Those documents should be identified for the DSB, which can demand relevant controller material under Articles 30(4) and 58. Party access can remain limited by protected security or commercial interests.

## Merits use

| Finding | Proper litigation use | Overclaim to avoid |
|---|---|---|
| No DPIA despite a proved trigger and no valid exemption | Accountability defect; require assessment and specified interim or final control where the actual risk supports it | Automatic statutory invalidity, erasure or damages |
| Legislative assessment fails to address actual high-risk processing | Rebut an Article 35(10) defence; request the actual assessment and operational file | Public silence proves no assessment exists |
| Avoidable field, join, access privilege or persistent copy | Direct Article 5/25 proportionality and minimisation challenge | DPIA label alone proves the defect |
| Control ineffective against a concrete identified threat | Article 32 and DAC security challenge with targeted remediation or restriction | A breach anywhere proves Austrian DAC8 insecurity |
| Correction or deletion cannot be traced across copies | Accountability, accuracy and remedy-propagation challenge | Technical message capability creates a substantive erasure right |

## See Also

- [[dsb-bvwg-evidence-and-interim-toolkit|DSB and BVwG Evidence and Interim-Protection Toolkit]] ([DSB and BVwG Evidence and Interim-Protection Toolkit](dsb-bvwg-evidence-and-interim-toolkit.md))
- [[dac8-security-architecture-and-audit-evidence|DAC8 Security Architecture and Audit Evidence]] ([DAC8 Security Architecture and Audit Evidence](dac8-security-architecture-and-audit-evidence.md))
- [[dac8-remedy-and-outcome-matrix|DAC8 Remedy and Outcome Matrix]] ([DAC8 Remedy and Outcome Matrix](dac8-remedy-and-outcome-matrix.md))

## Sources

- [GDPR Articles 35 and 36](../../raw/articles/2026-09-04-gdpr-articles-35-36-dpia-conditions.md)
- [Austrian WFA and consultation record](../../raw/articles/2026-09-04-austria-krypto-mpfg-wfa-privacy-assessment-record.md)
- [Austrian DPIA lists](../../raw/articles/2026-09-04-austria-dpia-required-and-exempt-lists.md)
- [CJEU C-60/22](../../raw/articles/2026-09-04-cjeu-c60-22-accountability-documentation-limit.md)
- [CJEU C-61/22](../../raw/articles/2026-09-04-cjeu-c61-22-legislative-dpia-limit.md)
- [CJEU C-340/21](../../raw/articles/2026-09-04-cjeu-c340-21-tax-authority-breach-security.md)
- [MiCA and DORA evidence sources](../../raw/articles/2026-09-04-mica-dora-casp-evidence-generators.md)
- [EDPS Opinion 9/2023](../../raw/articles/2026-08-30-edps-opinion-9-2023-dac8-detailed-extraction.md)
- [Austrian DSG section 21 consultation duty, original record](../../raw/articles/2026-09-04-austria-dsg-section-21-consultation-duty.md), with [correct official locator](../../raw/articles/2026-09-04-dsg-21-consultation-source-locator-correction.md).
