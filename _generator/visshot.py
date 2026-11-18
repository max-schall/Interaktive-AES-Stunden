#!/usr/bin/env python3
"""Screenshots aller Grafiken (canvas/svg in .vis) einer Reihe – je Umschalter-Option und Stepper-Schritt.
Aufruf: visshot.py <ordner> [--only=<datei-teil>] [--out=<dir>] [--dark] [--w=1280 --h=720]"""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
args = [a for a in sys.argv[1:] if not a.startswith('--')]
opt = dict(a[2:].split('=', 1) for a in sys.argv[1:] if a.startswith('--') and '=' in a)
OUT = Path(opt.get('out', Path(__file__).resolve().parent / 'visshots'))
OUT.mkdir(parents=True, exist_ok=True)
W, H = int(opt.get('w', 1280)), int(opt.get('h', 720))
dark = '--dark' in sys.argv

JS_FIGS = """() => {
  const out = [];
  document.querySelectorAll('.station').forEach(st => {
    st.querySelectorAll('canvas, svg.svgfig, .vis svg').forEach((g, i) => {
      const vis = g.closest('.vis') || g.parentElement;
      if (!vis.dataset.fig) { vis.dataset.fig = st.id + '-' + out.length; out.push({st: st.id, fig: vis.dataset.fig}); }
    });
  });
  return out;
}"""

with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/chromium-browser')
    ctx = b.new_context(viewport={'width': W, 'height': H}, color_scheme='dark' if dark else 'light', device_scale_factor=1)
    for folder in args:
        for f in sorted((ROOT / folder).glob('[0-9][0-9]_*.html')):
            if 'only' in opt and opt['only'] not in f.name:
                continue
            pg = ctx.new_page()
            errs = []
            pg.on('pageerror', lambda e: errs.append(str(e)))
            pg.goto(f.as_uri()); pg.wait_for_timeout(300)
            figs = pg.evaluate(JS_FIGS)
            for fg in figs:
                pg.evaluate(f"document.querySelector('[data-go=\"{fg['st']}\"]').click()")
                pg.wait_for_timeout(500)
                vis = pg.locator(f"[data-fig=\"{fg['fig']}\"]")
                segs = vis.locator('.seg button')
                nseg = segs.count()
                stp = vis.locator('[data-st="1"]')
                states = []
                for si in range(max(1, nseg)):
                    if nseg:
                        segs.nth(si).click(); pg.wait_for_timeout(250)
                    nstep = 0
                    if stp.count():
                        pos = vis.locator('.st-pos').inner_text() if vis.locator('.st-pos').count() else 'Schritt 1 / 1'
                        nstep = int(pos.split('/')[-1])
                    for k in range(max(1, nstep)):
                        pg.wait_for_timeout(900)
                        name = f"{folder}_{f.stem}_{fg['fig']}_s{si}_k{k}{'_d' if dark else ''}.png"
                        vis.screenshot(path=str(OUT / name))
                        states.append(name)
                        if nstep and k < nstep - 1:
                            stp.click()
                    if nstep:
                        vis.locator('[data-st="0"]').click() if vis.locator('[data-st="0"]').count() else None
                print(f"{f.name} {fg['fig']}: {len(states)} Bilder")
            for e in errs:
                print('   ERR', e[:200])
            pg.close()
    b.close()
