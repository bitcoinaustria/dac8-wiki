---
title: "DAC8 VfGH-to-CJEU Research Report"
type: report
sources:
  - wiki/topics/austrian-dac8-implementation.md
  - wiki/topics/dac2-crs-austrian-litigation.md
  - wiki/concepts/individualantrag-article-140.md
  - wiki/concepts/article-267-preliminary-reference.md
  - wiki/topics/dac8-charter-proportionality.md
  - wiki/references/epicenter-vorratsdatenspeicherung-precedent.md
  - wiki/references/austria-eu-precedent-matrix.md
  - wiki/references/austrian-gold-plating-and-claimant-audit.md
  - wiki/references/dac8-com-argument-audit.md
  - wiki/theses/vfgh-to-cjeu-dac8-route.md
generated: 2026-08-27
---

# DAC8 VfGH-to-CJEU Research Report

## Ergebnis

Der Weg zu einer EuGH-Vorabentscheidung ist real, aber er sollte nicht als ein einziger „Bürger → Individualantrag → VfGH → EuGH“-Fall geplant werden. Nach den vollständigen österreichischen Vorratsdatenakten, der DAC2-Trilogie, der aktuellen VfGH-Judikatur und einem Wortlautvergleich von DAC8 und Krypto-MPfG ist eine **koordinierte Zweigleisigkeit** deutlich belastbarer:

1. **Österreichischer Home-State-CASP → direkter Individualantrag nach Art. 140 B-VG.** Der CASP ist unmittelbarer Normadressat und kann sich auf Erwerbsfreiheit sowie konkret belegte technische und administrative Mehrkosten berufen. Gegenstand sollte ein präzise isolierter österreichischer Umsetzungsüberschuss sein.
2. **Konkreter Nutzer → Art.-15/17/18-DSGVO-Anfrage → § 24 DSG-Beschwerde bei der DSB → BVwG → Antrag auf Vorlage nach Art. 267 AEUV und gegebenenfalls amtswegige Normenkontrolle → Art. 144 B-VG/VwGH.**

Innerhalb der Nutzerschiene sind zwei Fälle zu trennen:

- Ein **tatsächlich nicht meldepflichtiger Nutzer**, dessen vollständige §-18-Daten dennoch nach § 20 Abs. 1 verarbeitet werden, ist der sauberste Kläger gegen das österreichische Gold-Plating.
- Ein **meldepflichtiger österreichischer Nutzer** ist der passende Fall für die breitere Gültigkeitsfrage der DAC8-Richtlinie nach Art. 7, 8 und 52 Abs. 1 GRC. Er kann aber nicht geltend machen, gerade durch die überschießende Erfassung nicht meldepflichtiger Personen verletzt zu sein.

Ein gemeinsamer, undifferenzierter Antrag von Nutzer und CASP ist nicht zu empfehlen. Rechte, unmittelbare Betroffenheit, zumutbare Umwege und Anfechtungsumfang unterscheiden sich. Besser sind getrennte, sachlich koordinierte Verfahren.

## Der stärkste österreichische Angriffspunkt: § 20 Abs. 1 Krypto-MPfG

DAC8 trennt im Anhang VI zwischen zwei Ebenen:

- Abschnitt III verlangt Selbstauskunft und Sorgfaltsprüfung, damit der Anbieter die Steueransässigkeit und Meldepflicht eines Nutzers feststellen kann.
- Abschnitt II verlangt Identitäts- und jährliche Transaktionsinformationen „with respect to“ meldepflichtigen Nutzern und bestimmten beherrschenden Personen.

§ 20 Abs. 1 Krypto-MPfG geht darüber ausdrücklich hinaus. Ein Anbieter muss die in § 18 definierten meldepflichtigen Informationen **für alle Kunden hinsichtlich aller Transaktionen und Kryptowerte** ermitteln, erfassen, speichern und verarbeiten, unabhängig davon, ob der Kunde meldepflichtig ist.

Der textliche Umsetzungsüberschuss ist klar. Die österreichischen Erläuterungen bestätigen ihn. Auch Deutschland und die Niederlande zeigen eine praktisch verfügbare Umsetzung, die Selbstauskunft allgemein einholt, die Transaktionsaggregate aber auf meldepflichtige Nutzer bezieht.

Das bedeutet noch nicht automatisch Unions- oder Verfassungswidrigkeit. DAC8 enthält keine klare Vollharmonisierungsklausel. Der tragfähige Angriff lautet daher nicht bloß „Gold-Plating ist verboten“, sondern:

- Verstoß gegen Zweckbindung, Datenminimierung und Speicherbegrenzung nach Art. 5 Abs. 1 lit. b, c und e DSGVO;
- fehlende strikte Erforderlichkeit und Präzision der nationalen Rechtsgrundlage nach Art. 6 Abs. 3 DSGVO;
- Eingriff in Art. 7, 8 und 52 Abs. 1 GRC sowie § 1 DSG;
- für den CASP zusätzlich unverhältnismäßige Erwerbsausübungsbeschränkung nach Art. 6 StGG.

Der wichtigste EuGH-Anker ist C-175/20, *Valsts ieņēmumu dienests*: Auch steuerliche Datenerhebung muss nach Relevanz, Zweck, objektiven Kriterien, strikter Erforderlichkeit und Zeitraum begrenzt sein. Der Staat wird unterscheiden, dass dort eine offene behördliche Anforderung und hier ein gesetzlich definiertes DAC-System vorlag. Die DAC2-Trilogie und C-623/22, *Belgian Association of Tax Lawyers*, sind näherliegende Gegenjudikatur.

Der Fall braucht deshalb eine technisch und rechtlich überzeugende weniger eingriffsintensive Alternative: Selbstauskunft für alle, aber Erzeugung der nach § 18 klassifizierten, bewerteten und jährlich aggregierten Steuerprofile erst für meldepflichtige Nutzer. Zu beweisen ist, dass dieses Modell bei Wohnsitzwechseln, Korrekturen und Prüfungen gleich wirksam bleibt.

## Korrektur der Aufbewahrungsrüge

§ 20 Abs. 4 Krypto-MPfG betrifft nur Informationen, die „gemäß diesem Bundesgesetz **übermittelt**“ wurden. Die Erläuterungen sprechen ebenfalls von gemeldeten oder übermittelten Informationen. Die Behauptung, § 20 Abs. 4 zwinge zur zehnjährigen Speicherung des vollständigen Transaktionsprofils jedes niemals meldepflichtigen Nutzers, ist daher falsch.

§ 39 ist gesondert zu prüfen. Der Gesetzestext verlangt zehnjährige Aufbewahrung „dieser Dokumente“, die die Schritte zur Einhaltung von Melde- und Sorgfaltspflichten belegen. Die Materialien sprechen weiter von „Dokumenten und Informationen“. Daraus entstehen zwei alternative, nicht gleichzeitig als feststehend zu behandelnde Fälle:

1. Bei enger Auslegung hat das Krypto-MPfG für die vollständigen, nie übermittelten §-20-Abs.-1-Daten keine klare spezielle Löschfrist. Das ist ein Bestimmtheits- und Speicherbegrenzungsproblem. Der Staat wird einwenden, Art. 5 Abs. 1 lit. e DSGVO gelte unmittelbar und verhindere unbegrenzte Speicherung.
2. Bei weiter Behörden- oder Providerinterpretation erfasst § 39 auch die gesamten zugrunde gelegten Transaktionsinformationen. Dann muss die konkrete zehnjährige Speicherung definitiv nicht meldepflichtiger Nutzer auf strikte Erforderlichkeit geprüft werden.

Die richtige Tatsachengrundlage ist eine Art.-15-Auskunft, die Aufbewahrungsrichtlinie des CASP, Löschjobs und Backups, die konkrete Rechtsgrundlage und eine dokumentierte Ablehnung eines Lösch- oder Einschränkungsbegehrens.

Die Wahl von zehn statt fünf Jahren für tatsächlich übermittelte Daten liegt im von DAC8 eröffneten Korridor. Sie bleibt eine nationale Verhältnismäßigkeitsfrage, ist aber kein klarer formeller Umsetzungsfehler.

## CASP als direkter Art.-140-Antragsteller

VfGH G 105/2025 vom 18. Dezember 2025 ist der wichtigste neue Präzedenzfall. Der VfGH akzeptierte den direkten Antrag von Unternehmen, die vor einem festen Stichtag Schnittstellen, elektronische Datenverarbeitung und interne Abläufe anpassen mussten. Erhebliche technische oder administrative Vorbereitungen zur Vermeidung von Sanktionen sind keine bloßen wirtschaftlichen Reflexwirkungen; die aktuelle Beeinträchtigung beginnt früh genug, damit die Kosten durch rechtzeitige Normprüfung noch vermieden oder reduziert werden können.

G 606/2015 ua zur Registrierkassenpflicht bestätigt diese Linie: technische und administrative Vorbereitungen mit ins Gewicht fallendem Aufwand begründen unmittelbare und aktuelle Betroffenheit; ein Unternehmen muss nicht gegen eine sanktionierte Pflicht verstoßen, um Rechtsschutz zu erlangen.

Für einen Austria-Home-CASP ist die Zulässigkeitsposition heute besonders gut, weil § 20 bereits seit 1. Jänner 2026 gilt. Ein Antrag braucht dennoch:

- zweifelsfreie Einordnung nach § 15 Krypto-MPfG und MiCA Art. 60 oder 63;
- Darstellung, warum kein echter zumutbarer Bescheid- oder Feststellungsweg für die konkrete Verfassungsfrage besteht;
- genaue gesetzliche Pflichten und einen trennbaren Anfechtungsumfang;
- aktuelle, bereits durchgeführte oder vertraglich gebundene Maßnahmen;
- Rechnungen, Verträge, Engineering-Stunden, FTE, Speicher- und Sicherheitskosten;
- eine Kostenzerlegung zwischen EU-Mindestumsetzung und österreichischer Mehrpflicht.

Die offizielle WFA schätzt bei zwölf potenziell betroffenen Anbietern rund EUR 500.000 Implementierungsaufwand und EUR 425.000 jährlichen Aufwand je Unternehmen. Sie behandelt das Regime als neue Informationsverpflichtung und setzt im WFA-Modell null Prozent Sowieso-Kosten an. Das belegt Materialität, aber nicht die Verfassungswidrigkeit: Die WFA trennt den unvermeidbaren EU-Baseline-Aufwand nicht von § 20 Abs. 1 oder anderen österreichischen Entscheidungen.

G 105/2025 und G 606/2015 sind auf der Sachebene Warnungen. Der VfGH hielt ein tägliches, detailliertes und weites Datenmonitoring beziehungsweise ein breites elektronisches Steueraufzeichnungssystem für verhältnismäßig. Ein erfolgreicher CASP-Antrag muss daher den spezifischen nationalen Überschuss und die gleich wirksame mildere Lösung beweisen, nicht bloß hohe Gesamtkosten.

## Nutzer als Kläger: Rechtsweg und Auswahl

Die österreichische Vorratsdatenspeicherung zeigt, dass providergerichtete Speicherpflichten die Rechtssphäre der Nutzer unmittelbar betreffen können. Sie rechtfertigt aber heute keinen automatischen direkten Individualantrag.

Im Vorratsdatenfall waren außergewöhnliche Umstände entscheidend: zahlreiche und teilweise unbekannte Provider, darunter Provider von Kommunikationspartnern, laufend neu entstehende Datensätze und Löschung nach sechs Monaten, bevor wirksame Normprüfung erreichbar sein konnte.

Bei DAC8 kennt der Nutzer regelmäßig seinen CASP. Die Daten werden wesentlich länger verarbeitet. Vor allem entschied der VfGH in G 178/2024 am 28. April 2026 zur verpflichtenden eImpfpass-Verarbeitung, dass § 24 DSG-Beschwerde, BVwG-Beschwerde und anschließende Art.-144-Kontrolle einen zumutbaren Weg bilden. Erwartet geringe Erfolgschancen bei der DSB ändern daran nichts. G 385/2018 zu ELGA und V 532/2020 zu Smart Metern weisen in dieselbe Richtung.

Der Nutzerweg sollte daher konkret aufgebaut werden:

1. Vertrag, Konto, österreichischer gesetzlicher Nexus und Verarbeitung seit 1. Jänner 2026 sichern.
2. Steueransässigkeit und Meldepflicht für den konkreten Zeitraum beweisen; Staatsbürgerschaft ist nicht entscheidend.
3. Nach Art. 15 DSGVO alle §-18/§-20-Daten, Quellen, Zwecke, Empfänger, Zugriffe und Fristen verlangen.
4. Löschung, Einschränkung oder Widerspruch nach der sachlich passenden DSGVO-Norm verlangen und die Antwort sichern.
5. Eine eng gefasste §-24-DSG-Beschwerde gegen konkrete Verarbeitung erheben.
6. Zum BVwG gehen und eine entscheidungserhebliche Art.-267-Frage sowie erforderlichenfalls einen Antrag des Gerichts nach Art. 140 B-VG anregen.
7. Art.-144- beziehungsweise VwGH-Rechtsschutz ausschöpfen.

Für den Gold-Plating-Fall muss der Nutzer im relevanten Zeitraum ausschließlich in einem nicht teilnehmenden Staat steuerlich ansässig sein, keine relevante Doppelansässigkeit besitzen und trotzdem tatsächlich nach § 20 Abs. 1 verarbeitet werden. „Nicht-EU“ genügt nicht automatisch, weil auch teilnehmende Drittstaaten meldepflichtig sein können. Ein österreichischer Steuerresident ist im Regelfall gerade kein nicht meldepflichtiger Nutzer.

## Epicenter/AKVorrat: was der Präzedenzfall wirklich lehrt

Die erfolgreiche österreichische Vorratsdatenkampagne bestand aus mehreren Verfahren:

- G 47/2012: abstrakte Normprüfung auf Antrag der Kärntner Landesregierung;
- G 59/2012: Individualantrag Michael Seitlinger;
- G 62/2012 ua: Christof Tschohl plus 11.129 weitere Personen;
- VfGH-Vorlage vom 28. November 2012, EuGH C-594/12 verbunden mit C-293/12;
- Ungültigerklärung der Richtlinie 2006/24/EG am 8. April 2014;
- österreichische Aufhebung in G 47/2012 ua am 27. Juni 2014.

AKVorrat, seit 2016 epicenter.works, organisierte und finanzierte die Kampagne. Die erfolgreichen natürlichen Personen waren Seitlinger und Tschohl; die Organisation war nicht selbst die in den Urteilen genannte Individualantragstellerin.

Die 11.129 zusätzlichen Anträge wurden am 10. Juni 2014 abgewiesen, weil nur Tschohls konkrete Verträge und gegenwärtige Verarbeitung dargelegt waren. Eine allgemeine Kampagnenvorgabe, nur Betroffene sollten Vollmacht erteilen, ersetzte keine individualisierte Tatsachendarstellung. Dieser inhaltliche Mangel war nicht verbesserbar.

Die übertragbare Lehre ist daher nicht „Massenantrag funktioniert“, sondern: ein präziser Lead-Claimant, vollständige Individualfakten, exakter Anfechtungsumfang, tragfähige Verfahrensausnahme und eine entscheidungserhebliche EuGH-Frage.

## DAC2: der nächste und adverse Präzedenzfall

Die österreichische DAC2/CRS-Klage durchlief genau den heute naheliegenden Nutzerweg:

**DSB → BVwG W211 2232955-1/7E → VfGH E 2097/2021 → VwGH Ro 2023/04/0021.**

Gegenstand war ein deutsches Bankkonto eines österreichischen Bürgers mit einem Wert von rund EUR 40. VfGH und VwGH sahen keine ernstlichen Gültigkeitszweifel und keine Vorlagepflicht. Bereits verworfene Argumente umfassen anlasslose Vollerfassung, fehlende Bagatellgrenze, generelle Hacking-Risiken, Erfassung steuerehrlicher Personen und Gleichsetzung mit Kommunikationsmetadaten.

DAC8 muss deshalb präzise unterschieden werden. Gemeldet werden je Kryptowert und Kategorie jährliche Gesamtwerte, Einheiten und Anzahlen für Erwerbe, Veräußerungen, reportable retail payments und Transfers sowie aggregierte ausgehende Transfers an DLT-Adressen, die keinem qualifizierenden Intermediär zugeordnet sind.

Nicht gemeldet werden Wallet-/DLT-Adressen, einzelne Transaktionsdaten, Transaktions-IDs oder Gegenparteien. Eine behauptete Rekonstruktion über öffentliche Ledger braucht reproduzierbaren Sachverständigenbeweis und zusätzliche Daten; Rhetorik genügt nicht.

## Weitere Angriffspunkte

### § 15 Abs. 1 Z 1 und MiCA Art. 60

MiCA Art. 60 ist eine Mitteilung an die Behörde des Herkunftsmitgliedstaats; die gewöhnliche grenzüberschreitende Passport-Tätigkeit läuft über Art. 65. § 15 Abs. 1 Z 1 ist deshalb unionskonform am überzeugendsten als österreichische Home-State-Anknüpfung zu lesen.

Ein möglicher Doppelmeldungsfehler wird erst konkret, wenn Österreich einen ausländischen Art.-60-Anbieter allein wegen seiner Passport-Tätigkeit in Österreich ebenfalls zur Meldung verpflichtet. Vor einem Prozess sollte eine schriftliche BMF/FAG-Position eingeholt werden. Verneint die Behörde die österreichische Pflicht, verschwindet der Angriffspunkt; bejaht sie sie, kann dies eine besonders klare Art.-267-Auslegungsfrage werden.

### § 22 Abs. 2

Die jährlich neu entstehende Registrierungspflicht betrifft registrierungspflichtige Kryptowert-Betreiber außerhalb der MiCA-Art.-60/63-Schiene, nicht den gewöhnlichen MiCA-CASP. DAC8 überlässt den Mitgliedstaaten wirksame, verhältnismäßige und abschreckende Durchsetzungsmaßnahmen. Ein abstrakter Angriff ist schwach. Relevant wird die Norm bei tatsächlich kumulierten Sanktionen für fortgesetzte Nichtregistrierung; dann sind Verhältnismäßigkeit, Art. 49 Abs. 3 GRC und die konkrete Deliktsstruktur zu prüfen.

### Krypto-MPfG-DV

Die Durchführungsverordnung ordnet die Übermittlung der in § 18 Krypto-MPfG genannten Informationen über das FinanzOnline-Portal-Webservice an und verweist für XML/WSDL auf gesonderte BMF-Spezifikationen. Ohne die operative Spezifikation und eine konkrete Anforderung außerhalb der gesetzlichen Ermächtigung ist ein Verordnungsprüfungsantrag nicht sinnvoll. Die bloße Existenz der technischen Durchführungsvorschrift ist kein eigener Angriffspunkt.

### Erwerbsfreiheit, Gleichheit und Erwägungsgrund 12

Art. 6 StGG ist die sauberste CASP-Rüge, wenn eine trennbare österreichische Mehrbelastung konkret belegt wird. Die bloße Behauptung, DAC8 halte ein niedrigeres Schutzniveau für ausreichend, genügt ohne Vollharmonisierung nicht.

Eine Inländerdiskriminierung folgt nicht allein daraus, dass ein anderer Mitgliedstaat ein anderes Gesetz erlässt. Erforderlich sind ein tatsächlich passportender ausländischer Vergleichsanbieter, identische Leistungen und Kundengruppen, das ausländische Umsetzungsgesetz, der Nachweis, dass § 15 ihn nicht erfasst, und ein quantifizierter Wettbewerbsnachteil. G 107/2013 ist hierzu restriktiv; E 945/2016 lässt die Rüge bei echter unionsrechtlich vermittelter Schlechterstellung zu.

Erwägungsgrund 12, wonach der Verwaltungsaufwand für die Branche so gering wie möglich gehalten werden soll, ist Auslegungshilfe und kein selbstständiges Grundrecht oder Maximum-Harmonisierungsgebot. Er kann eine echte Unklarheit zugunsten der weniger belastenden Auslegung lösen, aber nicht allein eine Norm aufheben.

## Kandidaten für Art.-267-Fragen

### Nationale Mehrverarbeitung

> Sind Art. 8ad und Anhang VI Abschnitte II und III der Richtlinie 2011/16/EU in der Fassung der Richtlinie (EU) 2023/2226 in Verbindung mit Art. 25 dieser Richtlinie und Art. 5 Abs. 1 lit. b, c und e, Art. 6 Abs. 3 und Art. 23 DSGVO dahin auszulegen, dass sie eine nationale Regelung erlauben oder verlangen, nach der ein meldender Anbieter sämtliche den §-18-Krypto-MPfG-Kategorien entsprechenden Transaktionsinformationen für alle Transaktionen und Kryptowerte jedes Kunden ermitteln, erfassen, speichern und verarbeiten muss, unabhängig davon, ob dieser Kunde ein meldepflichtiger Nutzer ist?

Diese Frage ist für einen nicht meldepflichtigen Nutzer und einen CASP entscheidungsnäher als eine pauschale Ungültigkeitsrüge gegen DAC8.

### Gültigkeit von DAC8

> Sind die durch Richtlinie (EU) 2023/2226 verlangten, identitätsverknüpften jährlichen Werte, Einheiten und Anzahlen je Kryptowert und Transaktionskategorie mit Art. 7, 8 und 52 Abs. 1 GRC vereinbar, wenn die generalisierte Erfassung ohne individuellen Verdacht, die vorgelagerte Verarbeitung, Aufbewahrung, behördliche Zugriffe, Rechtsbehelfe und eine konkret nachgewiesene Korrelation mit öffentlichen Ledger-Daten gemeinsam berücksichtigt werden?

Die Vorlagefrage muss im konkreten Verfahren entscheidungserheblich sein. Ein Kläger kann eine Vorlage beantragen, aber nicht erzwingen. Ein nationales Gericht darf eine Gültigkeitsrüge verwerfen, aber nach *Foto-Frost* einen EU-Rechtsakt nicht selbst für ungültig erklären. Letztinstanzliche Gerichte müssen sich mit ordnungsgemäß erhobenen Vorlagefragen befassen und eine Nichtvorlage nach *Consorzio* und *KUBERA* begründen.

## Präzedenzfall-Balance

Unterstützend, aber unterscheidbar:

- *Digital Rights Ireland/Seitlinger*;
- *Tele2/Watson*, *La Quadrature*, *SpaceNet* und *Commissioner of An Garda Síochána*;
- VfGH G 72-74/2019 ua zum Bundestrojaner und Kfz-Daten;
- C-175/20, *Valsts ieņēmumu dienests*, zu Zweckbindung, Datenminimierung, Kriterien und Fristen;
- *Ligue des droits humains* und Gutachten 1/15 zu systematischen Profilen und Sicherungen;
- EGMR *Ferrieri and Bonassisa v Italy* zu präzisen Grenzen und wirksamer Kontrolle bei steuerlichem Bankdatenzugriff.

Advers oder begrenzend:

- österreichische DAC2-Trilogie;
- C-623/22, *Belgian Association of Tax Lawyers*, zur grundsätzlichen Verhältnismäßigkeit von DAC6;
- EGMR *G.S.B. v Switzerland* und *Othymia Investments* zur internationalen Steueramtshilfe;
- G 105/2025 und G 606/2015 ua zu breiten Daten- und Steuer-Compliance-Pflichten;
- *Unibet* und *État luxembourgeois* zum ausreichenden inzidenten Rechtsschutz;
- der Unterschied zwischen vertraulichem Behördenaustausch und öffentlicher Offenlegung in *Schecke* und *Luxembourg Business Registers*.

## Audit der DAC8.com/Bull-Bitcoin-Argumente

Tragfähig sind die anlasslose Systematik, Identitäts- und Adressverknüpfung, jährliche per-asset Aggregate, fehlende Bagatellgrenze und ein plausibles physisches Sicherheitsrisiko bei entsprechendem Beweis.

Zu qualifizieren sind die Reichweite der erfassten Anbieter, die tatsächliche Fähigkeit zur Blockchain-Korrelation und Behauptungen mangelnder Wirksamkeit. Die Kommission räumt Messlücken ein; der Europäische Rechnungshof dokumentiert Qualitäts-, Nutzungs- und Monitoringprobleme. Beides beweist keine generelle Untauglichkeit.

Nicht als DAC8-Feldschema haltbar sind Behauptungen, Wallet-Adressen, Daten, Transaktions-IDs oder Gegenparteien würden gemeldet, alle P2P-/DEX-/non-custodial Vorgänge seien erfasst oder jeder Datensatz werde unterschiedslos in 27 nationale Datenbanken repliziert.

Bull Bitcoin erklärt, am 24. Februar 2026 eine französische Klage eingebracht zu haben. Es wurde kein amtliches Aktenzeichen, Beschluss, Vorlagebeschluss oder gerichtsbestätigter Volltext gefunden. Das ist derzeit Parteivorbringen, kein Präzedenzfall.

## Priorisierte Beweisakte

### CASP

- MiCA-Art.-60/63/65-Status und österreichischer §-15-Nexus;
- schriftliche BMF/FAG-Auskunft zu streitigen Anknüpfungen;
- Feldherkunft und Datenfluss für jede §-18-Kategorie;
- getrennte Verarbeitung meldepflichtiger und nicht meldepflichtiger Populationen;
- §-20/§-39-Aufbewahrung, Löschjobs und Backups;
- bestehende MiCA-, TFR-, AML-, Rechnungslegungs- und Vertragsdaten;
- WFA-Baseline versus firmenspezifische Zusatzkosten;
- Rechnungen, Verträge, Tickets, FTE, Speicher, Security, DPIA und Art.-30-Dokumentation;
- reproduzierbarer Beweis einer behaupteten Public-Ledger-Korrelation;
- präziser Haupt- und Eventualantrag mit trennbarem Aufhebungsumfang.

### Nutzer

- exakte Steueransässigkeit und Meldepflicht im relevanten Zeitraum;
- realer CASP-Vertrag, Controller und österreichischer gesetzlicher Nexus;
- Datenschutzinformation, Selbstauskunft und Art.-15-Export;
- jedes tatsächlich gespeicherte, übermittelte und zugängliche Feld;
- konkrete Aufbewahrungsfrist und Lösch-/Einschränkungsantwort;
- tatsächlicher Report oder Bestätigung, dass kein Report erfolgt;
- Zugriffs-, Sicherheits- und Protokollierungsregeln;
- eine für die Entscheidung notwendige Vorlagefrage.

## Priorisierung der Fälle

| Fall | Einschätzung |
|---|---|
| Direkter Art.-140-Antrag eines gewöhnlichen Nutzers | Sehr geringe Zulässigkeit nach G 178/2024. |
| CASP-Art.-140-Antrag mit belegten Kosten | Gute Zulässigkeit; materielle Erfolgsaussicht nur bei präzisem nationalem Überschuss. |
| Nicht meldepflichtiger Nutzer gegen § 20 Abs. 1 | Plausibelster Datenschutzfall; über DSB/BVwG, mit tatsächlicher Speicher- und Löschakte. |
| Breite DAC8-Ungültigkeit als „Mass Surveillance“ | Niedrig bis offen; DAC2, C-623/22 und EGMR sind erhebliche Gegenjudikatur. |
| Zehn Jahre für alle Nutzer nach § 20 Abs. 4 | Als Behauptung falsch; § 20 Abs. 4 gilt für übermittelte Daten. |
| § 15-Host-State-Doppelmeldung | Potenziell stark, aber erst bei bestätigter breiter Behördenanwendung. |
| § 22 Abs. 2 | Schwach ohne richtigen non-MiCA-Antragsteller und tatsächliche Mehrfachsanktionen. |
| Krypto-MPfG-DV | Kein eigener Fall ohne konkreten ultra-vires Formatbefehl. |

## Forschungsgrenzen

- Keine reale CASP-Verarbeitungsakte, Kostenzerlegung oder Betroffenenanfrage lag vor.
- Die konkrete Liste teilnehmender Staaten muss für den behaupteten nicht meldepflichtigen Nutzer am Einreichungszeitpunkt geprüft werden.
- Keine österreichische Behördenauskunft zur Art.-60/65-Anwendung lag vor.
- Kein amtliches französisches Gerichtsaktenzeichen wurde gefunden.
- Das EDPS-PDF war automatisiert nicht lokal abrufbar; die amtliche Seite und URL sind im Manifest dokumentiert.
- Französische konsolidierte Volltexte waren wegen Publisher-WAF nicht lokal speicherbar; kanonische URLs sind als Remote-Lücken ausgewiesen.

## Wiki und Volltextkorpus

- [Strategie-These](../wiki/theses/vfgh-to-cjeu-dac8-route.md)
- [Gold-Plating- und Klägeraudit](../wiki/references/austrian-gold-plating-and-claimant-audit.md)
- [Epicenter/AKVorrat-Präzedenz](../wiki/references/epicenter-vorratsdatenspeicherung-precedent.md)
- [DAC2/CRS-Klage](../wiki/topics/dac2-crs-austrian-litigation.md)
- [Österreich/EU-Präzedenzmatrix](../wiki/references/austria-eu-precedent-matrix.md)
- [DAC8.com/Bull-Bitcoin-Audit](../wiki/references/dac8-com-argument-audit.md)
- [Volltext-Manifest](../../legal-docs/_index.md)
- [SHA-256-Prüfsummen](../../legal-docs/SHA256SUMS)

Dies ist ein Forschungsartefakt, keine Rechtsberatung und keine Prognose über Zulässigkeit, Vorlage oder Ausgang.
