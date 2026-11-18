from render import *

WS = {
'01_Geschmack': dict(sections=[
    ('richtungen', [
        TAB('Ergänze die Tabelle zu den Geschmacksrichtungen.', ['Geschmacksrichtung', 'Beispiel', 'angeboren: Vorliebe oder Abneigung?'],
            [['süß', '[[reifes Obst, Honig]]', '[[Vorliebe]]'], ['salzig', '[[Brezel, Käse]]', '[[Vorliebe]]'], ['sauer', '[[Zitrone, unreifes Obst]]', '[[Abneigung]]'],
             ['bitter', '[[Rosenkohl, Kaffee]]', '[[Abneigung]]'], ['umami', '[[Parmesan, Brühe]]', '[[Vorliebe]]']], h=7),
    ]),
    ('evolution', [
        A('Erläutere, warum die angeborenen Geschmacksvorlieben und -abneigungen für das Überleben der Menschen in der Steinzeit wichtig waren.', 4,
          'Süße Lebensmittel sind reif und liefern viel Energie; Fett liefert ebenfalls viel Energie; Salz war selten und ist wichtig für den Wasserhaushalt. // Saure und bittere Lebensmittel können unreif, verdorben oder giftig sein – die Abneigung schützte vor Vergiftungen.'),
    ]),
    ('gewoehnung', [
        L('Unbekannte Lebensmittel müssen erst als [[sicher]] eingestuft werden, bevor wir sie mögen. Oft muss man ein Lebensmittel [[8- bis 10-mal]] probieren. Der Geschmack ist also [[veränderbar]].'),
        A('Nenne ein Lebensmittel, das du früher nicht mochtest und heute gern isst. Erkläre, wie es dazu kam.', 2, 'Individuell, z. B. Oliven: im Urlaub mehrmals probiert und daran gewöhnt (Geschmacksgewöhnung).'),
    ]),
    ('biografie', [
        INFO('Fragen für deine Essbiografie: Was war dein Lieblingsessen als Kind? · Wer kocht für dich? · Welche Lebensmittel magst du gar nicht? · Gibt es an Festtagen besondere Gerichte? · Welche Tischregeln gibt es in deiner Familie? · Was ist im Moment dein Lieblingsessen?'),
        BOX('Stelle auf einem Zeitstrahl dar, welche Lieblingsessen du schon hattest (Kleinkind – Kindergarten – Grundschule – heute).', 28, loes='Individuelle Lösung: Zeitstrahl mit mindestens drei Lebensabschnitten und je einem Lieblingsessen.'),
    ]),
    ('uebungen', [
        RF(['f|Alle Menschen mögen von Geburt an bittere Lebensmittel.|Bittere Lebensmittel lehnen wir von Geburt an ab.', 'r|Umami bedeutet „herzhaft, würzig“.',
            'r|Schon im Mutterleib nimmt ein Baby Geschmack wahr.', 'f|Der Geschmack eines Menschen ist ab der Geburt festgelegt.|Der Geschmack entwickelt sich ein Leben lang weiter.']),
    ]),
]),

'02_Koerper': dict(sections=[
    ('hunger', [
        TAB('Erkläre die drei Begriffe und nenne je ein Beispiel.', ['Begriff', 'Erklärung', 'Beispiel'],
            [['Hunger', '[[körperliches Signal: Der Körper braucht Energie]]', '[[Magenknurren in der 4. Stunde]]'], ['Appetit', '[[Lust auf etwas Bestimmtes, auch ohne Hunger]]', '[[Duft von Popcorn im Kino]]'], ['Sättigung', '[[Signal: genug gegessen]]', '[[angenehmes Völlegefühl nach dem Essen]]']], h=9, widths=[18, 47, 35]),
    ]),
    ('blutzucker', [
        L('Hunger spürst du, wenn dein [[Blutzuckerspiegel]] sinkt. Dann sendet der Körper Signale an das [[Hungerzentrum]] im Gehirn. Das Sättigungsgefühl setzt erst etwa [[15–20]] Minuten nach Beginn des Essens ein.'),
        A('Erkläre, warum es problematisch ist, Hunger- und Sättigungssignale dauerhaft zu übergehen.', 2, 'Man nimmt die natürlichen Reize nicht mehr wahr und isst mehr, als man braucht. // Folgen: Übergewicht und ernährungsmitbedingte Krankheiten wie Diabetes Typ 2 oder Gicht.'),
    ]),
    ('faktoren', [
        SORT('Ordne die Einflussfaktoren zu.', ['Durst', 'Stimmung', 'Religion', 'Allergie', 'Erinnerungen', 'Einkommen', 'Sättigung', 'Beobachtung anderer', 'Familienrezepte'],
             ['physiologisch', 'psychologisch', 'soziokulturell'], loes=[['Durst', 'Allergie', 'Sättigung'], ['Stimmung', 'Erinnerungen', 'Beobachtung anderer'], ['Religion', 'Einkommen', 'Familienrezepte']]),
    ]),
    ('sprueche', [
        A('„Iss deinen Teller leer, dann gibt es morgen schönes Wetter.“ Nimm Stellung zu diesem Erziehungsspruch.', 3, 'Kinder lernen so, ihr Sättigungsgefühl zu unterdrücken, und essen mehr als nötig. // Besser: kleine Portionen nehmen, bei Bedarf nachschöpfen und auf den eigenen Körper hören.'),
    ]),
    ('uebungen', [
        A('Beschreibe eine Situation, in der du Hunger hattest, und eine, in der du nur Appetit hattest.', 2, 'Individuell, z. B. Hunger: nach dem Sport, Magen knurrt. Appetit: Lust auf Eis beim Vorbeigehen an der Eisdiele.'),
    ]),
]),

'03_Umwelt': dict(sections=[
    ('faktoren', [
        BOX('Erstelle eine Mindmap „Äußere Einflussfaktoren auf mein Essverhalten“ mit mindestens sechs Faktoren und je einem Beispiel.', 45, loes='Familie und Erziehung (Familienrezepte), Kultur und Region (Maultaschen), Religion (halal, koscher, Fastenzeit), Lebensstil und Werte (vegetarisch, regional), Einkommen (Bio-Lebensmittel), Freunde (Mittagspause), Werbung und Angebot (2 für 1), Gefühle (Frustessen).'),
    ]),
    ('religion', [
        ZU('Ordne zu.', ['halal', 'koscher', 'Karfreitag', 'Schweinefleisch'], ['in Islam und Judentum verboten', 'im Islam erlaubte Lebensmittel', 'viele Christen verzichten auf Fleisch', 'im Judentum erlaubte Lebensmittel'], loes=[4, 1, 3, 2]),
    ]),
    ('gefuehle', [
        A('Erkläre, warum viele Menschen bei Stress oder Frust zu Süßigkeiten greifen.', 2, 'Zucker und Fett setzen im Gehirn Botenstoffe frei, die Glücksgefühle auslösen. // Wer als Kind mit Süßem getröstet oder belohnt wurde, nutzt Essen oft weiter zur Regulierung von Gefühlen.'),
        A('Nenne drei Alternativen zum Frustessen.', 1, 'z. B. Bewegung/Sport, Musik hören, mit jemandem reden, Spaziergang, Hobby'),
    ]),
    ('reize', [
        TAB('Ordne zu: innerer Reiz (i) oder äußerer Einflussfaktor (a)?', ['Beispiel', 'i / a'], [['Magenknurren', '[[i]]'], ['Werbespot für Limonade', '[[a]]'], ['Durstgefühl', '[[i]]'], ['Familientradition am Sonntag', '[[a]]'], ['Angebot „3 für 2“', '[[a]]']], h=6, widths=[80, 20]),
    ]),
    ('uebungen', [
        A('Nenne drei Gerichte, die ihr zu Hause oft esst. Analysiere, welche Einflussfaktoren dahinterstecken.', 3, 'Individuell; z. B. Spaghetti (schnell, günstig – Einkommen, Zeit), Omas Rouladen (Familientradition), Döner (Freunde, Region).'),
    ]),
]),

'04_Tischsitten': dict(sections=[
    ('deutsch', [
        A('Nenne vier Tischsitten, die in Deutschland üblich sind.', 2, 'Hände waschen vor dem Essen; mit Messer und Gabel essen; Ellenbogen nicht auf den Tisch; nicht schmatzen oder schlürfen; nicht mit vollem Mund sprechen.'),
    ]),
    ('welt', [
        TAB('Beschreibe eine Tischsitte aus jedem Land.', ['Land', 'Tischsitte'], [['China', '[[Schlürfen erlaubt (Kompliment); Anstandsrest lassen]]'], ['Indien', '[[mit der rechten Hand essen; Teller leer essen]]'], ['Russland', '[[Teller nicht leer essen]]'], ['Japan', '[[Stäbchen nie senkrecht in den Reis stecken]]']], h=8, widths=[20, 80]),
    ]),
    ('gedeck', [
        BOX('Zeichne ein Gedeck für ein Mittagessen (Draufsicht). Beschrifte Teller, Gabel, Messer, Dessertlöffel und Glas.', 50, loes='Teller in der Mitte, einen Daumen breit von der Tischkante; Gabel links; Messer rechts, Schneide zum Teller; Dessertlöffel oberhalb des Tellers, Griff nach rechts; Glas oberhalb der Messerspitze.'),
    ]),
    ('fehler', [
        A('In einem Gedeck liegt die Gabel rechts, die Messerschneide zeigt nach außen und das Glas steht links. Verbessere.', 2, 'Gabel nach links, Messerschneide zum Teller drehen, Glas oberhalb rechts über die Messerspitze stellen.'),
    ]),
    ('uebungen', [
        A('Timo ist bei seinem neuen Chef in China zum Essen eingeladen. Erläutere, wie er sich vorbereiten sollte, und begründe, warum das wichtig ist.', 3, 'Er sollte sich über die chinesischen Tischsitten informieren (Stäbchen, Schlürfen erlaubt, Anstandsrest). // So vermeidet er, den Gastgeber unabsichtlich zu beleidigen, und zeigt Respekt vor der anderen Kultur.'),
    ]),
]),

'05_Sinnexperiment': dict(sections=[
    ('sinne', [
        TAB('Ergänze die Leitfragen und je zwei passende Adjektive.', ['Sinn', 'Leitfrage', 'Adjektive'],
            [['Sehen', '[[Wie sieht die Tomate aus?]]', '[[rot, glänzend]]'], ['Riechen', '[[Wie riecht sie?]]', '[[fruchtig, nach Gras]]'], ['Tasten', '[[Wie fühlt sie sich an?]]', '[[glatt, prall]]'], ['Hören', '[[Was hörst du beim Abbeißen?]]', '[[knackig, leise]]'], ['Schmecken', '[[Wie schmeckt sie?]]', '[[süßlich, wässrig]]']], h=8, widths=[16, 50, 34]),
    ]),
    ('schritte', [
        L('1. Schritt: Lebensmittel[[auswahl]] – 2. Schritt: [[Vorbereitung]] (Einkauf, Hände waschen, Material, Regeln) – 3. Schritt: [[Durchführung]].'),
        A('Beschreibe, warum Hygiene auch bei einem Sinnexperiment wichtig ist.', 2, 'Die Lebensmittel werden angefasst und gegessen; ungewaschene Hände oder geteilte Löffel übertragen Keime.'),
    ]),
    ('woerter', [
        SORT('Ordne: neutral beschreibend oder wertend?', ['lecker', 'glänzend', 'eklig', 'knackig', 'super', 'fruchtig', 'widerlich', 'saftig'], ['neutral', 'wertend'], loes=[['glänzend', 'knackig', 'fruchtig', 'saftig'], ['lecker', 'eklig', 'super', 'widerlich']]),
    ]),
    ('bogen', [
        BOX('Beobachtungsbogen: Führe das Sinnexperiment durch und notiere deine Eindrücke.', 40, label='Sehen · Riechen · Tasten · Hören · Schmecken · Mundgefühl', loes='Individuelle Beobachtungen mit neutralen Adjektiven zu allen Sinnen.'),
    ]),
    ('uebungen', [
        A('Diskutiert, warum eure Geschmackswahrnehmungen unterschiedlich sein können.', 2, 'Jeder Mensch hat eine eigene Essbiografie, unterschiedliche Erfahrungen und Gewohnheiten; auch Tagesform, Hunger und Erwartungen beeinflussen die Wahrnehmung.'),
    ]),
]),

'06_Wiederholung': dict(ichkann=True, sections=[
    ('begriffe', [
        ZU('Ordne die Begriffe den Erklärungen zu.', ['Essbiografie', 'Appetit', 'soziokulturell', 'Tischsitten', 'umami'],
           ['Verhaltensregeln beim Essen', 'herzhaft, würzig', 'alle Erfahrungen mit Essen und Trinken', 'Gesellschaft und Kultur betreffend', 'Lust auf etwas Bestimmtes'], loes=[4, 5, 1, 3, 2]),
    ]),
    ('ordnen', [
        A('Nenne Einflussfaktoren auf dein Essverhalten und ordne sie nach inneren und äußeren Einflussfaktoren.', 3, 'Innere Reize: Hunger, Durst, Sättigung. // Äußere Einflussfaktoren: Familie, Kultur/Region, Religion, Lebensstil, Einkommen, Freunde, Werbung, Gefühle.'),
    ]),
    ('quiz-st', [
        RF(['r|Die Vorliebe für Süßes ist angeboren.', 'f|Bei einem Menü benutzt man das Besteck von innen nach außen.|von außen nach innen', 'r|Beim Sinnexperiment beginnt man mit dem Sehen.', 'f|Appetit entsteht nur, wenn der Blutzucker sinkt.|Das ist Hunger; Appetit ist Lust auf etwas Bestimmtes.']),
    ]),
]),
}
