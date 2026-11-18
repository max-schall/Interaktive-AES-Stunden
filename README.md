# Interaktive AES-Stunden

Interaktive HTML-Präsentationen mit Arbeitsblättern für das Fach **Alltagskultur, Ernährung, Soziales (AES)** der Klassen 6–10 – 15 Reihen, 115 Stunden. Grundlage ist der Aufbau von *starkeSeiten AES* (Klett); Texte, Grafiken und Simulationen sind eigenständig erstellt.

**Online:** https://max-schall.github.io/Interaktive-AES-Stunden/

- `index.html` – Startseite: Klassenstufe → Thema → Stunde
- `<Klasse>-<Thema>/00_Uebersicht.html` – Übersicht der Reihe mit Hinweisen für Lehrkräfte
- `<Klasse>-<Thema>/NN_….html` – Präsentation (eigenständig, offline lauffähig)
- `<Klasse>-<Thema>/NN_….pdf` / `NN_…_Lösung.pdf` – Arbeitsblatt (mit QR-Code zur Präsentation) und Lösung
- `fonts/` – Schriften (müssen neben den Reihen liegen)
- `_generator/` – Quellen und Skripte

## Reihen

| Klasse | Themen (Stunden) |
|---|---|
| 6 | Essverhalten (6) · Nahrungszubereitung (10) |
| 7 | Ernährung und Nährstoffe (11) · Nachhaltige Ernährung (7) |
| 8 | Qualität von Lebensmitteln (7) · Gesundheit und Stress (10) |
| 9 | Körper und Körpergestaltung (8) · Nachhaltiger Konsum (8) · Textilien und Mode (7) · Qualitätsorientierung (8) |
| 10 | Arbeit und Freizeit (6) · Haushalt und Familie (8) · Ernährung und Gesundheit (7) · Lebensgestaltung und Konsum (6) · Lernen durch Engagement (6) |

Jede Reihe endet mit einer Stunde „Wiederholung“ (Karteikarten, Quiz, „Ich kann …“-Liste).

## Bauen

    cd _generator
    python3 build.py                        # alle Präsentationen und Übersichten
    python3 build.py 9-Koerper              # nur eine Reihe
    python3 build_index.py                  # Startseite
    python3 test.py 9-Koerper               # alle Stationen headless durchklicken, JS-Fehler melden
    python3 audit.py 9-Koerper [--w=390 --h=844]   # Layout-Prüfung: verdeckter, überlappender, abgeschnittener Text
    python3 visshot.py 9-Koerper [--dark]   # Screenshots aller Grafiken in allen Zuständen
    cd arbeitsblaetter && python3 render.py --alle   # Arbeitsblätter und Lösungen (PDF)

Die Inhalte einer Stunde stehen in `_generator/src/<Reihe>/NN_Name.html` (Kopfkommentar mit Metadaten, Stationen als
`<section class="station">`, Skript am Ende). Design: `_generator/core.css` + `_generator/aes.css`, Bausteine:
`_generator/core.js` + `_generator/lib_aes.js`, Reihen: `_generator/series.py`, Arbeitsblätter:
`_generator/arbeitsblaetter/data/<Reihe>.py`.

## Online

Die Adresse für die QR-Codes steht in `_generator/arbeitsblaetter/render.py` (`PAGES`).
Wird ein anderer Ort gewählt, `PAGES` ändern und `render.py --alle` erneut ausführen.
