from render import *

WS = {
'01_Kaufentscheidungen': dict(sections=[
    ('typen', [
        TAB('Die vier Kaufentscheidungstypen', ['Typ', 'Merkmal', 'Beispielprodukt'], [['extensiv', '[[ausführlich informieren und vergleichen]]', '[[Smartphone, Sofa]]'], ['limitiert', '[[Auswahl begrenzt, z. B. auf Marken]]', '[[Turnschuhe]]'], ['habitualisiert', '[[aus Gewohnheit]]', '[[Milch, Mehl]]'], ['Impulskauf', '[[spontan, ohne Nachdenken]]', '[[Schokoriegel an der Kasse]]']], h=9),
    ]),
    ('blasen', [
        ZU('Ordne die Aussagen zu.', ['extensiv', 'limitiert', 'habitualisiert', 'Impulskauf'], ['„Nur heute 50 %! Sofort gekauft.“', '„Ich nehme immer dieselbe Zahnpasta.“', '„Ich lese Tests und vergleiche fünf Laptops.“', '„Ich kaufe nur meine Lieblingsmarke.“'], loes=[4, 3, 1, 2]),
    ]),
    ('aida', [
        TAB('Das AIDA-Modell', ['Buchstabe', 'Bedeutung', 'Mittel der Werbung'], [['A', '[[Attention – Aufmerksamkeit]]', '[[Signalfarben, Jingle, Slogan]]'], ['I', '[[Interest – Interesse]]', '[[Detailinformationen]]'], ['D', '[[Desire – Verlangen]]', '[[Rabatt, Lifestyle, Image]]'], ['A', '[[Action – Handlung]]', '[[„Jetzt kaufen“-Button]]']], h=8),
    ]),
    ('pruefen', [
        BOX('Klebe eine Werbeanzeige ein oder beschreibe sie. Markiere die vier AIDA-Phasen und prüfe ein Werbeversprechen.', 50, loes='Individuell: Phasen korrekt markiert; Werbeversprechen auf Mess- und Überprüfbarkeit geprüft.'),
    ]),
    ('uebungen', [
        A('Reflektiere dein eigenes Kaufverhalten: Welcher Typ bist du bei welchen Produkten?', 3, 'Individuell, z. B. habitualisiert bei Lebensmitteln, extensiv bei Elektronik, Impulskäufe bei Süßigkeiten.'),
    ]),
]),

'02_Bewusst_kaufen': dict(sections=[
    ('anforderungen', [
        L('[[Qualität]] ist der Grad, in dem ein Produkt bestimmte Anforderungen erfüllt. Qualitätsanforderungen sind [[individuell]] verschieden.'),
    ]),
    ('stufen', [
        A('Nenne die fünf Stufen des Kaufentscheidungsprozesses.', 3, '1. Produktwunsch, 2. Informationssuche, 3. Bewertung (Tabelle), 4. Kaufentscheidung, 5. nach dem Kauf: Bewertung.'),
    ]),
    ('tabelle', [
        TAB('Vergleiche drei Turnschuhe (Punkte 1–5, Gewicht 1–3).', ['Qualitätsmerkmal', 'Gewicht', 'Produkt 1', 'Produkt 2', 'Produkt 3'], [['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['Summe (Punkte × Gewicht)', '', '', '', '']], h=8),
    ]),
    ('preis', [
        A('Erkläre das Preis-Leistungs-Verhältnis an einem Beispiel.', 2, 'Zwei Produkte erfüllen die gleichen Qualitätsmerkmale, eines ist deutlich teurer – das günstigere hat das bessere Preis-Leistungs-Verhältnis.'),
        A('Nimm Stellung: „Markenprodukte sind immer besser als No-Name-Produkte.“', 2, 'Stimmt nicht: Der Preis allein sagt nichts über die Qualität; Eigenmarken und No-Name-Produkte schneiden in Tests oft gleich gut ab.'),
    ]),
    ('uebungen', [
        RF(['r|Qualitätsanforderungen sind individuell.', 'f|Ein teureres Produkt ist immer besser.|nicht unbedingt', 'r|Wichtige Merkmale kann man stärker gewichten.']),
    ]),
]),

'03_Siegel': dict(sections=[
    ('arten', [
        TAB('Label-Arten', ['Art', 'Wer vergibt?', 'Beispiel'], [['Gütesiegel', '[[staatliche oder gemeinnützige Stellen]]', '[[EU-Bio-Siegel]]'], ['Gütezeichen', '[[Gütegemeinschaften]]', '[[RAL]]'], ['Prüfzeichen', '[[unabhängige Prüfstellen]]', '[[GS-Zeichen]]'], ['Eigenmarke', '[[Handelsunternehmen selbst]]', '[[Bio-Eigenmarke]]']], h=9),
    ]),
    ('oeko', [
        SORT('Ordne die Siegel zu.', ['Demeter', 'GOTS', 'Blauer Engel', 'EU-Bio-Siegel', 'Grüner Knopf', 'FSC'], ['Lebensmittel', 'Textilien', 'Elektro, Papier, Holz'], loes=[['Demeter', 'EU-Bio-Siegel'], ['GOTS', 'Grüner Knopf'], ['Blauer Engel', 'FSC']]),
    ]),
    ('check', [
        A('Nenne aus Sicht der Verbrauchenden je zwei Vor- und Nachteile von Siegeln.', 3, 'Vorteile: schnelle Orientierung, kontrollierte Standards. Nachteile: unübersichtlich (über 1000), teils Werbezwecke ohne Mehrwert, Kriterien unbekannt.'),
    ]),
    ('faelle', [
        A('Patrick wundert sich: Auf einer Packung Haferflocken sind mehrere fast identische Bio-Siegel. Erkläre.', 2, 'Co-Labelling: Der Händler druckt seine Eigenmarke neben das gleichbedeutende EU-Bio-Siegel.'),
    ]),
    ('uebungen', [
        BOXES('Suche drei Siegel auf Kleidung oder Lebensmitteln, zeichne sie ab und erkläre ihre Bedeutung.', ['Siegel 1', 'Siegel 2', 'Siegel 3'], h=30, loes='Individuell.'),
    ]),
]),

'04_Verbraucherschutz': dict(sections=[
    ('inst', [
        L('Verbraucherschutzorganisationen wollen [[informieren]], beraten, unterstützen und bei Bedarf [[rechtlichen Beistand]] leisten.'),
        TAB('Institutionen des Verbraucherschutzes', ['Institution', 'Aufgabe'], [['Aufsichtsbehörden', '[[prüfen Vorschriften, verhängen Strafen]]'], ['Schlichtungsstellen', '[[vermitteln außergerichtlich im Streit]]'], ['Verbraucherzentralen', '[[gemeinnützig; beraten und dürfen klagen]]']], h=9),
    ]),
    ('faelle', [
        ZU('Wer hilft?', ['Aufsichtsbehörde', 'Schlichtungsstelle', 'Verbraucherzentrale'], ['Beratung zum ersten Handyvertrag', 'Restaurant hält Hygieneregeln nicht ein', 'Streit mit dem Energieversorger ohne Gericht'], loes=[3, 1, 2]),
    ]),
    ('tests', [
        A('Erkläre den Unterschied zwischen Tests der Stiftung Warentest und Bewertungen auf Vergleichsportalen.', 2, 'Stiftung Warentest testet unabhängig nach festgelegten Kriterien. Viele Vergleichsportale erhalten Provisionen und sind nicht unabhängig; etwa ein Viertel der Bewertungen ist gefälscht.'),
    ]),
    ('mogel', [
        A('Erkläre den Begriff Mogelpackung.', 1, 'Eine Verpackung täuscht mehr Inhalt vor, als enthalten ist, oder es ist weniger Inhalt bei gleichem Preis drin.'),
        A('Eine Chipstüte enthält statt 200 g nur noch 175 g, der Preis bleibt bei 1,99 €. Berechne den Grundpreis vorher und nachher.', 2, 'vorher 9,95 €/kg, nachher 11,37 €/kg – etwa 14 % teurer.'),
    ]),
    ('uebungen', [
        A('Recherchiere Adresse und Beratungsangebote der Verbraucherzentrale in deiner Nähe.', 2, 'Individuell.'),
    ]),
]),

'05_Verbraucherrechte': dict(sections=[
    ('begriffe', [
        TAB('Pflicht oder freiwillig?', ['Begriff', 'Bedeutung', 'Pflicht/freiwillig'], [['Gewährleistung', '[[Händler haftet 2 Jahre für Mängel]]', '[[Pflicht]]'], ['Garantie', '[[Zusatzleistung von Händler oder Hersteller]]', '[[freiwillig]]'], ['Umtausch', '[[einwandfreie Ware tauschen]]', '[[freiwillig (Kulanz)]]'], ['Widerruf', '[[14 Tage ohne Grund (online, Haustür)]]', '[[Pflicht]]']], h=9),
    ]),
    ('stufen', [
        L('Bei einem Mangel hast du zuerst das Recht auf [[Nacherfüllung]], also Reparatur oder [[Ersatz]]. Gelingt das nicht, kannst du den Kaufpreis [[mindern]] oder vom Vertrag [[zurücktreten]].'),
    ]),
    ('maengel', [
        SORT('Offener oder verdeckter Mangel?', ['Kratzer auf dem Display', 'Akku hält kürzer als beschrieben', 'falsche Größe', 'minderwertiges Material'], ['offener Mangel', 'verdeckter Mangel'], h=18, loes=[['Kratzer auf dem Display', 'falsche Größe'], ['Akku hält kürzer als beschrieben', 'minderwertiges Material']]),
    ]),
    ('faelle', [
        A('Du hast deinen neuen Wollpullover zu heiß gewaschen. Jetzt ist er verfilzt. Erläutere deine Rechte.', 2, 'Keine Gewährleistung, da kein Mangel beim Kauf, sondern ein eigener Pflegefehler. Umtausch nur aus Kulanz.'),
        A('Eine Käuferin hat ein drei Monate altes, nicht funktionierendes Smartphone. Erkläre ihre Rechte.', 2, 'Gewährleistung gegenüber dem Händler: zuerst Reparatur oder Ersatz; im ersten Jahr muss der Händler beweisen, dass der Mangel nicht schon beim Kauf bestand. Beleg vorlegen.'),
    ]),
    ('uebungen', [
        A('Erkläre, warum du die AGB vor Abschluss eines Kaufvertrags lesen solltest.', 1, 'Dort stehen z. B. Lieferzeiten, Umtausch- und Garantieregeln, Mahnverfahren.'),
    ]),
]),

'06_Online_Shopping': dict(sections=[
    ('pro', [
        TAB('Online oder vor Ort?', ['', 'Vorteile', 'Nachteile'], [['online', '[[rund um die Uhr, Preisvergleich, Lieferung]]', '[[Rücksendungen, Müll, Daten, Fake Shops]]'], ['vor Ort', '[[Beratung, anprobieren, Arbeitsplätze, Innenstadt]]', '[[Öffnungszeiten, evtl. teurer, kleinere Auswahl]]']], h=14),
    ]),
    ('fake', [
        A('Nenne fünf Merkmale, die auf einen Fake Shop hinweisen.', 3, 'Auffällige Internetadresse ohne https, dubiose Logos/Namen, zu günstige Preise, fehlende AGB, fehlendes Impressum, nur Vorkasse, Siegel nicht verlinkt.'),
    ]),
    ('widerruf', [
        L('Ein Vertrag im Internet heißt [[Fernabsatz]]. Du hast ein Widerrufsrecht von [[14]] Tagen. Ausgenommen sind z. B. [[Maßanfertigungen]] und schnell verderbliche Ware.'),
        A('Erkläre, welche Auswirkungen das Widerrufsrecht beim Online-Shopping auf die Umwelt hat.', 2, 'Viele bestellen mehrere Artikel zur Auswahl und schicken sie zurück: zusätzliche Transporte, Verpackungsmüll, CO₂; manche Rücksendungen werden vernichtet.'),
    ]),
    ('tipps', [
        A('Nenne vier Tipps für sicheres Online-Shopping.', 2, 'Qualität informieren, Preise vergleichen, Zusatzkosten prüfen, AGB lesen, sichere Bezahlmethode, Bestellbestätigung aufbewahren.'),
    ]),
    ('uebungen', [
        MC('Welche Ware kannst du nach einer Online-Bestellung widerrufen?', ['*Turnschuhe', 'Maßhemd', 'frischen Fisch', 'entsiegelte CD']),
    ]),
]),

'07_Warentest': dict(sections=[
    ('vorbild', [
        A('Erkläre das Ziel eines Warentests.', 1, 'Verbrauchenden durch unabhängige Informationen eine objektivere Produktauswahl ermöglichen.'),
    ]),
    ('schritte', [
        A('Nenne die sieben Schritte eines Warentests.', 3, '1. Testthema festlegen, 2. Informationen recherchieren, 3. Produkte auswählen, 4. Test vorbereiten, 5. durchführen, 6. auswerten und reflektieren, 7. veröffentlichen.'),
    ]),
    ('protokoll', [
        TAB('Protokollbogen (Noten 1–5)', ['Testkriterium', 'Produkt 1', 'Produkt 2', 'Produkt 3'], [['Duft (Blindprobe)', '', '', ''], ['Wirkdauer', '', '', ''], ['Hautverträglichkeit', '', '', ''], ['Umweltfreundlichkeit', '', '', ''], ['Preis', '', '', ''], ['Gesamtergebnis', '', '', '']], h=8),
        A('Erkläre, was eine Blindprobe ist und wozu sie dient.', 1, 'Neutrale Präsentation der Proben (ohne Marke), damit die Testenden objektiv urteilen.'),
    ]),
    ('vergleich', [
        A('Vergleicht eure Testkriterien mit denen der Stiftung Warentest. Erklärt die Unterschiede.', 3, 'Individuell; Stiftung Warentest nutzt Labormessungen, Expertinnen und viele Testpersonen und gewichtet die Kriterien.'),
    ]),
    ('uebungen', [
        L('Ein Deo erhält die Noten 2; 1,5; 3 und 2,5. Das Gesamtergebnis ist [[2,25]] (Summe [[9]] : 4).'),
    ]),
]),

'08_Wiederholung': dict(ichkann=True, sections=[
    ('begriffe', [
        ZU('Ordne zu.', ['Impulskauf', 'Gewährleistung', 'Mogelpackung', 'Co-Labelling', 'Fernabsatz'], ['Vertrag aus der Ferne', 'täuscht mehr Inhalt vor', 'spontaner Kauf', 'gesetzlich, 2 Jahre', 'Eigenmarke neben Siegel'], loes=[3, 4, 2, 5, 1]),
    ]),
    ('fall', [
        A('Zeynep hat online spontan Kopfhörer bestellt. Sie sind zerkratzt und unbequem. Erläutere ihre Möglichkeiten und wie sie den nächsten Kauf vorbereiten sollte.', 5, 'Widerruf innerhalb von 14 Tagen oder Gewährleistung (Ersatz). Nächstes Mal: Qualitätsmerkmale festlegen, Tests lesen, im Fachmarkt probehören, Preise vergleichen, nicht nach Likes kaufen.'),
    ]),
    ('quiz-st', [
        RF(['r|Werbung will Bedürfnisse wecken.', 'f|Ein Umtausch einwandfreier Ware ist Pflicht.|freiwillig', 'r|Verbraucherzentralen sind gemeinnützig.', 'f|Fake Shops haben immer ein Impressum.|oft fehlt es']),
    ]),
]),
}
