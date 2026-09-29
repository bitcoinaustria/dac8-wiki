---
title: "Rechnungshof Bund 2011/9, IT-Projekt PAD (BMI): no random control routines for police-file access logs"
source: "https://www.rechnungshof.gv.at/rh/home/home/Informationstechnologie_im_BMI_-_IT-Projekt_PAD"
type: articles
ingested: 2026-09-29
fetched: 2026-09-29
content_format: pdf
confidence: high
tags: [austria, rechnungshof, bmi, pad, logging, protocol-review, random-checks, audit, controls, historical]
summary: "The Court of Audit found every PAD query logged but no random control routines for checking access legality in this decentralised police application, and recommended them; the BMI agreed. Historical audit, not a current or tax-system finding."
---

# Rechnungshof Bund 2011/9, IT-Projekt PAD (BMI): no random control routines for police-file access logs

The Austrian Court of Audit reviewed the BMI police application PAD (Protokollier-, Anzeigen- und Datenmodul), the police case-logging and file system, in report Reihe Bund 2011/9. The data-protection section is at pp. 120–125. At TZ 21.1 (p. 122) it records: "Jeder Datenverwendungsvorgang (Abfrage, Änderung oder Übermittlung) in der Applikation PAD wurde in dieser protokolliert und war somit nachvollziehbar" (every query, change or transmission was logged and traceable). Log evaluation followed the rules for central BMI applications under §§ 57 ff SPG, "ausschließlich im Dienstweg unter Einbindung des jeweiligen Datenschutzbeauftragten" (only through official channels with the data-protection officer). However: "Kontrollroutinen hinsichtlich der Zulässigkeit von Datenzugriffen mit einer zufallsabhängigen Auswahl und Überprüfung ... waren für die Applikation PAD als lokale bzw. dezentrale Anwendung nicht vorgesehen" (random-selection checks on access legality were not provided for PAD as a local or decentralised application).

At TZ 21.2 the Court recommended random control routines for the log data in the redesign; the BMI agreed (TZ 21.3; final recommendation 9, p. 131). At TZ 22 the Court also noted a Datenschutzkommission review, pending in January 2011, of whether PAD's name-based suggestion list complied with § 13(2) SPG.

Evidence class: official audit finding (primary). It is a concrete Austrian example of the gap between logging and proactive detection: complete logs existed, but no routine random review for that system. It is dated about 15 years ago and concerns a police application. It does not establish current PAD, EKIS or BMF practice, and the recommendation was accepted. OGH case law records later criminal PAD-query cases (RS0114637 T11, 17 Os 9/17b; RS0095301 T3, 14 Os 140/20z), but the Rechtssatz entries read do not say how those queries were detected.
