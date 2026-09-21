---
title: "Europäische Belege zu Datenmissbrauch und Gefährdungsrisiken"
type: report
sources:
  - wiki/references/european-data-misuse-and-physical-risk.md
  - wiki/references/dac8-physical-risk-causation.md
  - wiki/references/financial-data-breach-and-security-authorities.md
generated: 2026-09-19
tags: [europe, eu, insider-threat, physical-security, dac8, evidence]
summary: "Ergänzung mit europäischen Insiderfällen, EU-Risikomaßstäben und einem anhängigen EuGH-Verfahren, jeweils mit Grenzen der Übertragbarkeit auf DAC8."
---

# Datenmissbrauch und Gefährdungsrisiken: europäische Belege

Stand: 19. September 2026. Erstellt mit [LLM Wiki](https://github.com/bitcoinaustria/dac8-wiki). Forschungsunterlage, keine Rechtsberatung.

## Kurzbefund

Amtliche europäische Quellen belegen den Missbrauch dienstlicher Datenzugänge und die Verwendung personenbezogener Informationen zur Erpressung. EU-Leitlinien berücksichtigen ausdrücklich körperliche Schäden und Datenverknüpfungen. Das stützt eine konkrete Prüfung von Schadensfolgen und Zugriffsschutz. Es beweist weder einen durch DAC8 verursachten Angriff noch die Unverhältnismäßigkeit des gesamten Meldesystems.

## 1. Niederlande: belegter Verkauf aus Behördenzugängen

Die Rechtbank Overijssel verurteilte einen Mitarbeiter der Finanzverwaltung wegen der entgeltlichen Weitergabe von Fahrzeughalterdaten. Festgestellt wurden 216 Abfragen mit anschließender Offenlegung, unter anderem von Namen und Adressen. Das Gericht spricht ausdrücklich von möglichen erheblichen Gefahren für die Betroffenen. Es stellt jedoch keinen anschließenden Angriff fest. Die Daten waren keine Krypto- oder Vermögensmeldungen. [Urteil vom 27.9.2022, ECLI:NL:RBOVE:2022:2703, Abschnitte 4.5 und 7.3](https://uitspraken.rechtspraak.nl/details?id=ECLI:NL:RBOVE:2022:2703), [amtlicher Volltext als XML](https://data.rechtspraak.nl/uitspraken/content?id=ECLI:NL:RBOVE:2022:2703).

In einem weiteren Fall nutzte eine Gerichtsmitarbeiterin Informationen aus Gerichtssystemen zur Erpressung eines Mannes unter Gewaltandrohungen gegen ihn und Angehörige. Die [Gerichtsmitteilung vom 27.5.2026](https://www.rechtspraak.nl/organisatie-en-contact/organisatie/rechtbanken/rechtbank-overijssel/nieuws/2026/05/oud-medewerker-rechtbank-amsterdam-krijgt-vier-jaar-cel-voor-het-verkopen-van-vertrouwelijke-gegevens-en-afpersing) berichtet über ihre Verurteilung. Die Rechtskraft beider niederländischer Entscheidungen wurde nicht verifiziert.

Hinweise auf Zusammenhänge verkaufter Daten mit anderen Gewalttaten sind davon zu trennen. Die [Staatsanwaltschaft vom 6.5.2026](https://www.om.nl/actueel/nieuws/2026/05/06/om-eist-celstraf-tegen-ex-rechtbankmedewerker-voor-verkopen-persoonsgegevens-en-afpersing) erklärt ausdrücklich, wegen unzureichenden Nachweises entsprechender Kenntnis keine Beteiligung der Mitarbeiterin an diesen Angriffen angeklagt zu haben.

**Bedeutung:** Dienstliche Zugriffsberechtigung und tatsächliche Zweckbindung sind getrennt zu prüfen. Ein Schutzkonzept muss auch missbräuchliche Einzelabfragen und Weitergaben erfassen, nicht nur externe Angriffe.

## 2. Finnland: Datenabfluss mit anschließender Erpressung

Im Vastaamo-Verfahren bestätigte das Berufungsgericht Verurteilungen wegen Dateneinbruchs und Erpressung im Zusammenhang mit Psychotherapiedaten. Der Oberste Gerichtshof ließ das Rechtsmittel nicht zu. Das belegt einen europäischen Fall nachgelagerter Erpressung, nicht körperlicher Gewalt oder des Missbrauchs von Finanzdaten. [Berufungsgericht, 26.2.2026, R 24/1302](https://www.tuomioistuimet.fi/ajankohtaista/tiedotteet/helsingin-hovioikeus-korotti-vastaajan-rangaistusta-vastaamo-asiassa-r-24-1302/), [Oberster Gerichtshof, 13.7.2026, R1/2026/921](https://www.korkeinoikeus.fi/sv/aktuellt/nyhetsarkiv/hogsta-domstolen-avslog-ansokan-om-besvarstillstand-i-arendet-gallande-dataintranget-i-vastaamo-darefter-foljande-utpressningsbrott/).

## 3. EU-Maßstab: Schäden vorausschauend bewerten

Die [EDPB-Leitlinien 9/2022, Version 2.0](https://www.edpb.europa.eu/system/files/documents/2023-04/edpb_guidelines_202209_personal_data_breach_notification_v2.0_en.pdf) unterscheiden die Folgenabschätzung vor der Verarbeitung von der Bewertung eines eingetretenen Lecks. Rn. 104 bezieht hypothetische Datenschutzverletzungen ein. Rn. 107–115 behandeln Datenkombinationen, Identifizierbarkeit, körperliche Schäden und dauerhafte Folgen. Wahrscheinlichkeit und Schadensschwere müssen dennoch konkret bewertet werden. Daraus folgt nicht automatisch eine gesonderte Folgenabschätzungspflicht für jede gesetzlich angeordnete Verarbeitung.

[Europol, IOCTA 2025, S. 14](https://www.europol.europa.eu/cms/sites/default/files/documents/Steal-deal-repeat-IOCTA_2025.pdf), beschreibt angeworbene Mitarbeiter, gekaufte Zugangsdaten und eingeschleuste Beschäftigte als Zugriffswege. Der [Rechtsstaatlichkeitsbericht der Kommission 2025 zu den Niederlanden, S. 8–9 und Fn. 69](https://commission.europa.eu/document/download/02c5f8a3-cb3c-466f-92f0-5233129091df_en?filename=2025+Rule+of+Law+Report+-+Country+Chapter+Netherlands.pdf) dokumentiert Probleme bei der Nachvollziehbarkeit unberechtigter Behördenzugriffe, zugleich aber neue Überwachungsmaßnahmen und funktionierende Strafverfolgung. Beide Quellen sind keine Feststellung österreichischer Sicherheitsmängel.

## 4. Risikobezogene Zugangsbeschränkungen im EU-Recht

[Art. 15 der Richtlinie (EU) 2024/1640](https://eur-lex.europa.eu/eli/dir/2024/1640/oj/eng) verlangt unter außergewöhnlichen, nach nationalem Recht festzulegenden Umständen Zugangsbeschränkungen zum Register wirtschaftlicher Eigentümer, unter anderem bei unverhältnismäßigen Entführungs-, Erpressungs- und Gewaltrisiken. Die Regelung betrifft bestimmte Zugänge von Verpflichteten und Personen mit berechtigtem Interesse. **Der Behördenzugriff, einschließlich der Steuerbehörden, ist davon nicht erfasst.** Es handelt sich nicht um eine Ausnahme von DAC8-Meldungen.

Der anhängige Fall [C-609/26, Luxembourg Business Registers II, ABl. vom 31.8.2026](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:C_202604484), betrifft gerade die erforderliche Individualisierung solcher Risiken, die Bedeutung besonders gefährdeter Gruppen und bereits anderweitig verfügbarer Informationen. Das sind Vorlagefragen, noch keine Antworten des EuGH. Der Fall bietet einen konkreten weiteren Rechercheansatz, aber keinen bestehenden Befreiungsanspruch für Kryptonutzer.

## Folgerung für die österreichische Argumentation

Aus den Quellen lässt sich folgende Prüfung ableiten: Berücksichtigt die Risikobewertung, dass Identität, eine nutzbare Adresse und Hinweise auf Kryptoaktivität gemeinsam die Auswahl und Lokalisierung eines Opfers erleichtern könnten? Welche wirksamen Kontrollen begrenzen zweckwidrige Abfragen und Weitergaben?

Dabei bleibt die tatsächliche Meldung maßgeblich. [§ 18 Krypto-MPfG](https://ris.bka.gv.at/Dokumente/Bundesnormen/NOR40273817/NOR40273817.html) enthält Identitätsdaten und Jahresaggregate, keine individuellen Wallet-Adressen oder aktuellen Bestände. Ein Tätigkeitsvolumen kann vom Täter als Vermögen missverstanden werden, beweist aber keines. Eine Verknüpfung mit Blockchain-Daten benötigt zusätzliche nachgewiesene Informationen.

Die stärkere Argumentation richtet sich daher gegen konkret unzureichend begründete Datenkombinationen, Zugriffe oder Speicherdauern. Die bloße Existenz von Datenlecks genügt nicht. Auch nach [EuGH C-340/21, Rn. 30–38](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62021CJ0340) beweist ein erfolgreicher Angriff für sich allein keine unzureichenden Sicherheitsmaßnahmen. Die neuen Fälle ersetzen weder den Nachweis der betroffenen Verarbeitung noch eine konkrete Gefährdungsdarlegung.

## Quellenkritischer Hinweis

Die im Zusammenhang mit Intesa berichtete italienische Datenschutzentscheidung wird nicht als endgültig bestätigter Sanktionsfall verwendet: Die [aktuelle Mitteilung des Garante](https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/10235001) verzeichnet eine gerichtliche vorläufige Aussetzung und ein anhängiges Rechtsmittel. Das ist weder eine endgültige Aufhebung noch eine Bestätigung der ursprünglichen Feststellungen.
