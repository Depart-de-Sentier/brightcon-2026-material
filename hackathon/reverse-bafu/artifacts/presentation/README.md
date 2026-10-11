# The Brightcon 2026 presentation

[dis-aggregating-system-processes.pdf](dis-aggregating-system-processes.pdf) is the deck as
presented: eight slides and three backup slides.

The source is `deck.json` (slide order and sections) and one HTML section per slide in
`slides/`, with the speaker notes in each slide's `<aside>`. The slides refer to their images by
the id the slide tool stored them under (`/_blob/<id>`). The files are in `screenshots/`, and
`scripts/slide_deck_pdf.py` maps each id to its file. To rebuild the PDF from these sources
(needs google-chrome):

```bash
uv run python scripts/slide_deck_pdf.py
```

| # | Slide | Numbers from | Image, made by |
|---|---|---|---|
| 1 | `cover`: Dis-aggregating system processes | – | – |
| 2 | `the-101`: The system processes we looked at | `results/system_terminated_extended.csv`, `results/usable_information.csv` | – |
| 3 | `pipeline`: Five steps from system process to unit process | `specs/` | – |
| 4 | `evidence-ranges`: Seven inputs exact, six only as ranges (cement ZN/D) | `specs/c3490cfc-cement-zn-d.json` | `cement-zn-tab-3-14.png`, a crop of the cited report page |
| 5 | `benchmark`: We built 100 system processes from unit processes, then dis-aggregate them | `results/benchmark/flow-n100-seed7.csv`, `blind-all-n100-seed7.csv` | `amount-parity-{bounded,oracle,distractors,blind-all}.png`, `scripts/slide_amount_parity.py` |
| 6 | `real-cases`: The 51 system-processes dis-aggregated | `results/flow_comparison.json`, `results/climate_comparison.csv` | `pooled-parity.png`, `scripts/slide_pooled_parity.py` |
| 7 | `apme-eco-profiles`: The 12 worst matches: APME eco-profiles | `results/flow_comparison.json`, `results/ecoprofile_agreement.csv` | `apme-parity.png`, `scripts/slide_apme_parity.py` |
| 8 | `community`: What works, what's next | `exports/`, `results/benchmark/flow-n100-seed7.csv` | – |
| 9 | `evidence-exact` (backup): burnt shale | `specs/d8ec4be3-burnt-shale.json` | `burnt-shale-tab-3-9.png`, a crop of the cited report page |
| 10 | `evidence-no-number` (backup): anthraquinone | `specs/e6293140-anthraquinone-at-plant.draft.json` | `anthraquinone-tab-44-3.png`, `anthraquinone-energy.png`, crops of the cited report page |
| 11 | `evidence-not-this-dataset` (backup): titanium dioxide | `specs/f29ea928-…`, `specs/bc92bf5a-…` | `tio2-confidential-85-3.png`, a crop of the cited report page |

The report crops show pages of the reports in the BAFU-2026 documentation bundle, cited on
each slide. The plot scripts read the committed result files, so they run without Brightway
(except `slide_apme_parity.py`, which needs the `bafu-2026` project to tell each dataset's
declared flows from the rest).
