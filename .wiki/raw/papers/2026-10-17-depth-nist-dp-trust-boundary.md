---
title: "NIST226: privacy unit, composition and trusted-curator boundary"
source: "https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-226.pdf"
type: papers
ingested: 2026-10-17
fetched: 2026-10-17
content_format: pdf
tags: [differential-privacy, trust-model, composition, privacy-unit]
summary: "Differential privacy protects specified releases and privacy units, not every raw-data holder or parallel exact release."
---

# NIST226: privacy unit, composition and trusted-curator boundary

SP800-226 final6March2025. Relevant full-PDF sections:2.1.2,2.4.2,2.6–2.7,4.2; printedpp.12–13,21–23,27–28,54–57.

Event-level guarantees need not protect a person's accumulated activity; repeated releases require composition accounting. Central DP trusts the raw-data curator; local DP changes exposure but trades accuracy. Parallel exact releases are not protected by a DP release. Empirical audits can find counterexamples, not prove the complete guarantee. These are formal protection boundaries, not a proposed implementation or claim that noisy statistics replace exact individual tax records.

Mechanical credibility 2; assessed independently from the research agent. Historical primary material is accepted for the bounded mechanism, not current prevalence. No underlying personal dataset was obtained.

