---
title: "Czybik2026: scaled context and a denominator inconsistency"
source: "https://www.usenix.org/system/files/usenixsecurity26-czybik.pdf"
type: papers
ingested: 2026-10-17
fetched: 2026-10-17
content_format: pdf
tags: [phishing, llm, field-experiment, denominator-error]
summary: "A contemporary university experiment supports scalable public-context phishing but contains an internally inconsistent headline percentage."
---

# Czybik2026: scaled context and a denominator inconsistency

Czybik et al., USENIX Security2026, pp.1687–1706. Final publisher PDF, especially printed1694 Table2; design and profile-stratification sections.

7,741 addresses;4,010 with public information. Table2 records330 clicks/3,177 delivered personalized emails; generic LLM65/1,735 and manual79/1,918. Reported10.0% is inconsistent with the stated delivered denominator:330/3,177≈10.39%, whereas330/3,310 sent≈9.97%.

Generic controls are randomized within public-information strata, but pooled headline comparisons mix public-data and no-data groups. Delivery was whitelisted; outcome is click only. Richer profiles performed worse than low/medium profiles. Public professional context is not leaked financial information. Mechanical credibility4: peer-reviewed+2, recent+1, institution+1; retain arithmetic qualification.

