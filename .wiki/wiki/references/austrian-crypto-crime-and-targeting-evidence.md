---
title: "Austrian Crypto-Crime and Targeting Evidence"
category: reference
sources:
  - raw/articles/2026-09-29-atcrypto-wels-2018-home-invasion-verdicts.md
  - raw/articles/2026-09-29-atcrypto-wels-2019-bitiago-office-robbery.md
  - raw/articles/2026-09-29-atcrypto-vienna-2025-kuzmin-homicide.md
  - raw/articles/2026-09-29-atcrypto-villach-2023-fake-bka-bitcoin-extortion.md
  - raw/papers/2026-09-29-atcrypto-bk-cybercrime-report-2025.md
  - raw/articles/2026-09-29-atcrypto-watchlist-finanzonline-crypto-phishing.md
  - raw/articles/2026-09-29-atcrypto-watchlist-bitpanda-coinbase-phishing.md
  - raw/articles/2026-09-29-atcrypto-bitpanda-breach-claim-denied.md
  - raw/articles/2026-09-29-atcrypto-ogh-7ob225-25a-bitcoin-insurance.md
  - raw/articles/2026-09-29-atcrypto-bmi-ripdeal-crypto-cases.md
  - raw/repos/2026-09-29-bearer-lopp-physical-attacks-dataset.md
created: 2026-09-29
updated: 2026-09-29
tags: [austria, physical-security, wrench-attacks, phishing, finanzonline, target-selection, fraud, ogh]
aliases: [Austrian crypto attacks, Krypto-Raub Österreich, FinanzOnline crypto phishing]
confidence: medium
volatility: hot
verified: 2026-09-29
summary: "Crypto-motivated coercion has occurred in Austria (Wels 2018 final convictions; Vienna 2025 homicide under Ukrainian proceedings), but every Austrian case with a known background involved victims selected through personal or business relationships; fraud and phishing dominate documented harm, and criminals already use the crypto tax-reporting reform and FinanzOnline branding as a pretext to harvest holdings."
---

# Austrian Crypto-Crime and Targeting Evidence

This reference collects Austrian evidence on physical attacks against crypto holders, crypto fraud and phishing, and leaks. It is the national counterpart to the French and US material in [[dac8-physical-risk-causation|DAC8 Physical-Risk Causation and Evidence]] ([DAC8 Physical-Risk Causation and Evidence](dac8-physical-risk-causation.md)) and [[bearer-asset-irreversibility-and-leak-consequences|Bearer-Asset Irreversibility and Leak Consequences]] ([Bearer-Asset Irreversibility and Leak Consequences](bearer-asset-irreversibility-and-leak-consequences.md)).

## Physical coercion cases

| Case | Facts | How the victim was selected | Procedural status | Confidence |
|---|---|---|---|---|
| Wels, June 2018 | home invasion of a crypto broker; exchange codes and face ID were forced out of him and funds moved on the spot | an acquaintance of the instigator blamed the victim for crypto-investment losses | five executors convicted with final effect (3 to 13 years); instigator's 3-year sentence (2 suspended) final at LG Linz, January 2020, per APA reporting | medium; judgment texts not read; reported amounts conflict (EUR 132,000 to about EUR 217,000) |
| Wels, July 2019 | armed robbery at a crypto firm's office; crypto transferred on the spot; firm insolvent weeks later | unknown | no arrest or verdict found | low; media only |
| Villach, June 2023 | a man posing as a German BKA officer demanded 60 BTC at a family's home, citing a murder contract linked to a crypto deal | not reported | arrest and partial confession reported; no verdict found | low; media only |
| Vienna, November 2025 | 21-year-old Ukrainian student killed after "a considerable sum" left his crypto wallet | a fellow student is among two suspects; tabloid reporting says he spoke openly about his holdings | suspects arrested in Ukraine; Austria transferred proceedings; detention extended as of June 2026; no indictment or verdict found | medium; police statements via media |

Victims in the Austrian cases with a known selection route were chosen through personal or business relationships or their own disclosure. No Austrian case attributes victim selection to leaked provider data, a register or tax data. In Wels 2018 the target was custodial exchange accounts, not only self-custody: coercion extracted credentials and biometrics.

No Austrian official source counts crypto-motivated violence. The Bundeskriminalamt's Cybercrime Report 2025 does not mention robbery, home invasion or kidnapping of crypto holders, and a BMI magazine feature on crypto crime is equally silent. Police statistics count offences by legal category, so this silence is not evidence that such attacks are absent.

## Fraud and phishing

- **Scale.** The Cybercrime Report 2025 records 63,459 cybercrime offences in 2025 and about EUR 120 million lost to cyber-trading fraud. It reports "a significant rise" in crypto fraud and increasing phishing aimed at "Inhaberinnen und Inhaber von Krypto-Börsen-Konten" (holders of crypto-exchange accounts). A Carinthian investment-fraud network with about 40,000 victims and EUR 20 million in proven losses was concluded in court.
- **Mass, not targeted.** Pig-butchering contacts go to "zufällig ausgewählte Personen" (randomly selected persons). Bitpanda impersonation is the most-reported phishing lure and reaches non-customers too. Watchlist Internet observed Coinbase-branded phishing rise in Austria after the 2025 Coinbase data theft; this shows contact attempts, not physical harm.
- **Rip-deals.** Vienna police describe schemes that spy out wallet access during in-person investor meetings. In one case, a 40-BTC loss followed an industrialist's public search for investors on a crowdfunding platform. The selection route here is self-published business information.

## DAC8 and FinanzOnline as a phishing pretext

Watchlist Internet documented a fake "Finanzamt" email in August 2025. It cited "neuen Steuervorschriften für Kryptowährungen, die ab 2025 in Kraft treten" (new crypto tax rules from 2025) and demanded a "mandatory form" on crypto holdings, with wallet connection via WalletConnect. A February 2026 SMS campaign with a fake FinanzOnline renewal portal asked whether the recipient uses crypto or holds gold, jewellery or larger cash amounts, then asked for banking logins. Watchlist links the pretext to the real EU tax-transparency reform and states that authorities send no such requests.

These warnings show that criminals already use the reporting reform, and the tax authority's brand, as a social-engineering pretext. The same campaigns combine wealth screening with address and login harvesting. The mass sending points the other way on data leaks: the senders lack a list of crypto holders and try to build one by self-disclosure. No genuine BMF, FinanzOnline or DAC8 dataset is involved.

Watchlist Internet is run by the ÖIAT and co-funded by the BMI's Bundeskriminalamt and the Oesterreichische Nationalbank. It is a consumer-protection platform, not an authority.

## Leaks affecting Austrian users

No confirmed breach at an Austrian crypto-asset service provider was found. In July 2025 a seller claimed to hold KYC, IBAN and wallet data for 5.4 million Bitpanda users; Bitpanda said the claim was false. This is adverse to any assertion of an Austrian provider leak. Only one search was run for other Austrian providers.

## Loss allocation and recovery in Austria

- **OGH 7 Ob 225/25a (25 March 2026).** Bitcoin lost after malware extracted the recovery phrase is not "simple theft" under the ABHP 2011 household-insurance conditions, because "kein physischer Gegenstand entwendet" (no physical object was taken). The holder bears the loss. This is a contract-interpretation holding on specific standard terms, read from the official summary; it is not a criminal-law ruling on whether crypto is a "Sache".
- **Tracing and freezing.** The Cybercrime Report describes C4 seizure capability since 2018 and about 1,000 authority wallets, and calls tracing "ressourcenintensiv" (resource-intensive). A BMI feature reports 140 ETH from a 2023 rip-deal frozen in time at a Seychelles provider. From 1 January 2025 the StPO treats crypto as assets, easing seizure and return. These qualify absolute irreversibility claims.

## Transfer to the Austrian DAC8 proceeding

- The threat class exists in Austria, including final convictions for a crypto home invasion. That supports prospective risk assessment, not a measured incremental DAC8 effect.
- Austrian cases show relationship-based and self-disclosure-based selection. Leak-based selection is documented abroad (Waltio police attribution) but not in Austria.
- The FinanzOnline phishing campaigns are the most direct Austrian link to DAC8. They show that reporting obligations create a credible pretext for fraud. The authority can counter this with communication, and the campaigns do not involve official data.
- Fraud is the dominant documented harm. An argument that emphasises physical risk should state that Austrian evidence for it is thin and mostly media-reported.

## Claims to exclude

- "Austrian crypto holders have been attacked using leaked data."
- "Bitpanda was breached."
- "DAC8 or FinanzOnline data leaked."
- "Stolen crypto can never be recovered in Austria."
- "The Vienna 2025 suspects have been convicted."

## See Also

- [[dac8-physical-risk-causation|DAC8 Physical-Risk Causation and Evidence]] ([DAC8 Physical-Risk Causation and Evidence](dac8-physical-risk-causation.md)) — causal ladder and proof requirements.
- [[bearer-asset-irreversibility-and-leak-consequences|Bearer-Asset Irreversibility and Leak Consequences]] ([Bearer-Asset Irreversibility and Leak Consequences](bearer-asset-irreversibility-and-leak-consequences.md)) — EU loss allocation and leak typology.
- [[austrian-risk-based-access-protection|Austrian Risk-Based Register-Access Protection]] ([Austrian Risk-Based Register-Access Protection](austrian-risk-based-access-protection.md)) — Austrian register-access restrictions.

## Sources

- [Wels 2018 home invasion verdicts](../../raw/articles/2026-09-29-atcrypto-wels-2018-home-invasion-verdicts.md)
- [Wels 2019 office robbery](../../raw/articles/2026-09-29-atcrypto-wels-2019-bitiago-office-robbery.md)
- [Vienna 2025 homicide](../../raw/articles/2026-09-29-atcrypto-vienna-2025-kuzmin-homicide.md)
- [Villach 2023 extortion](../../raw/articles/2026-09-29-atcrypto-villach-2023-fake-bka-bitcoin-extortion.md)
- [BK Cybercrime Report 2025](../../raw/papers/2026-09-29-atcrypto-bk-cybercrime-report-2025.md)
- [Watchlist Internet: FinanzOnline crypto phishing](../../raw/articles/2026-09-29-atcrypto-watchlist-finanzonline-crypto-phishing.md)
- [Watchlist Internet: Bitpanda and Coinbase phishing](../../raw/articles/2026-09-29-atcrypto-watchlist-bitpanda-coinbase-phishing.md)
- [Bitpanda breach claim denied](../../raw/articles/2026-09-29-atcrypto-bitpanda-breach-claim-denied.md)
- [OGH 7 Ob 225/25a](../../raw/articles/2026-09-29-atcrypto-ogh-7ob225-25a-bitcoin-insurance.md)
- [BMI crypto-crime feature and rip-deal appeal](../../raw/articles/2026-09-29-atcrypto-bmi-ripdeal-crypto-cases.md)
- [Lopp physical-attacks list](../../raw/repos/2026-09-29-bearer-lopp-physical-attacks-dataset.md)
