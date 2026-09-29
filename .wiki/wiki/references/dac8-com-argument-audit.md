---
title: "DAC8.com and Bull Bitcoin Argument Audit"
category: reference
sources:
  - raw/articles/2026-08-27-dac8-com-campaign-overview.md
  - raw/articles/2026-08-27-dac8-com-reverse-effect.md
  - raw/articles/2026-08-27-dac8-com-targeted-requests.md
  - raw/articles/2026-08-27-dac8-com-unproven-effectiveness.md
  - raw/articles/2026-08-27-bull-bitcoin-conseil-etat-action.md
  - raw/articles/2026-09-29-refreshat-conseil-etat-519158-dac8-suspension-refused.md
  - raw/articles/2026-09-29-refreshat-dac8-com-wording-september-2026.md
created: 2026-08-27
updated: 2026-09-29
tags: [dac8-com, bull-bitcoin, source-audit, proportionality, factual-claims]
aliases: [Bull Bitcoin DAC8 arguments]
confidence: high
volatility: hot
verified: 2026-09-29
summary: "Primary-source audit separating Bull Bitcoin's legally useful DAC8 arguments from claims requiring qualification or contradicted by the directive and Austrian law."
---

# DAC8.com and Bull Bitcoin Argument Audit

> DAC8.com is a useful advocacy lead, not an authoritative description of the reporting schema or litigation status.

## Supported by primary law

- Reporting is systematic and does not depend on individualized tax suspicion or a de minimis customer threshold.
- Reported identity fields include name, address, tax residence, TIN, and—for individuals—date and place of birth where applicable.
- Reporting begins for the 2026 period, with the first inter-authority exchange due in 2027.
- The annual report contains per-asset category aggregates. Most activity categories include value, units and count; the separate outward-transfer field contains value and units for DLT addresses not known by the provider to be associated with a VASP or financial institution, but no address or transaction count.
- Linking civil identity/home-address information to a crypto activity profile creates a plausible privacy and physical-security risk. A court filing still needs evidence of threat probability, access paths, and actual correlation capability.

## Requires qualification

- **“Every crypto business”**: DAC8 applies to defined reporting crypto-asset service providers and reportable users, with exclusions and jurisdictional routing rules.
- **“Blockchain correlation reveals everything”**: correlation may create additional inferences, but it requires separately held address or transaction information. The DAC8 report itself is not a wallet graph.
- **“No proof the system works”**: the Commission's 2025 evaluation acknowledges limitations in measuring benefits and the ECA identified data-quality, use, and monitoring weaknesses. Those materials do not conclude that DAC is inherently ineffective.
- **French lawsuit status**: Bull Bitcoin says it filed in the Conseil d'État on 24 February 2026 and filed a fuller brief on 22 May 2026; its own legal-action page, dated 3 July 2026, still says the brief is "to come". An official order confirms the litigation: on 14 September 2026 the interim-relief judge (n° 519158; applicants Paymium, Leonod and Satoshi Portal Inc.) rejected a 26 August 2026 suspension request solely for lack of urgency, without examining legality. A merits request is pending; its number is unpublished. The campaign's statement that "the Conseil d'État will rule after a reference to the Court of Justice" is a prediction; no decision to refer has been located.

## Contradicted or unsupported as a description of DAC8

- The report does **not** contain wallet/DLT addresses.
- It does **not** contain transaction dates, transaction identifiers, or counterparties. The campaign still lists "dates" among reported data, and its 16 September 2026 suspension response says the decree requires "the complete transaction history of every one of their users". Both are inaccurate for the annual aggregate report.
- It is not automatically replicated into “27 national databases” for every person. The campaign now also says data will go into "a single European directory, hosted by the Commission". DAC8 does provide for a secure central directory for information communicated on crypto-assets (recital 38; Article 21(5) of Directive 2011/16/EU as amended). Each Member State may access only information on its own residents, and the Commission only for statistical purposes. The directory holds annual aggregates on Reportable Users, not the transactions of all EU residents. Multiple authorities and access systems still create a real exposure surface.
- Pure peer-to-peer, decentralized, or non-custodial activity is not automatically reportable without a covered reporting intermediary and reportable-user nexus.
- Targeted information requests are not functionally identical to annual automatic exchange; they differ in timing, evidentiary threshold, coverage, and enforceability.

## Litigation-ready core

The durable argument is not “DAC8 reports every wallet transaction.” It is that suspicionless identity-linked annual profiling across crypto-asset categories may be disproportionate when exact fields, pre-report processing, retention, access, security, remedies, and less intrusive alternatives are assessed together. The merits comparison must include the adverse Austrian DAC2 decisions and CJEU C-623/22, not only Digital Rights Ireland.

For the exact field and inference boundaries, see [[dac8-field-necessity-and-alternatives|DAC8 Field Necessity and Less-Intrusive Alternatives]] ([DAC8 Field Necessity and Less-Intrusive Alternatives](dac8-field-necessity-and-alternatives.md)) and [[dac8-inference-linkage-and-error-evidence|DAC8 Inference, Linkage and Error Evidence]] ([DAC8 Inference, Linkage and Error Evidence](dac8-inference-linkage-and-error-evidence.md)).

## Sources

- [Conseil d'État order n° 519158](../../raw/articles/2026-09-29-refreshat-conseil-etat-519158-dac8-suspension-refused.md)
- [dac8.com wording, September 2026](../../raw/articles/2026-09-29-refreshat-dac8-com-wording-september-2026.md)
- [DAC8](../../../legal-docs/core/eu-dac8-directive-2023-2226.pdf)
- [Consolidated Directive 2011/16/EU](../../../legal-docs/core/eu-directive-2011-16-consolidated-2026.pdf)
- [Austrian Krypto-MPfG](../../../legal-docs/core/at-bgbl-i-96-2025-krypto-mpfg.pdf)
- [Commission 2025 DAC evaluation](../../../legal-docs/supporting/eu-com-2025-695-dac-evaluation.pdf)
- [ECA Special Report 03/2021](../../../legal-docs/supporting/eu-eca-special-report-03-2021.pdf)
