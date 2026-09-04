---
title: "When the Cookie Meets the Blockchain: Privacy Risks of Web Payments Via Cryptocurrencies"
source: "https://petsymposium.org/popets/2018/popets-2018-0038.php"
type: papers
ingested: 2026-09-04
fetched: 2026-09-04
content_format: html
tags: [bitcoin, privacy, amount-matching, timing-intersection, cookies, re-identification, peer-reviewed]
summary: "Peer-reviewed experiment showing that amount and short timing windows can link web payments to public-ledger transactions and sometimes expand identity linkage to address clusters."
---

# When the Cookie Meets the Blockchain

Goldfeder, Kalodner, Reisman and Narayanan, Proceedings on Privacy Enhancing Technologies 2018(4), DOI 10.1515/popets-2018-0038, test passive linkage of cryptocurrency web purchases. Their attacker has purchase amount and a short timing window, and in some scenarios a tracking cookie or other identity context. Under those conditions the candidate set frequently collapses to one public-ledger transaction; observing more than one purchase can strengthen cluster linkage.

The experiment does not model DAC8's calendar-year aggregates. It does not show that an annual amount and unit total, without time, address or transaction identifier, uniquely identifies an on-chain transaction. It establishes a mechanism whose success depends materially on precision, timing, chain activity and auxiliary data.
