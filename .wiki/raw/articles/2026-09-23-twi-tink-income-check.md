---
title: "Tink: Income Check — classified income statistics from PSD2 bank transactions"
source: "https://tink.com/products/income-check/"
type: articles
ingested: 2026-09-23
fetched: 2026-09-23
content_format: html
extraction_tool: web-fetch
tags: [vendor-documentation, open-banking, psd2, income-verification, affordability, tink]
summary: "Tink Income Check classifies income streams from 3–12 months of item-level PSD2 bank transactions and reports per-stream total, mean, median, min and max; the vendor states process metrics but no income-estimation accuracy."
---

# Tink: Income Check — classified income statistics from PSD2 bank transactions

Inspected on 2026-09-23: the Tink product page for Income Check (https://tink.com/products/income-check/). The Tink developer documentation pages (docs.tink.com, "Introduction to Income Check") were attempted but rendered no readable content through the fetch tool, so this record rests on the product page, which is marketing-oriented.

**Inputs and granularity.** The end user authenticates to their bank through Tink's PSD2 account-information connection (vendor states 3,000+ connections in 19 European countries). Income Check analyses 3 to 12 months of item-level account transactions. Income is identified by proprietary classification models that use each money stream's "label, recurrence, date, size and stability" — i.e. transaction descriptions and timing, not only amounts.

**Outputs.** The report (JSON or PDF) contains account-holder details (name, IBAN, institution, and in some markets a national identity number) and, per classified income category (e.g. salary, pension, benefits), the total, maximum, minimum, mean and median amounts, with the underlying individual transactions visible per category.

**Vendor-stated claims and intended use.** The vendor states process outcomes — 20–40% fewer application drop-outs, up to 70% less first-party fraud, application handling in under ten minutes — but no accuracy or error rate for the income figures themselves. Intended uses are loan applications, affordability assessment, risk decisioning and onboarding, mainly by Northern European lenders.

**What this establishes.** A European open-banking provider sells income verification derived from bank transactions, and its output is itself a small set of summary statistics (totals, means, medians per stream). It does not establish independent accuracy, and the classification step depends on descriptions, recurrence patterns and dates of individual transactions within a single bank account known to be the applicant's — information absent from annual DAC8 aggregates of crypto-asset disposals and acquisitions.
