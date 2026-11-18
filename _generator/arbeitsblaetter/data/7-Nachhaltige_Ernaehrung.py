from render import *

WS = {
'01_Energiebedarf': dict(sections=[
    ('grund', [
        L('Der [[Grundumsatz]] ist die Energie, die der Körper in völliger Ruhe für Atmung, Herzschlag und Gehirn braucht. Faustformel: 1 kcal × [[kg Körpergewicht]] × [[24]] Stunden. Er hängt ab von Alter, [[Geschlecht]], Größe, Gewicht und Muskelmasse.'),
    ]),
    ('pal', [
        A('Lea wiegt 52 kg, ihr PAL-Wert ist 1,6. Berechne ihren Grundumsatz und ihren Gesamtenergiebedarf.', 3, 'Grundumsatz: 1 kcal × 52 × 24 = 1248 kcal // Gesamtenergiebedarf: 1248 kcal × 1,6 ≈ 1997 kcal (≈ 8360 kJ)'),
        A('Nenne je zwei Beispiele für den Grundumsatz und den Leistungsumsatz.', 2, 'Grundumsatz: Atmung, Herzschlag, Gehirntätigkeit, Körpertemperatur. // Leistungsumsatz: Fahrrad fahren, Treppensteigen, Fußball, Gartenarbeit.'),
    ]),
    ('bilanz', [
        A('Erkläre, was eine ausgeglichene Energiebilanz ist und was bei einer positiven Bilanz passiert.', 2, 'Zufuhr = Verbrauch: Das Gewicht bleibt stabil. // Positive Bilanz (Zufuhr > Verbrauch): Der Körper speichert Fett, langfristig Übergewicht.'),
    ]),
    ('aktiv', [
        A('Eine Butterbrezel hat 337 kcal. Wie lange müsste man ungefähr spazieren gehen bzw. Rad fahren, um diese Energie zu verbrauchen?', 1, 'ca. 92 Minuten spazieren, ca. 56 Minuten Rad fahren'),
    ]),
    ('uebungen', [
        A('Nenne drei Möglichkeiten, deinen Leistungsumsatz im Alltag zu steigern.', 1, 'Treppe statt Aufzug, mit dem Rad zur Schule, Haus- und Gartenarbeit, Sport im Verein.'),
    ]),
]),

'02_Klima': dict(sections=[
    ('treibhaus', [
        L('Neben Kohlenstoffdioxid tragen auch [[Methan]] und [[Lachgas]] zum Treibhauseffekt bei. Um sie zu vergleichen, rechnet man in [[CO₂-Äquivalenten]]. In Deutschland verursacht die Ernährung ca. [[15]] % der Treibhausgase.'),
        A('Nenne fünf Stationen der Lebensmittelkette, an denen Treibhausgase entstehen.', 2, 'Tierhaltung und Anbau (Dünger, Maschinen), Rodung von Wäldern, Verarbeitung, Verpackung, Transport, Handel und Lagerung, Zubereitung.'),
    ]),
    ('fussabdruck', [
        A('Erkläre, warum tierische Lebensmittel mehr Treibhausgase verursachen als pflanzliche.', 3, 'Tiere brauchen Futter, das erst angebaut werden muss, dazu Fläche und Wasser. // Wiederkäuer wie Rinder stoßen bei der Verdauung Methan aus, Ausscheidungen setzen Lachgas frei.'),
    ]),
    ('teller', [
        TAB('Vergleiche zwei Gerichte (CO₂e, gerundet).', ['Gericht', 'Zutaten', 'CO₂e'], [['Burger mit Pommes', '125 g Rind, 200 g Kartoffeln, Salat', '[[ca. 1,8 kg]]'], ['Linsen-Curry mit Reis', '125 g Linsen, 200 g Reis, regionales Gemüse', '[[ca. 0,8 kg]]']], h=8, widths=[28, 50, 22]),
    ]),
    ('dimensionen', [
        A('Nenne die fünf Dimensionen einer nachhaltigen Ernährung nach Karl von Koerber und gib zu einer ein Beispiel.', 2, 'Umwelt, Wirtschaft, Gesellschaft, Gesundheit, Kultur. // z. B. Umwelt: regional und saisonal einkaufen.'),
    ]),
    ('uebungen', [
        A('Nenne drei Handlungsmöglichkeiten für eine klimaverträgliche Ernährung.', 2, 'mehr pflanzliche Lebensmittel, regional und saisonal einkaufen, Verpackung und Lebensmittelabfälle vermeiden.'),
    ]),
]),

'03_Landwirtschaft': dict(sections=[
    ('vergleich', [
        TAB('Vergleiche.', ['', 'konventionell', 'ökologisch'], [['Anbau', '[[Monokultur]]', '[[Fruchtfolge]]'], ['Dünger', '[[mineralischer Dünger]]', '[[organischer Dünger]]'], ['Pflanzenschutz', '[[Pestizide erlaubt]]', '[[keine chemischen Pestizide]]'], ['Tierhaltung', '[[Stallhaltung, Massentierhaltung erlaubt]]', '[[artgerecht, Auslauf, Bio-Futter]]'], ['Gentechnik', '[[erlaubt]]', '[[verboten]]']], h=7),
    ]),
    ('kreislauf', [
        BOX('Zeichne den ökologischen Kreislauf eines Bio-Hofs mit Feld, Futter, Tieren und Dünger.', 35, loes='Feld → Futter → Tiere → Mist/Dünger → Feld; zusätzlich Lebensmittel für Menschen aus Feld und Tieren.'),
    ]),
    ('grundsaetze', [
        A('Nenne die vier Grundsätze der ökologischen Landwirtschaft.', 2, 'Bodenfruchtbarkeit, Tierschutz, Gewässerschutz, Artenvielfalt.'),
    ]),
    ('meinung', [
        A('Nimm Stellung: „Bio-Lebensmittel sind ihren höheren Preis wert.“', 3, 'Pro: Umwelt-, Tier- und Gewässerschutz, mehr Arbeit und Kontrollen rechtfertigen den Preis. // Kontra: nicht für alle bezahlbar; Bio aus Übersee ist nicht immer besser als regionale Ware.'),
    ]),
    ('uebungen', [
        RF(['r|2021 wurden knapp 89 % der Fläche in Deutschland konventionell bewirtschaftet.', 'f|In der ökologischen Landwirtschaft ist Gentechnik erlaubt.|Gentechnik ist verboten.', 'r|Bio-Betriebe werden von Öko-Kontrollstellen überprüft.', 'f|Konventionelle Landwirtschaft belastet die Umwelt weniger.|Sie belastet die Umwelt stärker.']),
    ]),
]),

'04_Regional_Saisonal': dict(sections=[
    ('regional', [
        A('Nenne vier Gründe, regionale Lebensmittel zu bevorzugen.', 2, 'kurze Transportwege (Klima), reif geerntet und frisch, aromatischer, sichert Arbeitsplätze in der Region, weniger Wasserverbrauch als Importware aus Trockengebieten.'),
        A('Vergleiche den CO₂-Ausstoß von Tomaten aus dem beheizten Treibhaus (ca. 9300 g/kg) und aus dem regionalen Freiland (ca. 85 g/kg).', 2, 'Treibhaustomaten verursachen über 100-mal so viel CO₂ wie Freilandtomaten.'),
    ]),
    ('saison', [
        TAB('Nenne je drei Obst- und Gemüsesorten, die jetzt bei uns Saison haben.', ['Monat', 'Obst', 'Gemüse'], [['Juni', '[[Erdbeeren, Kirschen, Himbeeren]]', '[[Spargel, Radieschen, Kopfsalat]]'], ['Oktober', '[[Äpfel, Birnen]]', '[[Kürbis, Kartoffeln, Rosenkohl]]'], ['Januar', '[[Lageräpfel]]', '[[Grünkohl, Feldsalat, Lauch]]']], h=8),
    ]),
    ('bio', [
        L('Bio-Lebensmittel erkennt man am [[EU-Bio-Siegel]], einem Blatt aus [[Sternen]]. Sie müssen zu mindestens [[95]] % aus ökologischen Zutaten bestehen. Anbauverbände wie [[Demeter]] oder Bioland haben noch strengere Regeln.'),
    ]),
    ('einkauf', [
        A('Erkläre, warum die Angabe „regional“ kritisch geprüft werden sollte.', 2, '„Regional“ ist gesetzlich nicht geschützt; jede Initiative legt eigene Kriterien fest – man sollte prüfen, was genau aus welcher Region stammt.'),
    ]),
    ('uebungen', [
        A('Plane mithilfe des Saisonkalenders ein Gericht mit regionalem, saisonalem Gemüse für diesen Monat.', 2, 'Individuell, z. B. Oktober: Kürbissuppe mit Kartoffeln und Lauch.'),
    ]),
]),

'05_Vegetarismus': dict(sections=[
    ('formen', [
        TAB('Was essen sie? Kreuze an (✓/✗).', ['', 'Fleisch', 'Fisch', 'Eier', 'Milch'], [['Pescetarier', '[[✗]]', '[[✓]]', '[[✓]]', '[[✓]]'], ['Ovo-Lakto-Vegetarier', '[[✗]]', '[[✗]]', '[[✓]]', '[[✓]]'], ['Lakto-Vegetarier', '[[✗]]', '[[✗]]', '[[✗]]', '[[✓]]'], ['Veganer', '[[✗]]', '[[✗]]', '[[✗]]', '[[✗]]']], h=6),
    ]),
    ('raten', [
        A('Erkläre den Unterschied zwischen Flexitariern und Veganern.', 2, 'Flexitarier essen überwiegend pflanzlich und nur selten Fleisch. // Veganer verzichten in allen Lebensbereichen auf tierische Produkte – auch Milch, Eier, Honig, Leder.'),
    ]),
    ('gruende', [
        A('Nenne die fünf Beweggründe für eine vegetarische Ernährung mit je einem Beispiel.', 4, 'ethisch-moralisch (Tierleid vermeiden), religiös (Hinduismus), ökologisch (Klima), sozial (Futtergetreide könnte Menschen ernähren), gesundheitlich (weniger Fett, keine Antibiotika-Rückstände).'),
    ]),
    ('naehrstoffe', [
        A('Nenne vier Nährstoffe, die bei veganer Ernährung kritisch sein können, und je eine pflanzliche Quelle.', 2, 'Vitamin B₁₂ (angereicherte Lebensmittel, Präparat), Eisen (Hafer, Hirse, Linsen), Calcium (Mineralwasser, Sesam), Jod (Jodsalz), Omega-3 (Leinöl).'),
    ]),
    ('meinung', [
        A('Nimm Stellung: „In der Mensa sollte es jeden Tag ein vegetarisches Gericht geben.“', 2, 'Individuell begründet.'),
    ]),
    ('uebungen', [
        RF(['f|Vegetarisch ist automatisch gesund.|Auch Pommes und Süßigkeiten sind vegetarisch.', 'r|Hülsenfrüchte sind gute pflanzliche Eiweißquellen.', 'f|Veganer essen Honig.|Honig ist tierisch.', 'r|Der Vegetarismus reicht bis ins 6. Jahrhundert v. Chr. zurück.']),
    ]),
]),

'06_Planetary_Health_Diet': dict(sections=[
    ('idee', [
        A('Erkläre, was man unter „planetarer Gesundheit“ versteht.', 2, 'Die Gesundheit der Menschen ist eng mit dem Zustand der Erde verknüpft: Schäden an Klima und Umwelt wirken auf Ernährung und Gesundheit zurück.'),
    ]),
    ('teller', [
        TAB('Ergänze die PHD-Mengen pro Tag.', ['Lebensmittel', 'Menge'], [['Gemüse', '[[300 g]]'], ['Vollkorngetreide', '[[232 g]]'], ['Obst', '[[200 g]]'], ['Hülsenfrüchte', '[[75 g]]'], ['Nüsse', '[[50 g]]'], ['Fleisch, Geflügel', '[[43 g]]'], ['zugesetzter Zucker', '[[31 g]]']], h=6, widths=[60, 40]),
    ]),
    ('vergleich', [
        A('Vergleiche deinen Fleischkonsum pro Woche mit der PHD. Was könntest du ändern?', 3, 'PHD: ca. 300 g pro Woche. Individueller Vergleich, z. B. fleischfreie Tage, kleinere Portionen, Hülsenfrüchte.'),
    ]),
    ('kritik', [
        A('Nenne je zwei Chancen und zwei Kritikpunkte der PHD.', 3, 'Chancen: schützt Klima und Gesundheit, genug Nahrung für 10 Mrd. Menschen, kulturell anpassbar. // Kritik: 2500 kcal passen nicht für alle, entspricht nicht traditionellen Essgewohnheiten, gelingt nur, wenn alle mitmachen.'),
    ]),
    ('uebungen', [
        A('Überprüfe zwei deiner Lieblingsgerichte: Entsprechen sie den Empfehlungen der PHD?', 2, 'Individuell.'),
    ]),
]),

'07_Wiederholung': dict(ichkann=True, sections=[
    ('begriffe', [
        ZU('Ordne zu.', ['PAL-Wert', 'Monokultur', 'Pescetarier', 'CO₂-Äquivalent'], ['isst Fisch, aber kein Fleisch', 'Treibhausgase in CO₂ umgerechnet', 'Maß für die körperliche Aktivität', 'nur eine Pflanzenart auf einer Fläche'], loes=[3, 4, 1, 2]),
    ]),
    ('fall', [
        A('Erstelle einen klimafreundlichen Speiseplan für drei Tage im Oktober (regional, saisonal, überwiegend pflanzlich). Begründe zwei Entscheidungen.', 5, 'z. B. Kürbissuppe, Linsen-Bolognese mit Vollkornnudeln, Ofenkartoffeln mit Quark und Rosenkohl; Begründung: Saison, regional, wenig Fleisch.'),
    ]),
    ('quiz-st', [
        RF(['r|Gesamtenergiebedarf = Grundumsatz × PAL-Wert.', 'f|Bio-Tomaten aus dem beheizten Gewächshaus sind besonders klimafreundlich.|Freilandware aus der Region ist viel klimafreundlicher.', 'r|Die PHD sieht etwa 300 g Fleisch pro Woche vor.', 'f|„Regional“ ist gesetzlich geschützt.|Nicht geschützt.']),
    ]),
]),
}
