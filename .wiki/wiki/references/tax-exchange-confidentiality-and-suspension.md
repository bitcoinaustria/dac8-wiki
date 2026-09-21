---
title: "Tax-Exchange Confidentiality, Review and Suspension"
category: reference
sources:
  - raw/articles/2026-09-19-sif-bulgaria-exchange-suspension.md
  - raw/articles/2026-09-19-sif-exchange-status-and-conditions.md
  - raw/articles/2026-09-19-oecd-cds-review-framework.md
  - raw/papers/2026-09-19-oecd-cds-terms-of-reference.md
  - raw/articles/2026-08-28-eu-directive-2011-16-consolidated-2026.md
created: 2026-09-19
updated: 2026-09-19
verified: 2026-09-19
volatility: hot
confidence: high
tags: [tax-exchange, confidentiality, audit, suspension, carf]
summary: "Actual exchange suspension and the Global Forum's review framework support a lifecycle-specific security assessment, not an assumption that safeguards are absent or infallible."
---

# Tax-Exchange Confidentiality, Review and Suspension

International tax exchange has both documented confidentiality failures and operational safeguards. The useful question is which dataset, recipient and processing stage a safeguard covers, and what evidence demonstrates its effectiveness.

## Actual suspension, followed by restored reciprocity

The [Swiss Federal Council's September 2019 announcement](../../raw/articles/2026-09-19-sif-bulgaria-exchange-suspension.md) documents withholding financial-account information after Bulgaria's tax-administration breach. This is stronger than a hypothetical warning that tax data might leak. It also disproves an assertion that exchange suspension exists only on paper.

The [current Swiss register](../../raw/articles/2026-09-19-sif-exchange-status-and-conditions.md) records restored reciprocity with Bulgaria on 11 October 2023. The example is CRS exchange under the Swiss–EU agreement, not a DAC8 incident, and establishes no physical attack. The status entry does not establish the first resumed transmission date.

## Separate collection, transmission and receipt

The Swiss register's footnotes distinguish domestic collection/reporting from onward transmission withheld pending confidentiality conditions or investigation. **A transmission stop need not stop collection, domestic storage or earlier recipient copies.** This is a lifecycle distinction, not an assertion that Swiss rules govern Austrian DAC8 processing.

[DAC Article 25(6)](../../raw/articles/2026-08-28-eu-directive-2011-16-consolidated-2026.md) contains breach notification and exchange/CCN suspension mechanisms. Restoration and verification must be described according to the actual provision; a joint verification is not invariably automatic. No existing Austrian suspension or affected recipient is established here.

## What an assessment should cover

The [Global Forum CDS terms of reference](../../raw/papers/2026-09-19-oecd-cds-terms-of-reference.md), paragraphs 9–16, cover:

| Area | Assessment criterion | Missing Austrian implementation evidence |
|---|---|---|
| Access | Need-to-know, least privilege and personnel controls | Actual roles, permissions and their review |
| Copies | Classification, storage, retention and destruction across the lifecycle | Copy inventory, backups and tested deletion |
| Detection | Monitoring, alerts, logging and internal/external audit | Test results, exceptions and remediation |
| Incident response | Investigation, correction and partner notification | Applicable escalation and containment process |

The [current framework](../../raw/articles/2026-09-19-oecd-cds-review-framework.md) expressly covers CRS and CARF, including pre-/post-exchange assessment, annual monitoring from 2026 and possible suspension. Detailed findings are confidential. Their absence from public sources is not evidence that assessment did not occur; the benchmark itself is not evidence that controls work.

## Relevance and limits

For an Austrian challenge, these sources help identify concrete security evidence and less intrusive control options. They also supply a serious counterargument: the system already imposes controls and can interrupt exchanges. A proposed alternative needs evidence of comparable tax effectiveness and practical risk reduction. Neither a foreign incident nor a confidentiality requirement alone resolves proportionality or admissibility.

## See Also

- [[dac8-security-architecture-and-audit-evidence|DAC8 Security Architecture and Audit Evidence]] ([DAC8 Security Architecture and Audit Evidence](dac8-security-architecture-and-audit-evidence.md))
- [[european-data-misuse-and-physical-risk|European Data Misuse and Physical-Risk Evidence]] ([European Data Misuse and Physical-Risk Evidence](european-data-misuse-and-physical-risk.md))
