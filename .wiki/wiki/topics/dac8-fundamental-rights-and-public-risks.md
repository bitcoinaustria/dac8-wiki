---
title: "DAC8 Fundamental Rights and Public Risks"
category: topic
sources:
  - raw/articles/2026-08-27-eu-directive-2023-2226-dac8.md
  - raw/articles/2026-08-27-austria-krypto-mpfg-section-18.md
  - raw/articles/2026-08-27-krypto-mpfg-section-20-retention.md
  - raw/articles/2026-08-27-edps-opinion-9-2023-dac8.md
  - raw/articles/2026-08-27-edpb-blockchain-guidelines-02-2025-final.md
  - raw/articles/2026-08-27-cjeu-digital-rights-ireland.md
  - raw/articles/2026-08-27-cjeu-la-quadrature-c-470-21.md
  - raw/articles/2026-08-27-cnil-2025-breach-report.md
  - raw/articles/2026-08-27-certik-wrench-attacks-h1-2026.md
  - raw/articles/2026-08-27-waltio-security-incident.md
  - raw/articles/2026-08-27-eu-edpb-aml-data-protection-record.md
  - raw/articles/2026-08-27-cjeu-c37-c601-20-aml-register.md
  - raw/articles/2026-08-27-cjeu-c562-20-rodl-partner-aml-risk.md
  - raw/articles/2026-08-27-vfgh-g265-2023-wiereg-public-access.md
  - raw/articles/2026-08-27-vfgh-g62-2025-wiereg-information.md
  - raw/articles/2026-08-27-vfgh-e2189-2025-wiereg-internal-data.md
  - raw/articles/2026-09-04-eu-delegated-regulation-2025-1140-mica-records.md
  - raw/articles/2026-09-04-cjeu-c340-21-tax-authority-breach-security.md
  - raw/articles/2026-09-04-ecthr-i-v-finland-database-security.md
  - raw/articles/2026-09-04-france-dgfip-tax-data-breach.md
  - raw/articles/2026-09-04-france-ficoba-account-register-breach.md
  - raw/articles/2026-09-04-coinbase-2025-data-theft-8k.md
  - raw/articles/2026-09-04-cnil-2025-breach-report-detailed-extraction.md
  - raw/papers/2026-09-04-ordekian-wrench-attacks-aft-2024.md
  - raw/articles/2026-09-04-ecthr-kurt-austria-physical-risk-threshold.md
created: 2026-08-27
updated: 2026-09-04
tags: [dac8, fundamental-rights, privacy, data-protection, security, communications]
aliases: [DAC8 dangers, DAC8 rights narrative, financial privacy risks]
confidence: medium
volatility: hot
verified: 2026-09-04
summary: "A litigation-and-communications framework separating established privacy interferences from evidence-dependent security, chilling, exclusion, and function-creep risks."
---

# DAC8 Fundamental Rights and Public Risks

> The public case can be broader than one Individualantrag. It must still distinguish what the law does, what a court can decide, and what evidence suggests may happen.

## Three evidence levels

| Level | Meaning | Safe formulation |
|---|---|---|
| Legal fact | follows from enacted text or controlling authority | “The law requires identity-linked annual crypto-activity reporting for reportable users.” |
| Supported risk | a plausible harm supported by institutional, technical, incident, or claimant evidence | “Combining identity data with retained transfer records can increase profiling and breach consequences.” |
| Advocacy hypothesis | policy judgment or causal claim not yet proved | “The regime may drive users toward less regulated channels”; label it and test it. |

This separation should be visible in the wiki, website, press material, and expert instructions. A strong campaign does not need to describe every risk as an already proven constitutional violation.

## Core justiciable rights

### Privacy and data protection

The clearest legal starting point is an interference with:

- **section 1 DSG**, which protects confidentiality of personal data and requires a sufficiently specific legal basis and adequate safeguards;
- **Article 8 ECHR**, because identity-linked financial information falls within private life;
- **Charter Articles 7 and 8**, when Austria implements DAC8 and when the validity or interpretation of the Directive itself is in issue;
- **Charter Article 52(1)**, which requires legality, respect for the essence of rights, a legitimate objective, and proportionality.

The dispute is not whether processing occurs. It is whether each layer is sufficiently precise, necessary, minimized, time-limited, secure, reviewable, and effective for its stated purpose.

For Austria, section 20(1) gives the strongest national claim because it expressly extends tax-purpose processing to all customers, transactions, and crypto-assets regardless of reportability. A reliably non-reportable user sharpens necessity. For a reportable user, the challenge reaches DAC8 itself and must confront the adverse DAC2 and DAC6 case law.

### Occupational freedom and property

An Austria-home CASP can invoke Article 6 StGG and, where EU law is engaged, Charter Article 16. The claim should concern the legal duty and the proven incremental build, not generalized displeasure with regulatory cost. Property arguments require a concrete interference with assets or obligatory expenditure and are usually secondary to occupational freedom.

The strongest provider theory is a costed, technically workable reportable-user-only alternative. MiCA, TFR, AML, accounting, and ordinary business records must be removed from the counterfactual because those burdens exist independently.

### Equality and legal certainty

Article 7 B-VG and the equality principle can address unjustified differences between comparable businesses or users. “Austrian providers are worse off” is not enough: the comparison group, home-state/passporting position, actual additional duty, cost, and absence of a rational justification must be proved.

Precision and foreseeability become important where section 20(1) mandates storage but the deletion rule for never-transmitted section 18 aggregate profiles is unclear. The claim must present the actual provider interpretation, retention schedule, and deletion response rather than assert two incompatible readings as fact.

### Effective remedy

Charter Article 47, section 1 DSG remedies, GDPR access/deletion/objection mechanisms, the DSB, BVwG, and constitutional review matter both substantively and procedurally. Weak transparency, unknown recipients, inaccessible logs, or an ineffective correction process can strengthen the claim. But the existence of DSB/BVwG review is also the strongest objection to a user's direct Individualantrag.

### Context-specific rights

The following should be used only with claimant evidence:

- **freedom of expression and association:** if reporting or linkage actually reveals donations, membership, journalism, religious practice, or political activity and produces a measurable chilling effect;
- **non-discrimination:** if risk scoring, de-risking, or exclusion follows from a protected characteristic or unjustified proxy;
- **professional secrecy:** only for an applicant and dataset covered by a legally recognised confidential relationship; CJEU C-694/20 cannot be generalized to all crypto users;
- **physical integrity and home safety:** relevant to risk and proportionality when a concrete disclosure path and threat record exist, but not a substitute for proving what DAC8 actually transmits.

## Public-risk map

### Financial and behavioural profiling

The report links civil identity, home address, tax residence, and annual per-asset/per-category values, units, and counts. That can reveal asset exposure, trading intensity, transfer patterns, and changes over time. The degree of behavioural inference depends on the fields, history, access, and any linkage to other datasets.

DAC8 does **not** itself transmit wallet addresses, DLT addresses, transaction dates, transaction IDs, or counterparties. The accurate risk statement is that a provider or authority may hold those facts under another regime and that combining them with DAC8 identity data can create a richer graph. The linkage path must be demonstrated.

### Purpose and function creep

MiCA, TFR, AML/CFT, and tax reporting create adjacent databases with different legal purposes. Directive 2011/16/EU Article 16 already permits received DAC information to be used for covered taxes as well as VAT, other indirect taxes, customs, AML/CFT, and—with specified routing—for Union restrictive measures. That is a legislated purpose range, not secret or unlimited reuse. The remaining danger is further repurposing, broad access, new analytics, or retention beyond the justification and safeguards for each permitted purpose. TFR Article 25 is a useful contrast because it expressly confines travel-rule data to AML/CFT and bars incompatible use.

The litigation question is whether further processing has a legal basis and safeguards. The communications question is whether democratic oversight keeps pace with technically easy reuse.

### AML comparator and its limits

AML case law supplies both protective and adverse authority. Public WiEReG access was invalidated in CJEU C-37/20 and C-601/20 and VfGH G 265/2023, while VfGH G 62/2025 protected meaningful legitimate-interest access and VfGH E 2189/2025 upheld case-specific internal register data. CJEU C-562/20 supports evidence-based enhanced risk controls and statutory retention while subjecting national measures to legality, certainty, proportionality, and non-discrimination.

The usable principle is differentiated access and lifecycle safeguards. The unusable shortcut is that invalid public access also invalidates confidential reporting or FIU access. The EDPB/EDPS AML record reinforces precise purpose, minimisation, accuracy, restricted access, bounded retention, and safeguards against disproportionate profiling and de-risking.

### Breach and physical-security consequences

Identity, home-address and financial-activity data can be valuable targeting material. The located evidence makes several attack paths concrete without proving a DAC8-specific breach:

- in August 2026 the French tax authority reported credential-based extraction of identity, contact, tax and cadastral data concerning 678,000 persons and businesses;
- in February 2026 stolen government credentials exposed identity, postal-address and IBAN information for about 1.2 million French account records;
- Coinbase reported that paid support workers or contractors obtained identity data, balance snapshots and transaction history; and
- CNIL recorded 6,167 breach notifications in 2025 and identified account compromise as a recurring access path.

The DLT-specific issue is narrower. A verified wallet address or transaction hash can create a persistent entry point into a public ledger whose past and future context may become more informative as labels and transactions accumulate. MiCA Delegated Regulation 2025/1140 establishes that covered provider records can link identified buyer/seller data to on-chain hashes and wallet addresses through an internal transaction-record number. DAC8 does not transmit those anchors. Any claim of added harm must prove the provider record, legal access path and actual join.

Research on physical attacks against cryptocurrency holders confirms a real coercion threat, but the located sample identifies public exposure, acquaintances, investigation and peer-to-peer encounters as targeting routes. It does not establish tax-reporting or government-database leakage as a cause. Nor does the current evidence support a categorical statement that a DAC8 dataset is more dangerous than every conventional asset list. Risk depends on the fields, accuracy, home-address content, custody, chain, address reuse, access controls and retention.

The Grand Chamber's *Kurt v Austria* test confines an Article 2 operational protection duty to a real and immediate risk to an identified person known or knowable to authorities. General sector risk does not meet that standard. Physical harm should therefore ordinarily operate as a severity, security and urgency factor within the privacy and data-protection case, unless the claimant has a documented specific threat.

CJEU C-340/21 supports a concrete assessment of the nature, implementation and practical effects of security measures. It also holds that a breach or third-party access does not by itself prove inadequate safeguards. The evidence should therefore be used to test compartmentalisation, least-privilege access, bulk export, monitoring, logging and response, not as an automatic invalidity argument.

### Chilling and self-censorship

People may change saving, donation, investment, or political behaviour when they expect durable financial profiling. This is a legitimate research and communications hypothesis. A court filing needs claimant testimony, survey or behavioural evidence, and a clear link between the reported fields and the protected activity.

### De-risking and exclusion

Complex due diligence, sanctions, and uncertain status can incentivise providers to reject difficult customers, countries, self-hosted-wallet users, or low-value accounts. The risk should be measured through account closures, transaction blocks, customer support records, pricing, and jurisdictional withdrawal. Without those facts, describe it as an incentive problem rather than established discrimination.

### Centralisation and competition

High fixed compliance and security cost may favour large intermediaries, reduce provider diversity, and push activity toward custodial or opaque channels. That can conflict with resilience, competition, and enforcement goals. The WFA estimates material provider-wide costs, but the section 20(1) increment still requires provider evidence.

### Cross-border accountability and long-lived error

Automatic exchange increases the number of institutions, legal systems, correction steps, and access points involved. Incorrect residence, valuation, duplication, or classification can persist and propagate. The public-interest test should therefore include routing, controller roles, recipient logging, correction propagation, deletion, and remedies in every receiving state.

## Litigation proof versus communications proof

| Proposition | Minimum litigation evidence | Useful public evidence |
|---|---|---|
| universal national processing is unnecessary | statutory field map, final non-reportable status, actual pipeline, narrower working design | simple EU-minimum versus Austrian-addition diagram |
| long retention is excessive | exact legal basis, production/backups/deletion schedule, authority purpose, alternatives | retention timeline and breach-window explanation |
| identity-to-ledger correlation is dangerous | exact stored addresses/IDs, method, false-positive rate, access path, expert report | bounded demonstration with synthetic or consented data |
| physical safety risk is material | claimant threat model, recipients, security controls/incidents, expert evidence | verified incident data with explicit no-causation caveat |
| chilling or de-risking occurs | declarations, account closures, transaction refusals, survey/behavioural data | anonymised case studies and transparent methodology |
| costs distort competition | invoices, FTEs, system deltas, customer/provider counterfactual | provider survey separating baseline from national excess |

## Communications guardrails

### Green: state directly

- reporting is routine, identity-linked, and not based on individualized suspicion;
- Austria expressly processes section 18 information for all customers and transactions under section 20(1);
- MiCA/TFR and tax reporting have different purposes and retention rules;
- privacy, data protection, security, correction, and effective remedies require independent scrutiny;
- the campaign seeks a judicial answer, not tax evasion or the abolition of lawful tax enforcement.

### Amber: qualify and source

- the profile can enable wider inference when combined with other records;
- breaches can create financial and physical risks;
- compliance can encourage provider concentration, de-risking, or migration to harder-to-supervise channels;
- targeted or reportable-user-only designs may be equally effective.

### Red: do not publish as fact

- DAC8 reports every wallet address, transaction, counterparty, or date;
- every person's data is copied into 27 unrestricted national databases;
- a reported amount proves untaxed income or criminality;
- DAC8 has already caused a particular kidnapping or breach without evidence;
- the CJEU or VfGH must refer, must annul, or has already endorsed the campaign's theory.

## Positive public frame

The campaign is strongest when framed as **targeted tax enforcement with constitutional safeguards**:

> Tax compliance and fundamental rights are compatible. Authorities should receive the information shown to be necessary for a defined tax purpose, from persons who are reportable, for a justified period, with secure access, correction, deletion, independent review, and no silent repurposing.

This frame is reusable across Member States and avoids making the project depend on hostility to taxation, MiCA, or regulated providers.

## See Also

- [[dac8-charter-proportionality|DAC8 Charter Proportionality]] ([DAC8 Charter Proportionality](dac8-charter-proportionality.md))
- [[mica-tfr-krypto-mpfg-nexus|MiCA, TFR, and the Krypto-MPfG Nexus]] ([MiCA, TFR, and the Krypto-MPfG Nexus](mica-tfr-krypto-mpfg-nexus.md))
- [[member-state-challenge-and-communications-playbook|Member-State Challenge and Communications Playbook]] ([Member-State Challenge and Communications Playbook](../references/member-state-challenge-and-communications-playbook.md))
- [[dac8-and-the-wealth-register-risk|DAC8 and the Wealth-Register Risk]] ([DAC8 and the Wealth-Register Risk](dac8-and-the-wealth-register-risk.md))
- [[aml-financial-intelligence-and-fundamental-rights|AML Financial Intelligence and Fundamental Rights]] ([AML Financial Intelligence and Fundamental Rights](aml-financial-intelligence-and-fundamental-rights.md))
- [[austrian-aml-crypto-implementation|Austrian AML Crypto Implementation]] ([Austrian AML Crypto Implementation](austrian-aml-crypto-implementation.md))
- [[identity-to-public-ledger-linkage-evidence|Identity-to-Public-Ledger Linkage Evidence]] ([Identity-to-Public-Ledger Linkage Evidence](../references/identity-to-public-ledger-linkage-evidence.md))
- [[financial-data-breach-and-security-authorities|Financial-Data Breach and Security Authorities]] ([Financial-Data Breach and Security Authorities](../references/financial-data-breach-and-security-authorities.md))
- [[krypto-mpfg-provider-record-architecture|Krypto-MPfG Provider Record Architecture]] ([Krypto-MPfG Provider Record Architecture](../references/krypto-mpfg-provider-record-architecture.md))
- [[dac8-physical-risk-causation|DAC8 Physical-Risk Causation and Evidence]] ([DAC8 Physical-Risk Causation and Evidence](../references/dac8-physical-risk-causation.md))

## Sources

- [DAC8](../../../legal-docs/core/eu-dac8-directive-2023-2226.pdf)
- [Krypto-MPfG](../../../legal-docs/core/at-bgbl-i-96-2025-krypto-mpfg.pdf)
- [EU Charter](../../../legal-docs/core/eu-charter-fundamental-rights-2016.pdf)
- [GDPR](../../../legal-docs/core/eu-gdpr-regulation-2016-679.pdf)
- [Final EDPB blockchain guidance](../../../legal-docs/supporting/eu-edpb-guidelines-02-2025-blockchain-v2.pdf)
- [CJEU and security-evidence corpus](../../../legal-docs/_index.md)
