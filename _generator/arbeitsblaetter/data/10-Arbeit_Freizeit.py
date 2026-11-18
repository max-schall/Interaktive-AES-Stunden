from render import *

WS = {
'01_Freizeit': dict(sections=[
    ('budget', [
        L('[[Freizeit]] ist die Zeit, in der eine Person nicht arbeiten muss und keine besonderen [[Verpflichtungen]] hat.'),
        TAB('Mein Schultag', ['Tätigkeit', 'Stunden'], [['Schlaf', ''], ['Schule', ''], ['Hausaufgaben', ''], ['Wege', ''], ['Essen, Körperpflege', ''], ['Pflichten', ''], ['Freizeit (24 h minus Summe)', '']], h=7),
    ]),
    ('funktionen', [
        A('Nenne je zwei Freizeitaktivitäten, die der Gesundheit, der Ruhe und Entspannung und sozialen Kontakten dienen.', 3, 'Gesundheit: Fußball, Schwimmen; Ruhe: Yoga, Lesen; soziale Kontakte: Freunde treffen, Spieleabend.'),
    ]),
    ('typ', [
        A('Beschreibe dein Freizeitverhalten. Welcher Freizeittyp bist du?', 3, 'Individuell.'),
    ]),
    ('zeitfresser', [
        A('Nenne drei Zeitfresser und je eine Gegenstrategie.', 3, 'Trödeln bei Hausaufgaben – zügig erledigen; Handy – Bildschirmzeit begrenzen; Aufschieben – Wochenplan mit To-dos; Haushalt allein – Aufgaben teilen.'),
    ]),
    ('uebungen', [
        A('Begründe, warum zu viele Freizeitaktivitäten krank machen können.', 2, 'Freizeitstress: keine Zeit zum Abschalten, Schlafmangel, Druck – wirkt wie ein stressiger Alltag.'),
    ]),
]),
'02_Naehmaschine': dict(sections=[
    ('sicher', [
        A('Nenne fünf Sicherheitsregeln an der Nähmaschine.', 3, 'Not-Aus kennen, Haare zusammenbinden, Ketten ablegen, Ärmel hochkrempeln, Kabel keine Stolperfallen, Maschine sicher hinstellen, Verletzung sofort melden.'),
    ]),
    ('teile', [
        TAB('Teile der Nähmaschine', ['Teil', 'Funktion'], [['Nähfuß', '[[drückt den Stoff auf die Stichplatte]]'], ['Handrad', '[[bewegt die Nadel von Hand (zu dir hin)]]'], ['Rückwärtsnähtaste', '[[zum Rückwärtsnähen/Verriegeln]]'], ['Garnrollenhalter', '[[hält die Garnrolle]]'], ['Sticheinstellungsrad', '[[wählt die Stichart]]']], h=8),
    ]),
    ('stiche', [
        L('Der [[Steppstich]] ist der wichtigste Stich zum Zusammennähen. Der [[Zick-Zack-Stich]] dient zum Versäubern. Die [[Stichlänge]] ist der Abstand der Einstiche, die [[Stichbreite]] die seitliche Bewegung der Nadel.'),
        A('Erkläre das Verriegeln.', 1, 'Naht am Anfang und Ende sichern: 2–3 Stiche vorwärts, dann mit der Rückwärtstaste auf der gleichen Stelle zurück.'),
    ]),
    ('probe', [
        BOX('Zeichne eine gerade Linie, eine Zackenlinie und eine Wellenlinie als Vorlage für deine Nähprobe auf Papier.', 40, loes='Individuell.'),
    ]),
    ('uebungen', [
        MC('Worauf übst du die ersten Nähte?', ['*auf Papier', 'auf dem Lieblingsshirt', 'auf Leder', 'auf dem Tisch']),
    ]),
]),
'03_Kreativ': dict(sections=[
    ('hobbys', [
        A('Erkläre, warum eine kreative Freizeitbeschäftigung sinnvoll sein kann.', 2, 'Entspannung, innere Ruhe, Talente entdecken (auch für die Berufsorientierung), Selbstgemachtes, oft nachhaltig.'),
    ]),
    ('techniken', [
        L('Textile Kulturtechniken sind z. B. [[Weben]], Stricken, Nähen, Häkeln, [[Knüpfen]] und [[Filzen]].'),
    ]),
    ('makramee', [
        A('Beschreibe, wie ein Kreuzknoten beim Makramee-Schlüsselanhänger geknüpft wird.', 3, 'Rechter Arbeitsfaden vorne über die Innenfäden nach links, linker Faden hinten herum nach vorne durch die Schlaufe, festziehen; nächster Knoten spiegelverkehrt.'),
    ]),
    ('diy', [
        BOX('Plane ein eigenes DIY-Projekt: Skizze, Material, Arbeitsschritte.', 45, loes='Individuell.'),
    ]),
    ('uebungen', [
        A('Erläutere den Zusammenhang deines DIY-Projekts mit der Nachhaltigkeit.', 2, 'z. B. alte Materialien weiterverwenden (Ökologie), Geld sparen (Ökonomie), Geschenk/gemeinsam basteln (Soziales).'),
    ]),
]),
'04_Arbeitsformen': dict(sections=[
    ('formen', [
        L('Arbeit ist eine körperliche und/oder [[geistige]] Tätigkeit, die die eigene [[Existenz]] sichert.'),
    ]),
    ('zuordnen', [
        TAB('Arbeitsformen', ['Form', 'bezahlt?', 'freiwillig?', 'Beispiel'], [['Erwerbsarbeit', '[[ja]]', '[[nein]]', '[[Beruf]]'], ['Hausarbeit', '[[nein]]', '[[nein]]', '[[putzen]]'], ['Familienarbeit', '[[nein]]', '[[nein]]', '[[Kinder betreuen]]'], ['Ehrenamt', '[[nein]]', '[[ja]]', '[[Feuerwehr]]']], h=8),
    ]),
    ('lohn', [
        A('Erkläre, welche Entlohnung es außer Geld geben kann.', 1, 'Anerkennung, Wertschätzung, Lob, ein schönes Zuhause, Freude am Gemeinwohl.'),
    ]),
    ('wandel', [
        A('Beschreibe, wie sich das Rollenbild „Hausfrau und Mutter“ verändert hat, und begründe.', 3, 'Die meisten Frauen arbeiten heute in Teil- oder Vollzeit; Haus- und Familienarbeit wird auf alle verteilt. Gründe: Gleichberechtigung, Ausbildung, finanzielle Sicherheit.'),
    ]),
    ('uebungen', [
        A('Diskutiere, warum ein Ehrenamt auch ohne Bezahlung einen Mehrwert hat.', 2, 'Für mich: Erfahrung, Kontakte, Anerkennung, Kompetenzen. Für die Gesellschaft: Hilfe, Zusammenhalt.'),
    ]),
]),
'05_Work_Life_Balance': dict(sections=[
    ('waage', [
        L('Work-Life-Balance beschreibt das [[Gleichgewicht]] zwischen Arbeit und [[Privatleben]].'),
    ]),
    ('tage', [
        A('Vergleiche die Tagesabläufe von Mia und Tom und beurteile ihre Work-Life-Balance.', 4, 'Mia: ruhiges Frühstück, Mittagspause, pünktlich Feierabend, Sport, Abend in Gesellschaft – ausgeglichen. Tom: Frühstück im Stehen, Essen am Schreibtisch, lange Arbeit, Akten vor dem TV – unausgeglichen, Burn-out-Gefahr.'),
    ]),
    ('faktoren', [
        SORT('Kraftquelle oder Stolperstein?', ['Freunde', 'Pendeln', 'Sport', 'Multitasking', 'Schlaf', 'Freizeitstress'], ['Kraftquelle', 'Stolperstein'], loes=[['Freunde', 'Sport', 'Schlaf'], ['Pendeln', 'Multitasking', 'Freizeitstress']]),
    ]),
    ('tipps', [
        A('Nenne vier Tipps für eine gute Work-Life-Balance.', 2, 'Erreichbare Ziele, Pausen, Erholung, Familie und Freunde treffen, Sport/Kreativität, Nein sagen.'),
    ]),
    ('uebungen', [
        A('Beschreibe deinen gestrigen Tag als Tagebucheintrag und beurteile deine Work-Life-Balance.', 4, 'Individuell.'),
    ]),
]),
'06_Wiederholung': dict(ichkann=True, sections=[
    ('begriffe', [
        ZU('Ordne zu.', ['Ehrenamt', 'Burn-out', 'DIY', 'Verriegeln', 'Freizeit'], ['Naht sichern', 'völlige Erschöpfung', 'mach es selbst', 'freiwillig fürs Gemeinwohl', 'Zeit ohne Verpflichtungen'], loes=[4, 2, 3, 1, 5]),
    ]),
    ('fall', [
        A('Tara ist gestresst und hat keine Zeit für Freundinnen. Erarbeite Ratschläge für sie.', 4, 'Hausarbeit im Familienrat fair verteilen, Wochenplan mit Pausen, feste Treffen, Hobby mit Bewegung/Tieren/Kreativität (z. B. Nachbarshund ausführen, Nähprojekt).'),
    ]),
    ('quiz-st', [
        RF(['r|Freizeit dient dem Stressausgleich.', 'f|Hausarbeit ist Erwerbsarbeit.|unbezahlt', 'r|Der Zick-Zack-Stich versäubert Kanten.', 'f|Work-Life-Balance ist für alle gleich.|individuell']),
    ]),
]),
}
