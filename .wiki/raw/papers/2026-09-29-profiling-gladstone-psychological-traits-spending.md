---
title: "Gladstone, Matz & Lemaire: Can psychological traits be inferred from spending? Evidence from transaction data"
source: "https://doi.org/10.1177/0956797619849435"
type: papers
ingested: 2026-09-29
fetched: 2026-09-29
content_format: pdf
extraction_tool: pdftotext
confidence: high
tags: [peer-reviewed, trait-inference, personality, card-transactions, bank-transactions, profiling, modest-accuracy]
summary: "Random-forest models on two million bank and card records of 2,193 UK money-app users predict personality only modestly (Big Five r = .15) but materialism better (r = .33); spending beats age and gender, accuracy is fairly stable across income groups, and the authors flag targeting of vulnerable people. A 2021 follow-up on 1,306 bank customers found similar limits."
---

# Can psychological traits be inferred from spending?

Joe J. Gladstone, Sandra C. Matz, Alain Lemaire, *Psychological Science* 30(7): 1087–1096 (2019). The accepted manuscript was read in full (UCL Discovery 10076117).

**Data.** The data were collected in May 2017 with a UK money-management app that aggregates users' bank and card accounts. 2,193 users took a survey and consented to linkage with their transactions, about two million records. Purchases were grouped into 279 broad spending categories, and 658 identifiable merchants were used for topic features. The targets were the Big Five personality traits (BFI-10), materialism and self-control.

**Accuracy.** In 10-fold cross-validated random-forest models the mean correlation between predicted and actual scores was .19 across all traits. Openness was lowest (r = .12) and materialism highest (r = .33; corrected ρ = .42). The narrow traits averaged r = .30 and the Big Five r = .15. Age and gender alone gave r = .11; combined with spending, r = .20 (ρ = .27). Accuracy rose with more data (1 month r = .15; 6 months r = .19). Sociodemographic moderators explained under 1% of prediction error (adjusted R² = .004). Only postcode deprivation reached significance: people in more deprived areas were harder to predict. Example associations: Openness with flights, Extraversion with dining and drinking, Agreeableness with donations, materialism negatively with donations. Spending predictions were much weaker than those from Facebook Likes (Fig. 2). The authors warn that firms could target people low in self-control with persuasive advertising for gambling or similar products.

**Corroboration (abstract only).** Tovanich, Centellegher, Bennacer Seghouani, Gladstone, Matz and Lepri, *EPJ Data Science* 10 (2021), doi:10.1140/epjds/s13688-021-00281-y, used transaction records of 1,306 bank customers and added temporal and category-dynamics features. Per the abstract, which is the only part read (the full text was not accessible to the fetch tool), inference "is a challenging task". Materialism and self-control were inferred with relatively high accuracy, and among the Big Five only Extraversion and Neuroticism reached reasonable performance.

**Evidence class and DAC8 transfer.** Peer-reviewed and consent-based, with honest reporting of modest effect sizes. It shows that item-level, merchant-categorised spending supports statistical inference of dispositional traits, but with considerable individual error. The correlations shown here are far from reliable individual labelling. The inputs are merchant categories over months, which DAC8 reports do not contain. The finding therefore bears on provider-held or open-banking records, not on the DAC8 annual aggregates.
