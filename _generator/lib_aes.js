/* ================= AES-Bausteine ================= */
/* Linien-Symbole (24 × 24, Kontur). icon('apfel') → <svg> */
const ICONS = {
  apfel: 'M12 7c-1.5-1.6-5-1.8-6.6.6C3.6 10.4 5 16 7.6 18.6c1.4 1.4 2.8 1 4.4.4 1.6.6 3 1 4.4-.4C19 16 20.4 10.4 18.6 7.6 17 5.2 13.5 5.4 12 7zM12 7c0-2 1-3.4 2.6-4',
  karotte: 'M14.5 9.5 4 20m10.5-10.5c1.5 1.5 1 3.5-.5 5L8 20H4v-4l5.5-6c1.5-1.5 3.5-2 5-.5zM15 9l3-3m-2.5 4.5L20 9m-6-3 1-4',
  brot: 'M5 11a3 3 0 0 1 1-6h12a3 3 0 0 1 1 6v8H5zM9 9v1m3-1v1m3-1v1',
  fisch: 'M3 12c3-5 9-6 13-2l4-3v10l-4-3c-4 4-10 3-13-2zM8 11v.01',
  ei: 'M12 3c-3.5 0-6 6-6 10a6 6 0 0 0 12 0c0-4-2.5-10-6-10z',
  milch: 'M8 3h8M9 3v3l-2 3v12h10V9l-2-3V3M7 13h10',
  fleisch: 'M3.5 11c0-4.5 4.5-7 9.5-7s8.5 3 8.5 7.5-4 8.5-9.5 8.5S3.5 16 3.5 11zM7.5 10c1.5-2 4.5-2.5 6.5-1M13.3 13a2.2 2.2 0 1 0 4.4 0a2.2 2.2 0 1 0 -4.4 0',
  oel: 'M10 2h4v3l2 3v12a2 2 0 0 1-2 2h-4a2 2 0 0 1-2-2V8l2-3zM10 5h4M12 12c-1.3 1.6-2 2.7-2 3.5a2 2 0 0 0 4 0c0-.8-.7-1.9-2-3.5z',
  tropfen: 'M12 3s-6 7-6 11a6 6 0 0 0 12 0c0-4-6-11-6-11z',
  zucker: 'M4 9l8-5 8 5v8l-8 4-8-4zM4 9l8 4 8-4M12 13v8',
  salz: 'M8 9h8l1 12H7zM9 9V6a3 3 0 0 1 6 0v3M11 4v.01M13 4v.01',
  blatt: 'M5 19c0-9 5-14 15-14 0 10-5 15-14 15M5 19l8-8',
  messer: 'M8 14.5 3 19.5l1.5 1.5 5-5M8 14.5 20 3c1.5 4 .5 8-3 11l-5.5 5.5z',
  topf: 'M4 10h16v6a4 4 0 0 1-4 4H8a4 4 0 0 1-4-4zM2 10h2m16 0h2M9 6c0-1 1-1 1-2m4 2c0-1 1-1 1-2',
  pfanne: 'M2 10h15l-1.4 5.8a2 2 0 0 1-2 1.5H5.4a2 2 0 0 1-2-1.5zM17 11.3l5-1.6',
  flamme: 'M12 21a6 6 0 0 0 6-6c0-4-3-6-3-9-2 1-3 3-3 5-1-1-2-2-2-4-2 2-4 5-4 8a6 6 0 0 0 6 6z',
  thermo: 'M14 14V5a2 2 0 0 0-4 0v9a4 4 0 1 0 4 0zM12 17v.01M12 9v6',
  schnee: 'M12 2v20M4 7l16 10M20 7 4 17M9 4l3 2 3-2M9 20l3-2 3 2',
  sonne: 'M12 8a4 4 0 1 0 0 8 4 4 0 0 0 0-8zM12 2v2m0 16v2M4.9 4.9l1.4 1.4m11.4 11.4 1.4 1.4M2 12h2m16 0h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4',
  mond: 'M20 14A8 8 0 1 1 10 4a6 6 0 0 0 10 10z',
  uhr: 'M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18zM12 7v5l3 2',
  kalender: 'M4 6h16v14H4zM4 10h16M8 3v4m8-4v4',
  herz: 'M12 20s-8-5-8-11a4.5 4.5 0 0 1 8-2.5A4.5 4.5 0 0 1 20 9c0 6-8 11-8 11z',
  gehirn: 'M9 4a3 3 0 0 0-3 3 3 3 0 0 0-2 5 3 3 0 0 0 2 5 3 3 0 0 0 6 1V5a3 3 0 0 0-3-1zM15 4a3 3 0 0 1 3 3 3 3 0 0 1 2 5 3 3 0 0 1-2 5 3 3 0 0 1-6 1',
  auge: 'M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12zM12 9a3 3 0 1 0 0 6 3 3 0 0 0 0-6z',
  ohr: 'M7 9a5 5 0 0 1 10 0c0 3-3 4-3 7a3 3 0 0 1-6 0M10 9a2 2 0 0 1 4 0',
  nase: 'M12 3c0 5-4 9-4 12a2 2 0 0 0 2 2h1m5-2a2 2 0 0 1-2 2h-1',
  mund: 'M4 12c3 4 13 4 16 0M4 12c3-2 6-2 8-1 2-1 5-1 8 1',
  hand: 'M18 11V6a2 2 0 0 0-4 0M14 10V4a2 2 0 0 0-4 0v2M10 10.5V6a2 2 0 0 0-4 0v8M18 8a2 2 0 1 1 4 0v6a8 8 0 0 1-8 8h-2c-2.8 0-4.5-.86-5.99-2.34l-3.6-3.6a2 2 0 0 1 2.83-2.82L7 15',
  person: 'M12 4a4 4 0 1 0 0 8 4 4 0 0 0 0-8zM4 21a8 8 0 0 1 16 0',
  gruppe: 'M9 5a3 3 0 1 0 0 6 3 3 0 0 0 0-6zM3 20a6 6 0 0 1 12 0M16 5a3 3 0 0 1 0 6m2 9a6 6 0 0 0-3-5',
  haus: 'M3 11 12 3l9 8M5 9v11h14V9M10 20v-6h4v6',
  euro: 'M18 6a7 7 0 1 0 0 12M4 10h9M4 14h9',
  wagen: 'M3 4h2l2.5 11h10L20 7H6.5M9 20a1 1 0 1 0 0-.01M17 20a1 1 0 1 0 0-.01',
  shirt: 'M8 3 3 6l2 5 2-1v11h10V10l2 1 2-5-5-3a4 4 0 0 1-8 0z',
  kreislauf: 'M20 12a8 8 0 0 1-14 5.3M4 12a8 8 0 0 1 14-5.3M18 2.5v4.2h-4.2M6 21.5v-4.2h4.2',
  erde: 'M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18zM3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18',
  fuss: 'M8 3c2 0 3 2 3 5s-1 5-3 5-3-2-3-5 1-5 3-5zM6 16h4v2a2 2 0 0 1-4 0zM16 7c2 0 3 2 3 4s-1 4-3 4-3-2-3-4 1-4 3-4zM14 18h4v1a2 2 0 0 1-4 0z',
  paket: 'M3 7l9-4 9 4v10l-9 4-9-4zM3 7l9 4 9-4M12 11v10M7.5 5l9 4',
  muell: 'M4 7h16M9 7V4h6v3M6 7l1 13h10l1-13M10 11v6m4-6v6',
  lkw: 'M2 6h11v10H2zM13 9h4l4 4v3h-8M6 19a2 2 0 1 0 0-.01M17 19a2 2 0 1 0 0-.01',
  fabrik: 'M3 21V10l6 4V10l6 4V6h4v15zM7 18h2m4 0h2',
  etikett: 'M3 12V4h8l10 10-8 8zM7.5 8a.5.5 0 1 0 0-.01',
  schild: 'M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z',
  schildok: 'M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6zM8.5 12l2.5 2.5 4.5-5',
  plus: 'M4 4h16v16H4zM12 8v8M8 12h8',
  smile: 'M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18zM8 14c1 1.5 2.5 2 4 2s3-.5 4-2M9 9v.01M15 9v.01',
  blitz: 'M13 2 4 14h7l-1 8 9-12h-7z',
  bett: 'M3 18V6m0 7h18v5M3 13V9h7v4m11 0v-2a3 3 0 0 0-3-3h-8',
  musik: 'M9 18V5l11-2v13M9 18a3 3 0 1 1-6 0 3 3 0 0 1 6 0zM20 16a3 3 0 1 1-6 0 3 3 0 0 1 6 0z',
  sprechen: 'M4 5h16v11H9l-5 4z',
  handy: 'M7 2h10v20H7zM11 18h2',
  rad: 'M2.5 16a3.5 3.5 0 1 0 7.0 0a3.5 3.5 0 1 0 -7.0 0M14.5 16a3.5 3.5 0 1 0 7.0 0a3.5 3.5 0 1 0 -7.0 0M6 16l4-7h5.5l2.5 7M10 9l2.5 7H6M15.5 9 14.5 6H17M10 9 9 7H7',
  laufen: 'M14 4a2 2 0 1 0 0-.01M10 21l2-6-3-3 2-5 4 3h3M6 12l3-4m3 7 3 2v4',
  waage: 'M12 3v18M5 21h14M4 8h16M4 8 2 14a3 3 0 0 0 4 0zM20 8l-2 6a3 3 0 0 0 4 0z',
  buch: 'M4 4h6a2 2 0 0 1 2 2v14a2 2 0 0 0-2-2H4zM20 4h-6a2 2 0 0 0-2 2v14a2 2 0 0 1 2-2h6z',
  idee: 'M9 18h6M10 21h4M12 3a6 6 0 0 0-4 10.5c.6.6 1 1.5 1 2.5h6c0-1 .4-1.9 1-2.5A6 6 0 0 0 12 3z',
  ziel: 'M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18zM12 7a5 5 0 1 0 0 10 5 5 0 0 0 0-10zM12 11a1 1 0 1 0 0 2 1 1 0 0 0 0-2z',
  warn: 'M12 3 2 20h20zM12 10v4M12 17v.01',
  check: 'M5 12l4 4 10-10',
  kreuz: 'M6 6l12 12M18 6 6 18',
  stern: 'M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z',
  lupe: 'M10 4a6 6 0 1 0 0 12 6 6 0 0 0 0-12zM15 15l6 6',
  schere: 'M6 4a3 3 0 1 0 0 6 3 3 0 0 0 0-6zM6 14a3 3 0 1 0 0 6 3 3 0 0 0 0-6zM8.5 8.5 20 20M8.5 15.5 20 4',
  nadel: 'M19 3 5 17l-2 4 4-2L21 5zM16 6l2 2M17 4.5l2.5 2.5',
  pinsel: 'M18 3l3 3-9 9-3-3zM9 12c-3 0-5 2-5 5 0 2-1 3-2 4 4 0 8-1 9-4z',
  koffer: 'M3 8h18v12H3zM8 8V5h8v3M3 13h18',
  welle: 'M2 8c3-3 5 3 8 0s5 3 8 0 4 0 4 0M2 14c3-3 5 3 8 0s5 3 8 0 4 0 4 0',
  wind: 'M3 8h11a3 3 0 1 0-3-3M3 12h16a3 3 0 1 1-3 3M3 16h7',
  baby: 'M12 4a5 5 0 1 0 0 10 5 5 0 0 0 0-10zM10 9v.01M14 9v.01M10.5 11.5c.8.6 2.2.6 3 0M7 21l2-5h6l2 5',
  waschen: 'M3 7h18l-2 13H5zM3 7l2-3h14l2 3M8 13c1.5-1.5 2.5 1.5 4 0s2.5 1.5 4 0',
  wlan: 'M2 9a15 15 0 0 1 20 0M5 13a10 10 0 0 1 14 0M8.5 16.5a5 5 0 0 1 7 0M12 20v.01',
  info: 'M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18zM12 11v6M12 7.5v.01',
  baum: 'M12 22v-6M12 2 5 12h4l-3 4h12l-3-4h4z',
  wasserhahn: 'M4 10h9a3 3 0 0 1 3 3v1M4 7v6M16 17v.01M16 20v.01M9 10V6h3',
  schuessel: 'M3 11h18a9 9 0 0 1-18 0zM8 7c0-1 1-1 1-2m3 2c0-1 1-1 1-2m3 2c0-1 1-1 1-2',
  loeffel: 'M12 2c2.8 0 4.5 2.4 4.5 5S14.6 11.5 12 11.5 7.5 9.6 7.5 7 9.2 2 12 2zM12 11.5V22',
  kuehl: 'M6 2h12v20H6zM6 9h12M9 5v2M9 12v3',
  telefon: 'M5 3h3.5l2 5-2.5 1.5a11 11 0 0 0 5.5 5.5L15 12.5l5 2V18a2 2 0 0 1-2 2A15 15 0 0 1 3 5a2 2 0 0 1 2-2z',
  glas: 'M6 3h12l-1.6 17.1a1 1 0 0 1-1 .9H8.6a1 1 0 0 1-1-.9zM6.7 10c2-1 3.5 1 5.3 0s3.3-1 5.3 0',
  huelse: 'M3 16c5 4 13 2 17-7 .8-2 1-4 1-6-2 .3-3.5 1.2-4.5 2.5C13 11 8 13 3 16zM7.0 14.6a1.5 1.5 0 1 0 3.0 0a1.5 1.5 0 1 0 -3.0 0M10.9 12.4a1.5 1.5 0 1 0 3.0 0a1.5 1.5 0 1 0 -3.0 0M14.3 9.2a1.5 1.5 0 1 0 3.0 0a1.5 1.5 0 1 0 -3.0 0',
  aehre: 'M12 22V9M12 9c-1.6-1.6-1.6-4.4 0-6 1.6 1.6 1.6 4.4 0 6zM12 13c-3 0-4.5-1.8-4.5-4 2.4 0 4.5 1.5 4.5 4zM12 13c3 0 4.5-1.8 4.5-4-2.4 0-4.5 1.5-4.5 4zM12 17.5c-3 0-4.5-1.8-4.5-4 2.4 0 4.5 1.5 4.5 4zM12 17.5c3 0 4.5-1.8 4.5-4-2.4 0-4.5 1.5-4.5 4z',
  bonbon: 'M7.8 12a4.2 4.2 0 1 0 8.4 0a4.2 4.2 0 1 0 -8.4 0M8.3 10 3 6.5v11L8.3 14M15.7 10 21 6.5v11L15.7 14M10.5 10.5l3 3',
  teller: 'M6.5 12a5.5 5.5 0 1 0 11.0 0a5.5 5.5 0 1 0 -11.0 0M9 12a3 3 0 1 0 6 0a3 3 0 1 0 -6 0M2.5 3.5v5a1.5 1.5 0 0 0 3 0v-5M4 10v10.5M21.5 3.5c-1.6 1-2.2 3-2.2 6.5h2.2v10.5',
  reibe: 'M7 4h10l2 17H5zM9 4a3 3 0 0 1 6 0M9.5 9h1.5m2 0h1.5M9 13h1.5m2.5 0h1.5M8.5 17h1.5m3.5 0h1.5',
  hobel: 'M4 3h9l7 18h-9zM6.7 9.5h8.8M9 14.5a3 1.3 0 0 0 6 0',
  wellholz: 'M7 9h10a1 1 0 0 1 1 1v4a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1v-4a1 1 0 0 1 1-1zM6 12H2.5M18 12h3.5M2.5 10.5v3M21.5 10.5v3',
  sieb: 'M3 9h14a7 7 0 0 1-14 0zM17 10.5l4.5-3M6.5 13h7M8 16h4',
  kelle: 'M4 12h12a6 6 0 0 1-12 0zM16 12V4.5a2 2 0 0 1 4 0V6',
  schaumkelle: 'M3 15a6 6 0 1 0 12 0a6 6 0 1 0 -12 0M7 13v.01M11 13v.01M9 15.5v.01M7 18v.01M11 18v.01M13.3 10.7 21 3',
  schneebesen: 'M12 22v-6M12 16C7 12 7 3 12 2c5 1 5 10 0 14zM12 16c-2-4-2-11 0-14 2 3 2 10 0 14z',
  ruehrgeraet: 'M4 4h11l3 3v3H7a3 3 0 0 1-3-3zM9 10v4m6-4v4M9 14c-2 2.3-2 5 0 7 2-2 2-4.7 0-7zM15 14c-2 2.3-2 5 0 7 2-2 2-4.7 0-7z',
  stabmixer: 'M9 2h6v9l-1 2h-4l-1-2zM12 5v2M11 13v4m2-4v4M7.5 17h9L15 21H9z',
  schaber: 'M12 2v10M8 12h8v5a4 4 0 0 1-4 4 4 4 0 0 1-4-4z',
  stecker: 'M9 2v5M15 2v5M6 7h12v4a6 6 0 0 1-12 0zM12 17v5',
  wolle: 'M3.5 13a7.5 7.5 0 1 0 15.0 0a7.5 7.5 0 1 0 -15.0 0M4.5 10.5c4 .5 8.5 5 9.5 10M4 15c3.5 0 6.5 2.5 7.5 5.5M8.5 6c5 .5 9.5 5 10 11M15.5 6.5 21.5 2.5',
  werkzeug: 'M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z',
  tausch: 'M7 7h10l-3-3M17 17H7l3 3M20 10v4M4 14v-4',
  magen: 'M8 2v4C5 7 3 10 4 14c1 5 6 8 11 6 3-1 5-4 5-7s-2-5-4.5-5-3.5 1.5-4.5.5S10 6.5 10 5V2',
  darm: 'M6 21V6a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v15M9.5 8h5a1 1 0 0 1 0 2.5h-5a1 1 0 0 0 0 2.5h5a1 1 0 0 1 0 2.5h-5a1 1 0 0 0 0 2.5H13',
  batterie: 'M3 7h15a1 1 0 0 1 1 1v8a1 1 0 0 1-1 1H3zM19 10h2v4h-2M6.5 10v4M10 10v4M13.5 10v4',
  zitrone: 'M3 13a9 9 0 0 0 18 0zM6.5 13a5.5 5.5 0 0 0 11 0M12 13v8M12 13l-5 5M12 13l5 5',
  becher: 'M5 5h12v13a3 3 0 0 1-3 3H8a3 3 0 0 1-3-3zM17 8h1.5a2.5 2.5 0 0 1 0 5H17M5 10h3m-3 4h3',
  saegemesser: 'M2 10.5h5v3H2zM7 9h14.5v3l-1.25 1.5L19 12l-1.25 1.5L16.5 12l-1.25 1.5L14 12l-1.25 1.5L11.5 12l-1.25 1.5L9 12l-1.25 1.5L7 12.5z',
  wiegemesser: 'M3 13c3 8 15 8 18 0zM5 13V6.5m14 6.5V6.5M3.5 5h3M17.5 5h3',
  schaeler: 'M10.5 13h3v9h-3zM12 13c-4 0-6-3-6-9M12 13c4 0 6-3 6-9M6 4h12M8.5 7h7',
  besteck: 'M7 3c2 0 3 2 3 4s-1 3-2 3v11M17 3v6c0 1-1 2-2 2v10M15 3v4m4-4v4',
  ringe: 'M7 6a5 1.6 0 1 0 10 0a5 1.6 0 1 0 -10 0M6 10a6 1.8 0 1 0 12 0a6 1.8 0 1 0 -12 0M5.5 14a6.5 2 0 1 0 13.0 0a6.5 2 0 1 0 -13.0 0M5 18.5a7 2.2 0 1 0 14 0a7 2.2 0 1 0 -14 0',
  kuh: 'M7 8C5 8 3 7 2 5c2 0 4 .5 5 1.5M17 8c2 0 4-1 5-3-2 0-4 .5-5 1.5M7 6.5c1-1.5 3-2 5-2s4 .5 5 2V14c0 1-.5 2-1.5 2.5L14 18v1.5a2 2 0 0 1-4 0V18l-1.5-1.5C7.5 16 7 15 7 14zM10 18h.01M14 18h.01M9.5 10v.01M14.5 10v.01',
  heu: 'M3 8a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2zM3 12.5h18M8 6v13M16 6v13',
  mist: 'M3 19c1-4 4-6 6-6 1-2 3-3 5-2 2 .5 3 2 3 4 2 .5 4 2 4 4zM9 9c-1-1 0-2 0-3M13 8c-1-1 0-2 0-3M17 10c-1-1 0-2 0-3',
  wender: 'M12 22v-9M8 13h8l1-10H7zM10.5 6v4M13.5 6v4'
};
function icon(name, cls = 'ico') { const d = ICONS[name]; return d ? `<svg class="${cls}" viewBox="0 0 24 24" aria-hidden="true"><path d="${d}"/></svg>` : ''; }

/* Kacheln mit Detailansicht: items [{ico, t, d (HTML), sub}]  o: {cols2, first}  */
function explore(root, items, o = {}) {
  root.classList.add('explore');
  root.innerHTML = `<div class="ex-tiles${o.cols2 ? ' cols2' : ''}">${items.map((it, k) => `<button class="ex-tile" data-k="${k}" aria-pressed="false">${icon(it.ico)}<b>${it.t}</b>${it.sub ? `<small>${it.sub}</small>` : ''}</button>`).join('')}</div>
    <div class="ex-panel" aria-live="polite"><p class="muted">${o.hint || 'Wähle eine Karte aus.'}</p></div>${o.count === false ? '' : `<p class="ex-count">Angesehen: <b>0</b> / ${items.length}</p>`}`;
  const show = k => {
    $$('.ex-tile', root).forEach(b => b.setAttribute('aria-pressed', +b.dataset.k === k));
    const b = $(`.ex-tile[data-k="${k}"]`, root); b.classList.add('seen');
    const it = items[k];
    $('.ex-panel', root).innerHTML = `<h4>${it.t}</h4>${/^\s*</.test(it.d) ? it.d : `<p>${it.d}</p>`}`;
    const c = $('.ex-count b', root); if (c) c.textContent = $$('.ex-tile.seen', root).length;
    if (o.onPick) o.onPick(k);
  };
  root.addEventListener('click', e => { const b = e.target.closest('.ex-tile'); if (b) show(+b.dataset.k); });
  if (o.first != null) show(o.first);
  return {show};
}

/* Reihenfolge herstellen: steps = richtige Reihenfolge (Texte) */
function sequence(root, steps, o = {}) {
  root.classList.add('seq');
  let order = [];
  const build = () => {
    do { order = shuffle(steps.map((s, k) => k)); } while (steps.length > 2 && order.every((v, i) => v === i));
    draw();
  };
  const draw = (mark) => {
    root.innerHTML = `${o.intro ? `<p class="muted" style="margin:0">${o.intro}</p>` : ''}<ol class="seq-list">${order.map((k, i) => `<li data-i="${i}" class="${mark ? (k === i ? 'ok' : 'err') : ''}"><span>${steps[k]}</span><span class="mv"><button data-mv="-1" aria-label="nach oben" ${i === 0 ? 'disabled' : ''}>↑</button><button data-mv="1" aria-label="nach unten" ${i === order.length - 1 ? 'disabled' : ''}>↓</button></span></li>`).join('')}</ol>
      <div class="controls"><button class="btn primary" data-q="check">Prüfen</button><button class="btn" data-q="solve">Lösung</button><button class="btn" data-q="new">Neu mischen</button><span class="sort-fb" aria-live="polite">${mark ? (order.every((v, i) => v === i) ? '<b class="good">Richtige Reihenfolge!</b>' + (o.done ? ' ' + o.done : '') : `<b>${order.filter((v, i) => v === i).length}</b> von ${steps.length} an der richtigen Stelle.`) : ''}</span></div>`;
  };
  root.addEventListener('click', e => {
    const mv = e.target.closest('[data-mv]'), q = e.target.closest('[data-q]');
    if (mv) { const i = +mv.closest('li').dataset.i, j = i + +mv.dataset.mv; [order[i], order[j]] = [order[j], order[i]]; draw(); const b = $(`li[data-i="${j}"] [data-mv="${mv.dataset.mv}"]`, root) || $(`li[data-i="${j}"] button`, root); if (b) b.focus(); return; }
    if (!q) return;
    if (q.dataset.q === 'new') return build();
    if (q.dataset.q === 'solve') order = steps.map((s, k) => k);
    draw(true);
  });
  build();
}

/* Balkendiagramm (HTML): data [{l, v, c, note}]  o: {unit, max, dec, sort, hl} */
function bars(root, data, o = {}) {
  const max = o.max || Math.max(...data.map(d => d.v));
  const list = o.sort ? data.slice().sort((a, b) => b.v - a.v) : data;
  root.classList.add('bars');
  root.innerHTML = list.map(d => `<div class="bar-row${d.hl ? ' hl' : ''}" title="${d.note || ''}"><span class="bl">${d.l}</span><span class="bt"><i style="width:0;--c:${d.c ? col(d.c) : 'var(--accent)'}" data-w="${Math.max(.5, d.v / max * 100)}"></i></span><span class="bv">${numDE(d.v, o.dec ?? 1)}${o.unit ? ' ' + o.unit : ''}</span></div>`).join('') + (o.note ? `<p class="bars-note">${o.note}</p>` : '');
  requestAnimationFrame(() => requestAnimationFrame(() => $$('i[data-w]', root).forEach(i => i.style.width = i.dataset.w + '%')));
}

/* Rechner: inputs [{id, l, min, max, step, v, unit, opts:[[wert, text]]}], out(vals) -> HTML */
function calc(root, inputs, out) {
  root.classList.add('calc');
  root.innerHTML = inputs.map(f => f.opts
    ? `<div class="opts"><span>${f.l}</span><div data-seg="${f.id}"></div></div>`
    : `<div class="slider"><label for="c-${f.id}">${f.l} <output id="o-${f.id}"></output></label><input type="range" id="c-${f.id}" min="${f.min}" max="${f.max}" step="${f.step || 1}" value="${f.v}"></div>`).join('') + '<div class="calc-out" aria-live="polite"></div>';
  const vals = {};
  const upd = () => {
    inputs.forEach(f => { if (!f.opts) { vals[f.id] = +$('#c-' + f.id, root).value; $('#o-' + f.id, root).textContent = numDE(vals[f.id], 2) + (f.unit ? ' ' + f.unit : ''); } });
    $('.calc-out', root).innerHTML = out(vals);
  };
  inputs.forEach(f => {
    if (f.opts) seg($(`[data-seg="${f.id}"]`, root), f.opts, v => { vals[f.id] = isNaN(+v) ? v : +v; if (root.dataset.ready) upd(); }, f.v);
    else $('#c-' + f.id, root).addEventListener('input', upd);
  });
  root.dataset.ready = 1; upd();
}

/* Meinungsbarometer: statements [{t, why}] – keine richtige Lösung, Anlass zum Gespräch */
function opinion(root, statements, o = {}) {
  const labs = o.labels || ['stimme gar nicht zu', 'eher nicht', 'unentschieden', 'eher ja', 'stimme voll zu'];
  root.classList.add('opinion');
  root.innerHTML = statements.map((s, k) => `<li data-k="${k}"><p class="ot">${s.t}</p><div class="scale">${labs.map((l, i) => `<button data-v="${i}" aria-pressed="false">${l}</button>`).join('')}</div><p class="ow"></p></li>`).join('');
  root.addEventListener('click', e => {
    const b = e.target.closest('[data-v]'); if (!b) return;
    const li = b.closest('li');
    $$('button', li).forEach(x => x.setAttribute('aria-pressed', x === b));
    const s = statements[+li.dataset.k];
    $('.ow', li).innerHTML = s.why ? '<b>Denkanstoß:</b> ' + s.why : '';
  });
}

/* Checkliste mit Auswertung: items [text], o: {eval(n, total) -> text} */
function checks(root, items, o = {}) {
  root.innerHTML = `<ul class="checks">${items.map((t, k) => `<li><label><input type="checkbox" data-k="${k}"><span>${t}</span></label></li>`).join('')}</ul><p class="checks-out" aria-live="polite"></p>`;
  const upd = () => { const n = $$('input:checked', root).length; $('.checks-out', root).innerHTML = o.eval ? o.eval(n, items.length) : `${n} von ${items.length} angekreuzt.`; };
  root.addEventListener('change', upd); upd();
}

/* Situationen nacheinander entscheiden: cases [{s, a:[...], ok, why}] */
function scenes(root, cases, o = {}) {
  root.classList.add('scene');
  let i = 0, score = 0;
  const show = () => {
    if (i >= cases.length) {
      root.innerHTML = `<div class="scene-card"><span class="sc-n">Auswertung</span><p><b>${score} von ${cases.length}</b> Situationen richtig gelöst. ${score === cases.length ? 'Sehr gut!' : 'Sprecht über die Situationen, die nicht geklappt haben.'}</p></div><div class="controls"><button class="btn primary" data-sc="again">Noch einmal</button></div>`;
      return;
    }
    const c = cases[i], ord = shuffle(c.a.map((x, k) => k));
    root.innerHTML = `<div class="scene-card"><span class="sc-n">${o.label || 'Situation'} ${i + 1} von ${cases.length}</span><p>${c.s}</p></div>
      <div class="scene-opts">${ord.map(k => `<button data-k="${k}">${c.a[k]}</button>`).join('')}</div><p class="scene-fb" aria-live="polite"></p>
      <div class="controls"><button class="btn primary" data-sc="next" hidden>${i + 1 < cases.length ? 'Nächste Situation →' : 'Auswertung'}</button></div>`;
  };
  root.addEventListener('click', e => {
    const a = e.target.closest('[data-sc]');
    if (a) { if (a.dataset.sc === 'again') { i = 0; score = 0; } else i++; return show(); }
    const b = e.target.closest('.scene-opts button'); if (!b || b.disabled) return;
    const c = cases[i], k = +b.dataset.k, ok = k === c.ok;
    if (ok) score++;
    $$('.scene-opts button', root).forEach(x => { x.disabled = true; if (+x.dataset.k === c.ok) x.classList.add('ok'); });
    if (!ok) b.classList.add('err');
    $('.scene-fb', root).innerHTML = (ok ? '<b class="good">Gut gehandelt.</b> ' : '<b class="bad">Besser nicht.</b> ') + (c.why || '');
    $('[data-sc="next"]', root).hidden = false;
  });
  show();
}

/* Markierte Stellen in einem Element (z. B. Etikett) erklären: .hs[data-k], info {k: html} */
function hotspots(root, panel, info) {
  root.addEventListener('click', e => {
    const h = e.target.closest('.hs'); if (!h) return;
    $$('.hs', root).forEach(x => x.classList.toggle('on', x === h));
    h.dataset.seen = 1;
    const n = $$('.hs[data-seen]', root).length, all = new Set($$('.hs', root).map(x => x.dataset.k)).size;
    panel.innerHTML = info[h.dataset.k] + `<p class="ex-count">Entdeckt: <b>${new Set($$('.hs[data-seen]', root).map(x => x.dataset.k)).size}</b> / ${all}</p>`;
  });
}

/* ---------- SVG-Helfer ---------- */
const svgNS = 'http://www.w3.org/2000/svg';
function svgEl(tag, attrs = {}, parent) { const e = document.createElementNS(svgNS, tag); for (const k in attrs) e.setAttribute(k, attrs[k]); if (parent) parent.appendChild(e); return e; }
const PAL = ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7'];
const pal = i => col(PAL[i % PAL.length]);

/* Ringdiagramm als SVG mit anklickbaren Segmenten: parts [{l, v, c}], onPick(k) */
function ringSVG(root, parts, o = {}) {
  const W = o.size || 320, R = W / 2 - 6, r = R * (o.inner ?? .5), cx = W / 2, cy = W / 2;
  const svg = svgEl('svg', {viewBox: `0 0 ${W} ${W}`, class: 'svgfig', role: 'img', 'aria-label': o.aria || 'Kreisdiagramm'});
  const tot = parts.reduce((s, p) => s + p.v, 0); let a = -Math.PI / 2;
  const segs = parts.map((p, k) => {
    const da = p.v / tot * Math.PI * 2, a2 = a + da, large = da > Math.PI ? 1 : 0;
    const P = (rr, ang) => `${cx + rr * Math.cos(ang)} ${cy + rr * Math.sin(ang)}`;
    const d = `M${P(R, a)} A${R} ${R} 0 ${large} 1 ${P(R, a2)} L${P(r, a2)} A${r} ${r} 0 ${large} 0 ${P(r, a)}Z`;
    const g = svgEl('path', {d, fill: col(p.c || PAL[k % 7]), stroke: C.surface, 'stroke-width': 2, class: 'hit', 'data-k': k}, svg);
    if (o.labels !== false && da > .28) { const m = (a + a2) / 2, t = svgEl('text', {x: cx + (R + r) / 2 * Math.cos(m), y: cy + (R + r) / 2 * Math.sin(m), 'text-anchor': 'middle', 'dominant-baseline': 'central', class: 'lbl', fill: '#fff', style: 'fill:#fff;font-size:12px'}, svg); t.textContent = p.short || p.l; }
    a = a2; return g;
  });
  if (o.center) { const t = svgEl('text', {x: cx, y: cy, 'text-anchor': 'middle', 'dominant-baseline': 'central', class: 'lbl', style: 'font-size:15px'}, svg); t.textContent = o.center; }
  root.innerHTML = ''; root.appendChild(svg);
  const pickK = k => { segs.forEach((s, i) => s.classList.toggle('dim', k != null && i !== k)); if (o.onPick) o.onPick(k); };
  svg.addEventListener('click', e => { const s = e.target.closest('[data-k]'); if (s) pickK(+s.dataset.k); });
  return {pick: pickK};
}
