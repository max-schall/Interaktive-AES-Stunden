# GHS-Gefahrenpiktogramme

Offizielle Piktogramme GHS01–GHS09 aus dem Download der BGHM
(https://www.bghm.de/arbeitsschuetzer/praxishilfen/sicherheitszeichen/kennzeichnung-von-gefahrstoffen,
Datei `Gefahrstoffe.zip`, 500 × 500 px GIF), auf 240 × 240 px verkleinert und als PNG gespeichert.

`build.py` bettet sie als Data-URI (`GHS_IMG`) in jede Stunde ein, die `GHS_IMG` verwendet,
damit die Dateien eigenständig bleiben.
