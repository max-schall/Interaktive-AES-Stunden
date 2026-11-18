from render import *

WS = {
'01_Schoenheitsideale': dict(sections=[
    ('wandel', [
        A('Beschreibe, wie sich Schönheitsideale im Lauf der Zeit verändert haben (mindestens zwei Epochen).', 3, 'Mittelalter/Barock: runde Körperformen = Fruchtbarkeit und Wohlstand, blasse Haut. // 1960er: sehr schlanke Models. // Heute (westlich): schlank und sportlich, Muskeln, verbreitet über soziale Medien.'),
    ]),
    ('einfluss', [
        A('Nenne sechs Faktoren, die beeinflussen, was wir schön finden.', 2, 'Kultur/Tradition, Alter, Religion, Medien, Idole, Geschlecht, Selbstbild, Zeitgeist, Familie, Peergroup.'),
    ]),
    ('filter', [
        A('Erkläre, warum der Vergleich mit Bildern in sozialen Medien unzufrieden machen kann.', 3, 'Die Bilder sind ausgewählt, gefiltert, retuschiert – so sieht niemand wirklich aus. Wer sich daran misst, findet sich selbst schlechter; Folgen können unnötige Diäten oder OPs sein.'),
    ]),
    ('meinung', [
        A('Nimm Stellung: „Bearbeitete Fotos in der Werbung sollten gekennzeichnet werden.“', 3, 'Individuell begründet, z. B. pro: Ehrlichkeit, Schutz junger Menschen; kontra: schwer zu kontrollieren.'),
    ]),
    ('uebungen', [
        A('Nenne drei Tipps, wie man sich im eigenen Körper wohlfühlen kann.', 2, 'ausgewogen essen und bewegen; nicht mit Models vergleichen; sich von Medien nicht negativ beeinflussen lassen; eigenen Stil entwickeln.'),
    ]),
]),

'02_Mode_Trends': dict(sections=[
    ('ausdruck', [
        L('[[Mode]] ist ein für einen bestimmten Zeitraum geltender [[Trend]]. Mit Kleidung zeigen wir unsere [[Zugehörigkeit]] zu Gruppen, Kulturen oder Religionen. Mode kann das [[Selbstwertgefühl]] stärken.'),
        ZU('Was zeigt die Kleidung?', ['Tracht', 'Kippa', 'Fan-Trikot', 'Uniform'], ['Beruf, Funktion', 'religiöse Zugehörigkeit', 'Tradition, Herkunft', 'Verein'], loes=[3, 2, 4, 1]),
    ]),
    ('anlass', [
        A('Beschreibe ein passendes Outfit für ein Vorstellungsgespräch und begründe.', 2, 'z. B. saubere Hose, Hemd/Bluse, ordentliche Schuhe – wirkt seriös und zeigt Respekt.'),
    ]),
    ('trendsetter', [
        A('Erkläre „Menschen formen Mode, Mode formt Menschen“.', 3, 'Trendsetter (Influencer, Prominente) setzen Trends. Viele übernehmen sie, um dazuzugehören – Mode beeinflusst so Lebens- und Denkweise und führt oft zu mehr Konsum als nötig.'),
    ]),
    ('meinung', [
        A('Welchen Modetrends folgst du? Beschreibe dein Verhalten.', 2, 'Individuell.'),
    ]),
    ('uebungen', [
        RF(['r|Mode ist eine Momentaufnahme.', 'f|Kleidung zeigt heute vor allem die Gesellschaftsschicht.|vor allem Geschmack und Persönlichkeit', 'r|Trends kommen oft wieder.']),
    ]),
]),

'03_Bodymodification': dict(sections=[
    ('arten', [
        TAB('Unterscheide.', ['', 'temporär', 'permanent'], [['Bedeutung', '[[vorübergehend]]', '[[dauerhaft]]'], ['Beispiele', '[[Frisur, Make-up, Bräune]]', '[[Tattoo, Piercing, Schönheits-OP]]'], ['Folgen', '[[keine Narben, muss wiederholt werden]]', '[[schwer rückgängig, oft Narben]]']], h=9),
    ]),
    ('kulturen', [
        A('Nenne zwei Beispiele für Körpergestaltung in anderen Kulturen und ihre Bedeutung.', 2, 'Maori-Tattoos: Herkunft und Status; Henna in Indien: Schmuck zu Festen; Ohrpflöcke oder Halsringe: Zugehörigkeit.'),
    ]),
    ('check', [
        A('Nenne vier Fragen, die man sich vor einem Tattoo stellen sollte.', 2, 'Gefällt mir das Motiv auch in 20 Jahren? Entscheide ich selbst? Ist das Studio seriös und hygienisch? Kenne ich die Risiken? Wie wirkt es im Beruf? Bin ich volljährig/sind die Eltern einverstanden?'),
    ]),
    ('prokontra', [
        TAB('Pro und Kontra Bodymodification', ['Pro', 'Kontra'], [['[[Ausdruck der Persönlichkeit, Erinnerung, Zugehörigkeit]]', '[[kaum rückgängig, Entzündungen, Allergien, Geschmack ändert sich, Kosten]]']], h=20),
    ]),
    ('uebungen', [
        A('Nimm Stellung: „Tattoo mit 16 – eine gute Idee?“', 3, 'Individuell begründet.'),
    ]),
]),

'04_Kleidung_Funktionen': dict(sections=[
    ('funktionen', [
        TAB('Erkläre die Funktionen und gib je ein Beispiel.', ['Funktion', 'Erklärung', 'Beispiel'], [['Scham und Schutz', '[[bedeckt, schützt vor Wetter und Gefahren]]', '[[Regenjacke, Feuerwehranzug]]'], ['Schmuck', '[[Selbstdarstellung, Selbstwertgefühl]]', '[[Lieblingsoutfit, Ohrringe]]'], ['Kennzeichnung', '[[zeigt Zugehörigkeit]]', '[[Uniform, Fan-Trikot, Tracht]]']], h=9),
    ]),
    ('zwiebel', [
        BOXES('Zeichne das Zwiebelprinzip und beschrifte die drei Schichten mit ihrer Aufgabe.', ['Schicht 1', 'Schicht 2', 'Schicht 3'], 28, loes=['Feuchtigkeitsregulierung (Funktionsshirt)', 'Wärme (Fleece, Wolle)', 'Wetterschutz: Regen, Wind (atmungsaktive Jacke)']),
    ]),
    ('funktionell', [
        A('Nenne vier Tragefunktionen funktioneller Kleidung.', 2, 'wasser- und winddicht, atmungsaktiv, thermoregulierend, angenehm zur Haut, gute Passform, Bewegungsfreiheit.'),
    ]),
    ('beruf', [
        A('Nenne drei Berufe mit Berufskleidung und erkläre ihre Funktion.', 2, 'Feuerwehr (Schutz vor Hitze), Klinik (Hygiene), Polizei (Kennzeichnung), Straßenbau (Warnfarbe).'),
    ]),
    ('uebungen', [
        A('Erkläre, warum man beim Wandern mehrere dünne Schichten statt eines dicken Pullis trägt.', 2, 'Man kann sich flexibel an Wetter und Anstrengung anpassen (Schichten aus- und anziehen); Funktionsschichten leiten Schweiß ab, die äußere schützt vor Wind und Regen.'),
    ]),
]),

'05_Diaeten': dict(sections=[
    ('formen', [
        TAB('Ergänze die Formen der Reduktionsdiät.', ['Form', 'Merkmal', 'Bewertung'], [['energiereduzierte Mischkost', '[[mäßig weniger Kalorien, alles erlaubt]]', '[[empfehlenswert]]'], ['Low Carb / Low Fat', '[[bestimmte Nährstoffe gemieden]]', '[[oft einseitig]]'], ['Monodiät', '[[nur bestimmte Lebensmittel]]', '[[Mangel, Jo-Jo]]'], ['Crashdiät', '[[stark reduzierte Energie]]', '[[Jo-Jo, Muskelverlust]]']], h=7),
    ]),
    ('jojo', [
        A('Erkläre den Jo-Jo-Effekt.', 3, 'Bei stark reduzierter Kalorienzufuhr senkt der Körper den Grundumsatz („Hungermodus“). Isst man danach wieder normal, wird mehr Energie gespeichert – man nimmt schnell wieder zu, oft über das Ausgangsgewicht.'),
    ]),
    ('check', [
        A('Prüfe das Werbeversprechen „5 kg in 7 Tagen mit der Ananas-Diät“ mit den drei Kriterien einer sinnvollen Diät.', 3, 'nicht alltagstauglich (einseitig, nicht durchzuhalten), nicht nährstoffdeckend (Mangel), nicht nachhaltig (Jo-Jo-Effekt) – unseriös.'),
    ]),
    ('bmi', [
        A('Erkläre, warum der BMI bei einem muskulösen Sportler nicht aussagekräftig ist.', 2, 'Der BMI berücksichtigt die Körperzusammensetzung nicht: Muskeln sind schwer – der Sportler hat einen hohen BMI, ohne übergewichtig zu sein.'),
    ]),
    ('uebungen', [
        A('Diskutiere, warum viele Jugendliche eine Diät machen, obwohl sie normalgewichtig sind.', 3, 'Schönheitsideal „schlank“, Vergleich mit Medien und Influencern, Druck der Peergroup, Unzufriedenheit mit dem eigenen Körper.'),
    ]),
]),

'06_Essstoerungen': dict(sections=[
    ('was', [
        A('Erkläre, was eine Essstörung ist.', 2, 'Eine ernsthafte Erkrankung, bei der der Umgang mit Essen und das Verhältnis zum Körper gestört sind; sie wirkt auf Körper und Seele und muss behandelt werden.'),
    ]),
    ('merkmale', [
        TAB('Ordne Merkmale zu.', ['Magersucht', 'Bulimie', 'Binge-Eating'], [['[[Untergewicht, verzerrte Körperwahrnehmung, Angst vor Zunahme]]', '[[Essanfälle, Erbrechen, Abführmittel, Scham]]', '[[Essanfälle ohne Hunger, kein Sättigungsgefühl, Übergewicht]]']], h=24),
    ]),
    ('umgang', [
        A('Beschreibe, wie du reagierst, wenn dir bei einer Freundin ein auffälliges Essverhalten auffällt.', 3, 'In Ruhe unter vier Augen ansprechen, beschreiben, was mir aufgefallen ist; Verständnis zeigen, keine Vorwürfe; behutsam zu Hilfe motivieren; selbst eine Vertrauensperson einweihen.'),
    ]),
    ('hilfe', [
        A('Nenne drei Hilfsangebote für Betroffene und Angehörige.', 2, 'Schulsozialarbeit, BZgA-Infotelefon Essstörungen, Haus- oder Jugendarzt, Beratungsstellen, Selbsthilfegruppen, Nummer gegen Kummer 116 111.'),
    ]),
    ('uebungen', [
        RF(['f|Essstörungen gehen von allein vorbei.|Sie müssen behandelt werden.', 'r|Auch Jungen und Männer können betroffen sein.', 'r|Bei Bulimie ist das Gewicht oft normal.']),
    ]),
]),

'07_Schoenheit_Ansicht': dict(sections=[
    ('wolke', [
        A('Beschreibe, was für dich Schönheit bedeutet.', 2, 'Individuell.'),
    ]),
    ('innen', [
        TAB('Äußere und innere Schönheit', ['äußere Schönheit', 'innere Schönheit'], [['[[Aussehen, Körperbau, Kleidungsstil, Frisur]]', '[[Charakter, Lachen, Ehrlichkeit, Hilfsbereitschaft, Humor]]']], h=18),
    ]),
    ('identitaet', [
        A('Erkläre, welche Einflüsse bei der Entwicklung der eigenen Identität eine Rolle spielen.', 3, 'Vorgaben der Eltern, gesellschaftliche Normen, Freunde und Peergroup, Medien; man probiert Verhalten, Auftreten und Aussehen aus.'),
    ]),
    ('komplimente', [
        A('Nenne einen Menschen, den du schön findest, und erkläre warum – ohne sein Aussehen zu beschreiben.', 2, 'Individuell.'),
    ]),
    ('uebungen', [
        A('Erkläre die Aussage „Wahre Schönheit kommt von innen“.', 2, 'Schönheit zeigt sich auch im Charakter und in der Ausstrahlung; wer sich selbst mag und ein gesundes Selbstvertrauen hat, wirkt schön.'),
    ]),
]),

'08_Wiederholung': dict(ichkann=True, sections=[
    ('begriffe', [
        ZU('Ordne zu.', ['Jo-Jo-Effekt', 'Bodymodification', 'Zwiebelprinzip', 'Trendsetter', 'subjektiv'], ['persönliche Wahrnehmung', 'Person, die Trends vorgibt', 'mehrere dünne Schichten', 'dauerhafte Körpergestaltung', 'Gewichtszunahme nach Diät'], loes=[5, 4, 3, 2, 1]),
    ]),
    ('fall', [
        A('Leonie fühlt sich nach dem Scrollen durch Fitness- und Beauty-Accounts schlecht und überlegt, eine Crashdiät zu machen. Gib ihr begründete Ratschläge.', 5, 'Bilder sind bearbeitet; Accounts entfolgen, die nicht guttun; keine Crashdiät (Jo-Jo, Mangel); ausgewogen essen und bewegen; Zeit mit Freunden und Hobbys; bei Sorgen mit Vertrauensperson sprechen.'),
    ]),
    ('quiz-st', [
        RF(['r|Schönheitsideale verändern sich mit der Zeit.', 'f|Ein Piercing ist temporär.|permanent', 'r|Fanbekleidung hat eine Kennzeichnungsfunktion.', 'f|Monodiäten sind empfehlenswert.|Sie sind einseitig.']),
    ]),
]),
}
