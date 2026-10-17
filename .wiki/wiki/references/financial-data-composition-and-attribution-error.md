---
title: "Financial-Data Composition and Attribution Error"
category: reference
sources:
  - raw/papers/2026-10-17-depth-composition-ganta.md
  - raw/papers/2026-10-17-depth-netflix-record-linkage.md
  - raw/papers/2026-10-17-depth-census-reconstruction.md
  - raw/papers/2026-10-17-depth-linkage-quality-ons.md
  - raw/papers/2026-10-17-depth-bloom-filter-cryptanalysis.md
  - raw/papers/2026-10-17-depth-hospital-linkage-errors.md
  - raw/papers/2026-10-17-depth-nist-deidentification.md
  - raw/papers/2026-10-17-depth-nist-dp-trust-boundary.md
  - raw/articles/2026-09-19-cjeu-c413-23p-identifiability.md
created: 2026-10-17
updated: 2026-10-17
verified: 2026-10-17
verification_scope: "New methods, experiments and NIST guidance checked. The separately linked C-413/23 P digest retains its September 19 legal verification; no Austrian production system or real-person data was tested."
volatility: warm
confidence: medium
tags: [financial-data, composition, record-linkage, error, privacy-guarantees, expert-evidence]
aliases: [Cumulative disclosure risk, Join quality and false attribution]
summary: "Joint processing can add information without proving correct identity or wealth; experiments, protection boundaries and falsification tests define the distinction."
---

# Financial-Data Composition and Attribution Error

Disclosure risk is a property of information available together to a specified actor, not merely a property of each field in isolation. Complementary records can narrow uncertainty, attach attributes or expose a relationship. They can also create persistent false associations. Both results matter to a financial-data assessment.

The question is not whether all financial data are re-identifiable. Routine DAC8 reports already identify their subjects. The relevant questions are what additional information a join exposes, how reliably it belongs to that person, and whether the actor can actually obtain the inputs.

## Identity enrichment is not de-anonymisation

A valid identifier can attach another provider, year or category of activity to an already named person. This may reveal a cross-provider relationship that neither provider sees alone. No name-removal attack is required. The hard factual questions are identifier quality, coverage, actual access and the new attributes produced.

A different operation starts with a pseudonymous chain address or record and tries to associate it with a person. That requires a discriminating anchor and validation. A third operation predicts a trait or wealth category. Success at one does not establish success at the others.

Nor does a stable identifier cure a wrong initial assignment. Source provenance, correction history and temporal scope must travel with derived records. “These rows share a key” establishes a database relation; “these assets beneficially belong to this person now” needs additional evidence.

## Four mechanisms require different evidence

| Mechanism | Input and possible gain | Necessary limiting test |
|---|---|---|
| Direct enrichment | Existing identity plus another keyed record adds fields or relationships | Identifier correctness, lawful availability and time compatibility |
| Candidate intersection | Joint constraints remove alternatives left by separate views | True target present and retained; incompatible inputs do not force a match |
| Reconstruction | Many complementary summaries constrain underlying records | Actual published constraints, multiple valid solutions and reconstruction endpoint |
| Attribute inference | A link or model supplies an additional characteristic | Attribute correctness, baseline performance and uncertainty |

These mechanisms need not occur in sequence. An identified report can be enriched without reconstructing transactions. A reconstructed feature bundle can be correct without establishing a unique original row. An attribute can be inferred correctly from common background information without the challenged dataset contributing anything.

The ONS methodology makes a useful vocabulary distinction: a **match** is the true relationship, a **link** the assigned classification, and **agreement** observed similarity. Confusing the three makes a confident output look like ground truth.

## What controlled composition experiments establish

[Ganta et al.](../../raw/papers/2026-10-17-depth-composition-ganta.md) experimentally intersect sensitive-value sets from independently anonymised overlapping releases. In the stated small-group condition, singleton results differed markedly between the Adult and IPUMS datasets. This establishes a concrete composition mechanism, not a universal success rate.

The decisive assumption is being able to locate the target's correct group in both releases. Inverse candidate-set size is not an independently calibrated probability that the inferred attribute belongs to the correct person. Larger groups and additional releases also had qualified effects.

For financial records, membership and meaning cannot be assumed. A transfer category in one year and a purchase category in another are not observations of one invariant balance. Own-account movements, fees and provider classification can produce incompatible constraints. An experiment must preserve these counterexamples instead of selecting only tuples known to intersect successfully.

## Reconstruction and attribute correctness are not identity proof

The [Census experiment](../../raw/papers/2026-10-17-depth-census-reconstruction.md) uses 34 overlapping table sets and confidential validation. Its national commercial-auxiliary precision of 41.2% was below a 45.9% modal-guess baseline. Stronger excess inference appeared in specifically defined vulnerable subgroups; averaging would conceal both findings.

The approximately 95% result applies only to nonmodal people in zero-solution-variability blocks who are population-unique on block, sex and age bin. It must not be presented as a general re-identification rate. The study's “confirmed” endpoint concerns correctness of appended features under its validation procedure, not unrestricted forensic proof of every person's identity.

The 2020 protection comparison reduced tested excess inference. Thus the paper supports both complementary-summary risk and the efficacy of appropriately designed protection. Dense census tables do not prove reconstruction from annual crypto-asset totals. The relevant lesson is to test the actual constraints and subgroup baselines, not import an impressive percentage.

## Sparse linkage needs an honest no-match result

The [Netflix paper](../../raw/papers/2026-10-17-depth-netflix-record-linkage.md) distinguishes controlled recovery under stipulated auxiliary-rating knowledge from its much smaller external IMDb proof of concept. The latter had two strong links without an independent identity oracle. These are not the same validation endpoint.

Its methodological value includes abstention and a test that removes the true target before rerunning. A forced best match will always return someone, including when the correct person is absent. A large gap between first and second scores can still reflect an incomplete candidate population rather than correct attribution.

An Austrian linkage assessment should therefore report accepted, ambiguous and rejected results, with precision-versus-coverage curves. Correctness must be measured against independent evidence, not inferred from a matching score or from the examiner recognising the proposed answer.

## Persistent identifiers can preserve mistakes

The [hospital validation study](../../raw/papers/2026-10-17-depth-hospital-linkage-errors.md) found both false links and missed matches when a persistent-identifier algorithm was checked against separately maintained clinical identifiers. Its exact error rates belong to that selected clinical experiment, not financial systems. The general mechanism is that a durable key can propagate an earlier association error rather than correct it.

ONS also warns that reference standards can be imperfect and unrepresentative. Reviewing only accepted links may estimate precision while missing true matches buried among nonlinks. Human review cannot supply identifying information absent from the available evidence.

A financial test should inject known misassignments and follow their propagation through reports, clusters, risk categories and inferred holdings. Then correct the source and test whether every derivative updates. Retention of a false profile is a distinct potential harm from disclosure of an accurate one. Its frequency and consequence remain empirical questions.

## Encodings and privacy guarantees have boundaries

The [basic Bloom-filter experiment](../../raw/papers/2026-10-17-depth-bloom-filter-cryptanalysis.md) recovered selected surname encodings using background frequencies and knowledge of the construction, without its key. It is a counterexample to treating an encoding label as confidentiality—not proof that all modern linkage cryptography fails or that a surname identifies one person.

[NIST 188](../../raw/papers/2026-10-17-depth-nist-deidentification.md) asks where transformation occurs, whether originals/maps remain, what auxiliary data exist, and how repeated releases interact. A protected query enclave can constrain raw exports while its outputs still require disclosure analysis.

[NIST 226](../../raw/papers/2026-10-17-depth-nist-dp-trust-boundary.md) supplies a different protection model. Differential privacy bounds the incremental influence of a specified privacy unit on specified outputs. Event-level protection is not automatically whole-person or lifetime protection. Repeated releases require accounting. Central-model protection of released outputs does not protect raw records from a compromised trusted curator; a parallel exact release retains its own risk.

This does not make the technology futile. It identifies where the privacy barrier lies. Noisy research statistics, exact case-specific access and mandatory named reports are different products and must not be substituted without testing legitimate utility.

The existing [C-413/23 P digest](../../raw/articles/2026-09-19-cjeu-c413-23p-identifiability.md) similarly keeps recipient identification means distinct from collection-stage duties. It retains its September legal verification. The technical conclusion here is actor-relative capability, not a blanket legal anonymity declaration.

## Three synthetic counterexamples

The following stipulated examples were checked arithmetically. They illustrate logical mistakes; no rates were estimated from people or Austrian systems.

**A singleton can be wrong.** Source A leaves candidates {17, 42, 93}; source B leaves {42, 71}. Their intersection is {42}. If the true person is 17 and source B belongs to another period or omits that person, the singleton is false. More agreement under invalid membership assumptions can increase confidence without increasing truth. A validation sample containing only correctly overlapping records would hide this failure.

**High sensitivity and specificity need not give high precision.** In an imagined screen of 100,000 people for a defined property, stipulate 99% sensitivity and a 1% false-positive rate. If the property occurs in 0.1%, expected true positives are 99 and false positives 999: precision is about 9.02%. At 1% prevalence they are 990 and 990: precision 50%. At 10% prevalence they are 9,900 and 900: precision 91.67%. These are expectations, not observed outcomes.

The calculation is `sensitivity*p / (sensitivity*p + false_positive_rate*(1-p))`. It concerns a defined screening classification; it is not a measured financial-ownership classifier or a reason to assume real-world error independence.

**Annual privacy parameters do not reset lifetime disclosure.** In a hypothetical pure-DP design, ten releases each providing epsilon 0.1 for the same person's contribution admit a basic sequential-composition upper bound of epsilon 1, under consistent adjacency and standard sequential-composition conditions: each release must satisfy its guarantee even conditional on prior outputs. This is a bound, not exact realised privacy loss and not a 1% or 100% breach probability. A joint mechanism or allocation of one total budget may behave differently. Deleting an old input does not retract a released output already held by others.

None of these examples proves inevitable financial loss. Together they demonstrate why the expert must specify membership, base rates, time scope and the exact guarantee before attaching meaning to a small candidate set or reassuring parameter.

## A falsifiable evaluation protocol

The experiment should be fixed before examining the claimant's result:

1. **Freeze the actor and inputs.** Routine annual fields, provider records, contacts, labels and public chains are separate increments. Record acquisition, legal availability, date and transformations.
2. **Define endpoints.** Candidate reduction, accepted-link correctness, reconstructed-record uniqueness, newly attached attribute correctness, current control and beneficial ownership are separate outcomes.
3. **Test absent and partial overlap.** Include no true match, persons present in only one source, stale names/addresses, shared households and recycled contact information.
4. **Test financial incompatibilities.** Include batching, omnibus custody, internal trades, fees, round amounts, own transfers, changing classifications and missing opening holdings.
5. **Protect ground truth from contamination.** Do not validate a label using the same heuristic or source that generated it. Document reference uncertainty and blind adjudication where feasible.
6. **Use relevant baselines.** Compare each input alone, public/background inference and the joint system. Report difficult and nonmodal subgroups, not only overall averages.
7. **Expose abstention and calibration.** Show rejected and ambiguous cases, coverage/precision tradeoffs, false discovery and sensitivity to thresholds. A ranking score is not automatically a probability.
8. **Follow errors and corrections.** Inject a wrong association, trace propagation and test correction through copies and derived profiles.
9. **Separate passive and active capabilities.** Possessed-data analysis differs from asking a provider, eliciting a transaction or accessing a recovery channel. Each extra capability needs its own authorisation and evidence.
10. **Compare alternatives on the same legitimate tasks.** Measure exposure reduction alongside completeness, error, latency, cost and user burden.

A failure to find material incremental information is an admissible result. So is a result showing a narrow but serious outlier risk. The report should state which conclusions remain robust when auxiliary information is weaker or unavailable.

## Expert conclusion

The supported proposition is not universal de-anonymisation. It is that joint availability can expose relationships or attributes absent from separate views, while also creating wrong and persistent associations. Both additional information and error must be assessed at the actual field, actor, population and time scope.

For DAC8, already named annual reports make direct identity enrichment a distinct question from blockchain attribution. The latter cannot borrow undisclosed provider anchors or turn service-cluster labels into ownership. For security, a harmful target-selection belief need not be accurate; that fact does not lower the standard for the expert's own attribution claims.

This gives a concrete evidentiary commission: measure incremental information, verify accepted links against independent evidence, preserve no-match results, and test whether less intrusive access/output designs preserve comparable legitimate utility. It neither assumes an Austrian defect nor treats the absence of complete wealth reconstruction as proof of harmlessness.

## See Also

- [[financial-privacy-and-everyday-autonomy|Financial Privacy and Everyday Autonomy]] ([Financial Privacy and Everyday Autonomy](financial-privacy-and-everyday-autonomy.md)) — everyday consequences of linked and inferred financial profiles.
- [[financial-data-threat-model-and-control-evaluation|Financial-Data Threat Model and Control Evaluation]] ([Financial-Data Threat Model and Control Evaluation](financial-data-threat-model-and-control-evaluation.md)) — integrated provider/report/ledger threat boundaries.
- [[transaction-profiling-and-sensitive-inference|Profiling and Sensitive Inference from Transaction Records]] ([Profiling and Sensitive Inference from Transaction Records](transaction-profiling-and-sensitive-inference.md)) — existing item-level inference and legal limits.
- [[phishing-causal-evidence-and-measurement|Phishing, Repeat Harm and Causal Measurement]] ([Phishing, Repeat Harm and Causal Measurement](phishing-causal-evidence-and-measurement.md)) — harm endpoints and transportability.
- [[provider-control-boundaries-and-observed-failures|Provider Control Boundaries and Observed Failures]] ([Provider Control Boundaries and Observed Failures](provider-control-boundaries-and-observed-failures.md)) — how actual access and copies condition the available inputs.

## Sources

The frontmatter lists exact immutable records. They preserve original publications, experiment locators, auxiliary-data assumptions and limits. The synthetic examples above are stipulated arithmetic, not empirical sources or an Austrian risk estimate.
