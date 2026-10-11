"""Build artifacts/flow-parity.html from results/flow_comparison.json (run scripts/flow_comparison.py first).

    python scripts/build_flow_parity.py
"""
from pathlib import Path

data = Path("results/flow_comparison.json").read_text()
tmpl = Path("scripts/templates/flow-parity.tmpl.html").read_text()
out = Path("artifacts/flow-parity.html")
out.write_text(tmpl.replace("/*DATA*/", data.replace("</", "<\\/")))
print(f"-> {out} ({out.stat().st_size / 1e6:.1f} MB)")
