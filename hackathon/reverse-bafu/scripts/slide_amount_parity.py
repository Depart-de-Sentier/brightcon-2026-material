"""Render one input-amount parity plot per benchmark row (fitted vs true amount) as PNGs for the deck.

    uv run python scripts/slide_amount_parity.py     # needs the two detail files below and google-chrome

Reads results/benchmark/flow-n100-seed7-detail.json (complete list, ranges, padded list) and
results/benchmark/blind-all-n100-seed7-detail.json (no list, every dataset a candidate), and writes
artifacts/presentation/screenshots/amount-parity-<scenario>.png for the four panels of the deck's
benchmark slide, all on the same log axes.

Each dot is one input of one synthetic case. The dots are the inputs the benchmark scores: true
inputs that supply >= 1 % of some flow of the target ("material"). A material true input that ends at
zero, or was left off the list (partial), is drawn in the strip under the x axis at its true amount.
A candidate that is not a true input but gets a material amount (a wrong input used) is drawn in the
strip left of the y axis at its fitted amount. Non-positive true amounts (a scrap credit) are skipped.
Same palette and scale as slide_pooled_parity.py.
"""

import json
import subprocess
import tempfile
from pathlib import Path

from slide_pooled_parity import crop_rows

S = 640
OUT = Path("artifacts/presentation/screenshots")
SOURCES = [("oracle", "results/benchmark/flow-n100-seed7-detail.json"), ("bounded", "results/benchmark/flow-n100-seed7-detail.json"),
           ("distractors", "results/benchmark/flow-n100-seed7-detail.json"), ("blind-all", "results/benchmark/blind-all-n100-seed7-detail.json")]
LO, HI = -19, 10          # decades on both axes, the same for every panel

PAGE = """<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Quicksand:wght@500;600&display=swap">
<style>html,body{margin:0;background:#ffffff}canvas{display:block}</style></head><body>
<canvas id="c" width="%(S)d" height="%(S)d"></canvas>
<script id="data" type="application/json">%(DATA)s</script>
<script>
const P = JSON.parse(document.getElementById('data').textContent), LO = %(LO)d, HI = %(HI)d, SPAN = HI - LO;
const SUP = {'-':'\\u207b','0':'\\u2070','1':'\\u00b9','2':'\\u00b2','3':'\\u00b3','4':'\\u2074','5':'\\u2075','6':'\\u2076','7':'\\u2077','8':'\\u2078','9':'\\u2079'};
const sup = n => String(n).split('').map(c => SUP[c] || c).join('');
function draw() {
  const g = document.getElementById('c').getContext('2d'), S = %(S)d;
  const M = {l: 118, r: 14, t: 14, b: 92}, B = 26;
  const X0 = M.l + B + 8, X1 = S - M.r, Y0 = M.t, Y1 = S - M.b - B - 8;
  const f = v => Math.min(1, Math.max(0, (Math.log10(v) - LO) / SPAN));
  const sx = v => X0 + f(v) * (X1 - X0), sy = v => Y1 - f(v) * (Y1 - Y0);
  const jit = (i, w) => ((i * 2654435761) %% 1000) / 1000 * (w - 10) + 5;   // deterministic spread across a strip
  g.font = '500 34px "Quicksand", sans-serif'; g.fillStyle = '#7E857F'; g.strokeStyle = '#E3DBCF'; g.lineWidth = 2;
  for (let d = -15; d <= HI; d += 10) {
    const x = sx(10 ** d), y = sy(10 ** d);
    g.beginPath(); g.moveTo(x, Y0); g.lineTo(x, Y1); g.stroke(); g.beginPath(); g.moveTo(X0, y); g.lineTo(X1, y); g.stroke();
    g.textAlign = 'center'; g.fillText('10' + sup(d), x, Y1 + B + 8 + 44);
    g.textAlign = 'right'; g.fillText('10' + sup(d), M.l - 12, y + 12);
  }
  g.fillStyle = 'rgba(60,83,67,0.06)'; g.fillRect(X0, Y1 + 8, X1 - X0, B); g.fillRect(M.l, Y0, B, Y1 - Y0);
  g.strokeStyle = '#2B2B2B'; g.lineWidth = 2.5; g.beginPath(); g.moveTo(sx(10 ** LO), sy(10 ** LO)); g.lineTo(sx(10 ** HI), sy(10 ** HI)); g.stroke();
  P.hit.forEach(([t, m]) => { g.fillStyle = 'rgba(60,83,67,0.45)'; g.beginPath(); g.arc(sx(t), sy(m), 6, 0, 2 * Math.PI); g.fill(); });
  g.fillStyle = 'rgba(176,96,64,0.55)';
  P.lost.forEach((t, i) => { g.beginPath(); g.arc(sx(t), Y1 + 8 + jit(i + 1, B), 5, 0, 2 * Math.PI); g.fill(); });
  P.wrong.forEach((m, i) => { g.beginPath(); g.arc(M.l + jit(i + 7, B), sy(m), 5, 0, 2 * Math.PI); g.fill(); });
  document.title = 'done';
}
document.fonts.load('500 34px "Quicksand"').catch(() => {}).then(draw);
</script></body></html>"""


def points(cases: list, sc: str) -> dict:
    hit, lost, wrong = [], [], []
    for c in cases:
        for r in c["scenarios"][sc]["candidates"]:
            t, x = r["truth"], r["fitted"]
            if r["role"] in ("true input", "withheld") and r["material_true"]:
                if t is None or t <= 0:
                    continue
                (hit.append([t, x]) if x and x > 0 else lost.append(t))
            elif r["role"] not in ("true input", "withheld") and r["material_fitted"]:
                wrong.append(x)
    return {"hit": hit, "lost": lost, "wrong": wrong}


def main() -> None:
    cache: dict[str, list] = {}
    OUT.mkdir(parents=True, exist_ok=True)
    for sc, src in SOURCES:
        if src not in cache:
            cache[src] = json.loads(Path(src).read_text())
        cases = cache[src]
        p = points(cases, sc)
        png = OUT / f"amount-parity-{sc}.png"
        with tempfile.TemporaryDirectory() as tmp:
            page = Path(tmp) / "p.html"
            page.write_text(PAGE % {"S": S, "LO": LO, "HI": HI, "DATA": json.dumps(p)})
            subprocess.run(["google-chrome", "--headless=new", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
                            "--force-device-scale-factor=1", f"--window-size={S},{S + 200}", "--virtual-time-budget=8000",
                            f"--screenshot={png.resolve()}", page.resolve().as_uri()],
                           check=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL, timeout=120)
        crop_rows(png, S)
        print(f"-> {png}  {len(p['hit'])} scored, {len(p['lost'])} lost, {len(p['wrong'])} wrong inputs used")


if __name__ == "__main__":
    main()
