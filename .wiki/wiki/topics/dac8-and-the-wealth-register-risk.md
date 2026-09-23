---
title: "DAC8 and the Wealth-Register Risk"
category: topic
sources:
  - raw/articles/2026-08-27-eu-directive-2023-2226-dac8.md
  - raw/articles/2026-08-27-austria-krypto-mpfg-section-18.md
  - raw/articles/2026-08-27-krypto-mpfg-section-20-retention.md
  - raw/articles/2026-08-27-eu-asset-register-feasibility-study-2024.md
  - raw/articles/2026-08-27-eu-amld6-directive-2024-1640-account-registers.md
  - raw/articles/2026-08-27-eu-directive-2024-1654-account-register-access.md
  - raw/articles/2026-08-27-austria-kontenregister-bmf-overview.md
  - raw/articles/2026-08-27-commission-wealth-taxation-study-2026.md
  - raw/articles/2026-08-27-commission-answer-e-001435-2024-asset-register.md
  - raw/articles/2026-08-27-echr-mn-others-san-marino.md
  - raw/articles/2026-08-27-echr-lb-hungary-tax-publication.md
  - raw/articles/2026-08-27-edpb-blockchain-guidelines-02-2025-final.md
  - raw/articles/2026-08-27-eu-amld6-2024-1640-system.md
  - raw/articles/2026-08-27-austria-kontregg-current.md
  - raw/articles/2026-08-27-cjeu-c37-c601-20-aml-register.md
  - raw/articles/2026-08-27-eu-directive-2026-799-insolvency-baris-access.md
created: 2026-08-27
updated: 2026-08-27
tags: [dac8, wealth-register, asset-register, baris, fundamental-rights, interoperability]
aliases: [Vermögensregister, de facto wealth register, crypto asset register]
confidence: high
volatility: hot
verified: 2026-08-27
summary: "DAC8 is not a complete wealth register, but its identity-linked crypto aggregates can become a register-like wealth-profile layer when combined with account discovery, provider records, and future EU interoperability."
---

# DAC8 and the Wealth-Register Risk

> The accurate claim is not “DAC8 is already a complete EU wealth register.” It is that DAC8 adds an identity-linked crypto-activity layer to an increasingly interoperable asset-discovery infrastructure.

## What counts as a wealth register?

Three meanings must be separated:

1. **Formal comprehensive register:** one official database listing a person's material assets and usually ownership or value.
2. **Federated asset-discovery system:** several registers connected through a common query point, allowing authorities to find asset relationships across classes and states.
3. **Functional wealth profile:** separate identity, account, transaction, tax, beneficial-ownership, and public-ledger data that can be joined to infer a person's assets or financial behaviour.

DAC8 fits the third category only in combination with other data. The EU has studied the first two categories, and parts of the second are already enacted for future operation.

## Current and enacted building blocks

| Layer | What it reveals | What it does not establish |
|---|---|---|
| DAC8/Krypto-MPfG report | identity, address, tax residence, and annual per-asset/per-category transaction values, units, and counts | no complete year-end net worth; no liabilities; no wallet addresses, transaction IDs, dates, or counterparties |
| Krypto-MPfG section 20(1) provider processing | tax-report fields for all customers, transactions, and crypto-assets, even before final reportability | does not automatically transmit every customer's profile |
| MiCA Article 68(9) | provider records of services, activities, orders, and transactions | no general tax or public-register purpose |
| TFR | granular originator/beneficiary and transfer identifiers for AML/CFT | Article 25 does not permit unrestricted tax or commercial reuse |
| Austrian Kontenregister | account, depot, and safe-deposit relationships | no balance or movements; those require a separate inspection route |
| AMLD6 Article 16 / BARIS, by 10 July 2029 | cross-border identification of bank, securities, crypto-asset accounts, and safe-deposit relationships | minimum BARIS data are identifiers and opening/closing dates, not a central balance or transaction database |
| Directive 2024/1654 | case-specific serious-crime access to BARIS and a standard format for transaction records requested under national law | no routine central ingestion of all transaction histories |
| Directive 2026/799 | future case-specific BARIS access through designated courts or administrative authorities for insolvency asset tracing | no public access and no new wallet, balance, or transaction-history fields |
| AMLD6 Article 18 access points, by 10 July 2029 | real-estate ownership, acquisition price, encumbrances, and ownership/price history for competent authorities | no unified cross-asset net-worth register |

Self-hosted crypto also prevents DAC8 from being a complete holdings register. Annual acquisition, disposal, payment, and transfer aggregates do not prove the balance or present owner of assets after an external transfer. A “net worth” label would therefore overstate both completeness and accuracy.

### What the AML package changes—and what it does not

Recast AMLD6 Article 16 requires national mechanisms for covered institution-held account relationships, including covered crypto-asset accounts, and BARIS interconnection by 10 July 2029. Mandatory BARIS fields are identity, unique account identifier, and opening/closing dates, not self-hosted addresses, balances, holdings, or transaction history. TFR requires both-party information for a CASP-involved self-hosted transfer regardless of value; EUR 1,000 is only the additional ownership-or-control assessment trigger. TFR does not prohibit self-custody or bring genuine person-to-person transfers without a CASP into the travel rule.

BARIS will not be FIU-only. Enacted legislation also provides case-specific access for designated serious-crime authorities and a future insolvency route through designated courts or administrative authorities. These are material access paths, but each is purpose- and safeguard-bound. National Article 16(5) extra fields do not enter BARIS.

The rights analysis must also separate access tiers. CJEU C-37/20 and C-601/20 and VfGH G 265/2023 invalidated unconditional public access to beneficial-ownership information. They did not invalidate controlled FIU, authority, or obliged-entity access. A future wealth-profile challenge should therefore identify the exact fields, recipient, threshold, search mode, logs, retention, linkage, and remedy rather than equate every controlled account-discovery mechanism with a public register.

## The EU asset-register study

The Commission-commissioned final feasibility study published in 2024 examined:

- new national asset registers interconnected at EU level;
- interconnection of existing national registers;
- a central EU register/database combining existing and new asset categories.

It was a study, not a legislative proposal or a decision to build the central scenario. Its legal analysis nevertheless gives the campaign unusually direct institutional support. For the central scenario it found that:

- broad asset coverage and aggregation greatly increase the seriousness of the interference;
- searchability can support conclusions about habits, daily life, and social relationships;
- the design is likely to risk a manifestly disproportionate privacy and data-protection interference;
- centralisation creates potentially dramatic cyberattack consequences;
- it is uncertain whether faster identification and cross-dataset correlation outweigh those disadvantages;
- non-public, authority-only access and strong security reduce risk but do not eliminate the proportionality problem.

This is the right source for arguing against a future comprehensive register. It is not proof that the narrower current DAC8 design already has every feature the study criticised.

The Commission later confirmed in answer E-001435/2024 that the work identified operational and legal obstacles and that its AML package did not establish a comprehensive EU-level asset register. The accurate policy-status claim is therefore “studied, not adopted.”

## Fundamental-rights objections

### 1. Aggregation changes the nature of the interference

One isolated account identifier is different from a searchable cross-asset history. Combining identity, residence, beneficial ownership, account relationships, crypto activity, transfer data, and public-ledger analysis can reveal more than each dataset separately. The legal assessment must therefore consider reasonably foreseeable interoperability and access, not only one field in isolation.

CJEU C-37/20 and C-601/20, *Luxembourg Business Registers*, paragraphs 41–44, recognised that identity plus ownership information can profile wealth and investment choices. Paragraphs 63–66 require strict necessity, clear rules, safeguards, and the least onerous equally effective means.

The decision invalidated unconditional **public** access. DAC8 is not public, so the outcome does not transfer automatically. The profiling principle and proportionality method remain relevant; the public-access severity must be expressly distinguished.

The ECtHR supplies the same calibration. *M.N. and Others v San Marino* treats banking documents as Article 8 data and requires effective procedural safeguards. *L.B. v Hungary* condemns systematic online publication of identity, home-address, and tax information. By contrast, *G.S.B. v Switzerland* shows that controlled tax-data exchange with a legal basis and effective safeguards can be lawful. The target is therefore excessive fields, access, aggregation, retention, publication, or deficient remedies—not every financial register as such.

### 2. A general search layer reverses the investigative model

A targeted request begins with a defined person, purpose, and legal threshold. A routine population-wide data layer collects first so that authorities can search later. The State must explain why universal acquisition or ready discoverability is needed and why targeted, risk-based, or reportable-user-first alternatives are not equally effective.

The strongest current Austrian version is narrow: why must section 20(1) create tax-report information for a person already reliably determined not to be reportable? A future comprehensive-register challenge would separately ask why asset classes and persons unrelated to a concrete AML or tax risk must enter a cross-searchable system.

### 3. Partial data can mislead as well as reveal

DAC8 values are transaction aggregates, not audited net wealth. They omit liabilities, self-hosted holdings, assets outside covered providers, ownership changes after transfers, and valuation context. A register-like profile can therefore create false positives, duplicate values, stale residence classifications, or an exaggerated appearance of wealth.

Accuracy, correction propagation, provenance, valuation method, temporal meaning, and the prohibition of adverse conclusions from incomplete data should be core safeguards.

### 4. Purpose stacking and function expansion

Directive 2011/16/EU Article 16 already permits DAC information to be used for covered taxes, VAT, other indirect taxes, customs, AML/CFT, and specified restrictive-measures work. That is an explicit purpose range, not secret function creep.

The objection is that adding new recipient groups, analytics, matching keys, or asset classes can transform the system's practical power without a fresh public necessity assessment. Each new linkage should have a precise legal basis, documented purpose, access threshold, retention rule, audit trail, and independent review.

### 5. Security and physical safety

High-value asset profiles are attractive for fraud, extortion, home invasion, and kidnapping. Centralisation increases the blast radius of compromised credentials, malicious insiders, bad queries, or system breaches. Pseudonymisation does not solve this where authorised users can resolve identity.

The court file needs an actual architecture and threat model. Public communication can rely on the EU study's cyber-risk warning and verified crypto-attack evidence, but must not claim that DAC8 has already caused a particular attack.

### 6. Financial autonomy and chilling

Durable State visibility can change lawful saving, donation, investment, association, or self-custody choices. This is a legitimate democratic concern. It becomes a legal claim only when the claimant shows the protected activity, what the data reveal, and a concrete chilling effect.

### 7. Equality and selective visibility

A crypto-only profile may make one form of lawful property unusually legible while comparable cash, valuables, private-company interests, or foreign structures remain less visible. That can distort risk assessment and burden regulated intermediaries and users disproportionately.

The State can justify different treatment where crypto creates distinct cross-border and intermediary gaps. An equality claim therefore needs a precise comparison group and proof that the different treatment is not rationally connected to those differences.

### 8. Effective remedy and democratic control

A person should be able to learn:

- which system contains which relationship or value;
- which authority queried it, subject to narrowly justified secrecy;
- the purpose and legal basis;
- the source and valuation date;
- recipients and onward uses;
- how to correct an error everywhere it propagated;
- when each copy, log, and backup is deleted;
- which independent body can stop unlawful access.

Complex federated systems can make controller responsibility and correction illusory. The architecture must preserve a nearby accountable controller and an effective judicial route.

## Less intrusive alternatives

- universal status identification but transaction aggregation only after reportability is established;
- account-relationship discovery separated from balance and transaction access;
- targeted requests with documented thresholds for granular records;
- distributed query or interconnection rather than a central copied database;
- result minimisation: return only a hit/no-hit or defined fields needed for the case;
- case-specific access, designated staff, strong authentication, immutable logs, notification, and independent audit;
- short, purpose-specific retention and deletion of never-used/non-reportable profiles;
- verified correction propagation and provenance;
- technical and legal separation between tax, AML/CFT, sanctions, and criminal-investigation datasets.

Austria's own Kontenregister supplies a useful design comparator: it separates relationship discovery from the more intrusive viewing of balances and movements. The State will also argue that one logged central query can be less intrusive than sending a request to hundreds of institutions. The campaign should demand those minimising features instead of claiming that decentralisation is always safer.

## State counterarguments

- equal taxation and the prevention of tax evasion and money laundering are weighty public interests;
- crypto is portable, cross-border, pseudonymous, and easy to move outside classic accounts;
- DAC8 exchange is confidential and consists mainly of annual aggregates;
- BARIS minimum data identify accounts rather than balances;
- Directive 2024/1654 requires case-by-case serious-crime access and preserves national request safeguards for transaction records;
- registers can reduce indiscriminate provider inquiries, improve audit logs, speed freezing, and reduce information leakage;
- fragmented systems create gaps, duplicate work, stale data, and opportunities for concealment;
- the 2026 Commission wealth-tax study stresses the enforcement value of asset registration, beneficial-owner exchange, and third-party reporting.

These arguments defeat a categorical claim that every asset register is unconstitutional. The litigation question is design-specific proportionality.

## Litigation position

Do not make a hypothetical future comprehensive register the sole ground for annulling current section 20. Instead:

1. attack the current all-customer tax-purpose processing with current facts;
2. use foreseeable interoperability to measure seriousness, security, purpose, and safeguards only where the legal links are enacted or technically real;
3. use the EU feasibility study to prove that central cross-asset aggregation raises acknowledged fundamental-rights problems;
4. challenge future Austrian AMLD6 implementation or an EU asset-register act on its actual enacted fields, access, retention, and remedies when those become reviewable;
5. preserve a separate communications demand: no comprehensive or federated wealth profile without a new democratic mandate and strict necessity proof.

## Communications language

### Strong and accurate

> DAC8 is not yet a complete wealth register. It creates an identity-linked crypto-activity profile that can become one layer of a de facto asset map when combined with account registers, provider transaction records, beneficial-ownership data, and public-ledger analysis. EU institutions have already studied deeper asset-register interconnection and have themselves warned of serious proportionality and cyber risks.

### Avoid

- “The EU already has one database containing everyone's full net worth.”
- “BARIS stores every balance and transaction.”
- “DAC8 reports every wallet and current holding.”
- “The 2024 study means the Commission decided to build a wealth register.”
- “Luxembourg Business Registers invalidated all non-public financial registers.”

## See Also

- [[transaction-data-wealth-inference|Vermögensschätzung aus Transaktionsdaten als Analogie für DAC8]] ([Vermögensschätzung aus Transaktionsdaten als Analogie für DAC8](../theses/transaction-data-wealth-inference.md))
- [[dac8-fundamental-rights-and-public-risks|DAC8 Fundamental Rights and Public Risks]] ([DAC8 Fundamental Rights and Public Risks](dac8-fundamental-rights-and-public-risks.md))
- [[mica-tfr-krypto-mpfg-nexus|MiCA, TFR, and the Krypto-MPfG Nexus]] ([MiCA, TFR, and the Krypto-MPfG Nexus](mica-tfr-krypto-mpfg-nexus.md))
- [[member-state-challenge-and-communications-playbook|Member-State Challenge and Communications Playbook]] ([Member-State Challenge and Communications Playbook](../references/member-state-challenge-and-communications-playbook.md))
- [[eu-aml-crypto-regulatory-stack|EU AML Crypto Regulatory Stack]] ([EU AML Crypto Regulatory Stack](eu-aml-crypto-regulatory-stack.md))
- [[austrian-aml-crypto-implementation|Austrian AML Crypto Implementation]] ([Austrian AML Crypto Implementation](austrian-aml-crypto-implementation.md))
- [[aml-financial-intelligence-and-fundamental-rights|AML Financial Intelligence and Fundamental Rights]] ([AML Financial Intelligence and Fundamental Rights](aml-financial-intelligence-and-fundamental-rights.md))

## Sources

- [EU asset-register feasibility study](../../../legal-docs/supporting/eu-asset-registry-feasibility-study-2024.pdf)
- [AMLD6 signed text](../../../legal-docs/supporting/eu-amld6-pe-37-2024-full.pdf)
- [Directive 2024/1654 signed text](../../../legal-docs/supporting/eu-directive-2024-1654-pe-44-2024-full.pdf)
- [CJEU C-37/20 and C-601/20](../../../legal-docs/supporting/eu-cjeu-c37-20-c601-20-luxembourg-registers.pdf)
- [ECtHR M.N. and Others v San Marino](../../../legal-docs/supporting/echr-mn-others-v-san-marino.pdf)
- [ECtHR L.B. v Hungary](../../../legal-docs/supporting/echr-lb-v-hungary.pdf)
- [DAC8](../../../legal-docs/core/eu-dac8-directive-2023-2226.pdf)
