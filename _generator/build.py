#!/usr/bin/env python3
"""Baut die AES-Unterrichtsreihen aus src/<reihe>/*.html in den Zielordner.
Aufbau wie bei den Interaktiven Chemiestunden: eine Station pro Bildschirm, Zeitleiste oben,
Hefteintrag zum Aufdecken, Übungen; dazu je Reihe eine Übersichtsseite.
Aufruf: build.py [reihe ...]   (ohne Argumente: alle Reihen)"""
import html, json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
from series import SERIES  # noqa: E402

FACH = 'AES'
FACH_LANG = 'Alltagskultur, Ernährung, Soziales'

# Gemeinsame Farben (gedeckt): Rückmeldung, Diagrammfarben c1–c7
COMMON = ("--good:#4E8A4C; --bad:#B4513F; --warn:#B9832A; --gold:#B08A2E; --water:#4A84B0; --hot:#C2623A; --cold:#4A84B0;\n"
          "  --c1:#C07650; --c2:#6E9868; --c3:#4D8796; --c4:#8C6B9A; --c5:#C39A45; --c6:#5B72A6; --c7:#A85E70;")
COMMON_DARK = ("--good:#7CC27A; --bad:#E58873; --warn:#E3B15A; --gold:#DDB65A; --water:#7DB4DD; --hot:#EE9068; --cold:#7DB4DD;\n"
               "    --c1:#E19A74; --c2:#94C08D; --c3:#78B3C2; --c4:#B794C4; --c5:#E2BF6E; --c6:#8EA2D6; --c7:#D58C9D;")
# Klassenfarben: warm und gedämpft, von Terrakotta (6) über Salbei, Petrol, Heide bis Schiefer (10)
PALETTES = {
    6: dict(light="--bg:#F8F3EC; --surface:#FFFDF9; --surface-2:#F1E7DB; --ink:#2B211A; --ink-2:#6E5D4F; --line:#E4D5C3;\n  --accent:#A9562F; --accent-ink:#FFFFFF;",
            dark="--bg:#1A1410; --surface:#231B16; --surface-2:#2E241D; --ink:#F3E9DF; --ink-2:#C4B2A1; --line:#43362C;\n    --accent:#EB9A70; --accent-ink:#1A1410;"),
    7: dict(light="--bg:#F2F5EF; --surface:#FDFEFB; --surface-2:#E4EBDF; --ink:#1C261D; --ink-2:#56655A; --line:#D1DCCB;\n  --accent:#4C7650; --accent-ink:#FFFFFF;",
            dark="--bg:#111711; --surface:#182019; --surface-2:#212B22; --ink:#E6EEE4; --ink-2:#A8B8A9; --line:#334133;\n    --accent:#93C495; --accent-ink:#111711;"),
    8: dict(light="--bg:#F0F5F5; --surface:#FBFEFE; --surface-2:#DFEAEA; --ink:#142427; --ink-2:#4E6467; --line:#CADADB;\n  --accent:#2C6B73; --accent-ink:#FFFFFF;",
            dark="--bg:#0F1718; --surface:#152022; --surface-2:#1D2A2C; --ink:#E2EDEE; --ink-2:#A0B6B8; --line:#2E4244;\n    --accent:#80C4CB; --accent-ink:#0F1718;"),
    9: dict(light="--bg:#F6F2F5; --surface:#FEFCFE; --surface-2:#ECE3EB; --ink:#251C26; --ink-2:#635567; --line:#DCD0DC;\n  --accent:#784C7D; --accent-ink:#FFFFFF;",
            dark="--bg:#171216; --surface:#20191F; --surface-2:#2A212A; --ink:#EFE7EF; --ink-2:#BCABBE; --line:#3F3340;\n    --accent:#CFA2D4; --accent-ink:#171216;"),
    10: dict(light="--bg:#F2F3F7; --surface:#FDFDFE; --surface-2:#E3E6EF; --ink:#1A1F2C; --ink-2:#575F73; --line:#D0D5E2;\n  --accent:#42548C; --accent-ink:#FFFFFF;",
             dark="--bg:#11141A; --surface:#181C25; --surface-2:#212633; --ink:#E7EAF2; --ink-2:#A8B0C4; --line:#323A4C;\n    --accent:#9AACE8; --accent-ink:#11141A;"),
}
FONTS = '<link rel="stylesheet" href="../fonts/fonts.css">'


def palette_css(grade):
    p = PALETTES[grade]
    fonts = ('  --f-display:"Fraunces",Georgia,"Times New Roman",serif;\n  --f-body:"Atkinson Hyperlegible","Segoe UI",system-ui,sans-serif;\n'
             '  --f-mono:"IBM Plex Mono",ui-monospace,"SFMono-Regular",Consolas,monospace;\n  --radius:18px;\n  font-size:clamp(16px, 0.75vw + 9px, 22px);\n')
    dark = f"    {p['dark']}\n    {COMMON_DARK}\n    color-scheme:dark;\n"
    return (":root{\n  " + p['light'] + "\n  " + COMMON + "\n" + fonts + "}\n"
            "@media (prefers-color-scheme: dark){\n  :root:not([data-theme=\"light\"]){\n" + dark + "  }\n}\n"
            ":root[data-theme=\"dark\"]{\n" + dark + "}\n")


def base_css():
    return (HERE / 'core.css').read_text(encoding='utf-8') + (HERE / 'aes.css').read_text(encoding='utf-8')


def base_js():
    return (HERE / 'core.js').read_text(encoding='utf-8') + '\n' + (HERE / 'lib_aes.js').read_text(encoding='utf-8')


def ghs_js():
    """Offizielle GHS-Piktogramme (ghs/*.png) als Data-URIs, damit jede Datei eigenständig bleibt."""
    import base64
    imgs = {q.stem: 'data:image/png;base64,' + base64.b64encode(q.read_bytes()).decode()
            for q in sorted((HERE / 'ghs').glob('GHS0*.png'))}
    return 'const GHS_IMG = ' + json.dumps(imgs) + ';\n'


META_RE = re.compile(r'^\s*<!--(.*?)-->', re.S)


def parse_lesson(path):
    txt = path.read_text(encoding='utf-8')
    m = META_RE.match(txt)
    meta = {}
    for line in m.group(1).strip().splitlines():
        if ':' in line:
            k, v = line.split(':', 1)
            meta[k.strip()] = v.strip()
    body = txt[m.end():]
    js = ''
    if '<script>' in body:
        i = body.index('<script>')
        js = body[i + 8:body.rindex('</script>')]
        body = body[:i]
    return meta, body.strip(), js


SEC_RE = re.compile(r'<section class="station" id="([^"]+)"([^>]*)>')
ATTR_RE = re.compile(r'data-([a-z]+)="([^"]*)"')


def build_lesson(series, idx, lessons, outdir, css, js):
    path, meta, body, ljs = lessons[idx]
    grade = series['grade']
    num = idx + 1
    secs = [(mm.group(1), dict(ATTR_RE.findall(mm.group(2)))) for mm in SEC_RE.finditer(body)]
    first = True

    def hide(mm):
        nonlocal first
        tag = mm.group(0)
        if first:
            first = False
            return tag
        return tag[:-1] + ' hidden>'
    body = SEC_RE.sub(hide, body)
    stations = [(i, a) for i, a in secs if 'yr' in a]
    tl = ['      <li><button class="tl-pill" data-go="start">Start</button></li>', '      <li class="sep" aria-hidden="true"></li>']
    for k, (sid, a) in enumerate(stations):
        cls = 'm' + (' first' if k == 0 else '') + (' last' if k == len(stations) - 1 else '')
        tl.append(f'      <li class="{cls}"><button class="tl-stop" data-go="{sid}"><span class="dot"><span class="num">{k + 1}</span></span><span class="yr">{a["yr"]}</span><span class="nm">{a.get("label", sid)}</span></button></li>')
    tl.append('      <li class="sep" aria-hidden="true"></li>')
    for sid, a in secs:
        if sid != 'start' and 'yr' not in a:
            tl.append(f'      <li><button class="tl-pill" data-go="{sid}">{a.get("label", sid)}</button></li>')
    prev = ['    <ol class="preview" aria-label="Stationen dieser Stunde">']
    for k, (sid, a) in enumerate(stations):
        prev.append(f'      <li><button data-go="{sid}"><span class="num">{k + 1}</span><span class="y">{a["yr"]}</span><span class="n"><b>{a.get("title", a.get("label"))}</b><span>{a.get("sub", "")}</span></span></button></li>')
    prev.append('    </ol>')
    body = body.replace('<!--PREVIEW-->', '\n'.join(prev))
    book = ''  # keine Buchverweise in der Ausgabe
    body = body.replace('<!--BOOK-->', book)
    body = body.replace('{{N}}', str(num)).replace('{{K}}', str(grade)).replace('{{R}}', series['name'])
    if idx + 1 < len(lessons):
        npath, nmeta = lessons[idx + 1][0], lessons[idx + 1][1]
        nxt = {'href': npath.name, 'label': f'Stunde {num + 1}: {nmeta["short"]}'}
        box = (f'<div class="next-lesson"><p><b>Nächste Stunde – {nmeta["title"]}:</b> {nmeta["q"]}</p>'
               f'<a class="btn primary" href="{npath.name}">Zu Stunde {num + 1} →</a></div>')
    else:
        nxt = {'href': '00_Uebersicht.html', 'label': 'Zur Übersicht'}
        box = '<div class="next-lesson"><p><b>Geschafft!</b> Das war die letzte Stunde dieser Reihe.</p><a class="btn primary" href="00_Uebersicht.html">Zur Übersicht der Reihe</a></div>'
    if 'id="uebungen"' in body and '<!--NONEXT-->' not in body:
        i = body.index('id="uebungen"')
        j = body.index('</section>', i)
        body = body[:j] + '  ' + box + '\n' + body[j:]
    head = f'''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{meta["title"]}</title>
{FONTS}
<style>
/* Layout: feste Stationsleiste oben, eine Station pro Bildschirm, Blätter-Leiste unten – gebaut für Beamer & Presenter */
{palette_css(grade)}{css}
</style>
</head>
<body data-next="{html.escape(json.dumps(nxt, ensure_ascii=False))}">
<div class="app">
<header class="top">
  <div class="brand"><b>{meta["short"]}</b><span>Stunde {num} · {FACH} · Klasse {grade}</span></div>
  <nav class="tl-scroll" aria-label="Stationen der Stunde">
    <ol class="tl" id="tl">
{chr(10).join(tl)}
    </ol>
  </nav>
  <a class="icon-btn" href="../index.html" title="Startseite: alle Klassen und Themen">⌂ Startseite</a>
  <a class="icon-btn" href="{path.stem}.pdf" target="_blank" rel="noopener" title="Arbeitsblatt zur Stunde (PDF)">Arbeitsblatt</a>
  <a class="icon-btn" href="00_Uebersicht.html" title="Zur Übersicht der Reihe">Übersicht</a>
  <button class="icon-btn" id="fs" title="Vollbild (F)">Vollbild</button>
</header>

<main id="stage">
'''
    tail = f'''
</main>

<footer class="pager">
  <button class="btn" id="prev">←</button>
  <div class="mid"><span id="pos"></span><span class="keys"> · Pfeiltasten ← → oder Presenter</span></div>
  <button class="btn primary" id="next">→</button>
</footer>
</div>

<script>
(() => {{
{js}
/* ================================================================ */
/* ================= Inhalte dieser Stunde ================= */
{ghs_js() if 'GHS_IMG' in ljs else ''}{ljs}
startApp();
}})();
</script>
</body>
</html>
'''
    (outdir / path.name).write_text(head + body + tail, encoding='utf-8')


def build_overview(series, lessons, outdir, css):
    grade = series['grade']
    items = []
    for k, (path, meta, body, _) in enumerate(lessons):
        facts = ''.join(f'<li>{f.strip()}</li>' for f in meta.get('facts', '').split('|') if f.strip())
        book = ''  # keine Buchverweise in der Ausgabe
        items.append(f'''    <li class="lesson">
      <div class="l-num">{k + 1}</div>
      <div class="l-body">
        <p class="eyebrow">Stunde {k + 1} · {meta.get("time", "1 Unterrichtsstunde")}{book}</p>
        <h2>{meta["title"]}</h2>
        <p class="l-q"><b>Leitfrage:</b> {meta["q"]}</p>
        <ul class="facts">{facts}</ul>
        <p class="l-int"><span class="tag info">Interaktiv</span> {meta.get("inter", "")}</p>
      </div>
      <div class="l-go"><a class="btn" href="{path.stem}.pdf" target="_blank" rel="noopener" title="Arbeitsblatt zur Stunde (PDF)">Arbeitsblatt</a><a class="btn primary" href="{path.name}">Öffnen →</a></div>
    </li>''')
    arc = '<i></i>'.join(f'<span>{html.escape(m["short"])}</span>' for _, m, _, _ in lessons)
    links = ''.join(f'\n  <a class="icon-btn" href="{h}" title="{t}">{t}</a>' for h, t in series.get('links', []))
    notes = '\n'.join(f'    <div class="box"><span class="tag {c}">{t}</span>\n      <p>{p}</p></div>' for t, c, p in series['notes'])
    page = f'''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{series["name"]} – Übersicht</title>
{FONTS}
<style>
{palette_css(grade)}{css}
</style>
</head>
<body>
<div class="app">
<header class="top">
  <div class="brand"><b>{series["name"]}</b><span>{FACH} · Klasse {grade}</span></div>
  <span style="flex:1"></span>
  <a class="icon-btn" href="../index.html" title="Startseite: alle Klassen und Themen">⌂ Startseite</a>{links}
  <a class="icon-btn" href="#hinweise">Hinweise für Lehrkräfte</a>
</header>

<main>
<section class="ov">
  <div class="ov-hero">
    <div class="txt">
      <p class="eyebrow">Unterrichtsreihe · {len(lessons)} Stunden · interaktive Präsentationen</p>
      <h1>{series["h1"]}</h1>
      <p class="lead">{series["lead"]}</p>
    </div>
    <div class="ov-facts">
      <div class="meter"><span>Stunden</span><b>{len(lessons)}</b><small>Präsentationen</small></div>
      <div class="meter"><span>Umfang</span><b>≈ {series["ue"]}</b><small>Unterrichtsstunden</small></div>
      <div class="meter"><span>Klasse</span><b>{series["grade"]}</b><small>Alltagskultur, Ernährung, Soziales</small></div>
    </div>
  </div>

  <div class="ov-arc" aria-hidden="true">
    {arc}
  </div>

  <ol class="lessons">
{chr(10).join(items)}
  </ol>

  <div class="section-head" id="hinweise" style="margin-top:2.6rem">
    <p class="eyebrow">Für Lehrkräfte</p>
    <h2>Hinweise zum Einsatz</h2>
  </div>
  <div class="takeaway ov-notes">
    <div class="box"><span class="tag info">Bedienung</span>
      <p>Blättern mit den Pfeiltasten, Bild↑/Bild↓ oder einem Presenter. <b>F</b> schaltet den Vollbildmodus. Über die Leiste oben springt man direkt zu jeder Station. Stationen lassen sich direkt verlinken, z. B. <code>{lessons[0][0].name}#merke</code>.</p></div>
    <div class="box"><span class="tag info">Aufbau jeder Stunde</span>
      <p>Start mit Leitfrage → nummerierte Stationen (Einstieg, Erarbeitung, Praxis) → <b>Hefteintrag</b>, der Punkt für Punkt aufgedeckt wird → <b>Übungen</b> mit Prüfen-Knopf und Quiz. Zu jeder Stunde gibt es ein Arbeitsblatt (PDF) mit Lösung.</p></div>
{notes}
    <div class="box"><span class="tag info">Technik</span>
      <p>Jede Datei ist eigenständig und funktioniert offline, auch vom USB-Stick. Die Schriften liegen im Ordner <code>fonts</code> neben den Reihen und werden nicht aus dem Internet geladen. Hell- und Dunkelmodus folgen der Systemeinstellung.</p></div>
  </div>
</section>
</main>
</div>
</body>
</html>
'''
    (outdir / '00_Uebersicht.html').write_text(page, encoding='utf-8')


def main(only=None):
    css, js = base_css(), base_js()
    for s in SERIES:
        if only and s['folder'] not in only:
            continue
        src = HERE / 'src' / s['folder']
        files = sorted(p for p in src.glob('[0-9][0-9]_*.html'))
        if not files:
            continue
        lessons = [(p, *parse_lesson(p)) for p in files]
        out = ROOT / s['folder']
        out.mkdir(exist_ok=True)
        for i in range(len(lessons)):
            build_lesson(s, i, lessons, out, css, js)
        build_overview(s, lessons, out, css)
        print('gebaut:', s['folder'], len(lessons), 'Stunden')


if __name__ == '__main__':
    main(sys.argv[1:] or None)
