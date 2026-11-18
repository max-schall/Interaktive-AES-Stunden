# Erzeugt die Startseite index.html (Klasse -> Thema -> Stunde) aus den Themenordnern.
import re, json, sys, pathlib, html
root = pathlib.Path(__file__).resolve().parent.parent
def title(p): return html.unescape(re.search(r'<title>([^<]+)', p.read_text(encoding='utf-8')).group(1)).replace(' – Übersicht', '').strip()
topics = []
# Reihenfolge innerhalb einer Klassenstufe wie im Unterricht; unbekannte Ordner hinten, alphabetisch
ORDER = ['6-Essverhalten', '6-Nahrungszubereitung', '7-Ernaehrung_Grundlagen', '7-Nachhaltige_Ernaehrung', '8-Lebensmittelqualitaet', '8-Gesundheit_Stress',
         '9-Koerper', '9-Nachhaltiger_Konsum', '9-Textil_Konsum', '9-Qualitaetsorientierung',
         '10-Arbeit_Freizeit', '10-Haushalt_Familie', '10-Ernaehrung_Gesundheit', '10-Lebensgestaltung', '10-Engagement']
rank = lambda n: ORDER.index(n) if n in ORDER else len(ORDER)
for d in sorted((d for d in root.glob('[0-9]*-*/') if (d/'00_Uebersicht.html').exists()), key=lambda d: (int(d.name.split('-')[0]), rank(d.name), d.name)):
    ov = (d/'00_Uebersicht.html').read_text(encoding='utf-8')
    lead = re.search(r'<p class="lead">(.*?)</p>', ov, re.S)
    lead = html.unescape(re.sub(r'<[^>]+>', '', lead.group(1))).strip() if lead else ''
    lessons = [{'file': f.name, 'title': title(f)} for f in sorted(d.glob('[0-9][0-9]_*.html')) if not f.name.startswith('00_')]
    topics.append({'id': d.name, 'grade': int(d.name.split('-')[0]), 'title': title(d/'00_Uebersicht.html'), 'lead': lead, 'lessons': lessons})
data = json.dumps(topics, ensure_ascii=False)
# Klassenfarben direkt aus der Palette der Präsentationen (build.py) übernehmen
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build import PALETTES  # noqa: E402
def tok(css, name): return re.search(rf'--{name}:(#[0-9A-Fa-f]{{6}})', css).group(1)
light = ' '.join(f'--g{g}:{tok(p["light"], "accent")}; --g{g}-ink:{tok(p["light"], "accent-ink")};' for g, p in sorted(PALETTES.items()))
dark = ' '.join(f'--g{g}:{tok(p["dark"], "accent")}; --g{g}-ink:{tok(p["dark"], "accent-ink")};' for g, p in sorted(PALETTES.items()))
rules = '\n'.join(f'.grade[data-g="{g}"]{{--c:var(--g{g})}}\n:root[data-grade="{g}"]{{--accent:var(--g{g}); --accent-ink:var(--g{g}-ink)}}' for g in sorted(PALETTES))
page = (pathlib.Path(__file__).with_name("index.template.html").read_text()).replace('/*DATA*/[]', data)
page = page.replace('/*GRADES_LIGHT*/', light).replace('/*GRADES_DARK*/', dark).replace('/*GRADES_RULES*/', rules)
(root/'index.html').write_text(page)
print(len(topics), sum(len(t['lessons']) for t in topics))
