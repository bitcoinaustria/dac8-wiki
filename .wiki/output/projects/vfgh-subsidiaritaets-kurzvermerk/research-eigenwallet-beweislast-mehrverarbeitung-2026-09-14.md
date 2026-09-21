---
title: "DAC8: Eigenwallets, Beweisfragen und zusätzliche Verarbeitung"
type: report
sources:
  - wiki/references/dac8-field-necessity-and-alternatives.md
  - wiki/references/krypto-mpfg-provider-record-architecture.md
  - wiki/references/dsb-bvwg-evidence-and-interim-toolkit.md
  - wiki/references/austrian-gold-plating-and-claimant-audit.md
  - raw/articles/2026-08-30-cjeu-c484-24-nth-haustechnik.md
  - raw/articles/2026-08-30-dac8-impact-assessment-evidence-and-options.md
generated: 2026-09-14
verified: 2026-09-14
---

# DAC8: Eigenwallets, Beweisfragen und zusätzliche Verarbeitung

Stand: 14. September 2026. Mit [LLM Wiki](https://github.com/bitcoinaustria/dac8-wiki) erstellt. Rechercheunterlage, keine Rechtsberatung.

## Kurzbefund

Die Einbeziehung eigener Wallets ist keine erst im Rat eingeführte Erweiterung. Für Transfers besteht eine dokumentierte steuerliche Begründung; offen bleibt die besondere Abwägung einer nachgewiesenen Eigenwallet-Ausnahme. Ein erfolgreicher Datenminimierungsangriff setzt nicht generell eine vom Kläger finanzierte Wirksamkeitsstudie voraus. Zu trennen sind die Rechenschaft des Verantwortlichen, die Prüfung österreichischer Zusatzpflichten und die Gültigkeit des EU-Meldesystems.

Bei nicht meldepflichtigen Nutzern ist eine zusätzliche steuerliche Verarbeitung konkret nachzuweisen. Bereits vorhandene MiCA- oder TFR-Aufzeichnungen schließen sie weder aus noch rechtfertigen sie automatisch. Eine eigene Datenbank ist dafür nicht erforderlich.

## 1. Eigenwallets: belegte Entwicklung und verbleibende Lücke

Die [Folgenabschätzung SWD(2022) 401](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=SWD:2022:401:FIN) dokumentiert folgende Schritte; Seitenangaben beziehen sich auf die gedruckte Zählung:

| Fundstelle | Aussage und Reichweite |
|---|---|
| Abschnitt 5, S. 24 bis 25, einschließlich Fn. 30 | Transferinformationen sollen unter anderem Bewegungen in selbstverwahrte Cold Wallets und den Abgleich mehrerer Anbieter sichtbar machen. Die Eigenverwaltung war damit bekannt. |
| S. 25 bis 29; Abschnitt 8, S. 44 | Salden-, gröbere Aggregat- und Einzeltransaktionsmodelle wurden verglichen. Gewählt wurde Option 5 mit asset- und kategorienbezogenen Aggregaten. |
| Anhang 2, IV.2.1, S. 55 | In der Mitgliedstaatenkonsultation wurde eine Ausnahme für Transfers zwischen Wallets desselben Steuerpflichtigen befürwortet. Das ist eine konsultative Position, kein beschlossener Ausnahmetatbestand. |

Der [Kommissionsvorschlag COM(2022) 707, Anhang VI Abschnitt II.A.3 lit. g bis i und IV.C.5](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:52022PC0707) sah bereits Transferaggregate ohne allgemeine Eigenwallet-Ausnahme vor. Die enge Abgrenzung betrifft Konten oder Adressen, die derselbe meldende Anbieter für denselben Nutzer führt. Sie findet sich in der [Endfassung, Anhang VI Abschnitt IV.C.4](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023L2226) wieder. Die Behauptung, erst der Rat habe eine allgemeine Ausnahme gestrichen, ist durch diese Textfolge nicht gedeckt.

Schon der [OECD-Konsultationsentwurf vom März 2022, Kommentar zu Abschnitt II Rn. 7, S. 24](https://web-archive.oecd.org/2022-03-22/627496-public-consultation-document-crypto-asset-reporting-framework-and-amendments-to-the-common-reporting-standard.pdf) erfasste ausdrücklich eigene private Wallets und eigene Konten bei anderen Anbietern. Der endgültige CARF behielt dies bei, nachprüfbar im [Kommentar 2023, Abschnitt II Rn. 7](https://www.oecd.org/en/publications/international-standards-for-automatic-exchange-of-information-in-tax-matters_896d79d1-en/full-report/component-7.html).

Eine tatsächlich dokumentierte Beschränkung betraf stattdessen bestimmte externe Adressen: Nach dem Entwurf, Kommentar II Rn. 26, S. 27, sollten diese für entsprechend gelistete Meldejurisdiktionen gemeldet werden, mit Ausnahmen für bekannte Anbieteradressen. Die [Endfassung 2022, Kommentar II Rn. 25 bis 26](https://web-archive.oecd.org/2022-10-10/642425-crypto-asset-reporting-framework-and-amendments-to-the-common-reporting-standard.pdf), sieht stattdessen ihre Aufbewahrung für Folgeanfragen sowie aggregierte Wert- und Einheitenmeldungen vor. Der OECD-Standard ist dabei keine eigenständige österreichische Eingriffsbefugnis.

**Offene Frage:** Weshalb genügte eine verifizierte Eigenwallet-Ausnahme aus Sicht der Entscheidungsträger nicht für die steuerlichen Kontrollzwecke? Die allgemeine Transferbegründung beantwortet diesen engeren Alternativenvergleich nicht abschließend. Umgekehrt belegt eine nicht aufgefundene spezielle Begründung weder, dass keine Abwägung stattfand, noch einen Rechtsverstoß.

**Konkrete Dokumentenspur:** SWD-Anhang 2, Sitzungstabelle S. 51 und II.2.1, S. 52, nennt die Working-Party-IV-Sitzungen vom 13. November 2020 und 24. März 2021 sowie das TAXUD-D2-Konzeptpapier „Possible expansion of the exchange of information framework in the field of taxation to include crypto-assets and e-money“. Das Papier und die Sitzungsprotokolle wurden in der öffentlichen Suche nicht aufgefunden. Der verlinkte Registereintrag war technisch nicht abrufbar. Weder Nichtöffentlichkeit noch Nichtexistenz sind damit festgestellt.

## 2. Beweisfragen: drei verschiedene Prüfungen

| Ebene | Tragfähiger Ausgangspunkt | Grenze |
|---|---|---|
| Konkrete Verarbeitung durch den Verantwortlichen | Art. 5 Abs. 2 DSGVO verlangt Rechenschaft. In C-175/20 trägt die Steuerbehörde den Nachweis ihrer Datenminimierung und des notwendigen Erhebungszeitraums. | Der Beschwerdegegenstand und die tatsächliche Betroffenheit müssen konkretisiert werden. Das Urteil entschied über eine behördliche Auskunftsanforderung, nicht über die Gültigkeit von DAC8. |
| Österreichische gesetzliche Zusatzpflicht | Art. 6 Abs. 3 DSGVO verlangt eine verhältnismäßige gesetzliche Grundlage. Unionsrechtlich nicht vorgeschriebene Mehrverarbeitung ist nicht allein deshalb verboten. | Die konkrete nationale Pflicht, ihr Zweck und eine nachvollziehbare Begrenzung sind zu bestimmen. Eine bloße Abweichung vom EU-Minimum ersetzt diese Prüfung nicht. |
| Unionsrechtlich vorgeschriebener Meldedatensatz | Art. 7, 8 und 52 Abs. 1 GRC begrenzen den Eingriff. Ein gezielter Vergleich weniger eingriffsintensiver Modelle kann die Erforderlichkeit erschüttern. | Keine allgemeine Pflicht zu einer veröffentlichten Einzelstudie für jedes Feld. C-623/22 akzeptierte das DAC6-Informationspaket in einer Gesamtprüfung. |

Fundstellen: [C-175/20, Rn. 71 und 74 bis 85](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:62020CJ0175), [C-484/24, Rn. 99 bis 103 und 116](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:62024CJ0484), [C-623/22, Rn. 143 bis 149](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:62022CJ0623).

NTH Haustechnik verortet die vollständige Abwägung bei der gesetzlichen Grundlage. Für die dortige gerichtliche Beweisverarbeitung verlangt das Urteil keine zusätzliche vollständige Abwägung bei jedem Verarbeitungsschritt, sofern die DSGVO-Anforderungen erfüllt sind. Daraus folgt weder eine Freistellung von operativer Datenminimierung noch eine Befugnis des Anbieters, gesetzliche Pflichten nach eigener Abwägung zu ersetzen.

**Folgerung:** Eigene empirische Belege können wichtig werden, sind aber nicht pauschal vor jedem Verfahren zu beschaffen. Zunächst sind vorhandene Begründungen und tatsächliche Verarbeitungsschritte zu klären. Eine fehlende öffentliche Feldstudie beweist keine Wirkungslosigkeit; umgekehrt ersetzt der allgemeine Nutzen des Steuerdatenaustauschs nicht jede konkrete Erforderlichkeitsprüfung.

### Zugang zu vorhandenen Nachweisen

| Benötigt | Möglicher Zugang | Grenze |
|---|---|---|
| Eigene Daten, gebildete Aggregate, Zwecke, Herkunft, Empfänger und Speicherdauer | Art. 15 DSGVO beim jeweiligen Verantwortlichen | Kein allgemeines Recht auf vollständige DSFA, interne Gutachten oder Sicherheitsarchitektur. |
| Datenfluss, Aggregations- und Löschregeln, Verarbeitungsverzeichnis, vorhandene DSFA und Auditbefunde | Konkret begründete Beiziehung im DSB-Verfahren; Untersuchungsbefugnisse nach Art. 58 Abs. 1 DSGVO, Verzeichniszugang nach Art. 30 Abs. 4 | Behördenzugang ist nicht gleich ungeschwärzte Herausgabe an den Beschwerdeführer. Relevanz für den Streit darlegen. |
| Beigezogene Akten und fehlende Sachverhaltsfeststellungen | § 17 sowie §§ 37, 39, 45 und 46 AVG; im BVwG-Verfahren nach Maßgabe des § 17 VwGVG | Amtswegige Ermittlung und rechtzeitiges, vollständiges Parteivorbringen wirken zusammen. Akteneinsicht unterliegt insbesondere § 17 Abs. 3 AVG. |
| Bestehende österreichische Bewertungen, Studien und WFA-Unterlagen | Informationsbegehren nach IFG an die zuständige informationspflichtige Stelle | Kein Anspruch auf Erstellung einer neuen Studie. Geheimhaltungsgründe und Teilzugang nach §§ 6 und 9 gesondert prüfen. |
| Konzeptpapier, Sitzungsunterlagen und weitere vorhandene Kommissions-/Ratsdokumente | Register und Zugang nach VO 1049/2001 | Antragsberechtigung nach Art. 2 und Schutzgründe nach Art. 4 prüfen; Teilzugang nach Art. 4 Abs. 6 bleibt möglich. |

Fundstellen: [DSGVO, Art. 15, 30 und 58](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679), [AVG, Fassung 14. September 2026](https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10005768&FassungVom=2026-09-14), [§ 17 VwGVG](https://www.ris.bka.gv.at/eli/bgbl/i/2013/33/P17/NOR40147930), [IFG, Fassung 14. September 2026](https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20012537&FassungVom=2026-09-14), [VO 1049/2001, Art. 2 bis 4 und 6](https://eur-lex.europa.eu/eli/reg/2001/1049/oj/eng).

Ein geeignetes Beweisthema wäre die Grundlage, auf der eine konkret festgestellte Profilbildung trotz Nicht-Meldepflicht als erforderlich beurteilt wurde. Nichtvorlage, Nichtvorhandensein und fehlende Veröffentlichung eines Dokuments sind unterschiedliche Befunde. Keiner davon beweist allein die Rechtswidrigkeit der Verarbeitung.

## 3. Nicht meldepflichtige Nutzer: welche Verarbeitung kommt hinzu?

Ausgangspunkt ist eine für den betreffenden Zeitraum abgeschlossene Nicht-Meldepflicht-Prüfung unter Einbeziehung sämtlicher Steueransässigkeiten. [§ 20 Abs. 1 Krypto-MPfG](https://www.ris.bka.gv.at/Dokumente/Bundesnormen/NOR40273819/NOR40273819.html) erfasst ausdrücklich auch diese Kunden. Sein Eingangssatz bindet die Verarbeitung an die Identifikation und Erfüllung der gesetzlichen Verpflichtungen. Das ist ein Ansatz für eine begrenzende Auslegung, aber keine im Wortlaut enthaltene allgemeine Ausnahme für bereits geprüfte Nichtmeldepflichtige.

Die folgende Matrix beschreibt mögliche Unterschiede, keine festgestellte Anbieterarchitektur:

| Verarbeitung | Bereits anderweitig mögliche Pflicht | Zu prüfender zusätzlicher Vorgang |
|---|---|---|
| Identität und Steueransässigkeit | Kundenidentifikation und Meldestatusprüfung | Steueransässigkeit, TIN und Statushistorie sind nicht mit AML-Identifikation gleichzusetzen. Erforderliche Statusnachweise bleiben möglich. |
| Einzeltransaktionen, Adressen, Hashes | Je Dienstleistung und Vorgang MiCA- und TFR-Aufzeichnungen | Nutzung vorhandener Transaktionsdaten für eine weitere steuerliche Auswertung; zusätzliche Felder, Zugriffsrechte oder Empfänger. |
| Marktwerte und Transaktionsklassen | Ausführungspreise und operative Transaktionsarten können bereits vorhanden sein | Steuerliche Bewertungszeitpunkte, Umrechnungen und Zuordnung zu §-18-Kategorien können zusätzliche Verarbeitung sein. Nicht jede Bewertung wird dafür neu erzeugt. |
| Jahresaggregate nach Asset und Kategorie | Eine identische universelle Jahresaggregation folgt nicht schon aus den hier geprüften MiCA-/TFR-Aufzeichnungen | Tatsächliche Berechnung, Speicherung oder Abfrage eines steuerlichen Jahresprofils trotz festgestellter Nicht-Meldepflicht. |
| Verknüpfung von Steuer- und Blockchain-Daten | Einzelne Verknüpfungen können für die bestehende Dienstleistung erforderlich sein | Zusätzliche steuerbezogene Verknüpfung oder erweiterte Nutzung. Auch eine Abfrage im bestehenden System ist Verarbeitung, ohne neue Datenbank. |
| Aufbewahrung | Eigenständige Aufbewahrungsregeln können weiter gelten | Welche steuerbezogenen Daten werden länger oder zu anderen Zwecken vorgehalten? § 20 Abs. 4 betrifft übermittelte Informationen; § 39 dokumentierte Melde- und Sorgfaltsschritte. |

Rechtsgrundlagen und Grenzen: [MiCA-Aufzeichnungen, VO (EU) 2025/1140, Art. 2 und Anhang Tabellen 3 und 4](https://eur-lex.europa.eu/eli/reg_del/2025/1140/oj/eng), [TFR, Art. 14 bis 16 sowie 25 und 26](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32023R1113), [DSGVO, Art. 4 Z 2, 5 und 6](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679), [§ 39 Krypto-MPfG](https://ris.bka.gv.at/Dokumente/Bundesnormen/NOR40273838/NOR40273838.html).

TFR-Daten werden auf Grundlage dieser Verordnung für AML/CFT-Zwecke verarbeitet. Die TFR schafft keine eigenständige Steuerbefugnis. Ob eine anderweitig gesetzlich angeordnete Nutzung zulässig ist, bedarf einer gesonderten Prüfung einschließlich der besonderen Zweckbindung. Ebenso beweist das Vorhandensein von MiCA-Aufzeichnungen weder eine zusätzliche Steuerkopie noch deren Erforderlichkeit.

**Milderes Modell als prüfbare Hypothese:** Statusprüfung und ihre Dokumentation bleiben bestehen. Ein vollständiges steuerliches Jahresprofil wird erst bei festgestellter Meldepflicht erzeugt. Notwendige Korrekturen müssten aus rechtmäßig vorhandenen Grunddaten möglich bleiben. Zu testen sind insbesondere rückwirkend korrigierte Selbstauskünfte, mehrere Ansässigkeiten und Änderungen der Austauschbeziehungen. Das Modell darf nicht voraussetzen, dass sämtliche Ausgangsdaten sofort gelöscht werden oder jede spätere Berechnung rechtlich und technisch möglich bleibt.

**Ergebnisabhängige Konsequenz:** Besteht keine zusätzliche steuerliche Verarbeitung, wird dieser konkrete Angriff schwächer. Besteht sie, lautet die Frage nicht „Warum besitzt der Anbieter überhaupt Transaktionsdaten?“, sondern welche zusätzliche Verarbeitung für welchen gesetzlichen Zweck noch erforderlich ist. Eine erfolgreiche Begrenzung kann operative Abhilfe schaffen, ohne dass DAC8 insgesamt für ungültig erklärt werden muss.

## Verbleibender Nachweisbedarf

1. Die konkrete Anbieter-Verarbeitung einschließlich abgeschlossener Statusprüfung und geltend gemachter Rechtsgrundlagen ist nicht festgestellt. Eine personen- oder länderspezifische Erfolgseinschätzung folgt aus dieser Notiz nicht.
2. Die spezielle Entstehungsgeschichte einer verifizierten externen Eigenwallet-Ausnahme bleibt offen. Vorhanden ist dagegen eine allgemeine Begründung der Transfermeldung.
3. Die Leistungsfähigkeit des statusabhängigen Aggregationsmodells ist nicht getestet. Vorhandene regulatorische Grunddaten, Korrekturen und geänderte Ansässigkeit sind dabei einzubeziehen.
