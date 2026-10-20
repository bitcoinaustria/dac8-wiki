---
title: "Website Arguments Page: Claim Map and Publication Boundaries"
type: report
status: draft
sources:
  - wiki/topics/privacy-financial-privacy-and-surveillance.md
  - wiki/references/surveillance-autonomy-and-democratic-safeguards.md
  - wiki/references/dac8-vs-dac2-distinguishing-arguments.md
  - wiki/references/dac8-equality-and-technology-neutrality.md
  - wiki/references/austria-eu-precedent-matrix.md
  - wiki/references/identity-to-public-ledger-linkage-evidence.md
  - wiki/references/tax-exchange-confidentiality-and-suspension.md
  - wiki/references/dac8-physical-risk-causation.md
  - wiki/references/dac8-transaction-granularity-and-reporting-layers.md
  - wiki/references/bearer-asset-irreversibility-and-leak-consequences.md
  - wiki/references/dac8-member-state-implementation-comparators.md
  - wiki/references/financial-data-composition-and-attribution-error.md
  - wiki/references/dac8-field-necessity-and-alternatives.md
  - wiki/references/dac8-data-lifecycle-access-retention-remedies.md
  - wiki/references/dac-history-timeline.md
generated: 2026-10-20
created: 2026-10-20
updated: 2026-10-20
tags: [campaign-copy, claim-map, privacy, dac8, website, editorial-evidence]
summary: "Maps every reason, objection and demand on the dac8.org arguments page to its sources and publication boundary; flags three claims for the campaign lawyer and three sources verified outside the wiki but not yet ingested."
---

# Website Arguments Page: Claim Map and Publication Boundaries

Working research note, 20 October 2026; not legal advice. This maps the page data in `src/data/arguments.ts` on the dac8.org branch `t3/privacy-arguments` (head `a8be730`, pull request 70). German and English carry the same claims; the claims below follow the English text.

Markers: **Lawyer** means clear the wording with the campaign lawyer before publication. **Gap** means the wiki holds no verified record yet. **Recheck** means the source could not be re-fetched on 20 October 2026.

## Departures from the 17 October draft

By editorial decision, the page does not reuse two examples from the [17 October campaign copy](report-privacy-campaign-copy-2026-10-17.md):

- the FCA example of domestic financial abuse (old argument 2, confidential help);
- the Festic et al. Swiss monitoring experiment (old argument 3, room to think).

They are replaced by evidence from Austria, Germany and Switzerland and by bitcoin-specific sources:

- the 1983 German census judgment's passage on chilling effects;
- the Austrian money-laundering report, Austrian phishing campaigns and an Austrian disciplinary decision;
- the Austrian account register and German bailiffs' account lookups;
- the Waltio, Ledger, Fractal ID and Trezor leaks.

Two foreign cases that readers may know, WikiLeaks and Canada, carry the point about political misuse. The dropped sources remain valid in the wiki; this is an editorial choice, not a correction.

Some arguments are retained in changed form:

- the provider-leak argument, now split into "target lists" and "the file grows thicker";
- "a profile is not proof", now inside "pseudonymous is not anonymous" and sourced to Möser and Narayanan instead of ONS;
- the replies to "nothing to hide", crime and encryption;
- the governance demands.

DAC8-specific reasons replace the old optional DAC8 bridge.

## Editorial evidence notes

### Reasons

| Reason | Claim | Sources | Publication boundary |
|---|---|---|---|
| privat | Privacy means deciding who knows what about you; at the till nobody asks your name. | [Hughes 1993](../raw/articles/2026-10-20-hughes-cypherpunk-manifesto-1993.md) | Advocacy, not evidence. Holds for everyday purchases; large cash dealings carry identification duties. The clause "a movement … in whose tradition bitcoin stands" is unsourced; the manifesto does not mention bitcoin. |
| privat | 1983: a legal order in which citizens cannot know who knows what about them is incompatible with informational self-determination. | [BVerfG, Rn. 146](../raw/articles/2026-10-20-bverfg-1983-volkszaehlungsurteil.md) | German law. Rn. 148 says the right is not unlimited, and [BFH IX R 36/21](../raw/articles/2026-08-27-germany-bfh-ix-r-36-21-crs.md) upheld CRS exchange under it. Never imply that German courts reject automatic tax exchange. The page number 43 was not rechecked. |
| privat | Data protection is a constitutional right in Austria; interference only "in der gelindesten, zum Ziel führenden Art". | [§ 1 DSG](../raw/articles/2026-08-30-austria-dsg-section-1-fundamental-right.md) | Accurate. Does not by itself decide DAC8's proportionality. |
| alle | Moving bitcoin through a provider stores who pays whom. The EU transfer-of-funds regulation requires names and wallet addresses, also for own wallets, kept for years for every customer. | [TFR](../raw/articles/2026-08-27-eu-tfr-regulation-2023-1113.md); [FM-GwG § 21](../raw/articles/2026-08-27-austria-fm-gwg-current-crypto.md) | These are AML records kept by the provider, not part of the DAC8 report. Ten years under the current FM-GwG; the future AMLR baseline is five years plus extensions. |
| alle | Single payments can reveal beliefs and health; the annual report carries only totals, while the provider holds every payment. | [EDPB 06/2020 §5.1](../raw/articles/2026-09-23-twi-edpb-psd2-transaction-inference.md) | Keep "can". Never attach the donation or medical examples to DAC8 annual totals. |
| alle | WikiLeaks, 2010: Visa, Mastercard and PayPal blocked donations without a court order. | [Bridy, pp. 1524–1525](../raw/papers/2026-10-20-bridy-internet-payment-blockades.md) | Secondary scholarship. Government pressure is the author's characterisation, not a finding. Payment processing was blocked; no donor accounts or donor data were involved. |
| alle | Canada, 2022: about 280 accounts, cards and credit lines frozen; banks had to pass information about the customers concerned to the police; courts in 2024 and 2026, not yet finally, held that this sharing breached the protection against unreasonable search. | [Parliamentary report, pp. 62–64](../raw/papers/2026-10-20-canada-dedc-report-financial-measures.md); [FINA evidence](../raw/articles/2026-10-20-canada-fina-frozen-accounts-testimony.md); [2024 FC 42 §§334, 341, 359](../raw/articles/2026-10-20-canada-2024-fc-42-emergencies-act.md); [2026 FCA 6 §§416, 451–474](../raw/articles/2026-10-20-canada-2026-fca-6-emergencies-act-appeal.md) | The disclosure duty covered designated persons, not all customers. Donors' names never went to banks, and small donors were not frozen unless they were in the protest zone. The appeal court held that freezing alone was not a seizure, so say the sharing, not the freezing, breached the Charter. Supreme Court leave (docket 42261) is pending. The page links the official appeal-court page. |
| alle | Surveillance works without a leak: people unsure whether they are recorded try not to stand out (1983). | [BVerfG, Rn. 146](../raw/articles/2026-10-20-bverfg-1983-volkszaehlungsurteil.md) | Constitutional reasoning, not a measurement. Replaces the Festic experiment. |
| selbstverwahrung | Bitcoin was designed in 2008 as electronic cash between people without a bank; whoever holds the keys can transfer without anyone's approval. | [Whitepaper abstract and section 2](../raw/articles/2026-10-20-nakamoto-whitepaper-abstract-transfer-model.md) | Design intent. Not legal equivalence to cash and not a security claim. |
| selbstverwahrung | Like cash, bitcoin draws criminals, remote and in person; the danger is data stores that identify people, not your own wallet. | [Physical risk](../wiki/references/dac8-physical-risk-causation.md); [bearer asset](../wiki/references/bearer-asset-irreversibility-and-leak-consequences.md) | The page cites only the whitepaper; the wiki supports the threat class. "Not your own wallet" is a policy framing: self-custody has its own loss risks and no refund backstop. |
| bargeld | Withdrawing bitcoin to self-custody: the annual total usually appears in the report, although the transfer triggers no tax by itself. | [Reporting layers](../wiki/references/dac8-transaction-granularity-and-reporting-layers.md); [§ 27b(3)](../raw/articles/2026-10-19-austrian-crypto-tax-boundaries.md) | The DAC8 category is "addresses not known to belong to a provider or financial institution", not "own wallet". "No tax" is a statutory inference; fees may be separate tax events. Keep "usually". |
| bargeld | Domestic bank accounts have no such annual report: bank-account exchange covers only customers resident abroad, while DAC8 also covers customers at home. | [Domestic scope](../raw/articles/2026-10-20-dac8-domestic-scope-versus-gmsg.md); [Kapitalabfluss-Meldegesetz](../raw/articles/2026-10-20-austria-kapitalabfluss-meldegesetz-expiry.md) | **Lawyer.** Correct for automatic exchange today: GMSG § 91 Z 1 covers other states only, while Krypto-MPfG § 14(1) Z 1 includes Austria. But banks reported outflows of EUR 50,000 or more, including cash withdrawals, from March 2015 to December 2022, and the account register exists. Never say banks never reported withdrawals. "Abroad" means another participating state. The domestic scope is required by DAC8 (recital 13 speaks of transactions), not Austrian gold-plating. |
| bargeld | The wallet address is not in the report, only the total; in the wrong hands the report still shows who probably keeps savings in self-custody. | [Art. 8ad](../raw/articles/2026-08-27-dac8-article-8ad-reporting-and-routing.md) | No DAC8 data have leaked. Outgoing totals can also be payments to other people, so "probably" must stay. |
| pseudonym | The blockchain lists payments under wallet addresses; if a leak shows which addresses are yours, past and future payments can be traced to you. | [Whitepaper section 10](../raw/articles/2026-09-29-acctmodel-bitcoin-whitepaper-privacy.md); [ledger linkage](../wiki/references/identity-to-public-ledger-linkage-evidence.md) | "Future" applies to reused or linkable addresses, not to every new address. "Forgets nothing" paraphrases persistence; do not say every address reveals a wallet. |
| pseudonym | At Fractal ID in Berlin, ID documents, home addresses and wallet addresses sat in one record until attackers copied it. | [Fractal ID](../raw/articles/2026-09-29-bearer-fractal-id-kyc-breach.md) | An identity-check provider's leak. No attack or tax data is attributed to it. |
| pseudonym | A named address plus information about recipients allows inferences about purchases, donations and relationships. | [Goldfeder 2018](../raw/papers/2026-09-04-goldfeder-cookie-blockchain-popets-2018.md) | Studied in a web-payment setting; needs labelled recipients. |
| pseudonym | Grouping addresses rests on assumptions; one wrong one can merge different people's payments. | [Möser and Narayanan](../raw/papers/2026-09-04-moeser-narayanan-bitcoin-clustering-fc-2022.md) | Correct. The right to correct errors is a policy demand. |
| zielliste | Suspected crypto wealth alone can lead to robbery and kidnapping, whether or not the presumed holdings are real; data at providers, service providers and authorities can give offenders a starting point. | [Physical risk](../wiki/references/dac8-physical-risk-causation.md) | Keep "can". No leak from DAC8 or an Austrian authority is linked to an attack. |
| zielliste | Sums and counts give a rough, possibly far-off estimate of money moved; whoever steals them still filters out people who look wealthy. | [Wealth inference](../wiki/theses/transaction-data-wealth-inference.md); [criminal markets](../wiki/references/criminal-data-markets-and-repeat-victimisation.md) | The second sentence is inferred from the targeting of high balances in other datasets. No DAC8 data have been stolen. |
| zielliste | Waltio leaked customers' emails, gains and losses and year-end balances; French police call the leak one reason for the rise; offenders pick victims and sometimes misjudge holdings. | [Waltio](../raw/articles/2026-08-27-waltio-security-incident.md); [Gendinfo digest](../raw/articles/2026-09-19-gendarmerie-waltio-target-selection.md); [wording](../raw/articles/2026-10-20-gendinfo-pegeot-attribution-precision.md) | "One reason" mirrors „notamment“; never "the reason", and never causation in a specific case. **Recheck.** Waltio is a private tax tool, not an authority. |
| zielliste | Ledger, 2020: names, postal addresses and phone numbers of about 272,000 buyers leaked, a list of people who probably self-custody. | [Ledger](../raw/articles/2026-09-29-bearer-ledger-2020-leak-ceo-disclosure.md); [postal boundary](../raw/articles/2026-10-19-ledger-postal-phishing-boundary.md) | Ledger said the list could not be linked to funds. Do not tie later postal phishing to these addresses. |
| zielliste | Fake FinanzOnline messages ask about crypto holdings; an SMS scam sent at random also asks about gold and cash. | [Watchlist Internet](../raw/articles/2026-09-29-atcrypto-watchlist-finanzonline-crypto-phishing.md) | Shows the pretext risk without any official data. Watchlist is a consumer platform. |
| akte | From 2036, about ten annual reports are always on file with the provider. | [§ 20 retention](../raw/articles/2026-08-27-krypto-mpfg-section-20-retention.md) | Deletion runs ten years after the end of each reporting period, so roughly ten are on file at any time. |
| akte | The provider prepares reporting data for all customers, beyond the directive; Germany and the Netherlands do so only for reported customers. | [Comparators](../wiki/references/dac8-member-state-implementation-comparators.md); [EB RV 306](../raw/articles/2026-09-10-erlrv-306-section-20-no-directive-basis.md) | DAC8 still requires status checks for every customer; the excess is the full § 18 profile. |
| akte | Ten years "aus Vereinfachungsgründen", against five years for bank-account reports and generally six in Ireland. | [EB RV 306](../raw/articles/2026-09-10-erlrv-306-section-20-no-directive-basis.md); [GMSG § 5](../raw/articles/2026-09-04-austria-gmsg-section-5-processing-retention.md); [Ireland](../raw/articles/2026-09-04-ireland-dac8-si-584-2025-retention-copy.md) | This raises a rational-ground question, not proof of invalidity. DAC8 allows five to ten years for provider records. |
| akte | Whether data is deleted when the period ends must be taken on trust: Trezor's shipping provider leaked 2019–2021 orders despite repeated written confirmations of deletion. | [Trezor](../raw/articles/2026-10-15-scam-trezor-shipmonk-retention.md) | First-party account. The deletion assurance came from a vendor; this was not statutory retention. |
| akte | Under AML rules the provider keeps ID, wallet addresses and transactions up to ten years after the relationship ends; DAC8 adds the tax number and tax residence; the tax office receives the reports from all providers (residents of Germany: the German tax office). | [FM-GwG](../raw/articles/2026-08-27-austria-fm-gwg-current-crypto.md); [Art. 8ad](../raw/articles/2026-08-27-dac8-article-8ad-reporting-and-routing.md) | Keep provider records separate from tax reports. "Currently" must stay. |
| akte | Bulgaria, 2019: data on more than six million people leaked from the tax authority; according to the OECD, this included exchanged account data. | [C-340/21 para. 12](../raw/articles/2026-10-20-cjeu-c340-21-para-12-affected-persons.md); [OECD](../raw/articles/2026-10-20-oecd-global-forum-bulgaria-breach-statement.md) | The breach was in the receiving authority's own systems, not the transmission channel. Six million counts all affected people, not only those with exchanged data. It concerned CRS/DAC2, not DAC8. Swiss exchange with Bulgaria resumed in 2023. |
| akte | Reports across providers and years, a tax-tool leak and attributable chain data can combine into a profile. | [Composition](../wiki/references/financial-data-composition-and-attribution-error.md) | A mechanism, not a measured rate. DAC8 reports contain no addresses. |
| anlasslos | Whoever buys through an exchange, broker or app is reported without suspicion; whoever buys person to person or is paid in bitcoin for goods and work is not in the report, and neither is suspect. | [Reporting layers](../wiki/references/dac8-transaction-granularity-and-reporting-layers.md) | Correct: DAC8 attaches to the reporting provider, not to suspicion. Never present the provider route as the honest one or other routes as evasion. A later sale through a provider can still be reported. |
| anlasslos | VfGH, 2014: retention hit "fast ausschließlich Personen, die keinerlei Anlass … gegeben haben". | [VfGH G 47/2012 ua](../raw/articles/2026-08-27-vfgh-data-retention-final-decision-full-de.md), Rz 183, checked against the legal-docs copy | The case concerned telecoms data. E 2097/2021 rejected the suspicionless-reporting argument for DAC2. |
| anlasslos | FIU, 2024: 11,111 reports, 1,228 of them from crypto providers; 8,138 led nowhere and are kept up to five years. | [A-FIU 2024](../raw/papers/2026-09-29-amlfail-a-fiu-lagebericht-geldwaesche-2024.md) | **Gap:** the five-year retention (report p. 17) was verified on 20 October 2026 but is not in the wiki record. These are AML reports, not DAC8. |
| anlasslos | Criminals open accounts with forged Austrian passports carrying real people's data. | [A-FIU 2024](../raw/papers/2026-09-29-amlfail-a-fiu-lagebericht-geldwaesche-2024.md); [NRA 2025](../raw/papers/2026-09-29-atkyc-nra-2025-forged-documents-remote-id.md) | Correct as stated. |
| anlasslos | The Commission estimated up to EUR 2.4 billion a year, scaled from bitcoin gains, without knowing how much was already taxed. | [Impact assessment](../raw/articles/2026-08-30-dac8-impact-assessment-evidence-and-options.md) | **Gap:** EUR 2.4 billion and Annex 4 (pp. 66–68) were verified on 20 October 2026 against Council document ST-15829-2022-ADD-2 but are not in the wiki. The wiki records EUR 3.6 billion of realised gains at 25 percent, and the Austrian impact assessment (WFA) cites EUR 1.7 billion. |
| zweck | Since DAC8, the directive allows all exchanged tax data, including bank-account data, to be used against money laundering and for EU sanctions. | [DAC history](../wiki/references/dac-history-timeline.md); [EU-AHG § 15](../raw/articles/2026-09-30-at-euahg-purpose-implementation.md) | A permission in EU law. Austria's EU-AHG § 15 does not reproduce the sanctions permission, and actual use is unproven. |
| zweck | The account register was created in 2015 by the act that loosened bank secrecy; since July 2026 the anti-fraud office uses it as well. | [BGBl I 116/2015](../raw/articles/2026-09-30-at-bgbl-i-116-2015-gmsg-kontregg-bwg.md); [BGBl I 46/2026](../raw/articles/2026-09-29-refresh-austria-kontregg-bgbl-i-46-2026.md) | Correct. The register shows that accounts exist, not balances. |
| zweck | German bailiffs looked up accounts 61,760 times in 2013 and 844,427 times in 2023. | Bundestag Drucksache 20/10841, answer 6, p. 6 (linked from the page) | **Gap:** verified on 20 October 2026 but not in the wiki. The counting method changed, so compare users rather than totals. |
| zweck | By 2029, account registers will be connected EU-wide and will include crypto accounts, without balances. | [AMLD6 registers](../raw/articles/2026-08-27-eu-amld6-directive-2024-1640-account-registers.md) | Future law. |

### Objections

| Objection | Answer's claim | Sources | Publication boundary |
|---|---|---|---|
| Nothing to hide | Privacy needs no justification; state interference does. | [§ 1 DSG](../raw/articles/2026-08-30-austria-dsg-section-1-fundamental-right.md) | Normative position. |
| Tax fairness | Austrian providers have withheld the tax for customers resident in Austria since 2024, but not for customers in Germany. Where tax is already withheld, the state must justify the extra annual totals. | [KESt](../raw/articles/2026-10-20-austria-crypto-kest-withholding-scope.md); [WFA](../raw/articles/2026-10-20-krypto-mpfg-wfa-revenue-estimate.md); [1948/AB](../raw/articles/2026-09-29-atrisk-ab-1948-crypto-tax-revenue-data.md); [equality](../wiki/references/dac8-equality-and-technology-neutrality.md) | **Lawyer.** (1) Applies to domestic providers and their branches only. (2) The test is unlimited tax liability (home or habitual abode in Austria), not residence abroad; the BMF says withholding "kann unterbleiben", so a German resident with an Austrian home may still be withheld from. (3) DAC8 requires domestic reporting. (4) The state will reply with reconciliation, loss offset, pre-2021 holdings, the foreign-provider gap and recital 13. (5) The WFA ties expected revenue to foreign holdings and relocation; this supports asking the question but does not prove the reports useless. |
| Crime | Whoever demands data on everyone must show the benefit and why targeted investigation does not suffice. | [Surveillance](../wiki/references/surveillance-autonomy-and-democratic-safeguards.md) | Normative. Does not deny that investigations benefit from data. |
| Encryption | Authorised insiders: an Austrian tax official made thousands of queries, more than 1,000 about people from his hometown; bribed Coinbase staff took ID images and balances. | [BMF disciplinary decision](../raw/articles/2026-09-29-atinsider-bmf-dk-2016-ais-thousands-queries.md); [Coinbase 8-K](../raw/articles/2026-09-04-coinbase-2025-data-theft-8k.md) | The disciplinary sanction was a EUR 5,000 fine. No DAC8 data were involved. |
| The court allowed it | The VfGH found balances and interest did not touch the core of private life; DAC8 reports more, including domestic customers, and keeps reports ten years instead of five; proportionality not yet decided. | [E 2097/2021](../raw/articles/2026-08-27-vfgh-e-2097-2021-dac2.md); [DAC8 vs DAC2](../wiki/references/dac8-vs-dac2-distinguishing-arguments.md) | E 2097/2021 is the strongest adverse authority. "Not decided" rests on RIS searches of 27 August 2026; recheck. The domestic scope is EU-mandated. |
| Own wallet only | No provider, no DAC8 report. Bought at a provider and transferred out: the total usually appears, without the address; the address stays with the provider. | [Reporting layers](../wiki/references/dac8-transaction-granularity-and-reporting-layers.md); [CARF wallet records](../raw/articles/2026-09-04-oecd-carf-external-wallet-address-retention.md) | Correct. Keep "usually". |
| Don't use an exchange | Privacy must not depend on avoiding the easiest route. | none | Normative. |

### Demands

| Demand | Claim | Sources | Publication boundary |
|---|---|---|---|
| No stockpiling of data | Determine reportability before preparing data; Germany and the Netherlands do so only for reported customers. | [Comparators](../wiki/references/dac8-member-state-implementation-comparators.md) | DAC8 still requires status checks for all customers. |
| Do not report transfers to your own wallet | They trigger no tax but after a leak show who probably keeps how much bitcoin at home. Austria should push in Brussels, including in the recast, "which needs unanimity" (letter). | [Reporting layers](../wiki/references/dac8-transaction-granularity-and-reporting-layers.md); [recast](../raw/articles/2026-09-30-eu-dac-future-com-2026-308-dac-recast.md); [recast status](../raw/articles/2026-09-30-eu-dac-future-dac-recast-procedural-status.md) | **Lawyer** (letter wording). Unanimity under Arts. 113 and 115 TFEU is recorded as of 30 September 2026; date it. Unanimity lets Austria block the recast, but a block leaves the existing DAC8 duty in force; removing it needs every Member State. The recast keeps the DAC8 fields in substance. Totals show money moved out, not holdings, so "probably" must stay. "No tax" is a statutory inference. |
| Collect only what taxation needs | Units and counts must be justified. | [Field necessity](../wiki/references/dac8-field-necessity-and-alternatives.md) | These fields are DAC8-mandated, so this is an EU-level demand. |
| Keep data for less time | Five years for bank reports and generally six in Ireland; "simplicity" is no reason; copies at service providers must be verifiably deleted. | as above; [Trezor](../raw/articles/2026-10-15-scam-trezor-shipmonk-retention.md) | Rational-ground question. DAC8 allows five to ten years for provider records. |
| Limit access, secure rights | Purpose limits; new purposes only by law; see your data before it is reported; correction, deletion and review. | [Lifecycle](../wiki/references/dac8-data-lifecycle-access-retention-remedies.md); [user duties](../raw/articles/2026-08-27-austria-krypto-mpfg-user-facing-duties.md) | Policy demand. The Krypto-MPfG already requires notice before the first report that a user's data are covered; the demand goes further, to seeing the content. |

### Items for the campaign lawyer

1. **Tax-fairness (KESt) objection:** the scope of withholding, the meaning of "customers in Germany", and the counterarguments listed above.
2. **Bank versus crypto domestic reporting:** the "Imagine your bank…" reason and the court objection. The GMSG and Krypto-MPfG contrast is exact. Check the wording against the Kapitalabfluss-Meldegesetz period (2015 to December 2022) and the Kontenregister.
3. **Recast unanimity line in the MPs' letter:** the procedural status date, and the point that a veto blocks the recast but does not remove DAC8.

### Sources verified outside the wiki or not rechecked

- EUR 2.4 billion Commission estimate (impact assessment, Annex 4, pp. 66–68): verified 20 October 2026, **Gap** in the wiki.
- Bundestag Drucksache 20/10841, account-lookup figures: verified 20 October 2026, **Gap** in the wiki.
- A-FIU retention of up to five years (report p. 17): verified 20 October 2026, **Gap** in the wiki.
- Gendinfo wording and job title: **Recheck**.
- The bitcoin-lineage clause in the Hughes paragraph: unsourced.

### Inventory candidates

The three gaps could become ingest candidates with the shape `{title, source, needed_for: arguments page claim, status: candidate}`. No records were created.
