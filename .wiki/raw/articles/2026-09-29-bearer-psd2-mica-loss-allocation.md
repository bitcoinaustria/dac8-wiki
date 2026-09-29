---
title: "PSD2 unauthorised-payment refund rules versus MiCA custodial liability: loss allocation contrast"
source: "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32015L2366"
type: articles
ingested: 2026-09-29
fetched: 2026-09-29
content_format: html
confidence: high
tags: [psd2, mica, unauthorised-payment, refund, irrevocability, custody-liability, self-custody, enacted-law]
summary: "Enacted EU law: PSD2 requires next-business-day refunds of unauthorised payments, limits payer liability to EUR 50 absent fraud or gross negligence, and protects bank payers. MiCA Article 75(8) makes custodians liable for attributable losses. No equivalent rule covers self-custodied crypto, and coerced payments are 'authorised' under both regimes."
---

# PSD2 and MiCA loss allocation

Source digest. Directive (EU) 2015/2366 (PSD2), text retrieved from EUR-Lex through a text-rendering proxy: Articles 64, 71, 72, 73, 74 and 80. Regulation (EU) 2023/1114 (MiCA), [signed Council text PE-54-2022-REV-1](https://data.consilium.europa.eu/doc/document/PE-54-2022-REV-1/en/pdf): Article 75(8).

**PSD2.**

- **Article 64(1)–(2):** a payment is authorised only with the payer's consent; without consent it is unauthorised.
- **Article 71(1):** rectification requires notification without undue delay, and at most 13 months after the debit.
- **Article 72:** the provider bears the burden of proving authentication; recorded use of an instrument is not necessarily sufficient proof of authorisation.
- **Article 73(1):** for an unauthorised transaction the payer's provider "refunds the payer ... immediately, and in any event no later than by the end of the following business day", unless it has reasonable grounds to suspect fraud and reports them in writing to the national authority.
- **Article 74(1):** the payer's liability for a lost, stolen or misappropriated instrument is capped at EUR 50, unless the payer acted fraudulently or with intent or gross negligence breached Article 69 duties. Under Article 74(3), after notification the payer bears no loss.
- **Article 80(1):** a payment order is irrevocable once received by the payer's provider.

**MiCA Article 75(8).** Custodial CASPs "shall be liable to their clients for the loss of any crypto-assets or of the means of access to the crypto-assets as a result of an incident that is attributable to them". Liability is capped at market value at the time of loss. Incidents occurring independently of the service, including problems inherent in the ledger, are excluded.

This is enacted law. What follows is a legal inference by this digest, not a holding.

1. For bank or e-money accounts, EU law gives the victim of an unauthorised payment a fast statutory refund claim against an identifiable, supervised provider. Credential theft through a leak therefore usually ends in a refund dispute, not a final loss.
2. For custodied crypto, MiCA offers a narrower route: provider liability for losses attributable to the provider.
3. Assets held by the owner (self-custody) have no counterparty. Nothing in either instrument gives the owner a refund or recall right against anyone, so possession of the key is decisive.

Limits:

- A transfer made under physical coercion is arguably "authorised" by the payer. On that reading Article 73 would not cover it, and the bank/crypto contrast narrows for wrench attacks. Instead, the practical differences are bank-side limits, delays, fraud monitoring and freeze/recall channels (see `raw/papers/2026-09-29-bearer-fbi-ic3-2025-report.md`). No case law was checked on duress and PSD2 authorisation.
- Whether a given crypto-asset (e.g. an e-money token) falls within PSD2 "funds" was not analysed.
- The Payment Services Regulation proposal was not checked for its current status.
