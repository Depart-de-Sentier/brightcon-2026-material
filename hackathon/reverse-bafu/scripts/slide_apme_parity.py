"""Render the flow-parity plot of the 12 worst-matching rebuilds, the APME eco-profiles, as a PNG for the deck.

    uv run python scripts/slide_apme_parity.py [--project bafu-2026]   # needs results/flow_comparison.json and google-chrome

The 12 are picked as in `slide_pooled_parity.py --drop-worst 12`: the counted rebuilds with the
largest median |log10(rebuilt / original)| over the flows both sides have. Every flow of the 12 is
split in two by the original dataset itself:

  declared   the eco-profile lists the flow in its own biosphere exchanges (~140 per dataset: the
             substances the industry survey recorded)
  link-only  the flow reaches the original only through its waste-treatment links (the other ~1,600,
             mostly 1e-15-level traces)

Declared flows are drawn as dots, link-only flows as a density, on the axes of the pooled plot. The
script prints, per dataset, the median log10 offset (rebuilt / original) of each group and the share
of link-only flows above the line: the numbers the slide quotes. Writes
artifacts/presentation/screenshots/apme-parity.png.
"""

import argparse
import glob
import json
import statistics
import subprocess
import tempfile
from math import log10
from pathlib import Path

import bw2data as bd

from flow_comparison import MultiSystem
from reverse_bafu import db
from reverse_bafu import spec as spec_mod
from slide_pooled_parity import crop_rows, median_miss

W, H = 1400, 1300
OUT = Path("artifacts/presentation/screenshots/apme-parity.png")

PAGE = """<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;500;600&display=swap">
<style>html,body{margin:0;background:#ffffff}canvas{display:block}</style></head><body>
<canvas id="c" width="%(W)d" height="%(H)d"></canvas>
<script id="data" type="application/json">%(DATA)s</script>
<script>
const P = JSON.parse(document.getElementById('data').textContent);   // [original, rebuilt, declared]
const SUP = {'-':'\\u207b','0':'\\u2070','1':'\\u00b9','2':'\\u00b2','3':'\\u00b3','4':'\\u2074','5':'\\u2075','6':'\\u2076','7':'\\u2077','8':'\\u2078','9':'\\u2079'};
const sup = n => String(n).split('').map(c => SUP[c] || c).join('');
function draw() {
  const g = document.getElementById('c').getContext('2d'), Wd = %(W)d, Ht = %(H)d;
  const M = {l: 150, r: 28, t: 24, b: 128}, B = 22;
  const X0 = M.l + B + 8, X1 = Wd - M.r, Y0 = M.t, Y1 = Ht - M.b - B - 8;
  let vmax = 0; for (const [o, m] of P) vmax = Math.max(vmax, o, m);
  const SPAN = 24, hi = Math.ceil(Math.log10(vmax) + 0.05), lo = hi - SPAN, NX = 150, NY = 150;
  const fx = v => (Math.log10(v) - lo) / SPAN, cell = v => Math.min(NX - 1, Math.max(0, Math.floor(fx(v) * NX)));
  const sx = v => X0 + fx(v) * (X1 - X0), sy = v => Y1 - fx(v) * (Y1 - Y0);
  const cells = new Map(), bottom = new Map(), left = new Map(), inc = (m, k) => m.set(k, (m.get(k) || 0) + 1);
  const dots = [], dotsB = [], dotsL = [];
  for (const [o, m, dec] of P) {
    if (dec) { if (o > 0 && m > 0) dots.push([o, m]); else if (o > 0) dotsB.push(o); else if (m > 0) dotsL.push(m); continue; }
    if (o > 0 && m > 0) inc(cells, cell(o) + NX * cell(m)); else if (o > 0) inc(bottom, cell(o)); else if (m > 0) inc(left, cell(m));
  }
  let cmax = 1; cells.forEach(c => { cmax = Math.max(cmax, c); });
  const a = c => 0.12 + 0.88 * Math.log(1 + c) / Math.log(1 + cmax);
  const cw = (X1 - X0) / NX, ch = (Y1 - Y0) / NY;
  g.font = '500 30px "Quicksand", sans-serif'; g.fillStyle = '#7E857F'; g.strokeStyle = '#E3DBCF'; g.lineWidth = 2;
  for (let d = Math.ceil(lo / 4) * 4; d <= hi; d += 4) {
    const x = sx(10 ** d), y = sy(10 ** d);
    g.beginPath(); g.moveTo(x, Y0); g.lineTo(x, Y1); g.stroke(); g.beginPath(); g.moveTo(X0, y); g.lineTo(X1, y); g.stroke();
    g.textAlign = 'center'; g.fillText('10' + sup(d), x, Y1 + B + 8 + 40);
    g.textAlign = 'right'; g.fillText('10' + sup(d), M.l - 14, y + 10);
  }
  g.textAlign = 'center'; g.fillStyle = '#555B57'; g.font = '500 30px "Quicksand", sans-serif';
  g.fillText('original elementary flow', (X0 + X1) / 2, Y1 + B + 8 + 92);
  g.save(); g.translate(34, (Y0 + Y1) / 2); g.rotate(-Math.PI / 2); g.fillText('rebuilt elementary flow', 0, 0); g.restore();
  const band = (f, fill) => { g.fillStyle = fill; g.beginPath(); g.moveTo(sx(10 ** lo), sy(10 ** lo * f)); g.lineTo(sx(10 ** hi / f), sy(10 ** hi));
    g.lineTo(sx(10 ** hi), sy(10 ** hi)); g.lineTo(sx(10 ** hi), sy(10 ** hi / f)); g.lineTo(sx(10 ** lo * f), sy(10 ** lo)); g.lineTo(sx(10 ** lo), sy(10 ** lo)); g.closePath(); g.fill(); };
  band(2, 'rgba(132,174,153,0.16)'); band(1.1, 'rgba(132,174,153,0.45)');
  g.fillStyle = 'rgba(60,83,67,0.06)'; g.fillRect(X0, Y1 + 8, X1 - X0, B); g.fillRect(M.l, Y0, B, Y1 - Y0);
  // link-only flows: a warm density
  cells.forEach((c, k) => { g.fillStyle = `rgba(168,96,63,${a(c)})`; g.fillRect(X0 + (k %% NX) * cw, Y1 - (Math.floor(k / NX) + 1) * ch, Math.ceil(cw), Math.ceil(ch)); });
  bottom.forEach((c, i) => { g.fillStyle = `rgba(168,96,63,${a(c)})`; g.fillRect(X0 + i * cw, Y1 + 8, Math.ceil(cw), B); });
  left.forEach((c, j) => { g.fillStyle = `rgba(168,96,63,${a(c)})`; g.fillRect(M.l, Y1 - (j + 1) * ch, B, Math.ceil(ch)); });
  g.strokeStyle = '#2B2B2B'; g.lineWidth = 2.5; g.beginPath(); g.moveTo(sx(10 ** lo), sy(10 ** lo)); g.lineTo(sx(10 ** hi), sy(10 ** hi)); g.stroke();
  // declared flows: dark dots with a white ring, on top
  const dot = (x, y) => { g.beginPath(); g.arc(x, y, 6, 0, 2 * Math.PI); g.fillStyle = '#3C5343'; g.fill(); g.lineWidth = 1.5; g.strokeStyle = '#FFFFFF'; g.stroke(); };
  for (const [o, m] of dots) dot(sx(o), sy(m));
  for (const o of dotsB) dot(sx(o), Y1 + 8 + B / 2);
  for (const m of dotsL) dot(M.l + B / 2, sy(m));
  document.title = 'done';
}
Promise.all([document.fonts.load('500 30px "Quicksand"'), document.fonts.load('600 30px "Quicksand"')]).catch(() => {}).then(draw);
</script></body></html>"""


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--project", default="bafu-2026")
    a = ap.parse_args()
    doc = json.loads(Path("results/flow_comparison.json").read_text())
    labels = [tuple(f) for f in doc["flows"]]                       # row -> (name, compartment, unit)
    counted = [s for s in doc["specs"] if s["counted"]]
    worst = sorted(counted, key=median_miss, reverse=True)[:12]
    db.set_project(a.project)
    # the rows of flow_comparison.json are the rows of its MultiSystem; rebuild it from the same nodes
    # (every spec's original and its -disagg rebuild, in spec order) to map rows to flow ids exactly -
    # several rows can share a (name, compartment, unit) label
    nodes = []
    for path in sorted(glob.glob("specs/*.json")):
        sp = spec_mod.load(path)
        nodes += [bd.get_node(database=db.INVENTORY_DB, code=sp.target_code),
                  bd.get_node(database=db.SANDBOX_DB, code=f"{spec_mod.node_prefix(sp)}-disagg")]
    sys_ = MultiSystem(nodes)
    assert sys_.n_flows == len(labels), (sys_.n_flows, len(labels))
    row_of = sys_.lca.dicts.biosphere          # flow id -> row
    points, rows_out = [], []
    for s in worst:
        node = bd.get_node(database=db.INVENTORY_DB, code=s["code"])
        declared = {row_of[e.input.id] for e in node.biosphere() if e["amount"] and e.input.id in row_of}
        dec_off, link_off = [], []
        for r, o, m in s["flows"]:
            if o < 0 or m < 0:
                continue
            is_dec = r in declared
            points.append([o, m, is_dec])
            if o > 0 and m > 0:
                (dec_off if is_dec else link_off).append(log10(m / o))
        above = sum(x > 0 for x in link_off) / len(link_off) if link_off else float("nan")
        rows_out.append((s["name"], s["strategy"], s["detected_by"], len(dec_off), len(link_off),
                         statistics.median(dec_off) if dec_off else float("nan"), statistics.median(link_off), above))
    print(f"{'dataset':45s} route detected  declared  link-only  median offset (decades) declared / link-only  link-only above line")
    for n, route, det, nd, nl, md, ml, ab in rows_out:
        print(f"{n[:45]:45s} {route:5s} {det:9s} {nd:8d} {nl:10d}   {md:+.2f} / {ml:+.2f}   {ab:.0%}")
    dec_all = [log10(m / o) for o, m, d in points if d and o > 0 and m > 0]
    link_all = [log10(m / o) for o, m, d in points if not d and o > 0 and m > 0]
    print(f"pooled: {len(points):,} flows; declared {len(dec_all):,} (median {statistics.median(dec_all):+.2f}), "
          f"link-only {len(link_all):,} (median {statistics.median(link_all):+.2f}, {sum(x > 0 for x in link_all) / len(link_all):.0%} above the line)")
    with tempfile.TemporaryDirectory() as tmp:
        page = Path(tmp) / "apme.html"
        page.write_text(PAGE % {"W": W, "H": H, "DATA": json.dumps(points)})
        OUT.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["google-chrome", "--headless=new", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
                        "--force-device-scale-factor=1", f"--window-size={W},{H + 200}", "--virtual-time-budget=8000",
                        f"--screenshot={OUT.resolve()}", page.resolve().as_uri()],
                       check=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL, timeout=120)
    crop_rows(OUT, H)
    print(f"-> {OUT}")


if __name__ == "__main__":
    main()
