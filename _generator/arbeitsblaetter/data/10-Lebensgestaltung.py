from render import *

WS = {
'01_Wohnformen': dict(sections=[
    ('formen', [
        TAB('Wohnformen', ['Wohnform', 'Vorteil', 'Nachteil'], [['bei der Familie', '[[spart Geld, Freunde in der Nähe]]', '[[wenig Selbstständigkeit]]'], ['Wohngemeinschaft', '[[günstig, nicht allein]]', '[[Kompromisse, wenig Ruhe]]'], ['Wohnheim', '[[oft am günstigsten]]', '[[Wartelisten, unordentlich]]'], ['Untermiete', '[[möbliert, zum Testen]]', '[[nur auf Zeit]]'], ['eigene Wohnung', '[[Privatsphäre]]', '[[alle Kosten allein]]']], h=8),
    ]),
    ('abwaegen', [
        A('Nenne zwei Regeln, die in einer WG das Zusammenleben erleichtern.', 2, 'Haushaltsplan mit fester Aufgabenteilung, Ruhezeiten, gemeinsame Haushaltskasse, regelmäßige WG-Besprechung.'),
    ]),
    ('finder', [
        A('Werte aus, welche Wohnform zu deinen Ansprüchen passt, und begründe.', 3, 'Individuell.'),
    ]),
    ('wer', [
        A('Diskutiere, wann es sinnvoll ist, eine Wohnung oder ein Haus zu kaufen.', 2, 'Wenn genug Eigenkapital vorhanden ist, das Einkommen sicher ist und man lange am Ort bleiben möchte; Nebenkosten (Notar, Grunderwerbsteuer) bedenken.'),
    ]),
    ('uebungen', [
        BOX('Erstelle eine Mindmap zum Thema „So will ich wohnen“.', 45, loes='Individuell: Lage, Größe, Kosten, allein/gemeinsam, Ausstattung, Mobilität, Nachhaltigkeit.'),
    ]),
]),
'02_Finanzen': dict(sections=[
    ('buch', [
        A('Erkläre, was ein Haushaltsbuch ist, und begründe, warum es beim Finanzmanagement hilft.', 3, 'Gegenüberstellung von Einnahmen und Ausgaben (Hand, PC, App). Man sieht, wofür man wie viel ausgibt, erkennt unnötige Ausgaben und kleine Geldfresser und kann Schulden vermeiden.'),
    ]),
    ('sparen', [
        TAB('50:30:20 bei 1.200 € Einkommen', ['Anteil', 'wofür?', 'Betrag'], [['50 %', '[[Fixkosten]]', '[[600 €]]'], ['30 %', '[[Wünsche]]', '[[360 €]]'], ['20 %', '[[Rücklage]]', '[[240 €]]']], h=8),
    ]),
    ('kredit', [
        L('Bei einem [[Kredit]] wird Geld für eine festgelegte [[Laufzeit]] geliehen. Zurückgezahlt werden der Betrag plus [[Zinsen]] in monatlichen [[Raten]].'),
    ]),
    ('schulden', [
        A('Stelle den Unterschied zwischen Verschuldung und Überschuldung dar und nenne je ein Beispiel für gute und schlechte Schulden.', 4, 'Verschuldet: Geld geliehen, kann aber fristgerecht zurückzahlen. Überschuldet: kann nicht mehr fristgerecht zurückzahlen. // Gut: Roller für den Weg zur Ausbildung, Weiterbildung. Schlecht: Smartphone auf Raten, Urlaub auf Kredit.'),
    ]),
    ('uebungen', [
        A('Überlege, wo du in deinem Alltag Geld einsparen kannst.', 2, 'Individuell, z. B. Getränke von zu Hause, Abos kündigen, gebraucht kaufen, Preise vergleichen.'),
    ]),
]),
'03_Versicherungen': dict(sections=[
    ('sozial', [
        L('Die fünf gesetzlichen Sozialversicherungen: [[Krankenversicherung]], [[Pflegeversicherung]], [[Rentenversicherung]], [[Arbeitslosenversicherung]] und [[Unfallversicherung]].'),
    ]),
    ('solidar', [
        A('Erkläre das Solidaritätsprinzip.', 2, 'Die Beiträge sind ein Prozentsatz des Einkommens: Wer mehr verdient, zahlt mehr. Alle haben die gleichen Ansprüche auf Leistungen – Versicherte sind auch für die anderen verantwortlich.'),
    ]),
    ('arten', [
        A('Erläutere den Unterschied zwischen gesetzlichen Sozialversicherungen und Individualversicherungen.', 3, 'Sozialversicherungen: Pflicht, Beitrag nach Einkommen, Solidaritätsprinzip. // Individualversicherungen: vertraglich, Beitrag nach persönlichem Risiko, meist freiwillig (Pflicht: Kfz-Haftpflicht).'),
    ]),
    ('faelle', [
        TAB('Wer zahlt?', ['Schaden', 'Versicherung'], [['Sturz von der Leiter bei der Arbeit', '[[gesetzliche Unfallversicherung]]'], ['Controller zerstört den Fernseher des Freundes', '[[Privathaftpflicht]]'], ['Einbruch, Laptop gestohlen', '[[Hausratversicherung]]'], ['Sturm deckt das Dach ab', '[[Gebäudeversicherung]]']], h=8),
    ]),
    ('uebungen', [
        A('Begründe, welche Individualversicherungen jede Person haben sollte, obwohl sie freiwillig sind.', 2, 'Privathaftpflicht (Schäden an anderen können existenzbedrohend teuer sein), Berufsunfähigkeitsversicherung (sichert das Einkommen).'),
    ]),
]),
'04_Flaechenkonkurrenz': dict(sections=[
    ('konflikte', [
        A('Erkläre an zwei Beispielen, was Flächen-Nutzungs-Konkurrenz bedeutet.', 3, 'Verschiedene Nutzungen konkurrieren um begrenzte Fläche, z. B. Mais für Biogas statt Nahrung; Neubaugebiet statt Wiese; Baumwolle statt Lebensraum am Aralsee.'),
    ]),
    ('fleisch', [
        A('Erläutere, was Flächen-Nutzungs-Konkurrenz mit Fleischkonsum zu tun hat.', 3, 'Für Futtermittel und Weiden wird viel Fläche gebraucht (in Deutschland ca. 60 % der Agrarfläche); 1 kg Rindfleisch braucht ein Vielfaches der Fläche pflanzlicher Lebensmittel. Dafür werden z. B. Regenwälder gerodet.'),
    ]),
    ('landgrabbing', [
        A('Erkläre, was Landgrabbing ist und welche Folgen es hat.', 3, 'Investoren aus Industrieländern kaufen große Flächen in Entwicklungsländern für Exportlandwirtschaft. Die Bevölkerung verliert Lebensraum und Lebensgrundlage, Armut und Hunger nehmen zu.'),
    ]),
    ('meinung', [
        A('Nimm Stellung: „Mais sollte nicht für Biogasanlagen angebaut werden.“', 3, 'Individuell; Pro: Fläche für Nahrung, Monokulturen; Kontra: erneuerbare Energie, Einkommen für Landwirte.'),
    ]),
    ('uebungen', [
        A('Beschreibe, wofür die Flächen an deinem Wohnort genutzt werden.', 2, 'Individuell.'),
    ]),
]),
'05_Gemeinsam_konsumieren': dict(sections=[
    ('angebote', [
        A('Erkläre den Begriff gemeinschaftlicher Konsum und nenne seine Ziele.', 3, 'Dinge werden von mehreren Personen genutzt: leihen, tauschen, mieten, teilen. Ziele: weniger Neuproduktion, längere Nutzung, Geld, Ressourcen und Umwelt schonen.'),
    ]),
    ('sortieren', [
        ZU('Ordne zu.', ['Bibliothek der Dinge', 'Tauschbörse', 'Repaircafé', 'Carsharing'], ['Toaster reparieren lassen', 'Auto für den Großeinkauf', 'Bohrmaschine ausleihen', 'Jacke gegen Jacke'], loes=[3, 4, 1, 2]),
    ]),
    ('auto', [
        A('Erörtere Vor- und Nachteile von Carsharing und Fahrgemeinschaften.', 3, 'Vorteile: günstiger bei wenig Fahrten, weniger Autos und Parkplätze, Umwelt. // Nachteile: nicht immer verfügbar, Planung nötig, auf dem Land wenig Angebote, Abhängigkeit von anderen.'),
    ]),
    ('kauf', [
        A('Nenne zwei Dinge, die du lieber leihen als kaufen solltest, und begründe.', 2, 'z. B. Anzug für den Abschlussball, Zelt, Werkzeug: selten genutzt, teuer, braucht Platz.'),
    ]),
    ('uebungen', [
        A('Beurteile, ob Carsharing für deine Familie sinnvoll wäre.', 3, 'Individuell: Wohnort, Angebot, Fahrleistung, Kosten.'),
    ]),
]),
'06_Wiederholung': dict(ichkann=True, sections=[
    ('begriffe', [
        ZU('Ordne zu.', ['Untermiete', 'Fixkosten', 'Überschuldung', 'Solidaritätsprinzip', 'Landgrabbing'], ['Landraub in Entwicklungsländern', 'regelmäßige Kosten', 'Beitrag nach Einkommen, gleiche Leistungen', 'vom Mieter gemietet', 'nicht fristgerecht zurückzahlen können'], loes=[5, 2, 4, 1, 3]),
    ]),
    ('fall', [
        A('Nila und Kai ziehen zusammen. Stelle die Kosten zusammen, die auf sie zukommen, und erkläre, worauf sie bei den Finanzen achten sollten.', 4, 'Kaution, Umzug, Einrichtung; monatlich Miete, Nebenkosten, Strom, Internet, Versicherungen (Haftpflicht, Hausrat), Lebensmittel, Mobilität. // Haushaltsbuch, Rücklagen (50:30:20), keine Konsumkredite.'),
        A('Erläutere, wie die beiden ihr Leben nachhaltig gestalten können.', 3, 'Secondhand-Möbel, Werkzeug leihen, Repaircafé, Carsharing/ÖPNV/Rad statt zwei Autos, nicht zu große Wohnung.'),
    ]),
    ('quiz-st', [
        RF(['r|Das Wohnheim ist oft die günstigste Wohnform.', 'f|Die Privathaftpflicht ist Pflicht.|freiwillig', 'r|Bei einem Kredit zahlt man Zinsen.', 'f|Kartoffeln brauchen mehr Fläche als Rindfleisch.|viel weniger']),
    ]),
]),
}
