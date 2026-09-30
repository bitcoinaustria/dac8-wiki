---
title: "Finanzdaten über Jahre: Vermögensprofile, Blockchain-Verknüpfung und Sicherheitsrisiken"
type: report
sources:
  - wiki/theses/transaction-data-wealth-inference.md
  - wiki/topics/dac8-and-the-wealth-register-risk.md
  - wiki/references/dac8-inference-linkage-and-error-evidence.md
  - wiki/references/dac8-blockchain-linkage-expert-evidence-protocol.md
  - wiki/references/dac8-data-lifecycle-access-retention-remedies.md
  - wiki/references/krypto-mpfg-provider-record-architecture.md
  - wiki/references/identity-to-public-ledger-linkage-evidence.md
  - wiki/theses/account-model-linkage-exposure.md
  - wiki/references/transaction-profiling-and-sensitive-inference.md
  - wiki/references/austrian-tax-risk-scoring-and-financial-data-use.md
  - wiki/references/austrian-insider-database-misuse.md
  - wiki/references/financial-data-breach-and-security-authorities.md
  - wiki/references/bearer-asset-irreversibility-and-leak-consequences.md
  - wiki/references/dac8-field-necessity-and-alternatives.md
  - wiki/references/dac-history-timeline.md
  - wiki/references/austrian-security-evidence-access.md
  - wiki/references/dac8-dpia-accountability-and-security-evidence.md
  - wiki/references/dac8-challenge-scope-and-residual-duties.md
  - raw/articles/2026-09-30-eu-dac-future-edps-opinion-20-2026-dac-recast.md
  - raw/articles/2026-09-30-eu-dac9-directive-2025-872.md
  - raw/articles/2026-08-27-eu-tfr-regulation-2023-1113.md
  - raw/articles/2026-08-27-eu-amlr-regulation-2024-1624.md
  - wiki/references/dac8-bulk-data-case-transfer-matrix.md
  - raw/articles/2026-09-19-coinbase-insider-social-engineering-disclosure.md
  - raw/articles/2026-09-29-bearer-kroll-claimant-data-breach.md
  - raw/articles/2026-09-29-bearer-fractal-id-kyc-breach.md
generated: 2026-09-30
verified: 2026-09-30
---

# Finanzdaten über Jahre

## Vermögensprofile, Blockchain-Verknüpfung und Sicherheitsrisiken

Argumentationsvermerk und Prüfprogramm für ein unabhängiges technisches Gutachten. Stand: 30. September 2026. Mit [LLM Wiki](https://github.com/bitcoinaustria/dac8-wiki) erstellt. Rechercheunterlage, keine Rechtsberatung und kein bereits durchgeführtes Sachverständigengutachten.

## Kurzbefund

Einzelne Finanzmeldungen können begrenzt sein und zusammen dennoch ein aussagekräftiges Personenprofil bilden. Wiederkehrende Identifikatoren verbinden Jahre und Anbieter. Bestandsdaten ergänzen Bewegungsdaten. Jahresaggregate enthalten keine Wallet-Adressen oder Transaktionskennungen. Einzelunterlagen des Anbieters können aber eine verlässliche Verbindung zur öffentlichen Blockchain enthalten und dadurch weitere Vorgänge außerhalb des Anbieters erschließen. Deshalb sind Meldungen und zusätzliche Zuordnungen getrennt zu untersuchen.

Das rechtfertigt die begrenzte Arbeitshypothese eines **„Vermögensregisters light“**: eine personenbezogen durchsuchbare Sammlung von Vermögenshinweisen und Finanzaktivitäten. Es rechtfertigt nicht die Behauptung, Behörden wüssten nach zehn Jahren zwangsläufig, was jemand insgesamt besitzt. Jährliche Krypto-Bruttoflüsse ergeben weder einen sicheren Bestand noch Nettovermögen. Auch ungenaue Profile können jedoch für Prüfungsentscheidungen oder missbräuchliche Zielauswahl relevant sein.

**Anbieterbestände sind selbst ein zentraler Risikogegenstand.** Gesetzlich veranlasste Sammlung und längere Aufbewahrung halten sensible Informationen bei privaten Anbietern verfügbar. Reale Anbieter- und Dienstleisterleaks belegen, dass solche Bestände entwendet werden können. Die Behördenmeldung ersetzt sie nicht, sondern schafft zusätzliche Kopien und Möglichkeiten anbieterübergreifender Verknüpfung. Die Risiken aller Ebenen sind gemeinsam zu bewerten; rechtmäßige Speicherung ist nicht gleichbedeutend mit risikoloser Speicherung.

Der stärkste Ansatz verbindet drei Fragen: **Was lernt das System zusätzlich? Wie zuverlässig ist dieses Wissen? Ist dieselbe Verwaltungswirkung mit weniger Daten oder engeren Zugriffen erreichbar?** Das vorgeschlagene Gutachten soll diese Fragen messen, nicht eine vorgegebene Antwort bestätigen.

Für das konkrete Nutzerverfahren steht die **verweigerte Löschung tatsächlich gespeicherter Daten beim Anbieter von Kryptowerte-Dienstleistungen (CASP)** im Vordergrund, auch soweit diese nicht im Jahresbericht stehen. Anbieteraufzeichnungen und behördliche Mehrjahresbestände bilden zwei getrennte Untersuchungsstränge. Welche Speicherung angegriffen werden kann und welche unabhängigen Pflichten fortbestehen, muss feldbezogen bestimmt werden.

## 1. Nicht ein Datensatz, sondern mehrere Informationsschichten

Der Vermerk behandelt finanzielle Datenkonzentration allgemein. Das Krypto-Meldesystem dient als konkreter, gesetzlich bestimmbarer Untersuchungsfall. Die folgenden Schichten sind auseinanderzuhalten:

| Informationsschicht | Unmittelbare Aussage | Wesentliche Grenze |
|---|---|---|
| Kontosalden und Depotwerte | Bestand eines erfassten Kontos zu einem Stichtag | Nicht das gesamte Vermögen; Schulden und Zurechnung gesondert |
| Jahresflüsse | Umfang erfasster Käufe, Verkäufe und Transfers | Aktivität ist kein Bestand und kein Gewinn |
| Registerbeziehungen | Verbindung zu Konten, Gesellschaften oder Eigentumsrechten, je nach Register | Eine Beziehung liefert nicht immer einen Wert oder wirtschaftliches Eigentum |
| Anbieter-Einzelunterlagen | Je nach Dienst genaue Vorgänge, Zeitpunkte und Identitäts- oder Adressbezüge | Existenz, rechtmäßiger Zugriff und tatsächliche Nutzung müssen belegt sein |
| Öffentliche Blockchain | Sichtbare Konten, Ausgänge und Transaktionen | Person, Schlüsselkontrolle, Zweck und Eigentum fehlen zunächst |

Das ist keine rein hypothetische Unterscheidung: Das österreichische Gesetz zum gemeinsamen Meldestandard für Finanzkonten ([GMSG, § 3 Abs. 2 Z 3 und § 7](https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20009250)) erfasst unter anderem Jahresend-Kontosalden oder -werte und jährliche Meldungen. Dagegen enthält [§ 18 Krypto-MPfG](https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20013064&Paragraf=18) identitätsbezogene Jahresaggregate nach Kryptowert und Kategorie, aber keine einzelnen Wallet-Adressen, Transaktionskennungen, Zeitpunkte oder Gegenparteien. Nicht jedes Feld enthält eine Anzahl von Vorgängen. Das External-Address-Aggregat nach lit. i für Übertragungen an Adressen, die dem Anbieter nicht als mit einem Dienstleister für virtuelle Vermögenswerte oder Finanzinstitut verbunden bekannt sind, enthält nur Wert und Einheiten.

Auch die geplante europäische Kontenregister-Verknüpfung BARIS ist kein allgemeiner Saldenspeicher: [Art. 16 der Richtlinie 2024/1640](https://eur-lex.europa.eu/eli/dir/2024/1640/oj/eng) betrifft unter anderem Konto- und Inhaberbeziehungen; die Verbindung ist bis 10. Juli 2029 vorgesehen. Die [EU-Machbarkeitsstudie zum Vermögensregister](https://op.europa.eu/en/publication-detail/-/publication/050b047e-3ff5-11ef-865a-01aa75ed71a1/language-en) ist eine Studie, kein bereits beschlossenes Gesamtvermögensregister. Die [Kommissionsantwort E-001435/2024](https://www.europarl.europa.eu/RegData/questions/reponses_qe/2024/001435/P10_RE%282024%29001435_EN.pdf) grenzt dies ausdrücklich ab.

**Argument:** Der mögliche Eingriff liegt auch im Verbinden unterschiedlicher Schichten. Technische Verknüpfbarkeit ist dabei von gesetzlicher Zugriffsbefugnis und tatsächlich ausgeübter Zusammenführung zu unterscheiden. Ob Daten in einer zentralen Datenbank liegen oder über vernetzte Abfragen zusammenkommen, beantwortet diese Frage noch nicht.

## 2. Was jährlich hinzukommt - und was weiterhin fehlt

Eine identitätsbezogene Jahresmeldung ist keine einmalige Momentaufnahme, wenn weitere Jahrgänge gleichzeitig verfügbar bleiben. Es entsteht eine Zeitreihe. Schon ohne genaue Einzelvorgänge können wiederkehrende Aktivität, Veränderungen des Handelsumfangs, Anbieter- und Asset-Wechsel oder wiederkehrende Abflüsse erkennbar werden. Datenqualität, Identitätsabgleich und Abdeckung bestimmen, wie vollständig diese Reihe ist.

| Verfügbare Meldeperioden | Zusätzliche Aussage über beobachtete Aktivität | Keine automatische Folgerung |
|---|---|---|
| 1 | Asset-Arten, jährliche Bruttoflüsse, teilweise Anzahl | Aktueller Bestand oder Besitz der Zielwallet |
| 3 | Wiederholung, Veränderungen, Anbieterwechsel | Alle erworbenen Einheiten werden noch gehalten |
| 5 | Längerer Verlauf; Einordnung ungewöhnlicher Jahre | Aktivitätsrang entspricht Vermögensrang |
| 10 | Langfristiges Profil; mehr Anknüpfungspunkte für Abgleiche | Vollständiges oder genaues Gesamtvermögen |

Diese Perioden sind Untersuchungsszenarien, keine heute vorhandene zehnjährige Krypto-Meldereihe. Die ersten österreichischen Krypto-Jahresdaten betreffen 2026; der Anbieter meldet spätestens am [31. Juli 2027 (§ 19)](https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20013064&Paragraf=19), der Austausch folgt spätestens am [30. September 2027 (§ 21)](https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20013064&Paragraf=21).

**Bestand und Bewegung sind verschiedene Größen.** Dasselbe Kapital kann mehrmals gekauft, verkauft und wiederangelegt werden. Eigenüberträge können mehrfach auftauchen, ohne neues Vermögen zu schaffen. Eine Auszahlung kann weiteres Halten, Schenkung, Zahlung, Verkauf oder Verwahrung bei einem anderen Anbieter bedeuten. Anfangsbestände, nicht beobachtete Vorgänge und Verbindlichkeiten fehlen möglicherweise dauerhaft. Mehr Jahre beseitigen diese strukturellen Lücken nicht zwangsläufig.

### Rechenbeispiel: identische Meldungen, verschiedene Bestände

Rein synthetische Annahmen: Anfangsbestand null, keine Gebühren, jedes Jahr ein Kauf von 1 BTC für 60.000 Euro, danach Auszahlung von 1 BTC an eine Adresse, die den beschriebenen Wissenstest des Anbieters erfüllt. Für beide Personen fallen jährlich dieselben Aggregate an: Erwerb 60.000 Euro / 1 BTC / 1 Vorgang; allgemeiner ausgehender Transfer 60.000 Euro / 1 BTC / 1 Vorgang; zusätzlich External-Address-Aggregat 60.000 Euro / 1 BTC. Die beiden Transferfelder überlappen hier und dürfen nicht als zwei Abflüsse addiert werden.

Person A hält die ausgezahlten BTC. Person B verschenkt sie anschließend außerhalb des Anbieters. Ohne zusätzliche Daten ändert diese Folgehandlung die Jahresmeldung des Anbieters nicht.

| Nach Meldeperioden | Identische kumulierte Erwerbe | A hält | B hält |
|---|---|---|---|
| 1 | 1 BTC | 1 BTC | 0 BTC |
| 3 | 3 BTC | 3 BTC | 0 BTC |
| 5 | 5 BTC | 5 BTC | 0 BTC |
| 10 | 10 BTC | 10 BTC | 0 BTC |

Das zeigt eine logische Grenze, keine gemessene Häufigkeit: Selbst identische Zehnjahresmeldungen sind mit erheblich verschiedenen Beständen vereinbar. Ein statistischer Schätzer ist dadurch nicht ausgeschlossen, benötigt aber eine unabhängige Fehlerprüfung. Zweites Beispiel: Werden dieselben 10.000 Euro zwanzigmal eingesetzt und wieder erlöst, können 200.000 Euro Bruttoerwerbe und 200.000 Euro Bruttoveräußerungen entstehen. Die Summen zeigen nicht, wie viel Geld neu eingebracht wurde; im Beispiel waren es nur 10.000 Euro.

Der positive Informationsgehalt bleibt: Im ersten Beispiel sind wiederkehrende Käufe und Auszahlungen beim Anbieter verlässlich beobachtet. Auch ein Nettomodell aus dessen Meldungen kann die unterschiedlichen späteren Verfügungen außerhalb des Anbieters nicht zwingend auflösen. Im zweiten Beispiel ist die Differenz von Erwerb und Veräußerung null. Das Gutachten soll deshalb Bruttosummen und sachgerecht gebildete Nettogrößen vergleichen; die Beispiele widerlegen keinen validierten statistischen Schätzer.

**Argument:** „Vermögensregister light“ bezeichnet hier eine mögliche Profil- und Suchfunktion, nicht eine vollständige Bilanz. Ob sie bei einer bestimmten Stelle tatsächlich besteht, ist gesondert zu belegen. Zu prüfen ist auch, ob Personen nach vermutetem Vermögen auswählbar werden und mit welchen Fehlzuordnungen. Eine Aktivitätsrangfolge ist unmittelbar berechenbar; ihre Verlässlichkeit als Vermögensrangfolge ist damit nicht bewiesen.

## 3. Zehn Jahre sind weder ein einmaliger Bestand noch eine Universalfrist

Bei jährlicher Erhebung und gleichzeitiger Aufbewahrung wachsen zunächst mehrere Jahrgänge an. Eine jahrgangsbezogene Frist führt bei ordnungsgemäßer Löschung später zu einem rollenden Zeitfenster, nicht zu einer automatisch unbegrenzt wachsenden Sammlung. Ein neuer Jahrgang setzt die Frist älterer Jahrgänge nicht von selbst zurück. Andere selbständige Speichergrundlagen oder offene Verfahren sind getrennt zu prüfen.

| Datenhalter und Kopie | Regel beziehungsweise offene Feststellung |
|---|---|
| Anbieter: bereits übermittelte Krypto-Informationen | [§ 20 Abs. 4 Krypto-MPfG](https://www.ris.bka.gv.at/Dokumente/Bundesnormen/NOR40273819/NOR40273819.html): Löschung zehn Jahre nach Ende des Meldezeitraums |
| Anbieter: dokumentierte Melde- und Sorgfaltsschritte | [§ 39 Krypto-MPfG](https://www.ris.bka.gv.at/Dokumente/Bundesnormen/NOR40273838/NOR40273838.html): zehn Jahre ab Ende des jeweiligen Meldezeitraums, anschließend Löschung |
| Österreichische Ursprungskopie bei der Behörde | Die Anbieterfrist gilt nicht automatisch. Konkrete nationale Grundlage und Erforderlichkeit der Dauer erheben |
| Im automatischen Austausch erhaltene Informationen | [DAC8, Art. 2 Abs. 2](https://eur-lex.europa.eu/eli/dir/2023/2226/oj/eng), und [DAC9, Art. 2 Abs. 3](https://eur-lex.europa.eu/eli/dir/2025/872/oj/eng): Art. 22 Abs. 3 mit mindestens fünf Jahren ab Empfang, zugleich nicht länger als erforderlich; Anwendung der Umsetzungsmaßnahmen erst ab 1. Januar 2028 |
| Modelle, Arbeitskopien, Exporte und weitere Empfänger | Eigene Zwecke, Fristen, Zugriff und Löschwirkung nachweisen; keine pauschale Übertragung der Anbieterfrist |

Für das Jahr 2026 bedeutet die genannte Anbieterregel eine Frist bis zum Ablauf 2036 und anschließende Löschung. Das ist keine Aussage über die BMF-Kopie. [Art. 25 Abs. 5 DAC](https://eur-lex.europa.eu/eli/dir/2011/16/2026-01-01/eng) bindet die Aufbewahrung verarbeiteter Informationen an die erforderliche Dauer und nationale Verjährungsregeln. Für vor 2028 empfangene Kopien sind Übergang und nationale Grundlage gesondert zu klären; die neue EU-Mindestfrist darf nicht als bereits 2027 geltend vorausgesetzt werden.

§ 20 Abs. 4 formuliert einen Löschzeitpunkt; § 39 ausdrücklich eine Aufbewahrungspflicht für dokumentierte Schritte. Ob § 20 allein eine Ablehnung früherer Löschung trägt, darf nicht vorausgesetzt werden. Seine Auslegung, § 20 Abs. 1 und weitere Speichergründe sind zu prüfen. Die bloße Beseitigung eines Löschzeitpunkts könnte den Schutz sogar schwächen.

Andere Anbieterunterlagen folgen eigenen Regeln: [§ 21 Finanzmarkt-Geldwäschegesetz (FM-GwG)](https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20009769) verlangt erforderliche Identifizierungs- und Transaktionsunterlagen grundsätzlich zehn Jahre ab Ende der Geschäftsbeziehung beziehungsweise der gelegentlichen Transaktion. Bei langer Kundenbeziehung können Unterlagen wesentlich älter als zehn Jahre werden. [MiCA, Art. 68 Abs. 9](https://eur-lex.europa.eu/eli/reg/2023/1114/oj/eng), nennt grundsätzlich fünf, auf rechtzeitiges Verlangen der zuständigen Behörde bis sieben Jahre; die Geldtransferverordnung [TFR, Art. 26](https://eur-lex.europa.eu/eli/reg/2023/1113/oj/eng), grundsätzlich fünf Jahre mit eigener Verlängerungsregel. Frist und Gegenstand dürfen weder auf jede andere Kopie noch pauschal auf „jede Transaktionskennung (TXID) wegen DAC8“ übertragen werden.

Für spätere Verfahrenszeitpunkte ist die grundsätzlich ab 10. Juli 2027 anwendbare [Geldwäscheverordnung 2024/1624, Art. 77 und 90](https://eur-lex.europa.eu/eli/reg/2024/1624/oj/eng), einzubeziehen. Sie sieht eine fünfjährige Grundfrist und eine fallbezogene Verlängerung bis fünf Jahre vor und lässt selbständige, datenschutzkonforme Fristen anderer Zwecke unberührt. Übergang und Verhältnis zum österreichischen Recht sind gesondert zu bestimmen; die heutige FM-GwG-Frist darf nicht ungeprüft als unveränderte Dauer in die Zukunft fortgeschrieben werden.

Eine Datenübersicht muss deshalb auch abgeleitete Merkmale und Identitätszuordnungen erfassen. Das Löschen einer Ausgangsmeldung löscht eine daraus erzeugte Zuordnung oder ein gespeichertes Risikomerkmal nicht automatisch. Backups benötigen eine kontrollierte Ablauf- und Wiederherstellungsregel; eine Wiederherstellung darf abgelaufene Daten nicht wieder regulär verfügbar machen.

**Argument:** Der Prüfgegenstand ist der gesamte Lebenszyklus: Welche Personenjahre bleiben wo miteinander verbindbar, für welchen Zweck und wie lange? Auch eine gesetzliche Aufbewahrungsdauer beantwortet nicht, ob sämtliche Jahrgänge während der ganzen Zeit im normalen Analysezugriff stehen müssen.

## 4. Der besondere Informationsgewinn einer Blockchain-Zuordnung

Eine verlässliche Verbindung zwischen Person und öffentlicher Blockchain kann mehr erschließen als den ursprünglichen Bericht. Öffentliche Vorgänge sind auch außerhalb des meldenden Anbieters auswertbar. Neue Transaktionen oder neue verlässliche Empfängerlabels können ältere Vorgänge später verständlicher machen. Der Informationsgewinn kann somit wachsen, obwohl die ursprüngliche Meldung unverändert bleibt.

Es sind mindestens vier Beweisschritte zu trennen: **Person zu Ausgang oder Adresse; Adresse zu weiteren Vorgängen; Vorgang zu Empfänger oder Dienst; Muster zu einer persönlichen Schlussfolgerung.** Ein Kundenauftrag beweist nicht, dass der Kunde die Zieladresse kontrolliert. Ein Dienstlabel benennt nicht zwangsläufig einen Händler oder Kaufgegenstand. Ein passender Betrag allein beweist keine Identität.

Die jährlichen Meldeaggregate enthalten keinen solchen Adressanker. Für erfasste MiCA-Dienstleistungen können dagegen zusätzliche Anbieterunterlagen vorhanden sein: Die [Delegierte Verordnung 2025/1140, Tabellen 3 und 4](https://eur-lex.europa.eu/eli/reg_del/2025/1140/oj/eng) sieht unter anderem identifizierte Käufer-/Verkäuferdaten sowie Transaktionshashes, Wallet-Adressen und Zeitangaben vor; die interne Aufzeichnungsnummer verbindet die Tabellen. Welche Felder im konkreten Dienst entstehen und wer sie rechtmäßig erhalten darf, ist nachzuweisen. Dies ist kein routinemäßiger Bestandteil des Steuerjahresberichts.

Eine weitere mögliche Ankerquelle ist die TFR: [Art. 14 Abs. 5 und Art. 16 Abs. 2](https://eur-lex.europa.eu/eli/reg/2023/1113/oj/eng) verlangen bei erfassten Transfers über 1.000 Euro zu oder von selbstgehosteten Adressen geeignete Maßnahmen zur Prüfung von Eigentum oder Kontrolle. Ein tatsächlich vorhandener und valider Kontrollnachweis ist stärker als ein bloßer Auftrag. Er beweist aber nicht ohne Weiteres heutige Kontrolle oder wirtschaftliches Eigentum an allen verbundenen Werten. Methode, Zeitpunkt, Datensatz, Speichergrund und Empfänger sind gesondert zu erfassen; die Zweckbindung erlaubt keine automatische steuerliche Wiederverwendung.

| Technik | Erkenntnis nach verlässlichem Identitätsanker | Verbleibende Grenze |
|---|---|---|
| Wiederverwendetes Ethereum-Konto | Öffentliche Historie und nativer Kontostand; Tokenstände über den jeweiligen Contract | Nicht alle anderen Adressen, Verbindlichkeiten oder wirtschaftliches Eigentum |
| Bitcoin-Adresse oder bekannter Ausgang | Konkrete Vorgänge; weitere Verbindungen durch geprüfte Heuristiken möglich | Eine Adresse ist keine vollständige Wallet. CoinJoin, PayJoin, Sammelauszahlungen oder gemeinsame Wallets können Zuordnungen verfälschen |
| Lightning | Kanalfinanzierung und -schließung können on-chain sichtbar sein; Netzwerkbeobachtung kann mehr zeigen | Geroutete Einzelzahlungen stehen nicht im öffentlichen Ledger; nicht jede Finanzierung ist als Kanal erkennbar |
| Bridges und DeFi | Sichtbare Positionen und Bewegungen über Contracts | Repräsentationen derselben Position nicht doppelt zählen; Sicherheiten und Verbindlichkeiten bei der Nettobewertung getrennt berücksichtigen |

Die Mechanismen sind durch [Ethereum-Dokumentation](https://ethereum.org/developers/docs/accounts/), [ERC-20](https://eips.ethereum.org/EIPS/eip-20), [Bitcoin-Forschung](https://www.usenix.org/conference/usenixsecurity22/presentation/kappos), [Lightning-Forschung](https://arxiv.org/pdf/2003.12470) und [Bridge-Dokumentation](https://ethereum.org/developers/docs/bridges/) konkret untersuchbar. Diese Quellen liefern keine Erfolgsquote für die Zuordnung allein aus jährlichen Kryptoaggregaten. Auch Studien zum Matching von [Webkäufen und Bitcoin-Transaktionen](https://petsymposium.org/popets/2018/popets-2018-0038.php) verwenden zusätzlichen Kauf- und Zeitkontext, der einer Jahresmeldung fehlt.

**Argument:** Ein gespeicherter Identitätsanker kann eine langfristige Erweiterung des Personenwissens ermöglichen. Reichweite und Zuverlässigkeit müssen für jede weitere Zuordnung belegt werden. Sensible Schlussfolgerungen erfordern besonders konkrete Daten: Eine vermeintliche Apothekenzahlung beweist keine Krankheit; Jahresaggregate enthalten schon den Händlerbezug nicht. Auch eine falsche sensible Zuschreibung kann relevant sein. Ob Art. 9 DSGVO greift, richtet sich nach den Informationen, welche die konkrete Verarbeitung offenzulegen erlaubt, nicht erst nach einer bewiesenen Krankheit ([C-252/21, Rn. 68-73](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:62021CJ0252)). Nicht alle Finanzdaten fallen automatisch darunter.

## 5. Datenkonzentration verändert Sicherheits- und Missbrauchsrisiken

Ein verknüpfbarer Bestand kann bei unbefugtem Zugriff mehr über eine Person offenlegen als eine einzelne Meldung. Relevante Wege sind externe Angriffe, gestohlene berechtigte Kennungen, zweckwidrige interne Abfragen, zu breite Exporte und unzureichend abgeschottete Dienstleister. Nicht nur die Wahrscheinlichkeit eines Zugriffs ist zu bewerten, sondern auch die je Zugriffsweg erreichbare Datenmenge und die möglichen Folgen.

### Anbieterbestände als attraktive Angriffsziele

Die privaten Anbieterbestände sind keine bloße Vorstufe des Behördenrisikos. **Sie bilden eigene attraktive Datensammlungen - hier als „Honeypots“ bezeichnet.** Wer Identität, Wohnadresse, finanzielle Aktivität und gegebenenfalls Blockchain-Anker gemeinsam erhält, kann daraus auch ohne private Schlüssel ein Zielprofil bilden. Aufbewahrungspflichten begrenzen die Möglichkeit, diesen Bestand auf Wunsch des Betroffenen zu entfernen. Welche Daten dadurch zusätzlich oder länger verfügbar bleiben, ist konkret zu ermitteln; bestehende Geschäfts- und sonstige Speicherzwecke sind im Vergleich mitzuberücksichtigen.

[§ 20 Abs. 1 Krypto-MPfG](https://www.ris.bka.gv.at/Dokumente/Bundesnormen/NOR40273819/NOR40273819.html) verlangt in Österreich die Ermittlung, Erfassung, Speicherung und Verarbeitung der meldepflichtigen Informationen für alle Kunden hinsichtlich aller Transaktionen und Kryptowerte, unabhängig von der Meldepflicht des einzelnen Nutzers. Hinzu kommen die in Abschnitt 3 getrennt beschriebenen Dokumentations- und Aufbewahrungspflichten. Es geht daher nicht nur um freiwilliges Datenhorten. Die Reichweite der gesetzlich veranlassten Bestände und der damit verbundenen Exposition gehört selbst in die Verhältnismäßigkeitsprüfung.

**Die Möglichkeit einer Entwendung ist durch konkrete Vorfälle belegt:** [Coinbase, SEC-Mitteilung 2025](https://www.sec.gov/Archives/edgar/data/1679788/000167978825000094/coin-20250514.htm), berichtet über bezahlte Personen mit berechtigten Supportzugängen und entwendete Kundeninformationen einschließlich Identitäts- und Adressdaten, Salden-Schnappschüssen und Transaktionshistorie. Der [Anbieterbericht vom 15. Mai 2025](https://www.coinbase.com/blog/protecting-our-customers-standing-up-to-extortionists) bestätigt, dass Kunden anschließend zur Übertragung von Geld verleitet wurden. Keine privaten Schlüssel oder direkter Zugriff auf Kundengeld waren nötig, um diesen Betrugsweg zu eröffnen.

Beim ausgelagerten Insolvenz-Dienstleister [Kroll, Mitteilung an FTX-Gläubiger 2023](https://ftxquestions.kroll.com/docs/Kroll_Notice_to_FTX_Claimants_4879-3276-7625-2.pdf), eröffnete die Übernahme einer Mitarbeiter-Telefonnummer den Zugriff auf Cloud-Dateien. Betroffen sein konnten Identität, Wohnadresse, Forderungsdaten und Kryptobestände. FTX-Systeme und Vermögenswerte waren davon nicht unmittelbar betroffen. Der Fall zeigt ein weiteres Datenkonzentrationsrisiko bei einem Dienstleister für mehrere Kryptounternehmen, nicht eine DAC8-Datenbank.

Auch der Identifizierungsdienstleister [Fractal ID, eigener Bericht vom 16. Mai 2025](https://web.fractal.id/a-better-way-is-possible-dataless-kyc-and-open-sourcing-fractal-id/), bestätigt seinen Leak von Juli 2024 und bezeichnet AML- und Vertragspflichten als Gründe fortbestehender Speicherung von Kundendaten. Die beschriebenen gespeicherten Datenarten schließen Identitätsdokumente, Wohn- und bei der Verifikation bereitgestellte Wallet-Adressen ein. Das ist eine Anbieteraussage, keine unabhängige Feststellung zur Rechtmäßigkeit oder zum Erfolg seines angekündigten neuen Speicherkonzepts.

### Das Meldesystem kommt hinzu und ersetzt die Anbieterbestände nicht

DAC8 betrifft nicht nur einen einzelnen Anbieter, sondern die jeweils berichtspflichtigen Anbieter im geregelten Anwendungsbereich. Meldungen mehrerer Anbieter können bei den zuständigen Stellen über Identifikatoren derselben Person zusammenführbar werden. Daraus kann ein breiterer Ausschnitt entstehen als aus einem einzelnen Anbieterbestand. Der Austausch schafft weitere Empfängerkopien. Er ist jedoch keine voraussetzungslose Weltdatenbank aller Anbieter oder sämtlicher Rohdaten; Zuständigkeit, Meldeumfang und Zugriff sind gesondert nachzuweisen.

| Risikoschicht | Zusätzliche Exposition | Konkrete Prüfgröße |
|---|---|---|
| Anbieter und Pflichtarchiv | Personenbezogene Daten bleiben über den laufenden Vorgang hinaus vorhanden | Zusätzliche Felder und Jahre; Zugang von Support, Betrieb und Administration |
| Gemeinsame Dienstleister | Ein Zugangsweg kann Daten aus mehreren Kundenunternehmen erreichen | Mandantentrennung, Reichweite einer Kennung, tatsächlich bereitgestellte Daten |
| Meldung, Austausch und Zusammenführung | Weitere Kopien; mögliche Verknüpfung mehrerer Anbieter und Jahre | Empfänger, Identitätsabgleich, Exportumfang und erreichbare Personenjahre |

Die Aufbewahrung kann einen Datenbestand auch dann als Angriffs- und Missbrauchsmaterial verfügbar halten, wenn sie gesetzlich vorgeschrieben ist. Ein aktuelles Behördenaudit beantwortet nicht die Sicherheit jedes beteiligten CASP oder Dienstleisters. Umgekehrt beseitigt bessere Anbietersicherheit nicht das Risiko weiterer Empfängerkopien. Gemeinsame Dienstleister und Kennungen können Risiken verbinden; eine statistische Unabhängigkeit der einzelnen Lecks darf nicht unterstellt werden.

**Argument:** Die gesetzgeberische Abwägung muss auch die veranlasste Exposition bei privaten Stellen erfassen. Bestehende AML-, MiCA- oder TFR-Pflichten lassen das Risiko nicht verschwinden; sie bestimmen, welche Abhilfe an welcher Pflicht ansetzen muss. Zu prüfen ist die Gesamtkette und der zusätzliche Beitrag jeder Regel. Ein Erfolg gegen nur eine Pflicht kann unvollständig sein, ohne dass die verbleibende Gefährdung dadurch kleiner wäre.

### Behördenmissbrauch und mögliche Folgen

Für Österreich gibt es konkrete historische Insider-Evidenz: Eine [BMF-Disziplinarentscheidung von 2019, S. 1 und 6-7](https://www.ris.bka.gv.at/Dokumente/Dok/DKT_BMF_20191009_02_084_18_DK_17_00/DKT_BMF_20191009_02_084_18_DK_17_00.pdf) dokumentiert jahrelange private Abfragen im Abgabeninformationssystem (AIS) auf Angehörige, eine anlassbezogene Logauswertung und weitere Abfragen nach der Anzeige. Sie belegt zugleich Warnungen und Überwachung. Protokolle ermöglichten die Rekonstruktion, verhinderten aber nicht jeden Missbrauch. Das beweist keine heutige DAC8-Lücke, Weitergabe oder körperlichen Folgeschaden.

Amtliche französische Vorfälle zeigen weitere reale Wege: Die [DGFiP-Mitteilung vom August 2026](https://presse.economie.gouv.fr/acces-illegitime-au-systeme-dinformation-de-la-direction-generale-des-finances-publiques/) nennt missbrauchte Kennungen und entwendete Steuer- und Katasterdaten. Beim [FICOBA-Vorfall vom Februar 2026](https://www.impots.gouv.fr/actualite/acces-illegitimes-au-fichier-national-des-comptes-bancaires-ficoba) waren Identitäts-, Adress- und Kontokennungsdaten betroffen; die [amtliche FAQ](https://www.impots.gouv.fr/sites/default/files/media/2_actu/home/2026/faq_ficoba.pdf) schließt Salden und Transaktionen aus. Das sind Behördenvorfälle, aber weder österreichische noch DAC8-spezifische Nachweise.

Die [französische Gendarmerie vom 13. September 2026](https://www.gendarmerie.interieur.gouv.fr/gendinfo/terrain/immersion/2026/la-strategie-de-la-gendarmerie-face-aux-cryptorapts-partie-2-2) beschreibt die Nutzung geleakter Waltio-E-Mail-Adressen zur kriminellen Zielauswahl, teilweise mit falscher Vorstellung über Bestände. Das ist eine amtliche operative Einschätzung, kein fallbezogenes gerichtliches Kausalurteil und kein Beleg „DAC8 verursacht Entführungen“. Sie zeigt aber, weshalb Zielauswahl aus Anbieterdaten nicht als bloß abstrakte Sorge behandelt werden sollte.

Körperliche Folgen von Informationsmissbrauch sind nicht auf Krypto beschränkt. Im Fall Amy Boyer beschreibt ein [US-Bundesgerichtsbeschluss, 2002 DNH 080, S. 1-3](https://www.nhd.uscourts.gov/sites/default/files/Opinions/02/02NH080.pdf), den Verkauf durch Vorwand beschaffter Arbeitsortinformationen an den späteren Mörder und die Tötung am Arbeitsplatz. Der Beschluss weist den geltend gemachten FCRA-Anspruch ab; er stellt nicht abschließend die Haftung für den Tod fest. Solche Fälle stützen den Mechanismus der Lokalisierung, keine österreichische Eintrittsquote. Für die vorausschauende Risikoprüfung muss nicht erst ein tödlicher DAC8-Vorfall vorliegen; Schadenersatz und Eilrechtsschutz haben eigene Voraussetzungen.

Bei selbstverwahrten Kryptowerten kann eine erzwungene, bestätigte Übertragung ohne rückbuchende Zentralstelle besonders schwer rückgängig zu machen sein. Ermittlungen, Empfängersperren bei Intermediären und fallweise Rückgewinnung bleiben möglich. Personenbezogene Daten allein erlauben keine Verfügung über private Schlüssel. Der relevante Risikomechanismus ist unter anderem Zielauswahl und Social Engineering, nicht eine automatische Entwendung durch Kenntnis des Vermögens.

**Gegenbefunde gehören dazu:** Der [Rechnungshof, Bund 2024/16, S. 14 und 79-82](https://www.rechnungshof.gv.at/rh/home/home/2024_16_IT-Sicherheit_BM.pdf) beschreibt eine starke BMF-Kontrollumgebung im überwiegend 2018-2022 untersuchten Zeitraum; keine Prüfung der späteren Kryptomeldearchitektur, Dienstleistermanagement außerhalb des Umfangs. Die [OECD-CDS-Prüfmaßstäbe, Rn. 9-16](https://www.oecd.org/content/dam/oecd/en/networks/global-forum-tax-transparency/confidentiality-data-safeguards-assessments-tor.pdf) verlangen Zugriffsbeschränkung, Lebenszyklusverwaltung, Überwachung und Audit. Fehlende öffentliche Detailberichte beweisen keine fehlenden Kontrollen. Nach [EuGH C-340/21, Rn. 39 und 42-52](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:62021CJ0340) beweist ein Leck allein auch keine unzureichenden Sicherheitsmaßnahmen.

Dieselbe Entscheidung weist dem Verantwortlichen den Nachweis angemessener Maßnahmen zu (Rn. 52-57). Eine begründete, nachgewiesene Angst vor künftigem Missbrauch kann unter den Voraussetzungen des Art. 82 DSGVO einen immateriellen Schaden darstellen (Rn. 77 und 84-86). Diese individuelle Schadensprüfung ist von vorbeugender Architektur- und Risikoprüfung zu trennen.

**Argument:** Zu untersuchen sind konkrete Zugriffsketten und zusätzliche Folgen der Kombination. Vorfälle belegen mögliche Mechanismen, nicht die österreichische Eintrittswahrscheinlichkeit. Ein fehlerhaftes Vermögensprofil kann selbst ein Risiko erzeugen, wenn es eine Person zu Unrecht als lohnendes Ziel erscheinen lässt.

## 6. Automatisierte Auswertung und Zweckausweitung

Die technische Möglichkeit einer Datenverknüpfung ist nicht gleichbedeutend mit ihrer heutigen Verwendung. Das BMF berichtet für 2024 über [6,6 Millionen vom Predictive Analytics Competence Center (PACC) mit Risikomodellen überprüfte Fälle](https://www.bmf.gv.at/presse/pressemeldungen/2025/august/pacc-ki.html). Die [parlamentarische Antwort 2592/AB, S. 3-4](https://www.parlament.gv.at/dokument/XXVIII/AB/2592/imfname_1710768.pdf) nennt unter anderem Machine Learning und Netzwerkanalyse. Sie belegt nicht, dass konkrete Finanzkontenmeldungen nach dem gemeinsamen Meldestandard (CRS) oder Kryptomeldungen bereits Modellinputs sind. Laut BMF erfolgen zusätzliche Steuerfestsetzungen durch Prüforgane, nicht allein durch ein Modell.

[§ 114 Abs. 4 BAO](https://ris.bka.gv.at/eli/bgbl/1961/194/P114/NOR40202626) erlaubt Verarbeitung für automatisiertes Risikomanagement und Betrugsbekämpfung nur soweit geeignet, erforderlich und angemessen. Ein Gutachten sollte deshalb nicht nur endgültige Steuerentscheidungen, sondern auch Verdachtsauswahl, Nachfragen und deren Fehlerfolgen untersuchen: Ein Mensch am Ende des Ablaufs korrigiert einen systematischen Fehler nicht zwangsläufig.

Bei ausgetauschten Informationen ist außerdem der gesetzlich vorgesehene Zweckrahmen zu bestimmen. [Art. 16 DAC](https://eur-lex.europa.eu/eli/dir/2011/16/2026-01-01/eng) eröffnet neben Steuerzwecken weitere bestimmte Verwendungen, unter anderem Geldwäsche- und Terrorismusfinanzierungsbekämpfung (AML/CFT) und Unionssanktionen. Daraus folgt kein unbeschränkter Zugriff auf alle Daten, keine automatische Nutzung in jedem Modell und keine gleiche Befugnis für jede Ursprungskopie.

**Argument:** Für jede Nutzung sind Datenquellen, Verknüpfungsregeln, Zweck, zuständige Stelle, menschliche Kontrolle und mögliche Konsequenzen offenzulegen oder unabhängig prüfbar zu machen. Die Untersuchung muss behauptete Nutzung und bloße technische Möglichkeit getrennt ausweisen.

## 7. Verhältnismäßigkeit und Vorratscharakter: was das Gutachten tragen kann

Wiederkehrende, verdachtsunabhängige Erhebung und längere Verfügbarkeit können einen **Vorratscharakter** haben: Daten über rechtmäßiges Verhalten werden vor einem konkreten Untersuchungsanlass verfügbar gehalten. Das ist eine Beschreibung des Designs, keine automatische Gleichsetzung mit Telekommunikations-Vorratsdatenspeicherung und kein Urteil über Rechtswidrigkeit.

Die rechtliche Abwägung unter [Art. 7, 8 und 52 Abs. 1 GRC](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:12016P/TXT) sowie den einschlägigen [DSGVO-Grundsätzen](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng) benötigt einen konkreten Datensatz und Zweck. [C-175/20, Rn. 63-84](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:62020CJ0175) betrifft Grenzen steuerbehördlicher Anforderungen, entscheidet aber kein automatisches EU-Meldesystem. Das technische Gutachten liefert Tatsachen für diese Abwägung; die rechtliche Schlussentscheidung bleibt beim Gericht.

Die Gegenposition ist ernst zu nehmen: Steuerkontrolle ist ein legitimer Zweck; komplexe Anbieterwechsel und grenzüberschreitende Vorgänge können einheitliche Meldungen rechtfertigen. Die [DAC8-Folgenabschätzung SWD(2022) 401](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=SWD:2022:401:FIN) verglich Salden-, Aggregat- und Einzeltransaktionsmodelle und wählte ein Zwischenmodell. Der [VfGH, E 2097/2021](https://www.ris.bka.gv.at/Dokumente/Vfgh/JFT_20230309_21E02097_00/JFT_20230309_21E02097_00.pdf), akzeptierte im damaligen DAC2-Fall Konto-, Saldo- beziehungsweise Wert- und Zinsdaten; abstrakte Sicherheitsbedenken begründeten keine ernstlichen Gültigkeitszweifel. Der [EuGH, C-623/22, Rn. 143-149](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:62022CJ0623), akzeptierte das geprüfte DAC6-Informationspaket. Eine gesondert veröffentlichte Wirksamkeitsstudie für jedes einzelne Feld ist keine allgemeine rechtliche Voraussetzung.

Ergänzende Vergleichsmaßstäbe bieten [C-817/19 zu Fluggastdaten](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:62019CJ0817) für gestufte Speicherung und kontrollierte Auswertung sowie [C-37/20 und C-601/20](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:62020CJ0037) für Registerzugriff. Die Unterschiede sind entscheidend: Fluggastdaten und allgemeiner öffentlicher Registerzugang sind keine vertraulichen Steuerjahresmeldungen. Die Ergebnisse können nicht unverändert übernommen werden.

Aktuelle fachliche Unterstützung für konkrete Schutzfragen bietet die [EDPS-Stellungnahme 20/2026, Rn. 54-58, gedruckte S. 16-17](https://data.consilium.europa.eu/doc/document/ST-12521-2026-INIT/en/pdf). Sie empfiehlt für den vorgeschlagenen DAC-Recast unter anderem zweckgebundenen, kontrollierten Registerzugriff sowie eine periodische Prüfung der weiteren Erforderlichkeit der Speicherung. Es handelt sich um eine beratende Stellungnahme zu einem Vorschlag, nicht um geltendes neues Recht oder eine Ungültigkeitsentscheidung zu DAC8.

**Verwendbarer Argumentationskern:** Die Begründung der Erhebung und fortgesetzten Speicherung beim Anbieter oder bei der Behörde muss der tatsächlich möglichen Zusammenführung Rechnung tragen. Mehrjährige Profile, weitere Identitätsanker, Fehlzuordnungen und Zugriffsmöglichkeiten können den Eingriff über den Inhalt einer einzelnen Meldung hinaus verstärken. Das allein widerlegt den steuerlichen Nutzen nicht. Es verlangt einen konkreten Vergleich von Nutzen, zusätzlichem Personenwissen und Schutzmöglichkeiten. Ein nachgewiesen gleich wirksames, weniger eingriffsintensives Konzept wäre stärker als der bloße Hinweis auf ein denkbares Datenleck.

## 8. Der konkrete Verfahrensansatz: verweigerte Löschung beim CASP

Für ein Nutzerverfahren beginnt die Prüfung nicht erst bei der jährlichen Übermittlung. Ausgangspunkt kann ein tatsächlich gespeicherter Datenbestand sein, dessen Löschung der Betroffene verlangt und der CASP unter Hinweis auf gesetzliche Pflichten ablehnt. [Art. 17 Abs. 3 lit. b DSGVO](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng) nimmt eine erforderliche Verarbeitung zur Erfüllung einer rechtlichen Verpflichtung vom Löschungsrecht aus. Die entscheidenden Fragen sind daher: **Verlangt die bezeichnete Norm gerade diese Daten weiterhin? Und ist die einschlägige Pflicht selbst grundrechtskonform?**

Das Gutachten sollte die tatsächlich gespeicherten Identitäts-, Adress- und Transaktionsverknüpfungen sowie daraus erschließbare Zahlungsbeziehungen untersuchen. Für jedes Feld ist zu prüfen, ob die vom CASP genannte Norm gerade dieses Feld erfasst. § 20 Abs. 4 und § 39 Krypto-MPfG benennen übermittelte Informationen und dokumentierte Melde- und Sorgfaltsschritte, nicht pauschal alle Adress- und Transaktionsbezüge. Die Begründung des CASP darf nicht ungeprüft als richtige rechtliche Einordnung übernommen werden.

Vorab ist zu klären, ob die weitere Speicherung zusätzlich auf FM-GwG, MiCA, TFR oder eine andere Grundlage gestützt werden kann. Ein Erfolg gegen die steuerliche Pflicht entfernt einen unabhängig gerechtfertigten Anker nicht automatisch. Die Feld-für-Feld-Matrix sollte enthalten: Datenfeld, tatsächliche Speicherung, genannte Norm, Normebene (EU-Verordnung, Richtlinienvorgabe oder nationaler Spielraum), weitere Speichergrundlagen, Fristbeginn, Löschdatum und verbleibender Informationsgewinn nach der beantragten Maßnahme. Damit lässt sich zeigen, welche Daten eine engere Regel tatsächlich entfernen oder abschotten würde. Über die Ungültigkeit entscheidungserheblicher EU-Normen entscheidet der EuGH, nicht der CASP oder ein nationales Gericht selbst ([Foto-Frost, C-314/85](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:61985CJ0314)).

**Argument:** Angegriffen wird die nachgewiesene fortgesetzte Speicherung oder Nutzung eines konkreten Bestands und gegebenenfalls die dafür maßgebliche gesetzliche Pflicht, nicht abstrakt „jede Kryptodatenverarbeitung“. Das technisch mögliche Profil und die beantragte Abhilfe müssen auf genau diesen Bestand bezogen werden. Das Gutachten ersetzt weder die Prüfung der im Verfahren maßgeblichen Normen noch die Begründung ihrer Entscheidungserheblichkeit.

## 9. Weniger eingriffsintensive Konzepte im Vergleich

Besonders naheliegend ist zunächst ein Vergleich mit unveränderten erforderlichen Feldern, aber engerer alltäglicher Verfügbarkeit. Dadurch bleibt das Informationsangebot für berechtigte Prüfungen grundsätzlich erhalten. Ob Zugriffsbarrieren tatsächlich gleich wirksam sind, muss dennoch gemessen werden. Änderungen vorgeschriebener Felder oder Fristen können eine Rechtsänderung verlangen; ein Datenhalter darf sie nicht eigenmächtig vornehmen.

Für den Löschungsansatz ist je Konzept anzugeben, ob es den konkreten CASP-Bestand betrifft und ob es ohne Rechtsänderung umsetzbar wäre. Eine bloße Begrenzung behördlicher Zugriffe ersetzt keine Änderung der beanstandeten Anbieterspeicherung.

| Vergleichskonzept | Mögliche Eingriffsminderung | Gegenargument und Messfrage |
|---|---|---|
| Kurze aktive Nutzung; ältere Daten in getrenntem Archiv mit begründeter Freigabe | Weniger Personenjahre im Routinezugriff | Aufwand und Verzögerung; welche Fälle gehen verloren oder werden später entdeckt? |
| Getrennte Identitäts- und Aktivitätsbereiche mit kontrollierter Verknüpfung | Weniger Rollen können vollständige Klartextprofile bilden | Pseudonyme bleiben personenbezogen; wie viel erschließt ein einzelner kompromittierter Zugang? |
| Beim CASP: getrenntes Pflichtarchiv, zweckgebundene Freigabe und feldweise Löschung bei Fristablauf | Weniger Anbieter- und Supportrollen erreichen alte Zuordnungen im normalen Betrieb | Vorgeschriebene Verfügbarkeit muss erhalten bleiben; Zweck, Norm und erreichbare Daten je Rolle vergleichen |
| Fallbezogene, zeitlich begrenzte Rechte; Vieraugenfreigabe für Massenexport | Erschwert zweckwidriges Browsen und Bulkentwendung | Verwaltungsaufwand und Zusammenwirken; Erkennungszeit und blockierte berechtigte Prüfungen messen |
| Engerer Routinebericht; Details bei objektiver Unstimmigkeit | Weniger Detail- und Transferwissen ohne konkreten Anlass | Neue Verdachtsfälle könnten unsichtbar werden; Trefferverlust und Nachfragen vergleichen |
| Kürzere Dauer mit begründetem Fortbestand für konkrete Verfahren | Weniger alte Kopien | Langfristige Prüfungen; Zusatznutzen jedes alten Jahrgangs und verlorene Beweise messen |
| Abfragen beim Datenhalter statt zentraler Vollkopie | Weniger zentrale Datenexposition | Anbieter-Ausfall, internationale Koordination, Verfügbarkeit; Risiko kann nur verlagert werden |
| Vorschau und nachprüfbare Berichtigung bis zu Empfängern und abgeleiteten Merkmalen | Weniger fortgeschriebene falsche Profile | Kein Vetorecht; Aufwand, Korrekturlatenz und verbliebene Fehler prüfen |

Noch nicht nachgewiesen ist ein vergleichbarer Gesamtnutzen dieser Konzepte. Ein sinnvoller Test erfasst gemeinsam: steuerlich oder administrativ brauchbare Treffer, falsche Verdachtsfälle, Nachfragen und Kosten sowie zusätzliches Personenwissen und erreichbare Datenmenge. Zugriffsrecht, technische Abschottung, Protokollierung und tatsächlich getestete Kontrolle sind unterschiedliche Nachweise. Ein bloß vorhandenes Log ist keine laufende Missbrauchserkennung.

## 10. Auftrag für ein unabhängiges technisches Gutachten

Der separate **„Technische Gutachtenauftrag zu Finanzdatenprofilen“** ist als ergebnisoffener Auftrag formuliert, nicht als Fortsetzung der Argumentation. Er prüft Zusatznutzen, Fehlzuordnungen, Sicherheitswege und Alternativen. Auch kein messbarer Informationszuwachs oder ein Ergebnis zugunsten des bestehenden Designs ist auszuweisen.

Die Anbieterprüfung beginnt bei den tatsächlich gespeicherten Daten und der Löschungsablehnung. Die Behördenprüfung beginnt bei den vorgesehenen Meldungen, zulässigen Zusammenführungen und überprüfbaren Kontrollen. Der allgemeinere Behördenbefund ist nicht automatisch für jede im CASP-Verfahren beanstandete Norm entscheidungserheblich.

Das Prüfprogramm umfasst fünf Aufgaben:

1. **Felder und Lebenszyklus:** Daten, Kopien, Identitätsbezüge, Zwecke, Fristen und Zugriffsrollen je Halter feststellen.
2. **Mehrjahresprofile:** Brutto- und sachgerechte Nettogrößen gegen bekannte Bestände prüfen; Eigenüberträge, Wiederanlage, Anfangsbestände und Schulden berücksichtigen.
3. **Blockchain-Zuordnung:** Jahresfelder und zusätzliche Anker stufenweise vergleichen; Transaktion, Adresse, Person, Kontrolle und Eigentum getrennt bewerten.
4. **Sicherheit:** Berechtigte Prüfung, Insiderabfrage, gestohlene Kennung, Massenexport und Dienstleisterzugriff mit ihren tatsächlichen Reichweiten untersuchen.
5. **Alternativen:** Dieselben Verwaltungsziele und Testfälle vergleichen; Nutzenverlust, Verzögerung, Kosten und bloße Risikoverlagerung ausdrücklich messen.

Bei Zuordnungen gehören Bezugsgröße, Kandidatenmenge, Nichtentscheidungen, Abdeckung und Unsicherheitsintervalle zum Ergebnis. Rein synthetisches Beispiel: Unter 100.000 Kandidaten bestehen nur 100 echte Verbindungen. Ein Verfahren findet 99 davon. Wenn es bei 0,1 Prozent der 99.900 Nichtverbindungen fälschlich anschlägt, entstehen rund 100 falsche Treffer. Damit ist nur etwa die Hälfte aller gemeldeten Treffer richtig. Das zeigt den Einfluss seltener echter Verbindungen, keine Fehlerquote eines konkreten Produkts.

**Zugang begrenzt den Befund:** Öffentliche und kontrollierte Testdaten zeigen Mechanismen und logische Grenzen. Reale Behördenwirkung oder Bevölkerungs-Fehlerquoten erfordern geeignete, rechtmäßig bereitgestellte Daten und bekannte Vergleichswerte. Fehlender Zugang beweist keine fehlenden Kontrollen.

Vorab festgelegte Zielgrößen, dokumentierter Code und Datenstand, Negativkontrollen sowie ein unabhängiger Wiederholungslauf sichern die Nachprüfbarkeit. Realdaten sind zu minimieren; öffentliche Fassungen enthalten keine nutzbaren Identitäts-Adress-Verbindungen. Hashen allein anonymisiert öffentliche Adressen nicht. Keine fremden Personen zu Demonstrationszwecken deanonymisieren.

Ergebnis sollen eine verständliche Zusammenfassung, eine Aussage-Evidenz-Grenzen-Matrix, Feld- und Fristenplan, dokumentierte Tests und ein Alternativenvergleich sein. Dieser Vermerk liefert dafür Hypothesen und Quellen, nicht bereits die unabhängigen empirischen Ergebnisse.

## 11. Welche Nachweise noch benötigt werden

Der nächste Erkenntnisschritt liegt vor allem in konkreten Unterlagen, nicht in weiteren allgemeinen Leak-Beispielen: Datenkopie und Löschungsantwort des CASP; tatsächliche Feld- und Rollenmatrix; Export- und Verknüpfungskonzept; Behördenfristen; Prüfumfang und Erledigungsstand bestehender Audits; Löschtests einschließlich Backups und abgeleiteter Merkmale; tatsächliche Analyseinputs und Korrekturwege.

Beweiswege sind zu trennen: [Art. 15 DSGVO](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng) betrifft eigene Daten und deren Verarbeitung, das [IFG](https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20012537) vorhandene Behördenaufzeichnungen mit Geheimhaltungs- und Teilzugangsgrenzen, die Aufsicht nach Art. 58 DSGVO und [§ 22 DSG](https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10001597&Artikel=2&Paragraf=22) notwendige, gegebenenfalls vertraulich geprüfte Nachweise. Daraus folgt kein unbegrenzter Anspruch auf institutionelle Sicherheitsunterlagen oder jede gewünschte Untersuchung.

Eine Datenschutz-Folgenabschätzung ist je konkreter Verarbeitung und möglicher Ausnahme zu prüfen. Die österreichische [DSFA-AV, Kategorie A17](https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20010206), enthält eine Ausnahme für bestimmte öffentliche Abgabenverarbeitungen. Ein nicht gefundenes Dokument beweist daher weder eine unterlassene Pflicht noch einen Sicherheitsmangel. Erforderlich sind entweder einschlägige Bewertung oder nachvollziehbare Ausnahmeprüfung; die materiellen Datenschutz- und Sicherheitsanforderungen bleiben maßgeblich.

### Befundstatus und Arbeitsgrundlage

**Belegt:** unterschiedliche Datenebenen und bezeichnete gesetzliche Anbieterfristen; mathematische Grenzen von Bruttoflüssen; technische Ankermechanismen und normativ vorgesehene Anbieterfelder; einzelne Missbrauchsfälle und dokumentierte Schutzvorkehrungen. **Durch konkrete Unterlagen zu belegen:** tatsächliche CASP-Felder, Löschungsablehnung, Behördenfristen und aktuelle Rollen. **Noch zu messen:** Vermögensschätzungs- und Matchinggüte, zusätzlicher Informationsgewinn sowie vergleichbare Effektivität der Alternativen. Ein tatsächlicher österreichischer DAC8-Missbrauch ist damit nicht nachgewiesen.

Arbeitsgrundlage sind das LLM Wiki (Versionsstand `d17892b21667f778fc8d035e3f1577858791f1a3`) und die verlinkten Primärquellen. Die Rechenbeispiele lassen sich mit `finanzdatenprofile-beispiele.py` reproduzieren; sie sind keine empirische Untersuchung.
