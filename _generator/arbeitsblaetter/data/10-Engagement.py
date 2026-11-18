from render import *

WS = {
'01_Ehrenamt': dict(sections=[
    ('ehrenamt', [
        L('Unter einem Ehrenamt versteht man [[freiwillige]], [[unentgeltliche]] Arbeit im [[gemeinnützigen]] Bereich. In Deutschland engagieren sich rund [[30 Millionen]] Menschen.'),
    ]),
    ('active', [
        A('Erkläre die Begriffe Active Citizenship und Empathie.', 3, 'Active Citizenship: aktive Bürgerschaft – soziales und politisches Engagement für das Gemeinwohl. // Empathie: Einfühlungsvermögen, Gefühle und Lebensumstände anderer verstehen.'),
    ]),
    ('finder', [
        A('Nenne Bereiche, in denen du dich engagieren könntest, und begründe mit deinen Stärken.', 3, 'Individuell, z. B. Sport (Trainerassistenz), Soziales (Tafel), Umwelt (Müllsammelaktion), Rettung (Jugendfeuerwehr).'),
    ]),
    ('lde', [
        A('Beschreibe ein Beispiel für Service Learning aus dem AES-Unterricht.', 2, 'z. B. Wissen über Kinderentwicklung bei einem Spiele- und Bastelnachmittag in der Kita einbringen; Lebensmittel retten bei der Tafel.'),
    ]),
    ('uebungen', [
        TAB('Einrichtung in unserer Gemeinde', ['Name', 'Ziel', 'Zielgruppe', 'Ansprechperson'], [['', '', '', ''], ['', '', '', '']], h=10),
    ]),
]),
'02_Projektmethode': dict(sections=[
    ('phasen', [
        TAB('Die drei Phasen', ['Phase', 'Schritte'], [['1. Planung', '[[Thema, Ziele, Meilensteine, Arbeits- und Zeitplan]]'], ['2. Durchführung', '[[Informationen beschaffen, Dokumentation, Abschlusspräsentation]]'], ['3. Bewertung', '[[Präsentation und Gesamtprojekt bewerten, Protokoll]]']], h=9),
    ]),
    ('kochbuch', [
        A('Erkläre den Begriff Meilenstein an einem Beispiel aus dem Kochbuch-Projekt.', 2, 'Wichtiger Zeitpunkt im Projekt, z. B. „Bis Ende KW 3 sind alle Rezepte ausgewählt und nachgekocht.“'),
    ]),
    ('planer', [
        TAB('Unser Arbeits- und Zeitplan', ['Aufgabe', 'Wer?', 'Bis wann?', 'erledigt'], [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']], h=8),
    ]),
    ('vierk', [
        L('Die 4 K: [[Kommunikation]], [[Kollaboration]] (Teamwork), [[kritisches Denken]] und [[Kreativität]].'),
    ]),
    ('uebungen', [
        A('Diskutiere die Aussage „In Projekten lernen wir fürs Leben!“.', 3, 'Individuell: Teamarbeit, Verantwortung, Zeitmanagement, Präsentieren, Problemlösen – Kompetenzen, die in Beruf und Alltag wichtig sind.'),
    ]),
]),
'03_Projektideen': dict(sections=[
    ('ideen', [
        ZU('Ordne zu.', ['Upcycling', 'Lebensmittelabfälle', 'Präventionstag', 'Fair-Trade-Point'], ['Waren auf Kommission vom Weltladen', 'Tasche aus alter Jeans', 'Resterezepte und Foodsharing', 'Expertinnen und Experten einladen'], loes=[4, 1, 2, 3]),
    ]),
    ('abfall', [
        A('Berechne: Wie viele kg Lebensmittel werfen 25 Personen im Jahr weg (78 kg pro Kopf)? Wie viel wäre es bei einer Halbierung?', 2, '25 × 78 kg = 1.950 kg; halbiert: 975 kg.'),
    ]),
    ('life', [
        A('Nenne vier Life Skills nach der WHO.', 2, 'Selbstwahrnehmung, Empathie, kreatives und kritisches Denken, Entscheidungen treffen, Problemlösen, Kommunikation, Beziehungsfähigkeit, Gefühls- und Stressbewältigung.'),
    ]),
    ('auswahl', [
        BOX('Unser Projekt: Titel, Ziel, drei Meilensteine, benötigte Partner.', 50, loes='Individuell.'),
    ]),
    ('uebungen', [
        A('Begründe, welches der vier Projekte am besten zu eurer Schule passt.', 3, 'Individuell.'),
    ]),
]),
'04_Schwerpunkt_Ernaehrung_Gesundheit': dict(sections=[
    ('biografie', [
        A('Beschreibe deine Essbiografie: Wie hat sich dein Geschmack verändert, und wer oder was hat dich geprägt?', 4, 'Individuell; innere Faktoren (Hunger, Gefühle) und äußere Faktoren (Familie, Herkunft, Freunde, Werbung).'),
    ]),
    ('rundgang', [
        A('Nenne vier Merkmale einer nachhaltigen und gesunden Ernährung.', 2, 'vollwertig (DGE), pflanzenbetont, regional, saisonal, bio, wenig Fleisch, wenig Verschwendung.'),
    ]),
    ('faktoren', [
        SORT('Einflussfaktoren auf die Gesundheit', ['Ernährung', 'Alter', 'Bewegung', 'Erbanlagen', 'Schlaf', 'Geschlecht'], ['beeinflussbar', 'kaum beeinflussbar'], loes=[['Ernährung', 'Bewegung', 'Schlaf'], ['Alter', 'Erbanlagen', 'Geschlecht']]),
    ]),
    ('mythen', [
        A('Nimm Stellung: „Bio-Produkte sind immer regional.“', 2, 'Falsch: Bio beschreibt die Erzeugung, nicht die Herkunft; Bio-Ware kann weit transportiert sein.'),
    ]),
    ('uebungen', [
        A('Erstelle eine Liste mit Präventionsmaßnahmen für Jugendliche.', 3, 'Ausgewogen essen, viel trinken, Bewegung, genug Schlaf, Impfungen und Vorsorge, Stressmanagement, Bildschirmzeit begrenzen, auf Alkohol und Nikotin verzichten.'),
    ]),
]),
'05_Schwerpunkt_Konsum_Leben': dict(sections=[
    ('kauf', [
        A('Wähle ein Produkt, das du gern kaufen möchtest. Beschreibe, wie Werbung deine Auswahl beeinflusst hat, und nenne drei Qualitätskriterien.', 4, 'Individuell.'),
    ]),
    ('rechte', [
        TAB('Meine Rechte', ['Recht', 'Dauer', 'gilt bei …'], [['Gewährleistung', '[[2 Jahre]]', '[[Mangel, gegenüber dem Händler]]'], ['Garantie', '[[freiwillig, z. B. 3 Jahre]]', '[[Bedingungen des Herstellers]]'], ['Widerruf', '[[14 Tage]]', '[[Online-Kauf, auch ohne Mangel]]']], h=8),
    ]),
    ('rundgang', [
        A('Stelle dar, welche Auswirkungen dein Kauf weltweit haben kann.', 3, 'Arbeitsbedingungen und Löhne in Produktionsländern, Rohstoff- und Wasserverbrauch, Transport und CO₂, Müll; Fair Trade und langlebige Produkte verbessern die Bilanz.'),
    ]),
    ('zukunft', [
        BOX('Mein Zukunfts-Zeitstrahl: Arbeit, Wohnen, Familie, Freizeit.', 45, loes='Individuell.'),
    ]),
    ('uebungen', [
        A('Beurteile, ob deine Work-Life-Balance derzeit ausgeglichen ist.', 3, 'Individuell.'),
    ]),
]),
'06_Abschluss': dict(ichkann=True, sections=[
    ('begriffe', [
        ZU('Ordne zu.', ['Krallengriff', 'Resilienz', 'Fast Fashion', 'Health Claims', 'Ehrenamt'], ['gesundheitsbezogene Werbeaussagen', 'seelische Widerstandskraft', 'freiwillige Arbeit fürs Gemeinwohl', 'sichere Haltung beim Schneiden', 'billige Mode im schnellen Wechsel'], loes=[4, 2, 5, 1, 3]),
    ]),
    ('quiz-st', [
        RF(['r|Fett liefert pro Gramm die meiste Energie.', 'f|Die Notrufnummer in Europa ist 911.|112', 'r|Online-Käufe kann man 14 Tage widerrufen.', 'f|Nahrungsergänzungsmittel sind Arzneimittel.|Lebensmittel']),
    ]),
    ('fall', [
        A('Mara (19) wohnt in einer WG und macht eine Ausbildung. Gib ihr drei Tipps aus dem AES-Unterricht für Ernährung, Finanzen und Zusammenleben.', 4, 'Ernährung: vollwertig frühstücken, keine NEM nötig. Finanzen: Haushaltsbuch, Privathaftpflicht, Rücklagen. Zusammenleben: Putzplan, Ich-Botschaften, Kompromisse.'),
    ]),
]),
}
