---
title: "AU10TIX: identity-verification admin credentials exposed for over a year (2024 reporting)"
source: "https://www.404media.co/id-verification-service-for-tiktok-uber-x-exposed-driver-licenses-au10tix/"
type: articles
ingested: 2026-09-29
fetched: 2026-09-29
content_format: html
confidence: medium
tags: [kyc-provider, identity-verification, credential-exposure, infostealer, coinbase, media-report]
summary: "Investigative report: an ID-verification vendor used by major platforms, including Coinbase, left admin credentials to a log platform with ID-document data exposed for more than a year; the company reported no evidence of exploitation."
---

# AU10TIX credential exposure

Source digest. Joseph Cox, 404 Media, 26 June 2024; only the introduction is outside the paywall. Details from the secondary account in [Malwarebytes, 27 June 2024](https://www.malwarebytes.com/blog/news/2024/06/driving-licences-and-other-official-documents-leaked-by-authentication-service-used-by-uber-tiktok-x-and-more). No first-party AU10TIX incident page was retrieved.

According to the reports, infostealer malware harvested an AU10TIX staff member's credentials, which were then posted to Telegram. The credentials stayed valid for more than a year. They gave access to a logging platform showing verification subjects' name, date of birth, nationality, ID number and document type, with links to document images. Named current or former clients include TikTok, Uber, X, PayPal, LinkedIn and Coinbase. Malwarebytes quotes AU10TIX: "While PII data was potentially accessible, based on our current findings, we see no evidence that such data has been exploited."

Evidence class: investigative journalism plus a company statement relayed by a security vendor. There is no regulator or court finding and no documented misuse.

DAC8 relevance: this is a general data-concentration example. Outsourced KYC can pool ID documents from many regulated firms, including a CASP, in one vendor system. It supports the controller-architecture and access-control point, not target selection or physical harm. The records described contain no holdings data.
