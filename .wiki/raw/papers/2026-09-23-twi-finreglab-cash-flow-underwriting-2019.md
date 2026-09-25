---
title: "FinRegLab / Charles River Associates: Cash-flow data in credit underwriting, empirical findings (2019)"
source: "https://finreglab.org/wp-content/uploads/2023/12/FinRegLab_2019-07-25_Research-Report_The-Use-of-Cash-Flow-Data-in-Underwriting-Credit_Empirical-Research-Findings.pdf"
type: papers
ingested: 2026-09-23
fetched: 2026-09-23
content_format: pdf
extraction_tool: web-fetch
tags: [independent-evaluation, cash-flow-underwriting, credit-default-prediction, transaction-data, finreglab, model-accuracy]
summary: "Third-party evaluation of six lenders' cash-flow models finds default-prediction AUCs of only .572-.725 (one as low as .532), and it tests default ranking only, not the accuracy of income or balances derived from transactions."
---

# The Use of Cash-Flow Data in Underwriting Credit: Empirical Research Findings

FinRegLab, July 2019. The analysis was designed and run by Charles River Associates (Marsha Courchane, Arthur Baines), who were retained by FinRegLab. FinRegLab is a US non-profit research organisation. It was set up with support from Flourish, a fintech venture fund spun out of Omidyar Network, and Flourish also funded this study (inside cover). So the evaluator is independent of the data vendors and of the lenders it studied, but its funder invests in fintech. The full 2019 report PDF (text extraction, pp. 1-33) was inspected.

**Data and granularity.** Six US non-bank lenders took part: Accion, Brigit, Kabbage, LendUp, Oportun and Petal. Five of them supplied loan-level data on more than 90,000 originated loans. The sixth supplied only its own internal analysis of more than 20,000 loans, which CRA "cannot independently verify" (p. 19). The cash-flow inputs were the participants' own variables and scores. These were built from bank-account data obtained through aggregators, and also from accounting software, payment processors, pay stubs and invoices. For consumers they reached back as far as 12 months (pp. 17-18). CRA saw the derived variables and scores, not item-level transactions. The data could not be pooled across lenders (p. 19).

**Target and figures.** The target was default or delinquency on small, short-term consumer and small-business loans, measured with logit models and ROC AUC (p. 20). Cash-flow-only models reached AUCs of **.592 to .725** at four participants and **.572** at a fifth, where there were few delinquent loans (p. 25). At one participant, cash-flow models scored .675 and .688, traditional FICO plus bureau attributes scored .720, and the combined model scored .758 (p. 27). The sixth participant's cash-flow ability-to-repay metric reached an AUC of **.532**, against .513 for a debt-to-income ratio. The report says their "closeness to .5 does not suggest ... a robust ability to predict delinquency" (p. 28). Income was only used to benchmark who the lenders serve. Participants' income metrics were compared with Census zip-code medians, and the report warns that these metrics "may differ from the Census benchmarks" and "may tend to underestimate borrowers' actual income levels" (p. 31). Stated limits: the sample sizes are modest. Pricing, downturns and larger or longer loans were not tested. "One should be cautious in extrapolating these results" (pp. 5, 33).

**Relevance to DAC8.** The report shows that, in independent testing, variables derived from transactions rank short-term default risk only moderately: AUCs of about .53-.73 on a 0.5-1.0 scale. It is also the only independent evaluation of this kind the authors knew of (p. 5). It does **not** measure how accurately transactions estimate a person's income, balances or wealth. The evaluators even flag that the lenders' income figures may understate true income. It also used lender-built features from up to 12 months of bank data, not annual per-asset aggregates. So it gives no basis for any accuracy claim about inferring income or wealth from DAC8-style annual totals (amount, units and transaction count per asset and category).
