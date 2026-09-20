---
title: "Financial-Data Breach and Security Authorities"
category: reference
sources:
  - raw/articles/2026-09-04-austria-rechnungshof-bmf-it-security-audit.md
  - raw/articles/2026-09-04-dac8-security-controller-breach-architecture.md
  - raw/articles/2026-09-04-austria-eu-ahg-section-19a-breach-response.md
  - raw/articles/2026-09-04-cjeu-c340-21-tax-authority-breach-security.md
  - raw/articles/2026-09-04-ecthr-i-v-finland-database-security.md
  - raw/articles/2026-09-04-france-dgfip-tax-data-breach.md
  - raw/articles/2026-09-04-france-ficoba-account-register-breach.md
  - raw/articles/2026-09-04-coinbase-2025-data-theft-8k.md
  - raw/articles/2026-09-04-cnil-2025-breach-report-detailed-extraction.md
  - raw/articles/2026-08-27-waltio-security-incident.md
  - raw/articles/2026-08-27-vfgh-e-2097-2021-dac2.md
  - raw/articles/2026-09-19-gendarmerie-waltio-target-selection.md
  - raw/articles/2026-09-19-bobigny-tax-insider-le-parisien.md
  - raw/articles/2026-09-19-bobigny-tax-insider-protos.md
  - raw/articles/2026-09-19-coinbase-insider-social-engineering-disclosure.md
  - raw/articles/2026-09-19-saavedra-plea-location-abuse.md
  - raw/articles/2026-09-19-doj-iza-saavedra-location-attack.md
  - raw/articles/2026-09-19-doj-saavedra-plea-status.md
  - raw/articles/2026-09-19-france-dgfip-wallet-risk-debate.md
created: 2026-09-04
updated: 2026-09-19
tags: [data-breach, tax-authority, casp, security, article-32, evidence, adverse-authority]
aliases: [DAC8 breach evidence, financial database security]
confidence: high
volatility: hot
verified: 2026-09-19
summary: "Incident and case-law matrix showing what real financial-data breaches establish, what concrete security review requires, and why abstract hacking risk remains insufficient."
---

# Financial-Data Breach and Security Authorities

> Real breaches make the threat model concrete. They do not prove that DAC8 is invalid or that any Austrian controller's safeguards are inadequate. The legally useful move is from generic probability to the exact data combination, access path, control failure, detection mechanism and remediability at each controller.

## Incident evidence by layer

The 19 September update concerns Waltio, Coinbase, Bobigny, Saavedra/Iza and the French parliamentary debate. Other incident and legal-authority entries retain their 4 September verification scope. Confidence varies by row; the Bobigny account is reported allegation, not an official factual finding.

| Source | Layer and access path | Data described by source | Evidentiary contribution | What it does not prove |
|---|---|---|---|---|
| French DGFiP, August 2026 | tax-authority systems; impersonated employee and authorised-third-party credentials | identity/contact, tax and cadastral address/surface data; 678,000 individuals and businesses | authority systems can suffer credential-based bulk extraction and delayed exfiltration detection | no crypto data, Austrian likelihood, misuse or security-law finding |
| French FICOBA, February 2026 | state account register; stolen inter-ministerial official credentials | identity, postal address and IBAN/RIB for about 1.2 million account records | a restricted financial register is exposed through a legitimate-access channel | no balances, transactions, crypto data or proven fraud |
| Coinbase Form 8-K and company disclosure, May 2025 | provider support systems; paid employees or contractors | name, address, ID images, masked identifiers, balance snapshots and transaction history | insider path plus acknowledged downstream impersonation losses | company excludes stolen keys and direct fund access; no physical harm established; public-address exposure not determined |
| Waltio disclosure and September 2026 Gendarmerie account | private crypto-tax service, not tax authority | provider identifies email, annual gain/loss and year-end asset balances | police expressly attribute criminal target selection to the leak | provider excludes identity documents, postal addresses, wallet addresses and transaction history; police account is not case-level causal adjudication |
| Bobigny, January 2026 reporting | alleged misuse of tax-employee access | new residential address according to derivative reporting | reported insider-to-violence sequence, distinct from external hacking | no inspected judgment, verified final outcome or established attack on a crypto investor from these searches |
| Saavedra/Iza, plea factual basis and DOJ accounts | abused police powers; fraudulent GPS warrant and separate database misuse | phone location used to locate a targeted person | admitted official-access misuse; DOJ connects the location to an armed home-invasion attempt | no tax-reporting data, no proof a static database supplied this address; no Austrian-system inference |
| CNIL annual report 2025 | general notification baseline | 6,167 notifications; sector and access-control observations | breaches and credential failures are a persistent institutional concern | no DAC8-specific rate, unique-person count, causation or Austrian finding |

DGFiP and FICOBA concern authority-held records rather than commercial-provider records. Both official accounts distinguish affected from unaffected fields; neither is an adjudication that the underlying reporting or register law was disproportionate.

Bobigny is a separate press-reported allegation; Waltio is a private provider. The [Bobigny original-report digest](../../raw/articles/2026-09-19-bobigny-tax-insider-le-parisien.md) records the subscription access limit, and the [derivative digest](../../raw/articles/2026-09-19-bobigny-tax-insider-protos.md) separates reported payment to attackers from an unverified data-sale price. The [Waltio police attribution](../../raw/articles/2026-09-19-gendarmerie-waltio-target-selection.md) and [Coinbase fraud disclosure](../../raw/articles/2026-09-19-coinbase-insider-social-engineering-disclosure.md) supersede the earlier blanket absence-of-harm wording.

## Governing authorities

The [[european-data-misuse-and-physical-risk|European evidence supplement]] ([European evidence supplement](european-data-misuse-and-physical-risk.md)) adds source-checked Dutch insider cases and EU risk-assessment materials. It also records the Garante's current interim-suspension notice, preventing an outdated Intesa sanction account from being treated as a final finding.

The [Saavedra filing](../../raw/articles/2026-09-19-saavedra-plea-location-abuse.md), [DOJ attack account](../../raw/articles/2026-09-19-doj-iza-saavedra-location-attack.md) and [plea-status update](../../raw/articles/2026-09-19-doj-saavedra-plea-status.md) are a factual insider-risk comparison, not governing security-law authority.

The [French parliamentary debate](../../raw/articles/2026-09-19-france-dgfip-wallet-risk-debate.md) provides a separate risk-assessment lead: an MP quoted a DGFiP warning about sensitive data concentration, but the warning concerned an additional wallet-declaration proposal. The underlying email was not independently inspected, and the minister expressly supported DAC8. It cannot be cited as an official conclusion that DAC8 is unsafe or unlawful.

| Authority | Usable proposition | Adverse or limiting proposition |
|---|---|---|
| CJEU C-340/21 | national courts must examine the nature, content, implementation and practical effect of security measures against concrete processing risks; the controller proves appropriateness in an Article 82 action | third-party access or a breach does not by itself prove inappropriate measures; feared misuse must be well founded for damages |
| ECtHR I v Finland | Article 8 may require practical and effective protection against unauthorised access rather than reliance only on ex post compensation | highly sensitive medical data and acknowledged non-compliant access controls materially limit transfer to tax reporting |
| VfGH E 2097/2021 | the DAC2 decision recognises the binding effect of GDPR Article 32 and other safeguards | abstract security concerns did not create serious validity doubts; a DAC8 argument needs system facts that were absent there |

CJEU C-340/21 is an Article 32 and Article 82 judgment, not a validity or proportionality ruling on mandatory reporting. It is best used to define the required factual review, not to convert every breach into proof of invalidity.

## DAC security architecture to test

Directive 2011/16/EU already allocates security responsibilities for the CCN and Member-State systems, limits accredited technical access, residence-gates DAC8 directory access and provides breach notification, exchange suspension and remediation mechanisms in Articles 21 and 25. Austria implements authority-side suspension in section 19a EU-AHG. These safeguards are adverse to a claim that no controls exist.

The 2024 Austrian Court of Audit report is further adverse authority. For the principally 2018-to-2022 period it records BMF ISO 27001 and ISO 27701 certification, standardised security reporting, installed IDS/IPS and SIEM, 255 security reviews and monthly BRZ vulnerability scans. The Court of Audit concluded that the BMF could detect, analyse and reduce security risks to a high degree. The report predates the Krypto-MPfG, excluded provider security management such as BRZ from scope and did not examine a DAC8 production architecture. It supports disclosure of the current system evidence, not an inference of current weakness.

The remaining factual questions are:

- which preventive and detective controls apply at the provider, Austrian authority, CCN or central directory and recipient authority;
- whether access is least-privilege, separately approved and logged;
- whether contractor, administrator and authorised-third-party credentials can export bulk records;
- whether identity and activity fields are compartmentalised or directly joinable with address-bearing records;
- how anomalous consultation and extraction are detected;
- how a correction, restriction, suspension or deletion propagates across copies;
- whether the controls are tested for effectiveness under Article 32(1)(d), not merely documented.

## Litigation use

The incident evidence supports requests for architecture, logs and risk assessments. It also supports treating the combination of home address and financial activity as a material security consideration. It does not carry a facial invalidity claim by itself.

A stronger case requires an identified controller and one of the following:

- a documented access-control or monitoring deficiency;
- unnecessary co-location or joinability of identity and address-bearing records;
- an unexplained bulk-export path;
- retention without a current-necessity review;
- a concrete refusal to disclose recipients or access logs where legally required;
- a correction, deletion or breach-response mechanism that fails in practice.

## Claims to exclude

- financial databases are inevitably breached;
- a breach proves the controller's Article 32 measures were inadequate;
- the DGFiP or FICOBA incidents involved crypto, DAC8 or Austrian systems;
- police attribution or press allegations are equivalent to a judicially established DAC8 leak-to-attack chain;
- CNIL notification counts measure DAC8 or crypto breach probability;
- private keys were exposed in the described incidents, Waltio exposed wallet addresses, or the Coinbase field list conclusively resolves public-wallet-address exposure.

## See Also

- [[data-risk-prevention-and-damages-thresholds|Data-Risk Prevention and Damages Thresholds]] ([Data-Risk Prevention and Damages Thresholds](data-risk-prevention-and-damages-thresholds.md)) — distinguishes preventive obligations from compensation and operational protection.

- [[dac8-data-lifecycle-access-retention-remedies|DAC8 Data Lifecycle: Access, Retention and Remedies]] ([DAC8 Data Lifecycle: Access, Retention and Remedies](dac8-data-lifecycle-access-retention-remedies.md))
- [[identity-to-public-ledger-linkage-evidence|Identity-to-Public-Ledger Linkage Evidence]] ([Identity-to-Public-Ledger Linkage Evidence](identity-to-public-ledger-linkage-evidence.md))
- [[dac8-vs-dac2-distinguishing-arguments|DAC8 versus DAC2: Distinguishing Arguments]] ([DAC8 versus DAC2: Distinguishing Arguments](dac8-vs-dac2-distinguishing-arguments.md))
- [[dac8-security-architecture-and-audit-evidence|DAC8 Security Architecture and Audit Evidence]] ([DAC8 Security Architecture and Audit Evidence](dac8-security-architecture-and-audit-evidence.md))

## Sources

- [CJEU C-340/21](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62021CJ0340)
- [ECtHR I v Finland](https://hudoc.echr.coe.int/eng?i=001-87510)
- [French DGFiP incident](https://presse.economie.gouv.fr/acces-illegitime-au-systeme-dinformation-de-la-direction-generale-des-finances-publiques/)
- [French FICOBA incident](https://www.impots.gouv.fr/actualite/acces-illegitimes-au-fichier-national-des-comptes-bancaires-ficoba)
- [Coinbase Form 8-K](https://www.sec.gov/Archives/edgar/data/1679788/000167978825000094/coin-20250514.htm)
- [CNIL annual report 2025](https://www.cnil.fr/sites/default/files/2026-05/rapport_annuel_2025.pdf)
- [Austrian Court of Audit, Bund 2024/16](https://www.rechnungshof.gv.at/rh/home/home/2024_16_IT-Sicherheit_BM.pdf)
