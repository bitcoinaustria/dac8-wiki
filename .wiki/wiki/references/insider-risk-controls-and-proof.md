---
title: "Insider-Risk Controls and Proof"
category: reference
sources:
  - raw/articles/2026-09-19-dora-detailed-access-controls.md
  - raw/articles/2026-09-19-dora-access-update-clarification.md
  - raw/articles/2026-09-19-edpb-insider-breach-example.md
  - raw/papers/2026-09-19-bra-criminal-insider-enablers.md
  - raw/articles/2026-09-04-mica-dora-casp-security-baseline.md
created: 2026-09-19
updated: 2026-09-19
verified: 2026-09-19
volatility: warm
confidence: high
tags: [insider-threat, dora, casp, access-control, evidence]
summary: "Binding CASP controls, EDPB guidance and qualitative European evidence identify testable insider-risk questions without assuming a breach or automatic high risk."
---

# Insider-Risk Controls and Proof

An authorised account can be used for an unauthorised purpose. Evidence about access restrictions, export capability and detection therefore matters separately from encryption or resistance to external intrusion.

## Three different evidence classes

| Source | What it establishes | What it does not establish |
|---|---|---|
| [DORA delegated regulation 2024/1774](../../raw/articles/2026-09-19-dora-detailed-access-controls.md), Arts 12, 20, 21, 23 | Binding detailed controls within its scope | That an Austrian provider complies or fails; application to the BMF |
| [EDPB Guidelines 01/2021, case 08](../../raw/articles/2026-09-19-edpb-insider-breach-example.md), paras 72–77 | Legitimate access can facilitate copying; risk assessment still matters | A real crypto incident or automatic high risk for every insider breach |
| [Brå report 2024:2](../../raw/papers/2026-09-19-bra-criminal-insider-enablers.md), pp 60–61 | Qualitative evidence of leaked information disrupting a housing/support service for gang defectors | A population incidence, DAC8 attack or judicially established physical injury |

The EDPB example is an important limit: basic contact-data copying warranted authority notification but not high-risk notification to individuals in that specific scenario. Severity depends on the actual data and context.

## Provider-side benchmark

[DORA's CASP scope](../../raw/articles/2026-09-04-mica-dora-casp-security-baseline.md) is narrower than the universe of DAC8 reporting operators. Under the ordinary detailed framework:

- Article 20 requires attributable identities and identity-lifecycle controls.
- Article 21 addresses least privilege, separation of duties, privileged access and revocation. Point (e)(iv) requires access-right updates when changes are necessary and at least annually, or every six months for systems supporting critical or important functions. The [terminology clarification](../../raw/articles/2026-09-19-dora-access-update-clarification.md) corrects the initial digest's looser “review” wording.
- Article 12 protects logging and requires attention to logging failures. Retaining a log is distinct from detecting abuse.
- Article 23 addresses collection and analysis for anomaly detection, including internal threats.

These duties provide a benchmark for inspecting the tax-data workflow. They do not authorise tax-purpose reuse of separate records, determine retention under another regime or demonstrate that every human query must receive prior individual approval.

## Decision-relevant proof

Useful implementation evidence would connect a specific dataset to its permitted roles, bulk-export permissions, review history, log coverage, alert tests and correction of identified defects. This is an evidentiary inference from the controls, not a claim of an unrestricted right to receive security documentation.

The comparison is between demonstrably effective controls and a specified residual risk. A documented duty alone does not prove effectiveness; a possible abuse alone does not prove inadequacy. Foreign experience supports examining the mechanism, not presuming an Austrian failure.

## See Also

- [[dac8-security-architecture-and-audit-evidence|DAC8 Security Architecture and Audit Evidence]] ([DAC8 Security Architecture and Audit Evidence](dac8-security-architecture-and-audit-evidence.md))
- [[european-data-misuse-and-physical-risk|European Data Misuse and Physical-Risk Evidence]] ([European Data Misuse and Physical-Risk Evidence](european-data-misuse-and-physical-risk.md))
