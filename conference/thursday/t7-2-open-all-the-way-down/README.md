# Open all the way down: a food database rebuilt on BAFU, live in Firefly for Brightway

**Session T7 — Open data · Thursday 24 September 2026, 16:00 · Manuel Klarmann, Eaternity (Zürich)**

Slides for the talk, as a self-contained HTML deck (no notebooks, no Python environment — nothing to install).

- **Live deck:** https://eos-lci.gitlab.io/eos-lci-presentations/brightcon-2026/
- **PDF export:** [`slides.pdf`](slides.pdf) (static; the live embeds and the turning icons are frozen)

## Open it locally

```bash
cd conference/thursday/t7-2-open-all-the-way-down
python3 -m http.server 8092      # then open http://localhost:8092/
```

Keys: → / Space next · ← previous · Home / End · the dots bottom-right are clickable · `#N` in the URL opens slide N.
Slide 2 consumes six "next" presses (the icon turns twice through its three faces). Two slides embed live pages
(the lci-workbench flow chart on slide 12 and the Flit app on slide 20) — they need an internet connection.

## What the talk introduces

1. **Firefly** — a glossary-first, web-based interface for Brightway: https://brightway.eaternity.ch ·
   source https://gitlab.com/eaternity/firefly (AGPL-3.0)
2. **EDB → BAFU/UVEK** — the Eaternity food inventory database rebuilt on Switzerland's public BAFU/UVEK background:
   19,289 inventories across 29 databases, zero ecoinvent references, built by 73 open tributary modules —
   https://gitlab.com/eos-lci (Apache-2.0 code, CC-BY-4.0 data) · browse: https://lci-workbench-0d71e7.gitlab.io
3. **The assistant** — a chat drawer in Firefly running Claude with a Brightway MCP server behind it.

## Licence

Slides: CC-BY-4.0. Deck rendering code (`engine.js`, `custom.js`): Apache-2.0. Screenshots of Firefly and
lci-workbench are © Eaternity AG, CC-BY-4.0. The Claude and Anthropic word marks belong to Anthropic PBC.
