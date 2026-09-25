---
title: "Baker & Kueng (NBER): Household financial transaction data, review of uses and measurement limits"
source: "https://www.nber.org/system/files/working_papers/w29027/w29027.pdf"
type: papers
ingested: 2026-09-23
fetched: 2026-09-23
content_format: pdf
extraction_tool: web-fetch
tags: [independent-evaluation, transaction-data, measurement-error, income-measurement, academic-review, data-completeness]
summary: "Academic review states that researchers 'can never be certain' they observe all of a person's accounts, which makes raw income and spending levels in transaction data hard to interpret, and it reports no validated error rate for income measured from transactions."
---

# Household Financial Transaction Data

Scott R. Baker (Kellogg School of Management, Northwestern; NBER) and Lorenz Kueng (Kellogg School of Management, Northwestern; NBER, as listed in the paper). NBER Working Paper 29027, July 2021, a review article that is not peer-reviewed at the NBER stage. The authors are academics, and no vendor funding is disclosed. The full working paper was inspected, focusing on section 3.2 (disadvantages).

**Data and granularity.** The paper reviews research that uses item-level household transaction data from banks, fintech and aggregator apps, and payment intermediaries. Examples include Meniga in Iceland and US bank and aggregator panels. It notes that income can be identified from "regular direct deposit paychecks or social security income", and that balances can be "partially imputed" from interest income when balance data are missing (section 2, p. 6). Its main advantage, in the authors' words, is that income and assets are exact at the level of each transaction, not recalled in a survey.

**Stated limits.** The first limit is account completeness: "a researcher can never be certain that they are observing all relevant financial accounts owned by an individual or a household". Researchers therefore drop users with few transactions, "no visible sources of income", or transfers to unlinked accounts, and "such ambiguity may make it difficult to interpret the raw levels of income and spending" (section 3.2.1, pp. 9-10). The second is sample selection: the unbanked and people who mostly use cash are missing, and app-based samples are skewed. Baker (2018) is cited for the claim that reweighting can "mostly" resolve this, but only for aggregate analysis (section 3.2.2, pp. 10-11). The third is categorisation: cash, checks and peer-to-peer transfers can be seen only partly or not at all. Categories are assigned by the data owner's algorithms, and "miscategorizations may occur" (section 3.2.3, pp. 11-12). The review gives **no quantitative error figure** for income or wealth derived from transactions against tax or payroll records.

**Relevance to DAC8.** The review supports the view that even complete item-level bank transaction data give income and balance levels that are uncertain for each person. Unobserved accounts, cash, and the classification of payments can all distort them, and the research literature handles this by excluding users or reweighting samples, not by validating individuals. It does **not** give an error rate. It also concerns bank transaction streams, not annual crypto-asset aggregates. DAC8 reports (amount, units and transaction count per asset and category) cover even less of a person's finances. So these completeness problems apply to them at least as strongly when anyone tries to infer income or wealth from them.
