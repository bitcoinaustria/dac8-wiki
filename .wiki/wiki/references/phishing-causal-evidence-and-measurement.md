---
title: "Phishing, Repeat Harm and Causal Measurement"
category: reference
sources:
  - raw/papers/2026-10-17-scam-gmail-breach-targeting.md
  - raw/papers/2026-10-17-scam-social-phishing-credentials.md
  - raw/papers/2026-10-17-scam-lain-longitudinal-controls.md
  - raw/papers/2026-10-17-scam-czybik-llm-denominators.md
  - raw/articles/2026-10-17-scam-nij-repeat-loss-records.md
  - raw/papers/2026-10-17-scam-deliema-vulnerability-not-wealth.md
  - raw/articles/2026-10-17-scam-gao-attribution-limits.md
  - raw/articles/2026-10-17-scam-empirical-precision-supplement.md
created: 2026-10-17
updated: 2026-10-17
verified: 2026-10-17
volatility: hot
confidence: medium
tags: [phishing, causality, targeting, repeated-exposure, measurement, adverse-evidence]
aliases: [Leak harm causal evidence, Phishing outcome denominators]
summary: "Observational targeting, contextual experiments, workplace controls and actual repeat payments support different links in the harm chain; none estimates Austrian DAC8 loss risk."
---

# Phishing, Repeat Harm and Causal Measurement

Three propositions need separate tests: whether information changes **who is approached**, whether it changes **what happens after an approach**, and whether it changes **financial or other harm**. Evidence for one is not automatically evidence for the others. The studies below make the general mechanism more concrete while exposing why a single purported “leak-to-loss multiplier” would be unsound.

## The studies answer different questions

| Study | Design and observed endpoint | Strongest usable conclusion | Boundary |
|---|---|---|---|
| Gmail, IMC2020 | Observational malicious-email receipt | Prior breached-address status associates with targeting | Not causal loss risk |
| Social Phishing, 2005 experiment | Contextual field comparison; valid credential authentication | Relevant relationship context can strongly affect disclosure | Not clearly randomized; early student setting |
| Lain, S&P2022 | Repeated workplace simulations with randomized controls | Exposure and control design matter across campaigns | One employer; no real loss |
| Czybik, USENIX2026 | University personalisation experiment; clicks | Public context can be exploited at scale | Allowlisted spam filtering, subgroup and arithmetic limits |
| NIJ2025 account | Linked completed payments from seized scam records | Repeat financial harm is concentrated and persistent | No nonpayer or failed-attempt denominator |
| DeLiema2025 | Cross-sectional survey of known-victim households | Vulnerability is not reducible to measured income category | Selected respondents; no causal wealth model |

Different samples, periods, messages and endpoints preclude pooling their coefficients as if they described successive stages in one Austrian population. Statistical significance does not repair that transportability problem.

## Prior exposure and targeting: association is meaningful but not causation

The [Gmail study](../../raw/papers/2026-10-17-scam-gmail-breach-targeting.md) measured 1.2 billion detected malicious emails during April–August 2020. Prior breach-corpus inclusion had average adjusted weekly targeting odds ratio 5.20. The endpoint is receiving phishing **or malware**, not successful phishing, a fivefold probability of theft, or measured wealth.

An odds ratio is not a risk ratio. If baseline probability is `p` and an odds ratio is `r`, the corresponding comparison probability is `r*p/(1-p+r*p)`, not `r*p`. That identity does not make this observational coefficient causal. Prior exposure can correlate with online footprint and other unmeasured factors; classifiers also determine which attacks enter the sample.

The useful finding is that breach-exposed populations can experience systematically different targeting. A DAC8 estimate would still need actual fields, a relevant population, outcomes and a counterfactual.

## Relevant context can affect behaviour

The [Social Phishing experiment](../../raw/papers/2026-10-17-scam-social-phishing-credentials.md) found valid university credential authentication in 349/487 acquaintance-context recipients versus 15/94 unfamiliar-sender controls. This is stronger than a click-only endpoint. Public relationship data, not leaked financial records, supplied the context. Allocation was not clearly documented as randomized; the 2005 student setting cannot supply a contemporary Austrian rate.

Its relevance is functional: knowing a real relationship can make an otherwise false approach more credible. The size of that particular contrast should not be transported to a tax-reporting context or described as the isolated effect of one financial data field.

The [2026 Czybik experiment](../../raw/papers/2026-10-17-scam-czybik-llm-denominators.md) adds evidence of scalable use of public professional context. It does not establish leaked-data causation. In particular, the final PDF's Table 2 reports 330 clicks and 3,177 delivered personalised emails but labels the rate 10.0%. The division gives about 10.39%; 10.0% instead matches the sent denominator. The raw counts should be retained rather than silently endorsing the inconsistency.

The [controlling precision supplement](../../raw/articles/2026-10-17-scam-empirical-precision-supplement.md) also makes clear that the sending server was allowlisted in the institution's spam filter, not guaranteed delivery: overall delivery was 89.5%. Pooled generic comparisons include people without public profiles. Richer profiles performed worse than low/medium profiles. This is adverse to a universal monotonic “more data means more success” claim, while still supporting context-dependent exploitation.

## Repeated exposure and control effectiveness

The [Lain study](../../raw/papers/2026-10-17-scam-lain-longitudinal-controls.md) followed 14,733 employees across eight campaigns over fifteen months. Messages and people are different denominators: 6,680 clicked messages out of 117,864 versus 4,729 people who clicked at least once. Among 3,747 people who ever performed a dangerous action, 896 repeated one.

Warnings reduced engagement in the tested configurations. Embedded post-failure training did not improve later detection in that implementation. Neither result warrants “training never works”, “warnings solve fraud”, or a realised financial-loss estimate. The control comparisons are more causally informative than the study's observational differences between kinds of people.

A useful technical inference is that incident response must consider subsequent attempts, not merely the first wave. Changing a password may remove stolen-login access without removing a contact list or the credibility of a real provider relationship. That distinction should be measured, not assumed to imply inevitable compromise.

## Actual repeated payments, not just experimental clicks

The [NIJ account](../../raw/articles/2026-10-17-scam-nij-repeat-loss-records.md) describes 1,383,755 victims and 11,870,085 completed incidents across four seized databases. Sixty-two percent had multiple incidents; a small group with more than twenty incidents generated a large revenue share. This supplies observed repeat-payment evidence rather than engagement alone.

It lacks unsuccessful solicitations and nonpayers. Therefore it cannot separate more frequent approaches from a greater probability of responding to each one, or prove that a particular leak supplied the addresses. The institutional account was read; the inaccessible underlying grantee report was not.

The [DeLiema survey](../../raw/papers/2026-10-17-scam-deliema-vulnerability-not-wealth.md) adds a different caution: financial fragility associated with reported frequency among selected known-victim respondents. The nonsignificant income comparison was specifically below USD50,000 versus at least USD50,000; nondisclosure was significant. As clarified in the supplement, this is not net wealth, a general absence of income effects or a causal targeting result. It supports keeping vulnerability and wealth conceptually separate.

## Negative and missing evidence are not interchangeable

[GAO's historical investigation](../../raw/articles/2026-10-17-scam-gao-attribution-limits.md) found apparent attributable identity theft in four of twenty-four selected breaches, none identified in eighteen, and insufficient information in two. It explicitly could not establish the full extent. These findings are adverse to assuming every breach causes identity theft, but not proof that eighteen breaches were harmless. Selection, detection and delayed or untraceable misuse remain problems.

The same discipline applies to modern company statements: “no losses reported at this date”, “confirmed no transactions during this attack” and “no systematic follow-up” are different findings. Reporting only successful cases exaggerates risk; reporting only detected immediate loss understates what remains unknown. Neither bias is cured by adding more incident anecdotes.

## What an Austrian empirical test should measure

An expert commission should define separate outcomes for confirmed extraction, attempted contact, engagement, secret disclosure or approval, completed transfer, recovered value, net loss and physical threats. Person counts must be deduplicated across suppliers, years and campaigns. It should retain nonresponders and failed attempts, not only victims.

Field-bundle comparisons should isolate relevance from volume: actual annual report fields; provider-held identifiers; contact/address records; and independently available public information. Use synthetic or consented contexts, a pre-registered analysis and ethical simulations—never deliberate exposure to real offenders. Randomize defensible informational/control conditions where possible; otherwise state what confounding remains.

Report effect uncertainty, subgroup composition, delivery/filtering conditions, repeated-person dependence, classifier error, attrition and outcome follow-up. A click advantage cannot establish loss severity; an enforcement loss total cannot establish the exposed population's risk. No product of coefficients from the studies above is a valid substitute.

## See Also

- [[surveillance-autonomy-and-democratic-safeguards|Surveillance, Autonomy and Democratic Safeguards]] ([Surveillance, Autonomy and Democratic Safeguards](surveillance-autonomy-and-democratic-safeguards.md)) — compatible evidence standards for the distinct non-breach chilling pathway.
- [[financial-data-composition-and-attribution-error|Financial-Data Composition and Attribution Error]] ([Financial-Data Composition and Attribution Error](financial-data-composition-and-attribution-error.md)) — information gains, no-match controls and error before the harm endpoint.
- [[criminal-data-markets-and-repeat-victimisation|Criminal Data Markets and Repeat Victimisation]] ([Criminal Data Markets and Repeat Victimisation](criminal-data-markets-and-repeat-victimisation.md)) — admitted feedback, pricing and high-balance selection.
- [[leaked-data-scams-and-targeted-attacks|Leaked Data, Financial Scams and Targeted Attacks]] ([Leaked Data, Financial Scams and Targeted Attacks](leaked-data-scams-and-targeted-attacks.md)) — concrete incident endpoints.
- [[financial-data-threat-model-and-control-evaluation|Financial-Data Threat Model and Control Evaluation]] ([Financial-Data Threat Model and Control Evaluation](financial-data-threat-model-and-control-evaluation.md)) — architecture, alternatives and audit deliverables.

## Sources

The frontmatter and linked immutable records preserve original publications, locators and methodological limits. The precision supplement controls the two stated shorthand ambiguities; the original records were not overwritten.
