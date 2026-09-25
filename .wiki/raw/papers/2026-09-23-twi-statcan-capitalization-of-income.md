---
title: "Statistics Canada: Experimental capitalization-of-income wealth imputation from tax records"
source: "https://www150.statcan.gc.ca/n1/pub/13-605-x/2025001/article/00002-eng.pdf"
type: papers
ingested: 2026-09-23
fetched: 2026-09-23
content_format: pdf
extraction_tool: web-fetch
tags: [official-statistics, capitalization-method, tax-records, record-linkage, wealth-distribution, experimental-statistics]
summary: "A national statistical office imputes household financial wealth from linked annual tax-reported investment income; the first model recovered only 44% of the national-accounts total, so recalibration and benchmarking were needed."
---

# Enhancing wealth distributions within the distributions of household economic accounts using a capitalization of income method

James Gauthier, Statistics Canada, Latest Developments in the Canadian Economic Accounts, Catalogue no. 13-605-X, released 16 July 2025. The full 11-page PDF was inspected.

Inputs: the Survey of Financial Security (SFS), which directly observes household assets, is linked to the Administrative Personal Income Masterfile (APIM). The APIM is built from Canada Revenue Agency T1 returns and T4/T4A/T5 slips, which give annual investment income per filer, with family linkages (pp. 8–9). The capitalization formula is A = I/r (p. 8). Return ratios are estimated for SFS respondents from reported investment income divided by surveyed assets. A regression, log(ratio) ~ log(income) + age + age² + region + family type, then imputes ratios to tax filers who were not sampled, including filers with no declared investment income (pp. 9–12). Real estate and liabilities are excluded, so only financial assets are estimated (p. 9).

Quantified results and errors: average return ratios are about 3% for the bottom 90% by income and 5% for the top 10%. By age, they range from 2% to 8% (Table 3, p. 11). The first model produced C$3.19 trillion of financial assets, or 44% of the National Balance Sheet total of C$7.26 trillion for Q4 2018. After recalibrating to survey proportions it reached C$5.83 trillion (80%), and it was then benchmarked to the national totals (p. 13). Estimated top wealth extends beyond C$3 billion, against less than C$60 million in the survey alone (p. 14). Shares for the top 1% / 10% / 20% are 26.6 / 65.0 / 81.2%, compared with 24.8 / 56.9 / 73.9% under the Parliamentary Budget Office's Pareto method (Table 4, p. 15). The stated limitations are the choice of rates, unrealized gains, tax-sheltered accounts, and the static nature of survey-derived ratios (pp. 8, 16).

Parallel to DAC8: this is direct official-statistics precedent for linking identity-level annual tax-reported flow totals with other records to impute individual-level wealth. The imputed microdata are used only for published distributional statistics, which are benchmarked to macro totals and labelled experimental. It is not an assessment of any individual. The method relies on survey-observed stock-to-flow ratios, i.e. ground truth for a sample. It also shows large aggregate under-coverage (44% before recalibration) even for income yields. DAC8 flows are gross trading flows rather than yields, and no comparable survey ground truth for crypto holdings is cited.
