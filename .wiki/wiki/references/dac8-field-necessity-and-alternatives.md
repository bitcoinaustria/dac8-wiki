---
title: "DAC8 Field Necessity and Less-Intrusive Alternatives"
category: reference
sources:
  - raw/articles/2026-08-27-eu-directive-2023-2226-dac8.md
  - raw/articles/2026-08-30-dac8-impact-assessment-evidence-and-options.md
  - raw/articles/2026-08-27-cjeu-c175-20-sia-ss-tax-data.md
  - raw/articles/2026-08-27-cjeu-c-623-22-dac6.md
  - raw/articles/2026-08-30-cjeu-c394-23-mousse-data-minimisation.md
  - raw/articles/2026-08-30-cjeu-c484-24-nth-haustechnik.md
  - raw/articles/2026-08-27-cjeu-c37-c601-20-aml-register.md
  - raw/articles/2026-08-27-eca-special-report-03-2021.md
  - raw/articles/2026-08-27-commission-dac-evaluation-2025.md
  - raw/articles/2026-09-04-ireland-dac8-si-584-2025-retention-copy.md
  - raw/articles/2026-09-04-netherlands-dac8-decision-records-retention.md
  - raw/articles/2026-09-04-france-dac8-prefiling-copy-and-records.md
  - raw/articles/2026-09-04-eu-dac8-xml-correction-deletion.md
  - raw/articles/2026-09-04-austria-krypto-mpfg-legislative-materials-audit.md
  - raw/articles/2026-09-04-cjeu-ligue-bulk-profiling-safeguards.md
  - raw/articles/2026-09-04-ecthr-s-marper-data-lifecycle-effectiveness.md
  - raw/articles/2026-09-04-commission-dac-evaluation-2025-detail.md
created: 2026-08-30
updated: 2026-09-30
tags: [dac8, data-minimisation, strict-necessity, reporting-fields, alternatives, proportionality]
aliases: [DAC8 field necessity, DAC8 less intrusive alternatives]
confidence: high
volatility: warm
verified: 2026-09-04
summary: "Field-level necessity matrix separating strong tax identifiers and event fields from transfer and external-address fields that require a more specific incremental justification."
---

# DAC8 Field Necessity and Less-Intrusive Alternatives

> The strongest EU-law argument is substantive field-level necessity, not a claimed duty to publish a separate legislative proof for every field. DAC8's identity-linked annual dataset must be necessary as designed, while CJEU C-623/22 shows that the Court may uphold a reporting package collectively.

## Legal test and adverse law

CJEU C-175/20, paragraphs 63–84, requires specific purposes, objective limits, strict necessity and exclusion of data not needed for the tax task. C-394/23, paragraphs 22–29, 36–43 and 51–56, tests whether a neutral, less intrusive alternative is equally effective, but arose from consumer-contract processing and is only analogous here. C-484/24, paragraphs 94–103 and 116, places the complete suitability, necessity and balancing inquiry on the legislative legal basis; by analogy, its court-specific holding cautions against demanding that every later CASP or authority operation repeat the complete Charter balance.

C-623/22, paragraphs 143–149, is the principal counterauthority. The Court reviewed the DAC6 information package as a whole and upheld it without requiring a separately published empirical demonstration for each element. The usable distinction is structural: paragraph 147 describes DAC6 as early and targeted information about hallmarked cross-border arrangements presenting a potential tax-avoidance risk. DAC8 reports annually for every reportable user with reportable activity, without a comparable hallmark or individual-risk trigger.

## Judicial calibration of evidence

EU and Convention law do not establish a categorical requirement for a separately published empirical study of every reporting field. Suitability may be accepted where a measure plausibly contributes to the objective even when evasion, false positives or incomplete causal evidence remain. *Digital Rights Ireland*, paragraphs 49–50, *Ligue des droits humains*, paragraphs 106 and 123–124, and *S. and Marper*, paragraphs 115–117, illustrate different parts of that limit.

The stronger necessity inquiry asks whether the exact field remains objectively connected to the tax task, whether an equally effective less intrusive design can be established, whether the legislature genuinely considered the affected rights and alternatives, and whether operational safeguards match the field's inference and misuse risk. Missing public field evidence opens that inquiry; it does not prove ineffectiveness or invalidity.

The Austrian explanatory materials give specific reasons for some identity, source, asset-name and valuation elements but do not separately analyse section 18(1)(3)(c) to (i). That silence is narrower than an absence of EU reasoning: DAC8 recitals and the impact assessment support the package collectively. The evidentiary task is therefore to connect the unexplained marginal field to a measurable added interference and a tested narrower comparator.

## Field matrix

| Field group | Direct tax or administration use | Necessity pressure | Credible narrower comparator | State answer |
|---|---|---|---|---|
| Name, address, residence, TIN, date and place of birth | Identity matching and allocation to the competent state | Low. Core identifiers are difficult to replace. Date and place of birth may deserve separate examination where stronger identifiers are available. | Article 8ad(3)(a) already substitutes name, Identification Service identifier and issuing state for the ordinary identity set in the specified identification-service case; test whether that enacted limitation can apply. | The substitution is confined to confirmation through a qualifying Member-State or Union service; other cross-border matching still needs stable identifiers. |
| Fiat acquisitions and disposals: value, units and count | Gross acquisition and disposal activity; plausibility and basis follow-up | Low to medium. Fiat disposals are directly relevant; acquisitions support basis and completeness checks. | Values first; units or counts only where they measurably improve matching or risk selection. | Units and counts detect implausible values, fragmentation and classification errors. |
| Crypto-to-crypto acquisitions and disposals | Risk selection and possible taxable-event analysis depending on national law | Medium. Tax treatment differs and the report cannot pair the two sides without dates or transaction IDs. | Value aggregates followed by targeted ledger requests where a jurisdiction treats the exchange as relevant. | The same data must serve several Member States and permit cross-provider completeness checks. |
| Retail payments above USD 50,000 | Identifies high-value use for goods or services | Medium. The field has a specific threshold but reports no merchant, purpose or date. | Higher or graduated thresholds; value-only reporting; targeted follow-up. | High-value spending can reveal undeclared disposals and the threshold already limits collection. |
| Incoming and outgoing transfers: value, units, count and known type | Reconciliation, hidden-disposal detection and movement between or outside reporting providers | High. A transfer is not necessarily a taxable event; categories can include own-wallet movements, collateral, loans and unknown uses. | Aggregate value only; tax-event categories first; additional fields after an objective mismatch or risk trigger. | Transfers are necessary to avoid mistaking disappearance from one provider for non-taxable inactivity and to reconcile fragmented crypto activity. |
| Transfers to DLT addresses not known by the provider to be associated with a VASP or financial institution: value and units | Identifies annual outward value and units meeting that provider-knowledge test | Highest. The trigger is the provider's lack of knowledge, not a tax consequence. The field contains no address or transaction count and does not prove that no intermediary exists. | Omit the routine aggregate; request provider-held transfer details only after a documented discrepancy or risk indicator. | The field marks where automatic intermediary reporting may lose visibility; a coarse aggregate is less intrusive than transmitting addresses or individual transactions. |

## What the impact assessment proves and does not prove

The Commission considered balance-only, highly aggregated, transaction-by-transaction and hybrid models. It selected the hybrid as more useful for risk selection and less burdensome than transaction-by-transaction reporting. That deliberate middle ground is material State evidence.

The assessment also records substantial uncertainty: the crypto tax gap was difficult to quantify, modelled revenue relied on assumptions, peer-to-peer displacement was acknowledged, and benefits depended on Member-State use. It labels the chosen data the minimum required but contains no independent ablation study showing the incremental detection value of each unit, count, transfer-type or external-address aggregate. The correct proposition is therefore **uncertain field-specific incremental necessity**, not absence of any legislative evidence.

## Alternatives by evidentiary maturity

| Alternative | Status | Litigation use |
|---|---|---|
| Transaction-by-transaction reporting | Considered and rejected as more burdensome | Supports the State: DAC8 is not the most intrusive available design. |
| Balance-only or coarser aggregate reporting | Considered and rejected as less useful for frequent trading and likely to cause follow-up requests | Provides a real comparator, but equal effectiveness must be proved rather than assumed. |
| Report tax-event/value fields routinely; obtain transfer detail after an objective mismatch | Legally and technically plausible; not proved equally effective | Best candidate for an expert or authority-data comparison. |
| Apply a threshold beyond the retail-payment field | Plausible but vulnerable to fragmentation and boundary avoidance | Requires distributional and evasion testing. No-threshold invalidity by itself is weak. |
| Determine residence/reportability first and materialise the complete section 18 annual aggregate profile only for reportable users | Directly relevant to Austria's section 20(1) excess | Strong for a genuinely non-reportable claimant; does not reduce the EU dataset for an Austrian reportable user. |
| Retain provider reporting records for six or seven years instead of ten | Enacted in Ireland and the Netherlands within DAC8's permitted range | Concrete alternative to Austria's maximum period; equal effectiveness must be tested against Austrian audit and limitation rules. |
| Provide the user with the concrete information before filing | Enacted in France | Demonstrates a practicable accuracy safeguard; does not establish a veto or automatic suspension. |
| Reuse compliant CRS due diligence and existing tax self-certification | Enacted in Germany, France and the Netherlands | Reduces duplicate collection, not the final reportable dataset. |
| Propagate an established correction or deletion through typed exchange messages | Built into the binding EU XML format | Supports a traceable downstream remedy; technical capability is not a substantive right to deletion. |
| Privacy-enhancing matching or zero-knowledge designs | Research concept, not a proven equivalent | Do not present as an available equally effective substitute without a working comparison. |

The Identification Service option is the strongest enacted proof that the ordinary identity bundle is not invariably required. Where the statutory conditions are met, Article 8ad(3)(a) allows name, the service identifier and issuing Member State to replace address, residence TIN and birth data. This is a defined limitation, not a complete alternative to DAC8 reporting. Its practical value remains an open implementation fact: whether Austria provides a qualifying service, which providers can use it and how multiple tax residences are handled must be verified before relying on it for a claimant.

The USD 50,000 retail-payment threshold is not a general de-minimis exclusion. A lower-value movement may still fall within another reportable transfer category. It should not be presented as proof that DAC8 already exempts small users or small transactions generally.

## Proof that would materially improve the claim

1. Map each field to the Austrian tax rule and actual BMF risk or assessment task.
2. Obtain the field definitions, validation rules and correction behaviour used in the Austrian transmission schema.
3. Run a field-ablation test: compare detection and false-positive performance with and without units, counts, transfer types and the external-address aggregate.
4. Test tax-event-only, value-only, thresholded and risk-triggered designs against the same cases and evasion scenarios.
5. Separate revenue recovered because of DAC8 from audits that would have occurred using returns, DAC2, AML or provider records.
6. Record administrative cost and additional follow-up under every comparator.
7. Record actual error and correction rates for each challenged field and the share of signals leading to a new audit, correction or additional tax.
8. Separate those outcomes from cases that would already have been identified through returns, DAC2, AML or provider records.
9. Document human review, purpose logs and independent audit for any automated selection or matching process.

Until the first DAC8 exchange by September 2027, DAC8-specific outcome evidence is necessarily ex ante. Earlier DAC evaluations and audit reports can inform design risk but do not prove or disprove DAC8's field-level effect.

The European Court of Auditors' 2021 report criticised data quality, use and monitoring in older DAC instruments but also recommended extending mandatory exchange to crypto-assets. The Commission's 2025 evaluation excludes DAC8 because its first exchange had not occurred; it reports improved DAC2 matching and an overall positive DAC1/DAC2 assessment while still noting uneven use and weak causal attribution of revenue. Both sources are mixed context, not DAC8 outcome evidence.

## Pleading boundary

- Do not claim that EU law requires a separate legislative memorandum for each field.
- Do not transpose C-175/20's controller accountability rule into a categorical burden on the EU legislature to prove each field separately.
- Do not claim that non-taxable transfers are irrelevant to tax risk selection.
- Do not equate usefulness, administrative convenience or fewer follow-up requests with strict necessity without examining alternatives.
- Do not import public-register, communications-retention or PNR outcomes as controlling tax-reporting rules.
- Frame the requested result narrowly: removal, conditioning or stricter use of a specific field can succeed without invalidating the complete DAC8 system.

## See Also

- [Financial-data concentration proof and alternatives](financial-data-concentration-proof-and-alternatives.md) — actual archive/PET comparators, adverse utility findings and the remaining equality-of-benefit test.

- [[dac8-inference-linkage-and-error-evidence|DAC8 Inference, Linkage and Error Evidence]] ([DAC8 Inference, Linkage and Error Evidence](dac8-inference-linkage-and-error-evidence.md))
- [[dac8-data-lifecycle-access-retention-remedies|DAC8 Data Lifecycle: Access, Retention and Remedies]] ([DAC8 Data Lifecycle: Access, Retention and Remedies](dac8-data-lifecycle-access-retention-remedies.md))
- [[dac8-vs-dac2-distinguishing-arguments|DAC8 versus DAC2: Distinguishing Arguments]] ([DAC8 versus DAC2: Distinguishing Arguments](dac8-vs-dac2-distinguishing-arguments.md))
- [[dac8-member-state-implementation-comparators|DAC8 Member-State Implementation Comparators]] ([DAC8 Member-State Implementation Comparators](dac8-member-state-implementation-comparators.md))
- [[dac8-bulk-data-case-transfer-matrix|DAC8 Bulk-Data Case Transfer Matrix]] ([DAC8 Bulk-Data Case Transfer Matrix](dac8-bulk-data-case-transfer-matrix.md))
- [[dac8-aeoi-effectiveness-and-evidence-limits|DAC8, AEOI Effectiveness and Evidence Limits]] ([DAC8, AEOI Effectiveness and Evidence Limits](dac8-aeoi-effectiveness-and-evidence-limits.md))

## Sources

- [Directive (EU) 2023/2226 (DAC8)](../../../legal-docs/core/eu-dac8-directive-2023-2226.pdf)
- [Commission impact assessment SWD(2022) 401](../../../legal-docs/supporting/eu-swd-2022-401-dac8-impact-assessment.pdf)
- [CJEU C-175/20](../../../legal-docs/supporting/eu-cjeu-c175-20-valsts-ienemumu-dienests.pdf)
- [CJEU C-623/22](../../../legal-docs/core/eu-cjeu-c623-22-belgian-tax-lawyers.pdf)
- [CJEU C-394/23](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62023CJ0394)
- [CJEU C-484/24](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62024CJ0484)
- [Ireland SI 584/2025](../../raw/articles/2026-09-04-ireland-dac8-si-584-2025-retention-copy.md)
- [Netherlands implementing decision](../../raw/articles/2026-09-04-netherlands-dac8-decision-records-retention.md)
- [France pre-filing copy](../../raw/articles/2026-09-04-france-dac8-prefiling-copy-and-records.md)
- [EU XML correction and deletion](../../raw/articles/2026-09-04-eu-dac8-xml-correction-deletion.md)
- [Austrian legislative-materials audit](../../raw/articles/2026-09-04-austria-krypto-mpfg-legislative-materials-audit.md)
- [CJEU Ligue des droits humains](../../raw/articles/2026-09-04-cjeu-ligue-bulk-profiling-safeguards.md)
- [ECtHR S and Marper](../../raw/articles/2026-09-04-ecthr-s-marper-data-lifecycle-effectiveness.md)
- [Commission DAC evaluation detailed extraction](../../raw/articles/2026-09-04-commission-dac-evaluation-2025-detail.md)
