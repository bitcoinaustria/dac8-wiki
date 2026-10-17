---
title: "Criminal Data Markets and Repeat Victimisation"
category: reference
sources:
  - raw/articles/2026-10-17-scam-kbm-feedback-admissions.md
  - raw/articles/2026-10-17-scam-kbm-completed-dpa.md
  - raw/articles/2026-10-17-scam-murray-priced-lists.md
  - raw/articles/2026-10-17-scam-lam-plea-scope.md
  - raw/articles/2026-10-17-scam-lam-large-balance-information.md
  - raw/articles/2026-10-17-scam-rac-insider-convictions.md
  - raw/articles/2026-10-17-scam-rac-confiscation-update.md
  - raw/articles/2026-10-15-scam-epsilon-admitted-data-reuse.md
  - raw/articles/2026-10-15-scam-epsilon-trial-harm.md
  - raw/articles/2026-10-15-scam-fca-recovery-rooms.md
  - raw/articles/2026-10-17-depth-meiggs-selection-signals.md
  - raw/articles/2026-10-17-depth-community-carrier-authority.md
  - raw/articles/2026-10-17-depth-faulk-admitted-demands.md
  - raw/articles/2026-10-17-depth-faulk-restitution-order.md
created: 2026-10-17
updated: 2026-10-17
verified: 2026-10-17
volatility: hot
confidence: medium
tags: [data-broker, financial-fraud, insider-risk, repeat-victimisation, criminal-economics]
aliases: [Criminal value of customer data, Victim-list feedback loops]
summary: "Admissions and enforcement records establish priced targeting, response feedback, high-balance selection and insider resale, without supplying a DAC8 attack rate."
---

# Criminal Data Markets and Repeat Victimisation

Customer data can be an input to a criminal business without being a payment credential. It can identify whom to approach, which relationship to impersonate, who previously responded, or which account appears worth pursuing. These are different economic functions. Their existence is supported by records of admitted conduct and prosecution, not only by warnings about what might happen.

The source set does not demonstrate that every retained field is valuable, that value increases monotonically with data volume, or that Austrian reporting systems have the same access weaknesses. This reference assesses mechanisms, not a prevalence estimate.

## Separate the data-acquisition routes

| Route | What the record establishes | What it does not establish |
|---|---|---|
| External intrusion | Customer data taken outside authorised systems; prior incident reference supplies examples | That every attempted scam came from that intrusion |
| Insider extraction/resale | RAC convictions and Lam plea account establish abuse of trusted access | That possession of a valid login made the conduct authorised |
| Deliberate brokerage | Epsilon and KBM admissions establish knowing supply to fraud clients | A technical security breach or GDPR-lawful original collection |
| Original-scam records | Prior response/payment context supports later targeting and recovery approaches | Hacking of a bank, CASP or authority database |

A security assessment confined to external hacking excludes several established mechanisms. Conversely, combining every misuse route under “data leak” obscures which controls could have interrupted it. A consent-resolved complaint, corporate admission, guilty plea and trial conviction also carry different evidentiary weight.

## Different offenders seek different signals

**Capacity:** a liquid balance or other indication of ability to pay. **Credibility:** a genuine customer relationship or transaction detail that makes an approach seem informed. **Responsiveness:** previous engagement, payment or an unresolved loss. **Operational opportunity:** identifiers that a weak support or account-change process may accept. These categories are a technical synthesis of the cases, not a validated criminal scoring model.

It follows that “the data do not prove total wealth” is not a sufficient answer to targeting risk. Nor should it be replaced by “criminals never need balances”. The sources establish both non-balance targeting and deliberate balance selection.

### High-balance targeting is not merely conjectural

The [Lam plea account](../../raw/articles/2026-10-17-scam-lam-plea-scope.md) confirms a plea concerning insider selection of large-balance accounts. The [information](../../raw/articles/2026-10-17-scam-lam-large-balance-information.md), count one §4, describes requests for monthly large-balance reports and approximately USD3.387 million successfully stolen, against USD6.536 million attempted. These detailed filing allegations should remain paired with the plea confirmation; the full stipulation was not retrieved. One customer's roughly USD417,300 was reimbursed.

The headline USD3.434 million combines two schemes. It is not all attributable to disclosed data. The scheduled 15 October 2026 sentence is now past but its outcome was not verified. This record proves neither current DAC8 report access nor an Austrian attack rate.

### Targeting information has a price distinct from stolen funds

The [Murray sentencing account](../../raw/articles/2026-10-17-scam-murray-priced-lists.md) describes a maintained list business: typically USD500 for 100–300 names, with contact details and sometimes age/email. More than USD5.2 million in broker receipts and more than USD9.5 million in victim losses are different measures. The listed population of over seven million is not the number proven to have lost money.

The inference is that downstream operators valued access to selected people. It does not establish a current market price for tax reports, a marginal price for each data field, or how those particular lists were originally acquired.

## Feedback can make the information reusable

The [KBM admissions](../../raw/articles/2026-10-17-scam-kbm-feedback-admissions.md) describe cross-client models using interaction histories and acquiring fraud-client response data that enhanced later targeting. The mechanism includes a feedback incentive as well as direct sales revenue. Finance initially refused a line of credit after fraud warnings, inhibiting licensing; managers obtained reversal and data shipments followed.

This matters because an access-control system can operate as designed while business decisions approve harmful onward disclosure. Internal approval does not make that disclosure lawful. Credentials and encryption do not by themselves address a deliberate business decision. KBM's [completed DPA and dismissal](../../raw/articles/2026-10-17-scam-kbm-completed-dpa.md) must be stated: these are admissions under deferred prosecution, not a corporate conviction. Its compensation population may overlap Epsilon's.

The earlier Epsilon records add reuse after one operator's closure and trial-reported repeated harm. The FCA's recovery-room account adds reapproach under another identity and sale of earlier victims' details. Together they establish that deleting one operator's live records or closing one scam does not necessarily remove information held by others. They do not demonstrate indefinite technical account access.

## Insider abuse can be detected and punished

The [RAC convictions](../../raw/articles/2026-10-17-scam-rac-insider-convictions.md) establish extraction and resale of accident-related information by customer-service staff. They also establish an effective countermeasure in that case: new monitoring revealed the conduct, followed by investigation and guilty pleas. Over 29,500 lines must not become 29,500 unique victims.

The [2026 confiscation update](../../raw/articles/2026-10-17-scam-rac-confiscation-update.md) is the same event, not another breach. GBP118,852.32 was ordered; only the smaller GBP33,125 payment was expressly confirmed. Neither record measures subsequent scam losses. Evidence that controls sometimes work belongs in the assessment alongside evidence of abuse.

## Cross-provider capabilities and subsequent demands

The [Meiggs/Harrington sentencing account](../../raw/articles/2026-10-17-depth-meiggs-selection-signals.md) identifies crypto executives, people thought to hold crypto and valuable social-media handles as selection categories. It does not establish how each target was discovered. Those categories are competing selection signals, not proof of an exclusively public-information route or absence of leaked data. The release still describes its approximate theft figure as alleged; the earlier stolen-or-attempted figure is not additive.

[The Community sentencing account](../../raw/articles/2026-10-17-depth-community-carrier-authority.md) describes a different intermediate capability: bribed carrier staff or customer impersonation enabled control of a communication channel, followed by recovery-chain access to other accounts. The initial capability was neither a wallet key nor necessarily an accurate balance estimate. But carrier authority is not itself a leaked financial record, and original target acquisition remains unspecified.

The [Faulk account](../../raw/articles/2026-10-17-depth-faulk-admitted-demands.md) adds admitted conduct involving theft followed by demands backed by threats of further account compromise. This supports staged harm rather than an assumption of endless technical access. The wire-fraud conspiracy plea and sentence must remain distinct from the extortion count dismissed at sentencing.

Its [2025 court-order supplement](../../raw/articles/2026-10-17-depth-faulk-restitution-order.md) also prevents treating the original restitution headline as a verified current total: the court identified legally incorrect, understated amounts and amendment litigation. That order does not establish final amended sums or money paid. Forfeiture, restitution and remission are not interchangeable recoveries.

The synthesis is a capability chain: selection information, a separate access or recovery weakness, newly obtained context, then theft or further demands. It does not establish that every stage needs a leak or exists in Austria. An annual tax identifier is not automatically a usable recovery credential. The expert must isolate what each actual field contributes at each stage rather than transfer the entire foreign attack to DAC8.

## Consequences for a technical opinion

The useful unit of analysis is a **reachable data combination**: what one person, compromised role, contractor or permitted onward recipient can obtain and join. Counting database rows alone misses whether identifiers, contact information and financial attributes become available together.

An expert should distinguish the ability to select a promising target from the ability to prove beneficial ownership. A criminal can act on an inaccurate belief; false-positive selection may still cause distress, fraud attempts or coercion. This is a threat-model inference, not a measured rate. Court-grade attribution standards remain necessary when asserting who actually owned funds.

The case set supports testing support/export privileges, business approvals, recipient due diligence, response-data reuse and supplier reach. It does not establish that every such feature is present in an Austrian CASP or tax authority. Nor does it show that abolishing one reporting duty would remove independently required AML, transfer or investment-service records.

The correct comparison is therefore the current lawful baseline against specified alternatives: which additional fields, copies, users, purposes and retention periods change the opportunity? A claim about the marginal effect of DAC8 needs that comparison; foreign fraud totals cannot substitute for it.

## See Also

- [[leaked-data-scams-and-targeted-attacks|Leaked Data, Financial Scams and Targeted Attacks]] ([Leaked Data, Financial Scams and Targeted Attacks](leaked-data-scams-and-targeted-attacks.md)) — incident-level endpoints and physical-harm attribution.
- [[phishing-causal-evidence-and-measurement|Phishing, Repeat Harm and Causal Measurement]] ([Phishing, Repeat Harm and Causal Measurement](phishing-causal-evidence-and-measurement.md)) — empirical tests and selection limits.
- [[financial-data-threat-model-and-control-evaluation|Financial-Data Threat Model and Control Evaluation]] ([Financial-Data Threat Model and Control Evaluation](financial-data-threat-model-and-control-evaluation.md)) — integrated architecture and audit protocol.

## Sources

The frontmatter lists immutable source digests. The linked digests preserve original URLs, dates, procedural status, denominators and source-specific limits. Repeated source documents for one event are not counted as independent incidents.
