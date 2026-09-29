---
title: "Ledger: 2020 customer-database leak, CEO disclosure and follow-on phishing"
source: "https://www.ledger.com/message-ledgers-ceo-data-leak"
type: articles
ingested: 2026-09-29
fetched: 2026-09-29
content_format: html
confidence: high
tags: [ledger, data-breach, hardware-wallet, postal-address, phishing, physical-security, primary-disclosure]
summary: "Provider disclosure of ~1M emails and ~272,000 name/postal-address/phone records of hardware-wallet buyers; acknowledges phishing and customer fear of physical attack, denies any link to wallet balances."
---

# Ledger 2020 customer-database leak

Source digest. Pascal Gauthier (CEO, Ledger), open letter dated 21 December 2020. Locators: opening paragraphs (scope), paragraph beginning "Some of you have also expressed concerns about potential physical attacks", closing paragraphs (refund refusal). Supplemented by Ledger's undated, currently maintained [phishing-campaigns status page](https://www.ledger.com/phishing-campaigns-status), section "Physical mail prompting users to scan a QR code or visit a website".

Ledger states that a July 2020 attack exfiltrated its June 2020 e-commerce database. Its July forensic review confirmed about 1 million stolen email addresses and 9,532 detailed records. A dump published on RaidForums on 20 December 2020 showed about 272,000 records with postal address, first and last name and telephone number. Ledger states the leak did not affect devices, the app or funds and that "there is no way to make any correlation between the data that has leaked and the funds on your wallet". It acknowledges email and SMS phishing seeking the 24-word recovery phrase and customers' fear of physical attack because shipping addresses leaked. Its advice anticipates coercion: PIN-wipe after three attempts, a decoy PIN and passphrase, and keeping the recovery sheet outside the home. Ledger refused refunds. The status page adds that customers received physical letters at home directing them to enter the recovery phrase.

This is a first-party company statement, not a judicial or police finding. It establishes that a leak of identity, postal address and "bought a hardware wallet" status reached the public, and that postal addresses were then used for phishing. It does not establish balances, a wallet-address link or any completed physical attack. Later reports of extortion emails threatening home invasion come from media and security vendors (e.g. [Bitdefender, 14 May 2021](https://www.bitdefender.com/en-gb/blog/hotforsecurity/threat-actors-target-ledger-data-breach-victims-in-new-extortion-campaign), which reports a later sextortion-style variant and no payments to the listed wallets). These reports are not verified here. The peer-reviewed victim survey of this breach is already recorded in `raw/papers/2026-09-19-abramova-breach-fulltext.md`.

DAC8 relevance: the leak involved a private retailer's customer list, not tax data. It supports the target-selection stage (a leaked identity and address combined with crypto-holder status). The company's own point that the list showed no balances is limiting evidence: it cuts against, and does not support, any claim that the victims' wealth could be inferred from the list. DAC8 records add annual transaction values, which this leak did not contain.
