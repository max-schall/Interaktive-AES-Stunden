# Arbeitsblätter zu den Präsentationen

Erzeugt zu jeder Präsentation `<Name>.pdf` (Arbeitsblatt, 2 Seiten) und `<Name>_Lösung.pdf`
direkt neben der HTML-Datei.

    python3 render.py --alle                    # alle Reihen
    python3 render.py 6-Essverhalten             # eine Reihe
    python3 render.py 6-Essverhalten 01_Geschmack   # einzelne Blätter

Voraussetzungen: Python 3 mit `beautifulsoup4` und `segno` (QR-Code zur Präsentation, nur wenn `PAGES` in render.py gesetzt ist), `chromium-browser` (Druck nach PDF).

## Aufgaben bearbeiten

Die Aufgaben stehen in `data/<Reihe>.py`. Pro Präsentation gibt es einen Eintrag mit einer
Liste `sections`: `(station_id, [Aufgaben])`. Die Abschnittsüberschriften, der Titel, die
Leitfrage und der Hefteintrag (für die Lösung) werden aus der HTML-Datei gelesen.

Aufgabentypen (Lösungen werden immer mitgegeben):

| Typ | Beispiel |
|---|---|
| `A(text, zeilen, loes)` | offene Frage; mehrere Lösungsabsätze mit ` // ` trennen |
| `L(text)` | Lückentext, Lücken als `[[Lösung]]` |
| `GL(text, [zeilen])` | Gleichungen ergänzen, Lücken als `[[…]]` |
| `TAB(text, kopf, zeilen)` | Tabelle; Zelle `[[Lösung]]` = leer auf dem Arbeitsblatt |
| `MC(text, optionen)` | Ankreuzen; richtige Optionen mit `*` beginnen |
| `RF([...])` | Richtig/falsch: `'r|Aussage'` oder `'f|Aussage|Verbesserung'` |
| `BOX(text, höhe_mm, loes=…)` / `BOXES(text, labels, höhe, loes=[…])` | Zeichenfelder |
| `ZU(text, links, rechts, loes=[…])` | Zuordnung; je rechtem Eintrag die passende Nummer links |
| `SORT(text, begriffe, kategorien, loes=[[…], …])` | Begriffe sortieren |
| `INFO(text)` | Hinweiskasten ohne Nummer |

Das Skript meldet Abschnitte ohne Aufgaben, Aufgaben ohne Lösungstext und Blätter,
bei denen der Platz für den Heftaufschrieb zu klein wird (`<-- PRÜFEN`).
