from render import *

WS = {
'01_Familie_Haushalt': dict(sections=[
    ('formen', [
        TAB('Familienformen', ['Familienform', 'Wer lebt zusammen?'], [['Kernfamilie', '[[Kind(er) mit Mutter und Vater]]'], ['Ein-Eltern-Familie', '[[Kind(er) mit einem Elternteil]]'], ['Patchworkfamilie', '[[Kinder haben nicht alle die gleichen Eltern]]'], ['Regenbogenfamilie', '[[gleichgeschlechtliche Eltern mit Kind(ern)]]'], ['Pflege-/Adoptivfamilie', '[[Kind(er) bei Pflege- bzw. Adoptiveltern]]']], h=8),
    ]),
    ('wandel', [
        L('Die klassische Vater-Mutter-Kind-Familie macht 2022 nur noch rund [[60]] % der Familien aus. Etwa [[20]] % der Familien sind [[alleinerziehend]].'),
    ]),
    ('funktionen', [
        SORT('Ordne die Aufgaben den Funktionen des Haushalts zu.', ['Einkommen beschaffen', 'Werte vermitteln', 'Geborgenheit', 'Kinderwunsch erfüllen', 'Finanzen planen', 'Erholung'], ['ökonomisch', 'Sozialisierung', 'Regeneration', 'Reproduktion'], loes=[['Einkommen beschaffen', 'Finanzen planen'], ['Werte vermitteln'], ['Geborgenheit', 'Erholung'], ['Kinderwunsch erfüllen']]),
    ]),
    ('bedeutung', [
        A('Beschreibe, welche Bedeutung ein Haushalt a) für die einzelnen Familienmitglieder und b) für die Gesellschaft hat.', 4, 'a) Schutzraum, Wohlbefinden, Geborgenheit, Versorgung, Erholung, Betreuung und Pflege. // b) Werte, Normen und Traditionen werden weitergegeben, Kinder in die Gesellschaft eingegliedert, das Fortbestehen der Gesellschaft gesichert.'),
    ]),
    ('uebungen', [
        A('Erläutere den Begriff Kernfamilie und nenne Vor- und Nachteile einer anderen Familienform.', 3, 'Kernfamilie: Kind(er) leben mit Mutter und Vater. Beispiel Mehrgenerationenfamilie: Vorteile – gegenseitige Hilfe, Betreuung durch Großeltern; Nachteile – wenig Platz, mehr Konflikte.'),
    ]),
]),
'02_Geschlechterrollen': dict(sections=[
    ('geschichte', [
        L('Artikel [[3]] des Grundgesetzes: „Männer und Frauen sind [[gleichberechtigt]].“ 1958 trat das Gesetz über die Gleichberechtigung in Kraft. Heute regeln die Ehegatten die [[Haushaltsführung]] im gegenseitigen Einvernehmen (§ 1356 BGB).'),
    ]),
    ('teilzeit', [
        TAB('Teilzeitarbeit', ['Vorteile', 'Nachteile'], [['[[mehr Zeit für Kinder und Familie]]', '[[geringeres Einkommen]]'], ['[[Pflege von Angehörigen möglich]]', '[[geringere Rente]]'], ['[[weniger Doppelbelastung]]', '[[schlechtere Karrierechancen]]']], h=8),
    ]),
    ('armut', [
        A('Erkläre den Begriff Mütterarmut und erläutere, warum vor allem Alleinerziehende von Armut betroffen sind.', 4, 'Mütterarmut: Mütter sind häufiger von Armut betroffen, v. a. im Alter. Gründe: Teilzeit, ungleiche Bezahlung, geringere Karrierechancen, schlechte Vereinbarkeit – dadurch geringere Rentenbeiträge. // Alleinerziehende haben nur ein Einkommen, arbeiten oft in Teilzeit und tragen die Kosten für die Kinder allein.'),
    ]),
    ('staat', [
        A('Nenne vier Leistungen der sozialen Sicherung in Deutschland.', 2, 'Kindergeld, Elterngeld/Elternzeit, Kitaplatz ab einem Jahr, Bürgergeld, Wohngeld, BAföG, Bildungspaket.'),
        A('Erläutere den Begriff Gender-Mainstreaming.', 1, 'Politische Strategien zur Förderung der Gleichstellung von Frauen und Männern.'),
    ]),
    ('uebungen', [
        A('Beschreibe einen Beruf, der als „typisch“ für ein Geschlecht gilt, und begründe deine Meinung dazu.', 3, 'Individuell, z. B. Erzieherin/Kfz-Mechatroniker: Rollenbilder, Vorbilder; heute stehen alle Berufe allen offen (Girls’ Day, Boys’ Day).'),
    ]),
]),
'03_Arbeitsteilung': dict(sections=[
    ('rollen', [
        A('Beschreibe, warum die Hausarbeit heute auf alle Familienmitglieder verteilt werden muss.', 2, 'In vielen Familien arbeiten beide Eltern, um Geld zu verdienen. Um Beruf und Haushalt zu vereinbaren, muss die Arbeit auf alle verteilt werden.'),
    ]),
    ('kinder', [
        A('Erläutere § 1619 BGB in eigenen Worten.', 2, 'Kinder, die bei den Eltern wohnen und von ihnen versorgt werden, müssen im Haushalt mithelfen – so, wie es ihrem Alter und ihren Kräften entspricht.'),
        A('Nenne fünf altersgerechte Hausarbeiten für Jugendliche.', 2, 'Zimmer sauber halten, Staub saugen, einkaufen, kochen, Geschirrspüler ausräumen, Müll wegbringen, Bad putzen, Wäsche waschen, auf Geschwister aufpassen.'),
    ]),
    ('plan', [
        BOX('Erstelle einen Wochen-Haushaltsplan für deine Familie: Aufgaben, Tage, Zuständige.', 50, loes='Individuell: Aufgaben mit Zeitbedarf, Zuständigen und Tagen; gerecht und altersgerecht verteilt.'),
    ]),
    ('planung', [
        A('Nenne vier Fragen, die man vor dem Erstellen eines Haushaltsplans klären sollte.', 3, 'Welche Aufgaben fallen täglich, wöchentlich, monatlich an? Wie viel Zeit brauchen sie? Wer kann oder will was übernehmen? Welche Zeiten sind durch Schule, Arbeit, Hobbys blockiert? Welche Geräte können helfen?'),
    ]),
    ('uebungen', [
        A('Ermittle zwei Zeitfresser in deinem Haushalt und mache Verbesserungsvorschläge.', 3, 'Individuell, z. B. Wäsche sortieren – Wäschekorb je Farbe; Spülen von Hand – Geschirrspüler; Suchen – feste Plätze.'),
    ]),
]),
'04_Wohnen': dict(sections=[
    ('anzeige', [
        A('Beschreibe, welche Informationen eine Wohnungsanzeige enthält und welche oft fehlen.', 3, 'Enthalten: Zimmerzahl, Wohnfläche, Kaltmiete, Lage, Bezugstermin, Kontakt. // Fehlen oft: Höhe der Nebenkosten, Kaution, Ausstattung (Küche, Bad), Etage, Heizungsart.'),
    ]),
    ('begriffe', [
        ZU('Ordne zu.', ['Kaltmiete', 'Nebenkosten', 'Kaution', 'Mietspiegel', 'Budget'], ['Übersicht über die ortsübliche Miete', 'zur Verfügung stehende Geldmittel', 'Miete nur für den Wohnraum', 'Sicherheit beim Mieten', 'Müllabfuhr, Abwasser, Heizung'], loes=[4, 5, 1, 3, 2]),
    ]),
    ('budget', [
        TAB('Mein Monatsbudget', ['Posten', 'Betrag in €'], [['Einnahmen', ''], ['Kaltmiete', ''], ['Nebenkosten', ''], ['Strom, Internet, Handy', ''], ['Mobilität', ''], ['Lebensmittel', ''], ['Freizeit, Kleidung', ''], ['Rest', '']], h=7),
    ]),
    ('zukunft', [
        A('Skizziere, wie du dir dein Leben in 10–15 Jahren vorstellst (Wohnen, Arbeit, Familie, Hobbys).', 4, 'Individuell.'),
    ]),
    ('uebungen', [
        A('Erläutere die Zusammenhänge zwischen Haushaltssituation und Konsum.', 2, 'Das Budget begrenzt den Konsum: Hohe feste Kosten (Miete) lassen wenig Geld für Freizeit, Kleidung oder Sparen. Wer günstiger wohnt (WG), hat mehr Spielraum.'),
    ]),
]),
'05_Kinder_foerdern': dict(sections=[
    ('spiel', [
        L('Spielformen sind z. B. [[Konstruktionsspiele]], [[Rollenspiele]], [[Regelspiele]], Bewegungsspiele und Wettkampfspiele. Die Bewegung fördert die [[motorische]] und die kognitive Entwicklung.'),
    ]),
    ('sortieren', [
        TAB('Spielformen', ['Spielform', 'Beispiel', 'Was wird gelernt?'], [['Konstruktionsspiel', '[[Lego, Sandburg]]', '[[Feinmotorik, Kreativität]]'], ['Rollenspiel', '[[Kaufladen]]', '[[Sprache, Einfühlung]]'], ['Regelspiel', '[[Memory, Uno]]', '[[Regeln, verlieren können]]'], ['Bewegungsspiel', '[[Klettern]]', '[[Gleichgewicht, Kraft]]'], ['Wettkampfspiel', '[[Sackhüpfen]]', '[[Fairness, Teamarbeit]]']], h=8),
    ]),
    ('phasen', [
        A('Erkläre, was es heißt, Kinder zu fördern und zu fordern.', 2, 'Kinder entsprechend ihrer Entwicklungsstufe herausfordern, ohne sie dauerhaft zu über- oder unterfordern; Üben und Wiederholen, Anbahnen der nächsten Stufe.'),
    ]),
    ('gefuehle', [
        A('Beschreibe, wie du reagierst, wenn ein Kleinkind einen Wutanfall hat.', 2, 'Ruhig bleiben, beim Kind bleiben, nicht nachgeben und nicht schimpfen; später über die Gefühle sprechen und andere Verhaltensmöglichkeiten besprechen.'),
    ]),
    ('alter', [
        A('Beschreibe zwei Möglichkeiten, wie Jugendliche älteren Menschen im Alltag oder in der Freizeit helfen können.', 2, 'Einkaufen, Handy/Computer erklären, gemeinsam spielen oder spazieren gehen, vorlesen, Besuche im Seniorenheim, Mehrgenerationenhaus.'),
    ]),
    ('uebungen', [
        BOX('Plane eine Spielestunde für Kindergartenkinder oder für Seniorinnen und Senioren: Spiele, Material, Ablauf.', 40, loes='Individuell, z. B. Bewegungsspiel zum Aufwärmen, Regelspiel (Memory), kreatives Konstruktionsspiel, ruhiger Abschluss.'),
    ]),
]),
'06_Vielfalt_Konflikte': dict(sections=[
    ('beduerfnisse', [
        A('Analysiere, welche unterschiedlichen Bedürfnisse Kinder, Jugendliche, Berufstätige und alte Menschen haben.', 4, 'Kinder: Fürsorge, Spiel, feste Abläufe. Jugendliche: Selbstständigkeit, Freunde, Privatsphäre. Berufstätige: Entlastung, Pausen, wenig freie Zeit. Alte Menschen: Hilfe, Gesellschaft, Ruhe, möglichst viel Selbstständigkeit.'),
    ]),
    ('ich', [
        A('Formuliere die Du-Botschaft „Du räumst nie die Küche auf!“ als Ich-Botschaft.', 2, 'z. B. „Ich ärgere mich, wenn die Küche unaufgeräumt ist. Ich wünsche mir, dass wir sie gemeinsam aufräumen.“'),
    ]),
    ('konflikt', [
        L('Konflikte lösen: 1. die eigene Sichtweise mit [[Ich-Botschaften]] erklären, 2. die Sichtweise des Gegenübers [[nachvollziehen]], 3. [[Lösungen]] vorschlagen, 4. [[Kompromisse]] machen und sich einigen.'),
    ]),
    ('vielfalt', [
        A('Erläutere die Begriffe Diversität und Inklusion in eigenen Worten.', 3, 'Diversität: Vielfalt; Anerkennung und Wertschätzung aller Menschen unabhängig von Herkunft, Geschlecht, Alter, Religion, Behinderung … // Inklusion: Jeder Mensch ist Teil der Gesellschaft, niemand wird ausgeschlossen.'),
    ]),
    ('uebungen', [
        A('Beschreibe einen Konflikt aus deinem Alltag und formuliere eine Lösung mithilfe der vier Schritte.', 4, 'Individuell.'),
    ]),
]),
'07_Berufe': dict(sections=[
    ('felder', [
        L('Berufsfelder rund um AES: Gesundheit und [[Pflege]], Ernährung und [[Hauswirtschaft]], Fitness und [[Bewegung]] sowie [[Sozialwesen]].'),
    ]),
    ('bilder', [
        TAB('Berufsbilder', ['Beruf', 'Tätigkeit', 'Voraussetzung'], [['Fachkraft Fruchtsafttechnik', '[[Säfte aus Obst und Gemüse herstellen]]', '[[technisches Verständnis]]'], ['Kinderkrankenpflege', '[[kranke Kinder pflegen und betreuen]]', '[[Einfühlungsvermögen]]'], ['Hörakustiker/-in', '[[Hörsysteme anpassen, beraten]]', '[[handwerkliches Geschick]]'], ['Pflanzentechnologe/-in', '[[Pflanzen züchten und vermehren]]', '[[Interesse an Pflanzen]]']], h=9),
    ]),
    ('check', [
        A('Beschreibe deine Interessen und Stärken. Welcher Beruf rund um AES könnte zu dir passen? Begründe.', 4, 'Individuell.'),
    ]),
    ('zitate', [
        A('Nenne zwei Wege, wie du einen Beruf näher kennenlernen kannst.', 1, 'Praktikum, BIZ der Agentur für Arbeit, Berufsmesse, Berufe-Portale (z. B. planet-beruf.de), Gespräche mit Berufstätigen.'),
    ]),
    ('uebungen', [
        BOX('Steckbrief: Recherchiere einen weiteren Beruf im Bereich AES (Tätigkeiten, Voraussetzungen, Ausbildungsdauer, Perspektiven).', 45, loes='Individuell, z. B. Erzieher/-in: Kinder betreuen und fördern; Einfühlungsvermögen, Geduld; 3–5 Jahre (je nach Weg); Leitung, Studium Soziale Arbeit.'),
    ]),
]),
'08_Wiederholung': dict(ichkann=True, sections=[
    ('begriffe', [
        ZU('Ordne zu.', ['Patchworkfamilie', 'Mütterarmut', 'Kaution', 'Ich-Botschaft', 'Inklusion'], ['Sicherheit beim Mieten', 'niemand wird ausgegrenzt', 'Kinder haben nicht alle die gleichen Eltern', 'Gefühle ohne Vorwurf äußern', 'Armut durch Teilzeit und geringe Rente'], loes=[3, 5, 1, 4, 2]),
    ]),
    ('fall', [
        TAB('Meleks Budget (Einnahmen 950 €)', ['Posten', 'Betrag'], [['feste Ausgaben (Miete, NK, Strom, Handy, Fahrkarte, Versicherungen)', '[[400 €]]'], ['frei verfügbar', '[[550 €]]'], ['variable Ausgaben', '[[270 €]]'], ['Rest zum Sparen', '[[280 €]]']], h=8),
        A('Fitnessstudio: Jahresvertrag 25 €/Monat oder Halbjahresvertrag 35 €/Monat. Erläutere Vor- und Nachteile.', 3, 'Jahresvertrag: 300 € im Jahr, günstiger pro Monat, aber 12 Monate gebunden. Halbjahr: 210 € für 6 Monate, teurer pro Monat, aber flexibler.'),
    ]),
    ('quiz-st', [
        RF(['r|Kinder sind zur Mithilfe im Haushalt verpflichtet.', 'f|Mit der Kaltmiete sind alle Wohnkosten bezahlt.|nur der Wohnraum', 'r|Alleinerziehende haben ein hohes Armutsrisiko.', 'f|Elternzeit gibt es nur für Mütter.|für jeden Elternteil']),
    ]),
]),
}
