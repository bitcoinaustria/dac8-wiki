---
title: "Aiken, Blumenstock, Milusheva, Smith (World Bank): Phone-data prediction of well-being across four countries, near-zero for income"
source: "https://arxiv.org/html/2602.02805"
type: papers
ingested: 2026-09-23
fetched: 2026-09-23
content_format: html
extraction_tool: web-fetch
tags: [adverse-evidence, mobile-phone-metadata, income-prediction, cross-country-replication, population-heterogeneity, individual-level-accuracy]
summary: "A multi-country replication finds that phone metadata predicts an asset index only moderately (Pearson rho 0.20-0.59), consumption weakly and variably (0.09-0.54) and survey income essentially not at all (-0.01 to 0.03), with accuracy driven by sample heterogeneity."
---

# Predicting Well-Being with Mobile Phone Data: Evidence from Four Countries

Emily Aiken, Joshua E. Blumenstock, Sveta Milusheva, M. Merritt Smith. arXiv:2602.02805 (HTML version inspected; funded by the World Bank Global Data Facility "Mobile Phone Data for Policy" programme). Preprint, not yet peer-reviewed. I inspected Table 1, Figures 1-2 and the Discussion (Section 3) through the HTML rendering.

Data: matched survey-plus-phone-metadata samples in Afghanistan (n=528, rural Balkh), Côte d'Ivoire (n=773, national), Malawi (n=5,469, five largest cities) and Togo (n=4,345, national). About 2,000 features were derived per subscriber from calls, mobility, airtime recharges, mobile money and data usage. Models were LASSO, random forest and gradient boosting, with results reported on held-out test sets (Pearson rho).

Figures (Figure 1A): asset index rho = 0.20 (Afghanistan), 0.42 (Malawi), 0.44 (Côte d'Ivoire), 0.59 (Togo). Multidimensional poverty 0.29-0.57. Consumption 0.09-0.54. **Income -0.01 to 0.03**. Food security 0.04-0.17. Mental health 0.01-0.23. Transaction-type feature subsets alone predict the asset index less well than all data: mobile money 0.06-0.33, airtime recharges 0.09-0.32 (Figure 1B). Accuracy improves quickly up to about 1,000-2,000 training respondents and keeps rising to at least 4,500 (Figure 2A). Restricting to urban-only or rural-only subsamples lowers rho from 0.44-0.60 (national) to 0.33-0.51 (urban) and 0.32-0.37 (rural) (Figure 2B). The authors conclude that performance "depends largely on the heterogeneity of the target population", and that much predictive power comes from separating broad groups (e.g. rural and urban), not from fine within-group distinctions. They note that there is only one survey wave per country, so temporal decay and model drift cannot be assessed.

Limits for the thesis: across countries, behavioural transaction metadata recovers stock-like wealth proxies only moderately. It recovers flow income essentially not at all, and it degrades within homogeneous subpopulations, which is exactly where individual distinctions matter. Transaction-type features alone (mobile money, top-ups) are weak predictors. The paper does NOT show that phone data is uninformative. Asset-index correlations of about 0.4-0.6 remain useful for coarse ranking, poverty mapping or aggregate targeting. It also does not test European financial or crypto-asset data. Note: the income figure was extracted by a summarising fetch tool, and the precise income variable definition was not verified in the text.
