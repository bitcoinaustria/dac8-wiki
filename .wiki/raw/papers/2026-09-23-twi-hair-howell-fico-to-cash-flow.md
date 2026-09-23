---
title: "Hair, Howell, Johnson, Matsumoto (NBER): From FICO to cash flow, bank-statement data and small-business default"
source: "https://www.nber.org/system/files/working_papers/w33367/w33367.pdf"
type: papers
ingested: 2026-09-23
fetched: 2026-09-23
content_format: pdf
extraction_tool: web-fetch
tags: [independent-evaluation, cash-flow-underwriting, credit-default-prediction, bank-statement-data, academic-study, model-accuracy]
summary: "Academic out-of-sample test finds that 3-6 months of bank-statement variables raise small-business default-prediction AUC only from 0.608 to about 0.638 for young owners, and that a cash-flow-only model matches FICO at AUC 0.642; it does not test income estimation."
---

# Modernizing Access to Credit for Younger Entrepreneurs: From FICO to Cash Flow

Christopher M. Hair (BYU), Sabrina T. Howell (Harvard Business School, NBER), Mark J. Johnson (BYU) and Siena Matsumoto (UC Berkeley). NBER Working Paper 33367, January 2025, not peer-reviewed. The authors are academics. Some of the data were gathered for a FinRegLab project funded by the U.S. Department of Commerce (award MB22OBD8020266-T1-01). The lenders are anonymised, and no vendor funding is disclosed (title page). The full working paper was inspected, focusing on the data section and section 5.1.

**Data and granularity.** The data come from two fintech small-business lenders (A and B) and one loan marketplace. Lender A had 104,150 applications and 18,434 loans (2013-2024). Lender B had 58,668 applications and 25,762 loans (2015-2024). The platform had 199,300 applications (2022-2023) (pp. 13-14). The cash-flow inputs are standard variables that the Ocrolus API extracts from **business** checking-account statements. Lender A and the platform use **three months** of statements, and Lender B uses **six**. The paper notes that "industry practice is typically three months, and rarely more than six" (p. 13, fn. 17). The variables are average credits, debits and balances, the volatility of credits and balances, and counts of low or negative balances and daily-pay loans (pp. 14, 23-24). These are features derived from transactions, not raw item-level data.

**Target and figures.** The target is loan default. The models are out-of-sample random forests and OLS regressions (section 5.1). For owners aged up to 35, a baseline built on FICO has an ROC-AUC of **0.608**. Adding cash-flow variables raises it by **0.03**. For owners over 35, the baseline is **0.671** and the gain is **0.008** (Table 9, p. 30). In OLS, the cash-flow variables raise R-squared by **13.8%** overall, 23% for younger owners and 11.1% for older owners (Table 10, pp. 30-31). A cash-flow model without FICO and the FICO baseline both reach an AUC of **0.642** on the full sample (Table A.17, p. 31). In approval models, the AUC rises from 0.803 to 0.816 (pp. 22-23). Stated limits: the study covers fintech lenders and small-business loans only, and default is observed only for the two lenders, not for the platform. The authors "do not interpret this result to imply that cash flow data dominate FICO" (p. 31).

**Relevance to DAC8.** This is independent academic confirmation that bank-account flow data carry real but weak signals about repayment. Default-prediction AUCs are around 0.61-0.67, even with purpose-built balance and volatility features. The paper does **not** test whether transactions estimate income, revenue or wealth correctly against a verified benchmark. It uses short windows of 3-6 months of business-account statements, not annual per-person reports. So it gives no error rate for inferring a person's income or wealth from annual per-asset totals such as DAC8 amounts, units and transaction counts. If anything, it shows that richer, balance-level data still predict individual outcomes only modestly.
