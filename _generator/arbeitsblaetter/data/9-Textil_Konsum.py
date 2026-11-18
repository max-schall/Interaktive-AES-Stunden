from render import *

WS = {
'01_Textile_Kette': dict(sections=[
    ('kette', [
        L('Den gesamten Prozess, den eine Textilie von der Herstellung des Rohstoffs bis zur Entsorgung durchläuft, nennt man [[textile Kette]]. Mit jedem Schritt steigt der Wert des Produkts – man spricht von einer [[Wertschöpfungskette]].'),
        TAB('Ergänze die acht Schritte der textilen Kette.', ['Nr.', 'Schritt', 'Was passiert?'], [['1', '[[Faserherstellung]]', '[[Baumwolle anbauen; Chemiefasern herstellen]]'], ['2', '[[Garnherstellung]]', '[[Spinnen]]'], ['3', '[[Flächenherstellung]]', '[[Weben, Stricken]]'], ['4', '[[Veredelung]]', '[[Bleichen, Färben, Imprägnieren]]'], ['5', '[[Konfektion]]', '[[Zuschneiden, Nähen]]'], ['6', '[[Transport und Handel]]', '[[Verkauf]]'], ['7', '[[Gebrauch und Pflege]]', '[[Waschen, Trocknen]]'], ['8', '[[Entsorgung]]', '[[Container, Recycling]]']], h=7),
    ]),
    ('reise', [
        A('Erkläre, warum Kleidung oft eine Weltreise zurücklegt, bevor sie bei uns verkauft wird.', 2, 'Viele Länder produzieren wegen geringerer Lohnkosten und niedrigerer Sozial- und Umweltstandards billiger als Deutschland. Die einzelnen Schritte werden dort erledigt, wo es am günstigsten ist.'),
    ]),
    ('fasern', [
        SORT('Sortiere die Fasern.', ['Baumwolle', 'Polyester', 'Wolle', 'Viskose', 'Seide', 'Elasthan', 'Leinen', 'Polyamid'], ['Naturfasern', 'Chemiefasern'], loes=[['Baumwolle', 'Wolle', 'Seide', 'Leinen'], ['Polyester', 'Viskose', 'Elasthan', 'Polyamid']]),
        A('Erkläre, warum Mischgewebe ein Problem sind.', 1, 'Sie lassen sich nicht oder nur schwer in ihre Fasern trennen und recyceln.'),
    ]),
    ('altkleider', [
        L('Von Altkleidern gehen nur ca. [[10]] % an Bedürftige oder in Secondhandläden. Etwa [[40]] % werden nach Osteuropa oder Afrika exportiert, ca. 40 % zu [[Putzlappen]] oder Dämmstoff verarbeitet, der Rest wird [[verbrannt]].'),
    ]),
    ('uebungen', [
        TAB('Lies die Etiketten von drei Kleidungsstücken.', ['Kleidungsstück', 'Herkunftsland', 'Material'], [['', '', ''], ['', '', ''], ['', '', '']], h=8),
    ]),
]),

'02_Fast_Fashion_Umwelt': dict(sections=[
    ('schrank', [
        A('Erkläre den Begriff Fast Fashion.', 2, 'Mode, die in sehr kurzen Abständen in neuen Kollektionen zu sehr niedrigen Preisen angeboten wird. Kleidung wird zur Wegwerfware.'),
        L('Jede Person in Deutschland wirft pro Jahr ca. [[4,7]] kg Kleidung weg. Etwa jedes [[10.]] Kleidungsstück wird gar nicht verkauft.'),
    ]),
    ('tshirt', [
        A('Nenne vier Folgen der Textilproduktion für die Umwelt.', 2, 'Hoher Wasserverbrauch (ca. 2700 l pro T-Shirt), Pestizide beim Baumwollanbau, Chemikalien bei der Veredelung, CO₂-Ausstoß beim Transport, Mikroplastik, Müllberge.'),
    ]),
    ('oekologie', [
        TAB('Die drei Bereiche der Bekleidungsökologie', ['Bereich', 'Worum geht es?', 'Beispiel'], [['Humanökologie', '[[Gesundheit der Träger]]', '[[neue Kleidung vor dem Tragen waschen]]'], ['Produktionsökologie', '[[nachhaltige Herstellung]]', '[[Bio-Baumwolle, wenig Wasser]]'], ['Entsorgungsökologie', '[[nach dem Gebrauch]]', '[[weitergeben, recyceln]]']], h=10),
    ]),
    ('kauf', [
        A('Eine neue Kollektion ist da und alles kostet nur 5 €. Beschreibe, wie du dich verhalten würdest, und begründe.', 3, 'z. B. Nur kaufen, was ich wirklich brauche; vorher im eigenen Schrank schauen; Secondhand als Alternative; begründet mit Ressourcenverbrauch und Müll.'),
    ]),
    ('uebungen', [
        RF(['r|Neue Kleidung sollte man vor dem ersten Tragen waschen.', 'f|Alle Textilien lassen sich gut recyceln.|Mischgewebe kaum', 'r|Synthetische Kleidung verliert beim Waschen Mikroplastik.', 'f|Für ein T-Shirt braucht man ca. 27 l Wasser.|ca. 2700 l']),
    ]),
]),

'03_Fast_Fashion_Sozial': dict(sections=[
    ('preis', [
        TAB('Preisaufteilung eines T-Shirts für 4,99 € (ca.)', ['Posten', 'Betrag'], [['Einzelhandel', '[[2,50 €]]'], ['Markenwerbung', '[[1,24 €]]'], ['Fabrikkosten', '[[0,65 €]]'], ['Transport und Steuern', '[[0,55 €]]'], ['Lohnkosten', '[[0,05 €]]']], h=7),
        A('Bewerte die Aussage: „Ein teures T-Shirt ist fair produziert.“', 2, 'Falsch: Auch beim 19,99-€-T-Shirt erhält die Näherin nur ca. 20 ct; der Mehrpreis geht vor allem an Handel und Werbung. Nur Sozialsiegel geben Orientierung.'),
    ]),
    ('tag', [
        A('Beschreibe die Arbeitsbedingungen vieler Näherinnen in Asien (Arbeitszeit, Lohn, Gesundheit).', 3, 'Bis zu 16 Stunden am Tag, 6–7 Tage pro Woche, oft ohne Pausen; Mindestlohn in Bangladesch ca. 85 € im Monat, reicht kaum zum Leben, kein Kranken- oder Urlaubsgeld; fehlende Schutzkleidung, giftige Chemikalien, Sandstrahlen.'),
    ]),
    ('rechte', [
        L('Weltweit arbeiten ca. [[160 Millionen]] Kinder. Die [[Versammlungsfreiheit]] ist ein Menschenrecht – trotzdem werden [[Gewerkschaften]] in vielen Ländern behindert.'),
    ]),
    ('handeln', [
        A('Nenne drei Möglichkeiten, wie du als Kundin oder Kunde etwas für bessere Arbeitsbedingungen tun kannst.', 2, 'Weniger kaufen, auf Sozialsiegel achten (z. B. Fair Wear), secondhand kaufen, bei Unternehmen nachfragen, Petitionen unterstützen.'),
    ]),
    ('uebungen', [
        RF(['f|Ein teures T-Shirt wird immer fair produziert.|nicht automatisch', 'r|Viele Näherinnen arbeiten bis zu 16 Stunden am Tag.', 'r|Am meisten verdient der Einzelhandel.', 'f|Der Mindestlohn in Bangladesch reicht immer zum Leben.|oft nicht']),
    ]),
]),

'04_Slow_Fashion': dict(sections=[
    ('leiter', [
        A('Bringe in eine sinnvolle Reihenfolge (1 = zuerst versuchen): Secondhand kaufen – neu kaufen – reparieren – anziehen, was ich habe – tauschen/leihen – selber machen.', 2, '1. anziehen, was ich habe, 2. reparieren, 3. tauschen/leihen, 4. Secondhand kaufen, 5. selber machen, 6. neu kaufen (langlebig und fair).'),
    ]),
    ('pflege', [
        BOXES('Zeichne die Pflegesymbole.', ['Waschen 30 °C', 'nicht bleichen', 'nicht in den Trockner', 'Bügeln mittel'], h=26, loes='Bottich mit 30 – Dreieck durchgestrichen – Quadrat mit Kreis durchgestrichen – Bügeleisen mit zwei Punkten'),
        A('Nenne drei Tipps, wie Kleidung länger hält.', 1, 'Pflegesymbole beachten, seltener waschen/auslüften, lufttrocknen, kleine Schäden reparieren.'),
    ]),
    ('cycling', [
        TAB('Erkläre die Begriffe mit je einem Beispiel.', ['Begriff', 'Bedeutung', 'Beispiel'], [['Wiederverwendung', '[[Produkt wird weiter genutzt]]', '[[Flohmarkt, Tauschen]]'], ['Upcycling', '[[aus Altem wird Hochwertigeres]]', '[[Tasche aus Jeans]]'], ['Downcycling', '[[aus Altem wird Minderwertigeres]]', '[[Putzlappen]]']], h=10),
        A('Erkläre, warum man Altkleidercontainer vor dem Einwurf prüfen sollte.', 1, 'Nicht alle gehören gemeinnützigen Organisationen; manche Firmen sind nur auf Profit aus.'),
    ]),
    ('ideen', [
        BOX('Plane ein Upcycling-Projekt: Skizziere, was du aus einem alten Kleidungsstück machst, und notiere Material und Arbeitsschritte.', 45, loes='Individuell, z. B. Einkaufsbeutel aus T-Shirt: Ärmel abschneiden, Halsausschnitt vergrößern, unten Fransen schneiden und verknoten.'),
    ]),
    ('uebungen', [
        MC('Was ist am nachhaltigsten?', ['*weniger Kleidung kaufen', 'viel Bio-Kleidung kaufen', 'Kleidung häufig waschen', 'alles in den Altkleidercontainer']),
    ]),
]),

'05_Kreislaufwirtschaft': dict(sections=[
    ('kreis', [
        L('Der ideale Produktionsprozess ist ein [[Kreislauf]], in dem kein Abfall entsteht. Im [[technischen]] Kreislauf werden Gebrauchsgüter in ihre Rohstoffe zerlegt; im [[biologischen]] Kreislauf gelangen kompostierbare Verbrauchsgüter zurück in die Natur.'),
    ]),
    ('sortieren', [
        SORT('Ordne den Kreisläufen zu.', ['Smartphone', 'Bananenschale', 'Waschmaschine', 'Holzzahnbürste', 'Polyesterjacke', 'Kaffeesatz'], ['technischer Kreislauf', 'biologischer Kreislauf'], loes=[['Smartphone', 'Waschmaschine', 'Polyesterjacke'], ['Bananenschale', 'Holzzahnbürste', 'Kaffeesatz']]),
    ]),
    ('obsoleszenz', [
        A('Erkläre den Begriff geplante Obsoleszenz.', 2, 'Herstellerfirmen verkürzen absichtlich die Lebensdauer eines Produkts (Schwachstellen, keine Updates), damit früher ein neues gekauft wird.'),
        A('Nenne drei Kriterien, auf die du beim Kauf eines Elektrogeräts achtest.', 2, 'Langlebigkeit, Reparierbarkeit (Ersatzteile, Akku tauschbar), lange Software-Updates, Recyclingfähigkeit, einheitliches Ladekabel.'),
    ]),
    ('r', [
        TAB('Die R-Strategien', ['Strategie', 'Bedeutung', 'Beispiel'], [['Refuse', '[[ablehnen]]', '[[keine Plastiktüte]]'], ['Reduce', '[[reduzieren]]', '[[weniger kaufen]]'], ['Reuse', '[[wiederverwenden]]', '[[Mehrwegflasche]]'], ['Repair', '[[reparieren]]', '[[Repair-Café]]'], ['Recycle', '[[wiederverwerten]]', '[[Altgerät zum Wertstoffhof]]'], ['Rot', '[[kompostieren]]', '[[Bioabfall]]']], h=7),
    ]),
    ('uebungen', [
        RF(['r|In Elektroschrott stecken Gold, Silber und Platin.', 'f|Recycle ist die beste R-Strategie.|Refuse', 'r|Seit 2024 gibt es in der EU einheitliche Ladekabel.']),
    ]),
]),

'06_Fair_Trade': dict(sections=[
    ('preis', [
        A('Erkläre den Unterschied zwischen Marktpreis und Fairtrade-Mindestpreis.', 2, 'Der Marktpreis entsteht durch Angebot und Nachfrage und schwankt stark. Der Mindestpreis ist garantiert: Liegt der Marktpreis darunter, wird der Mindestpreis gezahlt.'),
        L('Zusätzlich erhalten die Kooperativen eine [[Fairtrade-Prämie]], mit der sie [[Gemeinschaftsprojekte]] wie Schulen oder Brunnen finanzieren.'),
    ]),
    ('standards', [
        A('Nenne fünf Fairtrade-Standards.', 3, 'Angemessener Lohn, geregelte Arbeitsbedingungen, keine Kinder- und Zwangsarbeit, demokratische Organisation, Versammlungsfreiheit/Gewerkschaften, Diskriminierungsverbot, umweltverträglicher Anbau.'),
    ]),
    ('produkte', [
        L('Am häufigsten fair gehandelt werden [[Kaffee]], Kakao und [[Bananen]]. Mischprodukte wie Schokolade müssen zu mindestens [[20]] % aus fairen Zutaten bestehen.'),
    ]),
    ('echt', [
        A('Auf einer Schokolade steht „fair produziert“, aber es ist kein Siegel zu sehen. Bewerte.', 2, 'Kritisch: Der Begriff „fair“ ist nicht geschützt. Nur zertifizierte Siegel (z. B. Fairtrade, GEPA fair+, Naturland Fair) garantieren Standards. Prüfen z. B. auf siegelklarheit.de.'),
    ]),
    ('uebungen', [
        BOX('Gestalte ein Plakat für einen Fair-Trade-Point an deiner Schule (Skizze).', 40, loes='Individuell: Produkte, Siegel, Preis, kurze Erklärung von Mindestpreis und Prämie.'),
    ]),
]),

'07_Wiederholung': dict(ichkann=True, sections=[
    ('begriffe', [
        ZU('Ordne zu.', ['Upcycling', 'geplante Obsoleszenz', 'Mischgewebe', 'Fairtrade-Prämie', 'Fast Fashion'], ['billige, schnell wechselnde Mode', 'kaum recycelbar', 'Geld für Gemeinschaftsprojekte', 'absichtlich verkürzte Lebensdauer', 'aus Altem wird Hochwertigeres'], loes=[5, 4, 2, 3, 1]),
    ]),
    ('fall', [
        A('Aylin braucht eine neue Winterjacke. Beschreibe, wie sie nachhaltig vorgehen kann (mindestens vier Schritte).', 4, 'Erst schauen, ob es eine gebrauchte Jacke gibt (Geschwister, Secondhand, Tausch); beim Neukauf auf Langlebigkeit und Siegel (Fair Wear, Öko-Tex) achten; Pflegehinweise beachten, lufttrocknen; alte Jacke weitergeben oder gemeinnützig spenden.'),
    ]),
    ('quiz-st', [
        RF(['r|Beim Spinnen entsteht Garn.', 'f|Etwa 90 % der Altkleider gehen an Bedürftige.|ca. 10 %', 'r|Die Näherin erhält bei einem 4,99-€-T-Shirt ca. 5 Cent.', 'f|Der Begriff „fair“ ist gesetzlich geschützt.|nicht geschützt']),
    ]),
]),
}
