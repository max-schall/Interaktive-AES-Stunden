from render import *

WS = {
'01_Gesundheit': dict(sections=[
    ('who', [
        A('Erläutere die WHO-Definition von Gesundheit mit eigenen Worten.', 3, 'Gesundheit ist mehr als „nicht krank sein“: Man muss sich körperlich, seelisch und sozial wohlfühlen – alle drei Bereiche gehören dazu.'),
    ]),
    ('kontinuum', [
        L('Die [[Salutogenese]] sieht Gesundheit nicht als Zustand, sondern als [[Prozess]]. Zwischen gesund und krank gibt es einen [[fließenden]] Übergang.'),
        BOX('Zeichne die Linie zwischen „krank“ und „gesund“ und markiere, wo du heute stehst. Begründe.', 18, loes='Individuell: Linie mit Markierung und Begründung.'),
    ]),
    ('kohaerenz', [
        TAB('Erkläre die drei Bereiche des Kohärenzgefühls.', ['Bereich', 'Bedeutung'], [['Verstehbarkeit', '[[Das eigene Leben ist verständlich und strukturiert.]]'], ['Bewältigbarkeit', '[[Zuversicht, Anforderungen meistern zu können]]'], ['Sinnhaftigkeit', '[[Das Leben ist sinnvoll, es lohnt sich, sich anzustrengen.]]']], h=9, widths=[28, 72]),
    ]),
    ('faktoren', [
        A('Erkläre, wie nach der Salutogenese auch ein Mensch mit einer chronischen Krankheit seine Gesundheit verbessern kann.', 3, 'Gesundheit ist ein Prozess: Durch Wissen über die Krankheit, Bewältigung (z. B. Therapie, Sport) und Sinn im Leben kann man sich Richtung „gesund“ bewegen – z. B. Lea mit Diabetes, die Handball spielt.'),
    ]),
    ('uebungen', [
        RF(['f|Gesundheit bedeutet nur, keine Krankheit zu haben.|körperliches, seelisches und soziales Wohlbefinden', 'r|Salutogenese bedeutet „Entstehung von Gesundheit“.', 'r|Körperliche und seelische Gesundheit beeinflussen sich gegenseitig.']),
    ]),
]),

'02_Einfluesse': dict(sections=[
    ('modell', [
        BOX('Zeichne das Schichtenmodell der Einflussfaktoren auf die Gesundheit (von innen nach außen) und beschrifte es.', 40, loes='innen: Alter, Geschlecht, Erbanlagen – individuelle Lebensführung – soziale Netzwerke – Lebens- und Arbeitsbedingungen – außen: ökonomische, kulturelle und Umweltbedingungen'),
    ]),
    ('hand', [
        SORT('Kann ich das beeinflussen?', ['Bewegung', 'Alter', 'Ernährung', 'Erbanlagen', 'Rauchen', 'Klima', 'Schlaf', 'Krieg im Land'], ['beeinflussbar', 'kaum beeinflussbar'], loes=[['Bewegung', 'Ernährung', 'Rauchen', 'Schlaf'], ['Alter', 'Erbanlagen', 'Klima', 'Krieg im Land']]),
    ]),
    ('lebensfuehrung', [
        A('Nenne je drei Verhaltensweisen, die die Gesundheit stärken bzw. schwächen.', 3, 'stärken: Bewegung, ausgewogene Ernährung, genug Schlaf, Freundschaften // schwächen: Rauchen, Alkohol, Bewegungsmangel, zu viel Bildschirmzeit, Dauerstress'),
    ]),
    ('welt', [
        A('Erkläre an einem Beispiel, wie Lebens- und Arbeitsbedingungen die Gesundheit beeinflussen.', 2, 'z. B. Kinderarbeit in einer Textilfabrik: keine Schule, schlechte Luft, Verletzungsgefahr, wenig Erholung.'),
    ]),
    ('uebungen', [
        A('Erläutere, wie individuelle Lebensführung und Gesundheit zusammenhängen.', 2, 'Mit der Lebensführung (Ernährung, Bewegung, Schlaf, Genussmittel) beeinflusst man die Gesundheit direkt – positiv wie negativ.'),
    ]),
]),

'03_Gesundheit_foerdern': dict(sections=[
    ('ressourcen', [
        L('Wertvolle Gesundheitsressourcen sind eine vollwertige [[Ernährung]], ausreichend [[Bewegung]] und gute [[soziale Kontakte]].'),
    ]),
    ('medien', [
        TAB('Folgen von Bewegungsmangel durch zu viel Mediennutzung', ['kurzfristig', 'langfristig'], [['[[Konzentrationsstörungen, Einschlafprobleme]]', '[[Übergewicht, Rückenleiden, Gelenkerkrankungen, Diabetes, Depressionen]]']], h=16),
    ]),
    ('bewegung', [
        A('Berechne, wie viele Minuten du dich gestern bewegt hast, und vergleiche mit der WHO-Empfehlung (60 Minuten).', 2, 'Individuell.'),
    ]),
    ('pause', [
        BOX('Plane eine „bewegte Pause“ für eine Woche: Notiere für jeden Tag eine Übung.', 35, loes='z. B. Mo Hampelmann, Di Schulterkreisen, Mi Wandsitz, Do Spiegelbild, Fr liegende Acht'),
    ]),
    ('uebungen', [
        A('Erstelle eine Liste mit fünf Aktivitäten, die dir guttun.', 2, 'Individuell.'),
    ]),
]),

'04_Vorsorge': dict(sections=[
    ('ebenen', [
        TAB('Ergänze die drei Ebenen der Prävention.', ['Ebene', 'Ziel', 'Beispiel'], [['primär', '[[Krankheiten verhindern]]', '[[Impfung, Zahnpflege]]'], ['sekundär', '[[Krankheiten früh erkennen]]', '[[Vorsorgeuntersuchung, Screening]]'], ['tertiär', '[[Folgen begrenzen, Rückfälle verhindern]]', '[[Reha nach Herzinfarkt]]']], h=9),
    ]),
    ('sortieren', [
        ZU('Ordne zu: primär (1), sekundär (2) oder tertiär (3)?', ['primär', 'sekundär', 'tertiär'], ['Hautkrebs-Screening', 'Fahrradhelm tragen', 'Reha nach Kreuzbandriss', 'Masernimpfung'], loes=[2, 1, 3, 1]),
    ]),
    ('kalender', [
        A('Nenne drei Vorsorgemaßnahmen, die für Jugendliche in deinem Alter wichtig sind.', 2, 'J1-Untersuchung (12–14 Jahre), Zahnarzt-Kontrolle alle 6 Monate, Impfungen prüfen (z. B. HPV, Tetanus), Sehtest.'),
    ]),
    ('alltag', [
        A('Erkläre den Unterschied zwischen Gesundheitsförderung und Prävention.', 2, 'Gesundheitsförderung umfasst alle Maßnahmen zur Erhaltung und Förderung der Gesundheit. Prävention ist ein Teil davon: Maßnahmen, um Krankheiten vorzubeugen.'),
    ]),
    ('uebungen', [
        RF(['r|Je früher eine Krankheit erkannt wird, desto größer sind oft die Heilungschancen.', 'f|Eine Reha gehört zur primären Prävention.|tertiären Prävention', 'r|Primäre Präventionsmaßnahmen beim Arzt bezahlt meist die Krankenkasse.']),
    ]),
]),

'05_Erste_Hilfe': dict(sections=[
    ('grundsaetze', [
        A('Nenne vier Grundsätze der Ersten Hilfe.', 2, 'Ruhe bewahren, Überblick verschaffen, Unfallstelle absichern, Eigensicherung geht vor, Notruf absetzen, Verletzte nicht allein lassen.'),
    ]),
    ('notruf', [
        TAB('Die W-Fragen beim Notruf 112', ['Frage', 'Beispiel'], [['Wo?', '[[Schulstraße 1, Schulküche]]'], ['Was?', '[[Schüler bewusstlos zusammengebrochen]]'], ['Wie viele?', '[[eine Person]]'], ['Welche Verletzungen?', '[[atmet nicht, Herzdruckmassage läuft]]'], ['Warten!', '[[auf Rückfragen warten, nicht auflegen]]']], h=7, widths=[28, 72]),
    ]),
    ('ablauf', [
        BOX('Zeichne ein Ablaufschema: Eine Person liegt am Boden.', 45, loes='Ansprechen/Berühren → reagiert: beruhigen, helfen // reagiert nicht: Hilfe rufen → Atmung prüfen (sehen, hören, fühlen) → atmet: stabile Seitenlage, Notruf, betreuen // atmet nicht: Notruf, Wiederbelebung 30 : 2 bis Rettungsdienst kommt'),
    ]),
    ('hdm', [
        L('Bei der Herzdruckmassage drückt man in der Mitte des Brustkorbs [[5–6]] cm tief, [[100–120]]-mal pro Minute. Im Wechsel [[30]]-mal drücken und [[2]]-mal beatmen.'),
    ]),
    ('wunden', [
        A('Erkläre die PECH-Regel und wann man sie anwendet.', 2, 'Pause, Eis, Compression, Hochlagern – bei Verletzungen an Gelenken, Knochen oder Muskeln (z. B. Verstauchung).'),
    ]),
    ('uebungen', [
        A('Beschreibe, wie du eine kleine Verbrennung an der Hand versorgst.', 1, 'Sofort mit lauwarmem, fließendem Wasser kühlen, höchstens 10 Minuten; bei größeren Verbrennungen nur steril abdecken und Notruf.'),
    ]),
]),

'06_Stress_Umfrage': dict(sections=[
    ('koerper', [
        A('Beschreibe, was bei Stress im Körper passiert.', 2, 'Adrenalin wird ausgeschüttet, Puls und Atmung beschleunigen sich, die Muskeln spannen sich an, das Gehirn wird besser durchblutet.'),
    ]),
    ('eustress', [
        TAB('Erkläre und nenne ein Beispiel.', ['', 'Erklärung', 'Beispiel'], [['Eustress', '[[positiver Stress, Herausforderung gemeistert]]', '[[schwierige Aufgabe gelöst, verliebt]]'], ['Distress', '[[negativer Dauerstress]]', '[[ständiger Streit, Dauererreichbarkeit]]']], h=10),
        A('Nenne vier Warnsignale für Dauerstress.', 1, 'Konzentrationsschwierigkeiten, Nervosität, Kopf-, Rücken- oder Bauchschmerzen, Schlafstörungen.'),
    ]),
    ('umfrage', [
        A('Nenne die fünf Schritte einer Umfrage.', 2, '1. Thema und Zielgruppe festlegen, 2. Fragebogen erstellen, 3. Durchführung, 4. Auswertung, 5. Präsentation'),
        ZU('Ordne die Fragetypen zu.', ['geschlossene Frage', 'Alternativfrage', 'Multiple Choice', 'offene Frage'], ['„Beschreibe eine Situation, die dich stresst.“', '„Was hilft dir? Sport / Musik / Freunde“', '„Wie gestresst bist du? 1 bis 5“', '„Hast du genug Pausen? Ja / Nein / Weiß nicht“'], loes=[4, 3, 1, 2]),
    ]),
    ('live', [
        BOX('Entwirf einen kurzen Fragebogen (4 Fragen, verschiedene Fragetypen) zum Thema „Stress im Schulalltag“.', 40, loes='Individuell mit mindestens einer geschlossenen, einer Alternativ-, einer Multiple-Choice- und einer offenen Frage.'),
    ]),
    ('uebungen', [
        A('Nimm Stellung: „Stress ist immer schlecht.“', 2, 'Nein: Eustress spornt an und stärkt das Selbstvertrauen. Nur Dauerstress (Distress) macht krank.'),
    ]),
]),

'07_Resilienz': dict(sections=[
    ('begriff', [
        L('[[Resilienz]] bezeichnet die seelische [[Widerstandskraft]]. Der Begriff kommt vom lateinischen resilire = [[zurückspringen]].'),
    ]),
    ('saeulen', [
        A('Nenne die sieben Säulen der Resilienz.', 2, 'Optimismus, Akzeptanz, Lösungsorientierung, Selbstwirksamkeit, Verantwortung, Bindung (Netzwerk), Zukunftsplanung.'),
    ]),
    ('schutz', [
        A('Nenne vier Schutzfaktoren, die sich positiv auf die Resilienz auswirken.', 2, 'intakte Familie, stabiler Freundeskreis, gutes Immunsystem, positiver Umgang mit Stress, ausgewogene Ernährung, Selbstwertgefühl, Vertrauen in eigene Stärken.'),
    ]),
    ('tom', [
        A('Tom hat schlechte Noten und zieht sich zurück. Diskutiere mithilfe von drei Säulen, wie er aus seinem Tief herauskommen könnte.', 4, 'Optimismus: „Im nächsten Halbjahr kann ich etwas ändern.“ // Lösungsorientierung: Lernplan, Nachhilfe. // Bindung: mit Freunden und Familie reden, Hilfe annehmen. // Zukunftsplanung: Zwischenziele setzen.'),
    ]),
    ('uebungen', [
        A('Analysiere eine herausfordernde Situation, die du gemeistert hast. Was hast du daraus gelernt?', 2, 'Individuell.'),
    ]),
]),

'08_Stress_Strategien': dict(sections=[
    ('strategien', [
        TAB('Erkläre die drei Strategien und nenne ein Beispiel.', ['Strategie', 'Vorgehen', 'Beispiel'], [['instrumentell', '[[Stressor verändern, verringern, verhindern]]', '[[Lernplan, Prioritäten setzen]]'], ['kognitiv', '[[Bewertung und Gedanken ändern]]', '[[„Eine Note ist kein Weltuntergang.“]]'], ['regenerativ', '[[sich erholen]]', '[[Sport, Musik, Schlaf]]']], h=10),
    ]),
    ('zuordnen', [
        SORT('Welche Strategie?', ['Joggen gehen', 'Handy weglegen beim Lernen', '„Ich schaffe das!“', 'früh schlafen', 'Aufgabe abgeben', 'Kopfkino vom Erfolg'], ['instrumentell', 'kognitiv', 'regenerativ'], loes=[['Handy weglegen beim Lernen', 'Aufgabe abgeben'], ['„Ich schaffe das!“', 'Kopfkino vom Erfolg'], ['Joggen gehen', 'früh schlafen']]),
    ]),
    ('gedanken', [
        A('Formuliere zu „Das schaffe ich sowieso nicht“ zwei hilfreiche Gedanken.', 2, 'z. B. „Ich fange mit dem Wichtigsten an.“ / „Ich habe schon schwierigere Arbeiten geschafft.“'),
    ]),
    ('atem', [
        L('Kastenatmung: [[4]] Sekunden einatmen – 4 Sekunden [[halten]] – 4 Sekunden [[ausatmen]] – 4 Sekunden halten.'),
    ]),
    ('uebungen', [
        A('Beschreibe eine Situation, die dich stresst, und zeige je einen Lösungsweg mit allen drei Strategien.', 4, 'Individuell.'),
    ]),
]),

'09_Beratungsstellen': dict(sections=[
    ('angebote', [
        A('Nenne vier Beratungsangebote und wobei sie helfen.', 3, 'Schulsozialarbeit (Streit, Mobbing, Schulprobleme), Nummer gegen Kummer 116 111 (anonym reden), Familienberatung (Trennung, Streit), Suchtberatung (Alkohol, Drogen, Medien), Mobbingberatung, Ernährungsberatung.'),
        L('Beratungsgespräche sind [[freiwillig]], [[vertraulich]] und [[kostenlos]].'),
    ]),
    ('mobbing', [
        A('Erkläre, was Mobbing ist, und beschreibe, was du tust, wenn du Mobbing beobachtest.', 3, 'Negative Handlungen gegen eine Person über einen längeren Zeitraum, auch online (Cybermobbing). // Nicht mitmachen, nicht weiterleiten, Beweise sichern, Lehrkraft oder Schulsozialarbeit informieren, Betroffene unterstützen.'),
    ]),
    ('welche', [
        ZU('Welche Stelle hilft?', ['Schulsozialarbeit', 'Suchtberatung', 'Familienberatung', 'Nummer gegen Kummer'], ['nachts anonym reden wollen', 'Eltern trennen sich', 'Streit mit einer Lehrkraft', 'kann nicht aufhören zu zocken'], loes=[4, 3, 1, 2]),
    ]),
    ('meinung', [
        A('Diskutiere die Aussage: „Es ist mir peinlich, über meine Probleme zu sprechen.“', 3, 'Verständlich, aber: Beratung ist vertraulich, Fachleute kennen solche Probleme; Hilfe holen ist ein Zeichen von Stärke; allein wird es oft schlimmer.'),
    ]),
    ('uebungen', [
        A('Notiere drei Fragen, die du bei einer Beratung stellen würdest.', 2, 'Individuell, z. B. „Was kann ich selbst tun?“, „Wer erfährt davon?“, „Wie geht es weiter?“'),
    ]),
]),

'10_Wiederholung': dict(ichkann=True, sections=[
    ('begriffe', [
        ZU('Ordne zu.', ['Salutogenese', 'Resilienz', 'Eustress', 'PECH', 'tertiäre Prävention'], ['positiver Stress', 'Reha nach Unfall', 'Gesundheit als Prozess', 'Pause, Eis, Compression, Hochlagern', 'seelische Widerstandskraft'], loes=[3, 5, 1, 4, 2]),
    ]),
    ('fall', [
        A('Samira hat eine stressige Prüfungswoche. Gib ihr Tipps mit den drei Stress-Strategien und nenne eine Gesundheitsressource.', 4, 'instrumentell: Wochenplan mit Prioritäten; kognitiv: hilfreiche Gedanken; regenerativ: Training, Schlaf, Musik. Ressource: Bewegung, Freunde, Ernährung.'),
    ]),
    ('quiz-st', [
        RF(['r|Die Nummer gegen Kummer ist 116 111.', 'f|Bei einer bewusstlosen Person, die atmet, beginnt man mit der Herzdruckmassage.|stabile Seitenlage', 'r|Resilienz kann trainiert werden.', 'f|Eine Impfung ist tertiäre Prävention.|primäre Prävention']),
    ]),
]),
}
