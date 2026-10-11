"""Build artifacts/replacement-priority.html from results/replacement_priority.csv
(run scripts/replacement_priority.py first).

    python scripts/build_replacement_page.py
"""
import csv
import json
from pathlib import Path

CATEGORIES = [
    "Climate change", "Acidification", "EF-particulate Matter", "Ecotoxicity, freshwater",
    "Eutrophication marine", "Eutrophication, freshwater", "Eutrophication, terrestrial",
    "Human toxicity, cancer", "Human toxicity, non-cancer", "Ionising radiation, human health",
    "Land use", "Ozone depletion", "Photochemical ozone formation - human health",
    "Resource use, fossils", "Resource use, minerals and metals", "Water use",
]
NUM = ("importance", "importance_median", "importance_climate", "dominant_share")
INT = ("breadth", "datasets_driven_climate", "direct_consumers", "blocks_our_rebuilds")

rows = []
for r in csv.DictReader(open("results/replacement_priority.csv")):
    cats = [float(r[k]) for k in r if k.startswith("imp_")]
    x = {k: v for k, v in r.items() if not k.startswith("imp_")}
    for k in NUM:
        x[k] = float(x[k])
    for k in INT:
        x[k] = int(x[k])
    x["cats"] = cats
    rows.append(x)
assert len(rows[0]["cats"]) == len(CATEGORIES)

data = json.dumps({"categories": CATEGORIES, "rows": rows}, ensure_ascii=False, separators=(",", ":"))
tmpl = Path("scripts/templates/replacement-priority.tmpl.html").read_text()
out = Path("artifacts/replacement-priority.html")
out.write_text(tmpl.replace("/*DATA*/", data.replace("</", "<\\/")))
print(f"-> {out} ({out.stat().st_size / 1e3:.0f} kB, {len(rows)} system processes)")
