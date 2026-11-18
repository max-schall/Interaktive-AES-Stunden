from render import *

WS = {
'01_Beduerfnisse': dict(sections=[
    ('insel', [
        A('Du bist auf einer einsamen Insel gestrandet. Nenne fünf Dinge, die du mitnimmst, und begründe.', 3, 'Individuell, z. B. Wasser, Plane, Feuerzeug, Messer, Erste-Hilfe-Set – Grundbedürfnisse und Sicherheit zuerst.'),
    ]),
    ('pyramide', [
        BOX('Zeichne die Bedürfnispyramide nach Maslow und beschrifte die fünf Stufen mit je einem Beispiel.', 45, loes='von unten: Grundbedürfnisse (Essen, Schlaf) – Sicherheit (Wohnung, Einkommen) – soziale Bedürfnisse (Freunde) – Individualbedürfnisse (Anerkennung) – Selbstverwirklichung (Talente entfalten)'),
    ]),
    ('bedarf', [
        L('Ein [[Bedürfnis]] ist ein empfundener Mangel, verbunden mit dem Wunsch, ihn zu beseitigen. Ein [[Bedarf]] befriedigt das Bedürfnis. Er kann [[materiell]] (z. B. Smartphone) oder nicht-materiell (z. B. Zeit mit Freunden) sein.'),
    ]),
    ('zuordnen', [
        ZU('Welche Stufe?', ['Grundbedürfnis', 'Sicherheit', 'sozial', 'Anerkennung', 'Selbstverwirklichung'], ['Applaus nach dem Auftritt', 'Mittagessen', 'Marathon laufen', 'Sparkonto', 'Klassenfahrt mit Freunden'], loes=[4, 1, 5, 2, 3]),
    ]),
    ('uebungen', [
        A('Nenne drei deiner Wünsche und ordne sie in die Pyramide ein. Welche lassen sich ohne Geld erfüllen?', 3, 'Individuell.'),
    ]),
]),

'02_Nachhaltigkeit': dict(sections=[
    ('wald', [
        A('Erkläre, woher der Begriff Nachhaltigkeit ursprünglich kommt.', 2, 'Aus der Forstwirtschaft vor ca. 300 Jahren: Man sollte nur so viele Bäume fällen, wie in absehbarer Zeit nachwachsen.'),
    ]),
    ('saeulen', [
        L('Nachhaltigkeit bedeutet, so zu leben, dass die [[nachfolgenden Generationen]] ihre Bedürfnisse auch noch befriedigen können.'),
        TAB('Erkläre die drei Säulen mit je einem Beispiel.', ['Säule', 'Ziel', 'Beispiel'], [['Ökologie', '[[Umwelt schützen]]', '[[Plastik vermeiden]]'], ['Ökonomie', '[[effizient wirtschaften]]', '[[langlebige Produkte]]'], ['Soziales', '[[Gerechtigkeit, gleiche Chancen]]', '[[faire Löhne]]']], h=8),
    ]),
    ('sdg', [
        A('Nenne vier der 17 Nachhaltigkeitsziele der Agenda 2030.', 2, 'z. B. keine Armut, kein Hunger, Gesundheit, Bildung, Geschlechtergleichheit, sauberes Wasser, Klimaschutz, nachhaltiger Konsum (Ziel 12).'),
    ]),
    ('enkel', [
        A('Erkläre den Begriff „Enkeltauglichkeit“ und nenne zwei enkeltaugliche Verhaltensweisen.', 2, 'So handeln, dass auch die Enkel noch gut leben können. // z. B. Fahrrad statt Auto, gebraucht kaufen, Reste essen.'),
    ]),
    ('uebungen', [
        RF(['r|Nachhaltigkeit betrifft alle Bereiche unseres Lebens.', 'f|Die Agenda 2030 hat 10 Ziele.|17 Ziele', 'r|Faire Löhne gehören zur sozialen Säule.']),
    ]),
]),

'03_Fussabdruck': dict(sections=[
    ('erden', [
        A('Erkläre, was der ökologische Fußabdruck zeigt.', 2, 'Er vergleicht die zur Verfügung stehenden Ressourcen mit dem tatsächlichen Verbrauch und zeigt, wie nachhaltig wir leben.'),
        L('Würden alle Menschen so leben wie wir in Deutschland, bräuchten wir etwa [[drei]] Erden. Weltweit sind es heute schon ca. [[1,8]] Erden.'),
    ]),
    ('tag', [
        A('Erkläre den Begriff Erdüberlastungstag.', 2, 'Der Tag, an dem die Menschheit alle Ressourcen verbraucht hat, die die Erde in diesem Jahr erneuern kann (2023: 2. August); danach leben wir „auf Pump“.'),
    ]),
    ('rechner', [
        TAB('Mein CO₂-Fußabdruck (Schätzung)', ['Bereich', 'meine Schätzung (t)', 'Ideen zum Verkleinern'], [['Ernährung', '', '[[mehr pflanzlich, regional, saisonal]]'], ['Mobilität', '', '[[Rad, Bus, Bahn]]'], ['Wohnen, Strom', '', '[[Licht aus, Ökostrom]]'], ['Konsum', '', '[[weniger, gebraucht kaufen]]']], h=8),
    ]),
    ('tipps', [
        A('Nenne fünf Möglichkeiten, deinen Fußabdruck zu verkleinern.', 2, 'pflanzlich essen, keine Lebensmittel wegwerfen, Fahrrad/ÖPNV, Strom sparen, gebraucht kaufen, Dinge lange nutzen, Müll vermeiden.'),
    ]),
    ('uebungen', [
        A('Vergleiche den Fußabdruck der USA (5,1 Erden) mit dem Indiens (0,8 Erden). Erkläre den Unterschied.', 2, 'In den USA: viel Konsum, große Autos und Häuser, viel Fleisch. In Indien leben viele Menschen mit wenig Konsum, aber auch in Armut.'),
    ]),
]),

'04_Verpackung': dict(sections=[
    ('materialien', [
        A('Vergleiche die CO₂-Emissionen von Aluminium (7,57 kg/kg), Einweg-Glas (0,62 kg/kg) und Mehrweg-Glas (0,04 kg/kg).', 2, 'Aluminium verursacht am meisten CO₂; Mehrweg-Glas am wenigsten, weil es viele Male wiederbefüllt wird.'),
    ]),
    ('plastik', [
        TAB('Plastik – Segen oder Fluch?', ['Vorteile', 'Nachteile'], [['[[leicht, wasserdicht, stabil, hygienisch]]', '[[verrottet nicht, Mikroplastik, aus Erdöl, wenig recycelt, Müllexporte]]']], h=18),
    ]),
    ('trennung', [
        ZU('Welche Tonne?', ['Gelbe Tonne', 'Papier', 'Altglas', 'Biomüll', 'Restmüll'], ['Bananenschale', 'Joghurtbecher', 'benutztes Taschentuch', 'Marmeladenglas', 'Zeitung'], loes=[4, 1, 5, 3, 2]),
    ]),
    ('einkauf', [
        A('Nenne vier Tipps, um Verpackungsabfall beim Einkauf zu vermeiden.', 2, 'Stofftasche mitnehmen, unverpackt kaufen, Mehrweg bevorzugen, einzeln Verpacktes vermeiden, vor Ort statt online kaufen.'),
    ]),
    ('uebungen', [
        A('Erkläre den Unterschied zwischen stofflicher und energetischer Verwertung.', 2, 'Stofflich: Aus Altmaterial entsteht neues Material (Altpapier → Papier). Energetisch: Abfall wird verbrannt, um Strom und Wärme zu gewinnen.'),
    ]),
]),

'05_Fleischkonsum': dict(sections=[
    ('wasser', [
        L('[[Virtuelles Wasser]] ist die gesamte Wassermenge, die zur Herstellung eines Produkts verwendet wird. Für 1 kg Rindfleisch sind es ca. [[15 400]] Liter, für 1 kg Getreide nur ca. [[1300]] Liter.'),
    ]),
    ('konsum', [
        A('Berechne deinen Fleischkonsum pro Woche (Schätzung) und vergleiche mit der DGE-Empfehlung.', 2, 'Individuell; DGE: höchstens 300–600 g pro Woche.'),
    ]),
    ('folgen', [
        TAB('Auswirkungen des Fleischkonsums', ['Bereich', 'Auswirkung'], [['gesundheitlich', '[[Herz-Kreislauf-Erkrankungen, Schlaganfall]]'], ['ökologisch', '[[Regenwaldabholzung, Wasserverbrauch, Methan]]'], ['sozial', '[[Futtermittel statt Nahrung in Entwicklungsländern]]'], ['wirtschaftlich', '[[Konkurrenz für kleine Betriebe]]']], h=8, widths=[25, 75]),
    ]),
    ('bewusst', [
        A('Nenne drei Möglichkeiten, Fleisch bewusster zu essen.', 2, 'öfter fleischlose Gerichte, kleinere Portionen, hochwertiges Fleisch aus artgerechter, regionaler Haltung, Hülsenfrüchte als Eiweißquelle.'),
    ]),
    ('uebungen', [
        RF(['r|Methan ist 25-mal klimaschädlicher als CO₂.', 'f|In Deutschland wird weniger Fleisch gegessen als empfohlen.|fast doppelt so viel', 'r|Für Futtermittel wird Regenwald abgeholzt.']),
    ]),
]),

'06_Lebensmittel_retten': dict(sections=[
    ('zahlen', [
        L('In Deutschland werden jährlich ca. [[10,9]] Millionen Tonnen Lebensmittel weggeworfen, mehr als die Hälfte in [[privaten Haushalten]]. Das sind ca. [[78]] kg pro Person; etwa die [[Hälfte]] ist vermeidbar.'),
    ]),
    ('kuehlschrank', [
        BOX('Zeichne einen Kühlschrank und trage ein, wo Fleisch, Milchprodukte, Käse/Reste, Gemüse, Butter/Eier hingehören.', 45, loes='unten (kälteste Zone, ca. 2 °C): Fleisch, Fisch; Mitte: Milchprodukte; oben: Käse, Reste; Gemüsefach: Gemüse, Salat; Tür: Butter, Eier, Getränke. Nicht in den Kühlschrank: Tomaten, Brot, Bananen.'),
    ]),
    ('vermeidbar', [
        SORT('Vermeidbar oder unvermeidbar?', ['Bananenschale', 'altes Brot', 'Knochen', 'Nudelreste', 'Nussschalen', 'welker Salat'], ['vermeidbar', 'unvermeidbar'], loes=[['altes Brot', 'Nudelreste', 'welker Salat'], ['Bananenschale', 'Knochen', 'Nussschalen']]),
    ]),
    ('reste', [
        A('Nenne zu drei Resten je ein Gericht.', 2, 'z. B. altes Brot → Arme Ritter; Kartoffeln → Bratkartoffeln; überreife Bananen → Bananenbrot.'),
    ]),
    ('uebungen', [
        A('Nenne fünf Tipps gegen Lebensmittelverschwendung.', 2, 'Einkauf planen, richtig lagern, MHD und Verbrauchsdatum unterscheiden, Sinne nutzen, Reste verwerten, einfrieren, krumme Ware kaufen, teilen.'),
    ]),
]),

'07_Kauftricks_Markterkundung': dict(sections=[
    ('markt', [
        A('Beschreibe vier Verkaufstricks im Supermarkt.', 3, 'Obst und Gemüse am Eingang, Bremszone, Milch hinten, große Einkaufswagen, Sonderangebote mit roten Schildern, Musik und Duft, Quengelzone.'),
    ]),
    ('regal', [
        TAB('Regalzonen', ['Zone', 'Höhe', 'Produkte'], [['Reckzone', '[[über 1,60 m]]', '[[günstigere Produkte]]'], ['Sichtzone', '[[Augenhöhe]]', '[[teure Markenprodukte]]'], ['Griffzone', '[[0,80–1,20 m]]', '[[beliebte Produkte]]'], ['Bückzone', '[[unter 0,80 m]]', '[[Eigenmarken, Großpackungen]]']], h=7),
    ]),
    ('erkannt', [
        A('Nenne Vor- und Nachteile von Kundenkarten.', 2, 'Vorteile: Rabatte, Gutscheine, Punkte. // Nachteile: Preisgabe persönlicher Daten, Analyse des Kaufverhaltens, gezielte Werbung, Bindung an ein Geschäft.'),
    ]),
    ('erkundung', [
        A('Nenne die fünf Schritte einer Markterkundung.', 2, '1. Fragestellung festlegen, 2. Erkundung vorbereiten (Erlaubnis, Bogen), 3. durchführen, 4. auswerten, 5. präsentieren.'),
    ]),
    ('bogen', [
        BOX('Entwirf einen Erkundungsbogen zum Thema „Verkaufstricks“ für einen Supermarkt in deiner Nähe.', 40, loes='Individuell, z. B. Tabelle mit Tricks, Ort im Markt, Beispiel, Notizen.'),
    ]),
    ('uebungen', [
        A('Nenne drei Gegenstrategien gegen Verkaufstricks.', 1, 'Einkaufsliste, satt einkaufen, Budget, Grundpreis vergleichen, oben und unten im Regal schauen.'),
    ]),
]),

'08_Wiederholung': dict(ichkann=True, sections=[
    ('begriffe', [
        ZU('Ordne zu.', ['Bedarf', 'Erdüberlastungstag', 'virtuelles Wasser', 'Quengelzone', 'Mehrweg'], ['Süßigkeiten an der Kasse', 'befriedigt ein Bedürfnis', 'wird wiederbefüllt', 'ab hier leben wir auf Pump', 'Wasser für die Herstellung'], loes=[2, 4, 5, 1, 3]),
    ]),
    ('fall', [
        A('Jonas kauft für das Wochenende mit 25 € ein. Beschreibe, wie er nachhaltig einkaufen kann (mindestens fünf Aspekte).', 5, 'Einkaufsliste, satt einkaufen, wenig und gutes Fleisch, regionales und saisonales Gemüse, Mehrweg/Leitungswasser, Stofftasche, unverpackt, Grundpreis vergleichen, Reste verwerten.'),
    ]),
    ('quiz-st', [
        RF(['r|Die Bedürfnispyramide stammt von Maslow.', 'f|Private Haushalte werfen am wenigsten Lebensmittel weg.|am meisten', 'r|Teure Markenprodukte stehen auf Augenhöhe.', 'f|Aluminium hat den geringsten CO₂-Ausstoß.|den höchsten']),
    ]),
]),
}
