from render import *

WS = {
'01_Gentechnik': dict(sections=[
    ('verfahren', [
        L('Gentechnik ist die gezielte Veränderung des [[Erbguts]]. Ein [[Gen]] wird aus der DNA eines Spenders entnommen und mit einem „Taxi“ – meist einem [[Virus]] oder Bakterium – in die DNA eines Empfängers eingeschleust. Das ist auch über [[Artgrenzen]] hinweg möglich.'),
    ]),
    ('ziele', [
        TAB('Grüne Gentechnik', ['Ziele', 'Bedenken'], [['[[Resistenz gegen Schädlinge]]', '[[ungehinderte Ausbreitung von gv Saatgut]]'], ['[[dürreresistente Pflanzen (Klimawandel)]]', '[[unbeabsichtigte Kreuzungen]]'], ['[[bessere Nährstoffqualität (Goldener Reis)]]', '[[fehlende Langzeitforschung, ethische Gründe]]']], h=8),
    ]),
    ('schere', [
        A('Beschreibe, wie die Gen-Schere CRISPR/Cas9 arbeitet, und nenne zwei Vorteile.', 3, 'Das Enzym Cas9 erkennt einen bestimmten DNA-Abschnitt und schneidet dort; einzelne Abschnitte werden verändert, ausgeschaltet oder ersetzt, ohne fremdes Erbgut einzuschleusen. // Vorteile: einfach, wirkungsvoll, kostengünstig, vielfältig anwendbar.'),
    ]),
    ('kennzeichnung', [
        RF(['r|Lebensmittel mit über 0,9 % GVO-Anteil müssen gekennzeichnet werden.', 'f|Milch von Kühen mit gv Futter muss gekennzeichnet werden.|muss nicht gekennzeichnet werden', 'r|Das EU-Bio-Siegel garantiert Gentechnikfreiheit.', 'f|Das „Ohne Gentechnik“-Siegel ist Pflicht.|freiwillig']),
    ]),
    ('uebungen', [
        A('Diskutiere, wie man gentechnisch veränderte Lebensmittel meiden kann.', 2, 'Auf Kennzeichnung in der Zutatenliste achten, Produkte mit „Ohne Gentechnik“-Siegel oder Bio-Siegel (EU-Bio, Demeter, Bioland, Naturland) kaufen.'),
    ]),
]),
'02_Dilemma_Diskussion': dict(sections=[
    ('dilemma', [
        A('Erkläre den Begriff Dilemma und beschreibe den Kern des Problems „Brauchen wir Gentechnik, um den Welthunger zu bekämpfen?“.', 3, 'Dilemma: Entscheidung zwischen zwei gleichermaßen unangenehmen Handlungen. // Kern: Mehr Menschen, weniger Fläche – gv Pflanzen könnten Erträge steigern, ihre Folgen für Mensch, Umwelt und Wirtschaft sind aber nicht ausreichend geklärt.'),
    ]),
    ('schritte', [
        L('Ablauf: 1. Dilemma im [[Plenum]] klären · 2. [[Einzelarbeit]] · 3. [[Kleingruppen]] · 4. [[Ping-Pong]]-Diskussion in zwei Großgruppen · 5. Rückkehr in die Kleingruppen · 6. Abschluss im Plenum.'),
    ]),
    ('argumente', [
        TAB('Meine Argumente', ['Pro Gentechnik', 'Kontra Gentechnik'], [['[[höhere Erträge]]', '[[Folgen nicht geklärt]]'], ['[[dürretolerant]]', '[[Abhängigkeit von Saatgutkonzernen]]'], ['[[weniger Spritzmittel]]', '[[Hunger ist ein Verteilungsproblem]]']], h=8),
    ]),
    ('pingpong', [
        A('Formuliere eine Erwiderung auf das Argument „Gv Pflanzen bringen höhere Erträge“.', 2, 'z. B. „Schon heute gibt es weltweit genug Nahrung; Hunger entsteht durch Armut, Kriege und ungerechte Verteilung.“'),
    ]),
    ('uebungen', [
        A('Erkläre, warum sich deine Einstellung zum Dilemma nach der Diskussion verändert haben kann.', 3, 'Individuell: neue Argumente der Gegenseite, Perspektivwechsel, Abwägen von Vor- und Nachteilen.'),
    ]),
]),
'03_Functional_Food': dict(sections=[
    ('was', [
        A('Erkläre den Begriff Functional Food und nenne drei Beispiele.', 3, 'Mit zusätzlichen Inhaltsstoffen (Vitamine, Mineralstoffe, Bakterienkulturen …) angereicherte Lebensmittel mit versprochenem Zusatznutzen; gesetzlich nicht definiert. // Beispiele: ACE-Getränk, probiotischer Joghurt, Jodsalz, Margarine mit Pflanzensterinen, Vitamin-Müsli.'),
    ]),
    ('claims', [
        TAB('Darf das draufstehen?', ['Produkt (pro 100 g)', 'Angabe', 'erlaubt?'], [['Kekse, 0,3 g Zucker', 'zuckerfrei', '[[ja]]'], ['Frischkäse, 7 g Fett', 'fettarm', '[[nein (max. 3 g)]]'], ['Brot, 7,5 g Ballaststoffe', 'ballaststoffreich', '[[ja (mind. 6 g)]]'], ['Riegel, 12 g Zucker', 'zuckerarm', '[[nein (max. 5 g)]]']], h=8),
    ]),
    ('arten', [
        SORT('Nährwertbezogen oder gesundheitsbezogen?', ['fettarm', 'Calcium trägt zur Erhaltung normaler Knochen bei', 'zuckerfrei', 'Vitamin C trägt zur normalen Funktion des Immunsystems bei'], ['nährwertbezogen', 'gesundheitsbezogen'], loes=[['fettarm', 'zuckerfrei'], ['Calcium trägt zur Erhaltung normaler Knochen bei', 'Vitamin C trägt zur normalen Funktion des Immunsystems bei']]),
    ]),
    ('bewerten', [
        A('Eine Zuckerlimo wirbt mit „hoher Gehalt an Vitamin C“. Beurteile.', 2, 'Erlaubt, wenn genug Vitamin C zugesetzt ist; die Limo bleibt aber stark zuckerhaltig und ist für eine vollwertige Ernährung nicht empfehlenswert.'),
    ]),
    ('uebungen', [
        A('Diskutiere Vor- und Nachteile von funktionellen Lebensmitteln.', 3, 'Vorteile: z. B. Jodsalz gegen Jodmangel, bequem. // Nachteile: teurer, Nutzen oft nicht belegt, keine Dosieranleitung (Überdosierung), oft viel Zucker.'),
    ]),
]),
'04_Nahrungsergaenzung': dict(sections=[
    ('trend', [
        A('Erkläre, was Nahrungsergänzungsmittel sind und warum sie nicht zu den Arzneimitteln gehören.', 3, 'Konzentrate von Nährstoffen oder Pflanzenextrakte in dosierter Form (Kapseln, Tabletten, Pulver). Sie sind Lebensmittel und sollen die Ernährung Gesunder ergänzen; sie dürfen weder Krankheiten heilen noch lindern.'),
    ]),
    ('etikett', [
        A('Nenne fünf Kennzeichnungselemente, die NEM zusätzlich tragen müssen.', 3, 'Bezeichnung „Nahrungsergänzungsmittel“, Stoffkategorie, empfohlene Tagesverzehrmenge, Nährstoffgehalt, Warnhinweis Tagesdosis, Hinweis „kein Ersatz für ausgewogene Ernährung“, Lagerung außerhalb der Reichweite von Kindern.'),
    ]),
    ('wer', [
        TAB('Wer kann NEM brauchen?', ['Personengruppe', 'Nährstoff', 'Begründung'], [['Schwangere', '[[Folsäure, Jod]]', '[[erhöhter Bedarf]]'], ['vegan Lebende', '[[Vitamin B12]]', '[[kommt fast nur in tierischen Lebensmitteln vor]]'], ['ältere Menschen', '[[Vitamin D]]', '[[selten draußen, Haut bildet weniger]]']], h=8),
    ]),
    ('gefahren', [
        A('Nenne drei Gefahren oder Nachteile von NEM.', 2, 'Überdosierung, Wechselwirkungen mit Medikamenten, Irrglaube an Ausgleich einer schlechten Ernährung, unnötige Kosten.'),
    ]),
    ('uebungen', [
        A('Beurteile: Ein gesunder 16-Jähriger nimmt täglich einen Proteinshake und eine Multivitamintablette.', 3, 'Bei vollwertiger Ernährung überflüssig (BfR); Eiweiß- und Vitaminbedarf wird über Lebensmittel gedeckt. Kosten und Überdosierungsgefahr.'),
    ]),
]),
'05_Consumer_Citizenship': dict(sections=[
    ('aktionen', [
        L('Unter Consumer Citizenship versteht man die aktive Vertretung eigener [[Interessen]] zur Verbesserung der [[Konsumumgebung]]. Man spricht auch von [[politischem]] Konsum.'),
    ]),
    ('zuordnen', [
        TAB('Aktionsformen', ['Aktion', 'Beispiel'], [['Boykott', '[[Produkte einer Firma nicht mehr kaufen]]'], ['Buykott', '[[gezielt Fairtrade-Produkte kaufen]]'], ['kooperativ', '[[Gespräch mit dem Unternehmen, Petition]]'], ['konfrontativ', '[[Demonstration, Goldener Windbeutel]]']], h=8),
    ]),
    ('gap', [
        A('Erkläre den Begriff Consumer-Citizen-Gap an einem Beispiel aus deinem Alltag.', 3, 'Abweichung zwischen Einstellung und Kaufverhalten. Beispiel: Tierwohl ist wichtig, trotzdem wird das billigste Fleisch gekauft.'),
    ]),
    ('nano', [
        A('Begründe, warum viele Verbrauchende eine Kennzeichnung aller Nanopartikel fordern.', 2, 'Nanoteilchen sind unsichtbar, reagieren schnell und gelangen leicht in den Körper; Risiken sind unklar. Bisher sind z. B. Nanopartikel in Verpackungen nicht kennzeichnungspflichtig.'),
    ]),
    ('uebungen', [
        A('Nenne ein Lebensmittel oder eine Verpackung, über die du dich geärgert hast, und eine passende Aktion.', 3, 'Individuell, z. B. Mogelpackung – Beschwerde bei der Verbraucherzentrale, Foodwatch-Abstimmung, Boykott.'),
    ]),
]),
'06_Verpackung': dict(sections=[
    ('pizza', [
        A('Nenne sechs Pflichtangaben nach der LMIV.', 3, 'Bezeichnung, Zutatenverzeichnis, Allergene, Menge bestimmter Zutaten, Nettofüllmenge, Mindesthaltbarkeitsdatum, Aufbewahrung, Name/Anschrift, Nährwerttabelle, ggf. Gebrauchsanleitung.'),
    ]),
    ('pflicht', [
        SORT('Pflicht oder freiwillig?', ['Zutatenverzeichnis', '„Neu!“', 'Allergene', 'Nutri-Score', 'Nettofüllmenge', 'Serviervorschlag'], ['Pflicht', 'freiwillig'], loes=[['Zutatenverzeichnis', 'Allergene', 'Nettofüllmenge'], ['„Neu!“', 'Nutri-Score', 'Serviervorschlag']]),
    ]),
    ('siegel', [
        ZU('Ordne zu.', ['EU-Bio-Siegel', 'V-Label', 'Glutenfrei-Siegel', 'Nutri-Score'], ['vegetarisch oder vegan', 'Nährwertqualität A bis E', 'ökologische Erzeugung', 'geeignet bei Zöliakie'], loes=[2, 4, 1, 3]),
    ]),
    ('green', [
        A('Erkläre den Begriff Greenwashing und nenne zwei Merkmale glaubwürdiger Angaben.', 3, 'Greenwashing: Unternehmen täuschen durch Werbung ein grünes Image vor, ohne sich wirklich für Nachhaltigkeit zu engagieren. // Glaubwürdig: unabhängiges, kontrolliertes Siegel; konkrete, überprüfbare Angabe (z. B. „80 % Recyclingkunststoff“).'),
    ]),
    ('uebungen', [
        A('Analysiere eine Verpackung von zu Hause: Pflichtangaben, freiwillige Angaben, Siegel. Begründe deine (Nicht-)Kaufentscheidung.', 4, 'Individuell.'),
    ]),
]),
'07_Wiederholung': dict(ichkann=True, sections=[
    ('begriffe', [
        ZU('Ordne zu.', ['GVO', 'Health Claims', 'NEM', 'Buykott', 'Greenwashing'], ['grünes Image vortäuschen', 'gezielt bestimmte Produkte kaufen', 'gentechnisch veränderter Organismus', 'Nährstoffkonzentrat in dosierter Form', 'nährwert- und gesundheitsbezogene Angaben'], loes=[5, 4, 1, 3, 2]),
    ]),
    ('fall', [
        A('Analysiere und beurteile die Lebens- und Ernährungsweise von Emilia und Leon.', 4, 'Positiv: ovo-lakto-vegetarisch, regelmäßig Sport. // Kritisch: Magnesium-, Zink- und B12-Tabletten bei vollwertiger Ernährung meist überflüssig (B12 über Milch und Eier); ACE-Saft ist Functional Food mit oft viel Zucker.'),
        A('Erläutere, wie sie Einfluss auf das geplante gv Versuchsfeld nehmen können.', 3, 'Bürgerinitiative, Gespräche mit Gemeinderat und Unternehmen (kooperativ), Unterschriften, Demonstration, Presse (konfrontativ).'),
    ]),
    ('quiz-st', [
        RF(['r|NEM sind rechtlich Lebensmittel.', 'f|Functional Food ist gesetzlich genau definiert.|nicht definiert', 'r|Bio-Produkte sind gentechnikfrei.', 'f|Der Nutri-Score ist Pflicht.|freiwillig']),
    ]),
]),
}
