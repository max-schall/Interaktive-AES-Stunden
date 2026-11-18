#!/usr/bin/env python3
"""Layout-Prüfung: Text, der Grafiken oder anderen Text überdeckt, abgeschnittener Text, SVG-Beschriftungen,
die sich überlappen oder aus der Grafik ragen. Geht jede Station jeder Stunde durch (inkl. Umschalter-Optionen).
Aufruf: audit.py <ordner ...> [--w=1280 --h=720] [--only=<datei-teil>]"""
import sys, json
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
args = [a for a in sys.argv[1:] if not a.startswith('--')]
opt = dict(a[2:].split('=', 1) for a in sys.argv[1:] if a.startswith('--') and '=' in a)
W, H = int(opt.get('w', 1280)), int(opt.get('h', 720))

JS = r"""(sid) => {
  const st = document.getElementById(sid), out = [];
  const vis = el => { const r = el.getBoundingClientRect(); const cs = getComputedStyle(el); return r.width > 0 && r.height > 0 && cs.visibility !== 'hidden' && cs.opacity !== '0'; };
  const inter = (a, b) => Math.max(0, Math.min(a.right, b.right) - Math.max(a.left, b.left)) * Math.max(0, Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top));
  const name = el => (el.id ? '#' + el.id : el.tagName.toLowerCase() + (el.className && el.className.baseVal === undefined && el.className ? '.' + String(el.className).split(' ')[0] : ''));
  const path = el => { const p = []; let e = el; while (e && e !== st && p.length < 3) { p.unshift(name(e)); e = e.parentElement; } return p.join(' > '); };
  // Textzeilen (HTML)
  const texts = [];
  const tw = document.createTreeWalker(st, NodeFilter.SHOW_TEXT);
  while (tw.nextNode()) {
    const n = tw.currentNode, el = n.parentElement;
    if (!n.textContent.trim() || !el || el.closest('svg, canvas, script, style, option, select') || !vis(el)) continue;
    const rg = document.createRange(); rg.selectNodeContents(n);
    for (const r of rg.getClientRects()) if (r.width > 2 && r.height > 2) texts.push({el, r, t: n.textContent.trim().slice(0, 40)});
  }
  // Grafiken
  const gfx = [...st.querySelectorAll('canvas, svg, img')].filter(g => vis(g) && !g.classList.contains('ico') && g.getBoundingClientRect().width > 40);
  for (const tx of texts) for (const g of gfx) {
    if (g.contains(tx.el) || tx.el.contains(g)) continue;
    const a = inter(tx.r, g.getBoundingClientRect());
    if (a > 30) out.push(`Text über Grafik: "${tx.t}" (${path(tx.el)}) ↔ ${path(g)} [${Math.round(a)}px²]`);
  }
  // Text über Text
  for (let i = 0; i < texts.length; i++) for (let j = i + 1; j < texts.length; j++) {
    const A = texts[i], B = texts[j];
    if (A.el === B.el || A.el.contains(B.el) || B.el.contains(A.el)) continue;
    const a = inter(A.r, B.r), m = Math.min(A.r.width * A.r.height, B.r.width * B.r.height);
    if (a > 40 && a > .2 * m) out.push(`Text über Text: "${A.t}" ↔ "${B.t}" (${path(A.el)} | ${path(B.el)})`);
  }
  // abgeschnittener Text
  st.querySelectorAll('*').forEach(el => {
    if (!vis(el) || el.closest('svg') || !el.textContent.trim() || el.matches('select, option, input, textarea, .tl-scroll, .table-wrap')) return;
    const cs = getComputedStyle(el);
    const clipX = /(hidden|clip|auto|scroll)/.test(cs.overflowX) && el.scrollWidth > el.clientWidth + 2;
    const clipY = /(hidden|clip)/.test(cs.overflowY) && el.scrollHeight > el.clientHeight + 3 && !el.matches('.bt, .bt *, .mc-bar');
    if ((clipX || clipY) && el.children.length < 6) out.push(`abgeschnitten: ${path(el)} "${el.textContent.trim().slice(0, 40)}" (${el.scrollWidth}×${el.scrollHeight} > ${el.clientWidth}×${el.clientHeight})`);
    const r = el.getBoundingClientRect();
    if (r.right > innerWidth + 2 && !el.closest('.table-wrap, .tl-scroll')) out.push(`ragt rechts raus: ${path(el)} (${Math.round(r.right)} > ${innerWidth})`);
  });
  // SVG-Beschriftungen
  st.querySelectorAll('svg').forEach(svg => {
    if (!vis(svg)) return;
    const sr = svg.getBoundingClientRect(), ts = [...svg.querySelectorAll('text')].filter(t => t.textContent.trim() && vis(t)).map(t => ({t, r: t.getBoundingClientRect()}));
    for (const a of ts) { if (a.r.left < sr.left - 2 || a.r.right > sr.right + 2 || a.r.top < sr.top - 2 || a.r.bottom > sr.bottom + 2) out.push(`SVG-Text ragt aus Grafik: "${a.t.textContent.trim().slice(0, 30)}" in ${path(svg)}`); }
    for (let i = 0; i < ts.length; i++) for (let j = i + 1; j < ts.length; j++) { const a = inter(ts[i].r, ts[j].r), m = Math.min(ts[i].r.width * ts[i].r.height, ts[j].r.width * ts[j].r.height); if (a > 20 && a > .15 * m) out.push(`SVG-Text überlappt: "${ts[i].t.textContent.trim().slice(0, 25)}" ↔ "${ts[j].t.textContent.trim().slice(0, 25)}" in ${path(svg)}`); }
  });
  // SVG-Text von später gezeichneten Formen verdeckt (Hit-Test an mehreren Punkten der Beschriftung)
  st.querySelectorAll('svg text').forEach(t => { if (vis(t)) t.style.pointerEvents = 'auto'; });
  st.querySelectorAll('svg text').forEach(t => {
    if (!vis(t) || !t.textContent.trim()) return;
    const r = t.getBoundingClientRect(); let hid = 0;
    for (const fx of [.2, .5, .8]) { const x = r.left + r.width * fx, y = r.top + r.height / 2; if (x < 0 || y < 0 || x > innerWidth || y > innerHeight) continue; const top = document.elementFromPoint(x, y); if (top && top !== t && !t.contains(top) && top.closest('svg') === t.closest('svg') && top.tagName.toLowerCase() !== 'svg') hid++; }
    if (hid >= 2) out.push(`SVG-Text verdeckt: "${t.textContent.trim().slice(0, 30)}" in ${path(t.closest('svg'))}`);
  });
  st.querySelectorAll('svg text').forEach(t => t.style.pointerEvents = '');
  return [...new Set(out)];
}"""

total = 0
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/chromium-browser')
    ctx = b.new_context(viewport={'width': W, 'height': H})
    for folder in args:
        for f in sorted((ROOT / folder).glob('*.html')):
            if 'only' in opt and opt['only'] not in f.name:
                continue
            pg = ctx.new_page(); pg.goto(f.as_uri()); pg.wait_for_timeout(250)
            ids = pg.eval_on_selector_all('.station', 'e => e.map(x => x.id)') or [None]
            found = []
            for sid in ids:
                if sid:
                    pg.evaluate(f"document.querySelector('[data-go=\"{sid}\"]') && document.querySelector('[data-go=\"{sid}\"]').click()")
                    pg.wait_for_timeout(350)
                if not sid:
                    continue
                segs = pg.locator(f'#{sid} .vis-head .seg button')
                for si in range(max(1, segs.count())):
                    if segs.count():
                        try: segs.nth(si).click(timeout=800); pg.wait_for_timeout(300)
                        except Exception: pass
                    for m in pg.evaluate(JS, sid):
                        found.append(f'{sid}{"/" + str(si) if segs.count() else ""}: {m}')
            found = list(dict.fromkeys(found))
            total += len(found)
            if found:
                print(f'== {folder}/{f.name}')
                for m in found[:25]:
                    print('   ', m)
            pg.close()
    b.close()
print('Befunde:', total)
