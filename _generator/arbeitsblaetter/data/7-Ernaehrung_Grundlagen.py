from render import *

WS = {
'01_Grundbegriffe': dict(sections=[
    ('einteilung', [
        L('[[Lebensmittel]] sind alle Stoffe, die gegessen oder getrunken werden. Man teilt sie in [[Nahrungsmittel]] und [[Genussmittel]] ein. Nahrungsmittel sind pflanzlicher oder [[tierischer]] Herkunft.'),
        A('Nenne drei pflanzliche, drei tierische Nahrungsmittel und zwei Genussmittel.', 2, 'pflanzlich: Kartoffeln, Linsen, Äpfel // tierisch: Milch, Ei, Fisch // Genussmittel: Kaffee, Schwarztee, Energydrinks'),
    ]),
    ('dichte', [
        A('Berechne die Nährstoffdichte (Vitamin C) für Pellkartoffeln (17 mg, 70 kcal) und Pommes frites (17 mg, 290 kcal) und vergleiche.', 3, 'Pellkartoffeln: 17 : 70 ≈ 0,24 mg/kcal // Pommes: 17 : 290 ≈ 0,06 mg/kcal // Pellkartoffeln liefern pro Kalorie etwa viermal so viel Vitamin C.'),
    ]),
    ('energie', [
        A('Erkläre mit eigenen Worten den Unterschied zwischen Nährstoffdichte und Energiedichte.', 2, 'Nährstoffdichte: wie viel eines Nährstoffs im Verhältnis zur Energie enthalten ist. // Energiedichte: wie viel Energie ein Lebensmittel pro Gramm liefert.'),
    ]),
    ('urteil', [
        SORT('Ordne: oft oder nur ab und zu essen?', ['Brokkoli', 'Gummibärchen', 'Vollkornnudeln', 'Sahnetorte', 'Naturjoghurt', 'Chips', 'Beeren', 'Limonade'], ['oft', 'ab und zu'], loes=[['Brokkoli', 'Vollkornnudeln', 'Naturjoghurt', 'Beeren'], ['Gummibärchen', 'Sahnetorte', 'Chips', 'Limonade']]),
    ]),
    ('uebungen', [
        A('100 g Paprika enthalten 120 mg Vitamin C und 30 kcal. Berechne die Nährstoffdichte.', 1, '120 : 30 = 4 mg/kcal – sehr hohe Nährstoffdichte'),
    ]),
]),

'02_Ernaehrungspyramide': dict(sections=[
    ('aufbau', [
        TAB('Ergänze die Lebensmittelgruppen der Pyramide.', ['Lebensmittelgruppe', 'Portionen am Tag', 'Ampelfarbe'],
            [['Getränke', '[[6]]', '[[grün]]'], ['Gemüse', '[[3]]', '[[grün]]'], ['Obst', '[[2]]', '[[grün]]'], ['Brot, Getreide, Beilagen', '[[4]]', '[[grün]]'], ['Milch und Milchprodukte', '[[3]]', '[[gelb]]'], ['Fleisch, Fisch, Ei, Hülsenfrüchte', '[[1]]', '[[gelb]]'], ['Fette und Öle', '[[2]]', '[[gelb]]'], ['Extras', '[[1]]', '[[rot]]']], h=6),
    ]),
    ('einordnen', [
        A('Ordne in die Pyramide ein: Banane, Pommes frites, Fruchtjoghurt, Linsen, Rapsöl, Haferflocken.', 2, 'Banane: Obst · Pommes frites: Extras · Fruchtjoghurt: Milch + Extras · Linsen: Fleisch/Fisch/Ei/Hülsenfrüchte · Rapsöl: Fette und Öle · Haferflocken: Brot, Getreide, Beilagen'),
    ]),
    ('tag', [
        BOX('Zeichne deine Pyramide von gestern: Male für jede Portion einen Baustein aus. Wo liegst du gut, wo nicht?', 40, loes='Individuelle Lösung mit Bewertung, z. B. zu wenig Gemüse, zu viele Extras.'),
    ]),
    ('handmass', [
        L('Beim [[Handmaß]] passt sich die Portion automatisch der [[Körpergröße]] und damit dem Bedarf an. Eine Scheibe Brot ist so groß wie die [[Handfläche]] mit Fingern.'),
    ]),
    ('uebungen', [
        RF(['r|Fruchtjoghurt zählt als Milchprodukt und als Extra.', 'f|Grün bedeutet „sparsam essen“.|Grün = reichlich', 'f|Kartoffeln gehören zum Gemüse.|zu Brot, Getreide, Beilagen', 'r|Hülsenfrüchte sollte man mindestens einmal pro Woche essen.']),
    ]),
]),

'03_Ernaehrungskreis': dict(sections=[
    ('kreis', [
        A('Nenne die sieben Lebensmittelgruppen des Ernährungskreises.', 2, 'Getränke; Getreide/Getreideprodukte/Kartoffeln; Gemüse und Salat; Obst; Milch und Milchprodukte; Fleisch/Wurst/Fisch/Eier; Fette und Öle'),
    ]),
    ('verteilung', [
        L('Man sollte mehr als [[drei Viertel]] pflanzliche und knapp [[ein Viertel]] tierische Lebensmittel essen. Die Energie sollte zu ca. [[55]] % aus Kohlenhydraten, [[30]] % aus Fett und [[15]] % aus Eiweiß stammen.'),
    ]),
    ('regeln', [
        A('Nenne fünf Kernaussagen der DGE „Gut essen und trinken“.', 3, 'Am besten Wasser trinken; Obst und Gemüse viel und bunt (5 am Tag); Vollkorn ist die beste Wahl; Fisch jede Woche; Fleisch und Wurst weniger ist mehr; pflanzliche Öle bevorzugen; Süßes, Salziges und Fettiges stehen lassen; Mahlzeiten genießen; in Bewegung bleiben.'),
    ]),
    ('vergleich', [
        TAB('Vergleiche Pyramide und Kreis.', ['', 'Ernährungspyramide', 'Ernährungskreis'], [['Gruppen', '[[acht]]', '[[sieben]]'], ['Mengenangabe', '[[Portionen pro Tag]]', '[[Größe der Segmente]]'], ['Süßes', '[[Extras, 1 Portion]]', '[[nicht abgebildet]]'], ['Getränke', '[[unterste Reihe]]', '[[in der Mitte]]']], h=8),
    ]),
    ('uebungen', [
        A('Erstelle ein Essprotokoll für einen Tag und überprüfe, welche DGE-Empfehlungen du einhältst.', 3, 'Individuelle Lösung.'),
    ]),
]),

'04_Naehrstoffe': dict(sections=[
    ('uebersicht', [
        TAB('Ordne die Nährstoffe ein.', ['energieliefernd (Makronährstoffe)', 'nicht energieliefernd (Mikronährstoffe)', 'energiefrei'], [['[[Kohlenhydrate, Fette, Eiweiße]]', '[[Vitamine, Mineralstoffe]]', '[[Wasser]]']], h=12),
    ]),
    ('aufgaben', [
        ZU('Ordne die Hauptaufgaben zu.', ['Brennstoffe', 'Baustoffe', 'Wirkstoffe'], ['regeln Körpervorgänge, stärken die Immunabwehr', 'liefern Energie, halten die Körpertemperatur', 'bauen Zellen und Gewebe auf'], loes=[3, 1, 2]),
    ]),
    ('energie', [
        A('100 g Vollmilch enthalten 3,5 g Fett, 4,8 g Kohlenhydrate und 3,3 g Eiweiß. Berechne den Energiegehalt in kJ.', 2, '3,5 · 37 + (4,8 + 3,3) · 17 = 129,5 + 137,7 ≈ 267 kJ (≈ 64 kcal)'),
    ]),
    ('mischung', [
        A('Begründe, warum Nudeln mit Ketchup zwar satt machen, aber dauerhaft für eine optimale Nährstoffversorgung ungeeignet sind.', 3, 'Sie liefern vor allem Kohlenhydrate (Energie), aber kaum Vitamine, Mineralstoffe, Ballaststoffe und wenig hochwertiges Eiweiß. // Kein Lebensmittel enthält alle Nährstoffe – erst die abwechslungsreiche Mischung versorgt den Körper.'),
    ]),
    ('uebungen', [
        L('1 g Kohlenhydrate liefert [[17]] kJ, 1 g Eiweiß [[17]] kJ und 1 g Fett [[37]] kJ.'),
    ]),
]),

'05_Wasser': dict(sections=[
    ('bilanz', [
        L('Der Körper eines Erwachsenen besteht zu ca. [[65]] % aus Wasser. Täglich verlieren wir ca. [[2,5]] Liter. Davon sollten wir ca. [[1,5]] Liter trinken, etwa [[1]] Liter nehmen wir über Lebensmittel auf.'),
    ]),
    ('aufgaben', [
        A('Nenne vier Aufgaben von Wasser im Körper.', 2, 'Bestandteil von Zellen und Körperflüssigkeiten; reguliert die Körpertemperatur; transportiert Nährstoffe; Ausscheidung von Abbauprodukten über die Niere.'),
        A('Beschreibe die Folgen von Wassermangel.', 2, 'Müdigkeit, Konzentrationsschwäche, Kopfschmerzen; das Blut „dickt ein“.'),
    ]),
    ('getraenke', [
        SORT('Gute Durstlöscher oder ungeeignet?', ['Leitungswasser', 'Cola', 'Kräutertee', 'Energydrink', 'Apfelschorle 1 : 3', 'Fruchtnektar', 'Mineralwasser', 'Eistee'], ['gut', 'ungeeignet'], loes=[['Leitungswasser', 'Kräutertee', 'Apfelschorle 1 : 3', 'Mineralwasser'], ['Cola', 'Energydrink', 'Fruchtnektar', 'Eistee']]),
    ]),
    ('lebensmittel', [
        A('Nenne drei wasserreiche Lebensmittel und zwei Verwendungen von Wasser in der Küche.', 2, 'Gurke, Tomate, Melone (über 85 % Wasser) // Lösungsmittel (Tee kochen), Quellmittel (Flocken), Garen von Nudeln und Kartoffeln'),
    ]),
    ('uebungen', [
        A('Vergleiche Leitungswasser und Mineralwasser.', 2, 'Leitungswasser: streng kontrolliert, günstig, umweltfreundlich, aber weniger Mineralstoffe. Mineralwasser: mehr Mineralstoffe, aber teurer und mit Transport und Verpackung.'),
    ]),
]),

'06_Kohlenhydrate': dict(sections=[
    ('aufbau', [
        TAB('Ergänze die Einteilung.', ['Gruppe', 'Bausteine', 'Beispiele'], [['Einfachzucker', '[[1]]', '[[Traubenzucker, Fruchtzucker]]'], ['Zweifachzucker', '[[2]]', '[[Haushaltszucker, Milchzucker]]'], ['Vielfachzucker', '[[viele]]', '[[Stärke, Zellulose, Glykogen]]']], h=7),
    ]),
    ('verdauung', [
        A('Beschreibe die Verdauung der Stärke vom Mund bis ins Blut.', 3, 'Mund: Amylase im Speichel baut einen Teil der Stärke zu Malzzucker ab. // Magen: Speisebrei wird mit Wasser und Magensäure durchmischt. // Dünndarm: Stärke wird vollständig zu Traubenzucker abgebaut, der ins Blut gelangt.'),
    ]),
    ('korn', [
        BOX('Zeichne einen Längsschnitt durch ein Getreidekorn und beschrifte Schale, Aleuronschicht, Mehlkörper und Keimling.', 30, loes='außen Frucht- und Samenschale, darunter Aleuronschicht, innen Mehlkörper (Stärke), an einem Ende der Keimling, am anderen die Bärtchen.'),
        A('Begründe, warum Vollkorn die beste Wahl ist.', 2, 'Vollkorn enthält alle Bestandteile des Korns – mehr Ballaststoffe, Vitamine, Mineralstoffe – wird langsam abgebaut und macht lange satt.'),
    ]),
    ('zucker', [
        A('Eine 0,5-l-Flasche Cola enthält ca. 53 g Zucker. Berechne die Zuckerwürfel (3 g) und bewerte mit der WHO-Empfehlung.', 2, '53 : 3 ≈ 18 Zuckerwürfel // Das ist mehr als die WHO-Obergrenze von 25–50 g zugesetztem Zucker für einen ganzen Tag.'),
    ]),
    ('uebungen', [
        A('Eine Jugendliche wiegt 50 kg. Wie viel Kohlenhydrate braucht sie täglich, und wie viel davon höchstens als Zucker?', 2, '50 · 5 g = 250 g Kohlenhydrate // höchstens ein Drittel als Einfach- und Zweifachzucker: ca. 83 g'),
    ]),
]),

'07_Fette': dict(sections=[
    ('aufbau', [
        BOX('Zeichne den Aufbau eines einfachen Fettes und beschrifte Glycerin und Fettsäuren.', 25, loes='Glycerin als „Rückgrat“, daran drei Fettsäuren (Ketten).'),
        L('Feste Fette wie Butter bestehen vor allem aus [[gesättigten]] Fettsäuren, Öle aus [[ungesättigten]] Fettsäuren. Omega-3- und Omega-6-Fettsäuren sind [[essenziell]].'),
        L('Gesättigte Fettsäuren haben [[keine]] Doppelbindung – alle C-Atome sind mit [[H-Atomen]] gesättigt. Ungesättigte Fettsäuren haben [[mindestens eine]] Doppelbindung.'),
    ]),
    ('aufgaben', [
        A('Nenne vier Aufgaben von Fett im Körper.', 2, 'Energie (37 kJ/g) und Energiespeicher; Schutz der Organe; Wärmeisolierung; Geschmacksträger; Transport der fettlöslichen Vitamine A, D, E, K.'),
    ]),
    ('versteckt', [
        A('Erkläre den Unterschied zwischen sichtbaren und versteckten Fetten und nenne je zwei Beispiele.', 3, 'Sichtbare Fette sieht und dosiert man selbst: Butter auf dem Brot, Öl im Dressing. // Versteckte Fette stecken unsichtbar in Lebensmitteln: Wurst, Käse, Chips, Schokolade, Kuchen.'),
    ]),
    ('kueche', [
        ZU('Welches Fett passt?', ['Schnitzel braten', 'Salatdressing', 'Kuchen backen'], ['Butter oder Margarine', 'Butterschmalz oder raffiniertes Rapsöl', 'kaltgepresstes Olivenöl'], loes=[3, 1, 2]),
    ]),
    ('uebungen', [
        A('Ein Jugendlicher wiegt 60 kg. Wie viel Fett darf er höchstens essen? Wie viel Energie ist das?', 2, 'höchstens 60 g Fett // 60 · 37 kJ = 2220 kJ (≈ 540 kcal)'),
    ]),
]),

'08_Eiweisse': dict(sections=[
    ('aufbau', [
        L('Eiweiße bestehen aus [[20]] verschiedenen Aminosäuren. [[Acht]] davon sind unentbehrlich und müssen mit der Nahrung aufgenommen werden. Eiweiße dienen vor allem als [[Baustoffe]].'),
    ]),
    ('wertigkeit', [
        A('Erkläre den Begriff „biologische Wertigkeit“.', 2, 'Sie gibt an, wie viel Gramm Körpereiweiß aus 100 g Nahrungseiweiß gebildet werden können. Referenz: Hühnerei = 100.'),
    ]),
    ('kombi', [
        A('Nenne drei Gerichte, bei denen sich Eiweiße ergänzen, und gib die Kombination an.', 3, 'Bauernfrühstück (Kartoffel + Ei), Müsli mit Milch (Getreide + Milch), Linsensuppe mit Brot (Hülsenfrüchte + Getreide), Pellkartoffeln mit Quark (Kartoffel + Milch).'),
    ]),
    ('kueche', [
        A('Berechne deinen Eiweißbedarf (0,9 g pro kg Körpergewicht) für ein Körpergewicht von 55 kg.', 1, '55 · 0,9 g = 49,5 g Eiweiß pro Tag'),
        A('Nenne drei Beispiele für die Denaturierung von Eiweiß in der Küche.', 1, 'Ei hart kochen, Fleisch braten, Eischnee schlagen, Zitronensaft in Milch, Joghurtherstellung.'),
    ]),
    ('uebungen', [
        A('Nimm Stellung: „Ich brauche Protein-Shakes, weil ich Sport mache.“', 3, 'Mit einer abwechslungsreichen Ernährung (Milchprodukte, Hülsenfrüchte, Getreide, Ei, Fisch) wird der Eiweißbedarf auch bei Sport gedeckt. Shakes sind teuer und meist unnötig.'),
    ]),
]),

'09_Vitamine_Mineralstoffe': dict(sections=[
    ('vitamine', [
        TAB('Ergänze die Tabelle.', ['Vitamin', 'Aufgabe', 'Vorkommen'], [['A', '[[Sehvorgang, Haut]]', '[[Karotten, Leber]]'], ['D', '[[Knochen, Zähne]]', '[[Fisch, Eigelb, Sonnenlicht]]'], ['C', '[[Immunsystem, Bindegewebe]]', '[[Paprika, Kiwi, Zitrusfrüchte]]'], ['B₁₂', '[[Blutbildung]]', '[[Fleisch, Fisch, Milch, Ei]]']], h=7),
    ]),
    ('loeslich', [
        L('Die Vitamine [[A, D, E, K]] sind fettlöslich, die Vitamine der [[B]]-Gruppe und Vitamin [[C]] sind wasserlöslich.'),
    ]),
    ('mineral', [
        A('Erkläre den Unterschied zwischen Mengen- und Spurenelementen und nenne je zwei Beispiele.', 2, 'Mengenelemente braucht der Körper in Gramm-Mengen: Calcium, Natrium, Kalium, Magnesium. // Spurenelemente nur in Milli- oder Mikrogramm: Eisen, Jod, Zink, Fluor.'),
    ]),
    ('schonend', [
        A('Nenne vier Regeln für eine vitaminschonende Zubereitung.', 2, 'erntefrisch verwenden; unzerkleinert und kurz waschen; kurz vor der Zubereitung zerkleinern; dünsten oder dämpfen; nicht warm halten; abgedeckt und dunkel lagern; bei fettlöslichen Vitaminen etwas Fett zugeben.'),
    ]),
    ('uebungen', [
        A('Nimm Stellung: Brauchst du Vitamin-C-Brausetabletten bei einer Erkältung?', 2, 'Meist nicht: Eine Paprika oder zwei Kiwis decken den Tagesbedarf. Eine vollwertige Ernährung liefert alle Vitamine.'),
    ]),
]),

'10_Ballaststoffe_Versuch': dict(sections=[
    ('ballast', [
        A('Beschreibe die Wirkung von Ballaststoffen im Mund, im Magen und im Darm.', 3, 'Mund: kräftiges Kauen, mehr Speichel. // Magen: Quellen, Magen wird gedehnt, schnelles und langes Sättigungsgefühl. // Darm: Speisebrei nimmt Wasser auf, Darmtätigkeit wird angeregt, Verstopfung verhindert.'),
    ]),
    ('rechner', [
        A('Stelle einen Tagesplan mit mindestens 30 g Ballaststoffen zusammen.', 3, 'z. B. Haferflocken (5 g) + Apfel (3 g) + 2 Scheiben Vollkornbrot (7 g) + Vollkornnudeln (7 g) + Brokkoli (4,5 g) + Himbeeren (5 g) = 31,5 g'),
    ]),
    ('sps', [
        ZU('Ordne zu.', ['Carotinoide', 'Sulfide', 'Glucosinolate', 'Flavonoide'], ['Duftstoffe in Zwiebeln und Knoblauch', 'Aromastoffe in Kohl und Senf', 'rote und blaue Farbstoffe in Beeren', 'orange Farbstoffe in Karotten'], loes=[2, 3, 4, 1]),
    ]),
    ('versuch', [
        TAB('Fettfleckprobe: Notiere Beobachtung und Ergebnis.', ['Lebensmittel', 'Beobachtung', 'Fett?'], [['Öl', '[[glasiger Fleck]]', '[[ja]]'], ['Gurke', '[[nichts zu sehen]]', '[[nein]]'], ['Erdnüsse', '[[glasiger Fleck]]', '[[ja]]'], ['Apfel', '[[nichts zu sehen]]', '[[nein]]']], h=7),
    ]),
    ('protokoll', [
        A('Nenne die sechs Schritte, um einen Versuch durchzuführen.', 2, '1. Ausgangsfrage formulieren, 2. Vermutungen aufstellen, 3. Versuch planen, 4. Versuch durchführen, 5. Versuch auswerten, 6. Abfälle entsorgen.'),
    ]),
    ('uebungen', [
        A('Erkläre, woran man bei der Iodprobe Stärke erkennt.', 1, 'Das Lebensmittel färbt sich blauschwarz.'),
    ]),
]),

'11_Wiederholung': dict(ichkann=True, sections=[
    ('begriffe', [
        ZU('Ordne zu.', ['Nährstoffdichte', 'Baustoff', 'biologische Wertigkeit', 'Ballaststoffe'], ['pflanzliche Faser- und Quellstoffe', 'Nährstoffgehalt : Energiegehalt', 'Körpereiweiß aus 100 g Nahrungseiweiß', 'baut den Körper auf'], loes=[2, 4, 3, 1]),
    ]),
    ('ordnen', [
        TAB('Nenne je zwei Lebensmittel mit viel …', ['Kohlenhydraten', 'Fett', 'Eiweiß', 'Vitamin C', 'Ballaststoffen'], [['[[Nudeln, Reis]]', '[[Butter, Salami]]', '[[Quark, Ei]]', '[[Paprika, Kiwi]]', '[[Vollkornbrot, Linsen]]']], h=12),
    ]),
    ('quiz-st', [
        RF(['r|Fett liefert pro Gramm mehr als doppelt so viel Energie wie Kohlenhydrate.', 'f|Im Ernährungskreis stehen Süßigkeiten in der Mitte.|Getränke stehen in der Mitte.', 'r|Vitamin D kann der Körper mit Sonnenlicht bilden.', 'f|Man sollte täglich mindestens 3 g Ballaststoffe essen.|mindestens 30 g']),
    ]),
]),
}
