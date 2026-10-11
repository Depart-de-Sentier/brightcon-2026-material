"""Print the presentation in artifacts/presentation/ to a PDF, one 1920x1080 page per slide.

    python scripts/slide_deck_pdf.py     # needs google-chrome

The deck's source is `deck.json` (slide order) and one HTML section per slide under `slides/`. The
slides refer to their images by the id the slide tool stored them under (`/_blob/<id>`); IMAGES maps
each id to its file in `screenshots/`. The slides are joined into one page with the layout defaults
the slide tool applies (sections and plain divs are flex columns, headings and paragraphs have no
margins, speaker notes in <aside> are hidden) and printed with headless Chrome. Writes
artifacts/presentation/dis-aggregating-system-processes.pdf.
"""

import json
import re
import subprocess
import tempfile
from pathlib import Path

DECK = Path("artifacts/presentation")
OUT = DECK / "dis-aggregating-system-processes.pdf"
IMAGES = {
    "1e7cf3b8761586503f107b8dc9a6f8f9": "cement-zn-tab-3-14.png",
    "feb8c3de253d50cb17bf78fc36557541": "amount-parity-bounded.png",
    "0c9e12b826b6225cf3ad717c19f90b0c": "amount-parity-oracle.png",
    "c0c25951ed0efaa6158a4f5c881ea6a1": "amount-parity-distractors.png",
    "6292c2eea49e2fb75fe380116b260865": "amount-parity-blind-all.png",
    "c8428376effbbeb0bef17ed5f7a7c9c3": "pooled-parity.png",
    "43fa9eac0507ff6ce7758d01941bef9a": "apme-parity.png",
    "a249cd491caefafc03aa37d5cbb1f37b": "burnt-shale-tab-3-9.png",
    "7a96e0109c9ab247526c1c7f75d5a030": "anthraquinone-tab-44-3.png",
    "20793df789a0bdc6fb3035f694742c2c": "anthraquinone-energy.png",
    "139a2408efbd2f9f3cfc90f907132949": "tio2-confidential-85-3.png",
}

HEAD = """<!doctype html><html><head><meta charset="utf-8"><title>TITLE</title>
<link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@300;400;500;600;700&display=swap" rel="stylesheet"><style>
@page { size: 1920px 1080px; margin: 0 }
html, body { margin: 0; padding: 0; background: #F0E9E1 }
* { box-sizing: border-box; -webkit-print-color-adjust: exact; print-color-adjust: exact }
section { position: relative; width: 1920px; height: 1080px; overflow: hidden;
          font-family: 'Quicksand', Arial, sans-serif; break-after: page; page-break-after: always }
section:last-of-type { break-after: auto; page-break-after: auto }
section:not([style*="display"]), div:not([style*="display"]) { display: flex; flex-direction: column }
h1, h2, h3, p { margin: 0 }
h1 { font-size: 96px; font-weight: 600; line-height: 1.1 }
h2 { font-size: 64px; font-weight: 600; line-height: 1.15 }
h3 { font-size: 44px; font-weight: 600; line-height: 1.2 }
p { font-size: 32px; line-height: 1.4 }
svg { display: block; flex: none }
img { display: block; flex: none }
aside { display: none }
table { border-collapse: collapse; width: 100% }
td, th { padding: 0.35em 0.6em; text-align: left; border: 1px solid rgba(43, 43, 43, 0.12) }
th { font-weight: 600 }
x-shape { display: block; flex: none }
x-shape[kind="arrow-right"] { clip-path: polygon(0 30%, 60% 30%, 60% 0, 100% 50%, 60% 100%, 60% 70%, 0 70%) }
</style></head><body>"""


def image(match: re.Match) -> str:
    blob = match.group(1)
    if blob not in IMAGES:
        raise SystemExit(f"slide image /_blob/{blob} has no file in IMAGES")
    return (DECK / "screenshots" / IMAGES[blob]).resolve().as_uri()


def main() -> None:
    deck = json.loads((DECK / "deck.json").read_text())
    slides = [(DECK / "slides" / f"{sid}.html").read_text() for sid in deck["order"]]
    page = HEAD.replace("TITLE", deck["title"]) + "".join(re.sub(r"/_blob/([0-9a-f]+)", image, s) for s in slides) + "</body></html>"
    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / "deck.html"
        src.write_text(page)
        subprocess.run(["google-chrome", "--headless=new", "--disable-gpu", "--no-sandbox", "--no-pdf-header-footer",
                        "--virtual-time-budget=15000", f"--print-to-pdf={OUT.resolve()}", src.as_uri()],
                       check=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL, timeout=180)
    print(f"{len(slides)} slides -> {OUT}")


if __name__ == "__main__":
    main()
