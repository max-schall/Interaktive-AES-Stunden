from render import *

WS = {
'01_Kennzeichnung': dict(sections=[
    ('etikett', [
        A('Nenne die neun Pflichtangaben auf verpackten Lebensmitteln.', 4, '1. Bezeichnung, 2. Zutatenverzeichnis, 3. Allergene, 4. Menge bestimmter Zutaten, 5. Nettofüllmenge, 6. MHD oder Verbrauchsdatum, 7. Name und Anschrift des Unternehmens, 8. Nährwertangabe, 9. Preis mit Grundpreis'),
    ]),
    ('pflicht', [
        SORT('Pflicht oder freiwillig?', ['Zutatenverzeichnis', 'Nutri-Score', 'Nettofüllmenge', 'EU-Bio-Siegel', 'Allergene', '„Neue Rezeptur!“', 'Nährwerte pro 100 g', 'Nährwerte pro Portion'], ['Pflicht', 'freiwillig'], loes=[['Zutatenverzeichnis', 'Nettofüllmenge', 'Allergene', 'Nährwerte pro 100 g'], ['Nutri-Score', 'EU-Bio-Siegel', '„Neue Rezeptur!“', 'Nährwerte pro Portion']]),
    ]),
    ('allergene', [
        A('Nenne sechs der 14 Hauptallergene und erkläre, wie sie gekennzeichnet werden.', 2, 'z. B. Gluten, Milch/Laktose, Eier, Erdnüsse, Schalenfrüchte, Soja, Fisch, Sellerie, Senf, Sesam … // Sie werden im Zutatenverzeichnis hervorgehoben, z. B. fett gedruckt.'),
    ]),
    ('preis', [
        A('Joghurt A: 500 g für 1,49 €. Joghurt B: 150 g für 0,55 €. Berechne die Grundpreise und entscheide.', 2, 'A: 1,49 € : 0,5 kg = 2,98 €/kg; B: 0,55 € : 0,15 kg ≈ 3,67 €/kg // A ist pro kg günstiger.'),
        A('Erkläre den Unterschied zwischen Mindesthaltbarkeitsdatum und Verbrauchsdatum.', 2, 'MHD: Bis dahin garantiert der Hersteller die Qualität; danach oft noch genießbar (prüfen). // Verbrauchsdatum: bei leicht Verderblichem (Hackfleisch); danach nicht mehr essen.'),
    ]),
    ('uebungen', [
        RF(['r|Die Zutat mit dem größten Anteil steht im Zutatenverzeichnis zuerst.', 'f|Nach dem MHD muss man Lebensmittel wegwerfen.|Oft noch genießbar – prüfen.', 'r|Die Nährwerte werden pro 100 g angegeben.', 'f|Der Nutri-Score ist Pflicht.|Er ist freiwillig.']),
    ]),
]),

'02_Nutri_Score': dict(sections=[
    ('skala', [
        TAB('Ordne die Inhaltsstoffe zu.', ['günstig (Pluspunkte)', 'ungünstig (Minuspunkte)'], [['[[Ballaststoffe, Eiweiß, Obst/Gemüse/Nüsse, bestimmte Öle]]', '[[Energie, Zucker, gesättigte Fettsäuren, Salz]]']], h=14),
    ]),
    ('rechner', [
        A('Beschreibe in eigenen Worten, wie der Nutri-Score berechnet wird.', 3, 'Für ungünstige Inhaltsstoffe gibt es Minuspunkte, für günstige Pluspunkte (pro 100 g). Aus der Differenz ergibt sich ein Punktwert, der einer der fünf Stufen A bis E zugeordnet wird.'),
    ]),
    ('vergleich', [
        A('Erkläre, warum man den Nutri-Score einer Tiefkühlpizza nicht mit dem eines Müslis vergleichen darf.', 2, 'Der Nutri-Score vergleicht nur Produkte derselben Produktgruppe; er sagt nichts über den Gesundheitswert im Vergleich zu ganz anderen Lebensmitteln aus.'),
    ]),
    ('muesli', [
        A('Vergleiche die beiden Müslis (Knusper-Choco: 25 g Zucker, 6,9 g gesättigte Fette, 5,8 g Ballaststoffe; Vollkorn-Frucht: 13 g Zucker, 1,7 g gesättigte Fette, 8,7 g Ballaststoffe). Begründe, welches ein A und welches ein D hat.', 3, 'Knusper-Choco: viel Zucker und gesättigte Fette, weniger Ballaststoffe → D. // Vollkorn-Frucht: weniger Zucker und Fett, mehr Ballaststoffe → A.'),
    ]),
    ('uebungen', [
        RF(['r|Der Nutri-Score ist freiwillig.', 'f|Eine A-Pizza ist gesünder als ein Apfel.|Man darf nur innerhalb einer Produktgruppe vergleichen.', 'r|Hersteller müssen den Nutri-Score auf alle Produkte ihrer Marke drucken, wenn sie ihn nutzen.', 'f|E ist dunkelgrün.|E ist rot.']),
    ]),
]),

'03_Zusatzstoffe': dict(sections=[
    ('klassen', [
        TAB('Ergänze Wirkung und Beispiel.', ['Funktionsklasse', 'Wirkung', 'Beispiel'], [['Konservierungsstoffe', '[[hemmen Mikroorganismen]]', '[[E 211]]'], ['Antioxidationsmittel', '[[verhindern Farbveränderung, Fettverderb]]', '[[E 300 Ascorbinsäure]]'], ['Emulgatoren', '[[verbinden Öl und Wasser]]', '[[E 322 Lecithin]]'], ['Süßungsmittel', '[[süßen fast kalorienfrei]]', '[[E 951 Aspartam]]']], h=7),
    ]),
    ('zulassung', [
        L('Zusatzstoffe müssen gesetzlich [[zugelassen]], technologisch [[notwendig]] und gesundheitlich [[unbedenklich]] sein. In Europa sind für konventionelle Lebensmittel ca. [[300]], für Bio-Produkte ca. [[50]] zugelassen.'),
    ]),
    ('energy', [
        A('Untersuche die Zutatenliste eines Energydrinks. Welche Zutaten sind Zusatzstoffe, welche sind bedenklich?', 3, 'Zusatzstoffe: Säuerungsmittel, Säureregulator, Farbstoff, Konservierungsstoff. // Bedenklich: viel Zucker (Karies, Übergewicht) und Koffein (Herzrasen, Schlafstörungen) – für Kinder nicht empfohlen.'),
    ]),
    ('getraenke', [
        TAB('Ordne die Getränke ein.', ['hypotonisch', 'isotonisch', 'hypertonisch'], [['[[Wasser, ungesüßter Tee]]', '[[Saftschorle 1 : 1, Sportgetränk]]', '[[Cola, Energydrink, Nektar]]']], h=12),
    ]),
    ('uebungen', [
        A('Erkläre, warum man nach dem Trinken von Limonade oft mehr Durst hat.', 2, 'Limonade ist hypertonisch: Die Zuckerkonzentration ist höher als im Blut. Um sie auszugleichen, wird dem Körper Wasser entzogen – man bekommt Durst.'),
    ]),
]),

'04_Qualitaetssicherung': dict(sections=[
    ('qualitaet', [
        A('Nenne je eine Anforderung an Lebensmittel aus Sicht von Verbrauchern, Herstellern, Handel und Politik.', 2, 'Verbraucher: Geschmack, Gesundheit, Preis. Hersteller: günstige Produktion, Image. Handel: lange Haltbarkeit, Transport. Politik: Gesundheitsschutz, Schutz vor Täuschung.'),
    ]),
    ('ebenen', [
        TAB('Beschreibe die drei Ebenen der Qualitätssicherung.', ['Ebene', 'Beschreibung'], [['1. Gesetze', '[[LFGB, LMHV – Schutz vor Gefährdung und Täuschung]]'], ['2. Eigenkontrolle', '[[Hersteller kontrollieren selbst nach HACCP]]'], ['3. amtliche Überwachung', '[[Behörden nehmen Proben und untersuchen sie im Labor]]']], h=10, widths=[28, 72]),
    ]),
    ('haccp', [
        A('Erkläre am Beispiel Joghurt, was ein kritischer Kontrollpunkt ist.', 3, 'Ein Punkt, an dem eine Gesundheitsgefahr entstehen kann und kontrolliert werden muss – z. B. die Kühlkette: Steigt die Temperatur über 8 °C (z. B. beim Transport), vermehren sich Keime. Temperaturen werden gemessen und dokumentiert.'),
    ]),
    ('auswahl', [
        A('Nenne vier Kriterien, nach denen du Lebensmittel auswählst.', 1, 'z. B. Preis, Geschmack, Herkunft, Bio, Gesundheit, Marke, Freunde.'),
    ]),
    ('uebungen', [
        A('Gib einen Tipp, wie du zu Hause die Kühlkette nach dem Einkauf einhältst.', 1, 'Kühlware zuletzt einkaufen, Kühltasche benutzen, sofort in den Kühlschrank stellen.'),
    ]),
]),

'05_Qualitaetsfaecher': dict(sections=[
    ('faecher', [
        A('Nenne die acht Qualitätswerte des Qualitätsfächers.', 2, 'Gesundheitswert, Eignungswert, ökonomischer Wert, sozialer Wert, ökologischer Wert, soziokultureller Wert, emotionaler Wert, Genusswert.'),
    ]),
    ('fragen', [
        ZU('Ordne die Fragen den Werten zu.', ['Gesundheitswert', 'ökologischer Wert', 'sozialer Wert', 'Eignungswert'], ['Wie nachhaltig ist die Verpackung?', 'Wie lange ist es haltbar?', 'An welcher Stelle steht Zucker?', 'Was verdienen die Erzeuger?'], loes=[2, 4, 1, 3]),
    ]),
    ('netz', [
        BOX('Bewerte ein Lebensmittel deiner Wahl mit dem Qualitätsfächer (1–5 Punkte) und zeichne ein Netzdiagramm.', 50, loes='Individuell: Netzdiagramm mit acht Achsen und Bewertung.'),
    ]),
    ('personen', [
        A('Erkläre, warum zwei Menschen dasselbe Lebensmittel unterschiedlich bewerten können.', 2, 'Die Gewichtung hängt von Lebensumständen ab: Einkommen, Alter, Familie, Gesundheit, Kochkenntnisse, Werte, Freunde, Lifestyle.'),
    ]),
    ('uebungen', [
        A('Welche Werte sind dir persönlich am wichtigsten? Begründe.', 2, 'Individuell.'),
    ]),
]),

'06_Convenience_Matrix': dict(sections=[
    ('stufen', [
        TAB('Ergänze die Verarbeitungsstufen mit je zwei Beispielen.', ['Stufe', 'Bezeichnung', 'Beispiele'], [['1', '[[küchenfertig]]', '[[geputzter Salat, Fischfilet]]'], ['2', '[[garfertig]]', '[[Fischstäbchen, frische Nudeln]]'], ['3', '[[mischfertig]]', '[[Tütensuppe, Backmischung]]'], ['4', '[[regenerierfertig]]', '[[TK-Pizza, Dosenravioli]]'], ['5', '[[verzehrfertig]]', '[[Fruchtjoghurt, Smoothie]]']], h=7, widths=[10, 30, 60]),
    ]),
    ('sortieren', [
        A('Erkläre, warum rohe Kartoffeln kein Convenience Food sind, Kartoffelpüree-Pulver aber schon.', 2, 'Rohe Kartoffeln sind Rohware, unverarbeitet. Püreepulver wurde industriell verarbeitet (Stufe 3, mischfertig).'),
    ]),
    ('bewertung', [
        TAB('Nenne Vor- und Nachteile.', ['Vorteile', 'Nachteile'], [['[[spart Zeit; gleichbleibende Qualität; hohe Hygiene; lange lagerbar]]', '[[viel Salz, Zucker, Fett; Zusatzstoffe; viel Verpackung; teurer; Verlust von Kochkenntnissen]]']], h=22),
    ]),
    ('matrix', [
        BOX('Erstelle eine Entscheidungsmatrix für Fruchtsaft, Fruchtsaftgetränk und Saftschorle mit mindestens drei Kriterien (eines zwingend) und triff eine begründete Entscheidung.', 45, loes='Matrix mit Produkten waagerecht, Kriterien senkrecht; z. B. zwingend „wenig Zucker“ – Fruchtsaftgetränk scheidet aus; Entscheidung z. B. für Saftschorle mit Begründung.'),
    ]),
    ('uebungen', [
        A('Nimm Stellung: „Convenience Food ist immer ungesund.“', 2, 'Nicht pauschal: TK-Gemüse ist z. B. nährstoffreich; Fertiggerichte enthalten oft viel Salz und Fett. Jedes Produkt muss einzeln beurteilt werden.'),
    ]),
]),

'07_Wiederholung': dict(ichkann=True, sections=[
    ('begriffe', [
        ZU('Ordne zu.', ['LMIV', 'HACCP', 'Grundpreis', 'regenerierfertig', 'Emulgator'], ['verbindet Öl und Wasser', 'muss nur erwärmt werden', 'Preis pro kg oder Liter', 'Verordnung zur Kennzeichnung', 'Risikoanalyse kritischer Kontrollpunkte'], loes=[5, 4, 3, 2, 1]),
    ]),
    ('fall', [
        A('Ihr kauft für einen Schulfest-Stand ein. Beschreibe, worauf ihr beim Einkauf achtet (Kennzeichnung, Allergene, Preis, Kühlung).', 5, 'Zutatenverzeichnis und Allergene prüfen; Grundpreise vergleichen; Nutri-Score innerhalb einer Gruppe nutzen; MHD/Verbrauchsdatum beachten; Kühlkette mit Kühltasche einhalten.'),
    ]),
    ('quiz-st', [
        RF(['r|Die 14 Hauptallergene werden hervorgehoben.', 'f|Isotonische Getränke haben mehr Zucker als das Blut.|Sie haben die gleiche Konzentration.', 'r|Fischstäbchen sind garfertig.', 'f|Der Qualitätsfächer hat fünf Werte.|Acht Werte.']),
    ]),
]),
}
