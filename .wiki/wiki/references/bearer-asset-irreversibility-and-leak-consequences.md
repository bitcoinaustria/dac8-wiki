---
title: "Bearer-Asset Irreversibility and Leak Consequences"
category: reference
sources:
  - raw/articles/2026-09-29-bearer-psd2-mica-loss-allocation.md
  - raw/articles/2026-09-29-bearer-esas-crypto-warning-2025.md
  - raw/papers/2026-09-29-bearer-fbi-ic3-2025-report.md
  - raw/articles/2026-09-29-bearer-ledger-2020-leak-ceo-disclosure.md
  - raw/articles/2026-09-29-bearer-kroll-claimant-data-breach.md
  - raw/articles/2026-09-29-bearer-fractal-id-kyc-breach.md
  - raw/articles/2026-09-29-bearer-au10tix-credential-exposure.md
  - raw/articles/2026-09-29-bearer-balland-kidnapping-status.md
  - raw/repos/2026-09-29-bearer-lopp-physical-attacks-dataset.md
  - raw/articles/2026-09-29-bearer-france-an-crypto-violence-answers.md
  - raw/articles/2026-09-29-bearer-france-decree-2025-840-rcs-address.md
  - raw/articles/2026-09-29-bearer-france-interior-crypto-guidance.md
  - raw/articles/2026-09-29-acctmodel-stablecoin-issuer-freeze-terms.md
  - raw/articles/2026-09-19-coinbase-insider-social-engineering-disclosure.md
  - raw/articles/2026-09-19-gendarmerie-waltio-target-selection.md
  - raw/papers/2026-09-19-abramova-breach-fulltext.md
created: 2026-09-29
updated: 2026-09-29
tags: [bearer-asset, self-custody, irreversibility, data-breach, kyc, physical-security, psd2, mica, france]
aliases: [Bearer-asset risk, crypto theft irreversibility, KYC leak consequences]
confidence: medium
volatility: hot
verified: 2026-09-29
summary: "EU law gives bank-payment victims a statutory refund for unauthorised payments but gives self-custody holders no refund or recall right; KYC and intermediary leaks have joined identity, address and crypto status, balances or wallet addresses, and France treats address exposure as a safety emergency, but no source attributes a physical attack to a specific leak or involves DAC8 data."
---

# Bearer-Asset Irreversibility and Leak Consequences

Self-custodied crypto-assets behave like bearer assets: control of the private key is control of the asset, and there is no account provider that can reverse a transfer. This article sets out how EU law allocates losses, which leaks have joined identity with crypto status, and what the evidence does and does not show about the step from leak to harm.

## Legal loss allocation

| Holding form | Instrument | Loss allocation | Limit |
|---|---|---|---|
| bank or e-money account | PSD2 Articles 64, 73 and 74 | unauthorised payment refunded by the end of the next business day; payer liability capped at EUR 50 unless fraud or gross negligence; provider bears the burden of proving authentication (Article 72) | a payment made under physical coercion is arguably "authorised"; no case law on duress was checked |
| custodial crypto account | MiCA Article 75(8) | custodial CASP liable for loss of crypto-assets or means of access "as a result of an incident that is attributable to them", capped at market value | excludes incidents independent of the service, including ledger-inherent problems; no refund right for customer-authorised transfers |
| self-custody | none | no counterparty; no refund or recall right | recovery only through tracing, freezing at a regulated intermediary or a stablecoin issuer, and seizure |

Sources: PSD2 and MiCA digest. The contrast between the rows is a legal inference recorded in that digest, not a holding.

The ESAs' October 2025 joint warning states that "losing private keys to crypto-assets results in the permanent and irreversible loss of access and ownership" and that MiCA holders "will not benefit from compensation schemes". It does not address coerced transfers.

For credential theft, the contrast is strong: a bank-account victim usually has a refund dispute, while a self-custody victim has a final loss. For wrench attacks, the contrast narrows. A bank payment extracted under duress may also be authorised. The practical differences are then bank-side limits, delays, fraud monitoring and recall channels. The FBI IC3 2025 report shows that recall working through banks: its Recovery Asset Team froze USD 679 million of USD 1.164 billion in attempted theft (58 percent). It gives no comparable figure for self-custody.

**Limiting evidence.** The French Interior Ministry describes crypto as "nativement traçable" and reports EUR 90 million in crypto seized by the asset-recovery agency AGRASC since 2014. CASPs must freeze and report under MiCA and the TFR, and stablecoin issuers reserve address-level freeze powers. "Irreversible" therefore means no refund right, not that funds can never be recovered.

## Leak typology by data content

What a leak contains determines which attack stage it serves.

| Leak | Data joined with identity | Stage served | Source status |
|---|---|---|---|
| Ledger, 2020 | customer status (bought a hardware wallet); about 272,000 records with name, postal address and phone; about one million emails | target selection by crypto-holder status; locating; phishing by email, SMS and postal letters seeking the recovery phrase | company disclosure; Ledger says there is "no way to make any correlation" between the data and wallet funds |
| Waltio, 2026 (already in the wiki) | email, annual gain or loss, year-end balances | target selection by apparent wealth; police attribute target selection to the leak | company disclosure plus Gendarmerie account |
| Kroll, 2023 (FTX and two other crypto bankruptcies) | name, address, email, phone, claim amount, account ID, "coin holdings and balances" | target selection by balance; locating; tailored fraud | breach notices in a court-supervised case; balance-tailored phishing is secondary reporting |
| Coinbase, 2025 (already in the wiki) | identity, address, ID images, balance snapshots, transaction history | impersonation fraud acknowledged by the company | company disclosure and Form 8-K |
| Fractal ID, 2024 (Berlin KYC provider) | names, contact data, ID images, physical addresses and wallet addresses for about 6,300 users | identity-to-ledger anchor plus locating | company disclosure with externally confirmed scope; ransom refused; Berlin criminal complaint |
| AU10TIX, 2024 (ID-verification vendor) | ID document data and images; clients reportedly included Coinbase | vendor concentration; no holdings data | investigative journalism; company states no evidence of exploitation |

Two patterns matter. First, outsourced KYC and claims intermediaries concentrate identity documents from many regulated firms; the Kroll, Fractal ID and AU10TIX incidents each ran through one compromised credential or phone number, and Coinbase through bribed support staff. Second, Fractal's records combine identity, home address and wallet address in one record — the anchor that [[identity-to-public-ledger-linkage-evidence|Identity-to-Public-Ledger Linkage Evidence]] ([Identity-to-Public-Ledger Linkage Evidence](identity-to-public-ledger-linkage-evidence.md)) treats as the high-persistence case. On account-based chains, one such address exposes balance and ordered history directly; see [[account-model-linkage-exposure|Account-Model Chains and Exposure After an Identity Link]] ([Account-Model Chains and Exposure After an Identity Link](../theses/account-model-linkage-exposure.md)).

## Physical-attack evidence and attribution status

- **Balland, January 2025.** A Ledger co-founder and his partner were abducted at home, with mutilation and a crypto ransom demand, reported as EUR 10 million. Seven people were formally charged; the judicial investigation is pending, and a further suspect was arrested in Spain in March 2026. Sources are media reports relaying the prosecutor. No source explains victim selection. A link to the 2020 Ledger leak is commentary only; the founder's public profile is an obvious alternative.
- **Lopp list.** A self-curated list of media-reported physical attacks has 363 rows from 2014 to 19 September 2026: 42 in 2024, 87 in 2025 and 63 in 2026 so far. France accounts for 23 of the 2025 rows and 42 of the 2026 rows; it includes a Vienna homicide in November 2025. Only a few rows mention a data source, and none names tax-authority data. There is no denominator, and it undercounts against French official figures.
- **French official counts.** The Interior Minister reported 77 cases of sequestration, abduction or extortion, or attempts, in the first half of 2026, against 45 in all of 2025; these figures are media-reported. A deputy's written question asserted about sixty in 2025. The counts use different definitions.
- **Victim research.** The Abramova and Böhme survey of Ledger-leak victims (already in the wiki) reports physical-safety concern and two reported physical threats, not verified assaults.

No source in this set attributes a completed physical attack to a specific leak. The Waltio police attribution concerns target selection and remains the strongest leak-to-targeting evidence.

## Official recognition in France

- In a Journal officiel answer of 15 September 2026, the Interior Ministry says that attacks on crypto professionals "ou de particuliers censés en détenir" (or on private individuals believed to hold crypto) have risen sharply. It lists prosecutorial, police and cyber-unit measures and a ten-measure plan of June 2026.
- The ministry also calls these crimes a variant of long-established organised-crime methods, not a new form. This is adverse to a claim that crypto creates a new threat type.
- Its January 2026 guidance states that private individuals are now also targeted. It advises against showing holdings or gains, and against wallet screenshots, and it recommends delaying the release of large amounts. It treats disclosure of holdings as a risk factor.
- Decree No. 2025-840 of 22 August 2025 lets company directors mask their home address in the company register (RCS) within five working days. Listed authorities and certain creditors keep access.
  - The Economy Ministry's answer calls the decree "une réponse rapide à une situation d'urgence susceptible de mettre en danger la sécurité des personnes" (a rapid response to an emergency liable to endanger personal safety).
  - The decree text itself states no rationale, and the answer does not tie it expressly to crypto.

These are official government positions, not judicial findings or audited statistics. They support the general point that a Member State treats address exposure as a personal-safety risk and can respond with access control rather than abolition of the register.

## Limits for DAC8

- None of these incidents involves tax-authority or DAC8 data.
- DAC8 reports are confidential, not published. The French register decree concerns public data and shows available minimisation measures, not equal risk.
- DAC8 annual reports contain identity, address and annual transaction values but no wallet address. A Fractal-type anchor arises only from provider-held MiCA or TFR records.
- The strongest transferable points are three. A leak of identity plus address plus crypto status or value serves target selection and locating. Self-custody removes the refund backstop that limits credential-theft losses in banking. And concentration at intermediaries has repeatedly failed through a single credential.
- The step from leak to attack remains unproved for any specific dataset. See [[dac8-physical-risk-causation|DAC8 Physical-Risk Causation and Evidence]] ([DAC8 Physical-Risk Causation and Evidence](dac8-physical-risk-causation.md)) for the causal ladder.

## Claims to exclude

- "Stolen crypto can never be recovered."
- "Bank customers are fully protected against coerced transfers."
- "The Ledger leak revealed customers' balances" or "caused the Balland abduction."
- "The Lopp list measures attack frequency."
- "France has recognised that tax data cause crypto kidnappings."
- "Any of these incidents involved DAC8 data."

## See Also

- [[dac8-physical-risk-causation|DAC8 Physical-Risk Causation and Evidence]] ([DAC8 Physical-Risk Causation and Evidence](dac8-physical-risk-causation.md)) — causal ladder and proof requirements.
- [[financial-data-breach-and-security-authorities|Financial-Data Breach and Security Authorities]] ([Financial-Data Breach and Security Authorities](financial-data-breach-and-security-authorities.md)) — authority and provider breach layers.
- [[european-data-misuse-and-physical-risk|European Data Misuse and Physical-Risk Evidence]] ([European Data Misuse and Physical-Risk Evidence](european-data-misuse-and-physical-risk.md)) — European insider and access cases.
- [[account-model-linkage-exposure|Account-Model Chains and Exposure After an Identity Link]] ([Account-Model Chains and Exposure After an Identity Link](../theses/account-model-linkage-exposure.md)) — exposure after a wallet-address leak.
- [[aml-kyc-effectiveness-evidence|AML and KYC Effectiveness Evidence]] ([AML and KYC Effectiveness Evidence](aml-kyc-effectiveness-evidence.md)) — KYC data collection whose concentration these leaks expose.

## Sources

- [PSD2 and MiCA loss allocation](../../raw/articles/2026-09-29-bearer-psd2-mica-loss-allocation.md)
- [ESAs joint warning, October 2025](../../raw/articles/2026-09-29-bearer-esas-crypto-warning-2025.md)
- [FBI IC3 2025 report](../../raw/papers/2026-09-29-bearer-fbi-ic3-2025-report.md)
- [Ledger 2020 leak](../../raw/articles/2026-09-29-bearer-ledger-2020-leak-ceo-disclosure.md)
- [Kroll claimant breach](../../raw/articles/2026-09-29-bearer-kroll-claimant-data-breach.md)
- [Fractal ID breach](../../raw/articles/2026-09-29-bearer-fractal-id-kyc-breach.md)
- [AU10TIX credential exposure](../../raw/articles/2026-09-29-bearer-au10tix-credential-exposure.md)
- [Balland abduction status](../../raw/articles/2026-09-29-bearer-balland-kidnapping-status.md)
- [Lopp physical-attacks list](../../raw/repos/2026-09-29-bearer-lopp-physical-attacks-dataset.md)
- [French written-question answers](../../raw/articles/2026-09-29-bearer-france-an-crypto-violence-answers.md)
- [French Decree 2025-840](../../raw/articles/2026-09-29-bearer-france-decree-2025-840-rcs-address.md)
- [French Interior Ministry guidance](../../raw/articles/2026-09-29-bearer-france-interior-crypto-guidance.md)
- [Circle and Tether freeze terms](../../raw/articles/2026-09-29-acctmodel-stablecoin-issuer-freeze-terms.md)
- [Coinbase insider disclosure](../../raw/articles/2026-09-19-coinbase-insider-social-engineering-disclosure.md)
- [Waltio police attribution](../../raw/articles/2026-09-19-gendarmerie-waltio-target-selection.md)
- [Abramova and Böhme full text](../../raw/papers/2026-09-19-abramova-breach-fulltext.md)
