/* Grundbibliothek (übernommen aus den Interaktiven Chemiestunden: Navigation, Quiz, Zuordnen, Lückentext …) */
'use strict';
const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => [...r.querySelectorAll(s)];
const RM = matchMedia('(prefers-reduced-motion: reduce)');
const MONO = '"IBM Plex Mono", ui-monospace, monospace';
const SANS = '"Atkinson Hyperlegible", system-ui, sans-serif';
const DISPLAY = '"Fraunces", Georgia, serif';

/* ---------------- Farben aus den Tokens ---------------- */
const C = {};
function readColors() {
  const cs = getComputedStyle(document.documentElement);
  ['bg','surface','surface-2','ink','ink-2','line','accent','gold','good','bad','warn','water','hot','cold','c1','c2','c3','c4','c5','c6','c7']
    .forEach(k => C[k.replace(/-/g, '')] = cs.getPropertyValue('--' + k).trim() || '#888888');
}
readColors();
matchMedia('(prefers-color-scheme: dark)').addEventListener('change', readColors);
new MutationObserver(readColors).observe(document.documentElement, {attributes: true, attributeFilter: ['data-theme']});

function rgb(h) { if (String(h).startsWith('rgb')) return String(h).match(/[\d.]+/g).slice(0, 3).map(Number); h = h.replace('#',''); if (h.length === 3) h = h.split('').map(c => c + c).join(''); const n = parseInt(h, 16); return [n >> 16 & 255, n >> 8 & 255, n & 255]; }
function alpha(h, a) { return `rgba(${rgb(h).join(',')},${a})`; }
function mix(a, b, t) { const A = rgb(a), B = rgb(b); return `rgb(${A.map((v, i) => Math.round(v + (B[i] - v) * t)).join(',')})`; }
const lerp = (a, b, t) => a + (b - a) * t;
const ease = t => t < .5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2;
const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
/* Startwert erst durchmischen, damit benachbarte Seeds (rng(i), rng(i + 1)) nicht fast gleiche Werte liefern */
function rng(seed) { let s = seed >>> 0; s = Math.imul(s ^ s >>> 16, 0x45d9f3b); s = Math.imul(s ^ s >>> 16, 0x45d9f3b); s = (s ^ s >>> 16) >>> 0; return () => (s = (s * 1664525 + 1013904223) >>> 0) / 4294967296; }
const fmt = (v, d = 3) => v.toLocaleString('de-DE', {maximumSignificantDigits: d});
const fix = (v, d = 1) => v.toLocaleString('de-DE', {minimumFractionDigits: d, maximumFractionDigits: d});
const shuffle = a => { for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
const SUP = s => String(s).replace(/[0-9+\-−]/g, c => ({'0':'⁰','1':'¹','2':'²','3':'³','4':'⁴','5':'⁵','6':'⁶','7':'⁷','8':'⁸','9':'⁹','+':'⁺','-':'⁻','−':'⁻'})[c]);
const SUB = s => String(s).replace(/[0-9]/g, c => '₀₁₂₃₄₅₆₇₈₉'[+c]);
function chargeStr(q) { return q === 0 ? '' : (Math.abs(q) > 1 ? Math.abs(q) : '') + (q > 0 ? '+' : '−'); }

function setup(cv) {
  const dpr = Math.min(window.devicePixelRatio || 1, 2);
  const w = cv.clientWidth, h = cv.clientHeight;
  const W = Math.round(w * dpr), H = Math.round(h * dpr);
  if (cv.width !== W || cv.height !== H) { cv.width = W; cv.height = H; }
  const ctx = cv.getContext('2d');
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  ctx.clearRect(0, 0, w, h);
  /* Schrift wächst mit der Grafik (Beamer), Bezugsbreite 560 px */
  TS = Math.max(.9, Math.min(1.6, w / 560));
  return {ctx, w, h};
}
let TS = 1, LABELQ = null;
const fs = s => Math.round(Math.max(12, s * TS) * 10) / 10;
function sphere(ctx, x, y, r, col, label, lc, stroke) {
  const g = ctx.createRadialGradient(x - r * .35, y - r * .4, r * .1, x, y, r);
  g.addColorStop(0, mix(col, '#ffffff', .45)); g.addColorStop(1, col);
  ctx.fillStyle = g; ctx.beginPath(); ctx.arc(x, y, r, 0, Math.PI * 2); ctx.fill();
  if (stroke) { ctx.strokeStyle = stroke; ctx.lineWidth = 1; ctx.stroke(); }
  if (label) {
    ctx.fillStyle = lc || '#fff'; ctx.font = `700 ${Math.max(9, r * .95)}px ${MONO}`;
    ctx.textAlign = 'center'; ctx.textBaseline = 'middle'; ctx.fillText(label, x, y + r * .06);
  }
}
function sign(ctx, x, y, r, plus) {
  ctx.strokeStyle = '#ffffff'; ctx.lineWidth = Math.max(1.4, r * .22); ctx.lineCap = 'round';
  const s = r * .48; ctx.beginPath(); ctx.moveTo(x - s, y); ctx.lineTo(x + s, y);
  if (plus) { ctx.moveTo(x, y - s); ctx.lineTo(x, y + s); }
  ctx.stroke();
}
/* Beschriftung. Wird innerhalb von canvasLoop gesammelt und nach allen Formen gezeichnet,
   damit keine Form eine Schrift verdeckt. o: {size, weight, color, align, base, font, maxW, halo} */
function label(ctx, txt, x, y, o = {}) {
  if (LABELQ && !o.now) { LABELQ.push([ctx, txt, x, y, o, ctx.getTransform(), ctx.globalAlpha]); return; }
  let size = fs(o.size || 14);
  const font = () => `${o.weight || 700} ${size}px ${o.font || SANS}`;
  ctx.font = font();
  txt = String(txt);
  if (o.maxW) {
    while (size > 9 && ctx.measureText(txt).width > o.maxW) { size -= .5; ctx.font = font(); }
    while (txt.length > 2 && ctx.measureText(txt).width > o.maxW) txt = txt.slice(0, -2) + '…';
  }
  const c = o.color || C.ink;
  ctx.textAlign = o.align || 'center'; ctx.textBaseline = o.base || 'middle';
  const light = /^#f|^#e|^#d|white|#fff/i.test(c) && c !== C.ink;
  if (o.halo !== false && !light) { ctx.save(); ctx.strokeStyle = alpha(C.surface, .9); ctx.lineWidth = Math.max(3, size * .28); ctx.lineJoin = 'round'; ctx.strokeText(txt, x, y); ctx.restore(); }
  ctx.fillStyle = c;
  ctx.fillText(txt, x, y);
}
function flushLabels() {
  const q = LABELQ; LABELQ = null; if (!q) return;
  for (const [ctx, txt, x, y, o, tf, ga] of q) { ctx.save(); ctx.setTransform(tf); ctx.globalAlpha = ga; label(ctx, txt, x, y, o); ctx.restore(); }
}
function roundRect(ctx, x, y, w, h, r) {
  r = Math.min(r, Math.abs(w) / 2, Math.abs(h) / 2);
  ctx.beginPath(); ctx.moveTo(x + r, y); ctx.arcTo(x + w, y, x + w, y + h, r); ctx.arcTo(x + w, y + h, x, y + h, r);
  ctx.arcTo(x, y + h, x, y, r); ctx.arcTo(x, y, x + w, y, r); ctx.closePath();
}

/* ---------------- Navigation ---------------- */
const STATIONS = $$('.station').map(s => s.id);
const LABEL = Object.fromEntries($$('.station').map(s => [s.id, s.dataset.label || s.id]));
const NEXT_LESSON = document.body.dataset.next ? JSON.parse(document.body.dataset.next) : null;
let cur = 0;
function go(id) { const i = STATIONS.indexOf(id); if (i >= 0 && i !== cur) { cur = i; render(true); } }
function render(scroll) {
  const id = STATIONS[cur];
  $$('.station').forEach(s => s.hidden = s.id !== id);
  $$('[data-go]', $('#tl')).forEach(b => b.dataset.go === id ? b.setAttribute('aria-current', 'step') : b.removeAttribute('aria-current'));
  const stops = $$('#tl li.m');
  const idx = stops.map(li => STATIONS.indexOf($('[data-go]', li).dataset.go));
  stops.forEach((li, i) => { li.classList.toggle('done', idx[i] < cur); li.classList.toggle('half', idx[i] === cur); });
  const prev = STATIONS[cur - 1], next = STATIONS[cur + 1];
  $('#prev').textContent = prev ? '← ' + LABEL[prev] : '←';
  $('#prev').disabled = !prev;
  if (next) { $('#next').textContent = LABEL[next] + ' →'; $('#next').disabled = false; }
  else if (NEXT_LESSON) { $('#next').textContent = NEXT_LESSON.label + ' →'; $('#next').disabled = false; }
  else { $('#next').textContent = '→'; $('#next').disabled = true; }
  $('#pos').textContent = `${cur + 1} / ${STATIONS.length}`;
  try { history.replaceState(null, '', '#' + id); } catch (e) {}
  if (scroll) {
    window.scrollTo({top: 0});
    const b = $(`#tl [data-go="${id}"]`);
    if (b) { const sc = $('.tl-scroll'); sc.scrollLeft = b.offsetLeft - sc.clientWidth / 2 + b.offsetWidth / 2; }
  }
  lastT = performance.now();
  for (const f of onShow) f(id);
}
const onShow = [];
document.addEventListener('click', e => { const b = e.target.closest('[data-go]'); if (b) go(b.dataset.go); });
$('#prev').onclick = () => { if (cur > 0) { cur--; render(true); } };
$('#next').onclick = () => {
  if (cur < STATIONS.length - 1) { cur++; render(true); }
  else if (NEXT_LESSON) location.href = NEXT_LESSON.href;
};
document.addEventListener('keydown', e => {
  if (e.target.closest('input, select, textarea') || e.altKey || e.ctrlKey || e.metaKey) return;
  if (['ArrowRight','PageDown'].includes(e.key)) { e.preventDefault(); if (cur < STATIONS.length - 1) $('#next').click(); }
  else if (['ArrowLeft','PageUp'].includes(e.key)) { e.preventDefault(); $('#prev').click(); }
  else if (e.key === 'f' || e.key === 'F') toggleFs();
});
function toggleFs() {
  try {
    if (document.fullscreenElement) document.exitFullscreen();
    else { const p = document.documentElement.requestFullscreen && document.documentElement.requestFullscreen(); if (p && p.catch) p.catch(() => {}); }
  } catch (e) {}
}
$('#fs').onclick = toggleFs;
document.addEventListener('fullscreenchange', () => $('#fs').textContent = document.fullscreenElement ? 'Vollbild beenden' : 'Vollbild');

/* ---------------- Render-Schleife ---------------- */
const visuals = [];
let lastT = performance.now();
function frame(now) {
  const dt = Math.min(.05, (now - lastT) / 1000); lastT = now;
  const id = STATIONS[cur];
  for (const v of visuals) if (v.station === id) v.tick(dt, now / 1000);
  requestAnimationFrame(frame);
}
function startApp() {
  const h0 = (location.hash || '').slice(1);
  if (STATIONS.includes(h0)) cur = STATIONS.indexOf(h0);
  render(false);
  requestAnimationFrame(frame);
}

/* ================= Bausteine ================= */
/* Hefteintrag: Punkte nacheinander aufdecken */
$$('.heft').forEach(h => {
  const items = $$('[data-step]', h), btn = $('[data-heft-next]', h), all = $('[data-heft-all]', h);
  let k = 0;
  const upd = () => { items.forEach((it, i) => it.classList.toggle('shown', i < k)); if (btn) { btn.disabled = k >= items.length; btn.textContent = k >= items.length ? 'Alles aufgedeckt' : `Nächster Punkt (${k + 1}/${items.length})`; } if (all) all.textContent = k >= items.length ? 'Wieder verdecken' : 'Alles zeigen'; };
  if (btn) btn.onclick = () => { k = Math.min(items.length, k + 1); upd(); };
  if (all) all.onclick = () => { k = k >= items.length ? 0 : items.length; upd(); };
  upd();
});

/* Multiple-Choice-Quiz. qs: [{q, a:[...], ok: index, why}] */
function mcQuiz(root, qs, o = {}) {
  let list = [], i = 0, score = 0, answered = false;
  function start() { list = o.pick ? shuffle(qs.slice()).slice(0, o.pick) : qs.slice(); i = 0; score = 0; show(); }
  function show() {
    if (i >= list.length) {
      const pct = score / list.length;
      root.innerHTML = `<div class="mc-end"><p class="eyebrow">Ergebnis</p><p class="mc-big">${score} / ${list.length}</p>
        <p class="lead">${pct === 1 ? 'Perfekt! Alles richtig.' : pct >= .7 ? 'Sehr gut! Fast alles richtig.' : pct >= .4 ? 'Ordentlich. Schau dir die Fehler noch einmal an.' : 'Wiederhole die Inhalte und versuch es noch einmal.'}</p>
        <button class="btn primary" data-mc="again">Neue Runde</button></div>`;
      return;
    }
    const q = list[i]; answered = false;
    const order = shuffle(q.a.map((t, k) => k));
    root.innerHTML = `<div class="mc-head"><span class="eyebrow">Frage ${i + 1} von ${list.length}</span><span class="score">Punkte: <b>${score}</b></span></div>
      <div class="mc-bar"><i style="width:${100 * i / list.length}%"></i></div>
      <h3 class="mc-q">${q.q}</h3>
      <div class="mc-opts">${order.map(k => `<button class="mc-opt" data-k="${k}">${q.a[k]}</button>`).join('')}</div>
      <p class="mc-why" aria-live="polite"></p>
      <div class="controls"><button class="btn primary" data-mc="next" hidden>${i + 1 < list.length ? 'Nächste Frage →' : 'Ergebnis anzeigen'}</button></div>`;
  }
  root.addEventListener('click', e => {
    const b = e.target.closest('.mc-opt, [data-mc]'); if (!b) return;
    if (b.dataset.mc === 'again') return start();
    if (b.dataset.mc === 'next') { i++; return show(); }
    if (answered) return;
    answered = true;
    const q = list[i], k = +b.dataset.k, ok = k === q.ok;
    if (ok) score++;
    $$('.mc-opt', root).forEach(x => { x.disabled = true; if (+x.dataset.k === q.ok) x.classList.add('ok'); });
    if (!ok) b.classList.add('err');
    $('.mc-why', root).innerHTML = (ok ? '<b class="good">Richtig!</b> ' : '<b class="bad">Leider falsch.</b> ') + (q.why || '');
    $('[data-mc="next"]', root).hidden = false;
    $('.score b', root).textContent = score;
  });
  start();
}

/* Zuordnen: Karten in Spalten sortieren. cats: [{id, name}], items: [{t, c}] */
function sorter(root, cats, items) {
  let sel = null;
  function build() {
    const its = shuffle(items.map((it, k) => ({...it, k})));
    root.innerHTML = `<div class="sort-pool" data-pool>${its.map(it => `<button class="sort-card" data-k="${it.k}">${it.t}</button>`).join('')}</div>
      <div class="sort-cols" style="--n:${cats.length}">${cats.map(c => `<div class="sort-col" data-c="${c.id}"><h3>${c.name}</h3><div class="sort-drop"></div></div>`).join('')}</div>
      <div class="controls"><button class="btn primary" data-s="check">Prüfen</button><button class="btn" data-s="reset">Neu mischen</button><span class="sort-fb" aria-live="polite"></span></div>`;
  }
  root.addEventListener('click', e => {
    const card = e.target.closest('.sort-card'), col = e.target.closest('.sort-col'), act = e.target.closest('[data-s]');
    if (act) {
      if (act.dataset.s === 'reset') { build(); sel = null; return; }
      let ok = 0, placed = 0;
      $$('.sort-col .sort-card', root).forEach(c => { placed++; const good = items[+c.dataset.k].c === c.closest('.sort-col').dataset.c; c.classList.toggle('ok', good); c.classList.toggle('err', !good); if (good) ok++; });
      const left = $$('[data-pool] .sort-card', root).length;
      $('.sort-fb', root).innerHTML = `<b>${ok}</b> von ${items.length} richtig zugeordnet${left ? ` · ${left} noch nicht einsortiert` : ''}${ok === items.length ? ' – perfekt!' : ''}`;
      return;
    }
    if (card) {
      if (sel === card) { card.classList.remove('sel'); sel = null; return; }
      if (sel) sel.classList.remove('sel');
      if (card.closest('.sort-col') && !sel) { /* zurück in den Pool bei erneutem Klick */ }
      sel = card; card.classList.add('sel'); card.classList.remove('ok', 'err');
      return;
    }
    if (col && sel) { $('.sort-drop', col).appendChild(sel); sel.classList.remove('sel'); sel = null; return; }
    if (e.target.closest('[data-pool]') && sel) { $('[data-pool]', root).appendChild(sel); sel.classList.remove('sel'); sel = null; }
  });
  build();
}

/* Paare finden: Begriff ↔ Erklärung. pairs: [[begriff, erklärung], ...] */
function matcher(root, pairs) {
  let selL = null, selR = null, done = 0, tries = 0;
  function build() {
    done = 0; tries = 0;
    const L = shuffle(pairs.map((p, k) => k)), R = shuffle(pairs.map((p, k) => k));
    root.innerHTML = `<div class="match"><div class="match-col">${L.map(k => `<button class="match-card term" data-k="${k}">${pairs[k][0]}</button>`).join('')}</div>
      <div class="match-col">${R.map(k => `<button class="match-card def" data-k="${k}">${pairs[k][1]}</button>`).join('')}</div></div>
      <div class="controls"><span class="score">Gefunden: <b>0</b> / ${pairs.length}</span><button class="btn" data-m="reset">Neu mischen</button><span class="sort-fb" aria-live="polite"></span></div>`;
  }
  root.addEventListener('click', e => {
    if (e.target.closest('[data-m="reset"]')) return build();
    const c = e.target.closest('.match-card'); if (!c || c.classList.contains('ok')) return;
    const isL = c.classList.contains('term');
    if (isL) { if (selL) selL.classList.remove('sel'); selL = selL === c ? null : c; } else { if (selR) selR.classList.remove('sel'); selR = selR === c ? null : c; }
    if (selL) selL.classList.add('sel'); if (selR) selR.classList.add('sel');
    if (selL && selR) {
      tries++;
      const a = selL, b = selR;
      if (a.dataset.k === b.dataset.k) { a.classList.add('ok'); b.classList.add('ok'); done++; $('.sort-fb', root).textContent = done === pairs.length ? `Alle Paare gefunden – mit ${tries} Versuchen!` : 'Passt!'; }
      else { a.classList.add('err'); b.classList.add('err'); setTimeout(() => { a.classList.remove('err'); b.classList.remove('err'); }, 650); $('.sort-fb', root).textContent = 'Passt nicht. Versuch es noch einmal.'; }
      a.classList.remove('sel'); b.classList.remove('sel'); selL = selR = null;
      $('.score b', root).textContent = done;
    }
  });
  build();
}


/* ---------- allgemeine Bausteine ---------- */
const col = c => !c ? C.ink : c[0] === '#' || c.startsWith('rgb') ? c : (C[c.replace(/-/g, '')] || c);

const numDE = (v, d = 2) => (+v).toLocaleString('de-DE', {maximumFractionDigits: d});

const parseNum = s => parseFloat(String(s).trim().replace(/\s/g, '').replace(',', '.'));

function cloze(root, text) {
  const ans = [];
  const body = text.replace(/\{([^}]+)\}/g, (m, g) => {
    const opts = g.split('|'), k = ans.length; ans.push(opts[0]);
    return `<select data-k="${k}" aria-label="Lücke ${k + 1}"><option value="">…</option>${shuffle(opts.slice()).map(x => `<option>${x}</option>`).join('')}</select>`;
  });
  root.classList.add('cloze');
  root.innerHTML = `<div class="cloze-text">${body}</div>
    <div class="controls"><button class="btn primary" data-c="check">Prüfen</button><button class="btn" data-c="solve">Lösung zeigen</button><button class="btn" data-c="reset">Zurücksetzen</button><span class="sort-fb" aria-live="polite"></span></div>`;
  root.addEventListener('change', e => { if (e.target.matches('select')) e.target.className = ''; });
  root.addEventListener('click', e => {
    const b = e.target.closest('[data-c]'); if (!b) return;
    const sels = $$('select', root), fb = $('.sort-fb', root);
    if (b.dataset.c === 'reset') { sels.forEach(s => { s.value = ''; s.className = ''; }); fb.textContent = ''; return; }
    if (b.dataset.c === 'solve') sels.forEach(s => s.value = ans[+s.dataset.k]);
    let ok = 0, empty = 0;
    sels.forEach(s => { const g = s.value === ans[+s.dataset.k]; if (!s.value) empty++; s.className = s.value ? (g ? 'ok' : 'err') : ''; if (g) ok++; });
    fb.innerHTML = ok === sels.length ? '<b class="good">Alles richtig!</b>' : `<b>${ok}</b> von ${sels.length} Lücken richtig${empty ? ` · ${empty} noch leer` : ''}.`;
  });
}

function trueFalse(root, items, o = {}) {
  root.classList.add('tf');
  function build() {
    const ks = shuffle(items.map((x, k) => k)).slice(0, o.pick || items.length);
    root.innerHTML = `<ol class="tf-list">${ks.map(k => `<li data-k="${k}"><p class="tf-t">${items[k].t}</p><div class="tf-btns"><button class="btn" data-v="1">${(o.labels || [])[0] || 'stimmt'}</button><button class="btn" data-v="0">${(o.labels || [])[1] || 'stimmt nicht'}</button></div><p class="tf-why"></p></li>`).join('')}</ol>
      <div class="controls" style="margin-top:.8rem"><span class="score">Richtig: <b>0</b> / ${ks.length}</span><button class="btn" data-tf="reset">Neue Runde</button></div>`;
  }
  root.addEventListener('click', e => {
    if (e.target.closest('[data-tf]')) return build();
    const b = e.target.closest('[data-v]'); if (!b) return;
    const li = b.closest('li'); if (li.dataset.done) return;
    li.dataset.done = 1;
    const it = items[+li.dataset.k], good = (b.dataset.v === '1') === it.ok;
    li.classList.add(good ? 'ok' : 'err'); b.classList.add(good ? 'ok' : 'err');
    $$('[data-v]', li).forEach(x => x.disabled = true);
    $('.tf-why', li).innerHTML = (good ? '<b class="good">Richtig erkannt.</b> ' : '<b class="bad">Leider nein.</b> ') + `Die Aussage ${it.ok ? 'stimmt' : 'stimmt nicht'}. ${it.why || ''}`;
    $('.score b', root).textContent = $$('li.ok', root).length;
  });
  build();
}

function taskSet(root, make, o = {}) {
  const n = o.n || 6;
  let tasks = [];
  root.innerHTML = `<div class="tasks-head"><div class="score"></div><div class="controls"><button class="btn" data-ts="all">Alle prüfen</button>${o.fixed ? '' : '<button class="btn primary" data-ts="new">Neue Aufgaben</button>'}</div></div><div class="tasks"></div>`;
  const box = $('.tasks', root);
  const norm = s => String(s).toLowerCase().replace(/\s+/g, '').replace(/[–−‐]/g, '-').replace(/[₀-₉]/g, c => '0123456789'['₀₁₂₃₄₅₆₇₈₉'.indexOf(c)]).replace(/[⁰¹²³⁴-⁹⁺⁻]/g, c => ({'⁰':'0','¹':'1','²':'2','³':'3','⁴':'4','⁵':'5','⁶':'6','⁷':'7','⁸':'8','⁹':'9','⁺':'+','⁻':'-'})[c]);
  const isNum = f => typeof f.a === 'number';
  function okField(f, v) {
    if (String(v).trim() === '') return null;
    if (isNum(f)) { const x = parseNum(v); return isFinite(x) && Math.abs(x - f.a) <= (f.tol ?? 0) + 1e-9; }
    if (f.cs) return (Array.isArray(f.a) ? f.a : [f.a]).some(a => String(a).replace(/\s/g, '') === String(v).replace(/\s/g, ''));
    return (Array.isArray(f.a) ? f.a : [f.a]).some(a => norm(a) === norm(v));
  }
  const show = f => isNum(f) ? numDE(f.a, 3) : (Array.isArray(f.a) ? f.a[0] : f.a);
  function newTasks() {
    const seen = new Set(); tasks = []; let guard = 0;
    while (tasks.length < n && guard++ < 400) { const t = make(tasks.length); const key = t.key || t.q; if (seen.has(key) && guard < 300) continue; seen.add(key); tasks.push(t); }
    box.innerHTML = tasks.map((t, i) => `<div class="task" data-i="${i}"><header><span>Aufgabe ${i + 1}</span>${t.tag ? `<span>${t.tag}</span>` : ''}</header>
      <div class="task-q">${t.q}</div>
      <div class="fields">${t.fields.map((f, j) => `<label${f.wide || t.fields.length === 1 ? ' class="wide"' : ''}><i>${f.l}</i><span class="inrow"><input type="text" ${isNum(f) ? 'inputmode="decimal"' : ''} data-j="${j}" autocomplete="off" spellcheck="false">${f.unit ? `<small>${f.unit}</small>` : ''}</span></label>`).join('')}</div>
      <div class="actions"><button class="btn primary" data-act="check">Prüfen</button><button class="btn" data-act="solve">Lösung</button></div><p class="fb" aria-live="polite"></p></div>`).join('');
    score();
  }
  function check(i) {
    const t = tasks[i], card = $(`.task[data-i="${i}"]`, box), fb = $('.fb', card);
    const ins = $$('input', card), res = ins.map((x, j) => okField(t.fields[j], x.value));
    if (res.every(r => r === null)) { fb.className = 'fb'; fb.textContent = 'Trage zuerst deine Antwort ein.'; return; }
    ins.forEach((x, j) => x.className = res[j] === null ? '' : res[j] ? 'ok' : 'err');
    t.ok = res.every(r => r === true);
    fb.className = 'fb ' + (t.ok ? 'ok' : 'err');
    fb.innerHTML = t.ok ? (t.good || 'Richtig!') : (t.hint || 'Noch nicht richtig. Versuch es noch einmal.');
    card.classList.toggle('ok', t.ok); score();
  }
  function solve(i) { const t = tasks[i], card = $(`.task[data-i="${i}"]`, box); $$('input', card).forEach((x, j) => x.value = show(t.fields[j])); check(i); }
  function score() { $('.score', root).innerHTML = `Richtig gelöst: <b>${tasks.filter(t => t.ok).length}</b> von ${tasks.length}`; }
  box.addEventListener('click', e => { const b = e.target.closest('[data-act]'); if (!b) return; const i = +b.closest('.task').dataset.i; b.dataset.act === 'check' ? check(i) : solve(i); });
  box.addEventListener('keydown', e => { if (e.key === 'Enter' && e.target.matches('input')) check(+e.target.closest('.task').dataset.i); });
  root.addEventListener('click', e => { const b = e.target.closest('[data-ts]'); if (!b) return; if (b.dataset.ts === 'new') newTasks(); else tasks.forEach((t, i) => { if ($$(`.task[data-i="${i}"] input`, box).some(x => x.value !== '')) check(i); }); });
  newTasks();
  return {renew: newTasks};
}

function quizTable(table, bQuiz, bAll) {
  table.addEventListener('click', e => { const td = e.target.closest('td.q'); if (td) td.classList.add('shown'); });
  if (bQuiz) bQuiz.onclick = () => { table.classList.add('quiz'); $$('td.q', table).forEach(td => td.classList.remove('shown')); };
  if (bAll) bAll.onclick = () => $$('td.q', table).forEach(td => td.classList.add('shown'));
}

function flipCards(root, cards) {
  root.classList.add('flips');
  root.innerHTML = cards.map(([f, b]) => `<button class="flip"><span class="f">${f}</span><span class="b">${b}</span></button>`).join('');
  root.addEventListener('click', e => { const c = e.target.closest('.flip'); if (c) c.classList.toggle('on'); });
}

function seg(root, opts, onPick, start) {
  root.classList.add('seg'); root.setAttribute('role', 'group');
  root.innerHTML = opts.map(([v, t]) => `<button data-v="${v}" aria-pressed="false">${t}</button>`).join('');
  const pick = v => { $$('button', root).forEach(b => b.setAttribute('aria-pressed', b.dataset.v === String(v))); onPick(v); };
  root.onclick = e => { const b = e.target.closest('button'); if (b) pick(b.dataset.v); };
  pick(start ?? opts[0][0]);
  return pick;
}

function stepper(root, n, onStep, o = {}) {
  let k = 0;
  root.innerHTML = `<button class="btn" data-st="-1">← Zurück</button><span class="st-pos"></span><button class="btn primary" data-st="1">${o.next || 'Weiter'} →</button>${o.reset !== false ? '<button class="btn" data-st="0">Von vorn</button>' : ''}`;
  root.classList.add('controls');
  const upd = () => { $('.st-pos', root).textContent = `Schritt ${k + 1} / ${n}`; $('[data-st="-1"]', root).disabled = k === 0; $('[data-st="1"]', root).disabled = k === n - 1; onStep(k); };
  root.addEventListener('click', e => { const b = e.target.closest('[data-st]'); if (!b) return; const d = +b.dataset.st; k = d === 0 ? 0 : clamp(k + d, 0, n - 1); upd(); });
  upd();
  return {go(i) { k = clamp(i, 0, n - 1); upd(); }, get k() { return k; }};
}

function canvasLoop(cv, station, draw) {
  let t = 0;
  visuals.push({station, tick(dt) { if (!cv.clientWidth) return; t += RM.matches ? 0 : dt; const {ctx, w, h} = setup(cv); LABELQ = []; try { draw(ctx, w, h, t, dt); } finally { flushLabels(); } }});
}

function wrapText(ctx, text, x, y, maxW, lh, o = {}) {
  const words = String(text).split(' '); let line = '', yy = y;
  lh = lh * fs(o.size || 13) / (o.size || 13); ctx.font = `${o.weight || 400} ${fs(o.size || 13)}px ${o.font || SANS}`; ctx.fillStyle = o.color || C.ink; ctx.textAlign = o.align || 'left'; ctx.textBaseline = 'top';
  for (const w of words) { const tst = line ? line + ' ' + w : w; if (ctx.measureText(tst).width > maxW && line) { ctx.fillText(line, x, yy); line = w; yy += lh; } else line = tst; }
  if (line) ctx.fillText(line, x, yy);
  return yy + lh;
}

function arrow(ctx, x1, y1, x2, y2, c, lw = 2.5, head = 10) {
  const a = Math.atan2(y2 - y1, x2 - x1);
  ctx.strokeStyle = col(c); ctx.fillStyle = col(c); ctx.lineWidth = lw; ctx.lineCap = 'round';
  ctx.beginPath(); ctx.moveTo(x1, y1); ctx.lineTo(x2 - Math.cos(a) * head * .6, y2 - Math.sin(a) * head * .6); ctx.stroke();
  ctx.beginPath(); ctx.moveTo(x2, y2); ctx.lineTo(x2 - head * Math.cos(a - .45), y2 - head * Math.sin(a - .45)); ctx.lineTo(x2 - head * Math.cos(a + .45), y2 - head * Math.sin(a + .45)); ctx.closePath(); ctx.fill();
}

function axes(ctx, w, h, o) {
  const p = Object.assign({l: 56, r: 18, t: 18, b: 44}, o.pad || {});
  const X = v => p.l + (v - o.x[0]) / (o.x[1] - o.x[0]) * (w - p.l - p.r);
  const Y = v => h - p.b - (v - o.y[0]) / (o.y[1] - o.y[0]) * (h - p.t - p.b);
  ctx.lineWidth = 1; ctx.strokeStyle = alpha(C.ink2, .18);
  for (const v of o.yt || []) { ctx.beginPath(); ctx.moveTo(p.l, Y(v)); ctx.lineTo(w - p.r, Y(v)); ctx.stroke(); label(ctx, (o.yf || String)(v), p.l - 8, Y(v), {align: 'right', size: 11, color: C.ink2, weight: 400, font: SANS}); }
  for (const v of o.xt || []) label(ctx, (o.xf || String)(v), X(v), h - p.b + 14, {size: 11, color: C.ink2, weight: 400, font: SANS});
  ctx.strokeStyle = C.ink2; ctx.lineWidth = 1.5; ctx.beginPath(); ctx.moveTo(p.l, p.t); ctx.lineTo(p.l, h - p.b); ctx.lineTo(w - p.r, h - p.b); ctx.stroke();
  if (o.xl) label(ctx, o.xl, (p.l + w - p.r) / 2, h - 10, {size: 12, color: C.ink2, weight: 700});
  if (o.yl) { ctx.save(); ctx.translate(14, (p.t + h - p.b) / 2); ctx.rotate(-Math.PI / 2); label(ctx, o.yl, 0, 0, {size: 12, color: C.ink2, weight: 700}); ctx.restore(); }
  return {X, Y, p};
}

function polyline(ctx, pts, c, lw = 2.5, dash) {
  ctx.strokeStyle = col(c); ctx.lineWidth = lw; ctx.lineJoin = 'round'; ctx.lineCap = 'round'; ctx.setLineDash(dash || []);
  ctx.beginPath(); pts.forEach(([x, y], i) => i ? ctx.lineTo(x, y) : ctx.moveTo(x, y)); ctx.stroke(); ctx.setLineDash([]);
}

function dotAt(ctx, x, y, c, r = 5) { ctx.fillStyle = col(c); ctx.beginPath(); ctx.arc(x, y, r, 0, 7); ctx.fill(); ctx.strokeStyle = C.surface; ctx.lineWidth = 2; ctx.stroke(); }

function donut(ctx, cx, cy, r, parts, o = {}) {
  const tot = parts.reduce((s, p) => s + p.v, 0); let a = -Math.PI / 2;
  parts.forEach((p, i) => {
    const da = p.v / tot * Math.PI * 2;
    ctx.fillStyle = col(p.c); ctx.beginPath(); ctx.arc(cx, cy, r, a, a + da); ctx.arc(cx, cy, r * (o.inner ?? .58), a + da, a, true); ctx.closePath(); ctx.fill();
    ctx.strokeStyle = C.surface; ctx.lineWidth = 2; ctx.stroke();
    if (o.hl === i) { ctx.strokeStyle = C.ink; ctx.lineWidth = 3; ctx.beginPath(); ctx.arc(cx, cy, r + 5, a, a + da); ctx.stroke(); }
    a += da;
  });
}

const pick = a => a[Math.floor(Math.random() * a.length)];

const randInt = (a, b) => a + Math.floor(Math.random() * (b - a + 1));

function selfCheck(root, items) {
  root.classList.add('selfcheck');
  root.innerHTML = items.map((it, k) => `<li><span>${it.t}</span><span style="display:flex;gap:.6rem;align-items:center;flex-wrap:wrap"><span class="seg" data-k="${k}"><button aria-pressed="false" data-v="2">sicher</button><button aria-pressed="false" data-v="1">geht so</button><button aria-pressed="false" data-v="0">unsicher</button></span>${it.href ? `<a href="${it.href}">wiederholen →</a>` : ''}</span></li>`).join('') + '<li class="sc-sum"><span class="note">Markiere ehrlich. Wo du unsicher bist, führt der Link zur passenden Station.</span><b class="sc-out"></b></li>';
  root.addEventListener('click', e => {
    const b = e.target.closest('[data-v]'); if (!b) return;
    $$('button', b.parentElement).forEach(x => x.setAttribute('aria-pressed', x === b));
    const vals = $$('.seg', root).map(s => { const p = $('[aria-pressed="true"]', s); return p ? +p.dataset.v : null; }).filter(v => v !== null);
    $('.sc-out', root).textContent = `${vals.filter(v => v === 2).length} sicher · ${vals.filter(v => v === 1).length} geht so · ${vals.filter(v => v === 0).length} unsicher`;
  });
}
