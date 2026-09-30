---
title: "DAC history PR14: fixed-head review and targeted correction follow-up"
source: "https://github.com/bitcoinaustria/dac8.org/pull/14"
type: repos
ingested: 2026-09-30
fetched: 2026-09-30
tags: [dac-history, source-correction, review-provenance, campaign-copy, implementation-status]
summary: "The review of website head45ff2b6 identified six distinct scope errors and two precision corrections. A targeted comparison with head645fc48 found those wording issues and Article16 dossier alignment addressed; no comprehensive new-head review, approval or merge is recorded."
revision: "645fc48e1a2bc12ff893f5fabc1ba50ac9bf74f6"
canonical_url: "https://github.com/bitcoinaustria/dac8.org/compare/45ff2b6575ab67a426aa084a76cf42298912be14...645fc48e1a2bc12ff893f5fabc1ba50ac9bf74f6"
---

# DAC history PR14: fixed-head review and targeted correction follow-up

## Reviewed and observed revisions

- Repository: `bitcoinaustria/dac8.org`; PR14, branch `dac-history`.
- Full independent fact-check: head `45ff2b6575ab67a426aa084a76cf42298912be14`, base `37c0fccbbf832656214242fb2c62cc56cd8b11b9`.
- Wiki reference used: gitlink `d17892b21667f778fc8d035e3f1577858791f1a3`, the EU Tax-Information Exchange Timeline.
- Main content: `/geschichte/`, `/en/history/`, `src/data/history.ts`; related SEO and dossier wording checked.
- Three independent review tracks covered standards, specification/later instruments, and early instruments/Austrian implementation. Public primary sources controlled over the wiki.
- Subsequent targeted comparison: observed open PR head `645fc48e1a2bc12ff893f5fabc1ba50ac9bf74f6`, one commit after the reviewed head, on 30 September 2026. This is not a fresh comprehensive review of that later head.

This record establishes what repository text was reviewed and changed, not the truth of law. Use the separately cited primary-law supplement and timeline for legal conclusions. No review posting, approval, website mutation or merge was performed by this fact-check operation.

## Findings at the reviewed head and observed follow-up

All line numbers are one-based. Original `history.ts` line numbers refer to `45ff2b6`; later numbers refer to `645fc48`.

| Finding at45ff2b6 | Original location | Targeted status at645fc48 |
|---|---|---|
| P2: SEO promises annual reporting on every customer, conflating checks with reporting. | `src/data/seo.ts:43,49` | Addressed: reporting duties of banks, platforms and crypto providers; same line numbers. |
| P2: DAC2 universally reviews every customer, disregarding account exceptions. | `history.ts:239,247`; era introduction565,602 | Addressed: residence determination under due-diligence rules with exemptions, at248,256; era refers to reportable accounts. |
| P2: DAC3 limited to binding rulings and unqualified five-year historical coverage. | `history.ts:272,279` | Addressed: information about rulings; specified older rulings subject to validity/turnover limits, at281,288. |
| P2: DAC6 lawyer notification holding and 2024 validity holding overstated. | `history.ts:367,374` | Addressed: privileged lawyers/non-client intermediaries and examined validity objections, at376,383. |
| P2: DAC7 counts physical goods/items rather than sale activities. | `history.ts:400,407` | Addressed: fewer than30 sales transactions and consideration≤EUR2,000 in the reporting period, at409,416. |
| P2: DAC9 central filing categorical and deadline presented as universal actual filing. | `history.ts:487–489,494–496` | Addressed: conditional central filing and first2024 returns due by30June2026, at501,503,508,510. |
| P3: Austrian DAC2 exchange deadline presented as exact execution day. | `history.ts:242,250` | Addressed: by/bis30September2018, at251,259. |
| P3: Inexact quotation of the German DAC5 proposal. | `history.ts:334` | Addressed: leaked-information paraphrase without false quotation, at343. |
| Clarification: EU sanctions scope and alignment with existing dossier wording. | `HistoryPage.astro:97,98`; dossierDE32,EN37 | Addressed: Article215 TFEU, no sender permission, and continuing purpose/secrecy/data-protection limits; both dossiers align. |

The independent axis reports contained two Standards P2 findings and three Spec P2 findings; DAC7 appeared in both. The primary-law track added two distinct P2 findings and two P3 precision findings. This is six distinct P2 scope corrections, not seven independent errors.

## Draft review comments preserved for reuse

These comments were proposed against the original head. They are not currently outstanding findings at the observed later head and were not posted by this review.

1. SEO: remove the universal customer claim; describe annual reporting obligations of banks, platforms and crypto providers.
2. DAC2: replace universal review with tax-residence determination under due-diligence rules, acknowledging exempt accounts; remove universal wording from the era introduction.
3. DAC3: remove the binding-only limitation and qualify historical validity/turnover conditions.
4. DAC6: specify privileged lawyers notifying non-client intermediaries; describe the2024 ruling as rejection of the examined validity challenges.
5. DAC7: use sale activities/transactions, retaining both the fewer-than30 and total-consideration≤EUR2,000 conditions.
6. DAC9: central filing is available subject to its conditions; the first calendar-year2024 returns were due by30June2026.
7. Dates and quotations: use by/bis for Austrian first-exchange deadlines and paraphrase the German DAC5 proposal faithfully.
8. Article16: retain the supported EU sender-permission waiver, specify Article215 purposes, and preserve purpose restrictions, secrecy and data protection in both languages.

## National-law question kept separate

The original review did not identify the Austrian authorization question as a website defect. The later website change does not add that research caveat. EU-AHG §15 does not itself expressly reproduce the EU sanctions-use exception; the complete interaction with SanktG2024 or other authority remains unresolved. This must not be turned into an allegation of defective transposition or unrestricted Austrian use.

## Evidence and limits

- [Pinned comparison](https://github.com/bitcoinaustria/dac8.org/compare/45ff2b6575ab67a426aa084a76cf42298912be14...645fc48e1a2bc12ff893f5fabc1ba50ac9bf74f6) is repository-change evidence.
- [Original history module](https://github.com/bitcoinaustria/dac8.org/blob/45ff2b6575ab67a426aa084a76cf42298912be14/src/data/history.ts) and [later module](https://github.com/bitcoinaustria/dac8.org/blob/645fc48e1a2bc12ff893f5fabc1ba50ac9bf74f6/src/data/history.ts) fix the text revisions.
- Legal conclusions were checked against official EU, RIS, Parliament, OECD and court material, not merely correspondence with the pinned wiki.
- Exact ELI retrieval sometimes encountered bot challenges; alternative official originals were used. No wrong-act source link was found in the reviewed stations.
- Green CI at the original reviewed head was observed; it does not establish legal accuracy, deployment contents or merge readiness.
- Later commits, check results, deployment and merge state require a new live check. The targeted follow-up is not approval.
