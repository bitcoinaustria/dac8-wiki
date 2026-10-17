---
title: "Financial-Data Threat Model and Control Evaluation"
category: reference
sources:
  - raw/articles/2026-10-17-scam-nist-authentication-recovery.md
  - raw/articles/2026-10-17-scam-nist-proofing-privacy.md
  - raw/articles/2026-10-17-scam-nist-sanitisation-validation.md
  - raw/articles/2026-10-17-scam-edpb-breach-examples.md
  - raw/articles/2026-10-17-scam-eba-ecb-payment-fraud-2025.md
  - raw/articles/2026-10-17-scam-eba-loss-allocation-supplement.md
  - raw/articles/2026-10-17-scam-edpb-financial-centralisation.md
  - raw/articles/2026-10-17-scam-cjeu-scalable-identity-theft.md
  - raw/articles/2026-10-17-scam-cjeu-quirin-fear-supplement.md
  - raw/articles/2026-10-17-scam-kbm-feedback-admissions.md
  - raw/articles/2026-10-17-scam-lam-large-balance-information.md
  - raw/articles/2026-10-15-scam-trezor-shipmonk-retention.md
  - raw/articles/2026-10-15-scam-trezor-brevo-phishing.md
  - raw/papers/2026-10-17-depth-nist-deidentification.md
  - raw/papers/2026-10-17-depth-nist-dp-trust-boundary.md
created: 2026-10-17
updated: 2026-10-17
verified: 2026-10-17
verification_scope: "New standards, empirical/control synthesis and the two named CJEU holdings were checked. Linked historical DAC8 field maps, retention law and protocol references retain their own verification dates; actual Austrian systems were not audited."
volatility: hot
confidence: medium
tags: [financial-data, threat-model, provider-risk, retention, blockchain, controls, expert-evidence]
aliases: [Financial data expert assessment, Leak threat model and alternatives]
summary: "An integrated technical assessment of reusable targeting information, longitudinal profiles, blockchain anchors, security boundaries and falsifiable alternatives, with explicit Austrian implementation gaps."
---

# Financial-Data Threat Model and Control Evaluation

Identity-linked financial records can create a reusable targeting and credibility resource. The relevant security property is not simply whether a database is encrypted: it is which people and systems can combine which attributes, for what purpose, over what period, and with what ability to extract them. This source-based assessment is not an independent audit of a provider or Austrian authority.

The strongest supported general argument concerns incremental opportunity and potentially serious consequences. The evidence does not provide a DAC8-specific breach probability, a reliable current net-wealth calculation for every user, or a proof that one alternative delivers identical tax utility.

## 1. Model the information ecosystem, not one database

At least five layers must be inventoried separately:

1. **Provider records:** identity checks, account and transfer records, support histories and other data actually held under their respective purposes and legal bases.
2. **Routine reports:** the fields actually transmitted in a defined annual reporting payload, not everything the provider can access.
3. **Additional access and processing:** lawful case-specific retrieval, joins, correction histories, exports and derived features.
4. **Contractor and operational copies:** mailing, support, fulfilment, analytics, backups and restored systems, each with its own field subset and access path.
5. **Copied-out information:** stolen exports and any identity or ledger mappings already derived from them.

A breach of one layer is not proof that all layers were exposed. Conversely, protecting the report interface does not establish security of the surrounding provider ecosystem. The ShipMonk account supplies a concrete warning about historical records surviving deletion assurances; Brevo shows that control of a genuine communication service can accompany list extraction. Neither proves that all suppliers fail.

The expert inventory should identify field provenance, purpose, identifier, time range, copy location, access role and onward destination. A diagram showing separate servers is insufficient if one support role or shared administrator can retrieve and join all of them.

## 2. Separate information functions from spend authority

Data can perform four different functions: select a plausible target, supply credible context, defeat a weak identity or recovery check, or reveal a useful financial/ledger relationship. None is identical to holding a private key or a valid payment credential.

The [criminal-market evidence](criminal-data-markets-and-repeat-victimisation.md) establishes both response-based selection and deliberate high-balance targeting. The [empirical evidence](phishing-causal-evidence-and-measurement.md) separates targeting from engagement and completed payments. It is therefore wrong both to dismiss all contact data as harmless and to treat all data exposure as direct access to funds.

**Technical inference:** a criminal's decision threshold is not a court's attribution threshold. Someone may be selected on an inaccurate estimate of wealth or control. The estimate's failure to prove ownership does not make the approach harmless. It does, however, prevent the expert from claiming accurate ownership or population-wide wealth inference without ground truth.

## 3. A multi-year profile is not the sum of annual flows

Repeated records can reveal persistence, changes in activity, recurring provider relationships and candidate targets for further inquiry. That is a meaningful information gain even when each annual record is incomplete. Its magnitude depends on identifiers, fields, classification, coverage and available auxiliary data.

But a flow is not a stock. The same units can be bought, transferred between a person's own accounts, exchanged and sold; adding reported values can count the same economic resources repeatedly. Missing opening holdings, unobserved counterparties, provider-internal activity, debt, derivatives and price changes further prevent simple conversion into net wealth. More years do not automatically remove those ambiguities.

The existing [concentration and inference reference](financial-data-concentration-proof-and-alternatives.md) and technical models distinguish observed activity from identified stock. This assessment does not refresh the linked legal field map. Any phrase such as “wealth register light” should be explicitly defined as a potentially linkable longitudinal financial-activity profile—not a demonstrated complete register of current net assets.

Retention also needs precise arithmetic. If a legal scheme requires each annual cohort to be kept for a fixed period, effective deletion can produce a rolling window rather than unlimited lawful accumulation. The applicable start/end rules, exceptions and copy-specific implementation must be verified. Continued new reporting, independently retained records and copies already stolen are separate reasons information may persist; they must not be collapsed into an invented perpetual statutory retention rule.

## 4. Blockchain anchors can extend observation beyond the original record

An annual aggregate is not an address, transaction identifier, wallet descriptor or viewing key. A matching method cannot silently borrow stronger provider-held anchors and attribute its success to the aggregate alone.

Where an actual record supplies a reliable identity-to-ledger anchor, historical public data may become interpretable and later public activity may be observable without another provider query. But the scope is conditional. One Bitcoin address does not reveal every future fresh address; a descriptor or derivation scope is different. Account-contract activity, pooled custody, off-chain systems and privacy protocols expose different information. A historical association can also become stale.

The [Bitcoin](bitcoin-utxo-observation-and-attribution.md), [account/contract](account-contract-chain-data-evidence.md) and [off-chain/privacy](offchain-private-ledger-observation-limits.md) references explain those protocol boundaries. This is why deleting an origin record cannot retract a stolen anchor or erase a public chain, while still being capable of reducing future provider-side exposure.

An examiner must separately establish a transaction candidate, address/cluster, entity, natural person, control at a specified time and beneficial ownership. A service label or historical signing ability is not a complete financial inventory. The [existing evidence protocol](dac8-blockchain-linkage-expert-evidence-protocol.md) supplies negative controls and measured attribution endpoints; it remains the proper place for a reproducible linkage experiment.

## 5. Harm is a branching process with feedback

One digital fraud path is extraction → selection/contact → engagement → disclosure or approval → transfer → unrecovered loss. Other paths differ: an insider may directly enable account misuse; genuine-session manipulation may require no stolen login; physical coercion may bypass the digital-disclosure stage. Repeat approaches add feedback and time dependence.

For a single precisely defined path, the chain rule can express conditional probabilities without assuming independence. It does not provide their values. Coefficients from unrelated Gmail, university, workplace and mail-fraud samples cannot populate one purported Austrian loss model. Multiple attempts against the same person must not be assumed independent.

Likewise, `1-(1-p)^n` estimates at least one breach only under specified identical, independent probabilities. Shared vendors, credentials and infrastructure create dependence; different controls create heterogeneity. Counting copies or providers is therefore not enough to calculate risk. The relevant scenario asks which compromise exposes which population and field combinations, including common-mode failure.

Severity, uncertainty and feasibility should be reported separately. Official physical-harm observations warrant inclusion in severity scenarios; they do not supply a person-level Austrian probability. A zero immediate-loss count does not prove a zero residual targeting risk, and an absence of follow-up does not prove later harm.

## 6. Authentication, recovery, intention and confidentiality are separate

[NIST SP800-63B-4](../../raw/articles/2026-10-17-scam-nist-authentication-recovery.md) distinguishes verifier-bound phishing resistance from manually entered OTPs and specifies separate recovery processes. [SP800-63A-4](../../raw/articles/2026-10-17-scam-nist-proofing-privacy.md) does not permit static knowledge as identity verification and requires attention to privacy, fraud effectiveness and redress within its scope. These are technical benchmarks, not automatic Austrian legal obligations.

The four questions are: who controls the authenticator; who can replace it; what action is actually being approved; and who can read/export customer records? A positive answer to the first does not settle the others. Correct personal details are evidence about attributes, not necessarily the current presenter.

Encryption at rest can protect lost storage while an authorised application session displays decrypted data. Phishing-resistant login can stop a verifier-impersonation route while a genuine user still follows deceptive instructions. Independent notification may help detect a recovery change but does not itself reverse a completed loss. Each control must be attached to its threat and tested there.

## 7. Empirical evidence does not make safeguards futile

The [EBA/ECB report](../../raw/articles/2026-10-17-scam-eba-ecb-payment-fraud-2025.md) supports SCA benefits for card fraud and documents substantial payer manipulation. Higher observed fraud for SCA credit transfers likely reflects higher-risk/value transaction selection; it is not a causal comparison or evidence that authentication causes fraud. Successful authentication must not automatically become a conclusion that a transfer was legally authorised.

Its loss-allocation figures also qualify a simplistic bank/crypto contrast: users bore about 85% of reported EEA credit-transfer losses in 2024, but approximately 59% in Austria, with providers about 40%. This is observed allocation, not an individual liability rule or the leaked-data share. The [controlling supplement](../../raw/articles/2026-10-17-scam-eba-loss-allocation-supplement.md) notes that insurance refunds are excluded, so these shares are not ultimate net household burden after insurance. Custody, self-custody, payment type and actual recovery possibilities must remain distinct.

The [EDPB breach examples](../../raw/articles/2026-10-17-scam-edpb-breach-examples.md) similarly distinguish exposure without observed transfers, static-information billing redirection and compromised genuine mailboxes. They support different safeguards and notification analysis, not an assertion that every exposed person suffered theft. Prevention can work; its residual boundaries still matter.

## 8. Mandatory preservation is not unchanged operational availability

The technical question is not only how long a record must exist. It is whether ordinary support, marketing, contractor or analytical systems must retain the same ability to access it throughout that period. Separate legal duties may justify preserving data while narrower archives reduce unnecessary availability. Whether a particular archive meets those duties requires evidence.

[NIST SP800-88r2](../../raw/articles/2026-10-17-scam-nist-sanitisation-validation.md) distinguishes sanitisation verification from adequacy validation. It is not a row-deletion standard, but its key/history and copy limitations expose why “we deleted it” or “the key was destroyed” can be overbroad. Testing should cover exports, subprocessors, backups, restoration and lawful holds, not just the current database.

Evidence of effective origin deletion is valuable even though it cannot recall a stolen copy. Those are complementary conclusions. Deletion, archive restriction, account recovery and withdrawal of a ledger association solve different problems; no single retention number measures all of them.

## 9. Concentration has benefits and costs; neither is self-proving

Shared data may improve detection, consistency and cross-provider investigations. Fragmented systems can duplicate errors, impede correction and hide patterns. Centralisation may permit stronger specialist controls than many weak local systems. These are legitimate candidate benefits, not verified facts about the current Austrian design.

There is also unusually direct primary authority for testing the concentration cost: [EDPB Statement2/2024](../../raw/articles/2026-10-17-scam-edpb-financial-centralisation.md) identifies greater interference and breach risk in the then-proposed central antifraud platform compared with distributed PSP processing. It calls for demonstrated necessity and proportionality.

That nonbinding proposal-stage position is not a DAC8 judgment or proof of equal distributed utility. Its useful lesson is methodological: the claim that more shared data prevents fraud cannot itself settle whether the proposed categories, joins, access and retention are necessary. A privacy-preserving design can also leak through queries, metadata or outputs; a cryptographic label is not an evaluation.

## 10. Compare defined architectures under the same legitimate workload

| Candidate change | Intended reduction | Residual risk or cost to test |
|---|---|---|
| Field/role separation | Fewer identities reachable with address plus financial context | Join privileges, administrator collusion and extra retrieval steps |
| Case-bound access and export approval | Less unattended bulk retrieval | Slow leakage, approval quality and investigation latency |
| Restricted statutory archive | Less routine exposure while preserving required records | Retrieval completeness, availability and exception handling |
| Shorter unnecessary supplier retention | Fewer historical operational copies | Restoration, subprocessor evidence and legal holds |
| Verifier-bound login plus robust recovery | Fewer credential/recovery impersonation paths | Genuine-user manipulation, exclusion and recovery burden |
| Independently verified high-risk changes | Less reliance on a compromised message or static data | Correlated channels, delays and legitimate-user rejection |
| Distributed or privacy-preserving analysis | Less raw central concentration | Utility loss, output leakage, correction and operational cost |

These are candidates, not findings that Austria lacks them or that they all satisfy the law. The assessment should include the existing design as a baseline, not construct a deliberately weak central system for comparison. Cost, availability, accessibility and tax/compliance utility belong beside privacy/security gains.

For each architecture, execute the same authorised tasks with documented data coverage and error conditions. Measure completeness, correction propagation, false associations, analyst effort, latency and service failure. Separately measure people/fields reachable per role, export volume, detection delay and restored-copy persistence. Equal archive retrieval for one task is not equal tax-enforcement utility overall.

## 11. Establish the marginal DAC8 contribution

The counterfactual is not a world without financial records. Applicable AML, transfer, service and accounting obligations may require some of the same provider data independently. A successful challenge to one rule would not automatically erase those records or stolen copies.

The relevant comparison asks which fields, reports, joins, copies, access purposes and retention periods the challenged requirement adds or changes. Aggregate impact can include concentration across providers, but an expert must identify actual exchange and access structures rather than assume one universal database.

This also separates three propositions: lawful state profiling may itself interfere with privacy; security failures may enable criminal use; a particular claimant may suffer damage. They have overlapping facts but different proof requirements. A technical opinion should illuminate those facts without deciding legal validity by assertion.

## 12. Prevention and compensation have different proof gates

The targeted [Scalable Capital holding](../../raw/articles/2026-10-17-scam-cjeu-scalable-identity-theft.md) distinguishes data theft from actual identity misuse while preserving compensation for other proven damage. The [Quirin supplement](../../raw/articles/2026-10-17-scam-cjeu-quirin-fear-supplement.md) recognises proven negative feelings tied to unlawful disclosure; it does not dispense with infringement, damage and causation. Neither makes actual financial theft the only relevant harm.

Conversely, an abstract risk does not establish an individual damages claim. Preventive processing/security assessment should not be postponed until a claimant has suffered completed fraud. Nor does its availability imply an automatic free-standing injunction: Quirin expressly limits the particular preventive merits remedy, leaves national remedies possible and distinguishes interim measures. The [threshold reference](data-risk-prevention-and-damages-thresholds.md) preserves these boundaries; Austrian standing and later procedural developments were not refreshed here.

## 13. Deliverables for an independent expert

The commission should be capable of producing findings adverse to the initial hypothesis. Required outputs are:

- a field-and-copy inventory, mapping each purpose/legal basis separately from actual technical availability;
- a role/join/export matrix tested with controlled identities, including contractors and restored archives;
- a longitudinal inference test that reports missing coverage, double counting, uncertainty and counterexamples rather than summing flows;
- a blockchain ablation test separating annual aggregates from stronger anchors and person attribution from ownership;
- a harm-evidence ledger with event deduplication, acquisition provenance, failed attempts, recoveries and competing explanations;
- matched-workload alternative results, including costs, false positives, exclusion, latency and utility;
- a reproducibility package containing synthetic examples, frozen versions and parameters, with independent rerun and protected personal evidence kept out of public artifacts.

Actual incidents should be reconstructed from lawfully available notifications, messages, logs and case records; no leaked dataset needs to be purchased or exposed. Where evidence is unavailable, report the missing fact and sensitivity of the conclusion. Lack of public architecture detail is not itself evidence of a defective control.

## 14. Joint availability can add information and propagate mistakes

The [[financial-data-composition-and-attribution-error|composition reference]] ([composition reference](financial-data-composition-and-attribution-error.md)) distinguishes direct enrichment, candidate intersection, reconstruction and attribute inference. Routine reports already identify their subjects; adding another provider or year can enrich that identity without any de-anonymisation attack.

A unique-looking candidate does not establish the true match. The target may be absent, the period wrong, or the source identifier misassigned. Persistent keys can propagate mistakes into later profiles and inferred holdings. These errors can coexist with genuine information gain; they are not reasons to assume harmlessness.

Experiments demonstrate both sides. Complementary releases can expose sensitive attributes under explicit overlap assumptions; reconstruction metrics may be weaker than a baseline overall but stronger for a narrow subgroup. Neither an impressive singleton rate nor a reassuring population average settles the claimant's result. Controlled absence, wrong-overlap and baseline tests are necessary.

The same distinction applies to the threat model: criminals can act on uncertain or false beliefs, while the expert must still prove the accuracy of their own attribution. A plausible target-selection profile and a reliable wealth measurement are different objects.

## 15. Privacy technologies must protect the relevant boundary

Removing names, restricting logins, encrypting storage and limiting released information address different threats. A token can reduce exposure if the mapping and useful auxiliary information are genuinely separated. A common usable linkage key can instead preserve joinability. The precise construction and actor capability matter.

[NIST188](../../raw/papers/2026-10-17-depth-nist-deidentification.md) distinguishes access, information content and disassociability and requires evaluation of repeated outputs. Protected query systems can reduce raw exports but still reveal information through their answers.

[NIST226](../../raw/papers/2026-10-17-depth-nist-dp-trust-boundary.md) makes a critical boundary explicit: central differential privacy protects specified outputs while trusting the holder of raw data. It is not a defence against compromise of that raw-data holder. Event-level or annual guarantees also do not automatically provide equivalent protection for a person's accumulated history; releases need the appropriate privacy unit and composition accounting.

These are not objections to using effective privacy technology. They prevent a mismatched guarantee from becoming reassurance about another threat. Noisy research statistics cannot simply replace exact named tax records; exact access, distributed computation, restricted archives and protected statistical outputs need separate matched-task evaluations.

## 16. Test capabilities across provider and lifecycle boundaries

The [[provider-control-boundaries-and-observed-failures|provider-control reference]] ([provider-control reference](provider-control-boundaries-and-observed-failures.md)) adds actual prevention and concrete boundary failures: restricted banking warehouses feeding ordinary shared exports, reporting applications with broader effective reach than intended entitlements, and historical copies outside current encryption coverage. Nominal role separation is therefore a starting hypothesis to test, not a completed assurance.

Define reachable combinations per role, time, population and field bundle. Then repeat the test after reporting/export, role change, archiving, restoration, supplier handoff and recovery exceptions. Distinguish prevention, detection, response timing and information already exposed. The counterfactual must preserve legitimate workload and exception handling, not merely remove access.

The additional [criminal case analysis](criminal-data-markets-and-repeat-victimisation.md) also separates target discovery from intermediate capabilities such as changing a communication channel, obtaining later account context and making further demands. For several of these additional cases, the source does not specify the original target-acquisition route. The supported transfer is to examine the relevant field's contribution to a specified stage, not to claim that every attack originated in a financial leak.

A reliable assessment should be able to conclude either that a proposed narrower design measurably reduces unnecessary reach with acceptable utility, or that an alleged alternative fails an identified legitimate task. Both outcomes are useful evidence.

## 17. Overall assessment

The sources support treating identifying financial data as potentially durable selection and credibility material, including at providers and contractors. They support analysing repeated reporting, usable joins and stolen ledger anchors separately from immediate account compromise. They also support effective safeguards and show why richer data, actual harm and legal remedies must not be assumed.

The most defensible conclusion is conditional but substantial: if a design exposes unnecessary combinations or broader populations than its demonstrated legitimate tasks require, it can create avoidable targeting opportunity and consequence. Whether the Austrian implementation does so, how large its incremental effect is, and which alternative preserves comparable utility remain empirical questions. A serious opinion should specify exactly how those questions will be answered.

## See Also

- [[privacy-financial-privacy-and-surveillance|Privacy, Financial Privacy and Surveillance]] ([Privacy, Financial Privacy and Surveillance](../topics/privacy-financial-privacy-and-surveillance.md)) — public-interest arguments remain separate from system-specific proof.
- [[financial-data-composition-and-attribution-error|Financial-Data Composition and Attribution Error]] ([Financial-Data Composition and Attribution Error](financial-data-composition-and-attribution-error.md)) — direct enrichment, reconstruction, wrong links and protection boundaries.
- [[provider-control-boundaries-and-observed-failures|Provider Control Boundaries and Observed Failures]] ([Provider Control Boundaries and Observed Failures](provider-control-boundaries-and-observed-failures.md)) — actual prevention, boundary failures and effective-reach tests.
- [[criminal-data-markets-and-repeat-victimisation|Criminal Data Markets and Repeat Victimisation]] ([Criminal Data Markets and Repeat Victimisation](criminal-data-markets-and-repeat-victimisation.md)) — exploitation economics and admitted feedback.
- [[phishing-causal-evidence-and-measurement|Phishing, Repeat Harm and Causal Measurement]] ([Phishing, Repeat Harm and Causal Measurement](phishing-causal-evidence-and-measurement.md)) — experiments, targeting associations and outcome denominators.
- [[leaked-data-scams-and-targeted-attacks|Leaked Data, Financial Scams and Targeted Attacks]] ([Leaked Data, Financial Scams and Targeted Attacks](leaked-data-scams-and-targeted-attacks.md)) — provider incidents, physical harm and source attribution.
- [[financial-data-concentration-proof-and-alternatives|Financial data concentration evidence and alternative processing designs]] ([Financial data concentration evidence and alternative processing designs](financial-data-concentration-proof-and-alternatives.md)) — existing Austrian fusion evidence and bounded utility comparisons.
- [[data-risk-prevention-and-damages-thresholds|Data-Risk Prevention and Damages Thresholds]] ([Data-Risk Prevention and Damages Thresholds](data-risk-prevention-and-damages-thresholds.md)) — targeted holdings and procedural limits.

## Sources

Immutable records in the frontmatter supply the newly checked technical and judicial sources. Linked protocol/field-map references retain their individual verification scopes. This assessment contains no production configuration, real victim dataset or measured Austrian person-level attack rate.
