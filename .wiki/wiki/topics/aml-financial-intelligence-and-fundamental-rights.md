---
title: "AML Financial Intelligence and Fundamental Rights"
category: topic
sources:
  - raw/papers/2026-08-29-nazzari-reuter-aml-system-2025.md
  - raw/papers/2026-08-29-fatf-state-of-effectiveness-2022.md
  - raw/papers/2026-08-29-eba-de-risking-opinion-2022.md
  - raw/articles/2026-08-27-eu-edpb-aml-data-protection-record.md
  - raw/articles/2026-08-27-cjeu-c37-c601-20-aml-register.md
  - raw/articles/2026-08-27-cjeu-c562-20-rodl-partner-aml-risk.md
  - raw/articles/2026-08-27-cjeu-c235-14-safe-interenvios.md
  - raw/articles/2026-08-27-cjeu-c694-20-lawyer-privilege.md
  - raw/articles/2026-08-27-cjeu-c-623-22-dac6.md
  - raw/articles/2026-08-27-cjeu-c175-20-sia-ss-tax-data.md
  - raw/articles/2026-08-27-vfgh-g265-2023-wiereg-public-access.md
  - raw/articles/2026-08-27-vfgh-g62-2025-wiereg-information.md
  - raw/articles/2026-08-27-vfgh-e2189-2025-wiereg-internal-data.md
created: 2026-08-27
updated: 2026-08-29
tags: [aml, fundamental-rights, charter, data-protection, profiling, access, retention, remedies]
aliases: [AML privacy case law, AML fundamental rights]
confidence: high
volatility: warm
verified: 2026-08-27
summary: "AML is a legitimate public interest, but collection, profiling, access, retention, onward use, and remedies remain separately reviewable; the strongest claims attack excess in a concrete data lifecycle rather than AML as a whole."
---

# AML Financial Intelligence and Fundamental Rights

> The durable legal theory is not “AML is invalid.” It is that every stage of a financial-intelligence lifecycle must have a precise legal basis, a demonstrated need, proportionate fields and recipients, reliable risk logic, bounded retention, and an effective remedy.

## Rights analysis by lifecycle

| Stage | Core question | Strong evidence |
|---|---|---|
| collection | are the fields necessary for the defined purpose and affected risk? | field map, user categories, narrower design |
| matching and profiling | are inferences evidence-based, accurate, and non-discriminatory? | model/rule logic, false positives, manual review |
| disclosure | who receives which fields under which threshold? | role and access matrix, logs, approval path |
| linkage and reuse | is a second purpose legally authorised and compatible? | linkage diagram, legal basis per data flow |
| retention | why is each record still needed for that period? | field-level schedule, holds, deletion proof |
| consequences | can a person correct error or challenge an adverse result? | notice, access, correction, review, appeal |

Charter Articles 7 and 8, Article 8 ECHR, and section 1 DSG protect against disproportionate personal-data interference. Charter Article 21 and equality guarantees matter where nationality, residence, occupation, geography, or association becomes a proxy for suspicion. Article 47 and constitutional procedural guarantees matter when access or an adverse decision cannot be effectively contested.

## Case-law matrix

| Authority | Claimant use | State counterargument or limit |
|---|---|---|
| CJEU C-37/20 and C-601/20, *Luxembourg Business Registers/Sovim* | unrestricted public access was a serious and disproportionate interference; supports access tiers, field minimisation, and safeguards | expressly distinguishes controlled authority and obliged-entity access |
| CJEU C-562/20, *Rödl & Partner* | AML risk must be evidence-based; national enhancements remain subject to legality, certainty, proportionality, and non-discrimination | confirms minimum harmonisation and Member-State power to adopt stricter, properly published AML rules |
| CJEU C-235/14, *Safe Interenvíos* | proportionality remains reviewable | enhanced, risk-sensitive due diligence can be lawful |
| CJEU C-694/20, *Orde van Vlaamse Balies* | even indirect disclosure is invalid where it unnecessarily reveals protected lawyer-client consultation | narrow professional-privilege holding, not a general secrecy right for financial records |
| CJEU C-623/22, *Belgian Association of Tax Lawyers* | preserves review for sufficiently serious rights interference | largely rejects a general DAC6 invalidity attack and upholds broad reporting architecture |
| CJEU C-175/20, *SIA SS* | tax collection requires clear law, specific purpose, objective criteria, strict necessity, and bounded time | concerned a targeted authority request, not automatic-exchange legislation |
| VfGH G 265/2023 | Austrian section 1 DSG and Article 8 ECHR prohibit unconditional public WiEReG access | does not invalidate access by authorities or obliged entities |
| VfGH G 62/2025 | legitimate-interest access must contain enough information to serve journalism and public-interest scrutiny | supports differentiated access, not universal closure |
| VfGH E 2189/2025 | open-public access remains distinct from internal processing | upholds case-specific identity resolution and beneficial-owner data for register integrity |

Data-retention and surveillance judgments such as *Digital Rights Ireland*, *Prokuratuur*, and *Ligue des droits humains* can illuminate blanket collection, access, independent review, profiling, and safeguards. They are analogies, not holdings that invalidate AML customer-due-diligence or tax-reporting systems. That distinction should be explicit in pleadings and public communication.

## The Austrian WiEReG trilogy

The three recent VfGH decisions reject both rhetorical extremes.

1. Unconditional public search was unconstitutional.
2. Qualified journalists and other legitimate-interest users can require meaningful information.
3. Internal identity resolution and controlled beneficial-owner processing can be lawful.

The transferable design principle is differentiated access: the data set, purpose, recipient, search mode, logging, restriction, and remedy should match the role. Public access, obliged-entity CDD, FIU analysis, criminal investigation, tax access, supervision, and the data subject's own access are not one legal category.

## Application to DAC8 and Krypto-MPfG

The WiEReG public-access cases are not direct authority against Krypto-MPfG. Krypto-MPfG reporting is not an open public register. A credible current claim instead asks whether section 20(1) creates tax-purpose collection and processing of section 18 information for customers already determined not to be reportable, whether that universal increment is necessary, how long it is held, and what access, correction, and deletion protections operate.

The State will rely on the strength of the tax-transparency and AML objectives, the risk of residence changes and incomplete self-certification, the overlap with existing CASP records, and adverse authority such as *Rödl & Partner*, *Safe Interenvíos*, C-623/22, and VfGH E 2189/2025. The response needs evidence, not slogans:

- a field-by-field processing map;
- a reliably non-reportable claimant and completed self-certification;
- the narrower architecture that still detects changed reportability;
- an exact retention and deletion analysis;
- proof of incremental burden or concrete data-subject impact;
- access, correction, and remedy gaps tied to enacted provisions.

Directive 2011/16 Article 16 also permits defined reuse of exchanged tax information for AML/CFT. The campaign should therefore challenge unlawful or disproportionate linkage, not state categorically that AML reuse is forbidden.

## Evidence discipline

Technical compliance, report volume, investigative use, confiscation and aggregate crime reduction are separate outcomes. AML information is demonstrably used in investigations, but current reviews do not establish a comparably strong causal reduction in total laundering or predicate crime. False-positive, cost and de-risking claims likewise require a defined stage, denominator and counterfactual.

This uncertainty does not disprove the legitimate public interest. Without more, implementation or output metrics cannot substitute for evidence that a particular data field, access path, retention period or customer category is necessary and proportionate. See [[aml-kyc-effectiveness-evidence|AML and KYC Effectiveness Evidence]] ([article](../references/aml-kyc-effectiveness-evidence.md)).

## Future AML implementation review

When Austria implements Directive 2024/1640 and AMLR, test the enacted system against a minimum safeguard checklist:

- exhaustive fields and covered accounts;
- precise purposes and recipient classes;
- differentiated access thresholds;
- query and disclosure logs;
- notice or a reasoned secrecy exception;
- accuracy, source quality, correction, and human review;
- controls against proxy discrimination and de-risking;
- field-level retention and legal holds;
- independent authorisation for intrusive access;
- effective judicial or administrative review;
- security, bulk-export restrictions, and breach response.

The EDPB and EDPS record is especially useful for profiling and information-sharing partnerships: an important public interest does not remove purpose limitation, necessity, minimisation, accuracy, role definition, restricted access, retention, and independent supervision. The enacted package already contains material safeguards—especially AMLR Article 76 and Directive 2024/1640 Articles 16, 19, and 70—so a challenge must identify why those safeguards fail for the concrete data flow rather than allege wholesale absence.

## Communication lines that survive scrutiny

- Financial intelligence can be legitimate and still become disproportionate through excessive fields, linkage, access, retention, or unreviewable profiling.
- Self-custody is not prohibited; CASP involvement triggers defined traceability and risk controls.
- BARIS is planned institutional account discovery, not a public list of every wallet and balance.
- The danger is function creep and error across connected systems, so safeguards must be assessed across the full data lifecycle.

## Claims to avoid

- “The CJEU has held AML databases unlawful.”
- “Public-register invalidity also invalidates controlled FIU access.”
- “Financial privacy creates a right to anonymous regulated accounts.”
- “Every risk classification is prohibited profiling.”
- “Data-retention judgments automatically control AML or DAC8.”
- “Professional privilege protects ordinary CASP transaction records.”

## See Also

- [[aml-kyc-effectiveness-evidence|AML and KYC Effectiveness Evidence]] ([AML and KYC Effectiveness Evidence](../references/aml-kyc-effectiveness-evidence.md))
- [[crypto-crime-measurement-and-aml-evidence|Crypto-Crime Measurement and AML Evidence]] ([Crypto-Crime Measurement and AML Evidence](../references/crypto-crime-measurement-and-aml-evidence.md))
- [[eu-aml-crypto-regulatory-stack|EU AML Crypto Regulatory Stack]] ([EU AML Crypto Regulatory Stack](eu-aml-crypto-regulatory-stack.md))
- [[austrian-aml-crypto-implementation|Austrian AML Crypto Implementation]] ([Austrian AML Crypto Implementation](austrian-aml-crypto-implementation.md))
- [[dac8-fundamental-rights-and-public-risks|DAC8 Fundamental Rights and Public Risks]] ([DAC8 Fundamental Rights and Public Risks](dac8-fundamental-rights-and-public-risks.md))
- [[dac8-and-the-wealth-register-risk|DAC8 and the Wealth-Register Risk]] ([DAC8 and the Wealth-Register Risk](dac8-and-the-wealth-register-risk.md))
- [[austria-eu-precedent-matrix|Austria and EU Precedent Matrix]] ([Austria and EU Precedent Matrix](../references/austria-eu-precedent-matrix.md))

## Sources

- [Nazzari and Reuter](../../raw/papers/2026-08-29-nazzari-reuter-aml-system-2025.md)
- [FATF state of effectiveness](../../raw/papers/2026-08-29-fatf-state-of-effectiveness-2022.md)
- [EBA de-risking opinion](../../raw/papers/2026-08-29-eba-de-risking-opinion-2022.md)
- [EDPB and EDPS AML/CFT safeguards](../../raw/articles/2026-08-27-eu-edpb-aml-data-protection-record.md)
- [CJEU C-37/20 and C-601/20](../../raw/articles/2026-08-27-cjeu-c37-c601-20-aml-register.md)
- [CJEU C-562/20](../../raw/articles/2026-08-27-cjeu-c562-20-rodl-partner-aml-risk.md)
- [CJEU C-235/14](../../raw/articles/2026-08-27-cjeu-c235-14-safe-interenvios.md)
- [CJEU C-694/20](../../raw/articles/2026-08-27-cjeu-c694-20-lawyer-privilege.md)
- [CJEU C-623/22](../../raw/articles/2026-08-27-cjeu-c-623-22-dac6.md)
- [CJEU C-175/20](../../raw/articles/2026-08-27-cjeu-c175-20-sia-ss-tax-data.md)
- [VfGH G 265/2023](../../raw/articles/2026-08-27-vfgh-g265-2023-wiereg-public-access.md)
- [VfGH G 62/2025](../../raw/articles/2026-08-27-vfgh-g62-2025-wiereg-information.md)
- [VfGH E 2189/2025](../../raw/articles/2026-08-27-vfgh-e2189-2025-wiereg-internal-data.md)
