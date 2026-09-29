---
title: "Fractal ID: 2024 KYC-provider breach exposing identity documents, physical addresses and wallet addresses"
source: "https://web.fractal.id/fractal-id-data-breach-post-mortem/"
type: articles
ingested: 2026-09-29
fetched: 2026-09-29
content_format: html
confidence: high
tags: [kyc-provider, data-breach, insider-credentials, wallet-address, identity-documents, eu, primary-disclosure]
summary: "Berlin-based web3 KYC provider reports theft of about 6,300 users' KYC records, which could include ID images, physical and wallet addresses, through a compromised admin account; an external forensic firm confirmed the scope and a ransom demand followed."
---

# Fractal ID KYC breach (July 2024)

Source digest. Two first-party posts, retrieved from Wayback Machine captures because the domain no longer resolves:

- "Fractal ID Data Breach Post Mortem", 19 July 2024 ([capture of 26 July 2024](http://web.archive.org/web/20240726003733/https://web.fractal.id/fractal-id-data-breach-post-mortem/)). Locators: "tl;dr", "Incident and response", "Who was affected and what data was compromised", "What we will do to protect customers".
- "Fractal ID Data Breach: External Confirmation of the Impact", 13 August 2024 ([capture of 15 August 2024](http://web.archive.org/web/20240815001435/https://web.fractal.id/fractal-id-data-breach-external-confirmation-of-the-impact/)). Locator: "Resonance Report Findings".

On 14 July 2024 an attacker used valid credentials of a long-serving operator with admin rights. The operator had reused credentials that were compromised in unrelated past hacks. The attacker queried a back-office API and exfiltrated records one by one for 29 minutes before being locked out. About 6,300 users (about 0.5%) were affected. Depending on the depth of verification, the data "may include names, email addresses or phone numbers, wallet addresses, physical addresses, images and pictures of any uploaded documents". Data were encrypted at rest but decrypted for display to the valid admin session. A party claiming responsibility demanded a ransom, which Fractal refused. Fractal notified data-protection authorities and filed a criminal complaint with the Berlin police cybercrime unit. It warned that the data could be sold or used by impersonators. The firm Resonance confirmed the scope and method within its 30-day log window.

This is a first-party company disclosure with an externally confirmed scope; no regulator or court finding was located. No misuse of these records against individuals is documented in the sources. The company itself notes that centrally stored KYC data leaves it in "a race between attackers and defenders".

DAC8 relevance: this incident is the closest adjacent evidence to the concern about identity-to-ledger anchors. A breach at a KYC intermediary can join identity, home address and on-chain wallet address in one record, which the existing reference articles treat as the high-persistence case. It shows that access control can fail through a single privileged account. It involves a private KYC vendor, not a CASP's DAC8 file or a tax authority. DAC8 reports contain no wallet addresses, so the wallet-address element arises only from provider-held MiCA/TFR records.
