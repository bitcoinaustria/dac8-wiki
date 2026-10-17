---
title: "Leaked Data, Financial Scams and Targeted Attacks"
category: reference
sources:
  - raw/articles/2026-10-15-scam-trezor-brevo-phishing.md
  - raw/articles/2026-10-15-scam-trezor-shipmonk-retention.md
  - raw/articles/2026-10-15-scam-trezor-support-2024.md
  - raw/articles/2026-10-15-scam-ledger-shopify-remediation.md
  - raw/articles/2026-10-15-scam-coinbase-costs-10q.md
  - raw/articles/2026-10-15-scam-epsilon-admitted-data-reuse.md
  - raw/articles/2026-10-15-scam-epsilon-trial-harm.md
  - raw/articles/2026-10-15-scam-eurojust-recovery-retargeting.md
  - raw/articles/2026-10-15-scam-fca-recovery-rooms.md
  - raw/articles/2026-10-15-scam-austria-recovery-knowledge.md
  - raw/articles/2026-10-15-scam-tyurin-stolen-bank-contacts.md
  - raw/articles/2026-10-15-scam-talktalk-parliament-harm.md
  - raw/articles/2026-10-15-scam-france-crypto-impersonation.md
  - raw/articles/2026-10-15-scam-france-breach-physical-harm.md
  - raw/articles/2026-10-15-scam-tangeman-stolen-databases.md
  - raw/articles/2026-10-15-scam-tangeman-sentencing.md
created: 2026-10-15
updated: 2026-10-17
verified: 2026-10-15
tags: [data-breach, financial-fraud, phishing, repeat-targeting, physical-security, evidence-limits]
aliases: [Leak-enabled phishing, Recovery scam evidence, Financial victim lists]
confidence: medium
volatility: hot
summary: "Primary sources document leak-enabled phishing, customer-list exploitation and repeated financial harm. Official physical-risk accounts are stronger than hypothetical warnings but do not establish a DAC8 leak or an Austrian attack probability."
---

# Leaked Data, Financial Scams and Targeted Attacks

Leaked contact and customer-relationship information can be used to select people and make fraudulent approaches credible even when no password, private key or exact wealth figure was disclosed. This is an observed exploitation pathway, not merely a theoretical possibility. The strength of evidence nevertheless differs for extraction, contact, engagement, theft and physical harm. Criminal reuse of legitimately collected marketing data and records from an earlier scam is a separate pathway from a security breach.

This reference expands incident evidence as checked on 15 October 2026. The 17 October analytical supplement below links separately verified market, empirical and control research; it does not refresh the incident snapshots or older legal authorities comprehensively.

## Distinguish the endpoints before counting victims

| Endpoint | Evidence needed | Mistake to avoid |
|---|---|---|
| Exposure or extraction | Identified system, fields and confirmed access/export | Counting every potentially accessible record as extracted |
| Targeted contact | A message or call linked to the exposed population | Treating every fraudulent approach as evidence of a leak |
| Engagement | Click, reply or interaction | Treating a click as a disclosed recovery phrase or a stolen balance |
| Secret disclosure or authorisation | Evidence that a secret was supplied or an operation approved | Assuming funds were directly accessible through contact data |
| Financial loss | Verified transfers, victim accounts or specified trial evidence | Equating company incident expenses with customers' stolen funds |
| Repeat harm | A consistent victim identity across successive frauds | Counting contacts as repeated successful thefts |
| Physical targeting or harm | Source of the target/address and evidence of its use | Converting aggregate operational attribution into a named leak-to-assault judgment |

This is an evidentiary sequence, not a claim that every incident passes through every stage. Fraud can fail; the same list can be reused; a physical approach can bypass digital secret disclosure entirely.

## Specific breaches followed by actual fraud approaches

| Record | Information and observed endpoint | Source status and limiting result |
|---|---|---|
| [Trezor support, January 2024](../../raw/articles/2026-10-15-scam-trezor-support-2024.md) | Name/email context; 41 direct recovery-seed requests after portal intrusion | First-party confirmation of contact; up to 66,000 potentially accessible records, not confirmed extraction. No disclosed seeds or compromised funds at reporting. |
| [Trezor/Brevo, September 2026](../../raw/articles/2026-10-15-scam-trezor-brevo-phishing.md) | 347,149 newsletter emails exported; campaign to about 347,000 recipients; about 2,500 clicks | Company account: compromise, campaign and engagement. No secret-disclosure or loss count. These denominators must remain separate. |
| [Ledger/Shopify, 2020–2021](../../raw/articles/2026-10-15-scam-ledger-shopify-remediation.md) | Insider order-data export; phishing acknowledged | Overlapping exposures, not additive customer counts; campaign losses not allocated between datasets. Supplier records are distinct from hardware keys. |
| [Financial-sector intrusions/Tyurin](../../raw/articles/2026-10-15-scam-tyurin-stolen-bank-contacts.md) | Stolen customer contacts used for deceptive securities promotion | DOJ account following guilty plea and sentence; direct financial-customer-list exploitation, not proof all exposed customers lost money. |
| [TalkTalk supplier incidents](../../raw/articles/2026-10-15-scam-talktalk-parliament-harm.md) | Committee received evidence of scam-call losses following supplier breaches | Witness evidence, not judicial causation. Committee expressly received no financial-loss evidence directly attributable to the separate cyberattack itself. |

The Trezor support case is particularly useful adverse evidence: a real intrusion and actual targeted requests did not produce the alleged final harm at the time of the statement. It supports timely intervention, not dismissal of the attempted exploitation. Conversely, the absence of keys in the exposed database does not make the later impersonation stage harmless.

Brevo adds an important distinction: an attacker used a compromised legitimate communication service as well as exporting a contact list. That access could contribute credibility independently of personalisation. The record does not isolate how much of the campaign's engagement was caused by leaked data rather than the sending channel.

### Coinbase: accounting is not a theft census

The [June 2026 Form 10-Q](../../raw/articles/2026-10-15-scam-coinbase-costs-10q.md) reports USD 306.654 million of net incident losses in Q2/H1 2025 and later net recoveries of USD 33.854 million in Q2 2026 and USD 25.244 million in H1 2026. The measure mixes reimbursements, direct legal costs and qualifying rewards if any. It confirms a realised financial burden but is not a customer-theft total or victim count. Quarter and half-year figures overlap; losses and later recoveries must both be disclosed.

## Data can become a reusable targeting asset

### Admitted cross-client reuse and trial-reported repeat harm

The [Epsilon corporate admissions](../../raw/articles/2026-10-15-scam-epsilon-admitted-data-reuse.md) establish more than exposure: transactional/response data from legitimate and fraudulent clients were combined, sold to known fraud operators and reused after one operator was closed by court order. This was deliberate onward use, not an intrusion.

The separate [post-trial sentencing account](../../raw/articles/2026-10-15-scam-epsilon-trial-harm.md) reports one client's fraud against more than 218,000 people, over USD 23.7 million in losses and over 12,000 people defrauded more than twenty times each. Corporate admissions under deferred prosecution and employees' jury convictions are different procedural facts. The reported compensation is separate from the original loss figures and cannot be treated as no recovery.

The supported mechanism is selection using observed behaviour, followed by repeated approaches. It does not require estimating a person's total wealth. A dataset can be valuable to a criminal because it identifies a relevant relationship or likely response, even where it contains no current balance. No comparable predictive accuracy for DAC8 annual aggregates was tested here.

### Recovery scams: domestic relevance without invented leak attribution

Three complementary sources establish reuse of prior-victim context:

- The [FCA](../../raw/articles/2026-10-15-scam-fca-recovery-rooms.md) describes original operators reapproaching victims under another identity or selling their details to recovery rooms.
- The [Austrian Bundeskriminalamt](../../raw/articles/2026-10-15-scam-austria-recovery-knowledge.md) describes detailed first-fraud knowledge used to rebuild trust under official, legal or financial-institution identities.
- [Eurojust's Austrian–Albanian operation](../../raw/articles/2026-10-15-scam-eurojust-recovery-retargeting.md) documents recontacting earlier investment victims for purported recovery, after an investigation originating in Vienna. It is an investigation account, not a conviction; its wider estimated losses are not all recovery-scam losses.

These sources must not be described as proof of a hacked government or provider database. Operators may possess records because they ran the original scam; others may buy them. Knowing details of a genuine prior loss does not authenticate the new caller. Reuse is established at a broader level than the precise acquisition route.

## Physical targeting: stronger official evidence, bounded attribution

The [French national cyber-assistance report](../../raw/articles/2026-10-15-scam-france-breach-physical-harm.md), printed pp.48–49, describes exploitation of crypto-sector breaches escalating in some situations to threats and assaults against victims or relatives. This is an official operational account of observed consequences, not only a hypothetical warning. It supplies no named-provider causal judgment or population denominator. Its personalised-IBAN phishing example has only possible attribution to particular earlier leaks; that weaker attribution must remain explicit.

The [French crypto-sector notice](../../raw/articles/2026-10-15-scam-france-crypto-impersonation.md) documents fake-adviser reports and relays prosecutors' warnings about bogus officials seeking more financial information or home contact. It describes the Waltio investigation at its stated update; it is not a current docket check or a finding that a named Waltio customer was assaulted.

In the [Tangeman plea announcement](../../raw/articles/2026-10-15-scam-tangeman-stolen-databases.md), DOJ expressly attributes crypto-theft target selection to stolen databases in an enterprise that also included residential burglars. The [sentencing update](../../raw/articles/2026-10-15-scam-tangeman-sentencing.md) records seventy months' imprisonment. The database provider, fields and route for each burglary remain unspecified. This is the same case 24cr417 as the existing Ferro evidence, not another criminal enterprise to add to incident counts.

Taken together with the earlier Waltio police attribution, this rules out the blanket statement that official evidence concerns only speculative exploitation. It does not establish that a specified Ledger, Kroll or Fractal ID leak caused a physical assault, that DAC8 data were involved, or that an Austrian controller's safeguards failed.

## Provider concentration and retention are independent risk strands

The relevant concentration is not limited to the final authority report. Support portals, mailing services, fulfilment partners and other intermediaries can hold different identifying subsets. A breach of one subset can create a plausible approach through which an offender seeks more information or induces an action. A protected wallet key does not protect the surrounding identity/contact ecosystem.

The [ShipMonk update](../../raw/articles/2026-10-15-scam-trezor-shipmonk-retention.md) supplies a concrete persistence counterexample: historical order records were included despite reported written deletion assurances. Its revised overall affected population is 80,689, not the sum of that figure and earlier components. This is a vendor-retention failure account, not evidence that every deletion policy fails or that a resulting assault occurred.

Ledger's announced segregation and reduced supplier-field plans show specific alternatives, but their implementation must be tested separately. The later archive implementation account remains in the existing concentration reference. These records support checking effective data removal and restricted availability, not relying solely on policy text.

For an assessment, keep at least four scopes separate:

1. Data actually retained by the principal provider and its contractors.
2. Data routinely supplied to an authority.
3. Information obtainable through additional access, joins or attacker interaction.
4. Data already copied outside the controller's reach.

Future access restrictions may reduce new exposure without recalling stolen copies. Conversely, previously stolen contact data do not automatically grant continuing account access. Persistent targeting and persistent technical access are different claims.

## Transfer to the Austrian DAC8 assessment

The useful proposition is concrete and limited: retention and joinability can create reusable selection and credibility resources, whose misuse does not require direct spend authority or an accurate net-wealth estimate. Some records demonstrate extraction-to-contact, others actual repeated financial harm, and French official observations extend the severity assessment to physical consequences. Their evidentiary differences are material, not reasons to disregard provider-side exposure.

For a specific system, the incremental effect still requires evidence. Do not silently add newsletter emails, telephone numbers, support tickets, wallet backups or a detailed transaction history to the routine annual report. Use the existing provider/report-layer mapping to identify the actual additional fields and joins. The Epsilon modelling involved transaction/response history, not annual tax aggregates; a hypothesis about matching the latter requires its own test.

The current evidence supports examining:

- whether a routine support role can view or export identity, address and financial attributes together;
- whether marketing, support and statutory archives share identifiers or export pathways;
- whether reduced contact/address collection, shorter unnecessary retention or compartmentalised access changes the reachable population;
- whether alleged deletion covers supplier copies, backups and restored data, with effectiveness evidence rather than assurances alone;
- whether official security notifications can be independently authenticated without requiring trust in an unsolicited message;
- whether incident response measures prevent contact, engagement, secret disclosure, transfer or net loss, measured separately.

These are testable design questions, not findings that Austrian controls are absent or that an alternative has equal tax utility. None of the new sources establishes a DAC8 breach, an Austrian leak-caused physical attack, or an incremental person-level attack rate.

## Deeper analytical supplement checked 17 October 2026

The [[criminal-data-markets-and-repeat-victimisation|criminal-market reference]] ([criminal-market reference](criminal-data-markets-and-repeat-victimisation.md)) adds admitted response-data feedback, a priced targeting-list business, explicit high-balance selection and insider resale. It preserves completed-DPA status, charging-document limits, reimbursement and successful monitoring. Deliberate brokerage, original-scam records and technical breaches remain different acquisition routes.

The [[phishing-causal-evidence-and-measurement|empirical reference]] ([empirical reference](phishing-causal-evidence-and-measurement.md)) distinguishes targeting associations, contextual experiments, actual repeat payments and effective controls. It retains denominator defects and adverse results. These studies cannot be combined into one Austrian leak-to-loss multiplier, and richer profiles are not uniformly more effective.

The [[financial-data-threat-model-and-control-evaluation|integrated technical assessment]] ([integrated technical assessment](financial-data-threat-model-and-control-evaluation.md)) connects those findings to field/copy inventories, rolling retention, blockchain anchors and matched-workload alternatives. It distinguishes login, recovery, transaction intention and confidentiality. Its security questions are not findings that Austria lacks the proposed safeguards.

## Remaining proof gaps

- **Acquisition provenance:** which exact records an attacker possessed and how they were obtained. Generic recovery calls cannot settle this.
- **Field contribution:** whether personal details, apparent provider status, financial amounts or control of the genuine sending channel changed the outcome.
- **Exposure denominator:** confirmed exposed people, non-victims, repeated attempts and outcome follow-up. Incident examples alone cannot estimate prevalence or relative risk.
- **Counterfactuals:** public profiles, voluntary disclosures, personal relationships and original-scam records as alternative targeting routes.
- **Local implementation:** actual roles, exports, data copies, retention and tested controls. Foreign incidents are not findings about Austria.
- **Procedural finality:** the source dates establish the reported pleas, sentences or investigations; later appeals and current dockets were not comprehensively checked.

The AMF recovery-scam survey was not ingested: full primary access returned a maintenance response, so indexed figures were not promoted as verified findings. No leaked dataset or private victim record was collected.

## See Also

- [[privacy-financial-privacy-and-surveillance|Privacy, Financial Privacy and Surveillance]] ([Privacy, Financial Privacy and Surveillance](../topics/privacy-financial-privacy-and-surveillance.md)) — broader everyday interests complement the documented leak and targeting pathway.
- [[provider-control-boundaries-and-observed-failures|Provider Control Boundaries and Observed Failures]] ([Provider Control Boundaries and Observed Failures](provider-control-boundaries-and-observed-failures.md)) — actual prevention, shared exports, reporting entitlements and historical-copy protection.
- [[criminal-data-markets-and-repeat-victimisation|Criminal Data Markets and Repeat Victimisation]] ([Criminal Data Markets and Repeat Victimisation](criminal-data-markets-and-repeat-victimisation.md)) — priced targeting, feedback and insider incentives.
- [[phishing-causal-evidence-and-measurement|Phishing, Repeat Harm and Causal Measurement]] ([Phishing, Repeat Harm and Causal Measurement](phishing-causal-evidence-and-measurement.md)) — empirical endpoints and adverse evidence.
- [[financial-data-threat-model-and-control-evaluation|Financial-Data Threat Model and Control Evaluation]] ([Financial-Data Threat Model and Control Evaluation](financial-data-threat-model-and-control-evaluation.md)) — integrated assessment and independent-expert protocol.
- [[financial-data-breach-and-security-authorities|Financial-Data Breach and Security Authorities]] ([Financial-Data Breach and Security Authorities](financial-data-breach-and-security-authorities.md)) — provider/authority layers and existing security-law boundaries.
- [[dac8-physical-risk-causation|DAC8 Physical-Risk Causation and Evidence]] ([DAC8 Physical-Risk Causation and Evidence](dac8-physical-risk-causation.md)) — causal ladder, competing targeting routes and claimant-specific proof.
- [[bearer-asset-irreversibility-and-leak-consequences|Bearer-Asset Irreversibility and Leak Consequences]] ([Bearer-Asset Irreversibility and Leak Consequences](bearer-asset-irreversibility-and-leak-consequences.md)) — distinguishes compromised surrounding data from key control and loss allocation.
- [[financial-data-concentration-proof-and-alternatives|Financial data concentration evidence and alternative processing designs]] ([Financial data concentration evidence and alternative processing designs](financial-data-concentration-proof-and-alternatives.md)) — archive implementation, legal-retention limits and alternative-utility testing.

## Sources

- [Trezor/Brevo campaign and exported emails](../../raw/articles/2026-10-15-scam-trezor-brevo-phishing.md)
- [Trezor/ShipMonk historical retention](../../raw/articles/2026-10-15-scam-trezor-shipmonk-retention.md)
- [Trezor support contact and no-loss findings](../../raw/articles/2026-10-15-scam-trezor-support-2024.md)
- [Ledger/Shopify overlap and remediation plans](../../raw/articles/2026-10-15-scam-ledger-shopify-remediation.md)
- [Coinbase incident costs and recoveries](../../raw/articles/2026-10-15-scam-coinbase-costs-10q.md)
- [Epsilon admitted data pipeline](../../raw/articles/2026-10-15-scam-epsilon-admitted-data-reuse.md)
- [Epsilon trial-reported harm and compensation](../../raw/articles/2026-10-15-scam-epsilon-trial-harm.md)
- [Eurojust Austrian–Albanian operation](../../raw/articles/2026-10-15-scam-eurojust-recovery-retargeting.md)
- [FCA recovery-room data reuse](../../raw/articles/2026-10-15-scam-fca-recovery-rooms.md)
- [Austrian police recovery-scam mechanism](../../raw/articles/2026-10-15-scam-austria-recovery-knowledge.md)
- [Tyurin: stolen financial-customer contacts](../../raw/articles/2026-10-15-scam-tyurin-stolen-bank-contacts.md)
- [TalkTalk parliamentary evidence boundary](../../raw/articles/2026-10-15-scam-talktalk-parliament-harm.md)
- [French crypto-sector impersonation notice](../../raw/articles/2026-10-15-scam-france-crypto-impersonation.md)
- [French annual report: exploitation and physical harm](../../raw/articles/2026-10-15-scam-france-breach-physical-harm.md)
- [Tangeman: explicit stolen-database attribution](../../raw/articles/2026-10-15-scam-tangeman-stolen-databases.md)
- [Tangeman: sentencing update in the same case](../../raw/articles/2026-10-15-scam-tangeman-sentencing.md)
