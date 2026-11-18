from render import *

WS = {
'01_Hygiene': dict(sections=[
    ('bereiche', [
        TAB('Nenne für jeden Hygienebereich drei Regeln.', ['persönliche Hygiene', 'Lebensmittelhygiene', 'Arbeitsplatzhygiene'],
            [['[[Hände gründlich waschen]]', '[[Obst und Gemüse waschen]]', '[[Arbeitsflächen abwischen]]'], ['[[lange Haare zusammenbinden]]', '[[kühl und abgedeckt lagern]]', '[[frische Spül- und Geschirrtücher]]'], ['[[Schmuck ablegen, Schürze tragen]]', '[[rohes Fleisch auf eigenem Brett]]', '[[Abfälle sofort entsorgen]]']], h=9),
    ]),
    ('haende', [
        A('Nenne vier Situationen, nach denen du dir in der Küche die Hände waschen musst.', 2, 'vor dem Kochen; nach dem Toilettengang; nach dem Naseputzen oder Niesen; nach dem Griff in die Haare; nach dem Anfassen von rohem Fleisch, Fisch oder Eiern.'),
    ]),
    ('keime', [
        A('Begründe, warum rohes Fleisch und Gemüse für den Salat nicht auf demselben Schneidebrett geschnitten werden dürfen.', 3, 'Auf rohem Fleisch können Krankheitserreger wie Salmonellen sein. // Sie würden auf das Gemüse übertragen, das nicht mehr erhitzt wird – man kann krank werden (Durchfall, Erbrechen, Fieber).'),
        A('Plane, wie du Reste vom Mittagessen möglichst hygienisch lagerst.', 2, 'Reste abkühlen lassen, in eine saubere Dose füllen, abdecken bzw. verschließen und im Kühlschrank lagern; bald verbrauchen.'),
    ]),
    ('chefkoch', [
        L('Bei der Chefkochprobe wird mit dem [[ersten]], sauberen Löffel die Speise aufgenommen und [[kontaktlos]] auf den zweiten Löffel gegeben. Probiert wird nur vom [[zweiten]] Löffel.'),
    ]),
    ('uebungen', [
        RF(['r|Unter Ringen sammeln sich viele Keime.', 'f|Man niest am besten in die Hand.|in die Armbeuge', 'f|Für Geschirr und Arbeitsflächen kann man dasselbe Tuch nehmen.|unterschiedliche Tücher verwenden', 'r|Salmonellen können auf rohem Geflügel vorkommen.']),
    ]),
]),

'02_Kuechenunfaelle': dict(sections=[
    ('gefahren', [
        TAB('Nenne je zwei Regeln, um diese Unfälle zu vermeiden.', ['Unfall', 'Regeln'],
            [['Schnittverletzung', '[[Tunnel-/Krallengriff; immer auf dem Brett schneiden; fallende Messer nie auffangen]]'], ['Verbrennung', '[[Topfhandschuhe; Abstand beim Öffnen des Backofens; Nudelwasser vom Körper weg abgießen]]'], ['Sturz', '[[Boden trocken halten; Stolperfallen wegräumen; Leiter benutzen]]']], h=11, widths=[22, 78]),
    ]),
    ('fettbrand', [
        A('Erkläre, warum man einen Fettbrand nie mit Wasser löschen darf, und beschreibe, wie man richtig löscht.', 3, 'Das Wasser verdampft auf dem heißen Fett explosionsartig und reißt brennende Fetttröpfchen mit – eine Stichflamme entsteht, schwere Verbrennungen drohen. // Richtig: Herd ausschalten, Brand mit Deckel oder Löschdecke ersticken.'),
    ]),
    ('notfall', [
        A('Nenne vier Schutzvorrichtungen in der Schulküche und erkläre, wann man sie braucht.', 3, 'Notausgang (Flucht bei Feuer), Verbandskasten (Verletzungen), Löschdecke (Fettbrand, brennende Kleidung), Not-Aus-Schalter (Strom in der ganzen Küche aus, z. B. bei defektem Gerät).'),
    ]),
    ('symbole', [
        ZU('Ordne die Gefahrensymbole ihrer Bedeutung zu.', ['Flamme', 'Ausrufezeichen', 'toter Baum und Fisch', 'Hand und Oberfläche mit Tropfen'], ['umweltgefährdend', 'ätzend', 'leicht entzündlich', 'gesundheitsschädlich, reizend'], loes=[3, 4, 1, 2]),
    ]),
    ('uebungen', [
        A('Beschreibe eine Unfallsituation, die du zu Hause erlebt hast, und erkläre, wie man sie hätte vermeiden können.', 3, 'Individuell, z. B. am heißen Topfdeckel verbrannt → Topfhandschuh benutzen.'),
    ]),
]),

'03_Arbeitsgeraete': dict(sections=[
    ('geraete', [
        TAB('Ergänze die Verwendung.', ['Arbeitsgerät', 'Verwendung'],
            [['Schaumkelle', '[[feste Speisen aus heißem Wasser oder Fett heben]]'], ['Teigschaber', '[[Schüsseln restlos ausschaben]]'], ['Schneebesen', '[[verrühren, schaumig schlagen]]'], ['Wellholz', '[[Teig gleichmäßig ausrollen]]'], ['Sieb', '[[Festes und Flüssiges trennen]]'], ['Handrührgerät mit Knethaken', '[[feste Teige wie Hefeteig kneten]]']], h=7, widths=[32, 68]),
    ]),
    ('waage', [
        A('Beschreibe, wie du mit einer Digitalwaage 250 g Mehl in einer Schüssel abwiegst.', 3, 'Waage einschalten, Einheit Gramm prüfen. // Leere Schüssel auflegen, TARA drücken – die Anzeige steht auf 0. // Mehl einfüllen, bis 250 g angezeigt werden.'),
    ]),
    ('topf', [
        A('Erkläre, warum der Topfboden genauso groß sein sollte wie die Herdplatte.', 2, 'Ist der Topf kleiner, geht Wärme seitlich an die Luft verloren – Energie wird verschwendet und es dauert länger.'),
    ]),
    ('gadgets', [
        A('Nimm Stellung: Brauchst du einen elektrischen Spiralschneider? Nutze die Prüffragen (Häufigkeit, Alternative, Reinigung, Preis, Platz).', 3, 'z. B. eher nicht: selten benutzt, viele Teile zu reinigen, teuer, braucht Platz; ein Sparschäler schneidet auch Streifen.'),
    ]),
    ('uebungen', [
        MC('Welche Aussagen stimmen?', ['*Mit TARA wird die Waage auf null gestellt.', 'Esslöffel eignen sich gut zum Rühren.', '*Kochlöffel aus Holz schonen die Beschichtung.', '*Für geschmolzene Schokolade nimmt man eine Edelstahlschüssel.', 'Milch misst man im Messbecher in Gramm.', 'Ohne Deckel kocht Wasser schneller.']),
    ]),
]),

'04_Vorbereitung': dict(sections=[
    ('startklar', [
        L('1. [[Spültuch]] und zwei Geschirrtücher bereitlegen – 2. alle [[Zutaten]] holen – 3. alle [[Arbeitsgeräte]] bereitlegen – 4. [[Arbeitsplatz]] einrichten – 5. loslegen.'),
    ]),
    ('platz', [
        BOXES('Zeichne den Arbeitsplatz von oben für Rechts- und Linkshänder. Beschrifte Schneidebrett, Rohware, verarbeitete Ware und Abfallschale.', ['Rechtshänder', 'Linkshänder'], 38,
              loes=['vorn Schneidebrett; oben links Rohware, Mitte verarbeitete Ware, rechts Abfallschale; Arbeitsrichtung links → rechts', 'gespiegelt: oben rechts Rohware, Mitte verarbeitete Ware, links Abfallschale; Arbeitsrichtung rechts → links']),
    ]),
    ('techniken', [
        TAB('Erkläre die Vorbereitungsarbeiten und nenne ein Beispiel.', ['Arbeit', 'Was wird entfernt?', 'Beispiel'],
            [['Waschen', '[[Schmutz, Erde, Pflanzenschutzmittel]]', '[[Äpfel, Kartoffeln]]'], ['Putzen', '[[ungenießbare Teile]]', '[[Kerngehäuse der Paprika]]'], ['Schälen', '[[Schalen und Häute]]', '[[Karotte mit dem Sparschäler]]']], h=8),
        A('Begründe, warum man Gemüse vor dem Zerkleinern wäscht und beim Putzen nur so wenig wie nötig entfernt.', 2, 'Nach dem Schneiden würden Vitamine ausgeschwemmt. // Wenig entfernen vermeidet Lebensmittelverschwendung.'),
    ]),
    ('salat', [
        A('Beschreibe, wie man Blattsalat richtig wäscht.', 3, 'Schüssel mit kaltem Wasser füllen; äußere Blätter sparsam entfernen; Blätter einzeln abpflücken; welke Stellen entfernen; Blätter ins Wasser tauchen und bewegen; im Sieb abtropfen lassen; wiederholen, bis kein Schmutz mehr am Boden ist.'),
    ]),
    ('uebungen', [
        RF(['f|Salat wäscht man unter fließendem Wasser.|in stehendem Wasser', 'r|Linkshänder arbeiten von rechts nach links.', 'r|Beim Putzen werden ungenießbare Teile entfernt.', 'f|Die Abfallschale steht bei Rechtshändern links.|rechts']),
    ]),
]),

'05_Zubereitung': dict(sections=[
    ('zerkleinern', [
        TAB('Ergänze die Tabelle zum Zerkleinern.', ['Technik', 'Ergebnis', 'Beispiel'],
            [['hobeln', '[[Scheiben]]', '[[Gurkensalat]]'], ['raspeln', '[[grobe, unregelmäßige Streifen]]', '[[Karottensalat]]'], ['reiben', '[[sehr feine Streifen, Mus]]', '[[Zitronenschale, Käse]]'], ['hacken', '[[fein zerkleinert]]', '[[Kräuter, Nüsse]]'], ['pürieren', '[[einheitliche Masse]]', '[[Suppe, Apfelmus]]'], ['passieren', '[[durch ein Sieb gedrückt]]', '[[Kartoffelbrei]]']], h=7),
    ]),
    ('mischen', [
        ZU('Ordne Technik und Beispiel zu.', ['rühren', 'schlagen', 'kneten', 'mixen'], ['Hefeteig', 'Smoothie', 'Rührteig', 'Sahne'], loes=[3, 4, 1, 2]),
    ]),
    ('unterheben', [
        A('Erkläre den Unterschied zwischen Rühren und Unterheben am Beispiel von Eischnee.', 3, 'Beim Rühren werden Zutaten kräftig vermischt – die Luftbläschen im Eischnee platzen, die Masse fällt zusammen, der Kuchen wird fest. // Beim Unterheben wird der Eischnee vorsichtig mit Teigschaber untergezogen – die Luft bleibt erhalten, der Kuchen wird locker.'),
    ]),
    ('zuordnen', [
        SORT('Ordne die Techniken.', ['hobeln', 'rühren', 'raspeln', 'kneten', 'pürieren', 'unterheben', 'hacken', 'schlagen'], ['Zerkleinern', 'Mischen'], loes=[['hobeln', 'raspeln', 'pürieren', 'hacken'], ['rühren', 'kneten', 'unterheben', 'schlagen']]),
    ]),
    ('uebungen', [
        A('Vergleiche das Schlagen von Sahne mit dem Schneebesen und mit dem Handrührgerät.', 2, 'Schneebesen: anstrengend, dauert länger, aber gut kontrollierbar. Handrührgerät: schnell und kraftsparend, Gefahr, dass die Sahne zu Butter wird.'),
    ]),
]),

'06_Messer': dict(sections=[
    ('aufbau', [
        BOX('Zeichne ein Messer und beschrifte Griff, Klinge, Schneide und Messerrücken.', 30, loes='Griff hinten; Klinge vorn mit geschärfter Schneide (unten) und stumpfem Messerrücken (oben); Spitze vorn.'),
    ]),
    ('messer', [
        TAB('Wofür verwendet man diese Messer?', ['Messer', 'Verwendung'],
            [['Gemüsemesser', '[[Putzen von Obst und Gemüse]]'], ['Sparschäler', '[[sparsames Schälen]]'], ['großes Kochmesser', '[[große, harte Lebensmittel; hacken]]'], ['Brotmesser', '[[Brot, Kuchen (grober Wellenschliff)]]'], ['Tomatenmesser', '[[Tomaten (feiner Wellenschliff)]]'], ['Wiegemesser', '[[Kräuter und Nüsse hacken]]']], h=7, widths=[30, 70]),
    ]),
    ('griffe', [
        A('Beschreibe den Krallengriff und den Tunnelgriff. Wann verwendet man welchen?', 4, 'Krallengriff (zum Schneiden in Scheiben): Finger bilden eine Kralle, Fingerspitzen nach innen, das Messer gleitet an den Knöcheln entlang, die Hand wandert nach hinten. // Tunnelgriff (zum Halbieren und Vierteln): Die Hand bildet über dem Lebensmittel einen Tunnel, das Messer wird hindurchgeführt.'),
    ]),
    ('regeln', [
        A('Nenne vier Regeln für den sicheren Umgang mit Messern.', 2, 'nie mit dem Messer laufen; immer auf dem Brett schneiden; zum Weitergeben ablegen; fallende Messer nie auffangen; nicht ins Spülbecken legen.'),
    ]),
    ('uebungen', [
        A('Begründe, warum man mit einem scharfen Messer sicherer arbeitet als mit einem stumpfen.', 2, 'Mit einem stumpfen Messer braucht man mehr Druck; es rutscht leichter ab und man verletzt sich.'),
    ]),
]),

'07_Garverfahren_feucht': dict(sections=[
    ('verfahren', [
        L('Garen ist das Zubereiten von Lebensmitteln unter [[Wärmeeinwirkung]]. Bei feuchter Hitze wird immer eine [[Flüssigkeit]] verwendet.'),
        TAB('Ergänze die Tabelle.', ['Garverfahren', 'Temperatur', 'Flüssigkeit', 'Beispiel'],
            [['Kochen', '[[100 °C]]', '[[viel]]', '[[Nudeln]]'], ['Garziehen', '[[75–95 °C]]', '[[viel]]', '[[Knödel]]'], ['Quellen', '[[75–95 °C]]', '[[wird ganz aufgenommen]]', '[[Reis]]'], ['Dünsten', '[[95–100 °C]]', '[[wenig, oft mit Fett]]', '[[Gemüse]]'], ['Dämpfen', '[[100 °C]]', '[[Wasserdampf]]', '[[Kartoffeln]]'], ['Druckgaren', '[[bis 120 °C]]', '[[Dampf unter Druck]]', '[[Linsen]]']], h=7),
    ]),
    ('naehrstoffe', [
        TAB('Karotten-Versuch: Notiere eure Beobachtungen.', ['', 'Kochen', 'Dünsten', 'Dämpfen'], [['Farbe', '', '', ''], ['Biss', '', '', ''], ['Geschmack', '', '', '']], h=9),
        INFO('Lösungshinweis: Gedünstete und gedämpfte Karotten sind farbintensiver, bissfester und aromatischer; beim Kochen gehen mehr Vitamine und Geschmack ins Wasser.'),
    ]),
    ('druck', [
        A('Nenne drei Sicherheitsregeln für den Dampfdrucktopf.', 2, 'mindestens ¼ l Wasser einfüllen; Dichtungsring prüfen und Deckel richtig schließen; erst öffnen, wenn der Druckanzeiger ganz unten ist.'),
    ]),
    ('zuordnen', [
        ZU('Welches Garverfahren passt?', ['Spaghetti', 'Kartoffelknödel', 'Reis', 'Brokkoli im Siebeinsatz'], ['Quellen', 'Dämpfen', 'Kochen', 'Garziehen'], loes=[3, 4, 1, 2]),
    ]),
    ('uebungen', [
        A('Erkläre, warum Würstchen garziehen und nicht kochen sollten.', 2, 'Bei sprudelndem Kochen (100 °C) platzen die Würstchen auf; beim Garziehen bei 75–95 °C bleiben sie ganz und saftig.'),
    ]),
]),

'08_Garverfahren_trocken': dict(sections=[
    ('verfahren', [
        TAB('Ergänze die Tabelle.', ['Garverfahren', 'Temperatur', 'Beispiel'],
            [['Braten', '[[120–200 °C, heißes Fett]]', '[[Schnitzel, Spiegelei]]'], ['Schmoren', '[[ca. 200 °C, dann 100 °C in Flüssigkeit]]', '[[Gulasch, Rouladen]]'], ['Grillen', '[[200–300 °C]]', '[[Grillgemüse]]'], ['Backen', '[[150–250 °C, heiße Luft]]', '[[Kuchen, Pizza]]'], ['Frittieren', '[[ca. 160–180 °C, schwimmend in Fett]]', '[[Pommes frites]]']], h=7),
    ]),
    ('ofen', [
        A('Vergleiche die Backofenprogramme Ober-/Unterhitze und Umluft.', 3, 'Ober-/Unterhitze: Hitze von oben und unten, nur ein Blech, vorheizen. // Umluft: Ventilator verteilt heiße Luft, mehrere Bleche, nicht vorheizen, 20–30 °C weniger – spart Energie.'),
    ]),
    ('fett', [
        A('Beschreibe, was passiert, wenn man Fleisch in kaltes bzw. in heißes Fett legt.', 3, 'Kaltes Fett: Es zischt nicht, Saft tritt aus, das Fleisch wird grau und zäh. // Heißes Fett: Es zischt, die Oberfläche bräunt sofort, Röststoffe entstehen, das Fleisch bleibt saftig.'),
    ]),
    ('video', [
        A('Nenne die acht Schritte zur Erstellung eines Erklärvideos.', 3, '1. Vorüberlegungen, 2. Informationen einholen, 3. Drehbuch schreiben, 4. Filmen, 5. Schneiden, 6. Vertonen/Untertiteln, 7. Film beurteilen, 8. Veröffentlichen.'),
        A('Begründe, warum Datenschutz und Urheberrecht beim Veröffentlichen eingehalten werden müssen.', 2, 'Personen haben ein Recht am eigenen Bild (DSGVO); fremde Musik und Bilder sind geschützt – Verstöße können teuer werden.'),
    ]),
    ('uebungen', [
        SORT('Feuchte oder trockene Hitze?', ['Kochen', 'Braten', 'Dämpfen', 'Grillen', 'Quellen', 'Backen', 'Dünsten', 'Frittieren'], ['feuchte Hitze', 'trockene Hitze'], loes=[['Kochen', 'Dämpfen', 'Quellen', 'Dünsten'], ['Braten', 'Grillen', 'Backen', 'Frittieren']]),
    ]),
]),

'09_Planung_Rezept': dict(sections=[
    ('aufgaben', [
        TAB('Nenne je zwei Arbeiten.', ['Vorbereitungsarbeiten', 'Zubereitungsarbeiten', 'Aufräumarbeiten', 'sonstige Arbeiten'],
            [['[[Tücher bereitlegen]]', '[[garen]]', '[[spülen]]', '[[Tisch decken]]'], ['[[Lebensmittel waschen]]', '[[abschmecken]]', '[[Herd reinigen]]', '[[Boden kehren]]']], h=9),
    ]),
    ('zeitplan', [
        A('Erkläre, warum ein Arbeitsplan Zeit spart.', 2, 'Die Reihenfolge ist durchdacht; Wartezeiten (Wasser erhitzen, Soße köcheln) werden für andere Arbeiten genutzt; Aufgaben sind im Team verteilt – am Ende ist alles gleichzeitig fertig.'),
    ]),
    ('rezept', [
        A('Ein Rezept ist für 4 Personen: 400 g Nudeln, 500 ml passierte Tomaten. Berechne die Mengen für 6 Personen.', 2, 'Faktor 6 : 4 = 1,5 // 600 g Nudeln, 750 ml passierte Tomaten'),
    ]),
    ('methode', [
        ZU('Was bedeuten die Abkürzungen?', ['EL', 'TL', 'Msp.', 'Pr.', 'Bd.'], ['Bund', 'Teelöffel', 'Prise', 'Esslöffel', 'Messerspitze'], loes=[5, 2, 4, 1, 3]),
    ]),
    ('spuelen', [
        A('Beschreibe, wie man richtig von Hand spült.', 3, 'Geschirr neben das Spülbecken stellen, Speisereste entfernen; warmes, stehendes Wasser mit wenig Spülmittel; Reihenfolge Gläser – Besteck – Teller – Geräte – Töpfe; Schüsseln mit Öffnung nach unten abtropfen lassen; mit sauberem Tuch abtrocknen.'),
    ]),
    ('uebungen', [
        BOX('Erstelle einen Arbeitsplan für „Nudeln mit Tomatensoße“ (Zeit, Arbeitsschritt, wer?).', 40, loes='z. B. 0 min Arbeitsplatz einrichten (alle) – 5 min Wasser aufsetzen (A) – 7 min Zwiebel schneiden (B) – 12 min Soße andünsten (B) – 17 min spülen (A), Soße köchelt – 22 min Nudeln ins Wasser, Tisch decken (C) – 32 min anrichten (alle).'),
    ]),
]),

'10_Wiederholung': dict(ichkann=True, sections=[
    ('begriffe', [
        ZU('Ordne zu.', ['Chefkochprobe', 'Not-Aus-Schalter', 'Krallengriff', 'Garziehen', 'Umluft'],
           ['Fingerspitzen nach innen', 'nicht vorheizen, 20–30 °C weniger', 'abschmecken mit zwei Löffeln', 'garen bei 75–95 °C', 'schaltet den Strom ab'], loes=[3, 5, 1, 4, 2]),
    ]),
    ('fall', [
        A('Fallbeispiel: Du kochst in der Ferienwohnung eine Gemüselasagne. Erläutere, worauf du achtest (Hygiene, Arbeitsgeräte, Vor- und Zubereitung, Garverfahren).', 6, 'Küche erkunden (Geräte, Löschdecke/Deckel); Hände waschen, Schmuck ab; Arbeitsplatz einrichten; Gemüse waschen, putzen, schneiden (Krallen-/Tunnelgriff, Auflageschnitt); Gemüse andünsten, Soße köcheln; Lasagne backen (Umluft ca. 20–30 °C weniger); Wartezeit zum Spülen und Tischdecken nutzen; mit Chefkochprobe abschmecken.'),
    ]),
    ('quiz-st', [
        RF(['r|Einen Fettbrand erstickt man mit einem Deckel.', 'f|Reis wird gekocht, bis das Wasser abgegossen wird.|Reis quillt; die Flüssigkeit wird vollständig aufgenommen.', 'r|Das Tomatenmesser hat einen feinen Wellenschliff.', 'f|Aufräumarbeiten macht man erst ganz am Ende.|Schon während der Wartezeiten aufräumen.']),
    ]),
]),
}
