---
title: "Technischer Gutachtenentwurf zu Finanzdatenprofilen"
type: report
summary: "Vertiefter quellen- und modellgestützter technischer Entwurf zu Finanzdatenprofilen: UTXO-/Account-Daten, Vertragsausführung, Wallet-/Sichtschlüssel, historische Zustände, L2, Attribution, Anbieterleaks und Zugriffsalternativen. Keine konkrete Produktivarchitektur geprüft."
sources:
  - wiki/references/financial-data-concentration-proof-and-alternatives.md
  - wiki/references/krypto-mpfg-provider-record-architecture.md
  - wiki/theses/transaction-data-wealth-inference.md
  - wiki/references/identity-to-public-ledger-linkage-evidence.md
  - wiki/references/financial-data-breach-and-security-authorities.md
  - wiki/references/bearer-asset-irreversibility-and-leak-consequences.md
  - wiki/references/austrian-tax-risk-scoring-and-financial-data-use.md
  - wiki/references/dac8-field-necessity-and-alternatives.md
  - wiki/references/austrian-security-evidence-access.md
  - wiki/references/bitcoin-utxo-observation-and-attribution.md
  - wiki/references/account-contract-chain-data-evidence.md
  - wiki/references/offchain-private-ledger-observation-limits.md
generated: 2026-09-30
verified: 2026-09-30
---

# Technischer Gutachtenentwurf zu Finanzdatenprofilen

**Technisch vertiefter Entwurf, Stand 30. September 2026.** Gegenstand: Erkenntnisgewinn, Fehlerrisiken und Sicherheitsfolgen langfristiger personenbezogener Finanzdatenbestände bei Anbietern und Behörden. Quellenarbeit mit LLM Wiki; eigene reproduzierbare Modellrechnungen. Verfasst als Arbeitsgrundlage für die anwaltliche Verwendung und die unabhängige sachverständige Prüfung.

Dies ist ein quellen- und modellgestützter technischer Entwurf, kein unterzeichnetes unabhängiges Sachverständigengutachten. Es wurden keine internen Anbieter- oder Behördenbestände geprüft und keine fremden Personen deanonymisiert. Die technischen Aussagen werden bereits begründet und bewertet; fehlende empirische Nachweise werden nicht durch angenommene Ergebnisse ersetzt. Die rechtliche Würdigung bleibt einer gesonderten Arbeit vorbehalten.

## 1 Auftrag und vorläufiges Gesamtergebnis

Untersucht wird, welches zusätzliche Wissen aus wiederkehrenden Finanzmeldungen, ihrer Aufbewahrung und ihrer Zusammenführung entstehen kann. Dazu gehören Aussagen über Aktivität und Vermögen, mögliche Verbindungen zu selbstverwahrten Kryptowerten sowie die Sicherheitsfolgen der Konzentration solcher Informationen. Ein zweiter Gegenstand ist, ob engere Daten- oder Zugriffskonzepte denselben konkret bestimmten Verwaltungsnutzen mit geringerer Exposition erreichen könnten. Die Untersuchung ist nicht auf DAC8 beschränkt; DAC8 und das österreichische Krypto-MPfG liefern einen besonders konkreten Anwendungsfall.

Das vorläufige Ergebnis hat fünf Teile:

1. **Ein Mehrjahresbestand ist informationsreicher als eine isolierte Jahresmeldung.** Bei verlässlicher Personenverknüpfung werden zeitliche Aktivitätsmuster, mehrere Anbieterbeziehungen und Wechsel sichtbar. Das gilt auch ohne eine einzige physische Gesamtdatenbank. Welche zusätzlichen Quellen eine bestimmte Behörde tatsächlich zusammenführt, ist dagegen noch nicht festgestellt.
2. **Aktivitätsdaten sind keine vollständige Vermögensbilanz.** Die eigenen Gegenbeispiele zeigen, dass identische Jahresmeldungen selbst über zehn Jahre mit stark unterschiedlichen Endbeständen vereinbar sind. Längere Beobachtung beseitigt unbekannte Anfangsbestände und nicht beobachtete Verfügungen nicht automatisch. Bestandsdaten und verifizierte Zusatzanker können diese Unbestimmtheit für Teilpositionen reduzieren.
3. **Ein verlässlicher Identitätsanker zu einer öffentlichen Blockchain kann den ursprünglichen Informationsumfang erheblich erweitern.** Dafür sind konkrete Adress- oder Transaktionsdaten wesentlich aussagekräftiger als Jahresaggregate. Transaktion, Dienst, Person, Schlüsselkontrolle und wirtschaftliches Eigentum sind unterschiedliche Beweisziele. Ein gelungener Treffer auf einer Stufe beweist die nächste nicht.
4. **Das Sicherheitsrisiko beginnt beim Anbieter, nicht erst bei der Steuerbehörde.** Dokumentierte Vorfälle belegen entwendete Identitäts- und Finanzdaten sowie nachfolgenden Täuschungsbetrug ohne entwendete private Schlüssel. Weitere Empfänger und zusammenführbare Jahrgänge können die Reichweite eines kompromittierten Zugangs erweitern. Eine systemspezifische Eintrittswahrscheinlichkeit ist aus diesen Vorfällen nicht ableitbar.
5. **Aufbewahrung und breite alltägliche Zugänglichkeit sind technisch trennbar.** Der eigene Archivvergleich demonstriert erhaltene Unterlagen bei engerem Routinezugriff. Er beweist weder praktische Sicherheitswirksamkeit noch gleichwertige Steuerprüfung im Produktivbetrieb. Öffentliche Vergleichsstudien zeigen sowohl mögliche Datenminimierung als auch messbare Nutzeneinbußen; sie ersetzen den aufgabenspezifischen Vergleich nicht.

Der Ausdruck „Vermögensregister light“ lässt sich technisch als personenbezogenes, mehrjähriges Profil aus beobachteten Positionen, Aktivitäten und abgeleiteten Vermögensindikatoren präzisieren. Er darf nicht als Feststellung eines vollständigen oder zuverlässig aktuellen Gesamt-Nettovermögens verstanden werden. Gerade die Differenz zwischen einem nützlichen Profil und einer unvollständigen Bilanz ist für Nutzen, Fehlzuordnung und Missbrauch wichtig.

## 2 Methode, Beweisstufen und Untersuchungsgrenzen

### 2.1 Was tatsächlich untersucht wurde

Der Entwurf beruht auf drei Methoden. Erstens wurden die einschlägigen Datenfelder und Aufbewahrungsvorgaben anhand öffentlich zugänglicher Primärquellen in ein technisches Beobachtungsmodell eingeordnet. Zweitens wurden dokumentierte Vorfälle und veröffentlichte Forschungsarbeiten auf den jeweils tatsächlich geprüften Endpunkt ausgewertet. Drittens wurden kontrollierte synthetische Beispiele mit einem beigefügten Python-Programm berechnet und durch Assertions geprüft. Assertions sind maschinelle Konsistenzprüfungen der vorgegebenen Modelle, kein Ersatz für eine empirische Validierung ihrer Annahmen.

Es handelt sich nicht um einen Penetrationstest, eine Untersuchung einer realen Meldeplattform oder die Reproduktion der externen Forschungsdatensätze. Die öffentlichen Studien werden als externe Befunde bewertet. Die eigene Modellrechnung benutzt ausschließlich erfundene Personenkennungen und Beträge. Sie zeigt logische Möglichkeiten, Gegenbeispiele und den Einfluss expliziter Annahmen, nicht deren Häufigkeit in einer realen Bevölkerung.

### 2.2 Vier verschiedene Aussagearten

| Aussageart | Was sie hier bedeutet | Reichweite |
|---|---|---|
| Normativer Eingaberahmen | Öffentlich festgelegtes Feld oder Frist | Kein Beweis, dass jede konkrete Implementierung korrekt oder identisch ist |
| Dokumentierter Befund | Öffentlich belegter Vorfall, Verwaltungsfall oder Forschungsversuch | Begrenzt auf dessen Zeitraum, Daten und Endpunkt |
| Eigene Modellanalyse | Nachvollziehbare Berechnung unter ausdrücklich festgelegten Annahmen | Logischer Mechanismus; keine gemessene Bevölkerungsquote |
| Noch offene Systemaussage | Behauptung über aktuelle Rollen, Kopien, Verknüpfungen oder Wirksamkeit | Benötigt tatsächliche Systemunterlagen oder kontrollierte Realdaten |

Ein gesetzlich vorgesehenes Feld ist nicht mit einer automatischen Verarbeitung durch jede Behörde gleichzusetzen. Technische Verknüpfbarkeit, rechtliche Befugnis und tatsächliche Verknüpfung werden deshalb getrennt geführt. Ebenso sind ein Angriffsweg und dessen konkrete Eintrittswahrscheinlichkeit unterschiedliche Aussagen.

### 2.3 Begriffe und Zielgrößen

„Bestand“ bezeichnet eine Position zu einem Zeitpunkt; „Bewegung“ einen Vorgang während eines Zeitraums. „Vermögen“ wird hier nicht unbemerkt zwischen Bruttobestand und Nettovermögen gewechselt. Gesamt-Nettovermögen setzt die sachgerechte Bewertung aller relevanten Positionen und Verbindlichkeiten voraus. Ein sichtbarer Kryptosaldo kann beliehen sein; eine Wallet kann fremde oder gemeinschaftliche Vermögenswerte enthalten.

„Zuordnung“ erhält stets einen Endpunkt: dieselbe Person über mehrere Meldungen, dieselbe öffentliche Transaktion, ein Dienstadressbestand, Schlüsselkontrolle oder wirtschaftliches Eigentum. „Exposition“ bezeichnet die Daten, die ein bestimmter Zugang tatsächlich erreichbar macht. Eine größere Zahl erreichbarer Felder ist nicht automatisch eine proportionale Erhöhung des Risikos; Inhalt und Verknüpfbarkeit verändern den möglichen Schaden.

## 3 Datenmodell: Meldung, Anbieterbestand und weitere Quellen

### 3.1 Die relevante Verarbeitungskette

Die technische Kette besteht mindestens aus Kundenidentifikation, Dienst- und Transaktionsaufzeichnungen, Bildung eines Meldeaggregats, Übermittlung, Speicherung beim Empfänger und späterer Verwendung. Diese Stufen können verschiedene Systeme, Verantwortliche und Dienstleister haben. Das Aggregat ist eine verlustbehaftete Zusammenfassung: Aus Einzeldaten kann eine Jahressumme gebildet werden; aus derselben Jahressumme lassen sich die Einzeldaten im Allgemeinen nicht eindeutig rekonstruieren.

Für das österreichische Beispiel meldet [§ 18 Krypto-MPfG](https://www.ris.bka.gv.at/Dokumente/BgblAuth/BGBLA_2025_I_96/BGBLA_2025_I_96.html) Identität und steuerliche Ansässigkeit sowie jährliche Werte und Einheiten je Kryptowert und Kategorie, meist auch Anzahlen. Wallet-Adressen, Transaktionshashes, Einzelzeitpunkte und Gegenparteien sind keine Routinefelder. Die Kategorie externer Adressen enthält Wert und Einheiten, keine Anzahl. Die Einstufung als dem Anbieter nicht bekannt mit einem Finanzinstitut oder Krypto-Dienstleister verbundene Adresse beweist keine Selbstverwahrung durch den Kunden.

Das folgende Modell trennt fünf Informationsschichten. Es beschreibt keine bereits vorgefundene österreichische Gesamtdatenbank.

| Schicht | Inhalt und zusätzliche Aussagekraft | Wesentliche Grenze |
|---|---|---|
| Jahresaggregate | Person, Anbieter, Zeitraum, Asset, Kategorie, Summen | Zeitliche Aktivität, keine einzelne Wallet oder vollständige Bilanz |
| Anbieter-Einzelunterlagen | Tatsächlich vorhandene Identitäts-, Auftrags-, Transfer- und Kontrollnachweise | Feldumfang hängt von Dienst und Rechtsgrundlage ab; keine automatische Behördenübermittlung |
| Kontobestandsdaten | Gemeldeter Jahresend-Saldo oder -Wert erfasster Konten | Beobachtete Teilposition, keine vollständige Vermögensabdeckung |
| Registerbeziehungen | Etwa Person–Konto- oder Person–Gesellschaft-Beziehung | Beziehung ist nicht deren Wert oder wirtschaftliche Alleinzuordnung |
| Öffentlicher Ledger | Chain-spezifische Vorgänge und Positionen nach einem verlässlichen Anker | Keine automatische Person, Schlüsselkontrolle oder rechtliche Eigentumsposition |

Die GMSG-Bestandsfelder ergeben sich aus [§ 3 Abs. 2 Z 3 und § 7 GMSG](https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20009250). Ihre technische Funktion unterscheidet sich von derjenigen der Kryptobewegungen. Ein gemeldeter Kontosaldo kann eine konkrete Teilposition direkt beobachten; eine kumulierte Kaufsumme nur eine Finanzierung oder Aktivität anzeigen. Die Verbindung beider Arten kann zusätzliche Widersprüche oder Ergänzungen sichtbar machen, bleibt aber von Abdeckung und korrekter Zuordnung abhängig.

### 3.2 Wie Daten verbunden werden können

Ein belastbarer Join, also eine Zusammenführung, benötigt kompatible Schlüssel und eine gültige Bedeutung. Eine Steueridentifikation muss zum richtigen Staat und Identifikationssystem gehören. Ein Name allein ist kein verlässlicher eindeutiger Schlüssel. Adresse und Geburtsdatum können helfen, können aber veraltet, falsch oder geteilt sein. Namensänderungen und mehrere Ansässigkeiten verlangen dokumentierte Regeln. Jeder Abgleich muss „keine Entscheidung“ zulassen, statt unklare Fälle zwangsläufig einer Person zuzuweisen.

Im technischen Sollmodell wird deshalb jede Zuordnung mit Quelle, Zeitbezug, Schlüsselart und Begründung gespeichert. Rohmeldungen bleiben von abgeleiteten Merkmalen getrennt. Eine korrigierte Identität oder ein widerrufenes Dienstlabel muss auffindbare abhängige Ergebnisse korrigieren können. Sonst kann ein einmaliger Fehler Jahrgänge und Quellen übergreifend fortwirken.

Ein Verbund muss keine physisch zentrale Datei sein. Eine Suchoberfläche, die mehrere getrennte Bestände unter derselben Personenkennung abfragt, kann funktional ein Gesamtdossier erzeugen. Die umgekehrte Folgerung wäre falsch: Daten im Verantwortungsbereich derselben Institution müssen nicht automatisch gemeinsam zugänglich sein. Entscheidend sind tatsächlich mögliche Abfragen, Rollen und Exporte, nicht die Zahl der Server.

### 3.3 Kopien und Fristen gehören zum Datenmodell

Zu unterscheiden sind produktiver Bestand, übermittelte Kopie, Pflichtarchiv, Backup, Export, Arbeitsdatei und abgeleitetes Merkmal. Die Löschung einer Ausgangstabelle beseitigt nicht von selbst eine zuvor exportierte Datei oder einen gespeicherten Adressanker. Das ist eine technische Folge mehrerer Kopien, keine Aussage über deren rechtlich zulässige Dauer. Ein wirksames Lebenszykluskonzept benötigt für jede Kopienklasse eigene Trigger und überprüfbare Lösch- oder Sperrmechanismen.

Für Anbieter bestimmt [§ 20 Abs. 1 und 4 sowie § 39 Krypto-MPfG](https://www.ris.bka.gv.at/Dokumente/BgblAuth/BGBLA_2025_I_96/BGBLA_2025_I_96.html) Erfassung unabhängig von persönlicher Meldepflicht sowie zehnjährige Fristen ab Ende des Bezugs-Meldezeitraums für die bezeichneten Informationen beziehungsweise Dokumente. Die [Materialien zu § 20, RV 306](https://www.parlament.gv.at/dokument/XXVIII/I/306/fnameorig_1723216.html) bestätigen eine Aufbewahrungs- und Löschpflicht. Diese Anbieterfrist wird im Modell nicht als Frist aller Behördenkopien verwendet.

Weitere notwendige Aufzeichnungen können unabhängig bestehen: [§ 21 FM-GwG](https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20009769) knüpft die heutige zehnjährige Frist grundsätzlich an das Ende der Geschäftsbeziehung oder die gelegentliche Transaktion; [MiCA Art. 68 Abs. 9](https://eur-lex.europa.eu/eli/reg/2023/1114/oj/eng) und [TFR Art. 26](https://eur-lex.europa.eu/eli/reg/2023/1113/oj/eng) haben eigene Gegenstände und Fristen. Eine Aufhebung nur einer Grundlage löscht daher nicht notwendig dieselben Daten unter anderen Grundlagen. Die grundsätzlich ab 10. Juli 2027 geltende [AMLR, Art. 77 und 90](https://eur-lex.europa.eu/eli/reg/2024/1624/oj/eng), verlangt eine gesonderte Übergangsbetrachtung; heutige Fristen werden nicht unbesehen zehn Jahre in die Zukunft fortgeschrieben.

Für Behördenkopien, Analysemerkmale und Sicherungen liegt hier kein verifiziertes vollständiges Fristeninventar vor. Ein generelles unbegrenztes Behördenarchiv wird deshalb ebenso wenig angenommen wie eine automatische Zehnjahreslöschung sämtlicher Kopien.

## 4 Mehrjahresprofile und Vermögensschlussfolgerungen

### 4.1 Sicherer Erkenntniszuwachs: zeitliche und anbieterübergreifende Aktivität

Wenn derselben Person Jahr für Jahr Käufe, Veräußerungen und andere Kategorien zugeordnet werden können, entsteht eine Zeitreihe. Sie kann wiederkehrende Erwerbsaktivität, Wechsel der verwendeten Assets, das Hinzutreten eines Anbieters und auffällige Änderungen zeigen. Das Wissen ist nicht bloß die wiederholte Kenntnis desselben Einzelbetrags. Ein einzelnes Jahr beantwortet beispielsweise nicht, ob eine Tätigkeit neu ist oder regelmäßig stattfindet; mehrere Jahre können das innerhalb ihres Beobachtungsbereichs unterscheiden.

Dieser Zuwachs ist zunächst deskriptiv: Er betrifft die erfasste Aktivität. Schon eine korrekt gebildete Zeitreihe kann für eine Nachfrage, Plausibilitätsprüfung oder Zielauswahl nützlich sein. Ihre Aussage darf aber nicht unbemerkt zu „diese Person verfügt heute über die Summe ihrer früheren Käufe“ aufgewertet werden. Das wäre eine andere Zielgröße mit zusätzlichen Voraussetzungen.

Eine längere Reihe kann zufällige Schwankungen verringern und konsistentere Muster zeigen. Sie kann ebenso veraltete Identitäten, wechselnde wirtschaftliche Berechtigungen oder systematische Erfassungsfehler ansammeln. Ein zusätzlicher Jahrgang garantiert daher keinen zusätzlichen Nutzen für jede Aufgabe. Der Mehrwert ist gegen ein konkret benanntes Ergebnis zu messen: etwa eine zutreffende Unstimmigkeit, eine richtige Nachforderung oder die Fehlerverteilung einer Bestandsprognose.

### 4.2 Durchgerechnetes Gegenbeispiel: dieselbe Meldung, anderes Vermögen

Im Modell werden zwei mögliche Welten derselben synthetischen Person verglichen. In beiden erwirbt sie jedes Jahr 1 BTC um 60.000 Euro beim betrachteten Anbieter und überträgt diesen anschließend an eine zunächst eigene externe Adresse. Die gemeldeten Jahreskategorien sind identisch. In Welt A hält sie die erworbenen Einheiten. In Welt B verschenkt sie diese nach der Auszahlung, ohne dass der spätere Vorgang beim betrachteten Anbieter beobachtet wird. Beide Welten beginnen ohne BTC; Gebühren, Kursänderungen und sonstige Positionen sind in diesem Kontrollfall ausgeschlossen.

| Zahl beobachteter Jahre | BTC-Endbestand Welt A | BTC-Endbestand Welt B |
|---|---|---|
| 1 | 1 | 0 |
| 3 | 3 | 0 |
| 5 | 5 | 0 |
| 10 | 10 | 0 |

Die Beobachtungen bleiben in allen vier Horizonten gleich, die Endbestände nicht. Damit ist ein vollständiger aktueller Bestand aus diesen Meldungen allein **nicht eindeutig identifizierbar**. Das ist ein logisches Ergebnis, keine Vermutung über die übliche Häufigkeit von Schenkungen. Ein einziger zulässiger Gegenfall widerlegt eine behauptete stets eindeutige Rekonstruktion; er widerlegt nicht jede statistisch nützliche Schätzung.

Unter der Zusatzannahme „keine spätere Verfügung und keine anderen BTC-Positionen“ wäre Welt A korrekt rekonstruierbar. Genau diese Voraussetzung ist aber nicht in den Jahresfeldern enthalten. Wird sie nur angenommen, muss das Resultat als konditionale Schätzung bezeichnet werden. Ein statistisches Modell könnte ihr anhand weiterer Daten eine Wahrscheinlichkeit geben; dafür benötigt es eine geeignete Vergleichsstichprobe und bekannte tatsächliche Bestände. Eine frei gewählte Annahme über typisches Halten ist keine gemessene Genauigkeit.

Das Modell ist absichtlich einfacher als die Realität. Unbekannte Anfangsbestände würden weitere vereinbare Endbestände zulassen. Eine verfügbare öffentliche Auszahlungstransaktion könnte den Folgeweg eingrenzen, aber eine spätere Schlüsselübergabe oder wirtschaftliche Übertragung muss nicht als erkennbare Eigentumsänderung on-chain erscheinen. Das Gegenbeispiel betrifft die Aussagekraft der festgelegten Beobachtung, nicht die Unmöglichkeit jeder zusätzlichen Ermittlung.

### 4.3 Bruttoumsatz misst nicht den gebundenen Bestand

Im zweiten Modell werden 10.000 Euro zwanzigmal vollständig eingesetzt: kaufen, zum unveränderten Preis verkaufen, denselben Betrag wieder verwenden. Ohne Gebühren entstehen 200.000 Euro Bruttokäufe und 200.000 Euro Bruttoverkäufe. Am Ende verbleiben 10.000 Euro, nicht 200.000 oder 400.000 Euro. Hohe Bruttowerte können daher Handelshäufigkeit statt hohen Bestand abbilden.

Auch die Differenz von Käufen und Verkäufen ist noch keine Gesamtvermögensrechnung. Ein Kauf tauscht Geld gegen ein anderes Asset; er schafft nicht schon für sich zusätzliches Nettovermögen. Eine richtige Bilanz muss Positionen, Bewertungszeitpunkte, Mittelherkunft und Verbindlichkeiten berücksichtigen. Kategorien mit unterschiedlichen Bewertungsregeln dürfen nicht ungeprüft in einer gemeinsamen Geldsumme verrechnet werden. Bei Krypto-zu-Krypto-Tausch kann derselbe wirtschaftliche Vorgang mehrere gemeldete Seiten haben.

Die praktische Fehlerfolge ist bedeutsam: Ein Ranking nach Bruttokäufen kann Vielhandelnde vor vermögendere Langzeithalter reihen. Die Rangfolge ist dann eventuell für Aktivitätsprüfung brauchbar, aber nicht als verifiziertes Vermögensranking. Für Missbrauch genügt einem Angreifer möglicherweise schon dieser ungenaue Hinweis; für eine hoheitliche Tatsachenfeststellung muss die Zielgröße genauer begründet werden.

### 4.4 Anbieterübergreifende Daten: Ergänzung und Doppelzählung

Ein Transfer derselben 1 BTC vom Konto einer Person bei Anbieter A zu ihrem Konto bei Anbieter B ist wirtschaftlich kein neuer Erwerb dieser Person. Zwei Beobachtungen desselben Transfers dürfen nicht als zwei zusätzliche Vermögenspositionen addiert werden. Wird der Vorgang nur als jährlicher Abgang und Zugang ohne individuellen Anker gesehen, sind ein Eigenübertrag und unabhängige Vorgänge unter Umständen mit demselben Aggregat vereinbar.

Im dritten Modell werden solche nicht unterscheidbaren Beobachtungen gegenübergestellt. Ein gemeinsamer geprüfter Transaktionsanker und die gesondert bekannte Personenbeziehung können den konkreten Eigenübertrag identifizieren. Die Jahresgleichheit des Betrags allein kann das nicht. Ein Transaktionshash kennzeichnet zudem eine Transaktion, nicht zwingend einen einzelnen Empfänger: Bei Sammeltransaktionen müssen Chain, Output beziehungsweise Ereignis und Anbieterzuordnung hinzukommen.

Für einen belastbaren Verbund sind daher Bewegungen als Vorgänge und Bestände als Positionen zu modellieren. Ein Ereignis kann mehrere Quellenbelege haben, ohne mehrfach gezählt zu werden. Unterschiedliche Quellen liefern einen Mehrwert, wenn sie zusätzliche Abdeckung oder Bestätigung bringen. Sie liefern nicht automatisch unabhängige Bestätigung, wenn beide aus derselben ursprünglichen Anbieteraufzeichnung stammen.

### 4.5 Die Fristuhr läuft für jeden Jahrgang getrennt

Das Modell setzt für den Jahrgang 2026 das Ende des Bezugszeitraums auf 31. Dezember 2026 und das Ende der Zehnjahresfrist auf 31. Dezember 2036. Der neue Jahrgang 2036 hat eine eigene Frist bis Ende 2046. Seine Aufnahme setzt die Uhr des Jahrgangs 2026 nicht zurück. Ein kontinuierlich nachwachsender Bestand kann deshalb eine dauerhafte Profilierungsfunktion behalten, ohne dass jeder einzelne Ursprungsdatensatz unbegrenzt aufbewahrt wird.

Die genaue Zahl gleichzeitig vorhandener Jahrgänge hängt vom Stichtag, der Meldeverzögerung und der tatsächlichen Löschumsetzung ab. „Zehn Jahre“ wird hier nicht pauschal mit genau zehn Tabellenzeilen zu jedem Zeitpunkt gleichgesetzt. Ein archivierter Vorgang, seine spätere Übermittlung und ein daraus abgeleitetes Merkmal sind ebenfalls verschiedene Objekte.

Für die 2026 beginnenden Kryptomeldungen ist eine zehnjährige Meldereihe heute noch kein empirisch beobachteter Bestand. Die erste Übermittlung erfolgt für 2026 erst 2027; [§ 19 Krypto-MPfG](https://www.ris.bka.gv.at/Dokumente/BgblAuth/BGBLA_2025_I_96/BGBLA_2025_I_96.html) regelt die Abgabe bis 31. Juli. Der hier untersuchte längere Horizont ist ein Szenario der fortlaufenden Sammlung. Er wird nicht als bereits gemessene österreichische Kryptoarchitektur ausgegeben.

### 4.6 Wann die Bezeichnung „Vermögensregister light“ sachgerecht ist

Sachgerecht ist die Bezeichnung als Kurzform für eine Funktion: Eine Person kann über Jahre mit verschiedenen beobachteten Finanzpositionen, Bewegungsmustern und Vermögensindikatoren auffindbar werden. Sie setzt weder lückenlose Vermögenskenntnis noch eine neue gesetzlich so bezeichnete Datenbank voraus. Durch Kontosalden, Registerbeziehungen und verlässliche Blockchain-Anker kann dieses Profil dichter werden als eine einzelne Bewegungsmeldung.

Nicht gerechtfertigt wäre die weitergehende Feststellung, aus jeder zehnjährigen Reihe lasse sich der gesamte aktuelle Besitz relativ genau berechnen. Der Entwurf findet dafür keine empirische Grundlage. Die Gegenmodelle zeigen strukturelle Lücken; Schulden, Fremdzuordnung und nicht erfasste Positionen kommen hinzu. Die technisch tragfähige Aussage lautet daher: **Langfristige, personenbezogen verknüpfbare Finanzdaten können ein bestandsnahes Teilprofil ermöglichen; dessen Umfang und Genauigkeit sind quellen- und personenbezogen zu prüfen.**

Auch „Vorratsdatenspeicherung“ ist hier zunächst eine beschreibbare Architekturfrage: Werden Informationen breit und länger für möglicherweise erst später ausgewählte Prüfungen verfügbar gehalten? Ob diese Struktur rechtlich mit einer bestimmten Vorratsdaten-Rechtsprechung vergleichbar ist, entscheidet dieser technische Entwurf nicht. Er liefert dafür die Merkmale: Anlass der Erfassung, Kreis der Betroffenen, Inhalt, Dauer, Verknüpfbarkeit und Zugriffswege.

## 5 Was tatsächliche österreichische Verwendung bereits belegt

Öffentliche Quellen belegen sowohl reale Datenverwendung als auch Grenzen der Integration. Die [BiRank-Studie, SNAMS 2021, Autorenfassung 2022, S. 1–3 und 5–6](https://arxiv.org/pdf/2209.01945), verband Firmenbuchfunktionen aus 1991–2021 über Namen und Adressen mit Steueridentitäten und Risikoindikatoren. Es handelte sich um ein BMF-finanziertes Forschungsverfahren mit PACC-Beteiligung. Das belegt eine implementierte quellenübergreifende Analyse, nicht heutigen Produktivbetrieb, CRS-/Kryptoinputs oder Gesamtvermögensrekonstruktion. Der zusätzliche Beitrag zum finalen Mehrmodell-Scoring blieb Zukunftsarbeit; die Referenzlabels waren teilweise statistische Risikomarkierungen.

Der [BFG-Fall RV/1300013/2020 vom 15. September 2022, S. 2–3 und 13](https://findok.bmf.gv.at/findok/resources/pdf/a1da345e-f5af-48f0-aab6-ce1431889289/140447.1.1.pdf), zeigt tatsächliche Verwendung ausländischer Kontomeldungen für 2017 und 2018. Es folgten Nachfragen und eine entrichtete Steuernachforderung von 33.356 Euro für 2017. Ein konkreter Kontrollnutzen ist damit dokumentiert. Der Fall isoliert nicht den Zusatznutzen des zweiten Jahres und belegt keine Notwendigkeit einer zehnjährigen Frist.

Im [BFG-Fall RV/5100216/2024 vom 20. Juni 2024, S. 2–3, 10–11 und 21–24](https://findok.bmf.gv.at/findok/resources/pdf/f3aa604f-ec13-4ee9-ace3-cba2eaa2759b/144911.1.1.pdf), wurden bei einer GMSG-Kontrolle elektronische Konto-/Depotlisten für 2020 und 2021 einschließlich nicht meldepflichtiger Beziehungen angefordert. Das BFG billigte die konkrete Anforderung. Nachforderungen sind somit ein dokumentierter Zugang zu zusätzlichen Informationen, nicht bloß eine abstrakte Möglichkeit. Vollständige spätere Übermittlung oder Profilbildung ist damit nicht festgestellt; der aktuelle Abschluss einer zugelassenen Revision wurde hier nicht verifiziert.

Der [Rechnungshofbericht Bund 2026/5, gedruckte S. 101–107, TZ 22–23](https://www.parlament.gv.at/dokument/XXVIII/III/292/imfname_1739208.pdf), unterscheidet dagegen verfügbare Plattformdaten, manuelle Nutzung und engere automatisierte Auswahl. Er berichtet keine bereits vollzogene universelle Datenverknüpfung. Empfehlungen für breitere Integration und angekündigte Erweiterungen sind keine gemessenen Ergebnisse; der Bericht betrifft nicht die hier gesuchten CRS-/Kryptomerkmale.

**Technische Bewertung:** Datenzusammenführung ist weder eine bloß erfundene Möglichkeit noch als allumfassender österreichischer Produktivbestand nachgewiesen. Für den konkreten Gutachtengegenstand fehlt ein aktuelles Inventar tatsächlich verwendeter Quellen, Merkmale, Join-Schlüssel und Zugriffsrollen. Der Entwurf hält deshalb belegte Nutzungsfälle, mögliche Architektur und heutige Umsetzung getrennt. Ein positiver Steuerfall gehört in den Alternativenvergleich ebenso wie ein begrenzter oder ausbleibender Zusatznutzen.

## 6 Blockchain-Zuordnung und zusätzliches Personenwissen

### 6.1 Direkte Anker und bloße Kandidaten

Ein dokumentierter Transaktionshash in der richtigen Chain erlaubt den Abruf ihres veröffentlichten Transaktionsdatensatzes, nicht automatisch etwaiger verdeckter Inhalte. Bei öffentlich adressbezogenen Ledger-Daten erlaubt eine bekannte Adresse die Untersuchung des entsprechenden Verlaufs. Beides sind direkte Anker für den jeweils sichtbaren Ausschnitt. Ein genauer Betrag in einem engen Zeitfenster liefert dagegen zunächst Kandidaten; ein Jahresaggregat liefert einen viel gröberen Beobachtungsraum. Bei vielen Vorgängen kann dieselbe Summe durch unterschiedliche Kombinationen entstehen. Interne Anbieterbuchungen müssen überhaupt keine einzelne On-Chain-Entsprechung haben.

Es wäre daher methodisch falsch, eine hohe Zuordnungsquote aus einer Untersuchung mit konkreten Adressen oder Minutenfenstern auf Jahresaggregate zu übertragen. Auch eine Anzahl von eins in einer Meldekategorie macht eine öffentliche Transaktion nicht ohne Weiteres eindeutig. Sie bezeichnet eine Kategorie beim Anbieter, nicht automatisch einen einzigen sichtbaren Blockchain-Vorgang. Für das reine jährliche Feldtupel liegt hier kein validierter empirischer Zuordnungstest vor.

Gesonderte Anbieterunterlagen können wesentlich stärkere Anker liefern. [Verordnung 2025/1140, Art. 1 und Anhang, Tabellen 3–4](https://eur-lex.europa.eu/eli/reg_del/2025/1140/oj/eng), verbindet für ihren Anwendungsbereich personenbezogene Käufer-/Verkäuferdaten und gegebenenfalls On-Chain-Daten über eine interne Transaktionsnummer. Die [TFR, Art. 14–16](https://eur-lex.europa.eu/eli/reg/2023/1113/oj/eng), enthält Angaben für erfasste Transfers und besondere Prüfungen selbstgehosteter Adressen. Das sind separate Aufzeichnungs- und Prüfpflichten, keine Erweiterung der Routine-Jahresmeldung. Eine Pflicht zur Kontrollprüfung beweist nicht die fehlerfreie Kontrolle im konkreten Fall; das Vorhandensein eines Datensatzes nicht seine automatische Steuerbehördenverwendung.

### 6.2 Was eine Blockchain technisch bestätigt — und was nicht

Ein Ledger ist zunächst ein nach Protokollregeln fortgeschriebener Zustand beziehungsweise eine geordnete Folge von Vorgängen. Bei Bitcoin werden bestehende ausgebbare Outputs verbraucht und neue erzeugt. Bei Ethereum werden Konten und Vertragszustände durch Ausführung verändert. Die Datenstruktur und ihre Validierung begrenzen mögliche Vorgänge; sie füllen aber keine außerhalb des Protokolls liegenden Tatsachen automatisch aus. Ein Kundenname, Kaufvertrag oder wirtschaftlicher Berechtigter ist kein notwendiger Bestandteil einer gewöhnlichen nativen Übertragung.

Die [Bitcoin-Grundschrift, Abschnitte 3–5 und 8](https://bitcoin.org/bitcoin.pdf), beschreibt Hashverkettung, Validierung und Einschlussbeweise. Ein kryptografischer Hash ist ein aus den Daten berechneter Prüfwert, keine Verschlüsselung der Daten. Eine Signatur bestätigt eine bestimmte Autorisierung nach den geprüften Regeln, nicht den bürgerlichen Namen hinter einem Schlüssel. Konsens bestimmt, welcher gültige Verlauf als maßgeblich behandelt wird; er ist keine Abstimmung darüber, ob eine beigefügte Behauptung wirtschaftlich wahr ist.

Für das Gutachten sind drei Ebenen zu unterscheiden. **Konsensdaten** sind Bestandteil des validierten Verlaufs, etwa ein verbrauchter Outpoint oder bestätigter Vertragszustand. **Reproduzierbare Ergänzungen** entstehen durch weitere Berechnung, etwa Input-Beträge aus früheren Outputs oder rekonstruierte Vertragsaufrufe. **Externe Deutung** verbindet diese Daten mit einem Dienst, einer Person oder einem Zweck. Eine gute Datenpipeline markiert diese Ebenen getrennt. Reproduzierbarkeit einer Berechnung beseitigt keine falsche externe Annahme.

Das öffentliche Ausgangsmaterial erlaubt dennoch weit mehr als eine isolierte Kontomitteilung: Bereits gespeicherte Vorgänge lassen sich erneut auswerten, neue Labels können ältere Beziehungen erklären, spätere Ausgaben können frühere Adressgruppen erweitern. Für diese zusätzliche Auswertung muss die betroffene Person nicht erneut beim Anbieter handeln. Ob und wie weit sie gelingt, hängt vom Datenmodell, Anker und Beobachter ab. Gerade diese bedingte Wiederverwendbarkeit unterscheidet einen Identitätsanker von einem abgeschlossenen Einzelbeleg.

„Die Blockchain beweist es“ ist daher nur mit einem genau benannten Objekt sinnvoll. Sie kann einen bestätigten Vorgang und seinen Protokollzustand sehr gut dokumentieren. Ob ein Mensch die Schlüssel selbst hält, treuhändig handelt, einen Anspruch verloren hat oder eine Zahlung für jemand anderen ausgeführt hat, bleibt eine zusätzliche Frage. Die Unvollständigkeit dieser Eigentumsprüfung macht das technisch sichtbare Aktivitätsprofil nicht wertlos; sie verhindert lediglich seine unbemerkte Umbenennung in eine vollständige Vermögensbilanz.

### 6.3 Bitcoin: Outputs, Skripte und die tatsächliche Wertrechnung

Bitcoin besitzt im UTXO-Modell kein obligatorisches personenbezogenes Konto mit einem gespeicherten Kontosaldo. Ein UTXO ist ein noch nicht ausgegebener Transaktionsoutput. Er enthält einen Wert und ein Sperrskript: Bedingungen, unter denen eine spätere Transaktion ihn ausgeben darf. Eine Adresse ist eine gebräuchliche Kodierung für bestimmte Empfangs-/Skriptarten, nicht ein Eigentümerfeld. Nicht jedes Skript hat eine eindeutige herkömmliche Adresse. Die Wallet ist Software mit Schlüsseln, Skriptwissen und Metadaten; ihre vollständigen Grenzen stehen nicht als „Wallet-ID“ in der Chain.

Der geprüfte [Bitcoin-Core-Quellstand, transaction.h, Strukturen COutPoint/CTxIn/CTxOut und Serialisierung](https://github.com/bitcoin/bitcoin/blob/4b612c6bf8cfa319a9df130d4b3d0523fddb6579/src/primitives/transaction.h), enthält in einem Input den Verweis auf eine frühere Transaktion samt Output-Index, Skript-/Witnessdaten nach Format und Sequenzangaben. Der Input-Betrag muss aus dem referenzierten Output ergänzt werden. Neue Outputs enthalten ganzzahlige Werte und Sperrskripte. Eine gewöhnliche Gebühr wird als Inputsumme minus Outputsumme berechnet; sie ist kein eigenständiges Empfänger-Output. Die besondere Coinbase-Transaktion wird nicht nach derselben Inputrechnung behandelt.

Im synthetischen Modell C1 werden zwei frühere Outputs von 0,7 und 0,5 BTC verbraucht. Die neue Transaktion erzeugt 0,4 und 0,7999 BTC. Aus ergänzten Input-Beträgen folgt 1,2 minus 1,1999 = 0,0001 BTC Gebühr. Fehlt der frühere zweite Output, weist das Programm die Betragsberechnung zurück, statt ihn als null zu behandeln. Die Rechnung ergibt weder einen Vermögenszuwachs von 1,2 BTC noch den Beweis, welcher neue Output Wechselgeld ist.

| Beobachtung im Beispiel | Direkt berechenbar | Zusätzliche ungeprüfte Annahme |
|---|---|---|
| Zwei verbrauchte Outputs | Beide Outpoints und ergänzte Inputsumme 1,2 BTC | Beide gehören wirtschaftlich derselben Person |
| Zwei neue Outputs | Werte 0,4 und 0,7999 BTC; Skripte werden im Modell nicht simuliert | Der größere oder ungerade Betrag ist sicher Wechselgeld |
| Differenz der Summen | 0,0001 BTC Gebühr | Die ganze Differenz sei Teil einer Zahlung an den sichtbaren Empfänger |

Die Identität eines konkreten Outputs besteht aus **Transaktionskennung plus Index**, gewöhnlich `txid:vout`. Ein Transaktionshash allein benennt bei einer Sammelauszahlung mehrere mögliche Kundenoutputs. Ein Indexer kann dem Nutzer übersichtliche Input-Adressen anzeigen; sie sind aus früheren Skripten erschlossen und nicht zusätzlich als Kundennamen in jedem Input gespeichert. Für einen Anbieteranker muss deshalb die Zuordnung zwischen Kundenauftrag und tatsächlichem finalem Output gesichert sein.

[BIP 141, Transaction ID und Witness program](https://bips.dev/141/), unterscheidet den traditionellen txid vom witness-einschließenden wtxid. Die Trennung von Witnessdaten ist keine Verschlüsselung. Bei bestimmten Ausgaben werden ein öffentlicher Schlüssel oder ein ausgeführtes Skript erkennbar; Outputs und Ausgabegraph bleiben beobachtbar. Ein Datensatz mit einem vermeintlichen „Transaktionshash“ muss seine Kennungsart festlegen, damit nicht zwei Hasharten als unterschiedliche wirtschaftliche Vorgänge gezählt werden.

Ein Transaktions-Locktime-Feld ist eine Ausführbarkeitsbedingung, kein gemessener Zeitpunkt des Kundenauftrags. Blockzeit und lokale Mempool-Empfangszeit gehören zum Beobachtungskontext. Sie liefern keine sekundengenaue universelle Erstellungsuhr. Bei Jahresgrenzen kann das für die Abgrenzung Auftrag, Broadcast, Bestätigung und Anbieterbuchung entscheidend sein. Die Zeitannahme muss vor einem Matchingtest festgelegt werden, nicht nach dem erwünschten Treffer.

Für einen BTC-Stichtagsbestand ist unter vollständiger Skriptzuordnung die Summe der zugeordneten, am Stichtag unspent Outputs sinnvoll. Ein jemals empfangener Gesamtbetrag ist eine andere Größe. Derselbe wirtschaftliche Bestand kann mehrfach umgeschichtet werden und dabei mehrfach als Eingang erscheinen. Gesperrte, geteilte oder fremdverwahrte Positionen verlangen außerdem eine Aussage zu Verfügbarkeit und Berechtigung. Ein sichtbarer UTXO ist deshalb ein überprüfbares Bilanzobjekt, aber noch keine vollständige Personenzuordnung.

### 6.4 Wallet-Erweiterung: Heuristik, Schlüsselzweig und Fehlerfortpflanzung

Die Common-Input-Heuristik vermutet, dass gemeinsam ausgegebene Inputs zusammengehören. Das kann bei gewöhnlich durch eine Wallet finanzierten Transaktionen nützlich sein, ist aber keine Konsensregel. [BIP 78, Motivation und Impacted heuristics](https://bips.dev/78/), beschreibt einen konstruktiven Gegenfall: Bei PayJoin kann der Empfänger eigene Inputs zu einer Zahlung beitragen. Auch gemeinschaftliche Transaktionen wie CoinJoin verlangen eine andere Behandlung. Dass eine Gegenkonstruktion existiert, beweist nicht ihre Häufigkeit; es widerlegt den universellen Satz „alle Inputs haben denselben wirtschaftlichen Eigentümer“.

Modell C1 lässt deshalb bei **identischer beobachteter Input-/Output-Projektion** zwei Eigentumswelten zu: In einer gehören beide Inputs X, in der anderen X und Y. Das Modell erzeugt keine vollständige PayJoin-Transaktion und prüft keine Signaturen. Es macht die logische Lücke sichtbar: Die betrachteten Graph-/Betragsdaten enthalten das stipulierte Eigentümerfeld nicht. Ein beobachteter gemeinsamer Input kann ein Anhaltspunkt sein; ein Schluss auf X verlangt zusätzliche Belege oder eine empirisch validierte Annahme.

Wechselgeldheuristiken versuchen den eigenen Rückfluss zu erkennen, etwa anhand von Beträgen, Skriptart oder Folgeaktivität. Sie müssen gegen Sammelauszahlungen, mehrere Empfänger und wechselnde Wallet-Verfahren getestet werden. Die ursprünglich angegebene Rechnungsadresse ist nicht ausnahmslos der finale Output: BIP 78 erlaubt unter bestimmten Bedingungen Output-Substitution. Der beweisfähige Anker ist die dokumentierte endgültige Zuordnung, nicht ungeprüft das zuerst genannte Empfangsziel. Kleinstbeträge oder unaufgeforderte Eingänge beweisen ebenso wenig, dass der Empfänger eine Beziehung wollte oder die Eingangsquelle mit ihm identisch ist.

Fehler verbreiten sich besonders bei transitiver Clusterbildung. Das eigene Modell C3 beginnt mit zwei getrennten Gruppen A–B und C–D. Eine falsche Kante B–C verbindet alle vier. Wird A verlässlich mit X verbunden, können danach C und D fälschlich X zugerechnet werden, obwohl die ursprüngliche falsche Entscheidung nur eine einzige Kante betraf. Löscht man später bloß das Personenlabel bei C, bleibt die fehlerhafte Verbindung im Graphen bestehen. Das Modell entfernt daher die Kante und berechnet die Gruppen erneut. Dies ist ein reproduzierbarer Korrekturmechanismus, keine gemessene Fehlerhäufigkeit.

Die empirische Relevanz solcher Erweiterungsfehler behandeln [Möser und Narayanan, Financial Cryptography 2022](https://arxiv.org/pdf/2107.05749). Kleine lokale Fehler können größere Cluster verunreinigen; konservative Schwellen lösen das Problem nicht ausnahmslos. Ein Gutachten muss deshalb nicht nur die Güte einzelner Kanten prüfen, sondern auch den Effekt ihrer Zusammensetzung. Mehrjährige Daten können zusätzliche richtige Kanten liefern; sie können ebenso eine frühere falsche Annahme über weitere Jahre fortschreiben.

Daneben existiert ein wesentlich stärkerer, **nicht heuristischer** Wallet-Anker. [BIP 32, Extended keys und CKDpub](https://bips.dev/32/), erlaubt aus einem erweiterten öffentlichen Schlüssel, dem xpub, die deterministische Ableitung nicht gehärteter Nachfolger. Mit korrekter Skriptpolicy und Pfaden können dadurch viele neu erzeugte Empfangsziele erkannt werden, obwohl einzelne Adressen nicht wiederverwendet wurden. Andere gehärtete Konten und unabhängige Wallets sind davon nicht automatisch umfasst. Ein xpub allein erlaubt keine Ausgabe; sein Beobachtungspotenzial ist trotzdem größer als das einer einzelnen Adresse.

Die [Bitcoin-Core-Deskriptor-Dokumentation, Key expressions und Multipath descriptors](https://github.com/bitcoin/bitcoin/blob/4b612c6bf8cfa319a9df130d4b3d0523fddb6579/doc/descriptors.md), beschreibt Skriptmengen samt Ableitungspolitik. Ein öffentlicher Deskriptor kann Empfangs-/Wechselgeldzweige oder Multisignatur-Skripte erschließen. Ein Scan bleibt durch Pfade, enthaltene Schlüssel und geprüfte Indexbereiche begrenzt. Ein privater Deskriptor kann hingegen Geheimnisse enthalten. Diese beiden Datenklassen dürfen weder beim Leak-Inventar noch beim Gutachten zusammenfallen. Ein Prüfsummen- oder Key-Fingerprint-Feld ist kein Identitätsnachweis.

Taproot verändert wiederum die **sichtbare Ausgabebedingung**, nicht die Öffentlichkeit sämtlicher Beträge. [BIP 341, Design und Script validation rules](https://bips.dev/341/), erlaubt einen Key-Path-Spend ohne Offenlegung aller optionalen Skripte beziehungsweise einen Script-Path-Spend mit Offenlegung des verwendeten Zweigs. Ein einzelner sichtbarer Signaturvorgang kann auch kooperative Bedingungen verbergen. Daraus folgt weder ein einziger menschlicher Signierer noch Alleineigentum. Unverwendete Bedingungen werden nicht vollständig sichtbar; Beträge und Ausgabeverweise bleiben dennoch Beobachtungsobjekte.

Auch eine „Taint“-Analyse benötigt eine offengelegte Modellentscheidung. Der historische Beitrag [Möser, Böhme und Breuker, Financial Cryptography 2014, Abschnitt 3.1](https://maltemoeser.de/paper/risk-scoring.pdf), unterscheidet unter anderem Poison und Haircut. Der Konsensdatensatz gibt keinen eindeutigen Anteil jedes Input-Werts an jedem Output vor. Poison markiert Erreichbarkeit aus einer gekennzeichneten Quelle; Haircut verteilt einen anteiligen Betrag. Das sind unterschiedliche Endpunkte, keine zwei konkurrierenden Messungen eines vorhandenen Eigentumsfelds.

Modell C2 kombiniert 0,5 gekennzeichnete mit 0,5 anderen BTC zu Outputs von 0,6 und 0,3999 BTC bei 0,0001 BTC Gebühr. Poison kennzeichnet beide Outputs, also 0,9999 BTC Nennwert. Haircut ordnet ihnen 0,3 und 0,19995 BTC sowie der Gebühr 0,00005 BTC gekennzeichneten Anteil zu. Der größere gekennzeichnete Nennwert unter Poison ist nicht der Nachweis, dass zusätzliche gekennzeichnete Coins entstanden sind: Ein Boolesches Erreichbarkeitslabel wurde mit einer Betragszuordnung verglichen. Ebenso wenig beweist irgendeine dieser Regeln Straftat, Wissen, Eigentum oder vollständiges Vermögen eines Empfängers.

**Technische Folgerung:** Adresswechsel kann öffentliche Zuordnung erschweren; ein geleakter xpub/Deskriptor kann diese Schranke für den enthaltenen Zweig ohne statistisches Clustering überwinden. Bei reiner Heuristik müssen dagegen Kantenunsicherheit, transitive Reichweite und Widerrufbarkeit geprüft werden. Anbieterakten dürfen deshalb nicht pauschal als „nur öffentliche Adressen“ eingestuft werden: Ihre genaue Schlüssel-/Pfad- und Kundenzuordnung entscheidet über den möglichen Zusatzgewinn. Dass Anbieter solche erweiterten Schlüssel tatsächlich sammeln oder melden, ist hier nicht festgestellt.

### 6.5 Ethereum: Auftrag, Ausführung und Zustand sind getrennte Datenebenen

Eine Ethereum-Adresse bezeichnet einen persistenten Kontokontext im jeweiligen Netz. Der native ETH-Bestand, Nonce, Code und Speicher gehören zum Zustandsmodell; eine Adresse kann zudem in beliebig vielen Tokenverträgen als Inhaber einer Position erscheinen. Der Informationsgewinn aus einem verlässlichen Identitätsanker kann deshalb unmittelbar eine Historie und einen Stichtagsbestand derselben Adresse betreffen, ohne Bitcoin-Wechselgeldheuristik. „Unmittelbar“ heißt hier korrekt zugängliche und interpretierte Chain-Daten, nicht vollständiges persönliches Vermögen.

Die [Ethereum-JSON-RPC-Dokumentation, Transaktions-, Receipt- und Zustandsmethoden](https://ethereum.org/developers/docs/apis/json-rpc/), trennt mehrere Objekte. Eine äußere Transaktion enthält je nach Typ unter anderem Ziel, nativen Wert, Nonce, Eingabebytes und Gebührenparameter; die Absenderadresse wird im RPC-Objekt aus der Signatur erschlossen. Ein Receipt ergänzt Ausführungsstatus, tatsächlichen Gasverbrauch und Logs. Der Zustand an einem Block beantwortet dagegen, welche Positionen nach dessen Vorgängen bestehen. Alle drei Objekte betreffen denselben Ablauf, aber unterschiedliche Fragen.

Ein `value` von 1 ETH ist nicht automatisch ein dauerhaft ausgeführter Transfer. `to` kann einen Vertrag oder Router bezeichnen, nicht den wirtschaftlichen Endempfänger. Eingabebytes, auch Calldata genannt, können einen Funktionsselektor und Argumente enthalten. Ein vier Byte langer Selektor ist keine eindeutige Beschreibung wirtschaftlicher Bedeutung: Namen können kollidieren und tatsächlicher Code kann anders handeln. Die [Transaktionsdokumentation, Data field](https://ethereum.org/developers/docs/transactions/), beschreibt diesen Aufrufmechanismus; für die Interpretation sind zutreffende Schnittstelle und damaliger Code erforderlich.

[EIP-140, REVERT, und EIP-658, Receipt status](https://eips.ethereum.org/EIPS/eip-140), unterscheiden rückgängig gemachte Ausführungswirkungen von der dokumentierten [Erfolgs-/Fehlerkennzeichnung des äußeren Aufrufs](https://eips.ethereum.org/EIPS/eip-658). Ein fehlgeschlagener Unteraufruf kann von seinem Elternaufruf behandelt werden; ein erfolgreicher äußerer Vorgang bedeutet daher nicht, dass jeder versuchte Unteraufruf erfolgreich war. Ein Trace kann auch versuchte, später verworfene Wirkungen zeigen. Erst die Prüfung der Fehlergrenze bestimmt, was bestehen bleibt.

Modell C6 nimmt eine gewöhnliche gültig aufgenommene Transaktion ohne Delegationsautorisierung mit fehlgeschlagener oberster Ausführung, 2 ETH Anfangsbestand, versuchter Zahlung von 1 ETH und hypothetischen 30.000 Gas zu 100 Gwei effektivem Preis an. Die Ausführungsgebühr beträgt 0,003 ETH. Der Zahlungsempfänger erhält aus diesem Versuch 0; beim Sender verbleiben ohne andere Effekte 1,997 ETH. Eine Rechnung, die den angeforderten einen ETH zusätzlich abzieht, wäre falsch. Das Programm berechnet ausschließlich diese gesetzten Werte; es führt keine EVM aus und validiert keine Transaktionsbytes. Blob- oder zusätzliche L2-Gebühren sind ausgeschlossen.

Eine verbreitete weitere Vereinfachung ist inzwischen ebenfalls falsch: „Bei einem Fehlschlag ändern sich außer Gebühren und Absender-Nonce keinerlei Daten.“ [EIP-7702, Behavior](https://eips.ethereum.org/EIPS/eip-7702), verarbeitet auf entsprechend aktivierten Chains Autorisierungstupel vor der eigentlichen Ausführung. Bereits verarbeitete Delegationsindikatoren bleiben ausdrücklich auch bei späterem Revert bestehen. Modell C6 stellt daneben eine zweite, ausdrücklich nur symbolische Code-/Nonce-/Statusprojektion mit gesetzter Delegation und geändertem Nonce einer gesonderten autorisierenden Adresse. Beide Beispiele haben Receipt-Status 0; die vorgelagerte Autorisierungswirkung unterscheidet sich. Für diese zweite Projektion werden weder derselbe Gaswert noch dieselbe Gebühren-/Saldo-Rechnung angenommen: Autorisierung hat eigene zusätzliche Gaskosten. Normale verworfene Call-Wirkungen werden dadurch nicht erhalten.

EOAs können nach diesem Verfahren persistent delegierten Code besitzen und trotzdem äußere Transaktionen initiieren. Ein nichtleeres Code-Feld beweist deshalb nicht mehr ausnahmslos ein klassisches Contract-Konto. Ebenso können Gebührenzahler und autorisierende Adresse auseinanderfallen. Historische Klassifikatoren, die Code, Nonce oder Gaspreis wie zeitlose Personenmerkmale behandeln, benötigen eine neue Validierung. Die Anwendung hängt vom tatsächlich aktivierten Fork der untersuchten Chain ab; der Status einer Spezifikation allein belegt ihn nicht.

Die [Geth-Tracer-Dokumentation, callTracer und prestateTracer](https://geth.ethereum.org/docs/developers/evm-tracing/built-in-tracers), beschreibt rekonstruierte Aufrufbäume und Zustandsdifferenzen. Explorer-„Internal Transactions“ sind daraus abgeleitete Ausführungsschritte, keine eigenständig signierten äußeren Transaktionen. `DELEGATECALL` bezeichnet die Adresse ausgeführten Codes; diese ist nicht automatisch Empfänger des im Proxy gehaltenen Vermögens. Tracereinstellungen können Unteraufrufe auslassen. Ein Zustandsdiff ist nach der Dokumentation kein kryptografischer Zustandsbeweis. Der verwendete Client, die Konfiguration und notwendige historische Daten gehören deshalb in die Beweisprovenienz.

**Technische Folgerung:** Ein Adressanker erlaubt auf einer transparenten Account-Chain einen breiten beobachtbaren Ausschnitt. Dieser ist als Historie bestätigter Wirkungen und Stichtagspositionen auszuwerten, nicht als Summe eingereichter Absichten oder aller Trace-Werte. Aktuelle Kontenmechanik verändert außerdem, welche Person aus einem Absender-, Gebühren- oder Code-Merkmal überhaupt vermutet werden darf.

### 6.6 Token, Verträge, L2 und wirtschaftliche Positionen

Ein nativer ETH-Saldo ist nicht die Summe aller Assets einer Adresse. Tokenpositionen liegen im Zustand der jeweiligen Verträge. [ERC-20, balanceOf und decimals](https://eips.ethereum.org/EIPS/eip-20), liefert einen ganzzahligen Vertragsbestand; Name, Symbol und Nachkommastellen sind optional. Ein Rohwert von 1.000.000 entspricht bei sechs Nachkommastellen einer Einheit, bei achtzehn nur 0,000000000001 Einheiten. Eine pauschale Anzeige mit achtzehn Stellen wäre kein harmloser Formatfehler, sondern eine andere Menge. Fehlen zuverlässige Einheitendaten, muss dies offenbleiben.

Ein Token wird mindestens durch Chain und Vertragsadresse, nicht durch sein Symbol identifiziert. Gleichlautende Symbole in mehreren Verträgen sind keine Beweise identischer Assets. `Approval` ist eine Berechtigung, nicht schon ein ausgeführter Transfer. Ein `Transfer`-Log ist ein emittierter Vertragsdatensatz; Nulltransfers sind ebenfalls vorgesehen. Aus dem bloßen Auftauchen eines Ereignisses folgt keine gewollte Beziehung des genannten Empfängers, kein wirtschaftlicher Wert und keine Zustimmung zu einer Zahlung. Der tatsächliche Emitter ist von den in seinen Parametern behaupteten Adressen zu unterscheiden.

Ein vereinfachtes gedankliches Gegenbeispiel illustriert die Grenze: Vertrag A gibt ein vertraut benanntes Transfer-Ereignis für X aus, während sein maßgeblicher Zustandsbestand für X unverändert bleibt. Der Log existiert dann tatsächlich; die externe Behauptung „X hat werthaltige Token erhalten“ ist dadurch nicht wahr. Dies ist kein ausgeführter Angriff und keine gemessene Spamquote, sondern eine Interpretationstrennung. Für einen Bestandsbefund sind Vertragsidentität, tatsächlich gültige Semantik und Stichtagszustand entscheidend. Die [Solidity-ABI-Spezifikation, Events](https://docs.soliditylang.org/en/latest/abi-spec.html), definiert das Kodieren von Ereignissen, keine Garantie für den wirtschaftlichen Wahrheitsgehalt beliebiger Ereignisparameter.

Auch eine vollständige Logliste ersetzt nicht universell den historischen Zustand. ERC-20 empfiehlt ein Mint-Ereignis aus der Nulladresse, schreibt aber kein universelles Burn-Ereignis vor. Andere oder nicht vollständig standardkonforme Vertragsregeln können Bestände zusätzlich verändern. Ein Ermittlungsmodell muss deshalb genau festlegen, wann es Ereignisse als vollständige Bewegungsbuchführung verwenden darf und wann es den Zustand separat prüft. Ein erfolgreicher äußerer Receipt-Status ersetzt zudem nicht automatisch die Prüfung einer Token-Rückgabe und ihrer tatsächlichen Wirkung.

Langfristige Profile benötigen **historische Vertragssemantik**. [ERC-1967, Proxy Storage Slots](https://eips.ethereum.org/EIPS/eip-1967), beschreibt persistenten Proxy-Speicher und wechselnde Implementierung. Die heutigen Schnittstellen-/Quellcodeinformationen können deshalb für einen früheren Vorgang falsch sein. Maßgeblich sind damalige Implementierung, gegebenenfalls Beacon-Ergebnis und ausgeführter Code. Änderungsereignisse sind empfohlen, nicht zwingend. Ein fehlendes Upgrade-Log beweist daher keine unveränderte Implementierung; fehlende Standard-Slots schließen nicht jede andere Proxy-Form aus.

Smart Accounts können mehrere oder begrenzte Berechtigungen haben. [ERC-1271, Specification und Rationale](https://eips.ethereum.org/EIPS/eip-1271), lässt zustands-, zeit- und berechtigungsabhängige Signaturprüfung zu. Eine erfolgreiche Challenge belegt zunächst die Akzeptanz der konkreten Daten unter den geprüften Regeln. Sie beweist weder die alleinige Verfügungsgewalt eines einzelnen Signierers noch wirtschaftliches Alleineigentum an allen Positionen. Bei Multisignatur kann ein Mitunterzeichner allein unzureichend sein; bei begrenzten Berechtigungen kann eine bestimmte Aktion erlaubt, eine andere ausgeschlossen sein. Zeitpunkt, Challenge-Zweck und damalige Konfiguration müssen feststehen.

Bei Bridges kommt ein weiteres Bilanzproblem hinzu. Die [OP-Standardbridge-Dokumentation, Design und Bridged tokens](https://docs.optimism.io/app-developers/guides/bridging/standard-bridge), beschreibt das Sperren ursprünglicher Token und das Prägen ihrer Repräsentationen beziehungsweise den umgekehrten Vorgang. Modell C4 setzt eine vollständig gedeckte, einlösbare 1:1-Position: 1 ursprüngliche Einheit ist gesperrt, 1 Repräsentation wird gehalten. Werden beide als unabhängiges Nutzervermögen addiert, entstehen rechnerisch 2 statt 1 wirtschaftlicher Position. Diese Annahmen werden nicht als Nachweis tatsächlicher Bridge-Reserven, Kursgleichheit oder Einlösesicherheit verwendet.

Aus dem gesamten Escrow-Vertragsbestand folgt nicht automatisch die Position eines einzelnen Nutzers. Ein Vertrag kann Vermögen vieler Berechtigter halten; die passende Nutzerposition ist ein geprüfter Anspruch, nicht ungeprüft seine gesamte Chain-Balance. Ein einziger Berechtigter ist möglich, wie im isolierten Modell C4 ausdrücklich angenommen. Dasselbe Zuordnungsprinzip gilt für fremdverwahrte Sammelbestände. Eine Personenbilanz braucht eine Verbindung zwischen beobachtetem Asset, zugrunde liegender Deckung, Anspruch und möglichen Verbindlichkeiten. Bruttobestand, verfügbare Position und Nettovermögen sind unterschiedliche Zielgrößen.

Ein konkretes Beispiel sind tokenisierte Vault-Anteile. [ERC-4626, convertToAssets, previewRedeem und maxRedeem](https://eips.ethereum.org/EIPS/eip-4626), trennt Anteilbestand, idealisierte Umrechnung ohne Gebühren/Slippage, gebührenberücksichtigende Vorschau und Einlösungslimits. Positive Anteile und positive Umrechnung können deshalb gleichzeitig mit derzeit deaktivierter Einlösung bestehen. Ein Null-Limit allein beweist umgekehrt keine wirtschaftliche Wertlosigkeit; konservative Unterschätzung ist erlaubt. Für eine Bilanz sind underlying Token, Einheiten, damalige Regeln, Berechtigung, Limits und Bewertung zu prüfen. Die Schnittstellenkonformität bescheinigt keine Solvenz.

Ein L2-System hat zusätzlich einen eigenen Ausführungszustand. Seine Einzahlungen, veröffentlichten Batches und Abrechnungsanker auf L1 sind nicht dasselbe wie alle individuellen L2-Salden. Die [OP-Derivation-Spezifikation, Engine Queue und About reorgs Post-Merge](https://specs.optimism.io/protocol/derivation.html), unterscheidet sequencer-bezogene `unsafe`-Blöcke sowie `safe`/`finalized` aus entsprechenden L1-Eingaben. Diese Eingabefinalität wird ausdrücklich von der Finalisierung optimistischer Withdrawal-/Output-Ansprüche getrennt. Eine Analyse muss angeben, welchen Status sie meint und welche konkreten Daten für die Rekonstruktion vorliegen.

Auch der Begriff „Zero Knowledge“ ist kein ausreichender Datenschutzbefund. Die [Ethereum-Dokumentation zu ZK-Rollups, Transactions und Data availability](https://ethereum.org/developers/docs/scaling/zk-rollups/), beschreibt veröffentlichte Transaktions- oder Zustandsdifferenzdaten als öffentlich. Ein Validity Proof prüft eine behauptete Zustandsänderung; eine zusätzliche Privacy-Gestaltung muss gesondert untersucht werden. Komprimierte Daten können Zustandsrekonstruktion erlauben, ohne jeden ursprünglichen Zwischenaufruf wiederzugeben. Der konkrete veröffentlichte Inhalt bestimmt die mögliche Profilbildung.

Die [Dokumentation zur Datenverfügbarkeit](https://ethereum.org/developers/docs/data-availability/) trennt außerdem rechtzeitige Verfügbarkeit von unbegrenztem historischen Abruf. Die ungefähr achtzehn Tage Mindestvorhaltung von Blobs nach [EIP-4844, Security Considerations](https://eips.ethereum.org/EIPS/eip-4844), sind keine universelle Löschfrist aller Beobachter und Archive. Ein fortbestehender L1-Root oder Proof ersetzt keine fehlenden historischen L2-Eingaben. Mehrjährige Auswertung benötigt daher ein tatsächliches Archiv der erforderlichen Daten; kurze Protokollvorhaltung ist weder Anonymitätsbeweis noch der Nachweis endgültigen Datenverlusts.

**Technische Folgerung:** Ein Adresssaldo ist bei Token, Smart Accounts, Bridges und L2 nur ein Teil der Beobachtung. Die öffentlich nachvollziehbare Technik erlaubt zusätzliche Erkenntnisse über konkrete Positionen; für ihr wirtschaftliches Zusammenzählen benötigt sie ein Vertrags-/Anspruchsmodell. Gleiche Zeichenfolge, erfolgreicher Aufruf oder großer Vertragsbestand ist jeweils eine schwächere Tatsache als „dieses Nettovermögen gehört dieser Person“.

### 6.7 Lightning und Privacy-Protokolle: andere Daten, andere Schlüsselrollen

Lightning verlagert wesentliche Zahlungen in Kanalzustände außerhalb einer öffentlichen Einzelzahlungs-Chronik. [BOLT 7, Channel-/Node-Announcements](https://raw.githubusercontent.com/lightning/bolts/master/07-routing-gossip.md), verbindet bei angekündigten Kanälen Node-Schlüssel mit einem Funding-Output und kann Netzwerkadressen enthalten. Die öffentliche Kapazität ist aber weder der aktuelle verfügbare Kanalbestand eines Teilnehmers noch sein persönliches Gesamtvermögen. Ein unangekündigter Kanal vermeidet die entsprechende öffentliche Gossip-Beziehung, nicht die Existenz der Funding-Transaktion. Ohne Zusatzinformationen ist ihre Einordnung als konkreter Kanal nicht automatisch eindeutig.

Kanalpartner und Routing-Knoten wissen mehr als ein passiver Chain-Leser, aber nicht notwendig alles. [BOLT 2, HTLC-Nachrichten](https://raw.githubusercontent.com/lightning/bolts/1aadb719b4007c4cea0ba6e36b08c4fb53788dee/02-peer-protocol.md), beschreibt lokale Beträge, Ablaufbedingungen und Payment-Hashes. Die [Onion-Spezifikation, BOLT 4](https://raw.githubusercontent.com/lightning/bolts/1aadb719b4007c4cea0ba6e36b08c4fb53788dee/04-onion-routing.md), begrenzt das Wissen gewöhnlicher Zwischenknoten über den vollständigen Pfad, garantiert aber nicht das Ausbleiben von Traffic-Analyse. Gemeinsame Hashes, Zeitbeobachtungen oder Anbieterakten können zusätzliche Korrelation erlauben; sie beweisen nicht automatisch beide Personenendpunkte oder den Zahlungszweck.

Eine custodiale Lightning-Wallet kann ihre eigenen Kundenbuchungen kennen, selbst wenn die öffentliche Chain keine entsprechende Einzeltransaktion enthält. Aus einem CASP-Kundendatensatz kann deshalb mehr folgen als aus einem Funding-Anker. Umgekehrt darf die gesamte Kanalhistorie nicht aus dem bloßen öffentlichen Öffnungsbeleg als bereits beobachtet dargestellt werden. Das sind Grenzen des Datenzugangs, nicht der Satz, Lightning sei gegen jede mögliche Beobachtung sicher.

Bei Monero begrenzen unterschiedliche Mechanismen unterschiedliche Informationen. Die [offiziellen Erläuterungen zu Ring-Signaturen, RingCT und Stealth-Adressen](https://www.getmonero.org/get-started/faq/), beschreiben die Verdeckung des tatsächlich ausgegebenen Inputs unter Kandidaten, vertrauliche Beträge und einmalige Empfängeroutputs. Öffentliche Prüfmaterialien existieren weiterhin. Die untersuchten Erläuterungen sind Mechanikquellen, keine vollständige aktuelle Sicherheitsanalyse oder Erfolgsquote einer Deanonymisierung. Historische Befunde über frühere Decoy-/Signaturversionen werden nicht auf alle heutigen Vorgänge übertragen.

Ein geleakter **Private View Key** schafft einen anderen Beobachter. Nach dem [Monero-View-only-Leitfaden, Einleitung](https://www.getmonero.org/resources/user-guides/view_only.html), können zusammen mit der zugehörigen Hauptadresse eingehende Vorgänge erkannt werden; ohne ergänzende Key Images werden ausgegebene Outputs und der korrekte Restbestand jedoch nicht zuverlässig erkannt. Eingänge zu summieren wäre auch hier keine aktuelle Bilanz. Ein Sichtschlüssel ist kein Ausgabeschlüssel. Identität, entschlüsselte Walletdaten, Key Images und Spend-Autorisierung müssen deshalb im Leak-Inventar getrennt bleiben.

Zcash ist komponentenweise zu betrachten. Transparente Inputs/Outputs sind nicht dasselbe wie Sapling-/Orchard-Noten. Die [abgerufene Protokollspezifikation, §§ 3.1–3.2.3, 4.15–4.16, 4.20 und 5.6.3–5.6.4](https://zips.z.cash/protocol/protocol.pdf), beschreibt verschlüsselte Noteninhalte, Commitments und öffentliche Nullifier gegen Doppelausgaben. Öffentliche Verifikation verlangt dabei nicht die Offenlegung jedes Empfängers und Betrags. Ein Nullifier ist deshalb nicht automatisch eine öffentliche Zuordnung zu einer zuvor unbekannten Note. Gemischte Vorgänge können zugleich transparente und verdeckte Bestandteile enthalten.

Incoming und Full Viewing Keys haben wiederum verschiedene Reichweiten; enthaltene Full-Viewing-Komponenten können zusätzliche Ausgabenbezüge erschließen, ohne automatisch Spend-Autorisierung zu liefern. [ZIP 316, Viewing Keys und Revisions](https://zips.z.cash/zip-0316), unterscheidet kombinierte Adressen und Sichtschlüssel nach ihren enthaltenen Komponenten. Eine Unified Address bedeutet nicht ausnahmslos shielded Nutzung. Die abgerufene Protokollversion `v2026.7.0-234-geaccf9 [NU6.2]` belegt einen Dokumentstand, nicht allein Mainnet-Aktivierung; ZIP-Revision 0 ist aktiv, Revision 1 zurückgezogen und Revision 2 Entwurf. Der betrachtete Vorgang muss zum tatsächlich verwendeten Stand passen.

**Technische Folgerung:** „Alle Kryptowährungen sind vollständig öffentlich“ und „Privacy-Technik verhindert jede Personenverknüpfung“ wären gleichermaßen falsch. Für den Gutachtengegenstand ist entscheidend, welche transparenten Komponenten, privaten Sichtdaten und Anbieteranker konkret zusammenkommen. Ein Leck kann deren Erkenntnisreichweite erweitern, ohne das kryptografische Verfahren zu brechen. Dass österreichische Anbieter routinemäßig xpubs oder private Sichtschlüssel halten, wird hier nicht behauptet; diese Kategorien sind feldgenau zu prüfen.

### 6.8 Was verschiedene Beobachter tatsächlich wissen

„Öffentlich“ bezeichnet den Zugang zu bestimmten Protokolldaten, nicht einen überall identischen Beobachtungsstand. Ein passiver Leser bestätigter Blöcke, ein eigener validierender Node, ein Explorer mit Zusatzindex, ein Wallet-/RPC-Dienst und ein identifizierender Anbieter besitzen unterschiedliche Informationen. Diese Unterschiede gehören in jede Aussage zur Verknüpfbarkeit. Eine Chain-Abfrage liefert beispielsweise nicht schon die IP-Adresse, von der die ursprüngliche Transaktion abgesendet wurde.

| Beobachter | Zusätzliche Information | Wesentliche Grenze |
|---|---|---|
| Ledger-Leser | Bestätigte Protokolldaten im betrachteten Netz | Keine Kundenidentität oder ursprüngliche IP allein aus den Blöcken |
| Eigener Node | Validierung und eigener Mempool-/Peer-Beobachtungsstand | Weiterleitender Peer ist nicht notwendig Ersteller; Sicht ist nicht global |
| Explorer/Indexer | Suchindizes, interpretierte Vorgänge, Labels und berechnete Graphen | Zusatzlabel und Parserentscheidung sind keine Konsensfelder |
| Wallet-/RPC-Dienst | Je nach Dienst abgefragte Adressen, Sitzung, IP, Zeitpunkt oder Konto | Nicht jeder Dienst protokolliert alles; ein fremdes Wallet ist nicht automatisch bekannt |
| Identifizierender Anbieter | Kundenakte und konkret dokumentierte Ein-/Auszahlungen | Interne Sammelverwaltung und Kundenforderungen bleiben vom Ledger zu unterscheiden |

Eine öffentliche Exploreranzeige kann somit mindestens drei Schichten vermischen: unmittelbar bestätigte Daten, daraus reproduzierbar berechnete Daten und externe Interpretation. „Transaktion in Block H“ ist anders zu prüfen als „Change“, „Börse X“ oder „Person Y“. Ein zweiter Explorer ist kein unabhängiger Identitätsbeleg, wenn beide dasselbe kommerzielle Label übernommen haben. Die Herkunft der Zusatzdaten muss bis zur ursprünglichen Beobachtung zurückverfolgbar sein.

Adressabfragen schaffen ihrerseits Metadaten: Ein Dienst kann erfahren, dass ein bestimmter Anschluss oder Benutzer gerade eine bestimmte Adresse betrachtet. Das beweist weder, dass ihm die Adresse gehört, noch dass die Abfrage geheim blieb. Der [USENIX-Befund von Torres, Willi und Shinde, 2023, Abschnitte 4–5](https://www.usenix.org/system/files/usenixsecurity23-torres.pdf), dokumentiert tatsächliche Wallet-Adressweitergaben im damaligen DApp-/Wallet-Sample. Diese anwendungsseitigen Anker sind unabhängig von Steueraggregaten entstanden. Ihre Existenz macht zusätzliche Verknüpfung realistisch, aber nicht jeden aktuellen Wallet-Nutzer identifiziert.

Auch verschlüsselter Transport ist keine vollständige Anonymisierung. [BIP 324, Motivation und Security/Design Goals](https://bips.dev/324/), trennt passive Entschlüsselbarkeit von aktiven Peers und Verkehrsanalyse. Ein berechtigter RPC-Endpunkt verarbeitet die Anfrage im Klartext seiner Anwendung, selbst wenn TLS sie auf dem Übertragungsweg schützt. Für die technische Bewertung muss deshalb benannt werden, **wo** die Vertraulichkeit endet und **wer** die Anschlussdaten tatsächlich erhält. Die bloße Verwendung einer öffentlichen Chain liefert keine Aussage über diese Dienstarchitektur.

Versionsgrenzen sind dabei real, nicht nur theoretisch: Die [offizielle Warnung zu Bitcoin Core 31.0 vom Juni 2026](https://bitcoincore.org/en/2026/06/06/privatebroadcast-ip-leak/) dokumentiert eine mögliche IP-Offenlegung durch bestimmte Retry-Verbindungen der optionalen Private-Broadcast-Funktion. [Core 31.1, PrivateBroadcast](https://bitcoincore.org/en/releases/31.1/), dokumentiert die Korrektur. Der Befund betrifft die bezeichnete Konfiguration, keine allgemeine Offenlegung aller Nutzer. Eine Spezifikation oder Datenschutz-Zielbeschreibung darf somit weder den tatsächlichen Implementierungsstand noch eine unabhängige Wirksamkeitsprüfung ersetzen.

Der [CCS-2025-Versuch von Wang et al., Autorenfassung v1, Abschnitte 8–9](https://arxiv.org/pdf/2508.21440), zeigt einen anderen Mechanismus: beobachteten RPC-Netzverkehr zeitlich mit Ledger-Vorgängen verbinden. Kontrollierte Geräte, Sicht auf Netzverkehr und genaue Zeitbezüge gehören zu seinen Versuchsbedingungen. Sein Endpunkt war eine IP-zu-Pseudonym-Verbindung, nicht wirtschaftliches Eigentum. Eine IP kann geteilt, dynamisch oder einem VPN zugeordnet sein. Der Befund darf weder als heutige Bevölkerungsquote noch als Ergebnis mit bloßen Jahresmeldungen verwendet werden.

**Technische Folgerung:** Ein realistisches Expositionsinventar umfasst nicht nur Meldefelder, sondern auch Adressabfragen, Kundenzuordnungstabellen und tatsächlich erhaltene Beobachtungs-/Walletdaten. Zusätzliche Dienstmetadaten können starke Anker liefern; ohne ihren belegten Zugang dürfen sie einem Modell nicht heimlich als Eingabe zugespielt werden.

### 6.9 Datenstand, Zeit und Reproduzierbarkeit

Ein Blockchain-Befund benötigt einen festgelegten Datenstand. Zu erfassen sind mindestens Netz und Chain-Identität, Blockhöhe und Blockhash, Transaktionskennung, gegebenenfalls Output-/Log-Index, Abfragezeit, Client-/Indexer-Version und relevante Beobachtungsparameter. Ein Hash identifiziert Inhalt; er belegt nicht von selbst, dass ein Block beim maßgeblichen Datenstand zur kanonischen Kette gehörte. Die Blockhöhe allein ist bei konkurrierenden Zweigen nicht eindeutig.

Das eigene Gegenmodell C5 enthält zwei alternative Zweige auf Höhe 100: unter dem symbolischen Hash A beträgt die betrachtete Position 1, unter Hash B 0. Das Modell simuliert keinen Angriff und keine Konsensentscheidung. Es zeigt lediglich, dass „Saldo bei Höhe 100“ ohne Zweigidentität keine vollständig spezifizierte Beobachtung ist. Wer Salden aus mehreren Abfragen addiert, muss denselben Zustand verwenden; sonst kann schon die Datengewinnung eine rechnerische Unstimmigkeit erzeugen.

[EIP-1898, Final, Specification und Rationale](https://eips.ethereum.org/EIPS/eip-1898), erlaubt für bestimmte Ethereum-Zustandsabfragen einen Blockhash und optional die Prüfung kanonischer Zugehörigkeit. Dies verhindert bei unterstützten Endpunkten die unbemerkte Mischung verschiedener Zustände. Eine Abfrage unter `latest` ist dagegen zeitabhängig. Eine einmal dokumentierte kanonische Zugehörigkeit ist kein Versprechen für jeden späteren Datenstand. Der Gutachter muss den erforderlichen Bestätigungs-/Finalitätsstand festlegen und bei relevanten Umorganisationen abhängige Ergebnisse neu prüfen.

Mempool-Beobachtungen sind vorläufig und beobachterabhängig. Eine Transaktion kann noch unbestätigt sein; Empfangszeit und Reihenfolge eines Nodes sind keine globale Uhr. Das versionierte [Bitcoin-Core-30.0-RPC gettxout](https://bitcoincore.org/en/doc/30.0.0/rpc/blockchain/gettxout/) berücksichtigt auf Wunsch den lokalen Mempool: Ein dort bereits ausgegebener Output kann dann fehlen, obwohl die bestätigte Kette ihn noch als unspent führt. Ein Null-Ergebnis allein beweist deshalb weder historischen Nullbestand noch eine bestimmte bestätigte Ausgabe. Die dokumentierten [Blockheader-Felder](https://bitcoincore.org/en/doc/30.0.0/rpc/blockchain/getblockheader/) enthalten Hash, Höhe, Bestätigungen und Blockzeit; ihre Bedeutung ist nicht mit einem kundenseitigen Auftragszeitpunkt gleichzusetzen.

„Heute nicht abrufbar“ bedeutet ebenfalls nicht „damals nicht vorhanden“. Historische Zustände, gespeicherte Blöcke und Suchindizes sind verschiedene Bestände. Die [Geth-Dokumentation vom Februar 2026, Archive mode](https://geth.ethereum.org/docs/fundamentals/archive), unterscheidet historischen Zustandszugriff von historischen Merkle-Beweisen. Versionsstand, aufbewahrte Trie-Daten und abgeschlossene Indexierung beeinflussen die Fähigkeit. Ein Archivname allein garantiert daher weder jede alte Antwort noch den zugehörigen kryptografischen Beweis.

Ein Einschlussbeweis kann unter einem festgelegten und vertrauenswürdig validierten Blockroot den Bezug bestimmter Daten zu diesem Zustand absichern. Er bestätigt nicht die externe Aussage „dieser Schlüssel gehört dieser Person“. Auch eine unveränderte Rohdatei kann ein falsches Dienstlabel enthalten. Integrität, Vollständigkeit, kanonische Zugehörigkeit und korrekte Interpretation sind vier gesonderte Prüfungen. Für eine wiederholbare Auswertung sind Rohantworten, Parameter und abgeleitete Kanten getrennt vorzuhalten, statt nur den fertigen Screenshot eines Explorers.

**Technische Folgerung:** Aussagekräftige Langzeitprofile brauchen historische Stichtage und nachvollziehbare Ableitungen. Wiederholte Abfragen können neue Informationen erschließen; sie können ebenso alte Befunde ändern. Eine Person–Adress-Verbindung muss deshalb zeitlich und sachlich begrenzt sein. Die Dauerhaftigkeit des öffentlichen Ausgangsmaterials beseitigt weder Versionsunterschiede noch Zuordnungsfehler.

### 6.10 Die Beweiskette darf keine Stufe überspringen

| Stufe | Mögliche Feststellung | Noch nicht damit festgestellt |
|---|---|---|
| Öffentlicher Vorgang | Transaktion, Output, Adresse oder Vertragsereignis | Zugehörigkeit aller beteiligten Adressen zu einer Person |
| Cluster oder Dienst | Mutmaßliche Adressgruppe oder verifiziertes Dienstlabel | Identität eines einzelnen Kunden dieses Dienstes |
| Personenverbindung | Nachvollziehbare Verbindung einer Person zum Vorgang | Aktuelle Schlüsselkontrolle und wirtschaftliches Eigentum |
| Bestand und Berechtigung | Bestimmte Position zum Stichtag unter geprüfter Zuordnung | Gesamtes aktuelles Nettovermögen einschließlich anderer Positionen und Schulden |

Eine Empfängeradresse einer Zahlung ist nicht allein deshalb eine eigene Adresse des Zahlenden. Die Salden eines Verwahrdienstes gehören nicht automatisch einem einzelnen Kunden. Ein überprüfter Kontrollnachweis hat einen Zeitpunkt und einen Umfang; er beweist nicht, dass später keine Schlüsselübergabe oder Änderung der Berechtigung erfolgt. Multisignatur, Gemeinschaftsvermögen und treuhändige Verwahrung verlangen weitere Tatsachen.

Ein technischer Zusatznachweis kann bei Bitcoin eine dokumentierte Nachrichten-Challenge sein. [BIP 322, Version 2.0.0, Full/Proof of Funds und Verification](https://bips.dev/322/), validiert nachrichtenbezogene Skriptbedingungen mittels virtueller, nicht im echten Netz ausgebbarer Transaktionen. Die Proof-of-Funds-Variante betrifft eine vom Signierenden ausgewählte Output-Menge; Existenz und Unspent-Status benötigen gesonderte Chain-Prüfung. Sie beweist weder Vollständigkeit noch frühere Transaktionsurheberschaft. Signieren im Auftrag anderer, eingeschränkte Skriptunterstützung und sofortige Zustands-/Schlüsseländerungen begrenzen den Nachweis. Bei geprüften, tatsächlich signaturpflichtigen Skriptbedingungen kann eine frische, zweckgebundene Challenge samt dokumentierter Version, Skriptmenge und Stichtag einen stärkeren Anker als ein bloßes Adresslabel liefern. Eine allgemein erfüllbare Skriptlösung wäre dagegen kein zusätzlicher Schlüsselautorisierungsbeleg. Wirtschaftliche Berechtigung wird durch beides nicht ersetzt.

Verbindungen sind deshalb als nachweisbare Kanten mit Quelle, Zeitpunkt und Unsicherheit zu führen. Eine heuristisch erzeugte Kante darf nicht als Primärnachweis in eine nächste Auswertung eingehen. Andernfalls kann eine schwache Anfangsannahme durch wiederholte Verwendung wie eine mehrfach bestätigte Tatsache aussehen.

### 6.11 Was der öffentliche Benchmark tatsächlich misst

[Ghost Clusters, USENIX Security 2025, Abb. 1 auf gedruckter S. 1363; Datengrundlage S. 1360–1361, Grenzen S. 1370](https://www.usenix.org/system/files/usenixsecurity25-lubbertsen.pdf), vergleicht kommerzielle Dienstadresslabels mit beschlagnahmten Beständen dreier Dienste. Die folgenden Falschzuordnungsanteile sind eigene Berechnungen aus den publizierten Zählwerten.

| Dienst | Richtige / bekannte Dienstadressen | Falsche / insgesamt zugeordnete Adressen |
|---|---|---|
| BestMixer | 44.821 / 182.612 = 24,54% Abdeckung | 19 / 44.840 = 0,0424% |
| Hansa | 913.171 / 1.157.519 = 78,89% Abdeckung | 1.695 / 914.866 = 0,1853% |
| Wall Street Market | 525.236 / 553.777 = 94,85% Abdeckung | 611 / 525.847 = 0,1162% |

Die Abdeckung ist TP/(TP+FN): der Anteil gefundener bekannter Dienstadressen. Der Falschzuordnungsanteil ist FP/(TP+FP): der falsche Anteil unter vergebenen Labels. Der vollständige Umfang tatsächlich nicht zum Dienst gehörender Vergleichsadressen fehlt; damit ist der Nenner FP+TN für eine allgemeine Falschpositivrate nicht bekannt. Hohe Präzision kann mit geringer Abdeckung zusammenfallen. Die Werte gelten für drei Dienste und den untersuchten kommerziellen Datenstand; nur BestMixers Fehlzuordnungen wurden einzeln untersucht. Diese Dienstbefunde validieren weder die Identität gewöhnlicher Personen noch deren wirtschaftliches Eigentum oder Gesamtvermögen.

Für einen Personenbestand muss deshalb ein anderer wahrer Vergleichswert erhoben werden. Erforderlich sind auch Fälle, in denen kein Treffer erreicht wird, und Fälle ohne echte Verbindung. Eine nur an erfolgreichen einfachen Zuordnungen geprüfte Genauigkeit verschweigt die Ausfälle im Ausgangsbestand.

### 6.12 Das Basisratenproblem in einer großen Kandidatenmenge

Das sechste eigene Modell nimmt ausdrücklich hypothetische Parameter an: 100.000 Kandidaten, davon 100 echte Verbindungen; 99% Trefferquote unter den echten Verbindungen und 0,1% Falschpositivrate unter den 99.900 Nichtverbindungen. Daraus folgen 99 erwartete richtige und 99,9 erwartete falsche Treffer. Das Verhältnis der erwarteten richtigen zu allen erwarteten Treffern beträgt rund 49,77%.

99,9 ist eine Erwartungszahl, keine gemessene Anzahl von Menschen. Die 0,1% stammen nicht aus Ghost Clusters und sind keine festgestellte Fehlerrate österreichischer Systeme. Das Modell demonstriert, warum eine klein erscheinende Falschpositivrate bei seltenen echten Verbindungen nicht automatisch hohe Verlässlichkeit der ausgegebenen Treffer bedeutet. Durch unabhängige Zusatzbelege, einen engeren Kandidatenraum und Nichtentscheidungen kann sich das Ergebnis ändern; diese Änderungen sind eigens zu messen.

### 6.13 Dauerhaftigkeit eines einmal entstandenen Ankers

Wird eine Identität verlässlich mit einer öffentlich sichtbaren Adresse verbunden und der Anker weitergegeben, kann dessen spätere Verwendung zusätzliche historische oder neue Aktivität erschließen. Das kann auch dann geschehen, wenn die ursprüngliche Meldung nicht mehr beim ersten Halter vorliegt. Das Ausmaß hängt von Adresswiederverwendung, öffentlich sichtbaren Folgewegen und zusätzlichen Daten ab; es ist nicht gleichbedeutend mit lückenloser Sichtbarkeit jedes künftigen Vorgangs.

Die [finalen EDPB-Leitlinien 02/2025, Version 2 vom Juli 2026, Rn. 63–64 und 103](https://www.edpb.europa.eu/system/files/2026-07/edpb_guidelines_202502_blockchain_v2_en.pdf), behandeln die schwierige Löschung und die Bedeutung wirksamer Verhinderung künftiger Verknüpfung. Sie halten auch fest, dass die Löschung geeigneter Off-Chain-Daten je nach Gestaltung und Sachverhalt künftige Identifikation verhindern kann. „Nach einem Anker ist Privatsphäre immer unmöglich“ wäre daher zu absolut.

Diese mögliche Schutzwirkung setzt voraus, dass erforderliche Zusatzdaten aus der Reichweite des jeweiligen Beobachters verschwinden. Eine bereits entwendete oder veröffentlichte Zuordnungskopie wird durch spätere Löschung beim ursprünglichen Halter nicht zurückgeholt. Wer einen geeigneten Anker bereits besitzt, kann den entsprechenden öffentlichen Ausschnitt auch ohne neue Anbieterabfrage oder neue Steuerübermittlung erneut untersuchen. Ein Pflichtarchiv und ein entwendeter Anker sind deshalb verschiedene Dauerhaftigkeitsprobleme: Das Archiv kann durch wirksame Zugriffskontrollen begrenzt werden; die vorhandene fremde Kopie lässt sich dadurch nicht nachträglich ungeschehen machen.

**Vorläufiger Befund:** Konkrete Anbieteranker können den Informationsgehalt eines entwendeten oder befugt erlangten Datensatzes deutlich über seine eigenen Zeilen hinaus erweitern. Wie weit, mit welchen Fehlern und gegenüber welcher Person, muss stufenweise belegt werden. Jahresaggregate allein tragen eine solche direkte Anschlussfähigkeit nicht als bereits bewiesene Tatsache.

## 7 Sicherheits- und Missbrauchsfolgen der Konzentration

### 7.1 Anbieterbestände sind ein eigenständiger Risikogegenstand

Die Anbieter halten den Ausgangsbestand, bevor eine Behörde eine Meldung erhält. Er kann im selben Geschäftskontext Identitätsnachweise, Kontakt- und Wohnadressdaten, Aktivitäten und finanzielle Positionen verbinden. Ein verpflichteter Bestand bleibt gegebenenfalls nach Kontoschließung oder trotz Löschungswunsch erhalten. Seine Sicherheitsfolgen sind deshalb unabhängig davon zu prüfen, ob die Behörde später eine umfassende Verknüpfung durchführt.

Der Ausdruck „Honeypot“ bezeichnet hier die Attraktivität dieses kombinierten Bestands für Angreifer, keine absichtlich eingerichtete Köderdatenbank. Die Konzentration hat mehrere Funktionen: Sie macht Zielpersonen erreichbar, kann deren finanzielle Attraktivität anzeigen und liefert Details für glaubwürdige Täuschung. Ein Adressanker kann darüber hinaus öffentliche Folgeinformationen erschließen. Die Kombination kann mehr ermöglichen als die isolierten Felder; bloße Byte- oder Datensatzzahlen beschreiben diesen Informationsgewinn nicht vollständig.

Das gilt auch bei rechtmäßiger Speicherung. Eine rechtliche Pflicht kann den Zeitraum verlängern, in dem ein kompromittierter Zugang diese Informationen vorfindet. Sie beweist nicht, dass jeder Vorfall gerade durch die Pflicht verursacht wurde, und sie verlangt nicht von selbst unbegrenzte Supportrechte. Für die Bewertung einer konkreten Regel ist der zusätzliche Bestand gegenüber sonst ohnehin bestehenden notwendigen Aufzeichnungen festzustellen. Das allgemeine Risiko der verbliebenen Aufzeichnungen besteht unabhängig von dieser Differenz weiter.

### 7.2 Tatsächliche Vorfälle und ihre technische Bedeutung

Der [Coinbase-Bericht an die SEC, Mai 2025, Item 1.05](https://www.sec.gov/Archives/edgar/data/1679788/000167978825000094/coin-20250514.htm), nennt bestochene Supportbeschäftigte oder Auftragnehmer und entwendete Kundeninformationen, darunter Identitätsunterlagen, Adressen, Salden-Schnappschüsse und Transaktionshistorien. Private Schlüssel und unmittelbarer Zugang zu Kundengeldern waren nicht betroffen. Der [Anbieterbericht vom 15. Mai 2025, Reimbursement criteria](https://www.coinbase.com/blog/protecting-our-customers-standing-up-to-extortionists), bestätigt dennoch nachfolgende Täuschung, durch die Kunden Geld übertrugen. Das ist ein dokumentierter Anbieter-Schadensweg ohne unmittelbaren Schlüsselverlust, nicht nur eine theoretische Warnung.

Die [Kroll-Mitteilung an FTX-Anspruchsteller von 2023, S. 1–2](https://ftxquestions.kroll.com/docs/Kroll_Notice_to_FTX_Claimants_4879-3276-7625-2.pdf), beschreibt einen SIM-Swap gegen einen Beschäftigten und Zugriff auf Cloud-Unterlagen eines Dienstleisters für mehrere Kryptounternehmen. Möglich betroffen waren Identitäts-, Wohnadress-, Forderungs-, Konto- und Kryptobestandsdaten. Die FTX-Vermögenssysteme waren nicht selbst betroffen. Der konkrete Informationsbestand mehrerer Unternehmen war somit an einem gemeinsamen Dienstleisterzugang exponiert; ein bestimmter nachfolgender Vermögensschaden wird aus der Mitteilung nicht abgeleitet.

[Fractal ID, eigener Bericht vom 16. Mai 2025](https://web.fractal.id/a-better-way-is-possible-dataless-kyc-and-open-sourcing-fractal-id/), bestätigt den Identifizierungsdaten-Leak von Juli 2024 und nennt AML- und vertragliche Pflichten für bestimmte verbliebene Unterlagen. Beschriebene Datenarten umfassen Identitätsdokumente, Wohnadressen und bereitgestellte Wallet-Adressen. Das belegt die Möglichkeit eines Identitäts-Adress-Ankers bei einem KYC-Dienstleister. Die Darstellung ist eine Anbieterquelle; deren Erklärung beweist weder die Notwendigkeit jedes Felds noch die Wirksamkeit des später beworbenen Konzepts. Der Primärtext war über den offiziellen Suchindex zugänglich, der direkte Origin-Abruf zuletzt unzuverlässig.

Die Fälle entstanden nicht durch nachgewiesene DAC8-Verarbeitung. Sie belegen aber unmittelbar relevante Mechanismen auf der Anbieterseite: Missbrauch berechtigter Zugänge, Konzentration beim Dienstleister und finanzielle Folgeangriffe aus reinen Informationen. Ein technischer Entwurf würde einen wesentlichen Teil des Gegenstands verfehlen, wenn er nur externe Angriffe auf Behörden untersuchte.

### 7.3 Zugriffsszenarien und Kontrollgrenzen

| Szenario | Zu bestimmende Reichweite | Maßgebliche Kontrollfrage |
|---|---|---|
| Zweckwidrige Einzelabfrage | Eine bestimmte Person, erreichbare Felder und Jahre | Werden tatsächlicher Fallbezug und spätere Abfrageprüfung wirksam geprüft? |
| Gestohlene Routinekennung | Alle ohne Zusatzfreigabe erreichbaren Kunden und Quellen | Was begrenzen Rolle, Sitzungsdauer, Abrufrate und Feldfreigabe tatsächlich? |
| Manipulierter Support oder Dienstleister | Kundensicht, Identitätsunterlagen, Historie, mehrere Auftraggeber | Sind historische Daten und Auftraggeber getrennt oder über denselben Zugang erreichbar? |
| Administrator oder Massenexport | Archive, Sicherungen, Kopien und Querverknüpfungen | Sind Freigabe, Schlüsselverwaltung, Export und Kontrolle wirklich unabhängig? |

Verschlüsselung im Ruhezustand schützt gegen bestimmte Datenträger- oder Speicherzugriffe. Sie verhindert nicht automatisch einen Export durch eine Anwendung, die für eine gestohlene berechtigte Sitzung entschlüsselt. Multifaktor-Authentifizierung begrenzt bestimmte Zugangsdiebstähle, nicht von sich aus den bestochenen berechtigten Beschäftigten. Protokollierung dokumentiert Zugriffe; ihre Schutzwirkung hängt zusätzlich von Auswertung, Erkennungszeit und Eingriffsmöglichkeit ab. Diese Aussagen sind technische Funktionsgrenzen, keine Feststellung fehlender Maßnahmen in einem konkreten System.

Ein positives Audit einer Behörde beantwortet nicht die Frage, welche privaten Dienstleister Unterlagen vorhalten. Umgekehrt ist ein Anbieterleck kein Auditbefund gegen das BMF. Der [Rechnungshofbericht Bund 2024/16, S. 14 und 79–82](https://www.rechnungshof.gv.at/rh/home/home/2024_16_IT-Sicherheit_BM.pdf), enthält positive BMF-Sicherheitsbefunde im untersuchten Zeitraum, überwiegend 2018–2022. Eine [BMF-Disziplinarentscheidung von 2019, S. 1 und 6–7](https://www.ris.bka.gv.at/Dokumente/Dok/DKT_BMF_20191009_02_084_18_DK_17_00/DKT_BMF_20191009_02_084_18_DK_17_00.pdf), dokumentiert dagegen private AIS-Abfragen und deren Rekonstruktion aus Protokollen. Beides ist einzubeziehen; weder Quelle stellt die heutige DAC8-spezifische Kontrollwirkung fest.

### 7.4 Zusätzliche Jahrgänge, Empfänger und gemeinsame Angriffswege

Eine Übermittlung beseitigt die Ausgangsdaten beim Anbieter nicht. Neben den Ausgangsbeständen können weitere Empfängerkopien entstehen. Wenn Meldungen mehrerer Anbieter im selben Zugriffskontext zusammenführbar sind, kann ein kompromittierter Empfänger mehr Quellen einer Person erreichen als ein einzelner Anbieter. Das ist ein bedingter Reichweitenbefund, nicht die Behauptung, jeder Zugang sehe die gesamte Branche.

Gemeinsame KYC- oder Supportdienste können ihrerseits mehrere Anbieter betreffen. Gleiches gilt für gemeinsame Administrationssysteme, Exportverzeichnisse oder Authentisierungsdienste. Risiken solcher Stellen sind nicht notwendig unabhängig. Ohne Beleg der Unabhängigkeit darf weder die Formel „ein Anbieter multipliziert mit Zahl aller Anbieter“ noch eine Wahrscheinlichkeit mindestens eines Leaks aus frei gewählten Einzelraten berechnet werden.

Zusätzliche Jahre erweitern zunächst den erreichbaren Beobachtungszeitraum. Ob der einzelne Angriff wahrscheinlicher wird, lässt sich daraus nicht bestimmen. Sein möglicher Informationsumfang kann dagegen konkret gemessen werden: erreichbare Personen, Quellen, Jahrgänge, Identitätsunterlagen und Ledger-Anker. Die Aussagekraft einer alten Position nimmt möglicherweise ab, während ihre Eignung für glaubwürdige Betrugsansprache oder falsche Zielauswahl fortbesteht.

### 7.5 Informationsmissbrauch braucht keine perfekte Vermögensbilanz

Eine Betrugsnachricht kann einen richtigen vergangenen Vorgang verwenden, ohne das gesamte heutige Vermögen zu kennen. Die falsche Vermutung großen Vermögens kann ebenfalls zu gefährlicher Zielauswahl führen. Die [französische Gendarmerie vom 13. September 2026](https://www.gendarmerie.interieur.gouv.fr/gendinfo/terrain/immersion/2026/la-strategie-de-la-gendarmerie-face-aux-cryptorapts-partie-2-2) beschreibt geleakte Waltio-E-Mail-Adressen als Mittel krimineller Kryptozielauswahl, teilweise mit falschen Bestandsvorstellungen. Das ist eine amtliche operative Einschätzung, kein fallbezogenes gerichtliches Kausalurteil und keine österreichische Eintrittsquote.

Finanzielle Täuschung, unerwünschte Profilbildung und körperliche Bedrohung haben unterschiedliche Beweis- und Schadenswege. Sie dürfen nicht als ein einziger automatisch eintretender Schaden behandelt werden. Für die technische Gefahrenanalyse sind Kontaktierbarkeit, finanzielle Hinweise, aktuelle Wohnadresse und tatsächlicher Ledger-Anker getrennt zu markieren. Ebenso ist aus einem benannten Händlerkontakt nicht ohne weitere Prüfung eine sensible persönliche Eigenschaft der zahlenden Person abzuleiten.

Bei selbstverwahrten nativen Kryptowerten bewirkt eine bestätigte Übertragung keine automatisch verfügbare Rückbuchung durch eine zentrale Stelle. Ermittlungen, Sicherstellungen oder Rückgewinnung über Intermediäre bleiben möglich; andere Assets können zusätzliche Sperrfunktionen haben. Datenkenntnis ist weiterhin kein privater Schlüssel. Der besondere Missbrauchsweg liegt darin, dass geleakte Informationen eine Person zur eigenen Verfügung über ihre Schlüssel bewegen oder als Ziel erscheinen lassen können. Daraus folgt keine pauschale Aussage, jede Kryptoverfügung sei endgültig verloren oder jeder Bankvergleich sei risikolos.

**Vorläufiger Befund:** Entwendbarkeit und mindestens ein finanzieller Folgeweg sind durch reale Anbieterberichte belegt. Der zusätzliche Umfang eines konkreten langjährigen oder anbieterübergreifenden Bestands ist dagegen durch eine Rollen- und Kopienprüfung zu bestimmen. Eine konkrete österreichische Leakwahrscheinlichkeit und die Unzulänglichkeit bestimmter aktueller Kontrollen wurden nicht festgestellt.

## 8 Technisch engere Daten- und Zugriffskonzepte

### 8.1 Der richtige Vergleichsgegenstand

Ein alternatives Design muss an derselben Aufgabe gemessen werden. Eine gezielte Prüfung vergangener Vorgänge, automatische Auswahl neuer Prüfungsfälle und sofortiger Massenabgleich sind unterschiedliche Aufgaben. Das vollständige Wiederauffinden einer bekannten Akte beweist nicht dieselbe Leistung wie das Entdecken einer unbekannten Unstimmigkeit. Ebenso ist ein unveränderter Modellscore kein Nachweis gleichen Steuerertrags.

Die Vergleichsbasis muss unabhängig fortbestehende Aufzeichnungen erhalten. Andernfalls wäre eine behauptete Datenreduktion nur eine Verlagerung in ein anderes System. Zu vergleichen sind deshalb mindestens Inhalt, Zahl der Kopien, erreichbare Rollen, Dauer, befugte Abrufbarkeit, Fehler und tatsächlich erzielter Nutzen. Manche Alternative wäre unter dem bestehenden Recht umsetzbar; eine Änderung gesetzlicher Meldefelder oder Fristen benötigte gegebenenfalls Rechtsänderung. Das rechtliche Urteil hierzu ist getrennt einzuholen.

### 8.2 Eigener Modellversuch: vollständiges Archiv, engerer Routinezugriff

Das fünfte Modell enthält 10.000 synthetische Personen, zehn Jahrgänge und acht abstrakte Felder je Personenjahr. Das ergibt 800.000 logische Datenzellen. Im Ausgangsmodell sind alle Zellen über den Routinezugang erreichbar. Die Alternative stellt diesem Zugang nur drei Felder des letzten Jahrgangs bereit. Ein vollständiges Archiv bleibt über eine gesonderte, im Modell bereits autorisierte Archivrolle abrufbar.

| Prüfgröße | Ausgangsmodell | Alternative |
|---|---|---|
| Routinemäßig erreichbare Zellen | 800.000 | 30.000 |
| Vollständiger archivierter Bestand | 800.000 im Vollbestand | 800.000 im Pflichtarchiv |
| Gespeicherte logische Zellen einschließlich Routinekopie | 800.000 | 830.000 |
| Ergebnisse der 100.000 autorisierten Vollaktenabfragen | Referenz | Alle Werte identisch |

Der routinemäßig erreichbare Umfang sinkt im Modell um 770.000 Zellen, entsprechend 96,25%. Eine historische Routineabfrage und eine Routineabfrage zusätzlicher Felder werden nicht bedient. Alle 100.000 geprüften, bereits autorisierten Archivabfragen liefern dagegen dieselben vollständigen Werte wie die Referenz. Der Test wurde ausgeführt, nicht nur vorgeschlagen.

Diese 96,25% sind ausschließlich eine Verringerung der erreichbaren **Zellenzahl unter den Modellannahmen**. Sie sind weder 96,25% weniger Datenschutzrisiko noch eine gemessene Sicherheitsverbesserung. Felder unterscheiden sich in Sensibilität und Verknüpfungswirkung. Die Alternative hat sogar mehr logische Speicherung durch die zusätzliche Routinekopie. Physischer Speicherverbrauch, Authentisierung, Verschlüsselung, Freigabezeiten, Administratoren, Protokolle und Sicherungen werden vom In-Memory-Programm nicht umgesetzt.

Das Ergebnis ist trotzdem konkret: Die behauptete Untrennbarkeit vollständiger Aufbewahrung und vollständiger Routineverfügbarkeit ist technisch widerlegt. Noch nicht belegt ist, dass die Routinebegrenzung ohne Nutzenverlust für eine bestimmte Steueraufgabe auskommt. Dafür muss geprüft werden, welche Fälle mit dem engeren Zugang überhaupt erkannt würden und wie eine begründete Archivöffnung im tatsächlichen Arbeitsablauf funktioniert.

### 8.3 Welche Trennung tatsächlich Schutzwirkung erzeugen könnte

Ein getrennt benanntes Archiv ist noch keine wirksame Trennung. Wenn dieselbe Routinekennung, derselbe Administrator oder derselbe Exportweg beide Bereiche erreicht, kann der behauptete Schutz ausfallen. Ein zu prüfendes Design benötigt daher eigenständige Berechtigungen, kontrollierte zeitliche Freigaben, möglichst getrennte Administrations- und Schlüsselwege, beschränkte Massenauszüge sowie nachträgliche Prüfung. Welche Kombination erforderlich und wirksam ist, hängt vom Bedrohungsmodell ab.

Identität und Aktivität können getrennt gehalten und nur für bestimmte Zwecke verbunden werden. Ein fester pseudonymer Schlüssel kann aber weiterhin Jahrgänge verknüpfen; eine Zuordnungstabelle oder charakteristische Aktivität kann identifizieren. Verschlüsselung oder Pseudonymisierung darf deshalb nicht mit Anonymisierung gleichgesetzt werden. Auch föderierte Abfragen können ein Gesamtdossier erzeugen, wenn ein berechtigter oder gestohlener Zugang die Einzelantworten sammeln darf.

Ein enger Routinebericht mit begründeter Nachforderung kann den zentralen Erstbestand verkleinern, hält aber möglicherweise die detaillierteren Anbieterunterlagen weiter vor. Es sind dann beide Seiten zu bilanzieren: weniger zentrale Exposition, fortbestehende private Exposition, zusätzliche Anfragewege, Antwortzeiten und Ausfälle. Keine dieser Varianten ist schon deshalb überlegen, weil sie „dezentral“ heißt.

### 8.4 Öffentliche Gestaltungskomparatoren

[Ledger, Bericht vom 15. Februar 2022, Abschnitt 2](https://www.ledger.com/blog-privacy-security-at-ledger-a-year-in-review), beschrieb bereits migrierte Bestelldaten älter als 18 Monate in einem segregierten, streng zugriffsbeschränkten Archiv bei fortbestehender zehnjähriger Rechnungslegungsaufbewahrung. Eine Reduktion auf drei Monate war damals ein noch nicht vollendetes Ziel. Das ist ein tatsächlicher Anbieterbericht über eine Architektur, kein unabhängiger Wirksamkeitsnachweis oder aktueller österreichischer CASP-Test.

Die [FTC-Beschwerde gegen Blackbaud, S. 2–5, Rn. 6–10, 16, 19 und 23](https://www.ftc.gov/system/files/ftc_gov/pdf/Blackbaud-Complaint.pdf), beanstandete unter anderem unnötige Bestände und schwache Trennung; die Vorwürfe wurden im Vergleich erledigt, nicht streitig gerichtlich bewiesen. Die verbindliche [Endanordnung vom 17. Mai 2024, PDF S. 10–14, Abschnitte II–IV](https://www.ftc.gov/system/files/ftc_gov/pdf/2023181_blackbaud_final_consent_package.pdf), verlangt konkrete Lösch-, Fristen- und Zugriffsmaßnahmen, erhält aber notwendige Unterlagen und Beweisholds. Sie zeigt ein differenziertes Gestaltungskonzept, nicht dessen bereits gemessenen Erfolg oder österreichische Rechtsgeltung.

### 8.5 Was datenärmere Analyseverfahren bereits leisten — und nicht leisten

[Project Hertha, BIS/Bank of England vom 5. Juni 2025, gedruckte S. 7–18, Tabelle 1 auf S. 12](https://www.bis.org/publications/project-hertha-identifying-financial-crime-patterns-real-time-retail-payment-systems.pdf), verwendete 1,8 Millionen synthetische Konten und 308 Millionen Transaktionen. Bei derselben Zielmarkierungsquote von 1% erfasste das Bankmodell 44% der simuliert rechtswidrig genutzten Konten, das minimale Netzwerkmodell 39% und Zusammenarbeit 49%. Das minimierte Einzelmodell war nicht gleichwertig. Gemessen wurde ein synthetisches Zahlungsnetz, keine Kryptobestands- oder Steuerprüfung. Die Markierungsquote wird hier nicht als allgemeine Falschpositivrate ausgegeben.

[Arora et al., 2023, S. 2 und 7–10, Tabellen 2, 4 und 5](https://arxiv.org/pdf/2310.04546), erprobten föderiertes Lernen und geschützte Mehrparteienberechnung. Die Fläche unter der Precision-Recall-Kurve betrug 0,79 zentral, 0,70 in lokaler föderierter Simulation und 0,49 im zeitbegrenzten verteilten Versuch. Die Bedingungen unterschieden sich: insbesondere zwanzig Trainingsdurchläufe gegenüber einem Durchlauf im begrenzten Betrieb. Geschützt wurde ein zusätzliches Bankmerkmal; wesentliche Transaktions- und Identitätsdaten lagen schon beim Hub. Eine formale Differential-Privacy-Garantie wurde nicht gegeben. Das ist ein Machbarkeitsbefund mit Grenzen, kein gleicher Steuerkontrollnutzen bei vollständig verhinderten Profilen.

**Vorläufige Bewertung:** Es gibt konkrete Alternativen, die nicht auf vollständiges Vergessen notwendiger Unterlagen angewiesen sind. Eigene Modelle belegen die logische Zugriffstrennung; öffentliche Versuche belegen Gestaltungsmöglichkeiten und Zielkonflikte. Der entscheidende nächste Nachweis ist der zusätzliche Nutzen der breiteren Verfügbarkeit gegenüber dem engeren Konzept unter identischen echten Aufgaben. Diesen Nachweis liefern die vorhandenen Quellen noch nicht.

## 9 Zusammengefasste Antworten auf die Gutachtenfragen

| Frage | Vorläufige technische Antwort | Beweisstatus |
|---|---|---|
| Ermöglichen mehrere Jahre mehr Personenwissen? | Ja, zeitliche Aktivität und Quellenbeziehungen werden unter verlässlichem Join sichtbar. | Mechanismus begründet; konkrete österreichische Breite nicht geprüft |
| Entsteht daraus eine vollständige Vermögensbilanz? | Nein, nicht aus den Bewegungsaggregaten allein; verschiedene Endbestände bleiben vereinbar. | Konstruktiv durch eigene Gegenmodelle gezeigt |
| Kann zusätzliche Datenfusion ein bestandsnahes Teilprofil liefern? | Ja, Bestandsfelder und verifizierte Anker können Lücken einzelner Quellen reduzieren. | Technische Möglichkeit; reale Abdeckung und Genauigkeit offen |
| Können Daten mit Blockchain-Aktivität verbunden werden? | Mit direkten, geprüften Anbieterankern ja; Jahresaggregate allein sind kein validierter direkter Anschluss. | Datenarchitektur und öffentliche Dienstbenchmarks; Personenfehler offen |
| Ist Missbrauch ohne private Schlüssel realistisch? | Ja, ein finanzieller Täuschungsweg ist dokumentiert; weitere Wege sind gesondert zu belegen. | Reale Anbieterberichte; keine DAC8-Schadensquote |
| Können Daten bei Anbietern oder gemeinsamen Dienstleistern entwendet werden? | Solche Entwendungen sind tatsächlich dokumentiert. Pflichtbestände gehören eigenständig in das Risikomodell. | Vorfälle belegt; konkrete heutige österreichische Kontrollen nicht geprüft |
| Sind engere Zugriffskonzepte technisch möglich? | Ja, vollständige Aufbewahrung und begrenzter Routinezugriff sind logisch vereinbar. | Eigener ausgeführter Archivvergleich; kein Produktivsicherheitsnachweis |
| Erreichen sie nachweislich gleichen Verwaltungsnutzen? | Für den konkreten Gegenstand noch nicht festgestellt; öffentliche Benchmarks zeigen auch Einbußen. | Aufgabenspezifischer Vergleich fehlt |

Für die anwaltliche Arbeit folgt daraus eine überprüfbare technische Grundlage, aber kein vorweggenommenes rechtliches Ergebnis: Der relevante Informationsumfang reicht über die isolierte Jahresmeldung hinaus. Er ist anhand des tatsächlichen Datenverbunds und des tatsächlichen Zugangs zu bestimmen. Gleichzeitig dürfen Vollständigkeit, Genauigkeit und Notwendigkeit eines solchen Verbunds nicht allein aus seiner technischen Machbarkeit abgeleitet werden.

## 10 Ergänzungen für die unabhängige sachverständige Fassung

### 10.1 Die noch fehlenden Systemnachweise

Für die Anbieterprüfung benötigt werden ein Feld-/Zweck-/Fristeninventar, dokumentierte Dienst- und Transaktionsschichten, Rollen und tatsächlich mögliche Exporte, Dienstleisterzugänge, Kopien und Löschtrigger. Für Behörden benötigt werden das aktuelle Quellen- und Merkmalsinventar, Join-Regeln, tatsächlich ausgeübte Abfragen, kopienspezifische Fristen und Nachweise der Kontrollprüfung. Sicherheitsrelevante Details müssen nicht öffentlich veröffentlicht werden; eine geschützte Prüfung kann ausreichend sein.

Die Zugangswege haben unterschiedliche Reichweite. Eigene Auskunft betrifft die eigenen Daten, nicht automatisch ein institutionelles Audit. Informationszugang betrifft vorhandene Unterlagen, nicht die Erstellung einer neuen Studie. Aufsichtsbehördliche oder gerichtliche Prüfung und Parteieinsicht sind nicht deckungsgleich. Die Abgrenzung dokumentiert die Quellenarbeit zu [DSG § 22](https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10001597) und [DSGVO Art. 15 und 58](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng). Voraussetzungen und Schutzinteressen sind rechtlich gesondert zu beurteilen. Es wurde keine Anfrage versandt.

Fehlende öffentliche Unterlagen sind eine Beweisgrenze, kein negativer Auditbefund. Für eine gerichtliche technische Grundlage sollte auch ein nicht zugänglicher oder nicht aussagekräftiger Prüfbereich ausdrücklich im Ergebnis stehen.

### 10.2 Ein vorab festgelegter empirischer Vergleich

Der nächste Versuch sollte dieselben rechtmäßig verfügbaren Prüfungsfälle unter einem, drei, fünf und zehn Jahren beziehungsweise verschiedenen Feldkombinationen vergleichen. Zuerst sind die Aufgaben, der zulässige Fallumfang und eine begründete Toleranz für Nutzeneinbußen festzulegen. Dann werden die Modelle ohne Kenntnis der tatsächlichen Fallausgänge ausgewertet. Die Vergleichsstichprobe braucht unabhängig bekannte wahre Werte; ein bisheriges Risikolabel darf nicht ohne Prüfung als Wahrheit gelten.

Für Vermögensschätzungen sind Abdeckung, absolute und relative Fehler, systematische Über-/Unterschätzung und Rangfehler getrennt zu berichten. Für Zuordnung sind Kandidatenmenge, Nichtentscheidungen, richtige und falsche Treffer, Abdeckung und Konfidenzintervalle je Stufe erforderlich. Große Beträge, kleine Bestände, wiederverwendete Adressen, Sammelauszahlungen, Eigenüberträge und fehlende On-Chain-Entsprechungen dürfen nicht aus der schwierigen Vergleichsgruppe entfernt werden.

Für das Archivdesign sind mindestens dieselben autorisierten Fälle, vollständige Rekonstruierbarkeit, Abrufzeiten, Freigabeaufwand und Ausfälle zu prüfen. Daneben werden erreichbare Personenjahre, sensitive Felder, Quellenverbindungen, Massenauszüge, Erkennung unzulässiger Zugriffe und Löschwirkung gemessen. Gleiches Abrufresultat und gleiche automatische Fallentdeckung bleiben zwei getrennte Endpunkte. Eine Alternative kann bei einem Endpunkt gewinnen und beim anderen verlieren.

Die Untersuchung darf selbst keinen neuen öffentlichen Identitäts-Blockchain-Bestand erzeugen. Echtdaten, falls erforderlich, gehören in einen minimierten geschützten Raum; Identitäten und Adressanker sind getrennt zu verwahren. Öffentlich können Methoden, aggregierte Ergebnisse und synthetische Negativkontrollen bereitgestellt werden. Fremde Personen zu Demonstrationszwecken zu deanonymisieren wäre keine notwendige Ergänzung dieses Entwurfs.

## Anhang: eigene Modelle und Reproduzierbarkeit

Das beigefügte Programm `gutachten-finanzdatenprofile-modelle.py` verwendet ausschließlich die Python-Standardbibliothek, Decimal-Arithmetik und synthetische Kennungen. Es liest keine Dateien, sendet keine Netzwerkanfragen und schreibt nur JSON auf die Standardausgabe. Die Ausführung erfolgte mit Python 3.12.14; alle Assertions bestanden. Der optimierte Python-Modus wird abgewiesen, damit Assertions nicht unbemerkt deaktiviert werden. Die Ausgabe wurde wiederholt und auf Identität geprüft.

Ausführung im Dokumentverzeichnis: `python3 -B gutachten-finanzdatenprofile-modelle.py`. Das JSON enthält zu jedem Modell seine Annahmen und Ergebnisse. Es ist kein amtliches XML-Meldeschema. Die allgemeine Abgangskategorie und ihr externer Teil im ersten Modell sind überlappende Beobachtungen, nicht zwei unabhängige Transfers. Die beiden EUR/BTC-Bewertungen von 60.000 beziehungsweise 10.000 gehören zu verschiedenen isolierten Modellen, nicht zu einem behaupteten Kursverlauf.

| Modell | Geprüftes Ergebnis | Nicht damit bewiesen |
|---|---|---|
| 1 Bestands-Eindeutigkeit | Gleiches Beobachtungsprofil, 10 BTC oder 0 BTC nach zehn Jahren | Häufigkeit oder durchschnittlicher Bestandsfehler |
| 2 Kapitalwiederverwendung | 200.000 Euro Käufe und Verkäufe bei 10.000 Euro Endbestand | Reale Handels- oder Vermögensverteilung |
| 3 Anbieterübertrag | Doppelbeobachtung eines Transfers; Jahreswert-Join kann falsch verbinden | Reale Join-Fehlerrate oder Eigentum allein aus TXID |
| 4 Fristuhr | 2026 bis Ende 2036; neuer Jahrgang setzt alte Uhr nicht zurück | Tatsächliche Behörden-/AML-Fristen oder Löschumsetzung |
| 5 Zugriff | 800.000 gegenüber 30.000 Routinezellen; 100.000 Archivresultate identisch | Leakwahrscheinlichkeit, physischer Speicher oder gleiche Fallentdeckung |
| 6 Basisrate | Verhältnis erwarteter Treffer 110/221 = rund 49,77% Präzision | Gemessene Zuordnungsleistung eines realen Systems |

SHA-256 des ausgeführten Modellprogramms: `2a0797c0e187be556b6eef950b91001a0041b56726bda269a6eaf66e0490efcc`.

Das zusätzliche Programm `gutachten-chaindaten-modelle.py` verwendet ebenfalls ausschließlich Standardbibliothek, Decimal und erfundene Kennungen. Es schreibt nur deterministisches JSON, nimmt keine Netzwerk-/Dateiabfragen vor und weist den optimierten Modus ab. Ausführung: `python3 -B gutachten-chaindaten-modelle.py`. Die Modelle wurden mit Python 3.12.14 ausgeführt; sämtliche Assertions bestanden. Wiederholte Ausgaben sind identisch. Es handelt sich um Kontrollrechnungen und symbolische Gegenwelten, nicht um einen Bitcoin-Parser, eine EVM, ein Signaturverfahren oder eine echte Konsenssimulation.

| Chain-Modell | Geprüftes Ergebnis | Nicht damit bewiesen |
|---|---|---|
| C1 UTXO | Input-Ergänzung, 0,0001 BTC Gebühr; verschiedene Eigentümerwelten mit identischer Projektion | Validierung realer Transaktionsbytes, Skripte oder Signaturen |
| C2 Wertpfad | Poison markiert 0,9999 BTC Nennwert; Haircut verteilt 0,5 BTC einschließlich Gebührenanteil | Straftat, Eigentum oder wahre eindeutige Input-Output-Allokation |
| C3 Cluster | Eine falsche Kante verbindet zwei Gruppen; Kantenwiderruf und Neuberechnung trennen sie | Empirische Fehlerhäufigkeit oder vollständiger Personenbestand |
| C4 Bridge | Eine 1:1-Position statt zweier unabhängig addierbarer Assets | Echte Deckung, Preisgleichheit, Einlösesicherheit oder Berechtigung |
| C5 Snapshot | Gleiche Höhe kann verschiedene Zweige und Positionen bezeichnen | Reorg-Häufigkeit oder Konsensvalidierung |
| C6 Revert | 1,997 ETH nach gesetztem Fehlschlag; gleiche Fehlerkennung bei verschiedener vorgelagerter Delegation | EVM-Ausführung, vollständige Gebührenrechnung aller Chains oder gültige Autorisierungstupel |

SHA-256 des ausgeführten Chain-Modellprogramms: `c8c3a0ba8c118e53cae8982027b94eb7ec7d740ebe1cdf052c4372ec54f37511`.

Der Entwurf und seine Modelle sind lokal erstellte Arbeitsunterlagen. Eine unabhängige sachverständige Fassung muss Autorenschaft, Qualifikation, Auftrag, überprüften Datenstand, zugängliche Systemunterlagen und verbleibende Grenzen ausdrücklich dokumentieren. Die vorhandenen Ergebnisse können dafür übernommen, reproduziert, präzisiert oder widerlegt werden.
