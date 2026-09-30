---
title: "Visa PET Challenge federated learning benchmark and privacy limits"
source: "https://arxiv.org/pdf/2310.04546"
type: papers
ingested: 2026-09-30
fetched: 2026-09-30
content_format: pdf
tags: [federated-learning, mpc, alternatives, synthetic-data, utility, privacy-limits]
confidence: low
credibility_score: 1
summary: "Implemented FL/MPC protects additional bank flags but leaves transactions and identity fields at the hub; utility and privacy limitations remain explicit."
---

# Federated financial anomaly detection

Arora et al., 6 October 2023, PDF pp. 2 and 7–10, Tables 2, 4 and 5. Implementation: https://github.com/Visa-Research/visa-pets-FL.

Seven million synthetic training transactions and 700,000 test transactions underpin a FL/MPC prototype. AUPRC is 0.79 centrally with bank flags, 0.70 in a twenty-epoch local federated simulation, and 0.49 in the time-limited distributed challenge with one epoch; baseline without flags is 0.60.

The hub already possesses transaction, name, account and address data. The additional bank flag is protected, not the full financial profile. The authors give no formal differential-privacy guarantee and identify repeated-query leakage. These results demonstrate a testable design, not equivalent performance or universal profile prevention.

Scoring: recent +1, recognised researchers +1, first-party vendor benchmark -1. Unique implemented comparison retained at low tier; no peer-review points assigned to this preprint.
