window.DECK = {
 "qrUrl": "https://brightway.eaternity.ch",
 "flitUrl": "https://flit.eaternity.org",
 "singleLang": true,
 "slides": [
  {
   "n": 1,
   "custom": "hero",
   "kicker": "BRIGHTCON 2026 · AALBORG · 24 SEPTEMBER 2026",
   "title": "Manuel Klarmann",
   "body": "Eaternity · Zürich",
   "chipsText": [],
   "logos": [
    "assets/eaternity-logo-on-dark.svg"
   ],
   "logoPlain": true,
   "footnote": ""
  },
  {
   "n": 2,
   "custom": "three-icons",
   "icons": [
    {
     "icon": "ui",
     "label": "LCA Interface",
     "head": "A glossary-first, web-based interface for LCA",
     "sub": "Firefly"
    },
    {
     "icon": "db",
     "label": "Food Inventories",
     "head": "A complete food inventory database, modelled on the latest science",
     "sub": "EDB → BAFU/UVEK · 73 tributaries"
    },
    {
     "icon": "ai",
     "label": "LCA AI Assistant",
     "head": "An AI assistant for Brightway — the latest models for everyone",
     "sub": "Claude Opus 5.5 + a Brightway MCP"
    }
   ]
  },
  {
   "n": 3,
   "custom": "screenshot-split",
   "frameId": "ff1",
   "visualSide": "right",
   "frameWide": 780,
   "kicker": "PART 1 · FIREFLY · 1 / 6",
   "title": "Firefly",
   "url": "brightway.eaternity.ch",
   "badge": "screenshot",
   "annotations": [
    {
     "title": "Web-based",
     "sub": "log in at brightway.eaternity.ch — or download it for macOS, Windows, Linux"
    },
    {
     "title": "Glossary first",
     "sub": "say what you mean; the inventory follows"
    }
   ],
   "footnote": "",
   "image": "assets/ff-landing.png",
   "icon": "assets/firefly-3.webp",
   "frameHigh": 448
  },
  {
   "n": 4,
   "custom": "full-image",
   "image": "assets/ff-app.png",
   "imageFallback": "assets/firefly-graph-open.png",
   "bg": "#ffffff"
  },
  {
   "n": 5,
   "custom": "dialog-pair",
   "kicker": "PART 1 · FIREFLY · 3 / 6",
   "title": "Works with your database",
   "annotations": [
    {
     "title": "Bring what you have",
     "sub": "a Brightway package or an ILCD zip from openLCA or SimaPro — from a file or straight from a URL"
    },
    {
     "title": "No lock-in",
     "sub": "take a project or a single database back out: Brightway, Excel, openLCA, ILCD, SimaPro — with dependencies and impact methods"
    },
    {
     "title": "The databases you already use",
     "sub": "ecoinvent, Agribalyse, USLCI, ELCD — import the package you are licensed for; bafu-2026 is shared as a Context Database to clone"
    }
   ],
   "importDialog": {
    "title": "Create New Project",
    "sub": "Start a new project or restore one from a backup.",
    "group1": "Start a new project",
    "tiles": [
     {
      "icon": "folder",
      "label": "Empty"
     },
     {
      "icon": "cloud",
      "label": "Remote"
     },
     {
      "icon": "pack",
      "label": "Import",
      "on": true
     }
    ],
    "group2": "Restore from a backup",
    "restore": {
     "icon": "archive",
     "label": "Restore"
    },
    "note": "Create a project from a Brightway data package (.bw2package) or an ILCD .zip package",
    "sourceLabel": "Source",
    "sources": [
     "Upload a file",
     "From a URL"
    ],
    "fileLabel": "Package File",
    "fileHint": ".bw2package · ILCD .zip — the format is detected from the file extension"
   },
   "exportDialog": {
    "title": "Export / Backup",
    "sub": "The export runs in the background and you download the finished file.",
    "scope": "Whole project",
    "formats": [
     {
      "label": "Backup (.tar.gz)",
      "desc": "Exact restore of everything — databases, methods, parameters, setups."
     },
     {
      "label": "BW2Package (Brightway)"
     },
     {
      "label": "Excel (bw2io layout)"
     },
     {
      "label": "openLCA (JSON-LD zip)"
     },
     {
      "label": "ILCD (zip)"
     },
     {
      "label": "SimaPro (CSV)"
     }
    ],
    "button": "Start export"
   },
   "footnote": ""
  },
  {
   "n": 6,
   "custom": "screenshot-split",
   "frameId": "ff4",
   "visualSide": "right",
   "frameWide": 740,
   "kicker": "PART 1 · FIREFLY · 4 / 6",
   "title": "Search — glossary first",
   "url": "brightway.eaternity.ch/browser",
   "badge": "screenshot",
   "annotations": [
    {
     "title": "Your words become glossary terms first",
     "sub": "concept · geography · exclusion · boundary"
    },
    {
     "title": "Inventories ranked by match — and by quality",
     "sub": "one mark per term: carried, left out, declared as left out; the quality score breaks ties"
    },
    {
     "title": "Embedding-based, so it works across languages and vocabularies",
     "sub": "meaning, not keywords — 14 international vocabularies behind it"
    }
   ],
   "footnote": "",
   "image": "assets/ff-search.png",
   "mockActive": "Browse",
   "mockText": "⌘K",
   "frameHigh": 517
  },
  {
   "n": 7,
   "custom": "screenshot-split",
   "frameId": "gl",
   "visualSide": "right",
   "frameWide": 700,
   "badge": "screenshot",
   "kicker": "WHY GLOSSARY FIRST",
   "title": "Your intent outlives any database",
   "url": "brightway.eaternity.ch/browser · glossary",
   "image": "assets/ff-glossary.png",
   "frameHigh": 525,
   "annotations": [
    {
     "title": "Say what you mean",
     "sub": "stored as glossary terms — never as a key into one database version"
    },
    {
     "title": "Matched across every database",
     "sub": "the best inventory you have, found for you"
    },
    {
     "title": "Upgrades itself",
     "sub": "a better inventory arrives → the match is re-scored"
    }
   ],
   "footnote": "207,564 terms · 16 namespaces — ecoinvent, Sentier, CPC, NACE, GS1, AGROVOC, HESTIA, FoodEx2, FoodOn, LanguaL … food or not."
  },
  {
   "n": 8,
   "custom": "screenshot-split",
   "frameId": "ff5",
   "visualSide": "right",
   "frameWide": 760,
   "kicker": "PART 1 · FIREFLY · 5 / 6",
   "title": "See it. Compute it. Change it.",
   "url": "brightway.eaternity.ch/graph",
   "badge": "screenshot",
   "annotations": [
    {
     "title": "Graph-based view",
     "sub": "the supply chain drawn as it is; expand any node"
    },
    {
     "title": "Instant impact calculation",
     "sub": "the score updates with the activity you open"
    },
    {
     "title": "Full information — and editable",
     "sub": "sources, functional unit, method, every exchange"
    }
   ],
   "footnote": "",
   "image": "assets/ff-graph.png",
   "noChrome": true,
   "mockActive": "Graph",
   "mockText": "Graph · split · table",
   "frameHigh": 590
  },
  {
   "n": 9,
   "custom": "screenshot-split",
   "frameId": "ff6",
   "visualSide": "right",
   "frameWide": 760,
   "kicker": "PART 1 · FIREFLY · 6 / 6",
   "title": "Run a calculation",
   "url": "brightway.eaternity.ch/calculator",
   "badge": "screenshot",
   "annotations": [
    {
     "title": "Setup → functional units → methods → Run LCA"
    },
    {
     "title": "Results, charts, contribution, Sankey"
    },
    {
     "title": "Compare and Monte Carlo"
    }
   ],
   "footnote": "IPCC 2021 GWP100 (BAFU), the full EF 3.1 16-category suite, GLAM v2 and more.",
   "image": "assets/ff-calculator.png",
   "noChrome": true,
   "mockActive": "Calculator",
   "mockText": "Run LCA",
   "frameHigh": 580
  },
  {
   "n": 10,
   "custom": "wide-shot",
   "kicker": "PART 1 · FIREFLY · THE COMPOSER",
   "title": "The new Composer — a glossary-first editor",
   "body": "Write what you mean — the inventory assembles itself.",
   "iconSvg": "<svg viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M13 21h8\"/><path d=\"M21.174 6.812a1 1 0 0 0-3.986-3.987L3.842 16.174a2 2 0 0 0-.5.83l-1.321 4.352a.5.5 0 0 0 .623.622l4.353-1.32a2 2 0 0 0 .83-.497z\"/></svg>",
   "image": "assets/ff-composer.png",
   "annotations": [
    {
     "title": "Text, not forms",
     "sub": "one line per process and exchange — the graph and the exchanges are derived from it"
    },
    {
     "title": "Meaning, not keys",
     "sub": "every name resolves through the glossary to the best inventory, with place, year and attributes in the line"
    },
    {
     "title": "Reproducible by design",
     "sub": "the .lci file is the model: diff it, version it, share it — a better inventory re-scores the match"
    }
   ],
   "footnote": ""
  },
  {
   "n": 11,
   "kicker": "PART 2 · THE DATABASE",
   "dark": true,
   "title": "EDB — the Eaternity Database",
   "body": "A complete, fully transparent food inventory database. Every number can be opened, every model re-run.",
   "bigTitle": true,
   "bullets": [
    {
     "stat": "19,289",
     "label": "inventories, transparent down to every exchange, source and model — nothing aggregated away"
    },
    {
     "stat": "p5 · p95",
     "label": "an uncertainty band on every exchange; Monte Carlo where a model ran"
    },
    {
     "stat": "country × year",
     "label": "most inventories are computed by models that take the country and the year as parameters"
    },
    {
     "stat": "1,000",
     "label": "restaurants run on it today — in production at Eaternity"
    }
   ],
   "footnote": ""
  },
  {
   "n": 12,
   "custom": "integration-map",
   "kicker": "PART 2 · EDB → BAFU/UVEK",
   "title": "Mapping our database to BAFU/UVEK: a third was missing",
   "body": "The Swiss BAFU/UVEK database directly covers only about a third of the food background processes. The rest we built — hundreds of tributary inventories. Not a swap: an integration infrastructure.",
   "provenance": {
    "segments": [
     {
      "pct": 35,
      "label": {
       "de": "Echter Direkt-Treffer (BAFU/UVEK-Abgleich)",
       "en": "Genuine direct BAFU/UVEK match"
      },
      "color": "#1B7A3D"
     },
     {
      "pct": 41,
      "label": {
       "de": "Stellvertreter / hergeleitet",
       "en": "Proxy / inferred"
      },
      "color": "#E8A33D"
     },
     {
      "pct": 18,
      "label": {
       "de": "Eigens gebaute Tributär-Inventare",
       "en": "Purpose-built tributary inventories"
      },
      "color": "#2E6BB0"
     },
     {
      "pct": 6,
      "label": {
       "de": "Vernachlässigbar — bewusst weggelassen",
       "en": "Negligible — deliberately omitted"
      },
      "color": "#9AA0A6"
     }
    ]
   },
   "hub": {
    "label": "lci-workbench",
    "badge": {
     "de": "Vergleich & Validierung",
     "en": "comparison & validation"
    }
   },
   "inner": [
    "HESTIA",
    "Agribalyse v4",
    "SALCA",
    {
     "de": "Nationalstatistik",
     "en": "national stats"
    },
    {
     "de": "Satellit",
     "en": "satellite"
    },
    "DeDuCE"
   ],
   "outer": [],
   "footnote": {
    "de": "«Vernachlässigbar» = bewusst weggelassene Hintergrundbeiträge ohne nennenswerten Klima-Effekt (z. B. Maschinen-Herstellung) — keine fehlenden Inventare. Grundlage: EDB-Basismapping, 2'145 Hintergrundprozesse, Stand 17.06.2026.",
    "en": "«Negligible» = deliberately omitted background contributions with no meaningful climate effect (e.g. machinery manufacture) — not missing inventories. Source: EDB base mapping, 2,145 background processes, 2026-06-17."
   },
   "provHead": {
    "de": "Wie der BAFU-Wert der 2'145 EDB-Hintergrundprozesse zustande kam",
    "en": "How the BAFU value of the 2,145 EDB background processes was derived"
   },
   "sizesHead": {
    "de": "Datenbank-Grösse (Aktivitäten) — Referenz lizenziert, BAFU/UVEK öffentlich",
    "en": "Database size (activities) — reference licensed, BAFU/UVEK public"
   },
   "sizes": {
    "a": {
     "label": {
      "de": "Referenz-Datenbank",
      "en": "reference database"
     },
     "val": {
      "de": "18'121",
      "en": "18,121"
     }
    },
    "b": {
     "label": "BAFU/UVEK 2026",
     "val": {
      "de": "11'947 (−34 %)",
      "en": "11,947 (−34%)"
     },
     "pct": 66
    },
    "gapLabel": {
     "de": "Lücke",
     "en": "gap"
    }
   }
  },
  {
   "n": 13,
   "custom": "tributary-catalogue",
   "kicker": "PART 2 · FROM THE GROUND UP",
   "title": "Models, not lookups — per country, per year, test-driven",
   "body": "73 tributary modules from national statistics and 3,700+ publications — per country, per year, test-driven.",
   "kpis": [
    {
     "num": "73",
     "label": "tributary modules (63 populated)"
    },
    {
     "num": "29,463",
     "label": "LCI activities"
    },
    {
     "num": "1,351",
     "label": "automated tests"
    },
    {
     "num": "253",
     "label": "countries & regions"
    }
   ],
   "groups": [
    {
     "head": "Emission models",
     "items": [
      "RothC",
      "ICBM",
      "Indigo-N (N₂O)",
      "Rice CH₄",
      "Livestock",
      "IPCC Tier 1",
      "SALCA (15 models + Agrammon)"
     ]
    },
    {
     "head": "Crop & product",
     "items": [
      "Crops (7,324 cells)",
      "Fruit",
      "Coffee",
      "Dairy",
      "Meat",
      "Fermentation",
      "Food processing",
      "Greenhouse",
      "Aquaculture",
      "Algae",
      "Salt"
     ]
    },
    {
     "head": "Supply chain",
     "items": [
      "Packaging",
      "Transport",
      "Fertiliser",
      "Pesticide",
      "Waste treatment",
      "Market (10,235 mixes)",
      "Origin",
      "Food loss",
      "Electricity (214 countries)"
     ]
    },
    {
     "head": "Data layers",
     "items": [
      "Agri data (FAOSTAT)",
      "National stats (40 agencies)",
      "HESTIA",
      "GeoData",
      "Nutrients",
      "Labour time"
     ]
    },
    {
     "head": "Corrections",
     "items": [
      "Allocation",
      "Biodiversity",
      "LUC",
      "Phosphorus",
      "Water scarcity (AWARE 2.0)"
     ]
    }
   ],
   "footnote": "lci-workbench, 2026-09-04 · 19,289 inventories across 29 databases — Brightway, openLCA, SimaPro, ILCD."
  },
  {
   "n": 14,
   "custom": "live-board",
   "embed": true,
   "titleBand": true,
   "kicker": "PART 2 · THE DATABASE · EDB → BAFU/UVEK",
   "title": "How the database is composed",
   "embedUrl": "https://lci-workbench-0d71e7.gitlab.io/flow-map/index.html?embed=3",
   "image": "assets/wb-flow.png",
   "renderW": 1280,
   "renderH": 1124,
   "boardX": 109,
   "boardY": 82,
   "boardW": 1062,
   "boardH": 789,
   "scale": 0.78,
   "footnote": "lci-workbench-0d71e7.gitlab.io/#/tributaries · live"
  },
  {
   "n": 15,
   "custom": "screenshot-split",
   "frameId": "iqs",
   "visualSide": "right",
   "frameWide": 740,
   "badge": "screenshot",
   "kicker": "PART 2 · QUALITY THAT PREVENTS REGRESSIONS",
   "title": "One quality system, three questions",
   "url": "lci-workbench-0d71e7.gitlab.io/#/quality",
   "image": "assets/wb-quality.png",
   "imageFit": "contain-light",
   "annotations": [
    {
     "title": "Evidence, scored",
     "sub": "35 factors on every record"
    },
    {
     "title": "Regressions, caught",
     "sub": "a ledger per artifact, checked daily"
    },
    {
     "title": "Hand-offs, guarded",
     "sub": "~140 links between projects, drift-alarmed"
    }
   ],
   "footnote": "Re-derived from the data on every run — nothing is asserted by hand."
  },
  {
   "n": 16,
   "custom": "full-image",
   "image": "assets/ff-edb-project.png",
   "bg": "#0b0f0d"
  },
  {
   "n": 17,
   "custom": "tributary-selector",
   "kicker": "PART 2 · TWO OF 73",
   "title": "Two examples from the catalogue",
   "body": {
    "de": "Wie ein Tributary eine konkrete Lücke füllt — am Beispiel von Strom und von SALCA.",
    "en": "How a tributary fills a concrete gap — using electricity and SALCA as examples."
   },
   "footnote": "Every tile is a tributary — click any to swap the example.",
   "embed": true,
   "gutterLabel": {
    "de": "",
    "en": ""
   },
   "laneA": {
    "head": {
     "de": "Strom",
     "en": "Electricity"
    },
    "sub": {
     "de": "Netzmix nach Land & Saison",
     "en": "grid mix by country & season"
    },
    "items": [
     {
      "de": "Stromverbrauch in der Produktion",
      "en": "electricity used in production"
     },
     {
      "de": "füllt eine Energie-Lücke",
      "en": "fills an energy gap"
     }
    ]
   },
   "laneB": {
    "head": "SALCA",
    "sub": {
     "de": "Emissionen auf dem Hof",
     "en": "on-farm emissions"
    },
    "items": [
     {
      "de": "N₂O, CH₄, Boden-Kohlenstoff",
      "en": "N₂O, CH₄, soil carbon"
     },
     "Agroscope method"
    ]
   },
   "defaultIds": [
    "electricity-lca",
    "lci-salca"
   ],
   "bodyTemplate": {
    "de": "Wie ein Tributary eine konkrete Lücke füllt — am Beispiel von {A} und von {B}.",
    "en": "How a tributary fills a concrete gap — using {A} and {B} as examples."
   }
  },
  {
   "n": 18,
   "custom": "dyn-deepdive",
   "slot": 0,
   "which": "slide1"
  },
  {
   "n": 19,
   "custom": "dyn-deepdive",
   "slot": 1,
   "which": "slide1"
  },
  {
   "n": 20,
   "kicker": "WHAT IT POWERS · FLIT",
   "title": "100,000 products, live",
   "body": "On this base we publish 100,000 European supermarket products — each with an A–E rating, a CO₂e value and a confidence score. Browse it here.",
   "footnote": "flit.eaternity.org",
   "custom": "phone-split",
   "steps": [
    {
     "title": {
      "de": "Suchen",
      "en": "Search"
     },
     "desc": {
      "de": "Produkt per Name oder Barcode",
      "en": "Any product by name or barcode"
     }
    },
    {
     "title": {
      "de": "Bewertung sehen",
      "en": "See the score"
     },
     "desc": {
      "de": "A–E-Note und CO₂e-Wert",
      "en": "A–E rating and CO₂e value"
     }
    },
    {
     "title": {
      "de": "Konfidenz prüfen",
      "en": "Review confidence"
     },
     "desc": {
      "de": "Transparenz pro Produkt",
      "en": "Per-product transparency"
     }
    }
   ],
   "urlChip": {
    "de": "flit.eaternity.org · live",
    "en": "flit.eaternity.org · live"
   },
   "phone": {
    "name": {
     "de": "Joghurt griech. Art, 500 g",
     "en": "Greek-style yoghurt, 500 g"
    },
    "band": "b",
    "co2": 1.9,
    "co2unit": {
     "de": "kg CO₂e",
     "en": "kg CO₂e"
    },
    "confLabel": {
     "de": "Konfidenz",
     "en": "Confidence"
    },
    "conf": 82
   },
   "live": true,
   "embed": true,
   "phoneWidth": 300
  },
  {
   "n": 21,
   "custom": "reveal",
   "kicker": "ONE MORE THING",
   "words": [
    "Free.",
    "Open.",
    "Yours."
   ],
   "line": "All of it. Take it, build on it.",
   "rows": [
    {
     "chip": "Apache-2.0",
     "what": "73 tributaries + the calculation engine",
     "where": "gitlab.com/eos-lci"
    },
    {
     "chip": "CC-BY-4.0",
     "what": "19,289 inventories, the models, the results",
     "where": "no licence fee, no gatekeeper"
    },
    {
     "chip": "AGPL-3.0",
     "what": "Firefly — the interface, the assistant, the MCP",
     "where": "gitlab.com/eaternity/firefly"
    }
   ]
  },
  {
   "n": 22,
   "custom": "assistant",
   "kicker": "PART 3 · THE ASSISTANT",
   "title": "Ask your project anything",
   "logos": [
    {
     "src": "assets/claude_ai_logo.svg",
     "alt": "Claude",
     "h": 34
    },
    {
     "src": "assets/anthropic_logo.svg",
     "alt": "Anthropic",
     "h": 26
    }
   ],
   "image": "assets/ff-assistant.png",
   "points": [
    "Claude Opus 5.5 — isolated, no internet",
    "Brightway MCP · 22 tools",
    "Delegates the busy work",
    "Complex analysis on demand"
   ]
  },
  {
   "n": 23,
   "custom": "close",
   "bg": "#f0fdf4",
   "urlLabel": "brightway.eaternity.ch",
   "kicker": "NOW",
   "title": "Live demonstration",
   "body": "Everything you just saw is open: the interface, the database, the models, the assistant. Read it, audit it, reuse it.",
   "contacts": [
    "Firefly: brightway.eaternity.ch · gitlab.com/eaternity/firefly (AGPL-3.0)",
    "Database + 73 tributaries: gitlab.com/eos-lci (Apache-2.0 / CC-BY-4.0)",
    "Platform: lci-workbench-0d71e7.gitlab.io",
    "Flit: flit.eaternity.org"
   ],
   "phoneCaption": "Flit · 100,000 products · A–E · CO₂e · confidence",
   "embed": false,
   "live": false,
   "noPhone": true
  }
 ],
 "tributaries": [
  {
   "id": "lci-agri-data",
   "name": "Agricultural Primary Production Data",
   "category": "data_layer"
  },
  {
   "id": "lci-bafu-catalog",
   "name": "BAFU/UVEK Catalog",
   "category": "catalog"
  },
  {
   "id": "lci-market",
   "name": "Market Reconstruction",
   "category": "supply_chain"
  },
  {
   "id": "lci-origin",
   "name": "Origin/Provenance LCI",
   "category": "supply_chain"
  },
  {
   "id": "lci-waste-treatment",
   "name": "Waste Treatment LCI",
   "category": "supply_chain"
  },
  {
   "id": "electricity-lca",
   "name": "Electricity Grid Mixes",
   "category": "infrastructure"
  },
  {
   "id": "lci-food-loss",
   "name": "Food Loss LCI",
   "category": "supply_chain"
  },
  {
   "id": "lci-greet-integration",
   "name": "GREET Cross-Validation",
   "category": "other"
  },
  {
   "id": "lci-hestia",
   "name": "HESTIA Data Layer",
   "category": "data_layer"
  },
  {
   "id": "lci-national-stats",
   "name": "National Statistics Data Layer",
   "category": "data_layer"
  },
  {
   "id": "lci-location",
   "name": "Location Resolver",
   "category": "other"
  },
  {
   "id": "lci-salt",
   "name": "Salt Solar Evaporation LCI",
   "category": "crop_model"
  },
  {
   "id": "lci-dairy",
   "name": "Dairy LCI",
   "category": "crop_model"
  },
  {
   "id": "lci-coffee",
   "name": "Coffee Green Bean LCI",
   "category": "crop_model"
  },
  {
   "id": "lci-ecotransit",
   "name": "EcoTransit Routing",
   "category": "other"
  },
  {
   "id": "lci-fruit",
   "name": "Fruit & Crop LCI",
   "category": "crop_model"
  },
  {
   "id": "lci-livestock",
   "name": "Livestock Model",
   "category": "emission_model"
  },
  {
   "id": "lci-transport-decision",
   "name": "Transport Mode Decision",
   "category": "other"
  },
  {
   "id": "lci-cotton",
   "name": "Cotton Lint LCI",
   "category": "other"
  },
  {
   "id": "lci-spices-additives",
   "name": "Spices & Additives LCI",
   "category": "other"
  },
  {
   "id": "lci-cashew",
   "name": "Cashew Kernel LCI",
   "category": "other"
  },
  {
   "id": "lci-fertiliser",
   "name": "Fertiliser LCI",
   "category": "supply_chain"
  },
  {
   "id": "lci-mushroom",
   "name": "Mushroom Cultivation LCI",
   "category": "other"
  },
  {
   "id": "lci-oilpalm",
   "name": "Oil Palm FFB LCI",
   "category": "other"
  },
  {
   "id": "lci-pesticide",
   "name": "Pesticide LCI",
   "category": "supply_chain"
  },
  {
   "id": "lci-phosphorus",
   "name": "Phosphorus Erosion Model",
   "category": "correction"
  },
  {
   "id": "lci-packaging",
   "name": "Packaging LCI",
   "category": "supply_chain"
  },
  {
   "id": "lci-transport",
   "name": "Transport LCI",
   "category": "supply_chain"
  },
  {
   "id": "lci-metals",
   "name": "Metals & Alloys LCI",
   "category": "other"
  },
  {
   "id": "lci-textile-processing",
   "name": "Textile Processing LCI",
   "category": "other"
  },
  {
   "id": "lci-allocation",
   "name": "Allocation Model",
   "category": "correction"
  },
  {
   "id": "lci-biodiversity",
   "name": "Biodiversity Characterization Factors",
   "category": "correction"
  },
  {
   "id": "lci-ipcc-tier1-agriculture",
   "name": "IPCC Tier 1 Agricultural Emissions Model",
   "category": "emission_model"
  },
  {
   "id": "lci-luc",
   "name": "Land Use Change Model",
   "category": "correction"
  },
  {
   "id": "lci-crop-residue-burning",
   "name": "Crop Residue Burning",
   "category": "other"
  },
  {
   "id": "lci-storage",
   "name": "Storage LCI",
   "category": "infrastructure"
  },
  {
   "id": "lci-fuel-combustion",
   "name": "Fuel Combustion",
   "category": "other"
  },
  {
   "id": "lci-irrigation",
   "name": "Irrigation LCI",
   "category": "other"
  },
  {
   "id": "lci-fishing",
   "name": "Fishing LCI",
   "category": "infrastructure"
  },
  {
   "id": "lci-fishing-equipment",
   "name": "Fishing Equipment LCI",
   "category": "infrastructure"
  },
  {
   "id": "lci-greenhouse",
   "name": "Greenhouse LCI",
   "category": "crop_model"
  },
  {
   "id": "lci-water-scarcity",
   "name": "Water Scarcity LCI",
   "category": "correction"
  },
  {
   "id": "lci-algae",
   "name": "Algae LCI",
   "category": "crop_model"
  },
  {
   "id": "lci-fishing-gear",
   "name": "Fishing Gear LCI",
   "category": "infrastructure"
  },
  {
   "id": "lci-aquaculture",
   "name": "Aquaculture LCI",
   "category": "crop_model"
  },
  {
   "id": "lci-recipe",
   "name": "Recipe Archetype LCI",
   "category": "other"
  },
  {
   "id": "lci-seed",
   "name": "Seed LCI",
   "category": "other"
  },
  {
   "id": "lci-lentil",
   "name": "Lentil LCI",
   "category": "other"
  },
  {
   "id": "lci-food-processing",
   "name": "Food Processing LCI",
   "category": "crop_model"
  },
  {
   "id": "lci-ingredient-declaration",
   "name": "Ingredient Declaration Parser",
   "category": "other"
  },
  {
   "id": "lci-salca",
   "name": "SALCA LCI",
   "category": "integration"
  },
  {
   "id": "lci-dfu",
   "name": "Daily Food Unit (DFU)",
   "category": "other"
  },
  {
   "id": "lci-fermentation",
   "name": "Fermentation LCI",
   "category": "crop_model"
  },
  {
   "id": "lci-icbm",
   "name": "ICBM Soil Carbon",
   "category": "emission_model"
  },
  {
   "id": "lci-indigo-n",
   "name": "Indigo-N Nitrogen Model",
   "category": "emission_model"
  },
  {
   "id": "lci-ingredient-amounts",
   "name": "Ingredient Amount Estimation",
   "category": "other"
  },
  {
   "id": "lci-nutrients",
   "name": "Nutrient Profiles (multi-country)",
   "category": "other"
  },
  {
   "id": "lci-rice-ch4",
   "name": "Rice CH₄ Model",
   "category": "emission_model"
  },
  {
   "id": "lci-rothc",
   "name": "RothC Soil Carbon",
   "category": "emission_model"
  },
  {
   "id": "lci-agri-integration",
   "name": "Agricultural Model Integration",
   "category": "integration"
  },
  {
   "id": "lci-geodata",
   "name": "Geodata Service",
   "category": "infrastructure"
  },
  {
   "id": "lci-capital-goods",
   "name": "Capital Goods & Infrastructure LCI",
   "category": "other"
  },
  {
   "id": "lci-chemicals",
   "name": "Industrial Chemicals LCI",
   "category": "other"
  },
  {
   "id": "lci-construction-materials",
   "name": "Construction Materials LCI",
   "category": "other"
  },
  {
   "id": "lci-crops",
   "name": "Crops LCI",
   "category": "other"
  },
  {
   "id": "lci-electronics",
   "name": "Electronics & ICT LCI",
   "category": "other"
  },
  {
   "id": "lci-forestry-wood",
   "name": "Forestry & Wood Products LCI",
   "category": "other"
  },
  {
   "id": "lci-fuels",
   "name": "Fuels & Refining LCI",
   "category": "other"
  },
  {
   "id": "lci-labour-time",
   "name": "Labour Time (KAA — Kumulierter Arbeitsaufwand)",
   "category": "other"
  },
  {
   "id": "lci-meat",
   "name": "Meat LCI",
   "category": "other"
  },
  {
   "id": "lci-pulp-paper",
   "name": "Pulp, Paper & Board LCI",
   "category": "other"
  },
  {
   "id": "lci-score-cache",
   "name": "Confidential score-cache system processes",
   "category": "other"
  },
  {
   "id": "lci-water-supply",
   "name": "Water Supply LCI",
   "category": "other"
  }
 ],
 "selected": [
  "electricity-lca",
  "lci-salca"
 ],
 "tributaryContent": {
  "lci-agri-data": {
   "kicker": {
    "de": "Agrar-Primärstatistik",
    "en": "Agricultural primary statistics"
   },
   "slide1": {
    "title": {
     "de": "Rund 20 Statistik-Ämter, eine einzige Abfrage",
     "en": "About 20 statistics agencies, one single query"
    },
    "body": {
     "de": "Jedes Agrar-Emissionsmodell braucht dieselben Eingaben, doch jede Zahl liegt bei einem anderen Amt im eigenen Bulk-Format. Diese Schicht vereinheitlicht rund 20 nationale und EU-Ämter plus das FAOSTAT-Panel - rund 230'000 Einträge - gegen eine gemeinsame HESTIA-Identität und liefert sie über einen einzigen Lese-Aufruf, überall gleich geformt und bis zur Quellzeile rückführbar.",
     "en": "Every agricultural emission model needs the same inputs, yet each number lives at a different agency in its own bulk format. This layer harmonises about 20 national and EU agencies plus the FAOSTAT panel - roughly 230'000 entries - against one shared HESTIA identity and serves them through a single reader call, identically shaped everywhere and traceable to its source row."
    },
    "footnote": {
     "de": "Quellen u. a. FAOSTAT, USDA, IBGE SIDRA, Destatis, Eurostat, CBS, Agreste, BFS, Agroscope. 218 HESTIA-Begriffe über 10 Kategorien; Lese-API mit 29 Skalar- plus 6 angereicherten Helfern.",
     "en": "Sources include FAOSTAT, USDA, IBGE SIDRA, Destatis, Eurostat, CBS, Agreste, BFS, Agroscope. 218 HESTIA terms across 10 categories; reader API with 29 scalar plus 6 enriched helpers."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 20,
      "suffix": {
       "de": " Ämter",
       "en": " agencies"
      },
      "label": {
       "de": "nationale und EU-Statistik-Ämter plus FAOSTAT, in eine Schicht harmonisiert",
       "en": "national and EU statistics agencies plus FAOSTAT, harmonised into one layer"
      }
     },
     {
      "n": 230000,
      "suffix": {
       "de": " Einträge",
       "en": " entries"
      },
      "label": {
       "de": "quellenbelegte Datenpunkte, jeder bis zur exakten Ursprungszeile rückführbar",
       "en": "source-traced data points, each traceable to its exact upstream row"
      }
     },
     {
      "n": 1,
      "suffix": {
       "de": " Aufruf",
       "en": " call"
      },
      "label": {
       "de": "Lese-Aufruf liefert den besten Wert - HESTIA-Identität statt Amts-Codes",
       "en": "reader call returns the best value - HESTIA identity, not agency codes"
      }
     }
    ],
    "items": [
     {
      "de": "Ertrag, Düngermenge, Tierbestand, Düngerprofil, Pestizide, Landnutzung, Energie, Preise",
      "en": "Yield, fertiliser rate, livestock count, mix, pesticides, land use, energy, prices"
     },
     {
      "de": "HESTIA-Begriffe als Identität; Amts-Codes (FAOSTAT, USDA, SIDRA) nur als Aliasse",
      "en": "HESTIA terms as identity; agency codes (FAOSTAT, USDA, SIDRA) only as aliases"
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Immer der schärfste verfügbare Wert - sonst sauberer Rückfall",
     "en": "Always the sharpest available value - else a clean fallback"
    },
    "body": {
     "de": "Derselbe Aufruf geht eine feste Reihenfolge durch und nimmt den ersten Treffer: subnational vor national, national vor Welt-Rückfall. So bekommt jede Abfrage die feinste verfügbare Auflösung statt eines flachen Durchschnitts - und welcher Tier antwortete, steht offen am Eintrag. Weizen Frankreich: 7,89 t/ha in Seine-et-Marne, 6,76 t/ha national, 3,2 t/ha im Welt-Rückfall - alles reale Werte.",
     "en": "The same call walks a fixed order and takes the first hit: sub-national before national, national before world fallback. So every query gets the finest available resolution instead of a flat average - and which tier answered is stated openly on the entry. French wheat: 7.89 t/ha in Seine-et-Marne, 6.76 t/ha national, 3.2 t/ha in the world fallback - all real values."
    },
    "footnote": {
     "de": "Vorrang-Kette (erster Treffer gewinnt): 1. nationale Agentur (subnational + national), 2. Eurostat, 3. FAOSTAT, 4. kuratierte Literatur (Land, dann GLOBAL), 5. FAOSTAT-ESB (nur N-Rate), 6. Caller-Default. Spread von rund 4,7 t/ha = reale räumliche Heterogenität.",
     "en": "Precedence chain (first hit wins): 1. national agency (subnational + national), 2. Eurostat, 3. FAOSTAT, 4. curated literature (country, then GLOBAL), 5. FAOSTAT-ESB (N-rate only), 6. caller default. Spread of about 4.7 t/ha = real spatial heterogeneity."
    },
    "bars": [
     {
      "label": {
       "de": "Subnational - Seine-et-Marne (Agreste)",
       "en": "Subnational - Seine-et-Marne (Agreste)"
      },
      "value": 7.89,
      "disp": {
       "de": "7,89 t/ha",
       "en": "7.89 t/ha"
      },
      "color": "#2e7d32"
     },
     {
      "label": {
       "de": "National - Frankreich (FAOSTAT-Panel)",
       "en": "National - France (FAOSTAT panel)"
      },
      "value": 6.76,
      "disp": {
       "de": "6,76 t/ha",
       "en": "6.76 t/ha"
      },
      "color": "#66a05a"
     },
     {
      "label": {
       "de": "Welt-Rückfall - GLO (kuratierte Literatur)",
       "en": "World fallback - GLO (curated literature)"
      },
      "value": 3.2,
      "disp": {
       "de": "3,2 t/ha",
       "en": "3.2 t/ha"
      },
      "color": "#b0bec5"
     }
    ]
   }
  },
  "lci-bafu-catalog": {
   "kicker": {
    "de": "Hintergrund-Katalog",
    "en": "Background catalogue"
   },
   "slide1": {
    "title": {
     "de": "Der Hintergrund hinter jedem verarbeiteten Lebensmittel",
     "en": "The background behind every processed food"
    },
    "body": {
     "de": "Strom, Wärme, Transport und Basis-Chemikalien stecken in jedem verarbeiteten Produkt. Diese Schicht stellt den offenen Schweizer BAFU/UVEK-Hintergrund als eine JSON-Datei bereit — ein Datensatz je Aktivität mit voller Austauschliste und vorberechnetem GWP100, per Code abrufbar ohne LCA-Engine.",
     "en": "Electricity, heat, transport and base chemicals sit inside every processed product. This layer serves the open Swiss BAFU/UVEK background as one JSON file — one record per activity with full exchange list and pre-computed GWP100, resolvable by code without an LCA engine."
    },
    "footnote": {
     "de": "Quelle: lci-bafu-catalog, results/bafu_catalog.json; neun Sektor-Gruppen aus Produktions-Austausch-Metadaten. 417'714 Austausche, 35,6 je Aktivität.",
     "en": "Source: lci-bafu-catalog, results/bafu_catalog.json; nine sector groups from production-exchange category metadata. 417,714 exchanges, 35.6 per activity on average."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 11747,
      "label": {
       "de": "Hintergrund-Aktivitäten, je ein Datensatz",
       "en": "background activities, one record each"
      }
     },
     {
      "n": 9,
      "label": {
       "de": "Sektor-Gruppen: Strom, Wärme, Brennstoffe, Transport, Chemie, Baustoffe, Abfall, Wasser, Agrar/Lebensmittel",
       "en": "sector groups: electricity, heat, fuels, transport, chemicals, materials, waste, water, agri/food"
      }
     }
    ],
    "items": [
     {
      "de": "Strom/Netz 2'040 · Wärme/Brennstoffe 3'322 · Transport 2'046",
      "en": "Electricity/grid 2,040 · Heat/fuels 3,322 · Transport 2,046"
     },
     {
      "de": "Volle Austauschliste je Aktivität: Produktion, Technosphäre, Biosphäre",
      "en": "Full exchange list per activity: production, technosphere, biosphere"
     },
     {
      "de": "122 Standorte, 16 Einheiten — der ganze Hintergrund an einem Ort",
      "en": "122 locations, 16 units — the entire background in one place"
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Eine Extraktion, gepinnt — statt Brightway in jedem Konsumenten",
     "en": "One extraction, pinned — instead of Brightway in every consumer"
    },
    "body": {
     "de": "Eine Aktivität per Code aufzulösen verlangt nativ das Brightway-Projekt; Mapping-Tributaries tun das zehntausendfach je Build, Konsumenten ausserhalb von Python gar nicht. Dieser Tributary extrahiert einmal, mit stabilem Schema, auf eine Referenz-Version gepinnt — alle sehen dieselben Zahlen. GWP100 je Datensatz.",
     "en": "Resolving an activity by code natively needs the Brightway project; mapping tributaries do this tens of thousands of times per build, consumers outside Python not at all. This tributary extracts once, with a stable schema pinned to one reference release — all see the same numbers. GWP100 per record (100%)."
    },
    "footnote": {
     "de": "Quelle: lci-bafu-catalog, README/Methods; GWP100 unter BAFU-Charakterisierung, 11'747 von 11'747 Aktivitäten. Konsumenten: lci-food-processing, -fruit, -livestock, EDB-Stack.",
     "en": "Source: lci-bafu-catalog, README/Methods; GWP100 under BAFU characterisation, 11,747 of 11,747 activities. Consumers: lci-food-processing, -fruit, -livestock, EDB stack."
    },
    "stats": [
     {
      "num": {
       "de": "1",
       "en": "1"
      },
      "label": {
       "de": "JSON-Datei — eine geteilte Extraktion, ohne Brightway-Laufzeit",
       "en": "JSON file — one shared extraction, no Brightway runtime"
      }
     },
     {
      "num": {
       "de": "100 %",
       "en": "100%"
      },
      "label": {
       "de": "GWP100 vorberechnet je Datensatz, abrufbar per Code",
       "en": "GWP100 pre-computed per record, resolvable by code"
      }
     },
     {
      "num": {
       "de": "1 Pin",
       "en": "1 pin"
      },
      "label": {
       "de": "eine Referenz-Datenbank-Version — alle Konsumenten sehen dieselben Zahlen",
       "en": "one reference-database release — every consumer sees the same numbers"
      }
     }
    ]
   }
  },
  "lci-market": {
   "kicker": {
    "de": "Markt-Mix",
    "en": "Market mix"
   },
   "slide1": {
    "title": {
     "de": "Die ganze Lieferkette vom Erzeuger bis zum Konsum — als offene Schicht",
     "en": "The whole supply chain from producer to consumption — as an open layer"
    },
    "body": {
     "de": "Jeder Markt-Mix beantwortet: welche Länder liefern in welchem Anteil, mit wie viel Transport und welchen Nachernte-Verlusten. lci-market rekonstruiert 125 Märkte (Landwirtschaft 56, Handel 41, Mineralien 24, Energie 4; 78 Produkte) — jede Zelle prüfbar.",
     "en": "Every market mix answers: which countries supply in what share, with how much transport and post-harvest loss. lci-market reconstructs 125 markets (agriculture 56, trade 41, minerals 24, energy 4; 78 products) — every cell auditable."
    },
    "footnote": {
     "de": "Quelle: lci-market README. Je Markt: Lieferanten-Anteile (FAOSTAT, BACI, USGS, EIA), Transport (SeaRoute, OSRM), Verluste (FAO 2019). 256 Tests.",
     "en": "Source: lci-market README. Per market: supplier shares (FAOSTAT, BACI, USGS, EIA), transport (SeaRoute, OSRM), losses (FAO 2019). 256 tests."
    },
    "renderer": "stacked-bar",
    "segments": [
     {
      "value": 56,
      "disp": {
       "de": "56",
       "en": "56"
      },
      "label": {
       "de": "Landwirtschaft",
       "en": "Agriculture"
      },
      "color": "#16a34a"
     },
     {
      "value": 41,
      "disp": {
       "de": "41",
       "en": "41"
      },
      "label": {
       "de": "Bilateraler Handel",
       "en": "Bilateral trade"
      },
      "color": "#8BC34A"
     },
     {
      "value": 24,
      "disp": {
       "de": "24",
       "en": "24"
      },
      "label": {
       "de": "Mineralien",
       "en": "Minerals"
      },
      "color": "#FFC107"
     },
     {
      "value": 4,
      "disp": {
       "de": "4",
       "en": "4"
      },
      "label": {
       "de": "Energie",
       "en": "Energy"
      },
      "color": "#FF9800"
     }
    ],
    "total": {
     "disp": {
      "de": "125 Märkte",
      "en": "125 markets"
     },
     "label": {
      "de": "rekonstruierte Markt-Mixe, 78 Produkte",
      "en": "reconstructed market mixes, 78 products"
     },
     "max": 125
    },
    "callout": {
     "de": "Anteile + Transport + Verluste — jede Zelle auf eine öffentliche Datenzeile rückführbar",
     "en": "Shares + transport + losses — every cell traceable to a public data row"
    }
   },
   "slide2": {
    "title": {
     "de": "Offene Statistik statt eingefrorenem Katalog — neu baubar für jedes Jahr",
     "en": "Open statistics instead of a frozen catalogue — rebuildable for any year"
    },
    "body": {
     "de": "Etablierte Kataloge liefern den Konsum-Mix als Black Box: Anteile eingefroren aufs Referenzjahr, nicht einsehbar, nicht weitergebbar. lci-market baut jeden Mix aus offenen Primärstatistiken neu — für jedes Jahr (FAOSTAT ab 1961).",
     "en": "Established catalogues deliver the consumption mix as a black box: shares frozen at the reference year, not inspectable, not redistributable. lci-market rebuilds every mix from open primary statistics — for any year (FAOSTAT from 1961)."
    },
    "footnote": {
     "de": "Quelle: lci-market README; Jahres-Parametrisierung (FAOSTAT ab 1961, BACI ab 1995). Validiert gegen offene MRIO-Anteile (Peng et al. 2024).",
     "en": "Source: lci-market README; year parameterisation (FAOSTAT from 1961, BACI from 1995). Validated against open MRIO shares (Peng et al. 2024)."
    },
    "bullets": [
     {
      "de": "Einsehbar: jede Lieferanten-, Transport- und Verlustzeile zeigt ihre öffentliche Quelle.",
      "en": "Inspectable: every supplier, transport and loss row shows its public source."
     },
     {
      "de": "Zeitlich neu baubar: Referenzjahr und Fenster sind Build-Parameter.",
      "en": "Rebuildable in time: reference year and window are build parameters."
     },
     {
      "de": "Datenbank-unabhängig: derselbe Mix speist jede Ziel-Datenbank.",
      "en": "Database-agnostic: the same mix feeds any destination database."
     },
     {
      "de": "Weitergebbar: nur offen lizenzierte Primärstatistik (FAOSTAT, BACI, USGS, EIA).",
      "en": "Redistributable: only openly licensed primary statistics."
     }
    ]
   }
  },
  "lci-origin": {
   "kicker": {
    "de": "Herkunfts-Mix aus offenen Handelsdaten",
    "en": "Origin mix from open trade data"
   },
   "slide1": {
    "title": {
     "de": "Welches Land liefert wirklich – die fehlende Schicht",
     "en": "Which country actually supplies it – the missing layer"
    },
    "body": {
     "de": "Keine offene Referenz-Datenbank kodiert den Herkunfts-Mix pro Ware und Land: Produktions-Inventare gibt es pro Land, doch die Bezugs-Gewichte je Erzeugerland fehlen. Diese Tributary rekonstruiert sie aus der bilateralen FAOSTAT-Handelsmatrix über «Inland + Importe − Exporte» und ersetzt zwei fehlerhafte Abkürzungen.",
     "en": "No open reference database encodes the origin mix per commodity and country: per-country production inventories exist, but the sourcing weights per producer are missing. This tributary rebuilds them from the bilateral FAOSTAT trade matrix via «domestic + imports − exports», replacing two flawed shortcuts."
    },
    "footnote": {
     "de": "Quelle: FAOSTAT bilaterale Handelsmatrix + Produktionsstatistik; jede Zelle aus der öffentlichen FAOSTAT-Veröffentlichung nachschlagbar.",
     "en": "Source: FAOSTAT bilateral trade matrix + production statistics; every cell lookup-able from the public FAOSTAT release."
    },
    "bars": [
     {
      "label": {
       "de": "Reine Inland-Annahme: gleicher Vektor für jede Ware",
       "en": "Domestic-only assumption: same vector for every commodity"
      },
      "value": 1,
      "disp": {
       "de": "falsch",
       "en": "wrong"
      },
      "color": "#9ca3af"
     },
     {
      "label": {
       "de": "Global gemittelter Importanteil: Partner-Signal gelöscht",
       "en": "Globally-averaged import share: partner signal erased"
      },
      "value": 1,
      "disp": {
       "de": "falsch",
       "en": "wrong"
      },
      "color": "#9ca3af"
     },
     {
      "label": {
       "de": "FAOSTAT-Handelsfluss-Rekonstruktion: Partner-Signal erhalten",
       "en": "FAOSTAT trade-flow reconstruction: partner signal preserved"
      },
      "value": 3,
      "disp": {
       "de": "diese Tributary",
       "en": "this tributary"
      },
      "color": "#16a34a"
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Anteils-Vektor plus Graph-Umbau-Plan",
     "en": "Share vector plus graph-restructuring plan"
    },
    "body": {
     "de": "Ein Entscheidungsbaum mit 6 Aktionen wählt pro Anfrage explizite Herkunft, FAOSTAT-Aufteilung oder «unbekannt». Bei der Aufteilung entsteht der Anteils-Vektor – z. B. Äpfel, CH 2020: 35 % Inland, Rest auf Italien, Frankreich, Spanien. Dazu ein Umbau-Plan in den Graphen, linear in der Zahl der Herkünfte (N−1 Duplikate + 1 Kante).",
     "en": "A 6-action decision tree picks per query between explicit origin, FAOSTAT split or «unknown». On the split the share vector emerges – e.g. apples, CH 2020: 35 % domestic, rest to Italy, France, Spain. Plus a restructuring plan into the calculation graph, linear in the number of origins (N−1 duplications + 1 edge)."
    },
    "footnote": {
     "de": "Anteils-Vektor summiert auf höchstens 1; Top-90-%-Kappung lässt den unzuverlässigen langen Schwanz weg. Mutationen: 1 Land = 7, 2 = 10, 3 = 13. 43 Tests bestehen lokal.",
     "en": "Share vector sums to at most 1; the top-90 % truncation drops the unreliable long tail. Mutations: 1 country = 7, 2 = 10, 3 = 13. 43 tests pass locally."
    },
    "renderer": "stacked-bar",
    "segments": [
     {
      "value": 0.35,
      "disp": {
       "de": "35 %",
       "en": "35 %"
      },
      "label": {
       "de": "Schweiz (Inland)",
       "en": "Switzerland (domestic)"
      },
      "color": "#16a34a"
     },
     {
      "value": 0.299,
      "disp": {
       "de": "29,9 %",
       "en": "29.9 %"
      },
      "label": {
       "de": "Italien",
       "en": "Italy"
      },
      "color": "#8BC34A"
     },
     {
      "value": 0.2015,
      "disp": {
       "de": "20,2 %",
       "en": "20.2 %"
      },
      "label": {
       "de": "Frankreich",
       "en": "France"
      },
      "color": "#FFC107"
     },
     {
      "value": 0.0975,
      "disp": {
       "de": "9,8 %",
       "en": "9.8 %"
      },
      "label": {
       "de": "Spanien",
       "en": "Spain"
      },
      "color": "#FF9800"
     }
    ],
    "total": {
     "disp": {
      "de": "94,8 %",
      "en": "94.8 %"
     },
     "label": {
      "de": "benannter Anteils-Vektor (Rest ist der gekappte Schwanz)",
      "en": "named share vector (remainder is the truncated tail)"
     },
     "max": 1
    },
    "callout": {
     "de": "Ein Vektor pro (Küchenland, Ware) – plus der Plan, der ihn in den Graphen trägt.",
     "en": "One vector per (kitchen country, commodity) – plus the plan that carries it into the graph."
    }
   }
  },
  "lci-waste-treatment": {
   "kicker": {
    "de": "DER BEHANDLUNGS-ZWEIG",
    "en": "THE TREATMENT LEG"
   },
   "slide1": {
    "title": {
     "de": "Der geprüfte Behandlungs-Zweig jeder Ökobilanz",
     "en": "The audited treatment leg of every footprint"
    },
    "body": {
     "de": "Jedes Lebensmittel trägt eine Abfall- oder Abwasser-Last. Diese Schicht ist der Behandlungs-Zweig: für alle 90 Hintergrund-Aktivitäten eine dokumentierte Pro-Pfad-Entscheidung — BAFU/UVEK behalten, wenn der Wert in einer publizierten Literatur-Klammer liegt (83 «keep»), oder korrigieren, wo die Funktion falsch ist (4 «adjust», 3 verworfen).",
     "en": "Every food product carries a waste or wastewater burden. This layer is the treatment leg: a documented per-pathway decision across all 90 background activities — keep the BAFU/UVEK match when its value sits in a published literature bracket (83 «keep»), or correct it where the function is wrong (4 «adjust», 3 dropped)."
    },
    "footnote": {
     "de": "90 Haupt-Aktivitäten (plus 73 erweitert = 163). Klammern aus Corominas 2013/2020, Moller 2009, Boldrin 2009, Serafini 2025. 72 Tests.",
     "en": "90 main activities (plus 73 extended = 163). Brackets from Corominas 2013/2020, Moller 2009, Boldrin 2009, Serafini 2025. 72 tests."
    },
    "renderer": "stacked-bar",
    "segments": [
     {
      "value": 83,
      "disp": {
       "de": "83",
       "en": "83"
      },
      "label": {
       "de": "behalten – Wert in publizierter Klammer",
       "en": "kept – value inside published bracket"
      },
      "color": "#2f7d57"
     },
     {
      "value": 4,
      "disp": {
       "de": "4",
       "en": "4"
      },
      "label": {
       "de": "korrigiert – falsche Funktion",
       "en": "corrected – wrong function"
      },
      "color": "#c8761f"
     },
     {
      "value": 3,
      "disp": {
       "de": "3",
       "en": "3"
      },
      "label": {
       "de": "verworfen – kein Äquivalent",
       "en": "dropped – no equivalent"
      },
      "color": "#9aa0a6"
     }
    ],
    "total": {
     "disp": {
      "de": "90",
      "en": "90"
     },
     "label": {
      "de": "Behandlungs-Aktivitäten, je geprüft",
      "en": "treatment activities, each checked"
     },
     "max": 90
    },
    "callout": {
     "de": "543 Verweise in 432 Lebensmitteln hängen an dieser Schicht. Eine von sieben Aktivitäten zeigte auf die falsche Funktion – etwa CH-Bioabfall, der statt auf Vergärung auf reine Sammel-Logistik verwies, oder Industrieabwässer ohne BAFU-Äquivalent.",
     "en": "543 references across 432 food products depend on this layer. One in seven activities pointed at the wrong function – e.g. CH biowaste resolving to collection logistics instead of digestion, or industrial effluents with no BAFU equivalent."
    }
   },
   "slide2": {
    "title": {
     "de": "Vorzeichen korrigiert, Herkunft aufgelöst",
     "en": "Sign corrected, origin resolved"
    },
    "body": {
     "de": "Zwei Achsen tragen den Wert. Methode: die Referenz-Datenbank gibt der Behandlung per Cutoff eine Gutschrift (negativ), der BAFU/UVEK-Hintergrund alloziert ökonomisch (positiv) – keine publizierte Behandlungs-Ökobilanz meldet negativ. Region: eine entkoppelte Mix-Schicht (Eurostat, 28 Länder plus Schweiz) routet durch den realen Landes-Mix statt einen Standardwert.",
     "en": "Two axes carry the value. Method: the reference database credits treatment via cutoff (negative), the BAFU/UVEK background allocates economically (positive) – no published treatment LCA reports negative. Region: a decoupled mix layer (Eurostat, 28 countries plus Switzerland) routes through the real country mix instead of a default."
    },
    "footnote": {
     "de": "Bioabfall je kg: Cutoff-Gutschrift bis −0,95 (Serafini 2025: −0,95 bis +0,55); ökonomische Allokation positiv (Abwasser-Klasse 5: +0,414, Corominas 2013). Last: CH-Mix ≈ 0,025, Deponie ≈ 0,30. Mixe aus Eurostat env_wastrt/env_ww_con, 2014–2022.",
     "en": "Biowaste per kg: cutoff credit to −0.95 (Serafini 2025: −0.95 to +0.55); economic allocation positive (wastewater class 5: +0.414, Corominas 2013). Burden: CH mix ≈ 0.025, landfill ≈ 0.30. Mixes from Eurostat env_wastrt/env_ww_con, 2014–2022."
    },
    "bars": [
     {
      "label": {
       "de": "Referenz-Datenbank, Cutoff-Netto-Gutschrift",
       "en": "Reference database, cutoff net credit"
      },
      "value": -0.95,
      "disp": {
       "de": "−0,95",
       "en": "−0.95"
      },
      "color": "#9aa0a6"
     },
     {
      "label": {
       "de": "BAFU/UVEK, ökonomische Allokation",
       "en": "BAFU/UVEK, economic allocation"
      },
      "value": 0.414,
      "disp": {
       "de": "+0,414",
       "en": "+0.414"
      },
      "color": "#2f7d57"
     },
     {
      "label": {
       "de": "Schweizer biologischer Bioabfall-Mix",
       "en": "Swiss biological biowaste mix"
      },
      "value": 0.025,
      "disp": {
       "de": "0,025",
       "en": "0.025"
      },
      "color": "#4a9c6d"
     },
     {
      "label": {
       "de": "Deponie-lastiger Mix (anderes Land)",
       "en": "Landfill-heavy mix (other country)"
      },
      "value": 0.3,
      "disp": {
       "de": "0,30",
       "en": "0.30"
      },
      "color": "#c8761f"
     }
    ]
   }
  },
  "electricity-lca": {
   "kicker": {
    "de": "STROM-MODELL",
    "en": "ELECTRICITY MODEL"
   },
   "slide1": {
    "title": {
     "de": "Es gibt keinen «europäischen Strom»",
     "en": "There is no «European electricity»"
    },
    "body": {
     "de": "Welches Netz ein Produkt nutzt, entscheidet seinen Strom-Fussabdruck — quer durch Europa um rund eine Grössenordnung. Das Tributary ersetzt einen flachen Durchschnitt durch den gemessenen Mix des jeweiligen Landes, statt eines Einheitswerts.",
     "en": "Which grid a product runs on decides its electricity footprint — roughly an order of magnitude across Europe. This tributary replaces one flat average with each country's measured mix, not a single value."
    },
    "footnote": {
     "de": "lci-electricity · kg CO₂e pro kWh, heimischer Mix 2023, Niederspannung · gegen IEA, electricityMap, IRENA und ENTSO-E abgeglichen.",
     "en": "lci-electricity · kg CO₂e per kWh, domestic-only 2023 mix, low voltage · cross-checked against IEA, electricityMap, IRENA and ENTSO-E."
    },
    "bars": [
     {
      "label": {
       "de": "Schweden",
       "en": "Sweden"
      },
      "value": 0.032,
      "disp": {
       "de": "0,032",
       "en": "0.032"
      },
      "color": "#7fb069"
     },
     {
      "label": {
       "de": "Frankreich",
       "en": "France"
      },
      "value": 0.039,
      "disp": {
       "de": "0,039",
       "en": "0.039"
      },
      "color": "#7fb069"
     },
     {
      "label": {
       "de": "Österreich",
       "en": "Austria"
      },
      "value": 0.052,
      "disp": {
       "de": "0,052",
       "en": "0.052"
      },
      "color": "#7fb069"
     },
     {
      "label": {
       "de": "Deutschland",
       "en": "Germany"
      },
      "value": 0.291,
      "disp": {
       "de": "0,291",
       "en": "0.291"
      },
      "color": "#9a9a9a"
     },
     {
      "label": {
       "de": "Italien",
       "en": "Italy"
      },
      "value": 0.413,
      "disp": {
       "de": "0,413",
       "en": "0.413"
      },
      "color": "#9a9a9a"
     },
     {
      "label": {
       "de": "Polen",
       "en": "Poland"
      },
      "value": 0.69,
      "disp": {
       "de": "0,690",
       "en": "0.690"
      },
      "color": "#d62828"
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Wo und wann der Strom bezogen wurde",
     "en": "Where and when the power was drawn"
    },
    "body": {
     "de": "Der gleiche Strom-Hintergrund, austauschbar pro Land, Jahr, Saison und wahlweise mit rekursiv aufgelösten Importen: 1'400 Aktivitäten. So springt derselbe Schweizer Mix 2023 von 8 g heimisch produziert auf 66 g, sobald die Importe aus den Nachbarnetzen mitzählen — derselbe Strom, andere Herkunftsbilanz.",
     "en": "The same electricity background, swappable per country, year, season and optionally with recursively resolved imports: 1'400 activities. The same Swiss 2023 mix jumps from 8 g produced domestically to 66 g once imports from the neighbour grids count — same power, different origin accounting."
    },
    "footnote": {
     "de": "lci-electricity · Schweiz 2023 · heimisch vs. mit Importen, Niederspannung · g CO₂e/kWh; gegen IEA und electricityMap abgeglichen.",
     "en": "lci-electricity · Switzerland 2023 · domestic vs with-imports, low voltage · g CO₂e/kWh; cross-checked against IEA and electricityMap."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 1400,
      "label": {
       "de": "austauschbare Strommixe (28 Länder × 5 Jahre × 10 Varianten)",
       "en": "swappable grid mixes (28 countries × 5 years × 10 variants)"
      }
     },
     {
      "n": 8,
      "suffix": {
       "de": "→66 g",
       "en": "→66 g"
      },
      "label": {
       "de": "Schweizer Mix 2023 CO₂e/kWh: heimisch vs. ab Stecker (mit Importen)",
       "en": "Swiss 2023 mix CO₂e/kWh: domestic vs at the plug (with imports)"
      }
     },
     {
      "n": 28,
      "label": {
       "de": "europäische Länder, je mit gemessenem Mix — kein Durchschnitt",
       "en": "European countries, each with its measured mix — no average"
      }
     }
    ],
    "items": [
     {
      "de": "Annual und saisonal, heimisch und mit rekursiv aufgelösten Importen — vier Hintergründe pro Land und Jahr.",
      "en": "Annual and seasonal, domestic and with recursively resolved imports — four backgrounds per country and year."
     },
     {
      "de": "Gemessene Technologie-Anteile je Periode, fleet-korrigiert — kein statischer Durchschnitt.",
      "en": "Measured per-period technology shares, fleet-corrected — no static average."
     }
    ]
   }
  },
  "lci-food-loss": {
   "kicker": {
    "de": "Verlust-und-Abfall-Korrektur",
    "en": "Loss-and-waste correction"
   },
   "slide1": {
    "title": {
     "de": "Datenbanken kennen die Produktion, nicht den Teller",
     "en": "Catalogues know production, not the plate"
    },
    "body": {
     "de": "Datenbanken liefern Inventare ab Hof, nicht ab Teller. Pro verzehrtem Kilo muss über fünf Stufen mehr produziert werden: 1,14× bei Milch, bis 2,09× bei Wurzeln & Knollen.",
     "en": "Catalogues publish inventories at the farm gate, not the plate. Per consumed kilo, more must be produced across five stages: 1.14× for dairy, up to 2.09× for roots & tubers."
    },
    "footnote": {
     "de": "Vorlauf-Multiplikator 1/(1 − kumulierter Verlust) je Warengruppe, Europa-Aggregat (Gustavsson 2011).",
     "en": "Upstream multiplier 1/(1 − cumulative loss) per commodity group, Europe aggregate (Gustavsson 2011)."
    },
    "bars": [
     {
      "label": {
       "de": "Milchprodukte",
       "en": "Dairy"
      },
      "value": 1.14,
      "disp": {
       "de": "1,14× (12,2% Verlust)",
       "en": "1.14× (12.2% loss)"
      },
      "color": "#2f7d32"
     },
     {
      "label": {
       "de": "Ölsaaten & Hülsenfrüchte",
       "en": "Oilseeds & pulses"
      },
      "value": 1.24,
      "disp": {
       "de": "1,24× (19,6%)",
       "en": "1.24× (19.6%)"
      },
      "color": "#4f9a52"
     },
     {
      "label": {
       "de": "Fleisch",
       "en": "Meat"
      },
      "value": 1.29,
      "disp": {
       "de": "1,29× (22,2%)",
       "en": "1.29× (22.2%)"
      },
      "color": "#74b377"
     },
     {
      "label": {
       "de": "Getreide",
       "en": "Cereals"
      },
      "value": 1.45,
      "disp": {
       "de": "1,45× (31,2%)",
       "en": "1.45× (31.2%)"
      },
      "color": "#9ab14f"
     },
     {
      "label": {
       "de": "Fisch & Meeresfrüchte",
       "en": "Fish & seafood"
      },
      "value": 1.46,
      "disp": {
       "de": "1,46× (31,4%)",
       "en": "1.46× (31.4%)"
      },
      "color": "#c2a23a"
     },
     {
      "label": {
       "de": "Früchte & Gemüse",
       "en": "Fruit & vegetables"
      },
      "value": 1.84,
      "disp": {
       "de": "1,84× (45,7%)",
       "en": "1.84× (45.7%)"
      },
      "color": "#c46b2e"
     },
     {
      "label": {
       "de": "Wurzeln & Knollen",
       "en": "Roots & tubers"
      },
      "value": 2.09,
      "disp": {
       "de": "2,09× (52,2%)",
       "en": "2.09× (52.2%)"
      },
      "color": "#a23e1e"
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Verlust als Graph-Umschreibung, nicht als Multiplikator",
     "en": "Loss as a graph rewrite, not a multiplier"
    },
    "body": {
     "de": "Statt die Nachfrage vorzumultiplizieren, schreibt diese Schicht den Rechengraphen um: Kante lösen, Wrapper, Food-Loss-Aktivität, Original-Kante anhängen. Vorlauf und weggeworfene Masse bleiben getrennt sichtbar.",
     "en": "Instead of pre-multiplying demand, this layer rewrites the calculation graph: detach edge, insert wrapper, add food-loss activity, re-attach. Upstream and discarded mass stay separately visible."
    },
    "footnote": {
     "de": "Vier-Schritt-Umschreibung über eine Skalar-Verlustrate; exakte Massenerhaltung. 30 Paritäts-Testvektoren sichern die Berechnung byte-genau.",
     "en": "Four-step rewrite via one scalar loss rate; exact mass conservation. 30 parity test vectors pin the computation byte-for-byte."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 4,
      "label": {
       "de": "Schritte je Umschreibung — lösen, Wrapper, Aktivität, anhängen",
       "en": "steps per rewrite — detach, wrapper, activity, re-attach"
      }
     },
     {
      "n": 2,
      "label": {
       "de": "sichtbare Effekte: Vorlauf-Mehrbedarf + verworfene Masse",
       "en": "visible effects: upstream over-production + discarded mass"
      }
     },
     {
      "n": 30,
      "label": {
       "de": "Paritäts-Testvektoren sichern die Berechnung byte-genau",
       "en": "parity test vectors pin the computation byte-for-byte"
      }
     }
    ],
    "items": [
     {
      "de": "Verlustrate je Knoten aus Kundendaten; Rückfall für 8 Warengruppen",
      "en": "Loss rate per node from client data; fallback for 8 groups"
     },
     {
      "de": "Verworfene Masse läuft an echten Abfall-Eintrag, regional austauschbar",
      "en": "Discarded mass routes to real waste entry, swappable per region"
     },
     {
      "de": "Dieselbe Umschreibung je Ware und Stufe; besitzt nur den Verlust-Keil",
      "en": "Same rewrite per commodity and stage; owns only the loss wedge"
     }
    ]
   }
  },
  "lci-greet-integration": {
   "kicker": {
    "de": "Eine unabhängige Referenz-Klammer für die eigenen Emissionsmodelle",
    "en": "An independent reference bracket for our own emission models"
   },
   "slide1": {
    "title": {
     "de": "Eine unabhängige Klammer, wo es sonst keine gibt",
     "en": "An independent bracket where none otherwise exists"
    },
    "body": {
     "de": "GREET (Argonne) ist ein US-Biotreibstoff-Instrument, keine Lebensmittel-Datenbank - nie eine direkte Inventar-Quelle. Doch seine Agrar-Scheibe deckt genau den Raum, wo unsere N2O- und Bodenkohlenstoff-Modelle am schwächsten sind, und wickelt die DayCent- und CCLUB-Referenz samt Unsicherheitsbändern als Klammer ein.",
     "en": "GREET (Argonne) is a US biofuels tool, not a food database - never a direct inventory source. Yet its agricultural slice covers exactly the space where our N2O and soil-carbon models are weakest, wrapping the DayCent and CCLUB reference with its uncertainty bands as a machine-readable bracket."
    },
    "footnote": {
     "de": "Eingewickelt: 6 N2O-Pflanzen (DayCent) + 4 Bodenkohlenstoff-Szenarien (CCLUB); abgeklammert: Bouwman, IPCC 2019, Shcherbak, RothC, ICBM. Quelle: cross_validation.json.",
     "en": "Wrapped: 6 N2O crops (DayCent) + 4 soil-carbon scenarios (CCLUB); bracketed: Bouwman, IPCC 2019, Shcherbak, RothC, ICBM. Source: README.md, cross_validation.json."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 6,
      "suffix": {
       "de": " Kulturen",
       "en": " crops"
      },
      "label": {
       "de": "N2O-Referenzzellen (DayCent), pro Kultur abgeklammert",
       "en": "N2O reference cells (DayCent), bracketed per crop"
      }
     },
     {
      "n": 4,
      "suffix": {
       "de": " Szenarien",
       "en": " scenarios"
      },
      "label": {
       "de": "Bodenkohlenstoff-Referenzzellen (CCLUB)",
       "en": "soil-carbon reference cells (CCLUB)"
      }
     },
     {
      "n": 5,
      "suffix": {
       "de": " Modelle",
       "en": " models"
      },
      "label": {
       "de": "eigene Workbench-Modelle gegen die unabhängige Referenz gehalten",
       "en": "own workbench models held against the independent reference"
      }
     }
    ],
    "items": [
     {
      "de": "Referenz aus DayCent- und CCLUB-Langläufen - sonst nirgends",
      "en": "Reference distilled from long DayCent and CCLUB runs - nowhere else"
     },
     {
      "de": "Jede Zelle: Zentralwert, Unsicherheitsband, Eingaben - nachvollziehbar",
      "en": "Each cell: central value, uncertainty band, inputs - re-derivable"
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Modellwahl mit externer Evidenz statt aus dem Bauch",
     "en": "Model choice with external evidence, not by gut feeling"
    },
    "body": {
     "de": "Der eigentliche Wert: Die Schwester-Tributaries (lci-indigo-n, lci-rothc, lci-icbm) wählen Standardmodell und Szenario-Gewichte aus einer unabhängigen Referenz statt aus dem Bauch. Über die sechs Kulturen trifft IPCC 2019 die Referenz im Mittel (1,02), Bouwman überschätzt vierfach (4,08) - Modellwahl wird messbar.",
     "en": "The real value: the sibling tributaries (lci-indigo-n, lci-rothc, lci-icbm) pick their default model and scenario weights from an independent reference, not by gut. Across the six crops IPCC 2019 hits the reference on average (1.02), Bouwman over-predicts fourfold (4.08) - making model choice measurable."
    },
    "footnote": {
     "de": "Achse = Mittel-Verhältnis zur GREET-Referenz, Ziel 1,0; zweite Klammer aus 6 Meta-Analysen (Cayuela 2017, 1'100+ Beob.) bestätigt die Wahl. Quelle: cross_validation.json.",
     "en": "Axis = mean ratio to the GREET reference, target 1.0; a second bracket of 6 meta-analyses (Cayuela 2017, 1,100+ obs.) confirms it. Source: cross_validation.json."
    },
    "bars": [
     {
      "label": {
       "de": "IPCC 2019 - trifft die Referenz (4/6 Kulturen im Band)",
       "en": "IPCC 2019 - hits the reference (4/6 crops in band)"
      },
      "value": 1.02,
      "disp": {
       "de": "1,02x",
       "en": "1.02x"
      },
      "color": "#16a34a"
     },
     {
      "label": {
       "de": "Shcherbak - leicht tief (1/6 im Band)",
       "en": "Shcherbak - slightly low (1/6 in band)"
      },
      "value": 0.86,
      "disp": {
       "de": "0,86x",
       "en": "0.86x"
      },
      "color": "#8BC34A"
     },
     {
      "label": {
       "de": "Bouwman - überschätzt vierfach (0/6 im Band)",
       "en": "Bouwman - over-predicts fourfold (0/6 in band)"
      },
      "value": 4.08,
      "disp": {
       "de": "4,08x",
       "en": "4.08x"
      },
      "color": "#dc2626"
     }
    ]
   }
  },
  "lci-hestia": {
   "kicker": {
    "de": "Offene Hof-Referenz für die ganze Werkbank",
    "en": "The open farm-gate reference for the whole workbench"
   },
   "slide1": {
    "title": {
     "de": "Ein offener Vergleichsmassstab, abfragbar für jedes Produkt",
     "en": "One open benchmark, queryable for every product"
    },
    "body": {
     "de": "Bisher gab es nur Einzel-Studien (nicht produktübergreifend vergleichbar) oder eine geschlossene Datenbank. Diese Schicht veröffentlicht den Poore-Nemecek-Massstab (2018) wortgetreu als JSON-Katalog: 42 Kategorien, je 5 Wirkungsachsen, acht Lieferketten-Stufen – offene Referenz auf gemeinsamer Funktionseinheit.",
     "en": "Until now there were only single studies (not comparable across products) or a closed database. This layer republishes the peer-reviewed Poore-Nemecek benchmark (2018) verbatim as a JSON catalogue: 42 categories, 5 impact axes each, eight supply-chain stages – an open reference on a common functional unit."
    },
    "footnote": {
     "de": "Quelle: Poore und Nemecek 2018 (Science), 1'434 Hof-Beobachtungen aus 119 Ländern. Daten CC-BY-NC-4.0, Code Apache-2.0.",
     "en": "Source: Poore and Nemecek 2018 (Science), 1'434 farm observations from 119 countries. Data CC-BY-NC-4.0, code Apache-2.0."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 42,
      "label": {
       "de": "Produkt-Kategorien, zwölf Produktgruppen",
       "en": "product categories, twelve product groups"
      }
     },
     {
      "n": 5,
      "label": {
       "de": "Wirkungsachsen je Eintrag, plus 8-Stufen-Lieferkette",
       "en": "impact axes per entry, plus 8-stage supply chain"
      }
     },
     {
      "n": 249,
      "suffix": {
       "de": "-fach",
       "en": "x"
      },
      "label": {
       "de": "Spanne je kg, von der Nuss (0,4) zum Rind (99,5)",
       "en": "range per kg, from nuts (0.4) to beef (99.5)"
      }
     }
    ],
    "items": [
     {
      "de": "Wortgetreu importiert; Stufensumme je Eintrag pro Release geprüft",
      "en": "Imported verbatim; per-entry stage-sum checked on every release"
     },
     {
      "de": "Gemeinsame Funktionseinheit (kg, L, Schlachtgewicht) mit FAO-Kennung",
      "en": "Common functional unit per entry (kg, L, carcass weight …) with FAO id"
     },
     {
      "de": "Acht nachgelagerte Tributaries lesen daraus, statt je neu einzulesen",
      "en": "Eight downstream tributaries read from it instead of re-ingesting it"
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Eine versionsfeste Quelle statt drei driftender Kopien",
     "en": "One version-pinned source instead of three drifting copies"
    },
    "body": {
     "de": "Die Schicht bündelt vier Hestia-Tabellen (Rückstands-Verbleib, Verbrennungsanteil, Pflanzenbiologie, Ökoklimazonen), die drei Emissions-Tributaries zuvor je privat und driftend einlasen. Eine typisierte Schnittstelle liefert nun dieselben Werte – Rückstandsanteile ergeben exakt 1,0, MD5-Manifest fixiert den Commit.",
     "en": "The layer also consolidates four Hestia glossary tables (residue retention, fraction burned, crop biology, ecoclimate zones) that three emission tributaries each ingested privately and drifting. One typed reader API now returns the same values – residue shares sum to exactly 1.0, an MD5 manifest pins the commit."
    },
    "footnote": {
     "de": "Konsumenten: lci-indigo-n, lci-rothc, lci-crop-residue-burning (zuvor je eigene Kopie). Manifest: data/HESTIA_VERSION.json.",
     "en": "Consumers: lci-indigo-n, lci-rothc, lci-crop-residue-burning (each a private copy before). Manifest: data/HESTIA_VERSION.json."
    },
    "stats": [
     {
      "num": {
       "de": "3 → 1",
       "en": "3 → 1"
      },
      "label": {
       "de": "private, driftende Kopien der Glossartabellen zu einer geteilten Quelle zusammengeführt",
       "en": "private, drifting copies of the glossary tables merged into one shared source"
      }
     },
     {
      "num": {
       "de": "37",
       "en": "37"
      },
      "label": {
       "de": "Glossartabellen mit MD5-Prüfsumme je Datei synchronisiert und gegen den Upstream-Commit fixiert",
       "en": "glossary tables synced with a per-file MD5 checksum, pinned to the upstream commit"
      }
     },
     {
      "num": {
       "de": "= 1,0",
       "en": "= 1.0"
      },
      "label": {
       "de": "Rückstandsanteile (eingearbeitet, entfernt, verbrannt) summieren per Konstruktion exakt",
       "en": "residue shares (incorporated, removed, burned) sum exactly by construction"
      }
     }
    ]
   }
  },
  "lci-national-stats": {
   "kicker": {
    "de": "Nationale Statistikämter als Datenschicht",
    "en": "National statistics agencies as a data layer"
   },
   "slide1": {
    "title": {
     "de": "Ein Welt-Durchschnitt — oder die echte Zahl des Amtes",
     "en": "One world average — or the agency's real number"
    },
    "body": {
     "de": "Statistikämter veröffentlichen riesige Mengen amtlicher, oft regionaler Agrardaten — doch hinter rund 40 Portalen mit je eigenen Einheiten und Codes. Diese Schicht zieht alle Ämter einmal in EINE Hülle, am Glossar verankert, mit Amts-Kennung und zitierter Herkunft pro Zeile, abrufbar über EINE Leser-Schnittstelle.",
     "en": "Statistics agencies publish vast amounts of official, often subnational farm data — but across some 40 portals each with its own units and codes. This layer pulls every agency once into ONE envelope keyed to the glossary, with agency identifier and cited provenance per row, reachable through ONE reader API."
    },
    "footnote": {
     "de": "Quelle: README (~3 Mio. Zeilen in 386 Hüllen-Dateien, Schema v3.0.0; 40 Ämter über 13 Quell-Domänen). FADN = EU-Buchhaltungsnetz der Höfe.",
     "en": "Source: README (~3M rows in 386 envelope files, schema v3.0.0; 40 agencies over 13 source domains). FADN = EU Farm Accountancy Data Network."
    },
    "stats": [
     {
      "num": {
       "de": "40",
       "en": "40"
      },
      "label": {
       "de": "Statistikämter, einmal in eine Hülle vereinheitlicht",
       "en": "statistics agencies, unified into one envelope"
      }
     },
     {
      "num": {
       "de": "~3 Mio.",
       "en": "~3M"
      },
      "label": {
       "de": "Datenzeilen über 13 Quell-Domänen",
       "en": "data rows across 13 source domains"
      }
     },
     {
      "num": {
       "de": "1",
       "en": "1"
      },
      "label": {
       "de": "Leser-Schnittstelle statt 40 Portal-Protokollen",
       "en": "reader API instead of 40 portal protocols"
      }
     },
     {
      "num": {
       "de": "jede Zeile",
       "en": "every row"
      },
      "label": {
       "de": "trägt Amts-Kennung + zitierte Herkunft mit Zeitstempel",
       "en": "carries agency identifier + cited, timestamped provenance"
      }
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Zuerst das Amt, erst dann der Durchschnitt",
     "en": "The agency first, the average only as fallback"
    },
    "body": {
     "de": "Diese Schicht ist die oberste, «gesourcete» Stufe der Datenkette: Eine Anfrage nach einem Eingangswert — Düngerrate, Ertrag, Tierbestand — für Land, Region und Jahr trifft zuerst hier auf den echten Amts-Wert. Nur wenn KEIN Amt etwas hat, fällt die Kette auf den Welt-Durchschnitt zurück.",
     "en": "This layer is the top, «sourced» tier of the data chain: a query for an input value — fertiliser rate, yield, livestock count — for a country, region and year hits the real agency value here first. Only when NO agency has it does the chain fall through to the world average."
    },
    "footnote": {
     "de": "Stufen (lci-agri-data): 1 = amtlich gesourcet (diese Schicht), 2–5 = FAOSTAT national, Literatur, Allokation, Standard. BFS = Bundesamt für Statistik.",
     "en": "Tiers (lci-agri-data): 1 = agency-sourced (this layer), 2–5 = FAOSTAT national, literature, allocation, default. BFS = Swiss Federal Statistical Office."
    },
    "renderer": "wet-dry-bars",
    "wet": {
     "value": 1,
     "disp": {
      "de": "Stufe 1",
      "en": "Tier 1"
     },
     "label": {
      "de": "Diese Schicht: echter Amts-Wert, regional + pro Jahr, mit Quelle",
      "en": "This layer: real agency value, subnational + per-year, with source"
     }
    },
    "dry": {
     "value": 5,
     "disp": {
      "de": "erst Stufe 2–5",
      "en": "only tiers 2–5"
     },
     "label": {
      "de": "Fallback: FAOSTAT-Welt-Durchschnitt der Referenz-Datenbank",
      "en": "Fallback: FAOSTAT world average from the reference database"
     }
    },
    "barMax": 5,
    "ratio": {
     "de": "zuerst geprüft",
     "en": "checked first"
    },
    "callout": {
     "de": "Die Kette gibt den ersten nicht-leeren Treffer zurück — und mit ihm die Stufe, die ihn lieferte.",
     "en": "The chain returns the first non-empty hit — and with it the tier that supplied it."
    }
   }
  },
  "lci-location": {
   "kicker": {
    "de": "Geografie-Auflöser",
    "en": "Geography resolver"
   },
   "slide1": {
    "title": {
     "de": "Jede Ortsangabe zu prüfbarer Geografie",
     "en": "Every place name to verifiable geography"
    },
    "body": {
     "de": "Freitext-Orte («AT,DE,FR», «Beauce», «Lower Saxony») sind für ein Modell nutzlos. Diese Schicht löst jede Angabe zu kanonischen Codes auf den Standard-Taxonomien GADM, ISO 3166 und UN M49 auf — die gemeinsame Geografie-Identität, an die alle orts-spezifischen Modelle binden.",
     "en": "Free-text places («AT,DE,FR», «Beauce», «Lower Saxony») are useless to a model. This layer resolves each one to canonical codes on the GADM, ISO 3166 and UN M49 standard taxonomies — the shared geographic identity every location-specific model binds to."
    },
    "footnote": {
     "de": "countries.py und resolver.py; 249 ISO-Alpha-2- und 249 Alpha-3-Codes, 244 UN-M49-Nummern; Laufzeit-Auflöser ohne Mapping-Ausgabe; Apache-2.0.",
     "en": "countries.py and resolver.py; 249 ISO alpha-2 and 249 alpha-3 codes, 244 UN M49 numbers; runtime resolver with no mapping output; Apache-2.0."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 6,
      "label": {
       "de": "unterschiedliche Eingabeklassen, jede mit eigener Regel - in einer festen Kette aus 9 Schritten",
       "en": "disjoint input classes, each with its own rule - in one fixed chain of 9 steps"
      }
     },
     {
      "n": 3,
      "label": {
       "de": "offene, zitierbare Taxonomien als Anker: ISO 3166, UN M49, GADM v4.1",
       "en": "open, citable taxonomies as anchor: ISO 3166, UN M49, GADM v4.1"
      }
     }
    ],
    "items": [
     {
      "de": "Land: 249 ISO-Alpha-2-/249 Alpha-3-Codes, 244 UN-M49-Nummern",
      "en": "country: 249 ISO alpha-2 / 249 alpha-3 codes, 244 UN M49 numbers"
     },
     {
      "de": "Sub-national: GADM-v4.1-Kennung über den injizierten Polygon-Auflöser",
      "en": "sub-national: GADM v4.1 identifier via the injected polygon resolver"
     },
     {
      "de": "Region: 5 Kennungen über 12 deutsche/englische Aliasse («europe»)",
      "en": "regional: 5 identifiers via 12 German/English aliases («europe»)"
     },
     {
      "de": "Jedes Ergebnis trägt prüfbare Provenienz: welcher Schritt es erzeugte",
      "en": "every result carries auditable provenance: which step produced it"
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Eine Kette für alle - statt in jeder Tributary neu und uneinheitlich",
     "en": "One chain for all - instead of re-built and divergent in every tributary"
    },
    "body": {
     "de": "Vorher trug jede Tributary eigene ISO-, Kontinent-, Mehrländer- und Koordinaten-Logik - gleiche Eingabe, je nach Konsument andere Kennung. lci-location ist eine Kette: lci-geodata, lci-ecotransit und lci-origin rufen sie unverändert auf, «europe» landet überall bei R0355. Injizierte Dienste einen Test und Produktion.",
     "en": "Before, each tributary carried its own ISO, continental, multi-country and coordinate logic - identical input, a different identifier per consumer. lci-location is one chain: lci-geodata, lci-ecotransit and lci-origin call it unchanged, «europe» lands at R0355 everywhere. Injected services unify test and production."
    },
    "footnote": {
     "de": "resolver.py, countries.py; «europe» → R0355 (Europa, 45 Länder); 55 Paritäts-Tests grün über 9 Schritte; Konsumenten: lci-geodata, lci-ecotransit, lci-origin; Apache-2.0.",
     "en": "resolver.py, countries.py; «europe» → R0355 (Europe, 45 countries); 55 parity tests green across 9 steps; consumers: lci-geodata, lci-ecotransit, lci-origin; Apache-2.0."
    },
    "stats": [
     {
      "num": {
       "de": "3",
       "en": "3"
      },
      "label": {
       "de": "Tributaries rufen dieselbe Kette unverändert auf - gleiche Eingabe, gleiche Kennung",
       "en": "tributaries call the same chain unchanged - same input, same identifier"
      }
     },
     {
      "num": {
       "de": "55",
       "en": "55"
      },
      "label": {
       "de": "Paritäts-Tests grün; bracketen die Bibliothek gegen die Produktion über alle 9 Schritte",
       "en": "parity tests green; bracket the library against production across all 9 steps"
      }
     }
    ]
   }
  },
  "lci-salt": {
   "kicker": {
    "de": "Salz-Produktion",
    "en": "Salt production"
   },
   "slide1": {
    "title": {
     "de": "Drei Salz-Routen, die der Referenz-Katalog gar nicht kennt",
     "en": "Three salt routes the reference catalogue simply does not carry"
    },
    "body": {
     "de": "Der offene BAFU/UVEK-Hintergrund kennt nur Industrie-Salz; Solar-Meersalz, Nigari und Auftausalz fehlen. Dieses Tributary baut alle drei als literaturbasierte Gate-to-Gate-Inventare neu auf — sie liegen rund drei Grössenordnungen auseinander.",
     "en": "The open BAFU/UVEK background carries only industrial salt; solar sea-salt, nigari and de-icing salt are absent. This tributary rebuilds all three as literature-based gate-to-gate inventories — spanning roughly three orders of magnitude."
    },
    "footnote": {
     "de": "Funktionseinheit 1 kg, Gate-to-Gate. Quellen: Akridge 2008, EuSalt 2021. 6 Mapping-Einträge, 37 Tests.",
     "en": "Functional unit 1 kg, gate-to-gate. Sources: Akridge 2008, EuSalt 2021. 6 mapping entries, 37 tests."
    },
    "bars": [
     {
      "label": {
       "de": "Solar-Meersalz",
       "en": "Solar sea-salt"
      },
      "value": 0.000476,
      "disp": {
       "de": "0,000476",
       "en": "0.000476"
      },
      "color": "#2e7d32"
     },
     {
      "label": {
       "de": "Auftausalz (Vakuum)",
       "en": "De-icing salt (vacuum)"
      },
      "value": 0.119,
      "disp": {
       "de": "0,119",
       "en": "0.119"
      },
      "color": "#1565c0"
     },
     {
      "label": {
       "de": "Nigari (Bittern-Koppelprodukt)",
       "en": "Nigari (bittern co-product)"
      },
      "value": 0.169,
      "disp": {
       "de": "0,169",
       "en": "0.169"
      },
      "color": "#6a1b9a"
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Warum es zählt: ein austauschbarer, rückführbarer Inventar-Layer statt Proxy-Raten",
     "en": "Why it matters: a swappable, traceable inventory layer instead of proxy guesses"
    },
    "body": {
     "de": "Ohne diese Inventare greift der Auto-Matcher zum nächsten Industrie-Proxy und überschätzt jede Route um das 3- bis 155-Fache. Drei offene Inventare ersetzen das; ihre Flüsse sind per Code an BAFU-Aktivitäten gebunden — Netz-Mix, Region oder Katalog tauschbar, ohne Werte neu herzuleiten.",
     "en": "Without these inventories the auto-matcher grabs the nearest industrial proxy and overstates each route by 3 to 155x. Three open inventories replace that; their flows bind by code to BAFU activities — grid mix, region or catalogue swappable without re-deriving values."
    },
    "footnote": {
     "de": "Validierung: Solar innert 15 %, Nigari innert 21 % der Open-Reference; Auftausalz im EuSalt-2021-Bereich 0,05-0,155.",
     "en": "Validation: solar within 15%, nigari within 21% of open reference; de-icing salt within EuSalt-2021 range 0.05-0.155."
    },
    "bullets": [
     {
      "de": "Drei unterschiedliche Routen statt einer Industrie-Pauschale",
      "en": "Three distinct routes, not one industrial blanket value"
     },
     {
      "de": "Jeder Wert auf Primärquellen rückführbar, keine Blackbox",
      "en": "Every value traceable to primary sources, no black box"
     },
     {
      "de": "Flüsse per Code an BAFU gebunden: Mix, Region tauschbar",
      "en": "Flows bound by code to BAFU: mix, region swappable"
     },
     {
      "de": "Ersetzt drei falsche Proxys (3-155x zu hoch)",
      "en": "Replaces three wrong proxies (3-155x too high)"
     }
    ]
   }
  },
  "lci-dairy": {
   "kicker": {
    "de": "MOLKEREI-MODELL",
    "en": "DAIRY MODEL"
   },
   "slide1": {
    "title": {
     "de": "Die fehlende Schicht zwischen Hof und Regal",
     "en": "The missing layer between farm and shelf"
    },
    "body": {
     "de": "Die Verarbeitung im Molkereibetrieb fehlt in der öffentlichen Referenz-Datenbank als eigener Eintrag — dort stehen nur Rohstoffe und Grundversorgung. Diese Tributary baut die Schicht: rund 100 Komposit-Inventare am Molkerei-Tor, aus 16 Literaturquellen aufgebaut. Jede Zelle ist eine Produktions-Exchange plus 8–12 benannte Hintergrundaktivitäten plus eine Rohmilch-Aufnahme — fixiert über eine dokumentierte Massen- und Fettbilanz.",
     "en": "Dairy-plant processing has no entry of its own in the public reference database — it carries only raw materials and bulk utilities. This tributary builds that layer: about 100 composite inventories at the dairy gate, assembled from 16 literature sources. Each cell is one production exchange plus 8–12 named background activities plus a raw-milk input — fixed by a documented mass and fat balance."
    },
    "footnote": {
     "de": "Katalog: 190 Mapping-Einträge, 100 Komposit-Aktivitäten, 16 Quellen, 91 Tests. Funktionale Einheit: 1 kg Molkereiprodukt am Molkerei-Tor. Geltungsbereich CH/RER plus regionale Fallbacks.",
     "en": "Catalogue: 190 mapping entries, 100 composite activities, 16 sources, 91 tests. Functional unit: 1 kg dairy product at the dairy gate. Scope CH/RER plus regional fallbacks."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 100,
      "suffix": {
       "de": "",
       "en": ""
      },
      "label": {
       "de": "Komposit-Inventare am Molkerei-Tor, neu aufgebaut",
       "en": "composite inventories at the dairy gate, rebuilt"
      }
     },
     {
      "n": 12,
      "suffix": {
       "de": " Exchanges",
       "en": " exchanges"
      },
      "label": {
       "de": "pro Zelle: 1 Produktion + 8–12 benannte Hintergrund-Inputs",
       "en": "per cell: 1 production + 8–12 named background inputs"
      }
     },
     {
      "n": 16,
      "suffix": {
       "de": " Quellen",
       "en": " sources"
      },
      "label": {
       "de": "peer-review-Literatur statt proprietärer Klumpen",
       "en": "peer-reviewed literature, not a proprietary lump"
      }
     }
    ],
    "items": [
     {
      "de": "Milchpulver, Rahm (15–45% Fett), Hart-/Weichkäse, Frischkäse, Joghurt, Sauermilch, Glace, Butterreinfett, Molke — je konventionell und Bio",
      "en": "Milk powders, cream (15–45% fat), hard/soft cheese, fresh cheese, yoghurt, soured milk, ice cream, clarified butter, whey — each conventional and organic"
     },
     {
      "de": "Physische Flüsse binden nur über den Namen an die Hintergrund-Aktivität, gelöst erst zur Rechenzeit",
      "en": "Physical flows bind to a background activity by name only, resolved at computation time"
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Jedes Kilo rückführbar — und der Hintergrund frei tauschbar",
     "en": "Every kilogram traceable — and the background freely swappable"
    },
    "body": {
     "de": "Der Vorgänger erbte die Molkerei-Prozesse aus einer proprietären Schweizer Akademie-Datenbank: nur rund vier Fünftel der Vorketten-Kinder lösten auf BAFU auf — das fehlende Fünftel liess Emissionen still wegfallen, und kein Prüfer konnte einen Tor-Wert auf eine Bilanz zurückführen. Hier trägt jeder Input eine Quellenangabe. Weil die Hintergrund-Aktivitäten nur über den Namen binden, lässt sich das Stromnetz regional umlegen oder die Hof-Milch austauschen — ohne eine Zelle neu zu rechnen.",
     "en": "The predecessor inherited dairy processing from a proprietary Swiss-academic database: only about four-fifths of the upstream children resolved to BAFU — the missing fifth silently dropped emissions, and no reviewer could trace a gate value back to a balance. Here every input carries a citation. Because background activities bind by name only, the grid can be re-pointed to a region or the farm milk swapped out — without recomputing a cell."
    },
    "footnote": {
     "de": "Validierungsbeleg: Schweizer Vollmilchpulver 13,39 kg CO₂eq/kg, innerhalb vier unabhängiger Literatur-Bänder; Bio-Variante 15,75. Massen- und Fettbilanz schliesst auf ±3–5%, im Test-Suite verankert.",
     "en": "Validation evidence: Swiss whole milk powder 13.39 kg CO₂eq/kg, inside four independent literature bands; organic variant 15.75. Mass and fat balance closes to ±3–5%, gated by the test suite."
    },
    "stats": [
     {
      "num": {
       "de": "~4/5",
       "en": "~4/5"
      },
      "label": {
       "de": "der Vorketten-Kinder lösten im alten proprietären Modell auf — ein Fünftel der Emissionen fiel still weg; hier: 100% benannt und rückführbar",
       "en": "of upstream children resolved in the old proprietary model — a fifth of emissions silently dropped; here: 100% named and traceable"
      }
     },
     {
      "num": {
       "de": "0",
       "en": "0"
      },
      "label": {
       "de": "Zellen neu zu rechnen, um Netz, Region oder Hof-Milch zu tauschen — die Bindung erfolgt nur über den Namen",
       "en": "cells to recompute when swapping grid, region or farm milk — binding is by name only"
      }
     },
     {
      "num": {
       "de": "±3–5%",
       "en": "±3–5%"
      },
      "label": {
       "de": "Schliessung der Massen- und Fettbilanz pro Produktkategorie, im Test-Suite verankert",
       "en": "mass-and-fat-balance closure per product category, gated by the test suite"
      }
     }
    ]
   }
  },
  "lci-coffee": {
   "kicker": {
    "de": "Kaffee-Grünbohne, nach Herkunft aufgelöst",
    "en": "Coffee green bean, resolved by origin"
   },
   "slide1": {
    "title": {
     "de": "Eine globale Sammelzeile wird zu 15 abfragbaren Herkunfts-Zellen",
     "en": "One global aggregate row becomes 15 queryable origin cells"
    },
    "body": {
     "de": "Kaffee-Grünbohne ist volumenstark, hat im öffentlichen BAFU/UVEK-Hintergrund aber keine Wiege-bis-Hoftor-Aktivität; andere Kataloge führen sie als eine globale Zeile. Diese Schicht baut je Land, Sorte und Aufbereitung eine eigene Zelle — 10 Produktionszellen plus 5 produktionsgewichtete Markt-Rekonstruktionen.",
     "en": "Coffee green bean is high-volume, yet has no cradle-to-farm-gate activity in the public BAFU/UVEK background; other catalogues list it as a single global row. This layer builds one cell per country, variety and processing — 10 production cells plus 5 production-weighted market reconstructions."
    },
    "footnote": {
     "de": "15 Einträge: 10 Produktionszellen (5 Arabica, 5 Robusta) über 7 Herkünfte (BR, CO, HN, IN, ID, VN, RoW) und 4 Aufbereitungen, plus 5 Markt-Rekonstruktionen. Funktionelle Einheit 1 kg Grünbohne, Referenzjahr 2020.",
     "en": "15 entries: 10 production cells (5 arabica, 5 robusta) across 7 origins (BR, CO, HN, IN, ID, VN, RoW) and 4 processing methods, plus 5 market reconstructions. Functional unit 1 kg green bean, reference year 2020."
    },
    "renderer": "stacked-bar",
    "segments": [
     {
      "value": 5,
      "disp": {
       "de": "5",
       "en": "5"
      },
      "label": {
       "de": "Arabica-Zellen",
       "en": "arabica cells"
      },
      "color": "#6f4e37"
     },
     {
      "value": 5,
      "disp": {
       "de": "5",
       "en": "5"
      },
      "label": {
       "de": "Robusta-Zellen",
       "en": "robusta cells"
      },
      "color": "#a9746e"
     },
     {
      "value": 5,
      "disp": {
       "de": "5",
       "en": "5"
      },
      "label": {
       "de": "Markt-Rekonstruktionen",
       "en": "market reconstructions"
      },
      "color": "#c9b79c"
     }
    ],
    "total": {
     "disp": {
      "de": "15",
      "en": "15"
     },
     "label": {
      "de": "Einträge statt einer globalen Zeile",
      "en": "entries instead of one global row"
     },
     "max": 15
    },
    "callout": {
     "de": "Jede Zelle gemeinsam auf Land, Sorte und Aufbereitung verschlüsselt — statt eine globale Sammelzeile, die die reale Herkunfts-Spreizung verbirgt.",
     "en": "Each cell keyed jointly on country, variety and processing — instead of one global aggregate row that hides the real per-origin spread."
    }
   },
   "slide2": {
    "title": {
     "de": "Ein vollständiges Inventar je Zelle — nicht ein fester Emissionsfaktor",
     "en": "A full inventory per cell — not one fixed emission factor"
    },
    "body": {
     "de": "Jede Zelle ist ein vollständiges Wiege-bis-Hoftor-Inventar: Dünger, Kalk, Pestizide, Diesel, Bewässerung und Aufbereitung binden als Technosphären-Flüsse an benannte BAFU/UVEK-Aktivitäten — Strom- oder Brennstoffmix bleibt tauschbar. Direkte Feldemissionen via IPCC 2019 Tier 1 auf BAFU-Biosphären-Schlüssel; per-Herkunft-Erträge (0,7 bis 3,73 t/ha) treiben die Spreizung.",
     "en": "Each cell is a full cradle-to-farm-gate inventory: fertiliser, lime, pesticides, diesel, irrigation and processing bind as technosphere flows to named BAFU/UVEK activities — grid or fuel mix stays swappable. Direct field emissions via IPCC 2019 Tier 1 to BAFU biosphere keys; per-origin yields (0.7 to 3.73 t/ha) drive the spread."
    },
    "footnote": {
     "de": "Erträge aus data/coffee_inputs.json (Indonesien Robusta 0,7 bis Vietnam Robusta 3,73 t/ha). Direkte Feldemissionen (N2O, NH3, NO3, CO2 aus Kalk, PO4, Pestizid) via IPCC 2019 Tier 1; Spreizung 3- bis 8-fach (Arabica), 2- bis 6-fach (Robusta). Land-Nutzungs-Änderung aus lci-luc.",
     "en": "Yields from data/coffee_inputs.json (Indonesia robusta 0.7 to Vietnam robusta 3.73 t/ha). Direct field emissions (N2O, NH3, NO3, CO2 from lime, PO4, pesticide) via IPCC 2019 Tier 1; spread three-to-eight-fold (arabica), two-to-six-fold (robusta). Land-use change from lci-luc."
    },
    "renderer": "stats",
    "stats": [
     {
      "num": {
       "de": "8×",
       "en": "8×"
      },
      "label": {
       "de": "Wiege-bis-Hoftor-Spreizung über die Herkünfte (3- bis 8-fach Arabica, 2- bis 6-fach Robusta), die eine globale Sammelzeile verbirgt",
       "en": "cradle-to-farm-gate spread across origins (3-8x arabica, 2-6x robusta) that a single global row hides"
      }
     },
     {
      "num": {
       "de": "3,73t/ha",
       "en": "3.73t/ha"
      },
      "label": {
       "de": "höchster per-Herkunft-Ertrag (Vietnam Robusta) der Ertrags-Bandbreite 0,7 bis 3,73 t/ha, die die Input-Verteilung pro kg treibt",
       "en": "highest per-origin yield (Vietnam robusta) of the 0.7 to 3.73 t/ha range that drives the per-kg input allocation"
      }
     }
    ]
   }
  },
  "lci-ecotransit": {
   "kicker": {
    "de": "Transport-Routing für die Sachbilanz",
    "en": "Transport routing for the inventory"
   },
   "slide1": {
    "title": {
     "de": "Pro Tonnenkilometer bepreist — doch niemand kennt die Distanz",
     "en": "Priced per tonne-kilometre — yet nobody holds the distance"
    },
    "body": {
     "de": "Offene Datenbanken liefern Frachtfaktoren pro Tonnenkilometer, kennen aber nie die echte Quelle-zu-Ziel-Distanz. Diese Schicht schliesst die Lücke: Aus zwei Koordinaten entsteht eine Aufschlüsselung pro Glied — Distanz und Quelle-bis-Rad-Intensität für Vor-, Haupt- und Nachlauf.",
     "en": "Open databases supply freight factors per tonne-kilometre but never the real origin-to-destination distance. This layer closes the gap: from two coordinates it builds a per-leg breakdown — distance and well-to-wheel intensity for pre-carriage, mainhaul and post-carriage."
    },
    "footnote": {
     "de": "Hauptlauf nach Clean-Cargo-Working-Group-Tradelane (GLEC-Framework), Standardjahr 2024; Distanzen pro Glied in km.",
     "en": "Mainhaul per Clean Cargo Working Group tradelane (GLEC Framework), default year 2024; per-leg distances in km."
    },
    "bullets": [
     {
      "de": "Die Lücke: kein offener Katalog trägt die Quelle-zu-Ziel-Distanz",
      "en": "The gap: no open catalogue carries origin-to-destination distance"
     },
     {
      "de": "Zwei Koordinaten hinein, drei Glieder mit eigener Distanz heraus",
      "en": "Two coordinates in, three legs each with own distance out"
     },
     {
      "de": "Hauptlauf via zitierbare Tradelane; Meilen via Geometrie-Schätzer",
      "en": "Mainhaul via citable tradelane; miles via geometry estimator"
     },
     {
      "de": "«Wie weit, welcher Modus-Split» — global und auditierbar",
      "en": "«How far, which mode split» — global and auditable"
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Multimodal, global, und bewusst nicht eingebacken",
     "en": "Multimodal, global, and deliberately not baked in"
    },
    "body": {
     "de": "Drei Modi werden geroutet (See, Luft, Boden; Schiene reserviert), der Geometrie-Schätzer deckt sechs Admin-Ebenen ab, und bei unbekannter Herkunft greift eine See-Pauschale von 14'664 km Tür-zu-Tür. Der tkm-Faktor wird erst nachgelagert gebunden — dieselbe Route übersteht jeden Datenbank- oder Brennstoff-Wechsel.",
     "en": "Three modes route today (sea, air, ground; rail reserved), the geometry estimator spans six admin levels, and for unknown origin a sea default of 14'664 km door-to-door applies. The tkm factor is bound only downstream — the same route survives any database or fuel change."
    },
    "footnote": {
     "de": "Konstanten gegen die Referenz gepinnt (10 Fälle, Ribbon-Faktor 1,417); Cache-Modus läuft ohne Zugangsdaten.",
     "en": "Constants pinned against the reference (10 cases, ribbon factor 1.417); cache mode runs without credentials."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 3,
      "suffix": {
       "de": " Modi",
       "en": " modes"
      },
      "label": {
       "de": "See, Luft, Boden geroutet; Schiene reserviert",
       "en": "sea, air, ground routed; rail reserved"
      }
     },
     {
      "n": 6,
      "suffix": {
       "de": " Admin-Ebenen",
       "en": " admin levels"
      },
      "label": {
       "de": "global, fein- bis grobauflösender Erst-/Letzte-Meile-Schätzer",
       "en": "global, fine-to-coarse first-and-last-mile estimator"
      }
     },
     {
      "n": 14664,
      "suffix": {
       "de": " km",
       "en": " km"
      },
      "label": {
       "de": "konservative See-Pauschale Tür-zu-Tür bei unbekannter Herkunft",
       "en": "conservative sea default door-to-door for unknown origin"
      }
     }
    ],
    "items": [
     {
      "de": "tkm-Faktor erst nachgelagert gebunden — kein Re-Routing",
      "en": "tkm factor bound only downstream — no re-routing"
     },
     {
      "de": "Live oder Cache-only ohne Zugangsdaten; Paritäts-Tests in der CI",
      "en": "Live or cache-only without credentials; parity tests in CI"
     }
    ]
   }
  },
  "lci-fruit": {
   "kicker": {
    "de": "Frucht- und Kulturpflanzen-Inventar",
    "en": "Fruit and crop inventory"
   },
   "slide1": {
    "title": {
     "de": "Die Spezialkulturen, die in der Referenz fehlen",
     "en": "The specialty crops missing from the reference"
    },
    "body": {
     "de": "Viele Frucht-, Gemuese- und Spezialkulturen der rund 2'300 EDB-Lebensmittel fehlen in der Referenz oder haben nur den Stellvertreter «Gemuese, unspezifisch». Dieser Layer baut je Kultur ein prozessbasiertes Inventar bis zum Hoftor – aus FAOSTAT-Ertraegen, länderspezifischen Düngeraten und Feldemissionen.",
     "en": "Many fruit, vegetable and specialty crops among the ~2'300 EDB products are missing from the reference or carry only a «vegetables, unspecified» proxy. This layer builds a process-based inventory to the farm gate per crop – from FAOSTAT yields, country-specific fertiliser rates and field emissions."
    },
    "footnote": {
     "de": "Funktionelle Einheit: 1 kg Erntegut ab Hoftor, Referenzjahr 2020 (2018–2025). Quellen: FAOSTAT-Ertraege, Ludemann 2022 (N/P/K), IPCC 2019 / EMEP-EEA 2019.",
     "en": "Functional unit: 1 kg of crop at the farm gate, reference year 2020 (2018–2025). Sources: FAOSTAT yields, Ludemann 2022 (N/P/K), IPCC 2019 / EMEP-EEA 2019."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 284,
      "label": {
       "de": "prozessbasierte Kultur-Aktivitäten",
       "en": "process-based crop activities"
      }
     },
     {
      "n": 37,
      "label": {
       "de": "Kulturpflanzen-Produkte",
       "en": "crop products"
      }
     },
     {
      "n": 29,
      "suffix": {
       "de": "",
       "en": ""
      },
      "label": {
       "de": "Anbau-Geografien (Länder + Aggregate)",
       "en": "growing geographies (countries + aggregates)"
      }
     }
    ],
    "items": [
     {
      "de": "Erdbeere, Mango, Kokosnuss, Macadamia, Goji, Okra, Avocado, Tee – einzeln modelliert.",
      "en": "Strawberry, mango, coconut, macadamia, goji, okra, avocado, tea – each modelled."
     },
     {
      "de": "Ohne den Layer fallen rund 30 Kategorien auf falsche Pauschal-Stellvertreter zurueck.",
      "en": "Without it, ~30 categories fall back to wrong blanket proxies or drop out."
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Eine Kultur, drei Achsen: Land, Jahr, Anbausystem",
     "en": "One crop, three axes: country, year, production system"
    },
    "body": {
     "de": "Jede Aktivität entsteht aus drei orthogonalen Schichten: agronomisches Kultur-Profil x länderspezifische Eintragsraten x kuratierter BAFU-Katalog – aufgelöst nach Land, Bezugsjahr und Anbausystem, mit sechs berechneten Feldemissionen je Zelle. Beheiztes/unbeheiztes Gewaechshaus, Tunnel und Freiland ergeben verschiedene Inventare; bei Gewaechshaus-Tomate dominiert die Heizenergie und treibt die 2–3-fache Spreizung zwischen NL und ES-Freiland.",
     "en": "Each activity is composed from three orthogonal layers: agronomic crop profile x country-specific input rates x curated BAFU catalogue – resolved by country, reference year and production system, with six computed field emissions per cell. Heated/unheated greenhouse, tunnel and open-field yield distinct inventories; for greenhouse tomato, heating energy dominates and drives the 2–3x spread between NL and ES open-field."
    },
    "footnote": {
     "de": "Sechs Feldemissionen je Zelle: N2O direkt/indirekt, NH3, NO3, PO4, Kalk-/Harnstoff-CO2, Pestizid-Verbleib (IPCC 2019 + EMEP-EEA 2019). Strommix-Tausch ist Konfiguration, keine Neuberechnung. 88 Tests; Agribalyse-3.1-Quervergleich.",
     "en": "Six field emissions per cell: direct/indirect N2O, NH3, NO3, PO4, lime/urea CO2, pesticide fate (IPCC 2019 + EMEP-EEA 2019). Swapping a grid mix is configuration, not re-derivation. 88 tests; Agribalyse 3.1 cross-check."
    },
    "stats": [
     {
      "num": {
       "de": "3",
       "en": "3"
      },
      "label": {
       "de": "Achsen je Eintrag: Land x Jahr x Anbausystem",
       "en": "axes per entry: country x year x production system"
      }
     },
     {
      "num": {
       "de": "46",
       "en": "46"
      },
      "label": {
       "de": "aufgelöste Anbau-Standorte",
       "en": "resolved growing locations"
      }
     },
     {
      "num": {
       "de": "6",
       "en": "6"
      },
      "label": {
       "de": "mechanisch berechnete Feldemissionen je Zelle",
       "en": "mechanically computed field emissions per cell"
      }
     },
     {
      "num": {
       "de": "≈ 2–3×",
       "en": "≈ 2–3×"
      },
      "label": {
       "de": "Gewaechshaus-Tomate (gasbeheizt NL) vs. Freiland (ES) – dokumentierte Heizenergie-Sensitivitaet",
       "en": "greenhouse tomato (gas-heated NL) vs. open field (ES) – documented heating-energy sensitivity"
      }
     }
    ]
   }
  },
  "lci-livestock": {
   "kicker": {
    "de": "Tierhaltung am Hoftor",
    "en": "Livestock at the farm gate"
   },
   "slide1": {
    "title": {
     "de": "Die Referenz-Datenbank kennt keine Milchkuh",
     "en": "The reference database has no dairy cow"
    },
    "body": {
     "de": "Die BAFU/UVEK-Referenz hat kein Hoftor-Inventar für Rind, Schaf, Poulet, Legehenne, Ziege oder Schwein, nur einen «Melk»-Stummel. Dieser Tributary baut es mechanismusgenau nach IPCC-Tier-2 wieder auf.",
     "en": "The BAFU/UVEK reference has no farm-gate inventory for cattle, sheep, broiler, laying hens, goat or pork, only a «milking» stub. This tributary rebuilds it mechanism by mechanism via IPCC Tier 2."
    },
    "footnote": {
     "de": "Prozessbasiertes IPCC-2019-Tier-2-Inventar: Pansen-Methan und Hofdünger CH4/N2O/NH3 nach System und Klimazone. 13 Regionen, Basisjahr 2024, 299 Tests.",
     "en": "Process-based IPCC 2019 Tier 2 inventory: enteric methane and manure CH4/N2O/NH3 by system and climate zone. 13 regions, base year 2024, 299 tests."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 8,
      "label": {
       "de": "Tierarten mit vollem Hoftor-Inventar",
       "en": "species lines with full farm-gate LCI"
      }
     },
     {
      "n": 35,
      "label": {
       "de": "prozessbasierte Aktivitäten",
       "en": "process-based activities"
      }
     },
     {
      "n": 0,
      "label": {
       "de": "Milchproduktion in der Referenz-Datenbank — die Luecke, die dieser Tributary schliesst",
       "en": "milk activities in the reference database — the gap this tributary closes"
      }
     }
    ],
    "items": [
     {
      "de": "Ohne die Schicht faellt Schweizer Milch von ~0,65 kg CO2eq/kg auf den Stummel.",
      "en": "Without the layer, Swiss milk drops from ~0.65 kg CO2eq/kg to the stub."
     },
     {
      "de": "Jeder Fluss deklariert: Pansen, Hofdünger, Futter, Stall, Energie.",
      "en": "Every flow declared: enteric, manure, feed, housing, energy."
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Nicht eine Zahl pro Tierart — sechs drehbare Hebel",
     "en": "Not one number per species — six turnable levers"
    },
    "body": {
     "de": "Statt einer Durchschnittszahl pro Tierart liegt unter jedem Archetyp dasselbe Tier-2-Geruest mit Rasse, Ration, Hofdünger-System, Region, Jahr und Allokation als offene Hebel. So lassen sich Gegenfragen rechnen statt nachschlagen.",
     "en": "Instead of one average per species, the same Tier 2 backbone sits under every archetype, with breed, ration, manure system, region, year and allocation exposed as levers. So counterfactuals can be computed, not looked up."
    },
    "footnote": {
     "de": "Vier Allokationsmethoden spannen den Schweizer Milch-Faktor über 0,731–0,969. Optionale Bovaer-Minderung (3-NOP): rund 26 % weniger Pansen-Methan. Gegen 11 Literaturwerte validiert.",
     "en": "Four allocation methods span the Swiss milk factor across 0.731–0.969. Optional Bovaer mitigation (3-NOP): roughly 26% less enteric methane. Validated against 11 literature values."
    },
    "bullets": [
     {
      "de": "Rasse + Ration: Pansen-Methan aus der Trockenmasse-Aufnahme.",
      "en": "Breed + ration: enteric methane from dry-matter intake."
     },
     {
      "de": "Hofdünger + Klimazone: CH4/N2O/NH3 nach Systemmix.",
      "en": "Manure + climate zone: CH4/N2O/NH3 by system mix."
     },
     {
      "de": "Region + Jahr: 13 Regionen, gueltig 2015–2035.",
      "en": "Region + year: 13 regions, valid 2015–2035."
     },
     {
      "de": "Resultat: 0,17 (Poulet) bis 10,5 (Lamm), Folge der Hebel.",
      "en": "Result: 0.17 (broiler) to 10.5 (lamb), from the levers."
     }
    ]
   }
  },
  "lci-transport-decision": {
   "kicker": {
    "de": "Verkehrsträger-Wahl",
    "en": "Transport-mode choice"
   },
   "slide1": {
    "title": {
     "de": "Ohne Modus kein Transport-Inventar",
     "en": "No mode, no transport inventory"
    },
    "body": {
     "de": "Diese Tributary entscheidet als Einzige im Transport-Stack, welcher Verkehrsträger eine Sendung trägt. Ohne fixierten Modus lässt sich der Faktor pro Tonnenkilometer nicht nachschlagen und das herkunftsbewusste Transport-Inventar bleibt offen. Sie sitzt zwischen Routing und Emissionsfaktoren und schliesst genau diese Lücke.",
     "en": "This tributary is the one layer in the transport stack that decides which mode carries a shipment. Until the mode is fixed, the per-tonne-kilometre factor cannot be looked up and the origin-aware transport inventory stays open. It sits between routing and emission factors and closes exactly that gap."
    },
    "footnote": {
     "de": "Quelle: lci-transport-decision (README, «Why the gap is real»). Stack: lci-ecotransit → lci-transport-decision → lci-transport.",
     "en": "Source: lci-transport-decision (README, «Why the gap is real»). Stack: lci-ecotransit → lci-transport-decision → lci-transport."
    },
    "renderer": "stacked-bar",
    "segments": [
     {
      "value": 1,
      "disp": {
       "de": "Routing",
       "en": "Routing"
      },
      "label": {
       "de": "Wie weit über welche Beine? — lci-ecotransit",
       "en": "How far on which legs? — lci-ecotransit"
      },
      "color": "#94a3b8"
     },
     {
      "value": 1,
      "disp": {
       "de": "Modus-Wahl",
       "en": "Mode choice"
      },
      "label": {
       "de": "Welcher Träger gewinnt? — diese Tributary",
       "en": "Which mode wins? — this tributary"
      },
      "color": "#3b82f6"
     },
     {
      "value": 1,
      "disp": {
       "de": "Emissionen",
       "en": "Emissions"
      },
      "label": {
       "de": "Wie viel pro Tonnenkilometer? — lci-transport",
       "en": "How much per tonne-km? — lci-transport"
      },
      "color": "#94a3b8"
     }
    ],
    "total": {
     "disp": {
      "de": "3 Schritte",
      "en": "3 steps"
     },
     "label": {
      "de": "vom Ort zum Transport-Inventar",
      "en": "from origin to transport inventory"
     },
     "max": 3
    },
    "callout": {
     "de": "Ohne den mittleren Schritt schliesst das Inventar nicht.",
     "en": "Without the middle step the inventory does not close."
    }
   },
   "slide2": {
    "title": {
     "de": "Eine Regel, zwei Stufen, vier Konstanten je Träger",
     "en": "One rule, two stages, four constants per mode"
    },
    "body": {
     "de": "Die Antwort kommt aus einem einzigen, deterministischen Aufruf ohne Laufzeit-Abhängigkeiten: Stufe 1 filtert nach Verderblichkeit (Reisezeit gegen Lagerfenster), Stufe 2 wählt den günstigsten der verbleibenden Träger. Logik und Konstanten je Träger liegen an einem prüfbaren Ort, fixiert durch Paritätstests gegen die Produktionsquelle — eine Referenzregel statt der flachen «immer Strasse»-Heuristik.",
     "en": "The answer comes from one deterministic call with no runtime dependencies: stage 1 filters by perishability (travel time against the storage window), stage 2 picks the cheapest surviving mode. Logic and per-mode constants live in one auditable place, pinned by parity tests against the production source — a reference rule instead of the flat «always road» heuristic."
    },
    "footnote": {
     "de": "Quelle: lci-transport-decision, decision.py (TRAVEL_SPEEDS, LOADING_TIMES, DISTANCE_PRICES, LOADING_PRICES). Konstanten verbatim aus der Produktionsquelle.",
     "en": "Source: lci-transport-decision, decision.py (TRAVEL_SPEEDS, LOADING_TIMES, DISTANCE_PRICES, LOADING_PRICES). Constants verbatim from the production source."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 2,
      "label": {
       "de": "Stufen: Verderblichkeit, dann Kosten",
       "en": "stages: perishability, then cost"
      }
     },
     {
      "n": 4,
      "label": {
       "de": "Träger: Strasse, Schiene, See, Luft",
       "en": "modes: road, rail, sea, air"
      }
     },
     {
      "n": 0,
      "label": {
       "de": "Laufzeit-Abhängigkeiten",
       "en": "runtime dependencies"
      }
     }
    ],
    "items": [
     {
      "de": "Stufe 1 filtert Modi über dem Lagerfenster — fällt offen auf den schnellsten zurück",
      "en": "Stage 1 drops modes over the storage window — fails open to the fastest"
     },
     {
      "de": "Stufe 2 minimiert die Kosten; Vor- und Nachlauf stets zum Strassen-Tarif",
      "en": "Stage 2 minimises cost; pre- and post-carriage always at the road rate"
     },
     {
      "de": "Konstanten als austauschbare Wörterbücher — Träger neu ableiten ohne Regeleingriff",
      "en": "Constants as swappable dictionaries — re-derive a mode without touching the rule"
     }
    ]
   }
  },
  "lci-cotton": {
   "kicker": {
    "de": "Baumwolle vom Feld bis zum Hoftor",
    "en": "Cotton from the field to the farm gate"
   },
   "slide1": {
    "title": {
     "de": "Ein Weltdurchschnitt — oder die echte Anbauregion",
     "en": "One world average — or the real growing region"
    },
    "body": {
     "de": "Die öffentliche Referenz-Datenbank kennt für Baumwolle nur einen globalen Stellvertreter (China): keine Indien-/Bangladesch-Aktivität, kein Split konventionell/biologisch, keine Stellhebel für Stickstoff, Harnstoff oder Bewässerung. Dieses Modul ersetzt den flachen Wert durch prozessbasierte Cradle-to-Farm-Gate-Aktivitäten je Region und System — Indien (national, Gujarat, Odisha), Bangladesch, Restwelt, Weltmarkt.",
     "en": "For cotton, the public reference database knows only one global proxy (China): no India/Bangladesh activity, no conventional/organic split, no levers for nitrogen, urea or irrigation. This module replaces that flat value with process-based cradle-to-farm-gate activities per region and system — India (national, Gujarat, Odisha), Bangladesh, Rest-of-World, global market."
    },
    "footnote": {
     "de": "Quelle: lci-cotton README + Methodik-Report. 11 Produktions-Aktivitäten plus 6 Markt-/Spiegel-Zeilen; 2 Referenzprodukte (gegerbte Faser, Saatbaumwolle); Referenzjahr 2020 (Daten 2018–2023). 28 Tests.",
     "en": "Source: lci-cotton README + methodology report. 11 production activities plus 6 market/mirror rows; 2 reference products (ginned lint, seed-cotton); reference year 2020 (data 2018–2023). 28 tests."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 1,
      "label": {
       "de": "globaler Stellvertreter (China) ersetzt — durch region- und systemaufgelöste eigene Aktivitäten",
       "en": "global proxy (China) replaced — by region- and system-resolved distinct activities"
      }
     },
     {
      "n": 11,
      "suffix": {
       "de": " benannte",
       "en": " named"
      },
      "label": {
       "de": "Produktions-Aktivitäten über Indien, Bangladesch, Restwelt und Weltmarkt (plus 6 Markt-/Spiegel-Zeilen)",
       "en": "production activities across India, Bangladesh, Rest-of-World and the global market (plus 6 market/mirror rows)"
      }
     },
     {
      "n": 2,
      "label": {
       "de": "Systeme als eigene Aktivitäten geführt: konventionell und biologisch — kein Flag auf einer geteilten Aktivität",
       "en": "systems carried as distinct activities: conventional and organic — not a flag on a shared activity"
      }
     }
    ],
    "items": [
     {
      "de": "Biosphäre aus per-Hektar-Raten gerechnet (Lachgas, Ammoniak, Nitrat, CO2, Pestizid)",
      "en": "biosphere computed from per-hectare rates (N2O, ammonia, nitrate, CO2, pesticide)"
     },
     {
      "de": "Technosphäre bindet Hintergrund-Aktivitäten per Katalog-Code, frei austauschbar",
      "en": "technosphere binds background activities by catalogue code, freely swappable"
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Was der Weltdurchschnitt verschluckt",
     "en": "What the world average swallows"
    },
    "body": {
     "de": "Weil die Feldemissionen je Region aus eigenen Eingangsraten und Emissionsfaktoren gerechnet werden, treten Unterschiede hervor, die ein Stellvertreter wegmittelt: Bangladesch oben (gleicher Stickstoff, tieferer Ertrag), mechanisierte Restwelt unten, Indien dazwischen — mit feldgemessenem Lachgas-Faktor 1,3 % statt globalem 1,0 %. Bio läuft als eigene Aktivität und steht per Konstruktion auf null.",
     "en": "Because each region's field emissions are computed from its own input rates and emission factors, differences a proxy averages away become visible: Bangladesh at the top (same nitrogen, lower yield), mechanised Rest-of-World at the bottom, India in between — with a field-measured nitrous-oxide factor of 1.3% instead of the global 1.0%. Organic runs as its own activity and sits at zero by construction."
    },
    "footnote": {
     "de": "Quelle: lci-cotton README (Figure 2) + region_gwp_only.typ. Werte = direkter On-Farm-Feldemissions-Beitrag in kg CO2eq/kg Lint; Technosphäre komponiert der Solver darüber. Indien-EF1 1,3 % aus Meta-Analyse 2023; Bio-Null per Testsuite geprüft.",
     "en": "Source: lci-cotton README (Figure 2) + region_gwp_only.typ. Values = direct on-farm field-emission contribution in kg CO2eq/kg lint; technosphere composed on top by the solver. India EF1 1.3% from 2023 meta-analysis; organic-zero checked by the test suite."
    },
    "bars": [
     {
      "label": {
       "de": "Bangladesch konventionell (350 kg Lint/ha)",
       "en": "Bangladesh conventional (350 kg lint/ha)"
      },
      "value": 1.85,
      "disp": {
       "de": "1,85",
       "en": "1.85"
      },
      "color": "#b45309"
     },
     {
      "label": {
       "de": "Indien konventionell (450 kg/ha, EF1 1,3 %)",
       "en": "India conventional (450 kg/ha, EF1 1.3%)"
      },
      "value": 1.33,
      "disp": {
       "de": "1,33",
       "en": "1.33"
      },
      "color": "#d97706"
     },
     {
      "label": {
       "de": "Restwelt konventionell (750 kg/ha, mechanisiert)",
       "en": "Rest-of-World conventional (750 kg/ha, mechanised)"
      },
      "value": 0.71,
      "disp": {
       "de": "0,71",
       "en": "0.71"
      },
      "color": "#f59e0b"
     },
     {
      "label": {
       "de": "Bio-Saatbaumwolle (Odisha / Restwelt) — null synthetischer Stickstoff",
       "en": "Organic seed-cotton (Odisha / Rest-of-World) — zero synthetic nitrogen"
      },
      "value": 0,
      "disp": {
       "de": "0,00",
       "en": "0.00"
      },
      "color": "#16a34a"
     }
    ]
   }
  },
  "lci-spices-additives": {
   "kicker": {
    "de": "GEWÜRZE & ZUSATZSTOFFE",
    "en": "SPICES & ADDITIVES"
   },
   "slide1": {
    "title": {
     "de": "Vom Pauschalwert zum echten Inventar",
     "en": "From a flat stub to a real inventory"
    },
    "body": {
     "de": "Zwölf Gewürz- und Zusatzstoff-Produkte trugen denselben Pauschalwert von 0,30 kg CO₂eq/kg — ohne einen einzigen Fluss. Dieses Modell ersetzt ihn durch prozessbasierte Komposite vom Feld bis zum Hoftor: Anbau, Düngerproduktion, Feld-Stickstoff und Trocknung.",
     "en": "Twelve spice and additive products carried the same flat 0.30 kg CO₂eq/kg — with not a single flow. This model replaces it with process-based composites from field to farm gate: cultivation, fertiliser production, field nitrogen and drying."
    },
    "footnote": {
     "de": "Quellen: Tamil Nadu Agricultural University 2020; ICAR-IISR Kerala; IPCC 2019 Tier 1; Trocknung nach Kurniawati et al. 2023.",
     "en": "Sources: Tamil Nadu Agricultural University 2020; ICAR-IISR Kerala; IPCC 2019 Tier 1; drying per Kurniawati et al. 2023."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 12,
      "label": {
       "de": "Produkte mit identischem 0,30-Platzhalter ersetzt",
       "en": "products with the identical 0.30 placeholder replaced"
      }
     },
     {
      "n": 0,
      "label": {
       "de": "Technosphären- und Feldemissions-Flüsse im alten Stub",
       "en": "technosphere and field-emission flows in the old stub"
      }
     }
    ],
    "items": [
     {
      "de": "Vorher: ein fixer Wert je Kultur, keine Flüsse",
      "en": "Before: one fixed value per crop, no flows"
     },
     {
      "de": "Nachher: Anbau-Inputs aus indischer Agronomie",
      "en": "After: cultivation inputs from Indian agronomy"
     },
     {
      "de": "Feld-Stickstoff (N₂O / NH₃ / NO₃), IPCC 2019 Tier 1",
      "en": "Field nitrogen (N₂O / NH₃ / NO₃), IPCC 2019 Tier 1"
     },
     {
      "de": "Trocknung als Energieprozess, an BAFU gekoppelt",
      "en": "Drying as energy process, linked to BAFU"
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Ein Wert pro Kultur statt eines für alle",
     "en": "One value per crop instead of one for all"
    },
    "body": {
     "de": "Mit eigenem Inventar je Kultur fächern sich die Fussabdrücke nach realer Agronomie auf. Treiber ist der Ertrag: Kurkuma liefert 5'500 kg/ha und landet bei rund 1,5–4 kg CO₂eq/kg, Kardamom nur 225 kg/ha — dieselbe Last auf 24× weniger Kilo — und erreicht 12,59.",
     "en": "With its own inventory per crop, footprints spread out along real agronomy. The driver is yield: turmeric delivers 5'500 kg/ha and lands at roughly 1.5–4 kg CO₂eq/kg, cardamom only 225 kg/ha — the same load over 24× fewer kilos — reaching 12.59."
    },
    "footnote": {
     "de": "Funktionseinheit: 1 kg getrocknetes Produkt am Hoftor, Indien, 2022. Kardamom Brightway-berechnet (BAFU GWP100).",
     "en": "Functional unit: 1 kg dried product at farm gate, India, 2022. Cardamom Brightway-computed (BAFU GWP100)."
    },
    "bars": [
     {
      "label": {
       "de": "Alter Platzhalter — gleich für alle 12",
       "en": "Old placeholder — same for all 12"
      },
      "value": 0.3,
      "disp": {
       "de": "0,30",
       "en": "0.30"
      },
      "color": "#9ca3af"
     },
     {
      "label": {
       "de": "Kurkuma (5'500 kg/ha)",
       "en": "Turmeric (5'500 kg/ha)"
      },
      "value": 2.75,
      "disp": {
       "de": "≈ 1,5–4",
       "en": "≈ 1.5–4"
      },
      "color": "#84cc16"
     },
     {
      "label": {
       "de": "Kardamom (225 kg/ha)",
       "en": "Cardamom (225 kg/ha)"
      },
      "value": 12.59,
      "disp": {
       "de": "12,59",
       "en": "12.59"
      },
      "color": "#15803d"
     }
    ]
   }
  },
  "lci-cashew": {
   "kicker": {
    "de": "Cashew-Kern-Inventar",
    "en": "Cashew kernel inventory"
   },
   "slide1": {
    "title": {
     "de": "Vom Platzhalter zur nachprüfbaren Bilanz",
     "en": "From placeholder to an auditable inventory"
    },
    "body": {
     "de": "Die Eaternity-Datenbank kannte Cashew-Kerne nur als zwei Platzhalter: ein fixes Treibhausgas-Ziel ohne physische Stoff- und Energiebilanz. Dieser Tributary ersetzt sie durch eine offene Prozess-Bilanz für 1 kg sortierten getrockneten Kern, in der jede Zahl auf eine zitierbare physische Grösse zurueckgeht und die Vorketten von der LCA-Engine aufgelöst werden.",
     "en": "The Eaternity database knew cashew kernels only as two placeholders: a fixed greenhouse-gas target with no physical material and energy inventory. This tributary replaces them with an open process inventory for 1 kg of selected dried kernel, where every figure traces to a citable physical quantity and supply chains are resolved by the LCA engine."
    },
    "footnote": {
     "de": "Funktionelle Einheit 1 kg sortierter getrockneter Kern, Obstgarten bis Werktor ohne Fernverkehr, RER 2022.",
     "en": "Functional unit 1 kg selected dried kernel, orchard to facility gate without long-distance transport, RER 2022."
    },
    "stats": [
     {
      "num": {
       "de": "2 → 1",
       "en": "2 → 1"
      },
      "label": {
       "de": "Platzhalter-Eintraege ohne Bilanz ersetzt durch 1 offene, nachprüfbare Prozess-Aktivität",
       "en": "placeholder records without an inventory replaced by 1 open, auditable process activity"
      }
     },
     {
      "num": {
       "de": "jede Zahl",
       "en": "every figure"
      },
      "label": {
       "de": "rueckverfolgbar auf eine publizierte physische Grösse - kein proprietaeres GWP-Ziel mehr eingebacken",
       "en": "traceable to a published physical quantity - no proprietary GWP target baked in anymore"
      }
     },
     {
      "num": {
       "de": "frei variierbar",
       "en": "freely tunable"
      },
      "label": {
       "de": "Ertrag, Energie und Emissionsfaktoren als offene Parameter - Sensitivitaets-Analyse erstmals möglich",
       "en": "yield, energy and emission factors as open parameters - sensitivity analysis possible for the first time"
      }
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Drei Quellen, zu einer Aktivität verkettet",
     "en": "Three sources chained into one activity"
    },
    "body": {
     "de": "Der Tributary baut die Bilanz aus drei publizierten Datenschichten: Anbau und Ertrag aus der RSB-Cashew-Studie, Verarbeitungsenergie aus einem indischen Energie-Audit und Feldemissionen nach IPCC 2019. Daraus entsteht eine Vordergrund-Aktivität mit 6 Technosphaeren-Flüssen an BAFU/UVEK-Ankern und 5 Biosphaeren-Flüssen, jeder mit p5/p95-Grenzen - und sichtbar wird der Stickstoff aus liegengelassenen Cashew-Aepfeln, der allein 86 % des Fussabdrucks treibt.",
     "en": "The tributary builds the inventory from three published data layers: cultivation and yield from the RSB cashew study, processing energy from an Indian energy audit and field emissions per IPCC 2019. This yields a foreground activity with 6 technosphere flows on BAFU/UVEK anchors and 5 biosphere flows, each with p5/p95 bounds - making visible the nitrogen from discarded cashew apples, which alone drives 86% of the footprint."
    },
    "footnote": {
     "de": "Quellen: RSB 2022 (Anbau, Ertrag), Dhanushkodi et al. 2016 (Verarbeitungsenergie), IPCC 2019 (Feld-N2O, EF1 + EF4/EF5). Referenz-Check 0,574 kg CO2eq/kg in Literaturspanne 0,3-3,3.",
     "en": "Sources: RSB 2022 (cultivation, yield), Dhanushkodi et al. 2016 (processing energy), IPCC 2019 (field N2O, EF1 + EF4/EF5). Reference check 0.574 kg CO2eq/kg within literature band 0.3-3.3."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 3,
      "label": {
       "de": "unabhaengig publizierte Datenschichten zu einer Aktivität verkettet - kein generischer Nuss-Proxy",
       "en": "independently published data layers chained into one activity - no generic nut proxy"
      }
     },
     {
      "n": 11,
      "label": {
       "de": "Flüsse pro kg Kern: 6 Technosphaere an BAFU-Ankern + 5 Biosphaere mit p5/p95-Grenzen",
       "en": "flows per kg kernel: 6 technosphere on BAFU anchors + 5 biosphere with p5/p95 bounds"
      }
     },
     {
      "n": 86,
      "suffix": {
       "de": " %",
       "en": "%"
      },
      "label": {
       "de": "des Fussabdrucks stammen aus Feld-N2O der verrottenden Cashew-Aepfel - sichtbar erst durch die offene Bilanz",
       "en": "of the footprint comes from field N2O of the decomposing cashew apples - visible only through the open inventory"
      }
     }
    ],
    "items": [
     {
      "de": "Energie und Material laufen über Technosphaeren-Anker; Vorketten löst die LCA-Engine auf.",
      "en": "Energy and material flow through technosphere anchors; supply chains resolved by the LCA engine."
     },
     {
      "de": "Hand-Schaelen braucht kaum Strom; die Waerme kommt als Biomasse aus den eigenen Schalen.",
      "en": "Hand-shelling needs almost no electricity; heat comes as biomass from its own shells."
     }
    ]
   }
  },
  "lci-fertiliser": {
   "kicker": {
    "de": "Dünger-Eingangsschicht",
    "en": "Fertiliser input layer"
   },
   "slide1": {
    "title": {
     "de": "Jede Düngersorte einzeln zugeordnet — statt ein pauschaler Durchschnitt",
     "en": "Every fertiliser grade mapped individually — instead of one pooled average"
    },
    "body": {
     "de": "402 Aktivitäten — N-, P-, K-Mineraldünger, Wirtschaftsdünger, Kalk, angrenzende Chemikalien und Agrar-Energie — fehlen in der offenen Schweizer Referenz. Diese Schicht ordnet sie sortenscharf zu: 247 von 260 Kernaktivitäten (95%) erhalten einen Anker, die übrigen 13 werden markiert.",
     "en": "402 activities — N, P, K mineral grades, manures, lime, adjacent chemicals and agricultural energy — are missing from the open Swiss reference. This layer maps them grade by grade: 247 of 260 core activities (95%) get an anchor, the remaining 13 are flagged."
    },
    "footnote": {
     "de": "402 = 262 Dünger + 50 Chemikalien + 90 Agrar-Energie; 95% (247/260) im Kern. 21 Regionen, 2015–2025 (Ref. 2023), 148 Tests. Quelle: README.md.",
     "en": "402 = 262 fertiliser + 50 chemicals + 90 agriculture energy; 95% (247/260) in core. 21 regions, 2015–2025 (ref. 2023), 148 tests. Source: README.md."
    },
    "renderer": "stacked-bar",
    "segments": [
     {
      "value": 262,
      "disp": {
       "de": "262",
       "en": "262"
      },
      "label": {
       "de": "Dünger-Kern (N/P/K, Wirtschaftsdünger, Kalk)",
       "en": "Fertiliser core (N/P/K, manures, lime)"
      },
      "color": "#3a7d44"
     },
     {
      "value": 90,
      "disp": {
       "de": "90",
       "en": "90"
      },
      "label": {
       "de": "Agrar-Energie",
       "en": "Agriculture energy"
      },
      "color": "#6aa84f"
     },
     {
      "value": 50,
      "disp": {
       "de": "50",
       "en": "50"
      },
      "label": {
       "de": "Industriechemikalien",
       "en": "Industrial chemicals"
      },
      "color": "#a9c47f"
     }
    ],
    "total": {
     "disp": {
      "de": "402",
      "en": "402"
     },
     "label": {
      "de": "zugeordnete Aktivitäten, sortenscharf",
      "en": "mapped activities, grade by grade"
     },
     "max": 402
    },
    "callout": {
     "de": "Vier offengelegte Strategien pro Zeile: Aggregat, Exakt-Treffer, Proxy mit Umrechnungsfaktor, vermerkter Nicht-Treffer — so ist die Verlässlichkeit pro Sorte prüfbar, nicht pro Katalog.",
     "en": "Four disclosed strategies per row: aggregate, exact-match, proxy with conversion factor, flagged non-match — so reliability is auditable per grade, not per catalogue."
    }
   },
   "slide2": {
    "title": {
     "de": "An jeder Sorte hängt die Feldemission — über vier unabhängige Achsen",
     "en": "Field emissions attached to every grade — across four independent axes"
    },
    "body": {
     "de": "Die Düngerproduktion ist nur die halbe Geschichte; auf dem Feld entstehen NH3, N2O, NOx und CO2. Diese Schicht hängt je Sorte ein IPCC-Tier-1-Overlay an, das auf vier Achsen reagiert: Sorte, Klimazone, Boden-pH und Ausbringmethode — Spreizungen, die ein Durchschnitt vernichtet.",
     "en": "Fertiliser production is only half the story; in the field come NH3, N2O, NOx and CO2. This layer attaches an IPCC Tier 1 overlay per grade, responding to four axes: grade, climate zone, soil pH and application method — spreads a single average destroys."
    },
    "footnote": {
     "de": "IPCC 2019 (N2O EF1 0,016 feucht / 0,005 trocken), EMEP/EEA 2019 (NH3 0,008–0,165), Agrammon 2022; CO2 aus Harnstoff (1,57 kg CO2/kg N). Quelle: README.md.",
     "en": "IPCC 2019 (N2O EF1 0.016 wet / 0.005 dry), EMEP/EEA 2019 (NH3 0.008–0.165), Agrammon 2022; CO2 from urea (1.57 kg CO2/kg N). Source: README.md."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 4,
      "label": {
       "de": "Feldemissions-Pfade je Zeile: NH3, N2O, NOx, CO2",
       "en": "field-emission pathways per row: NH3, N2O, NOx, CO2"
      }
     },
     {
      "n": 4,
      "label": {
       "de": "unabhängige Achsen: Sorte, Klimazone, Boden-pH, Ausbringmethode",
       "en": "independent axes: grade, climate zone, soil pH, application method"
      }
     },
     {
      "n": 20,
      "suffix": {
       "de": "×",
       "en": "×"
      },
      "label": {
       "de": "Spreizung der NH3-Verflüchtigung je Sorte und pH (0,008–0,165)",
       "en": "spread in NH3 volatilisation by grade and pH (0.008–0.165)"
      }
     }
    ],
    "items": [
     {
      "de": "Direkter Lachgasfaktor schwankt um Faktor drei — Default 0,01 verdeckt das.",
      "en": "Direct nitrous-oxide factor varies threefold — default 0.01 hides it."
     },
     {
      "de": "Biosphären-Flüsse per Katalogcode: Solver wählt die Methode.",
      "en": "Biosphere flows by catalogue code: solver picks the method."
     }
    ]
   }
  },
  "lci-mushroom": {
   "kicker": {
    "de": "PILZ-MODELL",
    "en": "MUSHROOM MODEL"
   },
   "slide1": {
    "title": {
     "de": "Pilze sind ein Energieprodukt",
     "en": "Mushrooms are an energy product"
    },
    "body": {
     "de": "Indoor-Pilzzucht lebt von Energie: Gas zur Substrat-Sterilisation und Strom für Klima und Licht. Wir bauen den Anbau als echten Prozess neu auf — diese zwei Schritte machen rund 89% der Bilanz und fehlten im alten Hintergrund-Datensatz ganz.",
     "en": "Indoor mushroom growing runs on energy: gas to sterilise the substrate, electricity for climate and light. We rebuild cultivation as a real process — these two steps make up about 89% of the footprint and were absent from the old background dataset."
    },
    "footnote": {
     "de": "1 kg frischer Austernpilz ab Hof, RER-Strommix. Quelle: Dorr et al. 2021 (HAL-03105622), Brightway-berechnet.",
     "en": "1 kg fresh oyster mushroom at farm gate, RER grid mix. Source: Dorr et al. 2021 (HAL-03105622), Brightway-computed."
    },
    "renderer": "stacked-bar",
    "segments": [
     {
      "value": 2.43,
      "disp": {
       "de": "2,43",
       "en": "2.43"
      },
      "label": {
       "de": "Strom · Klima + Licht · 56%",
       "en": "Electricity · climate + light · 56%"
      },
      "color": "#16a34a"
     },
     {
      "value": 1.45,
      "disp": {
       "de": "1,45",
       "en": "1.45"
      },
      "label": {
       "de": "Erdgas · Sterilisation · 33%",
       "en": "Natural gas · sterilisation · 33%"
      },
      "color": "#8BC34A"
     },
     {
      "value": 0.47,
      "disp": {
       "de": "0,47",
       "en": "0.47"
      },
      "label": {
       "de": "Spawn, Sperrholz, Übriges · 11%",
       "en": "Spawn, plywood, rest · 11%"
      },
      "color": "#FFC107"
     }
    ],
    "total": {
     "disp": {
      "de": "4,35",
      "en": "4.35"
     },
     "label": {
      "de": "kg CO₂eq / kg ab Hof",
      "en": "kg CO₂eq / kg at farm gate"
     },
     "max": 4.35
    },
    "callout": {
     "de": "Im US-Champignon-Datensatz fehlten Sterilisation und Klimaregelung ganz — darum lag der Wert ~7× zu tief.",
     "en": "The US button-mushroom dataset had no sterilisation or climate control — that is why the value sat ~7× too low."
    }
   },
   "slide2": {
    "title": {
     "de": "Drei echte Anbau-Inventare statt eines Platzhalters",
     "en": "Three real cultivation inventories, not a placeholder"
    },
    "body": {
     "de": "Statt fremde Tauschflüsse umzuhängen, modellieren wir die Pilzzucht als Prozess auf BAFU-Technosphäre: Austernpilz auf Kaffeesatz (RER) und Thai-Shiitake im Sägemehlbeutel. Jeder Input ist aus der Literatur transkribiert. Grösster Hebel bleibt der Strommix: 3,18 (FR) bis 7,65 (DE) kg CO₂eq/kg.",
     "en": "Instead of remapping someone else's exchanges, we model cultivation as a process on BAFU technosphere: oyster mushroom on coffee grounds (RER) and Thai shiitake in sawdust bags. Every input is transcribed from literature. Biggest lever stays grid mix: 3.18 (FR) to 7.65 (DE) kg CO₂eq/kg."
    },
    "footnote": {
     "de": "3 Mapping-Einträge ab Hof; Substrat als Cut-off-Nebenprodukt. Quelle: Dorr et al. 2021, Sukkanta 2021, Ueawiwatsakul 2014.",
     "en": "3 farm-gate mapping entries; substrate as cut-off byproduct. Sources: Dorr et al. 2021, Sukkanta 2021, Ueawiwatsakul 2014."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 3,
      "label": {
       "de": "Mapping-Einträge · Austernpilz RER (Produktion + Markt) + Thai-Shiitake",
       "en": "mapping entries · oyster RER (production + market) + Thai shiitake"
      }
     },
     {
      "n": 11,
      "label": {
       "de": "BAFU-Technosphäre-Inputs pro kg Austernpilz, alle transkribiert",
       "en": "BAFU technosphere inputs per kg oyster, all transcribed"
      }
     },
     {
      "n": 7,
      "suffix": {
       "de": "×",
       "en": "×"
      },
      "label": {
       "de": "zu tief ohne diese Tributary (~0,58 statt ~4,35); Strommix-Spanne FR→DE 3,18 → 7,65 (×2,4)",
       "en": "too low without this tributary (~0.58 vs ~4.35); grid-mix span FR→DE 3.18 → 7.65 (×2.4)"
      }
     }
    ],
    "items": [
     {
      "de": "Cradle-to-Farm-Gate; Substrat-Feedstocks als Cut-off ohne Vorbelastung",
      "en": "Cradle-to-farm-gate; substrate feedstocks cut-off, no upstream burden"
     },
     {
      "de": "Fehlende Mengen werden markiert, nicht aufgefüllt — kein Spatio-Temporal-Modell",
      "en": "Missing quantities flagged, not back-filled — no spatio-temporal model"
     }
    ]
   }
  },
  "lci-oilpalm": {
   "kicker": {
    "de": "PALMÖL-MODELL",
    "en": "OIL PALM MODEL"
   },
   "slide1": {
    "title": {
     "de": "Die Referenz-Datenbank kennt keine Palmfrucht – dieses Modell baut sie",
     "en": "The reference database has no oil-palm fruit – this model builds it"
    },
    "body": {
     "de": "Im BAFU/UVEK-Hintergrund fehlt eine Aktivität für Palmöl-Frischfruchtstände; die Einzelstudien sind publiziert, aber verstreut. Dieser Tributary baut die Schicht neu: sechs Regionen aus publizierten Einsatzraten, vier Feldemissionen aus offenen IPCC-2019- und EMEP/EEA-2019-Faktoren – so wird der FFB-Schritt jedes Palmöl-Produkts aus Primärquellen reproduzierbar.",
     "en": "The BAFU/UVEK background has no oil-palm fresh-fruit-bunch activity; the studies are published but scattered. This tributary builds the layer anew: six regions from published input rates, four field emissions from open IPCC 2019 and EMEP/EEA 2019 factors – making the FFB step reproducible from primary sources."
    },
    "footnote": {
     "de": "Cradle-to-Plantation-Gate, Mineralboden; je Aktivität 9 BAFU-Technosphäre-Referenzen + 4 modellberechnete Biosphären-Austausche; Referenzjahr 2020.",
     "en": "Cradle-to-plantation-gate, mineral soil; per activity 9 BAFU technosphere references + 4 model-computed biosphere exchanges; reference year 2020."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 0,
      "suffix": {
       "de": " in der Referenz",
       "en": " in the reference"
      },
      "label": {
       "de": "Palmfrucht-Aktivitäten im BAFU/UVEK-Hintergrund – die Lücke, die dieses Modell schliesst",
       "en": "Oil-palm fruit activities in the BAFU/UVEK background – the gap this model closes"
      }
     },
     {
      "n": 6,
      "label": {
       "de": "von Grund auf gebaute Regionen (IDN, MYS, GLO, THA, NGA, COL)",
       "en": "regions built from scratch (IDN, MYS, GLO, THA, NGA, COL)"
      }
     },
     {
      "n": 4,
      "label": {
       "de": "Feld-Biosphärenemissionen je Aktivität: N2O, NH3, NO3, Pestizid-Verbleib",
       "en": "field biosphere emissions per activity: N2O, NH3, NO3, pesticide fate"
      }
     }
    ],
    "items": [
     {
      "de": "Einsatzraten aus publizierten Primärstudien montiert, nicht geschätzt",
      "en": "input rates assembled from published primary studies, not estimated"
     },
     {
      "de": "Emissionen aus offenen IPCC-2019- und EMEP/EEA-2019-Faktoren berechnet",
      "en": "emissions computed from open IPCC 2019 and EMEP/EEA 2019 factors"
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Was die gebaute Schicht belastbar macht: drei Struktur-Entscheidungen",
     "en": "What makes the built layer durable: three structural choices"
    },
    "body": {
     "de": "Der Wert steckt im Bau. Der Ländermix bleibt erhalten: Indonesien (~59% der Weltproduktion, Ammoniumsulfat-N, 17'500 kg/ha) und Malaysia (~27%, Harnstoff-N, 20'700 kg/ha) tragen eigene gemessene Raten. Feldemissionen und Energie-Kohlenstoff sind getrennt und neu ableitbar; der Mineralboden-Scope ist explizit, Torf und Entwaldung gehen an die Landnutzungs-Schicht.",
     "en": "The value is in the build. The country mix is preserved: Indonesia (~59% of world production, ammonium-sulphate-N, 17'500 kg/ha) and Malaysia (~27%, urea-N, 20'700 kg/ha) each carry measured rates. Field emissions and energy carbon are split and rederivable; the mineral-soil scope is explicit, peat and deforestation hand off to the land-use layer."
    },
    "footnote": {
     "de": "Raten: Stichnothe & Schweinle 2011 (IDN), Zulkifli 2010 (MYS); GLO = FAOSTAT-2020-gewichteter Mittelwert; THA/NGA/COL als IDN-Proxys markiert.",
     "en": "Rates: Stichnothe & Schweinle 2011 (IDN), Zulkifli 2010 (MYS); GLO = FAOSTAT-2020-weighted mean; THA/NGA/COL flagged as IDN proxies."
    },
    "bullets": [
     {
      "de": "Ländermix erhalten – IDN und MYS (zusammen ~86% der Weltproduktion) tragen je eigene Raten; GLO ist ihr transparenter FAOSTAT-Mittelwert, keine dritte Annahme",
      "en": "Country mix preserved – IDN and MYS (together ~86% of world production) each carry own rates; GLO is their transparent FAOSTAT mean, not a third assumption"
     },
     {
      "de": "Zwei trennbare Hälften – Modell-Feldemissionen vs. vorgelagerter Energie-Kohlenstoff über BAFU-Referenzen; Hintergrund austauschbar ohne Neuableitung der Inventur",
      "en": "Two separable halves – model field emissions vs. upstream energy carbon via BAFU references; background swappable without rederiving the inventory"
     },
     {
      "de": "Expliziter Mineralboden-Scope – Torf-Entwässerung und Entwaldung gehen an die Landnutzungs-Schicht; jede Zelle markiert direkt, gewichtet oder dokumentierter Proxy",
      "en": "Explicit mineral-soil scope – peat drainage and deforestation hand off to the land-use layer; every cell flagged direct, weighted, or documented proxy"
     }
    ]
   }
  },
  "lci-pesticide": {
   "kicker": {
    "de": "Pestizid-Verbleibsmodell",
    "en": "Pesticide fate model"
   },
   "slide1": {
    "title": {
     "de": "Statt einem Pauschal-Pestizid: Verbleib pro Molekül",
     "en": "Instead of one generic pesticide: fate per molecule"
    },
    "body": {
     "de": "Offene Datenbanken kennen nur «Pestizid, unspezifisch», pauschal in den Boden. Dieses Tributary verteilt 1 kg Wirkstoff nach Stoffeigenschaften (Dampfdruck, Koc, Halbwertszeit) auf fünf Kompartimente — je nach Molekül völlig anders.",
     "en": "Open databases only know «pesticide, unspecified», flatly to soil. This tributary distributes 1 kg active ingredient by properties (vapour pressure, Koc, half-life) across five compartments — entirely differently per molecule."
    },
    "footnote": {
     "de": "Quelle: lci-pesticide README (PestLCI 2.0 + DT50-Gewichtung). Einheit: 1 kg Wirkstoff am regionalen Lager.",
     "en": "Source: lci-pesticide README (PestLCI 2.0 + DT50 weighting). Unit: 1 kg active ingredient at the regional storehouse."
    },
    "bars": [
     {
      "label": {
       "de": "Dimethenamide (Mais, offener Boden)",
       "en": "Dimethenamide (maize, open soil)"
      },
      "value": 76.8,
      "disp": {
       "de": "Boden 77% · Wasser 18% · Luft 5%",
       "en": "Soil 77% · Water 18% · Air 5%"
      },
      "color": "#8B5A2B"
     },
     {
      "label": {
       "de": "Isoproturon (Wintergetreide)",
       "en": "Isoproturon (winter cereals)"
      },
      "value": 57.6,
      "disp": {
       "de": "Boden 58% · Pflanze 24% · Wasser 14% · Luft 4%",
       "en": "Soil 58% · Plant 24% · Water 14% · Air 4%"
      },
      "color": "#A98467"
     },
     {
      "label": {
       "de": "Folpet (Reben, volles Blattwerk)",
       "en": "Folpet (vines, full canopy)"
      },
      "value": 18.6,
      "disp": {
       "de": "Pflanze 79% · Boden 19% · Wasser 2% · Luft 1%",
       "en": "Plant 79% · Soil 19% · Water 2% · Air 1%"
      },
      "color": "#16a34a"
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Eine abfragbare Schicht zwischen Literatur und Feld",
     "en": "A queryable layer between literature and field"
    },
    "body": {
     "de": "Die Wirkstoffmasse verteilt sich auf fünf Kompartimente (Luft, Wasser, Boden, Sediment, Grundwasser). Diese Schicht rechnet den Verbleib aus publizierten physikochemischen Daten und bindet ihn an den offenen BAFU/UVEK-Hintergrund.",
     "en": "Active-ingredient mass partitions across five compartments (air, water, soil, sediment, groundwater). This layer computes fate from published physicochemical data and binds it to the open BAFU/UVEK background."
    },
    "footnote": {
     "de": "Quelle: lci-pesticide mapping_summary.json. 4-stufig: direkt (0,85) · Stoffklasse (0,75) · Kategorie (0,65) · 2 Zwischenprodukte offen.",
     "en": "Source: lci-pesticide mapping_summary.json. 4-tier: direct (0.85) · compound class (0.75) · category (0.65) · 2 intermediates unmapped."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 5,
      "suffix": {
       "de": " Kompartimente",
       "en": " compartments"
      },
      "label": {
       "de": "Luft · Boden · Oberflächenwasser · Grundwasser · Pflanze — pro Kilo ausgebrachtem Wirkstoff",
       "en": "Air · soil · surface water · groundwater · plant — per kilo of applied active ingredient"
      }
     },
     {
      "n": 13,
      "suffix": {
       "de": " Wirkstoffe",
       "en": " compounds"
      },
      "label": {
       "de": "verbleib-aufgelöst (8 direkt, 5 Klassen), 30 Biosphären-Flüsse an den offenen Katalog gebunden",
       "en": "fate-resolved (8 direct, 5 classes), 30 biosphere flows bound to the open catalogue"
      }
     },
     {
      "n": 9,
      "suffix": {
       "de": " Schritte",
       "en": " steps"
      },
      "label": {
       "de": "Verbleibs-Kaskade: Abdrift · Interzeption · Verflüchtigung · Auswaschung · Abschwemmung · Persistenz-Gewichtung",
       "en": "fate cascade: drift · interception · volatilisation · leaching · runoff · persistence weighting"
      }
     }
    ],
    "items": [
     {
      "de": "Jede Fraktion aus Stoffparametern rückrechenbar",
      "en": "Every fraction back-derivable from parameters"
     },
     {
      "de": "Katalog-gebunden: Hintergrund, Region, Methode tauschbar",
      "en": "Catalogue-bound: swap background, region, method"
     },
     {
      "de": "RER plus 15 Länder, 2010–2024, offene Nutzungsindizes",
      "en": "RER plus 15 countries, 2010–2024, open use indices"
     }
    ]
   }
  },
  "lci-phosphorus": {
   "kicker": {
    "de": "Phosphor-Verluste vom Feld ins Gewässer",
    "en": "Phosphorus losses from field to water"
   },
   "slide1": {
    "title": {
     "de": "Ein Pauschalfaktor wird zu vier physikalischen Verlustpfaden",
     "en": "One blanket factor becomes four physical loss pathways"
    },
    "body": {
     "de": "Hintergrund-Datenbanken setzen den Phosphor-Verlust eines Felds ins Gewässer auf null oder einen pauschalen Faktor pro Kultur, der auf keine Bewirtschaftung reagiert. Diese Tributary baut die SALCA-P-Formulierung zu einem Prozessmodell, das die Fracht in vier physikalische Pfade zerlegt und jeden einzeln ausweist.",
     "en": "Background databases set a field's phosphorus loss to water to zero or a flat per-crop factor that responds to no management. This tributary builds the SALCA-P formulation into a process model that splits the load into four physical pathways and reports each separately."
    },
    "footnote": {
     "de": "Beispiel CH-Weizen konventionell: 1'200 mm Niederschlag, 10 % Hang, Silt-Lehm, 30 kg P2O5/ha. Einheit kg PO4/ha·Jahr. Erosion trägt hier rund 95 %; je nach Standort verschiebt sich das Gewicht.",
     "en": "Example Swiss wheat, conventional: 1'200 mm rainfall, 10 % slope, silt loam, 30 kg P2O5/ha. Unit kg PO4/ha·year. Erosion carries about 95 % here; the weight shifts by site."
    },
    "renderer": "stacked-bar",
    "segments": [
     {
      "value": 70,
      "disp": {
       "de": "~70",
       "en": "~70"
      },
      "label": {
       "de": "Erosion (partikulärer P am Hang)",
       "en": "Erosion (particulate P on the slope)"
      },
      "color": "#1f6f43"
     },
     {
      "value": 3,
      "disp": {
       "de": "~3",
       "en": "~3"
      },
      "label": {
       "de": "Oberflächen-Abfluss (Dünger)",
       "en": "Surface runoff (fertiliser)"
      },
      "color": "#3a9b6e"
     },
     {
      "value": 0.2,
      "disp": {
       "de": "~0,2",
       "en": "~0.2"
      },
      "label": {
       "de": "Grundwasser-Versickerung",
       "en": "Groundwater percolation"
      },
      "color": "#7cc8a4"
     }
    ],
    "total": {
     "disp": {
      "de": "~73",
      "en": "~73"
     },
     "label": {
      "de": "kg PO4 / ha · Jahr",
      "en": "kg PO4 / ha · year"
     },
     "max": 80
    },
    "callout": {
     "de": "Vier Pfade — Erosion, Abfluss, Drainage, Grundwasser — einzeln berechnet und einzeln ausgewiesen.",
     "en": "Four pathways — erosion, runoff, drainage, groundwater — each computed and reported separately."
    }
   },
   "slide2": {
    "title": {
     "de": "Eine abfragbare Schicht statt eines starren Faktors",
     "en": "A queryable layer instead of a rigid factor"
    },
    "body": {
     "de": "Das Modell reagiert auf genau die Eingaben, die eine Ökobilanz ohnehin trägt: Hang, Boden, Dünger-Form, Bodenbearbeitung, Drainage-Klasse, Land. Kulturen, Länder und Bearbeitungs-Klassen liegen in versionierten Tabellen — eine neue Kultur ist eine Daten-Änderung, kein Code.",
     "en": "The model responds to exactly the inputs an LCA already carries: slope, soil, fertiliser form, tillage, drainage class, country. Crops, countries and tillage classes live in versioned tables — a new crop is a data edit, not code."
    },
    "footnote": {
     "de": "Nachschlage-Layer: 170 von 241 GADM-Ländern voll bestückt, 28 Kulturen plus Rückfall, 3 Bearbeitungs-Klassen. Spanne pro Kultur drei bis vier Grössenordnungen. 39 Tests bestanden, Vertrauensbereich 0,70 bis 0,85.",
     "en": "Lookup layer: 170 of 241 GADM countries fully populated, 28 crops plus fallback, 3 tillage classes. Per-crop spread three to four orders of magnitude. 39 tests passing, confidence range 0.70 to 0.85."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 4,
      "label": {
       "de": "physikalische Verlustpfade — einzeln berechnet, einzeln ausgewiesen",
       "en": "physical loss pathways — computed and reported one by one"
      }
     },
     {
      "n": 28,
      "label": {
       "de": "Kulturen mit eigenem Bedeckungsfaktor, über 170 Länder parametrisiert",
       "en": "crops with their own cover factor, parameterised across 170 countries"
      }
     }
    ],
    "items": [
     {
      "de": "Neue Kultur, neues Land oder neue Bearbeitung: eine Tabellen-Änderung, kein Code.",
      "en": "New crop, country or tillage: a table edit, not code."
     },
     {
      "de": "Fracht schwankt pro Kultur über drei bis vier Grössenordnungen.",
      "en": "Load varies three to four orders of magnitude per crop."
     },
     {
      "de": "Jeder Pfad hat eigene Treiber: Erosion–Hang, Abfluss–Dünger, Drainage–Boden.",
      "en": "Each pathway has its own drivers: erosion–slope, runoff–fertiliser, drainage–soil."
     }
    ]
   }
  },
  "lci-packaging": {
   "kicker": {
    "de": "VERPACKUNGS-SCHICHT",
    "en": "PACKAGING LAYER"
   },
   "slide1": {
    "title": {
     "de": "Die fehlende Verpackungs-Schicht jedes Produkts",
     "en": "The missing packaging layer of every product"
    },
    "body": {
     "de": "Die BAFU/UVEK-Referenz liefert Rohstoffe, kaum fertige Lebensmittel-Verpackungen. Eine achtstufige Pipeline leitet Material, Gewicht und Entsorgung je Produkt ab - vom Namen zur vollen Bilanz statt eines Pauschalwerts.",
     "en": "The BAFU/UVEK reference provides raw materials but almost no finished food packaging. An eight-step pipeline derives material, weight and end-of-life per product - from name to full inventory instead of a flat assumption."
    },
    "footnote": {
     "de": "104 Eintraege (51 Verpackung + 53 Baustoff); Vertrauen 0,50-0,95. 2'418 von 2'458 Produkten klassifiziert (98,4 %). 255 Tests.",
     "en": "104 entries (51 packaging + 53 construction); confidence 0.50-0.95. 2'418 of 2'458 products classified (98.4%). 255 tests."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 104,
      "label": {
       "de": "statische Eintraege fuellen den BAFU/UVEK-Hintergrund",
       "en": "static entries fill the BAFU/UVEK background"
      }
     },
     {
      "n": 8,
      "suffix": {
       "de": "-stufig",
       "en": "-step"
      },
      "label": {
       "de": "Pipeline je benanntem Lebensmittel",
       "en": "pipeline per named food"
      }
     }
    ],
    "items": [
     {
      "de": "Material, Behälter, Gewicht, Lebensende aus Name und Nährwerten",
      "en": "material, container, weight, end-of-life from name and nutrients"
     },
     {
      "de": "jede Zelle traegt Auflösungs-Pfad und Vertrauenswert",
      "en": "every cell carries resolution path and confidence score"
     },
     {
      "de": "Material-/Entsorgungsflüsse spaet gebunden - DB und Land tauschbar",
      "en": "material/end-of-life flows bound late - database and country swappable"
     },
     {
      "de": "garantierter Rueckfall: jedes Produkt erhaelt eine Bilanz",
      "en": "guaranteed fallback: every product receives an inventory"
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Zwei Achsen, die ein Pauschalfaktor verschluckt",
     "en": "Two axes a flat factor swallows"
    },
    "body": {
     "de": "Ein Pauschalfaktor gibt jedem Produkt gleich viel Verpackung. Real unterscheiden sich die Mengen je Behälter um über eine Grössenordnung - 17,9 g/kg (Trockenfruchtschale) bis 358,5 g/kg (Konfitueren-Glas). Dieselbe Kunststoff-Verpackung: CH null Deponie, global rund 55 %.",
     "en": "A flat factor gives every product the same packaging. Real amounts differ by over an order of magnitude per container - 17.9 g/kg (dried-fruit tray) to 358.5 g/kg (jam jar). Same plastic package: CH zero landfill, global around 55%."
    },
    "footnote": {
     "de": "Verpackungs-Gewicht je kg aus dem 28-Produkt-Audit (2022). Entsorgung: BAFU (CH), Eurostat (EU), global. An BAFU/UVEK gebunden.",
     "en": "Packaging weight per kg from the 28-product audit (2022). End-of-life: FOEN (CH), Eurostat (EU), global. Bound to BAFU/UVEK activities."
    },
    "renderer": "stacked-bar",
    "segments": [
     {
      "value": 17.9,
      "disp": {
       "de": "17,9 g/kg",
       "en": "17.9 g/kg"
      },
      "label": {
       "de": "Trockenfrucht-Schale (PET)",
       "en": "dried-fruit tray (PET)"
      },
      "color": "#7fb069"
     },
     {
      "value": 55,
      "disp": {
       "de": "55 g/kg",
       "en": "55 g/kg"
      },
      "label": {
       "de": "UHT-Milch (HDPE)",
       "en": "UHT milk (HDPE)"
      },
      "color": "#4a90b8"
     },
     {
      "value": 100.5,
      "disp": {
       "de": "100,5 g/kg",
       "en": "100.5 g/kg"
      },
      "label": {
       "de": "Joghurt-Becher",
       "en": "yoghurt cup"
      },
      "color": "#e0a458"
     },
     {
      "value": 358.5,
      "disp": {
       "de": "358,5 g/kg",
       "en": "358.5 g/kg"
      },
      "label": {
       "de": "Konfitueren-Glas",
       "en": "jam jar"
      },
      "color": "#c0584b"
     }
    ],
    "total": {
     "disp": {
      "de": "Faktor 20 von leichtester zu schwerster Verpackung",
      "en": "factor 20 from lightest to heaviest packaging"
     },
     "label": {
      "de": "Verpackung je kg Produkt - vier Behälter",
      "en": "packaging per kg product - four containers"
     },
     "max": 540
    },
    "callout": {
     "de": "Zwei Achsen: die Menge spreizt um Faktor 20 (17,9–358,5 g/kg), das Land bestimmt das Lebensende — CH null Deponie, global rund 55 %. Ein Pauschalfaktor blendet beide aus.",
     "en": "Two axes: the amount spreads by a factor of 20 (17.9–358.5 g/kg), the country sets the end-of-life — CH zero landfill, global about 55%. A flat factor hides both."
    }
   }
  },
  "lci-transport": {
   "kicker": {
    "de": "Transport-Inventare",
    "en": "Transport inventories"
   },
   "slide1": {
    "title": {
     "de": "Statt einem Durchschnitts-Lastwagen: Transport, aufgelöst",
     "en": "Instead of one average lorry: transport, resolved"
    },
    "body": {
     "de": "Die BAFU/UVEK-Referenz kennt Transport nur als flache Flotten-Durchschnitte – ohne EURO-Klassen, Gewichtsbänder oder Kühlbetrieb. Diese Schicht komponiert 73 Transport-Inventare aus offener Primärliteratur je Tonnenkilometer, aufgelöst nach Verkehrsmittel, EURO-Klasse, Gewicht, Kühlung, Treibstoff, Land und Jahr.",
     "en": "The BAFU/UVEK reference knows transport only as flat fleet averages – no EURO classes, weight bands or refrigeration. This layer composes 73 transport inventories from open primary literature, each per tonne-kilometre, resolved by mode, EURO class, weight, refrigeration, fuel, country and year."
    },
    "footnote": {
     "de": "Quellen: EMEP/EEA Guidebook 2023 (Tier 2); IMO Fourth GHG Study 2020; Tassou et al. 2009; IPCC 2006. 7 Verkehrsmittel; Flottenmix CH, DE, FR, IT, ES, PL, EU27, RER; 2020.",
     "en": "Sources: EMEP/EEA Guidebook 2023 (Tier 2); IMO Fourth GHG Study 2020; Tassou et al. 2009; IPCC 2006. 7 modes; fleet mix CH, DE, FR, IT, ES, PL, EU27, RER; year 2020."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 73,
      "label": {
       "de": "komponierte Transport-Inventare, je an eine benannte BAFU-Aktivität gebunden",
       "en": "composed transport inventories, each bound to a named BAFU activity"
      }
     },
     {
      "n": 7,
      "label": {
       "de": "Verkehrsmittel – Strasse, Kühl, See, Bahn, Traktor, Personen, Helikopter",
       "en": "modes – road, refrigerated, sea, rail, tractor, passenger, helicopter"
      }
     },
     {
      "n": 8,
      "label": {
       "de": "Länder-Flottenmixe (CH, DE, FR, IT, ES, PL, EU27, RER), Jahre 2005–2025",
       "en": "country fleet mixes (CH, DE, FR, IT, ES, PL, EU27, RER), years 2005–2025"
      }
     }
    ],
    "items": [
     {
      "de": "Aufgelöst nach EURO-Klasse, Gewichtsband, Kühlbetrieb, Treibstoff",
      "en": "Resolved by EURO class, weight band, cooling mode and fuel"
     },
     {
      "de": "Jede Zelle aus offener Literatur, an BAFU gebunden",
      "en": "Each cell from open literature, bound to BAFU at the emission step"
     },
     {
      "de": "63 von 73 Einträgen literaturbasiert; Konfidenz 0,75 (0,40–0,90)",
      "en": "63 of 73 entries literature-sourced; confidence 0.75 (0.40–0.90)"
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Warum die Auflösung zählt: derselbe Tonnenkilometer, Faktor 78",
     "en": "Why resolution matters: the same tonne-kilometre, a factor of 78"
    },
    "body": {
     "de": "Ein Tonnenkilometer = eine Tonne Ware, einen Kilometer bewegt. Was sie an CO₂ verursacht, hängt fast nur vom Verkehrsmittel und seiner Auslastung ab: Vom Hochsee-Tanker bis zum Kühl-Lastwagen spannt diese Schicht denselben Tonnenkilometer über zwei Grössenordnungen auf – die Spreizung, die ein Durchschnitt verschluckt.",
     "en": "One tonne-kilometre = one tonne of goods moved one kilometre. What it emits depends almost entirely on the mode and its utilisation: from an ocean tanker to a small refrigerated lorry, this layer spreads the same tonne-kilometre across two orders of magnitude – the spread an average swallows."
    },
    "footnote": {
     "de": "Quellen: EMEP/EEA Guidebook 2023; IMO Fourth GHG Study 2020, Tab. 34; GLEC Framework v3. kg CO₂-Äq. je Tonnenkilometer; Containerschiff 0,0105 (kein Reefer); Faktor 78.",
     "en": "Sources: EMEP/EEA Guidebook 2023; IMO Fourth GHG Study 2020, Table 34; GLEC Framework v3. kg CO₂-eq per tonne-kilometre; container ship 0.0105 (non-reefer); factor 78."
    },
    "bars": [
     {
      "label": {
       "de": "Hochsee-Tanker",
       "en": "ocean tanker"
      },
      "value": 0.0046,
      "disp": {
       "de": "0,0046",
       "en": "0.0046"
      },
      "color": "#1f6f78"
     },
     {
      "label": {
       "de": "Containerschiff",
       "en": "container ship"
      },
      "value": 0.0105,
      "disp": {
       "de": "0,0105",
       "en": "0.0105"
      },
      "color": "#1f6f78"
     },
     {
      "label": {
       "de": "Bahn (Diesel)",
       "en": "rail (diesel)"
      },
      "value": 0.03,
      "disp": {
       "de": "0,030",
       "en": "0.030"
      },
      "color": "#3a8d5b"
     },
     {
      "label": {
       "de": "Lastwagen >32 t, EURO V",
       "en": "lorry >32 t, EURO V"
      },
      "value": 0.0642,
      "disp": {
       "de": "0,064",
       "en": "0.064"
      },
      "color": "#c98a2b"
     },
     {
      "label": {
       "de": "Kühl-Lastwagen 7,5–16 t, EURO V",
       "en": "refrigerated lorry 7.5–16 t, EURO V"
      },
      "value": 0.2004,
      "disp": {
       "de": "0,200",
       "en": "0.200"
      },
      "color": "#c2562f"
     },
     {
      "label": {
       "de": "kleiner Kühl-Lastwagen, EURO III",
       "en": "small refrigerated lorry, EURO III"
      },
      "value": 0.823,
      "disp": {
       "de": "0,823",
       "en": "0.823"
      },
      "color": "#a11d33"
     }
    ]
   }
  },
  "lci-metals": {
   "kicker": {
    "de": "Spezialmetalle",
    "en": "Specialty metals"
   },
   "slide1": {
    "title": {
     "de": "Metalle, die der Referenzkatalog gar nicht kennt",
     "en": "Metals the reference catalogue simply has no entry for"
    },
    "body": {
     "de": "Der BAFU/UVEK-Katalog kennt für Spezialmetalle keine Wiege-bis-Werktor-Bilanz; die generische Brücke greift zu falschen Aktivitäten (Ferrochrom statt Ferrosilizium). Dieser Zufluss baut jedes Metall prozessbasiert aus offener Literatur neu auf.",
     "en": "For specialty metals the BAFU/UVEK catalogue has no cradle-to-gate inventory; the generic bridge falls back on wrong activities (ferrochromium for ferrosilicon). This tributary rebuilds each metal as a process-based inventory from open literature."
    },
    "footnote": {
     "de": "Funktionelle Einheit: 1 kg veredeltes Metall am Werktor. Bänder: Aluminium 6,3-7,5; V2O5 68,4 (40-75). Vertrauen 0,82 bzw. 0,78.",
     "en": "Functional unit: 1 kg refined metal at plant gate. Bands: aluminium 6.3-7.5; V2O5 68.4 (40-75). Confidence 0.82 and 0.78."
    },
    "bars": [
     {
      "label": {
       "de": "Primaraluminium (Europa) - in jeder Getrankedose",
       "en": "Primary aluminium (Europe) - in every beverage can"
      },
      "value": 6.55,
      "disp": {
       "de": "6,55",
       "en": "6.55"
      },
      "color": "#4F8FC0"
     },
     {
      "label": {
       "de": "Vanadiumpentoxid (FR) - trifft Referenz 68,4 auf 0,7%",
       "en": "Vanadium pentoxide (FR) - hits 68.4 reference within 0.7%"
      },
      "value": 67.92,
      "disp": {
       "de": "67,92",
       "en": "67.92"
      },
      "color": "#7A5BA6"
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Eine Bilanz, jedes Netz - ohne Neuherleitung",
     "en": "One inventory, any grid - without re-derivation"
    },
    "body": {
     "de": "Jedes Metall ist eine methodenagnostische Bilanz, die physikalische Flüsse von der Katalog-Anbindung trennt - Anwender hängen den Strom auf jedes Netz um, ohne Neuherleitung. Primaraluminium liegt am EU-Netz bei 6,55, am China-Mix bei 18,46 kg CO2eq/kg.",
     "en": "Each metal is a method-agnostic inventory separating physical flows from the catalogue binding - consumers re-point electricity to any grid, without re-derivation. Primary aluminium lands at 6.55 on the EU grid and 18.46 kg CO2eq/kg on the China mix."
    },
    "footnote": {
     "de": "Aus results/metals_to_bafu_mapping.json. China-Mix 18,46 ist konservative Untergrenze im Band 16-20. Funktionelle Einheit: 1 kg Primaraluminium-Barren am Werktor.",
     "en": "From results/metals_to_bafu_mapping.json. China mix 18.46 is a conservative lower bound in the 16-20 band. Functional unit: 1 kg primary aluminium ingot at plant gate."
    },
    "renderer": "wet-dry-bars",
    "wet": {
     "value": 18.46,
     "disp": {
      "de": "18,46",
      "en": "18.46"
     },
     "label": {
      "de": "China-Mix (kohledominiert) - dasselbe Metall, anderes Netz",
      "en": "China mix (coal-dominant) - same metal, different grid"
     }
    },
    "dry": {
     "value": 6.55,
     "disp": {
      "de": "6,55",
      "en": "6.55"
     },
     "label": {
      "de": "Europa-Netz - hoher Wasserkraftanteil",
      "en": "European grid - high hydropower share"
     }
    },
    "barMax": 20,
    "ghostValue": 8.9,
    "ghostLabel": {
     "de": "alte generische Brucke (Welt auf Europa-Netz kollabiert)",
     "en": "old generic bridge (world collapsed onto European grid)"
    },
    "ratio": {
     "de": "rund 3x",
     "en": "about 3x"
    },
    "callout": {
     "de": "Strom am Schmelzofen ist der grosste Hebel auf die Aluminium-Bilanz. Weil die physikalischen Flusse von der Netz-Anbindung getrennt sind, hangt der Anwender denselben Barren von Europa (6,55) auf den China-Mix (18,46) um, ohne eine einzige andere Zahl neu herzuleiten. Die alte generische Brucke konnte das nicht - sie kollabierte das Welt-Aluminium auf das europaische Netz (rund 8,9 kg) und verfehlte die Realitat um mehr als das Doppelte.",
     "en": "Smelter electricity is the largest lever on the aluminium footprint. Because the physical flows are separated from the grid binding, a consumer re-points the same ingot from Europe (6.55) to the China mix (18.46) without re-deriving a single other number. The old generic bridge could not do this - it collapsed world aluminium onto the European grid (about 8.9 kg) and missed reality by more than two-fold."
    }
   }
  },
  "lci-textile-processing": {
   "kicker": {
    "de": "Textilverarbeitung",
    "en": "Textile processing"
   },
   "slide1": {
    "title": {
     "de": "Die fehlende Textil-Verarbeitungsstufe im Katalog",
     "en": "The textile-processing step the catalogue is missing"
    },
    "body": {
     "de": "Der BAFU/UVEK-Katalog kennt kein Verfahren, das synthetische Fasern zu Garn, Gewebe und Seil verarbeitet — eine Stufe in jedem Lebensmittel mit synthetischer Cordage. Diese Tributäre füllt sie: ein offenes, strom-verankertes Modell für den reinen Umwandlungs-Dienst.",
     "en": "The BAFU/UVEK catalogue has no process converting synthetic fibre into yarn, fabric and rope — a step inside every food product with synthetic cordage. This tributary fills it: an open, electricity-anchored model for the conversion service alone."
    },
    "footnote": {
     "de": "Funktionseinheit: 1 kg Faser-Verarbeitungsdienst. Energie-Intensitäten: van der Velden et al. 2014.",
     "en": "Functional unit: 1 kg fibre conversion service. Energy intensities: van der Velden et al. 2014."
    },
    "bullets": [
     {
      "de": "Schliesst echte Lücke: kein BAFU-Verfahren fürs Weben/Verseilen",
      "en": "Closes real gap: no BAFU process for weaving/twisting"
     },
     {
      "de": "Nur Verarbeitung — Polymer (Nylon, PET, PP) bleibt eigener Exchange",
      "en": "Conversion only — polymer (nylon, PET, PP) stays own exchange"
     },
     {
      "de": "Strom-verankert an realem BAFU-Prozess plus Wärme-Rest",
      "en": "Electricity-anchored to real BAFU process plus heat residual"
     },
     {
      "de": "Offene Literatur, p5/p95-Band, versionssicher (Sediment v2)",
      "en": "Open literature, p5/p95 band, version-safe (sediment v2)"
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Wie der Verarbeitungs-Dienst sauber entsteht",
     "en": "How the conversion service is built, cleanly"
    },
    "body": {
     "de": "1 kg Verarbeitungs-Dienst wird additiv aus zwei Energie-Termen gebaut: Strom an einem BAFU-Prozess verankert plus kleine Wärme-Restkorrektur. FR-Strom: 0,44 kg CO₂eq/kg (Band 0,31–0,82). Das Polymer bleibt separat, diese Stufe liegt stets additiv darüber.",
     "en": "1 kg of conversion service is built additively from two energy terms: electricity anchored to a BAFU process plus a small heat residual. FR grid: 0.44 kg CO₂eq/kg (band 0.31–0.82). The polymer stays separate, so this step is always additive on top."
    },
    "footnote": {
     "de": "Strom-Anker BAFU 559769 (0,068425 kg CO₂eq/kWh); Wärme-Rest BAFU 252893 (0,0676 kg CO₂eq/MJ). PP-Seil: 2,10 + 0,44 = 2,54 kg CO₂eq/kg.",
     "en": "Electricity anchor BAFU 559769 (0.068425 kg CO₂eq/kWh); heat residual BAFU 252893 (0.0676 kg CO₂eq/MJ). PP-rope: 2.10 + 0.44 = 2.54 kg CO₂eq/kg."
    },
    "renderer": "stacked-bar",
    "segments": [
     {
      "value": 0.376,
      "disp": {
       "de": "0,38",
       "en": "0.38"
      },
      "label": {
       "de": "Strom-Anker (5,5 kWh/kg)",
       "en": "Electricity anchor (5.5 kWh/kg)"
      },
      "color": "#2563eb"
     },
     {
      "value": 0.068,
      "disp": {
       "de": "0,07",
       "en": "0.07"
      },
      "label": {
       "de": "Wärme-Rest, Fixieren (1,0 MJ/kg)",
       "en": "Heat residual, setting (1.0 MJ/kg)"
      },
      "color": "#f59e0b"
     }
    ],
    "total": {
     "disp": {
      "de": "0,44",
      "en": "0.44"
     },
     "label": {
      "de": "kg CO₂eq je kg Verarbeitungs-Dienst (FR-Strom)",
      "en": "kg CO₂eq per kg conversion service (FR grid)"
     },
     "max": 0.5
    },
    "callout": {
     "de": "Additiv über dem Polymer, nie eingemischt: PP-Seil = 2,10 (Polymer) + 0,44 (Verarbeitung) = 2,54 kg CO₂eq/kg.",
     "en": "Additive over the polymer, never blended in: PP rope = 2.10 (polymer) + 0.44 (conversion) = 2.54 kg CO₂eq/kg."
    }
   }
  },
  "lci-allocation": {
   "kicker": {
    "de": "Allokation als umschaltbarer Regler",
    "en": "Allocation as a switchable knob"
   },
   "slide1": {
    "title": {
     "de": "Eingefrorene Allokation — jetzt umschaltbar",
     "en": "Frozen allocation — now switchable"
    },
    "body": {
     "de": "Liefert ein Prozess mehrere Koppelprodukte (Ölsaat-Pressung, Zuckerraffination, Milchtrennung, Schlachtung, Fischverarbeitung), backt die Referenz-Datenbank genau eine Lastaufteilung fest ein. Diese Schicht macht die Allokation umschaltbar — ökonomisch, nach Masse oder Energie.",
     "en": "When a process yields several co-products (oilseed crushing, sugar refining, dairy separation, slaughter, fish processing), the reference database bakes in exactly one split of the burden. This layer makes allocation switchable — economic, by mass or by energy."
    },
    "footnote": {
     "de": "Quelle: lci-allocation README; data/commodity_params (17 Dateien: 13 Mehrprodukt-Operationen plus 4 Saft/Kaltpress-Sensitivität); Basisjahr 2023.",
     "en": "Source: lci-allocation README; data/commodity_params (17 files: 13 multi-output operations plus 4 juice/cold-press sensitivity); baseline year 2023."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 1,
      "suffix": {
       "de": " → 3",
       "en": " → 3"
      },
      "label": {
       "de": "eingefrorene Allokation der Hintergrund-Datenbank wird zu drei umschaltbaren Methoden: wirtschaftlich, Masse, Energie",
       "en": "one frozen background allocation becomes three switchable methods: economic, mass, energy"
      }
     },
     {
      "n": 13,
      "label": {
       "de": "Mehrprodukt-Operationen über Ölsaat, Getreide, Zucker, Milch, Schlachtung, Geflügel und Fisch",
       "en": "multi-output operations across oilseed, grain, sugar, dairy, slaughter, poultry and fish"
      }
     },
     {
      "n": 0,
      "label": {
       "de": "neu geschriebene Hintergrund-Aktivitäten: die Korrektur ist ein dimensionsloser Multiplikator obendrauf",
       "en": "background activities re-authored: the correction is a dimensionless multiplier on top"
      }
     }
    ],
    "items": [
     {
      "de": "Massenanteil, Energiegehalt und Preis jedes Koppelprodukts offen in JSON — eine Gleichung pro Methode",
      "en": "Each co-product's mass, energy and price openly inspectable in JSON — one equation per method"
     },
     {
      "de": "Default-Build ist leer per Konstruktion: Korrekturen feuern nur bei Abweichung von der eingefrorenen Basis",
      "en": "Default build is empty by construction: corrections fire only when diverging from the frozen baseline"
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Eine Mapping-Datei deckt jede Methode, Region und Jahr ab — mit nachvollziehbarer Preisherkunft",
     "en": "One mapping covers every method, region and year — with traceable price provenance"
    },
    "body": {
     "de": "Der Hebel ist die Reichweite: dieselbe finale Mapping-Datei bedient ökonomische, Massen- und Energie-Allokation, jede Region (8 Aggregate: RER, GLO, RoW, RAF, RAS, RLA, RNA, RME) und jedes Jahr (2000–2024) — über einen Build-Schalter statt Duplikate pro Methode × Jahr × Region. Bei regionaler Bepreisung läuft jeder Preis durch eine 7-stufige Fallback-Kette (exaktes Land-Jahr → nächstes Jahr → Regions-Mittel → Welt-Mittel → Eltern-Proxy → Pink-Sheet-Index → Default) mit prüfbarer Herkunftsstufe. So wird Methoden-Sensitivität zur erstklassigen Ausgabe — Rohpalmöl trägt rund vier Fünftel des Wert-, aber nur ein Drittel des Massenanteils; Fischfilet fällt von 94 % auf 47 %.",
     "en": "The lever is reach: the same final mapping serves economic, mass and energy allocation, any region (8 aggregates: RER, GLO, RoW, RAF, RAS, RLA, RNA, RME) and any year (2000–2024) — via a build switch rather than duplicating activities per method × year × region. Under regional pricing every price flows through a 7-tier fallback chain (exact country-year → nearest year → regional average → world average → parent proxy → Pink Sheet index → default), each carrying an auditable provenance tier. This makes method sensitivity a first-class output — crude palm oil carries roughly four fifths of the economic but only a third of the mass share; fish fillet drops from 94% to 47%."
    },
    "footnote": {
     "de": "Quelle: lci-allocation README (Regional price resolution, 7-Tier-Kette; Results) und CLAUDE.md; FAOSTAT-Produzentenpreise, Weltbank Pink Sheet, SNB-Jahresmittel; Basisjahr 2023; 206 Tests.",
     "en": "Source: lci-allocation README (Regional price resolution, 7-tier chain; Results) and CLAUDE.md; FAOSTAT producer prices, World Bank Pink Sheet, SNB annual averages; baseline year 2023; 206 tests."
    },
    "stats": [
     {
      "num": {
       "de": "3 × 8 × 25",
       "en": "3 × 8 × 25"
      },
      "label": {
       "de": "Methoden × Regionen × Jahre aus einer einzigen Mapping-Datei statt aus duplizierten Aktivitäten",
       "en": "methods × regions × years from one single mapping instead of duplicated activities"
      }
     },
     {
      "num": {
       "de": "7",
       "en": "7"
      },
      "label": {
       "de": "Fallback-Stufen der Preisauflösung — jeder Preis trägt eine prüfbare Herkunftsstufe",
       "en": "price-resolution fallback tiers — every price carries an auditable provenance tier"
      }
     },
     {
      "num": {
       "de": "94 % → 47 %",
       "en": "94% → 47%"
      },
      "label": {
       "de": "Fischfilet-Anteil von Wert- auf Massen-Allokation: Methodenwahl als erstklassige Sensitivität",
       "en": "fish fillet share from economic to mass allocation: method choice as first-class sensitivity"
      }
     }
    ]
   }
  },
  "lci-biodiversity": {
   "kicker": {
    "de": "Biodiversität",
    "en": "Biodiversity"
   },
   "slide1": {
    "title": {
     "de": "Die fehlende Wirkungsachse",
     "en": "The missing impact axis"
    },
    "body": {
     "de": "Die Referenz-Datenbank trägt Klima, Eutrophierung und Toxizität — aber kein Biodiversitäts-Signal. So erhält jede Kultur in jedem Land denselben Wert, und regionale Vergleiche brechen zusammen. Dieser Tributary fügt die Achse hinzu: Er übersetzt die peer-reviewte Chaudhary-und-Brooks-Charakterisierung in den Tributary-Vertrag, damit Landnutzungs-Flüsse in einen regionalisierten Artenverlust-Score (PDF) werden.",
     "en": "The reference database carries climate, eutrophication and toxicity — but no biodiversity signal. So every crop in every country scores the same, and regional comparisons collapse. This tributary adds the axis: it ports the peer-reviewed Chaudhary-and-Brooks characterisation into the tributary contract, turning land-use flows into a regionalised species-loss score (PDF)."
    },
    "footnote": {
     "de": "Quelle: Chaudhary und Brooks 2018 (peer-reviewt). Charakterisierungs-Schicht, kein Inventar (bafu_key: null, keine Biosphären-Flüsse). Einheit PDF·m²-Jahr.",
     "en": "Source: Chaudhary and Brooks 2018 (peer-reviewed). Characterisation layer, not an inventory (bafu_key: null, no biosphere exchanges). Unit PDF·m²-year."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 243,
      "label": {
       "de": "Länder abgedeckt (plus 805 WWF-Ökoregionen mit 95-Prozent-Konfidenzintervallen)",
       "en": "countries covered (plus 805 WWF ecoregions with 95 percent confidence intervals)"
      }
     },
     {
      "n": 6,
      "label": {
       "de": "Landnutzungs-Typen, je 3 Intensitätsstufen",
       "en": "land-use types, each with 3 intensity levels"
      }
     },
     {
      "n": 2,
      "label": {
       "de": "getrennte Wirkungspfade: laufende Belegung (m²-Jahr) und einmalige Waldumwandlung (m²)",
       "en": "separate impact pathways: ongoing occupation (m²-year) and one-off forest transformation (m²)"
      }
     }
    ],
    "items": [
     {
      "de": "Dreistufige Auflösung: Ökoregion → Land → Welt-Mittel, auditierbar markiert",
      "en": "Three-step resolution: ecoregion → country → world, auditably marked"
     },
     {
      "de": "Schliesst die eine Wirkungskategorie, die der Katalog bisher nicht führte",
      "en": "Closes the one impact category the catalogue did not yet carry"
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Region statt globalem Mittel",
     "en": "Region instead of a global average"
    },
    "body": {
     "de": "Der eigentliche Wert ist die räumliche Auflösung: Über 228 Länder spannt der Acker-Faktor 5,8 Grössenordnungen (rund 621'000×). Ein globaler Multiplikator würde diese Spanne wegmitteln — und das Signal verbergen, dass tropische Ökoregionen den Verlust gefährdeter Arten dominieren. Die Schicht hält die Auflösung end-to-end durch und trennt Belegung sauber von Umwandlung.",
     "en": "The real value is spatial resolution: across 228 countries the cropland factor spans 5.8 orders of magnitude (about 621'000x). A single global multiplier would average that spread away — and hide the signal that tropical ecoregions dominate vulnerable-species loss. The layer preserves the resolution end-to-end, keeping occupation and transformation cleanly apart."
    },
    "footnote": {
     "de": "Quelle: Chaudhary und Brooks 2018; Ackerland-Belegung, mittlere Intensität; relativ zur Schweiz (6,0·10⁻¹⁴ PDF·m²-Jahr/m²-Jahr). 33 Validierungs-Tests.",
     "en": "Source: Chaudhary and Brooks 2018; cropland occupation, medium intensity; relative to Switzerland (6.0·10⁻¹⁴ PDF·m²-year/m²-year). 33 validation tests."
    },
    "bars": [
     {
      "label": {
       "de": "Schweiz",
       "en": "Switzerland"
      },
      "value": 1,
      "disp": {
       "de": "1×",
       "en": "1x"
      },
      "color": "#16a34a"
     },
     {
      "label": {
       "de": "Brasilien",
       "en": "Brazil"
      },
      "value": 4,
      "disp": {
       "de": "4×",
       "en": "4x"
      },
      "color": "#8BC34A"
     },
     {
      "label": {
       "de": "Indonesien",
       "en": "Indonesia"
      },
      "value": 16,
      "disp": {
       "de": "16×",
       "en": "16x"
      },
      "color": "#FFC107"
     },
     {
      "label": {
       "de": "Madagaskar",
       "en": "Madagascar"
      },
      "value": 26,
      "disp": {
       "de": "26×",
       "en": "26x"
      },
      "color": "#FF9800"
     },
     {
      "label": {
       "de": "Philippinen",
       "en": "Philippines"
      },
      "value": 36,
      "disp": {
       "de": "36×",
       "en": "36x"
      },
      "color": "#F57C00"
     },
     {
      "label": {
       "de": "Sri Lanka",
       "en": "Sri Lanka"
      },
      "value": 40,
      "disp": {
       "de": "40×",
       "en": "40x"
      },
      "color": "#E65100"
     }
    ]
   }
  },
  "lci-ipcc-tier1-agriculture": {
   "kicker": {
    "de": "IPCC-TIER-1-LANDWIRTSCHAFT",
    "en": "IPCC TIER 1 AGRICULTURE"
   },
   "slide1": {
    "title": {
     "de": "Der Standard, den jedes Land berichtet – endlich abrufbar",
     "en": "The standard every country reports – finally retrievable"
    },
    "body": {
     "de": "Jedes Land berichtet seine direkten Hof-Emissionen nach IPCC Tier 1. Doch die Methode liegt nur als Gleichungen in Kapitel-PDFs vor; Referenz-Datenbanken verdichten sie zu einer einzigen Regionalzahl. Dieser Baustein baut sie nach: neun Teilmodelle, 18 Gleichungen, jedes kg rückverfolgbar bis zu Kapitel und Gleichung.",
     "en": "Every country reports its direct on-farm emissions under IPCC Tier 1. Yet the method exists only as equations in chapter PDFs, and reference databases collapse it into one opaque regional number. This layer rebuilds it: nine sub-models, 18 equations, every kilogram traceable to its chapter and equation."
    },
    "footnote": {
     "de": "IPCC-Richtlinien 2006/2019, Band 4, Kapitel 2, 5, 10, 11 + Feuchtgebiete-Ergänzung 2013.",
     "en": "IPCC 2006/2019 Guidelines, Volume 4, Chapters 2, 5, 10, 11 + 2013 Wetlands Supplement."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 9,
      "label": {
       "de": "Teilmodelle – je eine Hof-Emissionsquelle, eigenes Parameterfile",
       "en": "sub-models – one per on-farm source, each with its own parameter file"
      }
     },
     {
      "n": 18,
      "label": {
       "de": "IPCC-Gleichungen, jede an ihr Quellkapitel zitiert",
       "en": "IPCC equations, each cited to its source chapter"
      }
     },
     {
      "n": 6,
      "label": {
       "de": "abgedeckte Biosphären-Flüsse: N₂O, CH₄, CO₂ (fossil + Landumwandlung), NH₃, NO₃",
       "en": "biosphere flows covered: N₂O, CH₄, CO₂ (fossil + land transformation), NH₃, NO₃"
      }
     }
    ],
    "items": [
     {
      "de": "Jedes kg N₂O, CH₄, CO₂ bis Kapitel und Gleichung rückverfolgbar.",
      "en": "Every kg of N₂O, CH₄ or CO₂ traceable to chapter and equation."
     },
     {
      "de": "Deckt Pfade ohne Detailmodell: Harnstoff/Kalk-CO₂, organische Böden.",
      "en": "Covers pathways no detailed model owns: urea/lime CO₂, organic soils."
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Eine Methode, zwei Aufgaben: Auffanglinie und Eichmass",
     "en": "One method, two jobs: fallback line and yardstick"
    },
    "body": {
     "de": "Tier 1 ist die globale Vorgabe, gegen die nationale Inventare berichten. Darum leistet der Baustein zweierlei: Auffanglinie für jede Kultur und jedes Tier ohne Detailmodell – und Eichmass für die vier Detailmodelle. Jeder der 1'742 Default-Werte ist dreifach abgeschrieben und durch zwei Prüfläufe gesichert.",
     "en": "Tier 1 is the global default national inventories report against. So the layer does two jobs: a fallback for every crop and animal without a detailed model – and an independent yardstick for the four detailed models. Each of the 1'742 default values is transcribed three times and pinned by two regression suites."
    },
    "footnote": {
     "de": "Detailmodell-Geschwister: Feld-Lachgas, Boden-Kohlenstoff (×2), Vieh, Reis; Querprüfung Zeile für Zeile statt Mittelung.",
     "en": "Tier 2 sibling models: field nitrous oxide, soil carbon (×2), livestock, rice; cross-checked row by row, not averaged."
    },
    "stats": [
     {
      "num": {
       "de": "1'742",
       "en": "1'742"
      },
      "label": {
       "de": "verifizierte Default-Werte – jeder dreifach unabhängig abgeschrieben, durch zwei Prüfläufe gesichert",
       "en": "verified default values – each transcribed three ways, pinned by two regression suites"
      }
     },
     {
      "num": {
       "de": "4",
       "en": "4"
      },
      "label": {
       "de": "mechanistische Detailmodelle, die gegen diese gemeinsame Basislinie geprüft werden",
       "en": "mechanistic detailed models checked against this common baseline"
      }
     },
     {
      "num": {
       "de": "5 / 9",
       "en": "5 / 9"
      },
      "label": {
       "de": "Klimazonen und Weltregionen, über den ISO-3166-Ländercode aufgelöst – die Vorgabe, gegen die Länder berichten",
       "en": "climate zones and world regions, resolved via the ISO 3166 country code – the default countries report against"
      }
     }
    ]
   }
  },
  "lci-luc": {
   "kicker": {
    "de": "Landnutzungsänderung",
    "en": "Land-use change"
   },
   "slide1": {
    "title": {
     "de": "Der Posten, den die Referenz-Datenbank weglässt",
     "en": "The term the reference database leaves out"
    },
    "body": {
     "de": "Hintergrundkataloge bilanzieren Energie, Dünger und Maschinen bis zum Hoftor – nicht aber den einmaligen CO₂-Stoss aus Rodung von Wald, Moor oder Savanne für dieses Produkt. Ein Welt-Durchschnitt hilft nicht: derselbe nationale Schnitt verbirgt Herkünfte zwei Grössenordnungen auseinander. Diese Tributary liefert den Posten – pro Rohstoff, Land und Region.",
     "en": "Background catalogues account for energy, fertiliser and machinery up to the farm gate — but not the one-off CO₂ pulse from clearing forest, peat or savannah for that product. A flat global average fails: one national figure hides origins two orders of magnitude apart. This tributary supplies the missing term — per commodity, country and region."
    },
    "footnote": {
     "de": "Quelle: results/luc_factors.json – Rindfleisch Brasilien, kg CO₂eq/kg, beides brasilianische Bundesstaaten unter einem nationalen Schnitt von 50,5.",
     "en": "Source: results/luc_factors.json — beef Brazil, kg CO₂eq/kg, both Brazilian states under one national average of 50.5."
    },
    "renderer": "wet-dry-bars",
    "wet": {
     "value": 84.95,
     "disp": {
      "de": "85,0",
      "en": "85.0"
     },
     "label": {
      "de": "Pará (Rind, Rodungsfront)",
      "en": "Pará (beef, clearing frontier)"
     }
    },
    "dry": {
     "value": 0.08,
     "disp": {
      "de": "0,08",
      "en": "0.08"
     },
     "label": {
      "de": "São Paulo (Rind, Altland)",
      "en": "São Paulo (beef, long-standing land)"
     }
    },
    "barMax": 100,
    "ratio": {
     "de": "≈ 1'000×",
     "en": "≈ 1'000×"
    },
    "ghostValue": 50.5,
    "ghostLabel": {
     "de": "nationaler Schnitt BR: 50,5",
     "en": "national average BR: 50.5"
    },
    "callout": {
     "de": "Ein einziger Konstantwert über-belastet Altland und unter-belastet die Rodungsfront zugleich – die Auflösung pro Herkunft ist der ganze Zweck.",
     "en": "A single constant over-charges long-standing land and under-charges the frontier at the same time — per-origin resolution is the whole point."
    }
   },
   "slide2": {
    "title": {
     "de": "182 Faktoren, jeder in seine Mechanismen zerlegt",
     "en": "182 factors, each split into its mechanisms"
    },
    "body": {
     "de": "Aus verstreuten offenen Quellen (Entwaldungsdaten, IPCC-Kohlenstoffvorräte, Trase-Lieferketten) entsteht eine abfragbare Schicht: 16 Rohstoffe, 23 Länder, 119 sub-nationale Herkünfte. 164 Faktoren empirisch, 18 biophysikalisch aus der Kohlenstoff-Differenz – jeder Faktor nachvollziehbar in seine Mechanismen zerlegt, hier Palmöl Indonesien.",
     "en": "From scattered open sources (deforestation data, IPCC carbon stocks, Trase supply chains) comes a queryable layer: 16 commodities, 23 countries, 119 sub-national origins. 164 factors empirical, 18 biophysical from the carbon-stock difference — every factor traceably split into its mechanisms, here Indonesian palm oil."
    },
    "footnote": {
     "de": "Quelle: results/luc_factors.json – Palmöl Indonesien, kg CO₂eq/kg, über 20 Jahre amortisiert (PAS 2050:2011). Standard IPCC AR5 GWP100.",
     "en": "Source: results/luc_factors.json — palm oil Indonesia, kg CO₂eq/kg, amortised over 20 years (PAS 2050:2011). IPCC AR5 GWP100 default."
    },
    "renderer": "stacked-bar",
    "segments": [
     {
      "value": 2.63,
      "disp": {
       "de": "2,63",
       "en": "2.63"
      },
      "label": {
       "de": "Biomasse (Kohlenstoffvorrat)",
       "en": "Biomass (carbon stock)"
      },
      "color": "#2e7d32"
     },
     {
      "value": 2.41,
      "disp": {
       "de": "2,41",
       "en": "2.41"
      },
      "label": {
       "de": "Moor-Entwässerung",
       "en": "Peatland drainage"
      },
      "color": "#6d4c41"
     },
     {
      "value": 1.55,
      "disp": {
       "de": "1,55",
       "en": "1.55"
      },
      "label": {
       "de": "Boden-Kohlenstoff",
       "en": "Soil organic carbon"
      },
      "color": "#a1887f"
     },
     {
      "value": 0.04,
      "disp": {
       "de": "0,04",
       "en": "0.04"
      },
      "label": {
       "de": "Biomasse-Verbrennung",
       "en": "Biomass burning"
      },
      "color": "#ef6c00"
     }
    ],
    "total": {
     "disp": {
      "de": "6,64",
      "en": "6.64"
     },
     "label": {
      "de": "Palmöl Indonesien, total",
      "en": "Palm oil Indonesia, total"
     },
     "max": 7
    },
    "callout": {
     "de": "Beim indonesischen Palmöl macht die Moor-Entwässerung allein 2,4 kg aus – ein Pauschalwert pro Rohstoff würde diesen Mechanismus unsichtbar machen.",
     "en": "For Indonesian palm oil peatland drainage alone is 2.4 kg — a flat per-commodity value would make this mechanism invisible."
    }
   }
  },
  "lci-crop-residue-burning": {
   "kicker": {
    "de": "Rückstandsverbrennung auf dem Feld",
    "en": "In-field residue burning"
   },
   "slide1": {
    "title": {
     "de": "Die Emissionen, die am Hoftor verschwinden",
     "en": "The emissions that vanish at the farm gate"
    },
    "body": {
     "de": "Cradle-to-farm-gate-Datenbanken enden am Hoftor und unterstellen, Rückstände blieben liegen. Wo nach der Ernte offen abgebrannt wird — Reisstroh in Asien, Zuckerrohr in Brasilien — fehlt die ganze Nicht-CO2-Bilanz.",
     "en": "Cradle-to-farm-gate databases stop at the farm gate and assume residues stay on the field. Where post-harvest open burning happens — rice straw in Asia, sugarcane in Brazil — the entire non-CO2 inventory is missing."
    },
    "footnote": {
     "de": "Bausteine: Akagi (2011) Emissionsfaktoren, IPCC (2019) N2O-Faktor und Rückstands-Regression, publizierte Land×Kultur-Verbrennungsanteile.",
     "en": "Building blocks: Akagi (2011) emission factors, IPCC (2019) N2O factor and residue regression, published country-by-crop fractions burnt."
    },
    "bullets": [
     {
      "de": "Beantwortet: Nicht-CO2-Fussabdruck pro Hektar je Kultur",
      "en": "Answers: per-hectare non-CO2 footprint by crop"
     },
     {
      "de": "Drei getrennte Quellen zu einer Schicht verbunden",
      "en": "Three separate sources joined into one layer"
     },
     {
      "de": "Additive Biosphären-Flüsse, jede Referenz-Datenbank",
      "en": "Additive biosphere flows, any reference database"
     },
     {
      "de": "Nur das Verbrennungsereignis — kein Doppelzählen",
      "en": "Combustion event only — no double counting"
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Drei rekombinierbare Lagen, sieben Schadstoffe, 6'158 Zellen",
     "en": "Three recombinable layers, seven pollutants, 6'158 cells"
    },
    "body": {
     "de": "Drei unabhängige, bei der Abfrage neu kombinierte Lagen: Rückstandsmenge, Verbrennungsanteil, Emissionsfaktor. Die Länderauflösung ist tragend: Schweizer Getreide (0,023) liegt 44-mal tiefer als brasilianisches Zuckerrohr (0,647).",
     "en": "Three independent layers recombined at query time: residue quantity, fraction burnt, emission factor. Country resolution is load-bearing: Swiss cereal (0.023) sits 44x below Brazilian sugarcane (0.647)."
    },
    "footnote": {
     "de": "Pro Zelle: CH4 (biogen), N2O, NH3 plus NOx, SO2, PM2.5, NMVOC. 6'158 Zellen, 209 Länder, 30 Kulturgruppen; 17 gegen IPCC 2019 gepinnt. AR6 GWP100, Konfidenz 0,80.",
     "en": "Per cell: CH4 (biogenic), N2O, NH3 plus NOx, SO2, PM2.5, NMVOC. 6'158 cells, 209 countries, 30 crop groupings; 17 pinned to IPCC 2019. AR6 GWP100, confidence 0.80."
    },
    "bars": [
     {
      "label": {
       "de": "Brasilianisches Zuckerrohr (Anteil 0,647)",
       "en": "Brazilian sugarcane (fraction 0.647)"
      },
      "value": 905,
      "disp": {
       "de": "905 kg CO2eq/ha",
       "en": "905 kg CO2eq/ha"
      },
      "color": "#dc2626"
     },
     {
      "label": {
       "de": "Brasilianischer Reis",
       "en": "Brazilian rice"
      },
      "value": 377,
      "disp": {
       "de": "377 kg CO2eq/ha",
       "en": "377 kg CO2eq/ha"
      },
      "color": "#f59e0b"
     },
     {
      "label": {
       "de": "Schweizer Getreide (Anteil 0,023, reguliert)",
       "en": "Swiss cereal (fraction 0.023, regulated)"
      },
      "value": 20.6,
      "disp": {
       "de": "20,6 kg CO2eq/ha",
       "en": "20.6 kg CO2eq/ha"
      },
      "color": "#16a34a"
     }
    ]
   }
  },
  "lci-storage": {
   "kicker": {
    "de": "Lager-Infrastruktur",
    "en": "Storage infrastructure"
   },
   "slide1": {
    "title": {
     "de": "Lagerbauten — in jeder Bilanz, nicht im Katalog",
     "en": "Storage structures — in every footprint, not the catalogue"
    },
    "body": {
     "de": "Silos, Ställe und Lagerhallen verkörpern Emissionen, die der BAFU/UVEK-Hintergrund nicht führt. Diese Schicht baut sechs Lagerbauten aus ihrer Stückliste auf — Stahl, Beton, Bewehrung je zu benannten Hintergrund-Aktivitäten aufgelöst statt eines groben Gebäude-Proxys.",
     "en": "Silos, barns and warehouses embody emissions the BAFU/UVEK background doesn't carry. This layer builds six storage structures from their bill of materials — steel, concrete, reinforcement each resolved to named background activities, not a coarse building proxy."
    },
    "footnote": {
     "de": "Stücklisten aus Nemecek & Kägi (2007), WFLDB 3.1 und SALCA/Agroscope Tanikon (gemeinfrei); Material-Faktoren aus der BAFU/UVEK-Referenz (OGD). Konfidenz 0,70–0,75.",
     "en": "Bills of materials from Nemecek & Kägi (2007), WFLDB 3.1 and SALCA/Agroscope Tanikon (public domain); material factors from the BAFU/UVEK reference (OGD). Confidence 0.70–0.75."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 6,
      "label": {
       "de": "Lager-Bauwerke neu aufgebaut — fehlen alle im BAFU/UVEK-Hintergrund",
       "en": "storage structures rebuilt — all missing from the BAFU/UVEK background"
      }
     },
     {
      "n": 3,
      "label": {
       "de": "Funktionseinheiten: m³ Lagervolumen, m³ Futtervolumen, Kuhplatz-Jahr",
       "en": "functional units: m³ storage, m³ forage, cow-place-year"
      }
     }
    ],
    "items": [
     {
      "de": "Jedes Bauwerk als Komposit aus BAFU-Baustoffprozessen — kein Einzel-Proxy",
      "en": "Each structure a composite of BAFU material processes — no single proxy"
     },
     {
      "de": "Jede Komponente einzeln in den Metadaten — umbindbar auf andere Material-Güten",
      "en": "Each component logged in metadata — re-bindable to other material grades"
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Das dominante Material treibt die Bilanz — Bauwerk für Bauwerk auflösbar",
     "en": "The dominant material drives the balance — resolvable structure by structure"
    },
    "body": {
     "de": "Weil jedes Bauwerk aus seiner echten Stückliste statt aus einem Proxy entsteht, trägt das dominante Material das Ergebnis: stahllastige Silos am intensivsten, GFK- und betonlastige knapp darunter, die Holz-Heuscheune rund eine Grössenordnung tiefer. Der Milchvieh-Stall läuft je Kuhplatz-Jahr über den Gebäude-Hallen-Anker. Alle sechs liegen quervalidiert in einem schmalen Band von −1,3 % bis +7,6 % gegenüber Agribalyse 3.2.",
     "en": "Because each structure is composed from its real bill of materials rather than a proxy, the dominant material carries the result: steel-heavy silos most intensive, GRP- and concrete-heavy ones just below, the timber forage barn roughly an order of magnitude lower. The dairy stall runs per cow-place-year via the building-hall anchor. All six land, cross-validated, in a narrow −1.3% to +7.6% band against Agribalyse 3.2."
    },
    "footnote": {
     "de": "Berechnete Werte, IPCC AR6 GWP100, BAFU-Methode. Silos je m³ Lagervolumen, Heuscheune je m³ Futtervolumen, Milchvieh-Stall je Kuhplatz-Jahr (6,5 m²/Platz, 35 J.). Quervalidiert gegen Agribalyse 3.2: alle sechs im Band −1,3 % bis +7,6 %, fünf von sechs innerhalb ±1,3 %.",
     "en": "Computed values, IPCC AR6 GWP100, BAFU method. Silos per m³ storage volume, forage barn per m³ forage volume, dairy stall per cow-place-year (6.5 m²/place, 35 yr). Cross-validated against Agribalyse 3.2: all six within −1.3% to +7.6%, five of six within ±1.3%."
    },
    "bars": [
     {
      "label": {
       "de": "Stahl-Futtersilo (Stahlblech 87 %)",
       "en": "Steel feed silo (steel sheet 87%)"
      },
      "value": 210.95,
      "disp": {
       "de": "210,95 /m³",
       "en": "210.95 /m³"
      },
      "color": "#16a34a"
     },
     {
      "label": {
       "de": "GFK-Türmsilo (GFK 87 %)",
       "en": "GRP tower silo (GRP 87%)"
      },
      "value": 198.78,
      "disp": {
       "de": "198,78 /m³",
       "en": "198.78 /m³"
      },
      "color": "#16a34a"
     },
     {
      "label": {
       "de": "Beton-Fahrsilo (Beton 72 %)",
       "en": "Concrete horizontal silo (concrete 72%)"
      },
      "value": 198.23,
      "disp": {
       "de": "198,23 /m³",
       "en": "198.23 /m³"
      },
      "color": "#FFC107"
     },
     {
      "label": {
       "de": "Holz-Heuscheune (Holzbau-Anker)",
       "en": "Timber forage barn (wood-hall anchor)"
      },
      "value": 60.8,
      "disp": {
       "de": "60,8 /m³",
       "en": "60.8 /m³"
      },
      "color": "#FF9800"
     },
     {
      "label": {
       "de": "Milchvieh-Stall (je Kuhplatz-Jahr)",
       "en": "Dairy stall (per cow-place-year)"
      },
      "value": 53.38,
      "disp": {
       "de": "53,38 /Platz·J",
       "en": "53.38 /place·yr"
      },
      "color": "#FF9800"
     }
    ]
   }
  },
  "lci-fuel-combustion": {
   "kicker": {
    "de": "Verbrennungs-Emissionen je Kilogramm Treibstoff",
    "en": "Combustion emissions per kilogram of fuel"
   },
   "slide1": {
    "title": {
     "de": "Der Verbrennungs-Baustein hinter dem Essen",
     "en": "The combustion building block behind food"
    },
    "body": {
     "de": "Traktor, Gewächshaus-Heizung und Trocknung verbrennen Treibstoff. Diese Schicht liefert die direkten Abgas-Emissionen je Kilogramm: neun Treibstoffklassen, zwölf Schadstoffe, biogen korrekt verbucht.",
     "en": "Tractors, greenhouse heating and drying burn fuel. This layer supplies the direct exhaust emissions per kilogram: nine fuel classes, twelve pollutants, biogenic carbon booked correctly."
    },
    "footnote": {
     "de": "Quelle: EMEP/EEA-Leitfaden 2019 (Tier 1, global gemittelt); Funktionseinheit 1 kg verbrannter Treibstoff.",
     "en": "Source: EMEP/EEA Guidebook 2019 (Tier 1, globally averaged); functional unit 1 kg of fuel combusted."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 9,
      "label": {
       "de": "Treibstoffklassen",
       "en": "fuel classes"
      }
     },
     {
      "n": 12,
      "label": {
       "de": "Schadstoffe je Treibstoff",
       "en": "pollutants per fuel"
      }
     },
     {
      "n": 28,
      "label": {
       "de": "Hestia-Begriffe eingebunden",
       "en": "Hestia terms wired in"
      }
     }
    ],
    "items": [
     {
      "de": "Nur die Verbrennung — Brennereintritt bis Abgas",
      "en": "Combustion only — burner inlet to exhaust"
     },
     {
      "de": "12 Schadstoffe: CO2, CH4, N2O, NOx, NH3, PM u.a.",
      "en": "12 pollutants: CO2, CH4, N2O, NOx, NH3, PM etc."
     },
     {
      "de": "Biosphären-Flüsse per Katalog-Code, Datenbank austauschbar",
      "en": "Biosphere flows by catalogue code, database swappable"
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Fossil oder pflanzlich: dieselbe Markierung entscheidet die Klimabilanz",
     "en": "Fossil or plant-based: one flag decides the climate footprint"
    },
    "body": {
     "de": "Eine explizite Fossil-/Biogen-Markierung am Kohlenstoff entscheidet die Klimabilanz. Fossile Treibstoffe liegen bei 2,0 bis 3,4 kg CO2eq/kg, Biotreibstoffe (Biodiesel 3,17 kg) fallen durch Abzug des pflanzlichen CO2 auf 0,02 bis 0,04 kg.",
     "en": "An explicit fossil-versus-biogenic flag on the carbon decides the climate footprint. Fossil fuels land at 2.0 to 3.4 kg CO2eq/kg; biofuels (biodiesel 3.17 kg) drop to 0.02 to 0.04 kg once plant CO2 is removed."
    },
    "footnote": {
     "de": "Quellen: EMEP/EEA-Leitfaden 2019 + IPCC AR6 GWP100. Diesel 3,160 kg CO2/kg, im ±5%-Band des IPCC-2006-Werts (3,186).",
     "en": "Sources: EMEP/EEA Guidebook 2019 + IPCC AR6 GWP100. Diesel 3.160 kg CO2/kg, within ±5% of the IPCC 2006 default (3.186)."
    },
    "bars": [
     {
      "label": {
       "de": "Benzin (fossil)",
       "en": "Petrol (fossil)"
      },
      "value": 3.447,
      "disp": {
       "de": "3,447",
       "en": "3.447"
      },
      "color": "#FF9800"
     },
     {
      "label": {
       "de": "Heizöl schwer (fossil)",
       "en": "Heavy fuel oil (fossil)"
      },
      "value": 3.212,
      "disp": {
       "de": "3,212",
       "en": "3.212"
      },
      "color": "#FF9800"
     },
     {
      "label": {
       "de": "Diesel (fossil)",
       "en": "Diesel (fossil)"
      },
      "value": 3.199,
      "disp": {
       "de": "3,199",
       "en": "3.199"
      },
      "color": "#FF9800"
     },
     {
      "label": {
       "de": "Erdgas (fossil)",
       "en": "Natural gas (fossil)"
      },
      "value": 2.022,
      "disp": {
       "de": "2,022",
       "en": "2.022"
      },
      "color": "#FF9800"
     },
     {
      "label": {
       "de": "Biodiesel (biogen)",
       "en": "Biodiesel (biogenic)"
      },
      "value": 0.039,
      "disp": {
       "de": "0,039",
       "en": "0.039"
      },
      "color": "#16a34a"
     },
     {
      "label": {
       "de": "Holz (biogen)",
       "en": "Wood (biogenic)"
      },
      "value": 0.034,
      "disp": {
       "de": "0,034",
       "en": "0.034"
      },
      "color": "#16a34a"
     },
     {
      "label": {
       "de": "Ethanol (biogen)",
       "en": "Ethanol (biogenic)"
      },
      "value": 0.017,
      "disp": {
       "de": "0,017",
       "en": "0.017"
      },
      "color": "#16a34a"
     }
    ]
   }
  },
  "lci-irrigation": {
   "kicker": {
    "de": "Bewässerung",
    "en": "Irrigation"
   },
   "slide1": {
    "title": {
     "de": "Bewässerung, offen aus Physik statt aus einer Referenz-Datenbank",
     "en": "Irrigation, built from physics instead of a reference database"
    },
    "body": {
     "de": "Bisher waren bewässerte Lebensmittel nur über eine lizenzierte Referenz-Datenbank plus Korrektur bewertbar. Dieser Tributary baut die Dienstleistung neu: Pumpenergie aus der hydraulischen Energiegleichung, rein aus BAFU-Flüssen.",
     "en": "Irrigated food was scoreable only via a licensed reference database plus correction. This tributary rebuilds the service: pump energy from the hydraulic energy equation, purely from BAFU flows."
    },
    "footnote": {
     "de": "Quelle: README lci-irrigation; Pumpenergie 0,272 kWh/m³ (Sprinkler/Oberfläche) bzw. 0,187 kWh/m³ (Tropf).",
     "en": "Source: lci-irrigation README; pump energy 0.272 kWh/m³ (sprinkler/surface), 0.187 kWh/m³ (drip)."
    },
    "bullets": [
     {
      "de": "Problem: lizenzierte Datenbank, Korrektur veraltet je Version.",
      "en": "Problem: licensed database, correction stales each version."
     },
     {
      "de": "Lösung: je Aktivität fünf BAFU-Technosphäre-Flüsse.",
      "en": "Fix: five BAFU technosphere flows per activity."
     },
     {
      "de": "Pumpenergie aus hydraulischer Gleichung, ohne Inventardaten.",
      "en": "Pump energy from hydraulic equation, no inventory data."
     },
     {
      "de": "Einheit: 1 m³ Wasser; Knappheit ausserhalb der Grenze.",
      "en": "Unit: 1 m³ water; scarcity outside the boundary."
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Dasselbe Feld, 16-fach unterschiedlicher Fussabdruck – je nach Stromnetz",
     "en": "Same field, a 16-fold different footprint – depending on the grid"
    },
    "body": {
     "de": "Der Wert liegt in der Differenzierung: 46 Varianten über drei Techniken (Sprinkler, Tropf, Oberfläche) tragen das echte nationale Stromnetz. Da Strom dominiert, reicht die Bandbreite von 0,029 (Brasilien, Wasserkraft) bis 0,447 kg CO₂eq/m³ (Indien, Kohle) – Faktor 16.",
     "en": "The value is differentiation: 46 variants across three techniques (sprinkler, drip, surface) carry the real national grid. As electricity dominates, the range spans 0.029 (Brazil, hydro) to 0.447 kg CO₂eq/m³ (India, coal) – a factor of 16."
    },
    "footnote": {
     "de": "Quelle: results/irrigation_to_bafu_mapping.json; GWP/m³ aus BAFU-Netzfaktoren 2025; 46 Varianten (20 Sprinkler, 14 Tropf, 12 Oberfläche).",
     "en": "Source: results/irrigation_to_bafu_mapping.json; GWP/m³ from BAFU grid factors 2025; 46 variants (20 sprinkler, 14 drip, 12 surface)."
    },
    "bars": [
     {
      "label": {
       "de": "Frankreich (Atomstrom)",
       "en": "France (nuclear grid)"
      },
      "value": 0.03,
      "disp": {
       "de": "0,030",
       "en": "0.030"
      },
      "color": "#16a34a"
     },
     {
      "label": {
       "de": "Spanien",
       "en": "Spain"
      },
      "value": 0.07,
      "disp": {
       "de": "0,070",
       "en": "0.070"
      },
      "color": "#65a30d"
     },
     {
      "label": {
       "de": "USA",
       "en": "USA"
      },
      "value": 0.129,
      "disp": {
       "de": "0,129",
       "en": "0.129"
      },
      "color": "#8BC34A"
     },
     {
      "label": {
       "de": "Deutschland",
       "en": "Germany"
      },
      "value": 0.131,
      "disp": {
       "de": "0,131",
       "en": "0.131"
      },
      "color": "#FFC107"
     },
     {
      "label": {
       "de": "Australien",
       "en": "Australia"
      },
      "value": 0.198,
      "disp": {
       "de": "0,198",
       "en": "0.198"
      },
      "color": "#FB8C00"
     },
     {
      "label": {
       "de": "Indien (Kohlestrom)",
       "en": "India (coal grid)"
      },
      "value": 0.295,
      "disp": {
       "de": "0,295",
       "en": "0.295"
      },
      "color": "#e11d48"
     }
    ]
   }
  },
  "lci-fishing": {
   "kicker": {
    "de": "FISCHFANG-AUSRÜSTUNG",
    "en": "WILD-CATCH FISHING GEAR"
   },
   "slide1": {
    "title": {
     "de": "Die fehlende Schicht: das Fanggerät selbst",
     "en": "The missing layer: the fishing gear itself"
    },
    "body": {
     "de": "In der Fisch-Bilanz sind Treibstoff und Fang erfasst — das fischende Gerät bleibt ein blinder Fleck. Die Referenz führt die Rohstoffe, aber kein Inventar je Gerät. Diese Schicht baut prozessbasierte Geräte-Inventare aus benannten Material-Prozessen und macht aus der stummen Null einen realen Beitrag.",
     "en": "In the fish footprint, fuel and catch are captured — the fishing gear stays a blind spot. The reference carries the raw materials but no per-gear inventory. This layer builds process-based gear inventories from named material processes, turning a silent zero into a real contribution."
    },
    "footnote": {
     "de": "32 Einträge, 27 mit Sachbilanz je Stück; sieben Gerätefamilien; FR/NL/MA/global; Referenzjahr 2020. Quellen: Ben-Ari et al. (2017), ADEME (2020), FAO Fishing Gear Types.",
     "en": "32 entries, 27 with a per-piece inventory; seven gear families; FR/NL/MA/global; ref. year 2020. Sources: Ben-Ari et al. (2017), ADEME (2020), FAO Fishing Gear Types."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 7,
      "label": {
       "de": "Gerätefamilien: Ringwaden, Grund-/Gespann-Schleppnetze, pelagische Schleppnetze, Spiegelnetze, Beiboot, Bojen/Reusen, Hilfsaggregate",
       "en": "gear families: purse seines, bottom/pair trawls, pelagic trawls, trammel nets, skiff, buoys/traps, auxiliaries"
      }
     },
     {
      "n": 32,
      "label": {
       "de": "Sachbilanzen pro Gerätestück, Wiege bis Bahre",
       "en": "per-piece inventories, cradle-to-grave"
      }
     },
     {
      "n": 31,
      "label": {
       "de": "von 32 Einträgen ohne Biosphären-Fluss — jede Emission läuft über benannte Hintergrund-Prozesse (Ausnahme: ein Kältemittel-Leck im Verdichter)",
       "en": "of 32 entries carry no biosphere flow — every emission runs through named background processes (one exception: a refrigerant leak in the compressor)"
      }
     }
    ],
    "items": [
     {
      "de": "Referenzen decken Treibstoff und Biomasse — das Gerät selbst fehlt.",
      "en": "References cover fuel and biomass — the gear itself is missing."
     },
     {
      "de": "Material- und Entsorgungs-Flüsse zeigen auf austauschbare Prozesse.",
      "en": "Material and disposal flows point at swappable processes."
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Faktor 180'000: warum ein Stellvertreter nicht genügt",
     "en": "A factor of 180'000: why one proxy will not do"
    },
    "body": {
     "de": "Fanggerät ist heterogener als alles andere in einer Lebensmittel-Bilanz: Die Klimalast pro Stück spannt rund fünf Grössenordnungen — vom Bojen-Seil bei rund 5 kg CO₂e bis zur 1'800-m-Ringwade bei rund 907'000 kg, fast nur Netz-Nylon. Ein Sammel-Stellvertreter ebnete das ein; jeder Eintrag trägt sein Rezept.",
     "en": "Fishing gear is more heterogeneous than anything else in a food inventory: the per-piece climate burden spans roughly five orders of magnitude — from a buoy rope at about 5 kg CO₂e to an 1'800 m purse seine at about 907'000 kg, almost all net nylon. One aggregate proxy flattens that; each entry carries its recipe."
    },
    "footnote": {
     "de": "Klimalast pro Stück (BAFU IPCC 2021 GWP100): grösstes rund 907'000 kg CO₂e (Ringwade), kleinstes rund 5 kg (Bojen-Seil) — Faktor rund 180'000.",
     "en": "Per-piece burden (BAFU IPCC 2021 GWP100): largest about 907'000 kg CO₂e (purse seine), smallest about 5 kg (buoy rope) — a factor of about 180'000."
    },
    "bars": [
     {
      "label": {
       "de": "Ringwade 1'800 m (Nylonmasse)",
       "en": "purse seine 1'800 m (nylon mass)"
      },
      "value": 906896,
      "disp": {
       "de": "906'896",
       "en": "906,896"
      },
      "color": "#0e7490"
     },
     {
      "label": {
       "de": "Grundschleppnetz 63 m",
       "en": "bottom trawl 63 m"
      },
      "value": 82807,
      "disp": {
       "de": "82'807",
       "en": "82,807"
      },
      "color": "#0891b2"
     },
     {
      "label": {
       "de": "Thunfisch-Beiboot (Polyester-Rumpf + Motor)",
       "en": "tuna skiff (GRP hull + engine)"
      },
      "value": 63895,
      "disp": {
       "de": "63'895",
       "en": "63,895"
      },
      "color": "#22a5b8"
     },
     {
      "label": {
       "de": "pelagisches Schleppnetz 114 m",
       "en": "pelagic trawl 114 m"
      },
      "value": 9864,
      "disp": {
       "de": "9'864",
       "en": "9,864"
      },
      "color": "#38bdc8"
     },
     {
      "label": {
       "de": "Spiegelnetz 100 m",
       "en": "trammel net 100 m"
      },
      "value": 36,
      "disp": {
       "de": "36",
       "en": "36"
      },
      "color": "#67c9b8"
     },
     {
      "label": {
       "de": "Bojen-Seil",
       "en": "buoy rope"
      },
      "value": 5,
      "disp": {
       "de": "5",
       "en": "5"
      },
      "color": "#86efac"
     }
    ]
   }
  },
  "lci-fishing-equipment": {
   "kicker": {
    "de": "Fanggeräte für die Fischerei",
    "en": "Fishing equipment for the fishery"
   },
   "slide1": {
    "title": {
     "de": "Der fehlende Gerätebau-Layer der Fischerei",
     "en": "The missing gear-construction layer for fisheries"
    },
    "body": {
     "de": "Eine Fischerei-Aktivität braucht das Bau-Inventar ihrer Fanggeräte. Die offene BAFU/UVEK-Referenz kennt die Materialien – Nylon 66, Stahl, HDPE, GFK, Blei –, aggregiert sie aber nicht zu Geräte-Inventaren. Dieser Layer liefert sie auf Material-Granularität.",
     "en": "A fishery activity needs the construction inventory of its gear. The open BAFU/UVEK reference knows the materials – nylon 66, steel, HDPE, GRP, lead – but does not aggregate them into gear inventories. This layer supplies them at material granularity."
    },
    "footnote": {
     "de": "Materialien aus AGRIBALYSE-2.0-Fischerei-Doku (Ben-Ari et al. 2017), quergeprüft gegen FAO und IFREMER. Frankreich, 2018.",
     "en": "Materials from AGRIBALYSE 2.0 fisheries doc (Ben-Ari et al. 2017), cross-checked against FAO and IFREMER. France, 2018."
    },
    "bullets": [
     {
      "de": "Problem: Bau-Inventare pro Stück fehlen im offenen Katalog",
      "en": "Problem: per-piece construction inventories absent from catalogue"
     },
     {
      "de": "Ein Proxy einebnet drei Grössenordnungen Ringwade↔Twin-Schleppnetz",
      "en": "A proxy flattens three orders: purse seine vs twin trawl"
     },
     {
      "de": "Ohne ihn wird der Gerätebau pro kg Fisch auf null gesetzt",
      "en": "Without it, gear build per kg fish is zeroed"
     },
     {
      "de": "Lösung: 23 Investitionsgüter über zehn Geräteklassen",
      "en": "Solution: 23 capital goods across ten gear classes"
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Jedes Gerät als Mehr-Material-Inventar – substituierbar, über drei Grössenordnungen",
     "en": "Each gear as a multi-material inventory – substitutable, across three orders of magnitude"
    },
    "body": {
     "de": "Jedes Stück wird in benannte Material-Exchanges zerlegt: das dominante Material ist der Anker, das volle Inventar – Materialien, Transport, Lebensende – steht in den Metadaten und ist einzeln austauschbar. Der Katalog spannt drei Grössenordnungen: ~40 kg CO₂eq für einen Dredge-Zahn bis ~900 t für eine Thunfisch-Ringwade.",
     "en": "Each piece is decomposed into named material exchanges: the dominant material is the anchor, the full inventory – materials, transport, end-of-life – lives in the metadata and is individually substitutable. The catalogue spans three orders of magnitude: ~40 kg CO₂eq for a dredge tooth to ~900 t for a tuna purse seine."
    },
    "footnote": {
     "de": "Spanne aus fishing_equipment_to_bafu_mapping.json: 42,63 kg (Dredge-Zahn) bis 903'388 kg ≈ 900 t (Thunfisch-Ringwade). Konfidenz 0,70; 14 Tests bestehen.",
     "en": "Span from fishing_equipment_to_bafu_mapping.json: 42.63 kg (dredge tooth) to 903'388 kg ≈ 900 t (tuna purse seine). Confidence 0.70; 14 tests pass."
    },
    "stats": [
     {
      "num": {
       "de": "23",
       "en": "23"
      },
      "label": {
       "de": "Composite-Inventare über zehn Geräteklassen",
       "en": "composite inventories across ten gear classes"
      }
     },
     {
      "num": {
       "de": "~21'000×",
       "en": "~21'000×"
      },
      "label": {
       "de": "Spanne: 42,63 kg bis 903'388 kg CO₂eq pro Stück – die ein Proxy einebnen würde",
       "en": "span: 42.63 kg to 903'388 kg CO₂eq per piece – that a proxy would flatten"
      }
     },
     {
      "num": {
       "de": "6",
       "en": "6"
      },
      "label": {
       "de": "Anker-Materialien, jede Zeile einzeln substituierbar",
       "en": "anchor materials, every row independently substitutable"
      }
     },
     {
      "num": {
       "de": "0",
       "en": "0"
      },
      "label": {
       "de": "hartcodierte Emissionsfaktoren – jeder Wert ist ein benannter Hintergrundprozess",
       "en": "hardcoded emission factors – every value is a named background process"
      }
     }
    ]
   }
  },
  "lci-greenhouse": {
   "kicker": {
    "de": "GEWAECHSHAUS-MODELL",
    "en": "GREENHOUSE MODEL"
   },
   "slide1": {
    "title": {
     "de": "Treibhaus-Werte, die mit Ort, Jahreszeit und Bauart rechnen",
     "en": "Greenhouse values that account for place, season and build type"
    },
    "body": {
     "de": "Die Referenz kennt nur fixe Treibhaus-Werte, ohne Klima, Bauart oder Saison. Diese Tributary rechnet den Heizbedarf pro Kultur, Land und Erntemonat aus offenen Klimadaten neu – rund 15-facher Unterschied allein durchs Klima.",
     "en": "The reference holds only frozen greenhouse values, ignoring climate, build type and season. This tributary recomputes heating demand per crop, country and harvest month from open climate data – about a 15-fold gap from climate alone."
    },
    "footnote": {
     "de": "Tomate im beheizten Venlo-Glashaus, Jahresmittel-Heizbedarf. Meteonorm-Normalen 1991–2020. 379 Tests gegen das Produktionsmodell.",
     "en": "Tomato in a heated Venlo glass house, annual-mean heating demand. Meteonorm normals 1991–2020. 379 tests against the production model."
    },
    "renderer": "wet-dry-bars",
    "wet": {
     "value": 24.1,
     "disp": {
      "de": "24,1",
      "en": "24.1"
     },
     "label": {
      "de": "Finnland (kalt)",
      "en": "Finland (cold)"
     }
    },
    "dry": {
     "value": 1.6,
     "disp": {
      "de": "1,6",
      "en": "1.6"
     },
     "label": {
      "de": "Portugal (warm)",
      "en": "Portugal (warm)"
     }
    },
    "barMax": 26,
    "ratio": {
     "de": "rund 15x",
     "en": "about 15x"
    },
    "callout": {
     "de": "Statt eines fixen Treibhaus-Werts: 1,6 bis 24,1 MJ Heizbedarf pro kg, je nach Klima – die Referenz-Datenbank liefert hier nur eine einzige eingefrorene Zahl.",
     "en": "Instead of one frozen greenhouse value: 1.6 to 24.1 MJ heating per kg depending on climate – the reference database offers a single frozen number here."
    }
   },
   "slide2": {
    "title": {
     "de": "Vier physikalische Lasten pro Zelle – an einen austauschbaren Hintergrund gebunden",
     "en": "Four physical loads per cell – bound to a swappable background"
    },
    "body": {
     "de": "Pro Zelle aus Kultur × Land × Erntemonat rechnet eine Wärmebilanz vier Lasten: Heizen, Kühlen, LED-Zusatzlicht und Hülle. Drei Bauart-Archetypen (Venlo-Glas, Multi-Tunnel, Parral) trennen Hightech-Glashaus vom Folientunnel.",
     "en": "Per crop × country × harvest-month cell a thermal balance computes four loads: heating, cooling, LED lighting and cladding. Three build archetypes (Venlo glass, multi-tunnel, parral) separate high-tech glass house from plastic tunnel."
    },
    "footnote": {
     "de": "12 Kulturen, 3 Archetypen, 24-Länder-Raster Europa; gate-to-gate. Energie-CO2 entsteht im austauschbaren Hintergrund (BAFU/UVEK), nicht als fixer Faktor.",
     "en": "12 crops, 3 archetypes, 24-country European grid; gate-to-gate. Energy CO2 emerges from the swappable background (BAFU/UVEK), not as a fixed factor."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 12,
      "suffix": {
       "de": " Kulturen",
       "en": " crops"
      },
      "label": {
       "de": "Gemüse, Kräuter, Beeren – von Tomate bis Basilikum",
       "en": "vegetables, herbs, berries – tomato to basil"
      }
     },
     {
      "n": 3,
      "suffix": {
       "de": " Archetypen",
       "en": " archetypes"
      },
      "label": {
       "de": "Venlo-Glas, Multi-Tunnel, Parral",
       "en": "Venlo glass, multi-tunnel, parral"
      }
     },
     {
      "n": 24,
      "suffix": {
       "de": " Länder",
       "en": " countries"
      },
      "label": {
       "de": "europäisches Referenzraster, sub-national verfeinerbar",
       "en": "European reference grid, refinable sub-nationally"
      }
     }
    ],
    "items": [
     {
      "de": "Vier Lasten je Zelle: Heizen, Kühlen, Zusatzlicht, Hülle",
      "en": "Four loads per cell: heating, cooling, lighting, cladding"
     },
     {
      "de": "Energieflüsse an austauschbare Hintergrund-Aktivitäten gebunden",
      "en": "Energy flows bound to swappable background activities"
     }
    ]
   }
  },
  "lci-water-scarcity": {
   "kicker": {
    "de": "WASSERKNAPPHEITS-SCHICHT",
    "en": "WATER-SCARCITY LAYER"
   },
   "slide1": {
    "title": {
     "de": "Vom flachen Liter zum orts-gewichteten Wert",
     "en": "From a flat litre to a location-weighted value"
    },
    "body": {
     "de": "Die Referenz bewertet Treibhausgase, aber kein Wasser – jeder Kubikmeter zählt gleich. Diese Schicht gewichtet jeden Liter nach lokaler Knappheit (AWARE 2.0); je nach Region bis zu zehnfach schwerer.",
     "en": "The reference scores greenhouse gases but not water – every cubic metre counts the same. This layer weights each litre by local scarcity (AWARE 2.0), up to tenfold heavier by region."
    },
    "footnote": {
     "de": "Quelle: AWARE 2.0 (Boulay et al. 2018; Seitfudem et al. 2025), WULCA + HESTIA sub-national. Faktor 0,1–100, Welt-Schnitt = 1.",
     "en": "Source: AWARE 2.0 (Boulay et al. 2018; Seitfudem et al. 2025), WULCA + HESTIA sub-national. Factor 0.1–100, world average = 1."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 3340,
      "label": {
       "de": "GADM-Regionen mit eigenem Knappheits-Faktor (247 Länder + 3'093 sub-national)",
       "en": "GADM regions with their own scarcity factor (247 countries + 3,093 sub-national)"
      }
     },
     {
      "n": 1000,
      "suffix": {
       "de": "×",
       "en": "×"
      },
      "label": {
       "de": "Spannweite der Knappheit, vom wasserreichsten (0,1) bis zum knappsten Gebiet (100)",
       "en": "scarcity span, from the most water-rich (0.1) to the scarcest region (100)"
      }
     }
    ],
    "items": [
     {
      "de": "Kette: GADM sub-national → Land → ISO → Region → Welt",
      "en": "Chain: GADM sub-national → country → ISO → region → world"
     },
     {
      "de": "Eintrag: Volumen, Faktor, Score, GADM-ID – prüfbar",
      "en": "Entry: volume, factor, score, GADM ID – auditable"
     },
     {
      "de": "Läuft beim Build, ohne das Inventar zu ändern",
      "en": "Runs at build time, without altering inventory"
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Derselbe Wasserverbrauch, am Herkunftsort neu gewichtet",
     "en": "The same water use, re-weighted at its origin"
    },
    "body": {
     "de": "Dieselbe Blauwasser-Menge – doch der Knappheits-Wert hängt vom Entnahmeort ab. Wasserreiche Schweiz (2,07) und arides Saudi-Arabien (38,1) trennt über eine Grössenordnung; 73 % der Regionen sind knapper.",
     "en": "The same blue-water volume – yet scarcity depends on the withdrawal site. Water-rich Switzerland (2.07) and arid Saudi Arabia (38.1) differ by over an order of magnitude; 73% of regions are scarcer."
    },
    "footnote": {
     "de": "AWARE 2.0, Agrar-Variante (m³ Welt-Äq./m³): Schweiz 2,07, Saudi-Arabien 38,1. 2'191 von 3'012 Regionen knapper.",
     "en": "AWARE 2.0, agricultural variant (m³ world-eq./m³): Switzerland 2.07, Saudi Arabia 38.1. 2,191 of 3,012 regions scarcer."
    },
    "renderer": "wet-dry-bars",
    "wet": {
     "value": 2.07,
     "disp": {
      "de": "2,07",
      "en": "2.07"
     },
     "label": {
      "de": "Schweiz, wasserreich (GADM-CHE)",
      "en": "Switzerland, water-rich (GADM-CHE)"
     }
    },
    "dry": {
     "value": 38.1,
     "disp": {
      "de": "38,1",
      "en": "38.1"
     },
     "label": {
      "de": "Saudi-Arabien, arid (GADM-SAU)",
      "en": "Saudi Arabia, arid (GADM-SAU)"
     }
    },
    "barMax": 40,
    "ratio": {
     "de": "≈ 18×",
     "en": "≈ 18×"
    },
    "callout": {
     "de": "Pro Kubikmeter Bewässerung: 2,07 vs. 38,1 m³ Welt-Äquivalent – bei identischem Wasserverbrauch im Inventar, allein durch den Herkunftsort.",
     "en": "Per cubic metre of irrigation: 2.07 vs 38.1 m³ world-equivalent – identical water use in the inventory, decided solely by origin."
    }
   }
  },
  "lci-algae": {
   "kicker": {
    "de": "Algen & Mikroalgen",
    "en": "Algae & microalgae"
   },
   "slide1": {
    "title": {
     "de": "Eine Lücke, die kein Referenzeintrag füllt",
     "en": "A gap no reference entry fills"
    },
    "body": {
     "de": "Algen, Alginat, Agar und Spirulina fehlen im öffentlichen BAFU/UVEK-Hintergrund; andere Kataloge nutzen grobe, regional unpassende Stellvertreter. Diese Schicht leitet aus Primärliteratur 8 zusammengesetzte plus 8 Korrektur-Zellen ab.",
     "en": "Algae, alginate, agar and spirulina have no entry in the public BAFU/UVEK background; other catalogues use coarse, regionally unfit proxies. This layer derives 8 composite plus 8 overlay-fix cells from primary literature."
    },
    "footnote": {
     "de": "Quelle: lci-algae README und Report. 11 publizierte Zellen; Jahre 2016–2024; 56 Tests.",
     "en": "Source: lci-algae README and report. 11 published cells; years 2016–2024; 56 tests."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 0,
      "suffix": {
       "de": "native Einträge",
       "en": "native entries"
      },
      "label": {
       "de": "Algen/Alginat/Agar/Spirulina im BAFU/UVEK-Referenzkatalog vorher",
       "en": "algae/alginate/agar/spirulina in the BAFU/UVEK reference catalogue before"
      }
     },
     {
      "n": 8,
      "suffix": {
       "de": "+ 8 Overlay",
       "en": "+ 8 overlay"
      },
      "label": {
       "de": "neu abgeleitete Gate-to-Gate-Zellen aus Primärliteratur",
       "en": "newly derived gate-to-gate cells from primary literature"
      }
     },
     {
      "n": 3,
      "suffix": {
       "de": "Grössenordnungen",
       "en": "orders of magnitude"
      },
      "label": {
       "de": "Spanne der Zellen: Setzling 0.003 bis Spirulina 9.7 kg CO₂eq/kg",
       "en": "span of the cells: nursery 0.003 to spirulina 9.7 kg CO₂eq/kg"
      }
     }
    ],
    "items": [
     {
      "de": "Makroalgen frisch & getrocknet, Wildernte",
      "en": "Macroalgae fresh & dried, wild harvest"
     },
     {
      "de": "Alginat & Agar — Produktion und Markt",
      "en": "Alginate & agar — production and market"
     },
     {
      "de": "Spirulina, standortspezifisch (China) und global",
      "en": "Spirulina, location-specific (China) and global"
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Jeder Fluss hängt an einem benannten Hintergrund",
     "en": "Every flow bound to a named background"
    },
    "body": {
     "de": "Jeder Energie-, Chemikalien- und Materialfluss ist Austausch gegen eine benannte Hintergrund-Aktivität, kein fester Emissionsfaktor. So ist die Schicht regional umschaltbar und bis zur Quelle rückführbar — und löst Stellvertreter-Fehler wie EU-Netz auf China-Teich, −55%.",
     "en": "Every energy, chemical and material flow is an exchange against a named background activity, not a hardcoded factor. So the layer is regionally swappable and traceable to source — resolving proxy errors like an EU grid on a Chinese pond, −55%."
    },
    "footnote": {
     "de": "Quelle: lci-algae README und Report. Spirulina-Netz CN ≈0.71 vs. EU ≈0.31 kg CO₂eq/kWh.",
     "en": "Source: lci-algae README and report. Spirulina grid CN ≈0.71 vs. EU ≈0.31 kg CO₂eq/kWh."
    },
    "bullets": [
     {
      "de": "Regional umschaltbar: Netz, Brennstoff oder Katalog tauschen propagiert durch jede Zelle.",
      "en": "Regionally swappable: swapping grid, fuel or catalogue propagates to every cell."
     },
     {
      "de": "Konsistent: ein Trocknungsterm (9.9 MJ/kg), ein Nass-Trocken-Faktor (4:1), geprüft.",
      "en": "Consistent: one drying term (9.9 MJ/kg), one wet-to-dry factor (4:1), checked."
     },
     {
      "de": "Rückführbar: jede Zelle aus zitierter Primärquelle, frisch auf 4 Stellen.",
      "en": "Traceable: every cell from a cited source, fresh to 4 sig figs."
     },
     {
      "de": "Löst Stellvertreter-Fehler: EU-Netz auf China-Teich −55%, falscher Brennstoff +38%.",
      "en": "Resolves proxy errors: EU grid on Chinese pond −55%, wrong fuel +38%."
     }
    ]
   }
  },
  "lci-fishing-gear": {
   "kicker": {
    "de": "Fanggerät · Kapitalausrüstung",
    "en": "Fishing gear · capital equipment"
   },
   "slide1": {
    "title": {
     "de": "Das Fanggerät selbst zählte bisher null",
     "en": "The fishing gear itself counted as zero until now"
    },
    "body": {
     "de": "In der Fisch-Bilanz sind Treibstoff und Fangmenge erfasst — das Gerät bleibt ein blinder Fleck: die Referenz-Datenbank führt Rohstoffe, aber keine Inventare je Stück, und naive Agribalyse-Schlüssel setzen den Beitrag auf null. Dieser Tributär baut je Stück ein prüfbares Werkstoff-Inventar für vier Grundschleppnetze und ein Thunfisch-Beiboot aus der französischen Fischerei-Literatur.",
     "en": "In the fish footprint, fuel and catch are captured — the gear stays a blind spot: the reference database carries raw materials but no per-piece inventories, and naive Agribalyse keys drop its contribution to zero. This tributary builds an auditable per-piece material inventory for four bottom trawls and one tuna skiff from the French fisheries literature."
    },
    "footnote": {
     "de": "results/fishing_gear_to_bafu_mapping.json. Quelle: HAL hal-02497715 (ADEME 2020), Etalab-Lizenz. Frankreich, 2020. Vertrauen 0,70.",
     "en": "results/fishing_gear_to_bafu_mapping.json. Source: HAL hal-02497715 (ADEME 2020), Etalab licence. France, 2020. Confidence 0.70."
    },
    "renderer": "wet-dry-bars",
    "wet": {
     "value": 63895,
     "disp": {
      "de": "63'895",
      "en": "63,895"
     },
     "label": {
      "de": "kg CO₂eq je Stück — mit prüfbarem Inventar",
      "en": "kg CO₂eq per piece — with auditable inventory"
     }
    },
    "dry": {
     "value": 0,
     "disp": {
      "de": "0",
      "en": "0"
     },
     "label": {
      "de": "bisher — Gerät kollabiert beim Remap auf null",
      "en": "before — gear collapsed to zero on remap"
     }
    },
    "barMax": 63895,
    "ratio": {
     "de": "von null auf real",
     "en": "from zero to real"
    },
    "ghostValue": 26076,
    "ghostLabel": {
     "de": "kleinstes Gerät (32-m-Schleppnetz)",
     "en": "smallest gear (32 m trawl)"
    },
    "callout": {
     "de": "Fünf Geräte zwischen ≈ 26 t und ≈ 64 t CO₂eq je Stück — zusammen rund 245 t verkörperte Emissionen, die im Fang-Footprint zuvor schlicht fehlten.",
     "en": "Five gears between ≈ 26 t and ≈ 64 t CO₂eq per piece — together about 245 t of embodied emissions that were simply missing from the catch footprint."
    }
   },
   "slide2": {
    "title": {
     "de": "Jeder Werkstoff verankert in einer benannten Aktivität",
     "en": "Every material bound to a named activity"
    },
    "body": {
     "de": "Statt eines Proxys ist jedes Gerät eine offene Liste: Werkstoff, Transport und Entsorgung lösen sich Stück für Stück in benannte BAFU/UVEK-Technosphäre-Aktivitäten auf. Regionalisierung oder anderes End-of-Life wird zum Katalog-Tausch; keine Biosphäre-Emission ist vorberechnet. Jede Zeile trägt den publizierten Referenzwert je Stück und das Verhältnis Schätzung/Referenz.",
     "en": "Instead of a proxy, each gear is an open list: material, transport and end-of-life each resolve to a named BAFU/UVEK technosphere activity. Regionalisation or an alternative end-of-life becomes a catalogue swap; no biosphere flow is pre-computed. Every row carries the published per-piece reference value and the estimated/reference ratio."
    },
    "footnote": {
     "de": "results/fishing_gear_to_bafu_mapping.json. Verhältnis Schätzung/Referenz 0,82–0,89 (Schnitt ≈ 0,86). Quelle: HAL hal-02497715 (ADEME 2020). Frankreich, 2020. Vertrauen 0,70.",
     "en": "results/fishing_gear_to_bafu_mapping.json. Estimated/reference ratio 0.82–0.89 (mean ≈ 0.86). Source: HAL hal-02497715 (ADEME 2020). France, 2020. Confidence 0.70."
    },
    "stats": [
     {
      "num": {
       "de": "5",
       "en": "5"
      },
      "label": {
       "de": "prüfbare Inventare je Stück (4 Schleppnetze + 1 Beiboot)",
       "en": "auditable per-piece inventories (4 trawls + 1 skiff)"
      }
     },
     {
      "num": {
       "de": "100 %",
       "en": "100%"
      },
      "label": {
       "de": "der Flüsse in benannte BAFU/UVEK-Aktivitäten aufgelöst",
       "en": "of flows resolved to named BAFU/UVEK activities"
      }
     },
     {
      "num": {
       "de": "0",
       "en": "0"
      },
      "label": {
       "de": "vorberechnete Biosphäre-Emissionen — Charakterisierung methoden-neutral",
       "en": "pre-computed biosphere emissions — characterisation method-agnostic"
      }
     },
     {
      "num": {
       "de": "0,82–0,89",
       "en": "0.82–0.89"
      },
      "label": {
       "de": "Verhältnis Schätzung/Referenz, je Zeile gegengeprüft",
       "en": "estimated/reference ratio, cross-checked on every row"
      }
     }
    ]
   }
  },
  "lci-aquaculture": {
   "kicker": {
    "de": "Aquakultur und Wildfang",
    "en": "Aquaculture and wild catch"
   },
   "slide1": {
    "title": {
     "de": "Sechzehn Fisch-Systeme, die im Referenz-Katalog gänzlich fehlen",
     "en": "Sixteen fish systems entirely absent from the reference catalogue"
    },
    "body": {
     "de": "Der BAFU/UVEK-Katalog enthält keinen Fisch- oder Aquakultur-Prozess; alle 16 Systeme — Pangasius, Lachs, Tilapia, Garnele, Muschel, Wildfang u.a. — fielen stumm aus der Bewertung. Diese Tributary baut sie als literaturbasierte Sachbilanzen.",
     "en": "The BAFU/UVEK catalogue holds no fish or aquaculture process; all 16 systems — pangasius, salmon, tilapia, prawn, mussel, wild catch and more — dropped silently from scoring. This tributary builds them as literature-based inventories."
    },
    "footnote": {
     "de": "52 Mapping-Einträge, 45 Aktivitäten. Geografien: VN, NO, GB, GR, FR, RER, GLO.",
     "en": "52 mapping entries, 45 activities. Geographies: VN, NO, GB, GR, FR, RER, GLO."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 16,
      "label": {
       "de": "Fisch-Systeme modelliert — von Pangasius und Tilapia über Lachs, Brasse, Wolfsbarsch und Garnele bis zu Muschel, Forelle, Seehecht, Seeteufel, Hering und Makrele",
       "en": "fish systems modelled — from pangasius and tilapia through salmon, bream, sea bass and prawn to mussel, trout, hake, monkfish, herring and mackerel"
      }
     },
     {
      "n": 0,
      "label": {
       "de": "Aquakultur-Prozesse im BAFU/UVEK-Referenz-Katalog vorher — alle betroffenen Produkte fielen stumm aus der Bewertung",
       "en": "aquaculture processes in the BAFU/UVEK reference catalogue before — every affected product dropped silently out of scoring"
      }
     }
    ],
    "items": [
     {
      "de": "Funktionelle Einheit: 1 kg Lebendfisch am Hoftor",
      "en": "Functional unit: 1 kg live fish at farm gate"
     },
     {
      "de": "Pangasius: 1 kg Filet",
      "en": "Pangasius: 1 kg fillet"
     },
     {
      "de": "Vier direkte Emissionsklassen",
      "en": "Four direct-emission classes"
     },
     {
      "de": "HFC-134a-/HCFC-22-Leckage, Teich-N₂O/CH₄",
      "en": "HFC-134a/HCFC-22 leakage, pond N₂O/CH₄"
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Ein Ersatzfaktor würde 25-fache Spannweite einebnen — austauschbarer Hintergrund hält sie offen",
     "en": "A proxy would flatten a 25× spread — a swappable background keeps it open"
    },
    "body": {
     "de": "Jeder Futter-, Energie-, Transport- und Verpackungs-Fluss verweist auf eine benannte Hintergrund-Aktivität statt auf einen festen Faktor. So tauscht ein Anwender Katalog oder Stromnetz aus, ohne eine Art neu herzuleiten.",
     "en": "Every feed, energy, transport and packaging flow resolves to a named background activity, not a fixed factor. A user swaps the catalogue or grid without re-deriving any species."
    },
    "footnote": {
     "de": "Spannweite je natürlicher Einheit: Brasse ≈ 2,4, Lachs ≈ 3,9, Tilapia ≈ 4,75.",
     "en": "Range per natural unit: sea bream ≈ 2.4, salmon ≈ 3.9, tilapia ≈ 4.75."
    },
    "renderer": "wet-dry-bars",
    "wet": {
     "value": 9,
     "disp": {
      "de": "≈ 9",
      "en": "≈ 9"
     },
     "label": {
      "de": "Pangasius-Filet, tiefgefroren — höchster Wert im Katalog",
      "en": "Pangasius fillet, frozen — highest in the catalogue"
     }
    },
    "dry": {
     "value": 0.36,
     "disp": {
      "de": "≈ 0,36",
      "en": "≈ 0.36"
     },
     "label": {
      "de": "Miesmuschel, Langleinen-Zucht — tiefster Wert im Katalog",
      "en": "Blue mussel, long-line — lowest in the catalogue"
     }
    },
    "barMax": 10,
    "ratio": {
     "de": "≈ 25×",
     "en": "≈ 25×"
    },
    "callout": {
     "de": "≈ 25-fache Spannweite in kg CO₂eq je kg funktioneller Einheit — die ein artübergreifender Ersatzfaktor löschen würde. Jede Art trägt ihren eigenen, aus Primärquellen abgeleiteten Parametersatz.",
     "en": "≈ 25× spread in kg CO₂eq per kg functional unit — which a cross-species proxy would erase. Each species carries its own primary-source-derived parameter set."
    }
   }
  },
  "lci-recipe": {
   "kicker": {
    "de": "Rezept-Schicht für zusammengesetzte Lebensmittel",
    "en": "Recipe layer for composed foods"
   },
   "slide1": {
    "title": {
     "de": "Die fehlende Schicht: zusammengesetzte Lebensmittel",
     "en": "The missing layer: composed foods"
    },
    "body": {
     "de": "Die Referenz-Datenbank kennt Rohstoffe und Einzelprozesse, aber nicht die tausenden zusammengesetzten Produkte (Brot, Babynahrung, Suppen, Fertiggerichte). lci-recipe zerlegt sie statistisch in ihre gemittelte Zutaten-Zusammensetzung und löst jede Zutat zu einer BAFU-Aktivität auf.",
     "en": "The reference database knows raw commodities and single processes, but not the thousands of composed products (bread, baby food, soups, ready meals). lci-recipe statistically decomposes them into an averaged ingredient mix and resolves each ingredient to a BAFU activity."
    },
    "footnote": {
     "de": "Quelle: results/recipe_to_bafu_mapping.json. Statistische Summierungs-Schicht, kein Prozessmodell — Emissionsfaktoren bleiben bei den BAFU- und Agrar-Tributaries.",
     "en": "Source: results/recipe_to_bafu_mapping.json. A statistical summarisation layer, not a process model — emission factors stay with the BAFU and agricultural tributaries."
    },
    "bullets": [
     {
      "de": "Problem: verarbeitete Lebensmittel haben in BAFU keinen eigenen Pfad.",
      "en": "Problem: processed foods have no BAFU pathway of their own."
     },
     {
      "de": "Lösung: in gemittelte Zutaten zerlegen, je Zutat zu BAFU auflösen.",
      "en": "Solution: decompose into averaged ingredients, resolve each to BAFU."
     },
     {
      "de": "Skalierung: 17'512 Produkte zu 71 Archetypen clustern.",
      "en": "Scaling: cluster 17'512 products into 71 archetypes."
     },
     {
      "de": "Sonst nur generischer Fallback für Brot, Babynahrung & Co.",
      "en": "Else only a generic fallback for bread, baby food etc."
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "8'747 Archetypen, an der Realität geeicht",
     "en": "8'747 archetypes, calibrated to reality"
    },
    "body": {
     "de": "Die Schicht liefert 8'747 Lebensmittel-Archetypen (8'770 Einträge): 71 aus eigenen Agribalyse-Kategorien, 8'612 aus der offenen Open-Food-Facts-Taxonomie, 87 produktspezifisch. Jeder trägt eine BAFU-aufgelöste Zutatenliste und GWP-Schätzwert: Brot 0,97, Poulet 3,12, Rind 39 kg CO2eq/kg.",
     "en": "The layer ships 8'747 composed-food archetypes (8'770 entries): 71 from its own Agribalyse categories, 8'612 from the open Open Food Facts taxonomy, 87 product-specific. Each carries a BAFU-resolved ingredient list and GWP estimate: bread 0.97, chicken 3.12, beef 39 kg CO2eq/kg."
    },
    "footnote": {
     "de": "Quelle: results/recipe_to_bafu_mapping.json (8'770 Einträge, 8'747 Archetypen); README.md Cross-Validation gegen publizierte LCA-Literatur.",
     "en": "Source: results/recipe_to_bafu_mapping.json (8'770 entries, 8'747 archetypes); README.md cross-validation against published LCA literature."
    },
    "renderer": "stacked-bar",
    "segments": [
     {
      "value": 8612,
      "disp": {
       "de": "8'612",
       "en": "8'612"
      },
      "label": {
       "de": "Föderiert aus Open Food Facts",
       "en": "Federated from Open Food Facts"
      },
      "color": "#2f7d5b"
     },
     {
      "value": 71,
      "disp": {
       "de": "71",
       "en": "71"
      },
      "label": {
       "de": "Agribalyse-Kategorie-Archetypen",
       "en": "Agribalyse category archetypes"
      },
      "color": "#6fae8c"
     },
     {
      "value": 87,
      "disp": {
       "de": "87",
       "en": "87"
      },
      "label": {
       "de": "Produktspezifische Rezept-Inventare",
       "en": "Product-specific recipe inventories"
      },
      "color": "#bcdccd"
     }
    ],
    "total": {
     "disp": {
      "de": "8'770",
      "en": "8'770"
     },
     "label": {
      "de": "Mapping-Einträge (8'747 ausgelieferte Archetypen)",
      "en": "Mapping entries (8'747 archetypes shipped)"
     },
     "max": 9000
    },
    "callout": {
     "de": "An der Realität geeicht: Brot 0,97 · Poulet 3,12 · Rind 39 kg CO2eq/kg — alle innerhalb publizierter LCA-Bereiche.",
     "en": "Calibrated to reality: bread 0.97 · chicken 3.12 · beef 39 kg CO2eq/kg — all within published LCA ranges."
    }
   }
  },
  "lci-seed": {
   "kicker": {
    "de": "Saatgut",
    "en": "Seed"
   },
   "slide1": {
    "title": {
     "de": "Saatgut ist ein eigenes System, nicht der Feldanbau",
     "en": "Seed is its own system, not field farming"
    },
    "body": {
     "de": "Saatgut zur Aussaat durchläuft Reinigung, Sortierung, Pelletierung, Beizung, Keimprüfung und Lager-Logistik — Schritte, die der Feldanbau derselben Frucht nicht kennt. Offene Abbildungen dafür fehlen; der Rückfall wäre proprietäre Altmengen oder ein Feldfrucht-Proxy, der Aufbereitungs-Strom und Beizmittel verfehlt.",
     "en": "Seed for sowing passes through cleaning, grading, pelleting, dressing, germination testing and storage logistics — steps the field crop of the same plant never sees. Open mappings are missing; the fallback would be proprietary legacy quantities or a field-crop proxy missing conditioning electricity and dressing."
    },
    "footnote": {
     "de": "Direkte Feldemissionen (N2O, NH3, NO3, Boden-C) bleiben bewusst bei den Agrar-Emissions-Tributaries — diese Schicht ist kein Feld-Emissionsmodell.",
     "en": "Direct field emissions (N2O, NH3, NO3, soil-C) deliberately stay with the agricultural-emissions tributaries — this layer is not a field-emission model."
    },
    "bullets": [
     {
      "de": "Reinigung, Sortierung & Pelletierung — der mechanische Aufbereitungs-Kern",
      "en": "Cleaning, grading & pelleting — the mechanical conditioning core"
     },
     {
      "de": "Chemische Beizung, Keimprüfung & Verpackung",
      "en": "Chemical dressing, germination testing & packaging"
     },
     {
      "de": "Lagerhaus-Logistik bis «ab regionalem Lager» als Systemgrenze",
      "en": "Storehouse logistics to «at regional storehouse» as the system boundary"
     },
     {
      "de": "Keine proprietären Altmengen — alles aus offenen, zitierbaren Quellen",
      "en": "No proprietary legacy quantities — everything from open, citable sources"
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Zwei Wege, 9 Kulturen, durchgängig offen",
     "en": "Two paths, 9 crops, open end to end"
    },
    "body": {
     "de": "Führt der BAFU-Katalog einen Saatgut-Aufbereitungsprozess, wird die Saatgut-Wurzel direkt darauf verankert (Zuckerrübe, Gerste, Weizen, Raps, Baumwolle, Dinkel) — der offene Zwilling, 1:1. Sonst baut die Schicht ein offenes Komposit aus publizierter Agronomie und BAFU-Technosphäre. 9 Kulturen, 28 Abbildungen.",
     "en": "Where the BAFU catalog carries a seed-conditioning process, the seed root anchors directly onto it (sugar beet, barley, wheat, rape, cotton, spelt) — the open twin, 1:1. Otherwise the layer builds an open composite from published agronomy plus BAFU technosphere. Both paths cover 9 crops across 28 mappings."
    },
    "footnote": {
     "de": "Konfidenz 0,66–0,92. Katalog-Anker erben die BAFU-Prozessunsicherheit; Komposite jene der publizierten Agronomie. BAFU-Katalogfaktoren 2025.",
     "en": "Confidence 0.66–0.92. Catalog anchors inherit BAFU process uncertainty; composites that of published agronomy. BAFU 2025 catalog factors."
    },
    "renderer": "stacked-bar",
    "segments": [
     {
      "value": 14,
      "disp": {
       "de": "14",
       "en": "14"
      },
      "label": {
       "de": "Direkte BAFU-Katalog-Anker",
       "en": "Direct BAFU catalog anchors"
      },
      "color": "#8B5E3C"
     },
     {
      "value": 14,
      "disp": {
       "de": "14",
       "en": "14"
      },
      "label": {
       "de": "Offene prozessbasierte Komposite",
       "en": "Open process-based composites"
      },
      "color": "#D9A441"
     }
    ],
    "total": {
     "disp": {
      "de": "28",
      "en": "28"
     },
     "label": {
      "de": "Saatgut-Abbildungen über 9 Kulturen",
      "en": "Seed mappings across 9 crops"
     },
     "max": 28
    },
    "callout": {
     "de": "Anker wo der Katalog ihn führt, Komposit wo er fehlt — nie ein Feldfrucht-Proxy.",
     "en": "Anchor where the catalog has one, composite where it does not — never a field-crop proxy."
    }
   }
  },
  "lci-lentil": {
   "kicker": {
    "de": "Hülsenfrüchte ab Hof",
    "en": "Pulses at farm gate"
   },
   "slide1": {
    "title": {
     "de": "Der fehlende Linsen-Datensatz — über Anker plus Korrektur gebaut",
     "en": "The missing lentil dataset — built as anchor plus correction"
    },
    "body": {
     "de": "BAFU/UVEK kennt weder Linse noch Ackerbohne; die generische Trockenbohne überschätzt das Feld-Lachgas rund zweifach. Dieser Zufluss ankert jeden Eintrag auf Eiweisserbse (BAFU 575749) und ersetzt das Feldprofil per IPCC-2019-Tier-1-Korrektur.",
     "en": "BAFU/UVEK has no lentil or faba bean; the generic dry bean overstates pulse field nitrous oxide roughly twofold. This tributary anchors each entry on protein pea (BAFU 575749) and substitutes the field profile via an IPCC 2019 Tier 1 correction."
    },
    "footnote": {
     "de": "Quelle: lci-lentil README; Anker BAFU 575749 (Eiweisserbsen, Sachsen-Anhalt). Referenz: BAFU/UVEK.",
     "en": "Source: lci-lentil README; anchor BAFU 575749 (protein peas, Saxony-Anhalt). Reference: BAFU/UVEK."
    },
    "bullets": [
     {
      "de": "Lücke: keine Linse/Ackerbohne; Proxy +2× Lachgas",
      "en": "Gap: no lentil/faba; proxy doubles nitrous oxide"
     },
     {
      "de": "Anker: Eiweisserbse BAFU 575749 (Energie, Maschinen)",
      "en": "Anchor: protein pea BAFU 575749 (energy, machinery)"
     },
     {
      "de": "Korrektur: IPCC 2019 Tier 1 als Biosphären-Austausche",
      "en": "Correction: IPCC 2019 Tier 1 as biosphere exchanges"
     },
     {
      "de": "Funktionelle Einheit: 1 kg Trockenkorn ab Hof, 2020–2025",
      "en": "Functional unit: 1 kg dried grain, farm gate, 2020–2025"
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Vier Einträge, je im publizierten Fenster",
     "en": "Four entries, each inside the published window"
    },
    "body": {
     "de": "Vier region-aufgelöste Hülsenfrucht-Bilanzen, alle im publizierten Literatur-Fenster. Zwei korrigierte Einträge zeigen beide Emissionsfaktor-Familien: kanadische Trockenfeld-Linse (Trockenklima-Tier-1, validiert an Pulse Canada, 600 Saskatchewan-Höfe) und europäische Ackerbohne (feucht-temperiert). Zwei europäische Linsen erben den Anker.",
     "en": "Four region-resolved pulse inventories, all inside the published literature window. Two corrected entries exercise both emission-factor families: Canadian rainfed lentil (dry-climate Tier 1, validated against Pulse Canada, 600 Saskatchewan farms) and European faba bean (wet/temperate). Two European lentils inherit the anchor."
    },
    "footnote": {
     "de": "kg CO₂-Äq je kg Trockenkorn (IPCC 2021 GWP100, vor Allokation). Quelle: lci-lentil README. Pulse Canada 2022 (600 Höfe); Clune 2017.",
     "en": "kg CO₂-eq per kg dried grain (IPCC 2021 GWP100, before allocation). Source: lci-lentil README. Pulse Canada 2022 (600 farms); Clune 2017."
    },
    "bars": [
     {
      "label": {
       "de": "Linse CA — Trockenfeld (korrigiert) · Fenster 0,28–0,45",
       "en": "Lentil CA — rainfed (corrected) · window 0.28–0.45"
      },
      "value": 0.326,
      "disp": {
       "de": "0,326",
       "en": "0.326"
      },
      "color": "#4C9A6B"
     },
     {
      "label": {
       "de": "Ackerbohne RER (korrigiert) · Fenster 0,35–0,65",
       "en": "Faba bean RER (corrected) · window 0.35–0.65"
      },
      "value": 0.423,
      "disp": {
       "de": "0,423",
       "en": "0.423"
      },
      "color": "#4C9A6B"
     },
     {
      "label": {
       "de": "Linse RER — Trockenfeld (Anker geerbt) · Fenster 0,35–0,75",
       "en": "Lentil RER — dryland (anchor inherited) · window 0.35–0.75"
      },
      "value": 0.626,
      "disp": {
       "de": "0,626",
       "en": "0.626"
      },
      "color": "#9AA8B5"
     },
     {
      "label": {
       "de": "Linse RER — Komposit-Proxy (Anker geerbt) · Fenster 0,35–0,75",
       "en": "Lentil RER — composite proxy (anchor inherited) · window 0.35–0.75"
      },
      "value": 0.626,
      "disp": {
       "de": "0,626",
       "en": "0.626"
      },
      "color": "#9AA8B5"
     }
    ]
   }
  },
  "lci-food-processing": {
   "kicker": {
    "de": "VERARBEITUNGS-MODELL",
    "en": "PROCESSING MODEL"
   },
   "slide1": {
    "title": {
     "de": "Die fehlende Schicht zwischen Hof und Verpackung",
     "en": "The missing layer between farm and packaging"
    },
    "body": {
     "de": "Die Referenz liefert Strom, Wärme und Wasser, aber keinen Verarbeitungsschritt. Diese Schicht schliesst die Lücke mit 428 literaturbasierten Inventaren: Eindampfen, Trocknen, Mahlen, Pressen, Fermentieren.",
     "en": "The reference provides electricity, heat and water but no processing step. This layer closes the gap with 428 literature-based inventories: evaporation, drying, milling, pressing, fermentation."
    },
    "footnote": {
     "de": "Tor-zu-Tor = 1 kg verarbeitetes Produkt am Werksausgang, zwischen Hof und Verpackung. 873 bestandene Tests.",
     "en": "Gate-to-gate = 1 kg processed product at plant exit, between farm and packaging. 873 passing tests."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 12,
      "label": {
       "de": "literaturgestützte Anlagen-Pools",
       "en": "literature-based plant pools"
      }
     },
     {
      "n": 442,
      "label": {
       "de": "fallspezifische Tor-zu-Tor-Inventare",
       "en": "case-specific gate-to-gate inventories"
      }
     },
     {
      "n": 362,
      "label": {
       "de": "erzeugte, quellen-rückführbare Aktivitäten",
       "en": "generated, source-traceable activities"
      }
     }
    ],
    "items": [
     {
      "de": "Substrat-Eigenschaften (Ausbeute, Brix) per Lookup gepaart",
      "en": "Substrate properties (yield, Brix) paired via lookup"
     },
     {
      "de": "Proxy ohne Neuherleitung: Birne erbt Apfel-Presse",
      "en": "Proxy without re-derivation: pear inherits apple press"
     },
     {
      "de": "Mehrstufige Kette (Saft → Konzentrat → Pulver)",
      "en": "Multi-step chain (juice → concentrate → powder)"
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Skalierbar und trotzdem prüfbar: jeder Wert quellen-rückführbar, der Hintergrund am Schluss austauschbar",
     "en": "Scales without losing auditability: every value source-traceable, the background swappable at the end"
    },
    "body": {
     "de": "Jeder Zahlenwert führt auf eine begutachtete Primärquelle mit fünf-achsiger Pedigree zurück, die Massenbilanz schliesst exakt, und Flüsse werden erst beim Mapping an eine Hintergrund-Aktivität gebunden — jede Zelle bleibt umhängbar.",
     "en": "Every value traces to a peer-reviewed primary source with five-axis pedigree, the mass balance closes exactly, and flows bind to a background activity only at mapping — every cell stays re-pointable."
    },
    "footnote": {
     "de": "Validierung trifft Publikation auf 1–3 %. Toleranz Voll-System ±10 %, Verarbeitung ±5–10 %. 9 Alt-Einträge in Migration.",
     "en": "Validation tracks published values within 1–3 %. Tolerance full-system ±10 %, processing ±5–10 %. 9 legacy entries migrating."
    },
    "bullets": [
     {
      "de": "Quellen-rückführbar: jeder Wert mit fünf-achsiger Pedigree",
      "en": "Source-traceable: every value with five-axis pedigree"
     },
     {
      "de": "Exakte Massenbilanz auf jedem Eintrag, keine Toleranz",
      "en": "Exact mass balance on every entry, no tolerance"
     },
     {
      "de": "Späte Hintergrund-Bindung: Netz/Szenario austauschbar",
      "en": "Late background binding: grid/scenario swappable"
     },
     {
      "de": "Validiert auf 1–3 %: Erdbeerpulver 5,62 / 5,57",
      "en": "Validated within 1–3 %: strawberry powder 5.62 / 5.57"
     }
    ]
   }
  },
  "lci-ingredient-declaration": {
   "kicker": {
    "de": "Vom Zutaten-Etikett zur footprint-fähigen Struktur",
    "en": "From the ingredient label to a footprint-ready structure"
   },
   "slide1": {
    "title": {
     "de": "Der erste Schritt zum Produkt-Footprint",
     "en": "The first step to a product footprint"
    },
    "body": {
     "de": "Jedes Verpackungsprodukt trägt seine Zusammensetzung nur als eine einzige, von Menschen geschriebene Etikettzeile. Diese Schicht überführt diesen Text in einen sauberen Zutatenbaum — Namen, Mengenanteile, verschachtelte Teil-Rezepte — als Grundlage für einen Footprint pro Zutat.",
     "en": "Every packaged product carries its composition only as a single, human-written label line. This layer turns that text into a clean ingredient tree — names, quantity shares, nested sub-recipes — the foundation on which a per-ingredient footprint can be computed at all."
    },
    "footnote": {
     "de": "Schicht 1 von 3: hier wird nur strukturiert. Das Nachschlagen der Zutatennamen in der Referenz-Datenbank übernehmen die Folge-Schichten.",
     "en": "Layer 1 of 3: this only structures. Looking up ingredient names in the reference database is the job of the following resolver layers."
    },
    "bullets": [
     {
      "de": "Eingabe: eine rohe Zutatenzeile von der Packungsrückseite. Ausgabe: ein strukturierter, maschinenlesbarer Eintrag je Zutat",
      "en": "Input: one raw ingredient line from the back of pack. Output: one structured, machine-readable record per ingredient"
     },
     {
      "de": "Erkennt die Sprache automatisch (Deutsch, Englisch, Französisch) aus Einleitung und Allergen-Hinweisen",
      "en": "Auto-detects the language (German, English, French) from the intro and allergen cues"
     },
     {
      "de": "Verschachtelte Teil-Rezepte wie «Schokolade (Kakaomasse, Zucker)» werden rekursiv zu einem Baum",
      "en": "Nested sub-recipes like «chocolate (cocoa mass, sugar)» become a recursive tree"
     },
     {
      "de": "Bewusst glossar-unabhängig: strukturiert nur — die nächste Schicht weist jedem Namen eine Aktivität zu",
      "en": "Deliberately glossary-independent: it only structures — the next layer assigns each name an activity"
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Das Chaos realer Etiketten gezähmt",
     "en": "Taming the chaos of real-world labels"
    },
    "body": {
     "de": "Reale Zutatenlisten sind unsauber: falsche Zeichenkodierung, Allergen-Hinweise, Mengen in Dutzend Schreibweisen. Der Parser normalisiert all das deterministisch — etwa eine 956-Zeichen-Zeile eines veganen Würstli-Labels zu 18 Haupt-Einträgen mit 32 Teil-Zutaten, ohne eine Warnung.",
     "en": "Real ingredient lists are messy: broken encoding, allergen cues, quantities in a dozen spellings. The parser normalises all of it deterministically — for instance a 956-character vegan sausage label into 18 top-level records with 32 nested sub-ingredients, without a single warning."
    },
    "footnote": {
     "de": "Pure Standardbibliothek, null Fremdabhängigkeiten; in EOS-Parität, 62 Tests. «8 %» / «<2 %» werden zu normierten Anteilen, «kann Spuren … enthalten» verworfen.",
     "en": "Pure standard library, zero third-party dependencies; in EOS parity, 62 tests. «8 %» / «<2 %» become normalised fractions, «may contain …» is dropped."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 16,
      "label": {
       "de": "reparierte Kodierungs-Fehler (Mojibake-Muster)",
       "en": "repaired encoding errors (mojibake patterns)"
      }
     },
     {
      "n": 3,
      "label": {
       "de": "Sprachen automatisch erkannt (DE, EN, FR)",
       "en": "languages auto-detected (DE, EN, FR)"
      }
     },
     {
      "n": 0,
      "label": {
       "de": "Fremdabhängigkeiten — pure Standardbibliothek",
       "en": "third-party dependencies — pure standard library"
      }
     }
    ],
    "items": [
     {
      "de": "Trennt an Kommas und Semikola, achtet auf Klammern",
      "en": "Splits on commas and semicolons, respecting nested brackets"
     },
     {
      "de": "Löst «8 %», «<2 %», «contains 2% or less» in Anteile auf",
      "en": "Resolves «8 %», «<2 %», «2% or less» into normalised fractions"
     },
     {
      "de": "Verwirft Allergen- und Zertifizierungs-Hinweise statt sie zu zählen",
      "en": "Drops allergen and certification cues instead of counting them"
     }
    ]
   }
  },
  "lci-salca": {
   "kicker": {
    "de": "SALCA-MODELL",
    "en": "SALCA MODEL"
   },
   "slide1": {
    "title": {
     "de": "Auf der offenen Agroscope-Methode SALCA aufgebaut",
     "en": "Built on Agroscope's SALCA method"
    },
    "body": {
     "de": "SALCA ist die etablierte Ökobilanzmethode der Forschungsgruppe Ökobilanzen von Agroscope — seit Jahren in Forschungsprojekten angewendet und seit Juni 2026 auf GitHub verfügbar. Wir setzen den Gleichungssatz in TypeScript um, gleichen ihn gegen den offiziellen Code ab und binden ihn als abfragbare, nach Mechanismus aufgelöste Schicht in unsere Pipeline ein.",
     "en": "SALCA is the established life-cycle assessment method of Agroscope's Life Cycle Assessment group — applied in research projects for years, and published on GitHub since June 2026. We re-implement the equation set in TypeScript, reconcile it against the official code, and wire it into our pipeline as a queryable, mechanism-resolved layer."
    },
    "footnote": {
     "de": "lci-salca · 15 SALCA-Domänenmodelle + Agrammon-NH₃ + MEXALCA · Methode: Agroscope (agroscope-ch/salca, LGPLv3) · gegen den offiziellen Code abgeglichen.",
     "en": "lci-salca · 15 SALCA domain models + Agrammon NH₃ + MEXALCA · method: Agroscope (agroscope-ch/salca, LGPLv3) · reconciled against the official code."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 15,
      "suffix": {
       "de": "+3",
       "en": "+3"
      },
      "label": {
       "de": "SALCA-Modelle neu umgesetzt",
       "en": "SALCA models re-implemented"
      }
     },
     {
      "n": 48,
      "suffix": {
       "de": "",
       "en": ""
      },
      "label": {
       "de": "Hof-Tor-Aktivitäten, mechanismus-aufgelöst",
       "en": "farm-gate activities, mechanism-resolved"
      }
     }
    ],
    "items": [
     {
      "de": "Plus Agrammon-NH₃, MEXALCA, SALCAsustain",
      "en": "Plus Agrammon NH₃, MEXALCA, SALCAsustain"
     },
     {
      "de": "Feld-N₂O · NH₃ · NO₃ · Feld-P · CH₄ · Boden-C — einzeln abrufbar",
      "en": "Field N₂O · NH₃ · NO₃ · field-P · CH₄ · soil-C — retrievable"
     },
     {
      "de": "Gegen den offiziellen Agroscope-Code abgeglichen, per Test verankert",
      "en": "Reconciled against the official Agroscope code, anchored by tests"
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Ein Hof-Tor-Wert — aufgelöst in seine Mechanismen, prüfbar und szenariofähig",
     "en": "One farm-gate total — resolved into its mechanisms, inspectable and scenario-ready"
    },
    "body": {
     "de": "Genau die Aufschlüsselung, die ein Hintergrund-Katalog als Einzelwert nicht liefert. Beispiel Schweizer Milchhof: 0,633 kg CO₂e pro kg Milch — und man sieht, woher jedes Gramm kommt. Enterisches und Hofdünger-CH₄ dominieren, Lachgas folgt, On-Farm-CO₂ rundet ab. Jeder Pfad ist einsehbar und unter Szenarien austauschbar.",
     "en": "Exactly the breakdown a background catalogue's single value doesn't carry. Swiss dairy farm: 0.633 kg CO₂e per kg milk — and you see where every gram comes from. Enteric and manure CH₄ dominate, nitrous oxide follows, on-farm CO₂ rounds it off. Each pathway is inspectable and swappable under scenarios."
    },
    "footnote": {
     "de": "lci-salca · Beispiel-Milchhof Mittelland (examples/swiss-dairy-farm.ts) · GWP nach IPCC AR6 · 0,633 kg liegt im Band 0,5–1,0 von Poore & Nemecek 2018.",
     "en": "lci-salca · example dairy farm, central plateau (examples/swiss-dairy-farm.ts) · GWP per IPCC AR6 · 0.633 kg sits in the 0.5–1.0 band of Poore & Nemecek 2018."
    },
    "renderer": "stacked-bar",
    "segments": [
     {
      "value": 73.5,
      "disp": {
       "de": "73,5 %",
       "en": "73.5%"
      },
      "label": {
       "de": "CH₄ enterisch + Hofdünger",
       "en": "CH₄ enteric + manure"
      },
      "color": "#FFC107"
     },
     {
      "value": 25.5,
      "disp": {
       "de": "25,5 %",
       "en": "25.5%"
      },
      "label": {
       "de": "N₂O (Feld direkt + indirekt + Lager)",
       "en": "N₂O (field direct + indirect + storage)"
      },
      "color": "#16a34a"
     },
     {
      "value": 1,
      "disp": {
       "de": "1,0 %",
       "en": "1.0%"
      },
      "label": {
       "de": "CO₂ aus Kalk",
       "en": "CO₂ from lime"
      },
      "color": "#60a5fa"
     }
    ],
    "total": {
     "disp": {
      "de": "0,633 kg CO₂e/kg Milch",
      "en": "0.633 kg CO₂e/kg milk"
     },
     "label": {
      "de": "Hof-Tor-Total, mechanisch aufgeschlüsselt",
      "en": "farm-gate total, decomposed by mechanism"
     },
     "max": 100
    },
    "callout": {
     "de": "Jeder Pfad einzeln abrufbar und austauschbar: einen Emissionsfaktor unter einem Szenario tauschen, ohne die Aktivität neu herzuleiten — was ein eingebackener Katalog-Einzelwert nicht erlaubt.",
     "en": "Each pathway retrievable and swappable: change one emission factor under a scenario without re-deriving the activity — which a baked-in catalogue single value doesn't allow."
    }
   }
  },
  "lci-dfu": {
   "kicker": {
    "de": "Funktionale Einheit",
    "en": "Functional unit"
   },
   "slide1": {
    "title": {
     "de": "Wovon man teilt, entscheidet das Ranking",
     "en": "What you divide by decides the ranking"
    },
    "body": {
     "de": "Bevor man Lebensmittel nach Umweltwirkung vergleicht, muss man wählen, wodurch man die Wirkung teilt. Jede Einfaktor-Einheit ist irgendwo kategorisch falsch, und ein Wechsel kann umkehren, was als nachhaltig gilt. Einen Konsens-Nenner gibt es bisher nicht (ISO 14040/14044, EU-PEF lassen ihn offen) – die DFU schliesst die Lücke.",
     "en": "Before ranking foods by environmental impact you must choose what to divide that impact by. Every single-factor unit is categorically wrong somewhere, and switching it can reverse what counts as sustainable. No consensus denominator exists (ISO 14040/14044, EU-PEF leave it open) – the DFU closes that gap."
    },
    "footnote": {
     "de": "Quelle: lci-dfu README («Why the gap is real») und publication/abstract.typ. EDB = Eaternity-Lebensmitteldatenbank.",
     "en": "Source: lci-dfu README («Why the gap is real») and publication/abstract.typ. EDB = Eaternity food database."
    },
    "bullets": [
     {
      "de": "Pro Kilo belohnt Wasser: Butter wirkt weit schlechter als die Milch, die sie konzentriert; eine 5-g-Fleisch-Bouillon «schlägt» Hackfleisch.",
      "en": "Per kilo rewards water: butter looks far worse than the milk it concentrates; a 5-g-beef broth «beats» minced beef."
     },
     {
      "de": "Pro Kalorie belohnt die fettesten Lebensmittel und ist für kalorienfreie undefiniert; pro Protein ist für proteinfreie undefiniert.",
      "en": "Per calorie rewards the fattiest foods and is undefined for calorie-free ones; per protein is undefined for protein-free ones."
     },
     {
      "de": "Die DFU misst statt einer Einzelgrösse, wie viel Tagesnahrung eine Portion liefert – gemittelt über Protein, Fett, Rest-Energie, Wasser und Trockenmasse.",
      "en": "Instead of one factor, the DFU measures how much daily nourishment a portion delivers – averaged over protein, fat, rest-energy, water and dry weight."
     },
     {
      "de": "Als einzige Kandidatin ist sie für jedes Produkt definiert; pro Kalorie, NRF und pro Protein lassen 5–13% der Produkte undefiniert.",
      "en": "It is the only candidate defined for every product; per-calorie, NRF and per-protein leave 5–13% of products undefined."
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Ein Nenner – für jede Wirkung, über den ganzen Katalog",
     "en": "One denominator – for every impact, across the whole catalogue"
    },
    "body": {
     "de": "Die DFU wird einmal aus den Nährwerten berechnet und teilt danach in die Wirkung hinein – dieselbe Einheit dient Klima, Wasserknappheit, Land und jedem weiteren Indikator. Sie skaliert linear mit der Masse, ist also über Zutaten und Menüs aufsummierbar, strikt positiv und allein aus der Nährwertdeklaration berechenbar.",
     "en": "The DFU is computed once from a food's nutrients, then divides into the impact – the same unit serves climate, water scarcity, land and any other indicator. It scales linearly with mass, so it is additive across ingredients and menus, strictly positive, and computable from the nutrition label alone."
    },
    "footnote": {
     "de": "Quelle: lci-dfu README + publication/abstract.typ. Klima IPCC 2021 GWP100, Wasserknappheit AWARE 2.0. EDB = Eaternity-Lebensmitteldatenbank.",
     "en": "Source: lci-dfu README + publication/abstract.typ. Climate IPCC 2021 GWP100, water scarcity AWARE 2.0. EDB = Eaternity food database."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 1,
      "label": {
       "de": "Nenner für jeden Indikator – Klima, Wasser, Land",
       "en": "denominator for every indicator – climate, water, land"
      }
     },
     {
      "n": 5,
      "label": {
       "de": "Label-Dimensionen, zu einer Grösse gemittelt",
       "en": "label dimensions, averaged into one quantity"
      }
     },
     {
      "n": 1973,
      "label": {
       "de": "von 2'331 EDB-Produkten direkt vom Label berechenbar",
       "en": "of 2,331 EDB foods computable straight from the label"
      }
     }
    ],
    "items": [
     {
      "de": "Masse-additiv: aufsummierbar über Zutaten, Rezepte und Menüs.",
      "en": "Mass-additive: summable across ingredients, recipes and menus."
     },
     {
      "de": "Impakt-agnostisch: ein Nenner pro Wirkung (Klima/Wasser korrelieren nur schwach, Spearman 0,37).",
      "en": "Impact-agnostic: one denominator per impact (climate/water correlate weakly, Spearman 0.37)."
     },
     {
      "de": "Kein Gesundheitsscore, kein Impaktmodell: liefert den Nenner, die LCA den Zähler.",
      "en": "Not a health score, not an impact model: gives the denominator, the LCA the numerator."
     }
    ]
   }
  },
  "lci-fermentation": {
   "kicker": {
    "de": "FERMENTATIONS-INVENTARE",
    "en": "FERMENTATION INVENTORIES"
   },
   "slide1": {
    "title": {
     "de": "47 Fermentations-Zutaten, die der Schweizer Referenz fehlen – als prüfbare Inventare",
     "en": "47 fermentation ingredients missing from the Swiss reference – as auditable inventories"
    },
    "body": {
     "de": "Starterkulturen, Probiotika, Zitronensäure, Hefe, Xanthan, Glutamat, Essige, Sojasauce, Tempeh, mikrobielles Lab – industriell fermentierte und synthetisierte Zutaten ohne brauchbaren BAFU/UVEK-Eintrag. Diese Tributary überführt die verstreuten Gate-to-Gate-Inventare in 47 Zellen über 21 Cluster, jede mit zitiertem Literatur-Zielwert und automatisch dagegen geprüft. Spanne: unter 1 kg CO₂-Äq (Essige, Presshefe) bis 8 kg (gefriergetrocknete Mikroben-Konzentrate).",
     "en": "Starter cultures, probiotics, citric acid, yeast, xanthan, glutamate, vinegars, soy sauce, tempeh, microbial rennet – industrially fermented and synthesised ingredients with no usable BAFU/UVEK entry. This tributary turns the scattered gate-to-gate inventories into 47 cells across 21 clusters, each with a cited literature target and auto-checked against it. Span: under 1 kg CO₂-eq (vinegars, compressed yeast) up to 8 kg (freeze-dried microbial concentrates)."
    },
    "footnote": {
     "de": "Gate-to-Gate, funktionelle Einheit 1 kg Produkt; 39 automatisierte Tests prüfen jeden Cluster gegen seinen Literatur-Zielwert. Quellen u. a. Pénicaud 2018, Gobert 2025, Ciriminna 2022, COFALEC/PwC 2012.",
     "en": "Gate-to-gate, functional unit 1 kg product; 39 automated tests check each cluster against its literature target. Sources incl. Pénicaud 2018, Gobert 2025, Ciriminna 2022, COFALEC/PwC 2012."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 47,
      "label": {
       "de": "Inventar-Zellen",
       "en": "inventory cells"
      }
     },
     {
      "n": 21,
      "label": {
       "de": "Produkt-Cluster",
       "en": "product clusters"
      }
     },
     {
      "n": 8,
      "suffix": {
       "de": " kg",
       "en": " kg"
      },
      "label": {
       "de": "CO₂-Äq am oberen Ende (gefriergetr. Kulturen)",
       "en": "CO₂-eq at the top (freeze-dried cultures)"
      }
     }
    ],
    "items": [
     {
      "de": "Fehlt in BAFU, falsch verlinkt oder verfahrenstechnisch unvollständig",
      "en": "Missing from BAFU, mis-linked, or process-incomplete"
     },
     {
      "de": "Jede Zelle mit zitiertem Literatur-Zielwert und publizierter Bandbreite",
      "en": "Every cell with a cited literature target and published range"
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Ein Durchschnittswert genügt nicht – zwei Muster, frei umhängbar",
     "en": "One average won't do – two patterns, freely repointable"
    },
    "body": {
     "de": "Derselbe Hefepasten-Anker (1,07 kg CO₂-Äq) passt als Basis für mehrere Mikroben-Produkte, taugt aber nicht als Endwert: gefriergetrocknete Milchsäurebakterien liegen bei 8 kg, getrocknete Hefe bei 1,9 kg. Statt fester Emissionsfaktoren nutzt die Tributary zwei Muster: direkter BAFU-Anker, wenn er in die Literaturspanne fällt, sonst Anker plus literaturbemessene Rest-CO₂-Korrektur für den fehlenden Schritt (z. B. Gefriertrocknung). Da die Bindung am benannten BAFU-Prozess bleibt, sind Strommix, Region oder Szenario tauschbar, ohne ein Inventar neu herzuleiten.",
     "en": "The same yeast-paste anchor (1.07 kg CO₂-eq) fits as a base for several microbial products but not as an endpoint: freeze-dried lactic-acid bacteria sit at 8 kg, dried yeast at 1.9 kg. Instead of fixed emission factors the tributary uses two patterns: a direct BAFU anchor where it lands within the literature range, else anchor plus a literature-sized residual CO₂ correction for the missing step (e.g. freeze-drying). Because the binding stays on the named BAFU process, grid mix, region or scenario are swappable without re-deriving any inventory."
    },
    "footnote": {
     "de": "Anker BAFU 292423 (Hefepaste aus Whey); Gefriertrocknung dominiert die Spanne der Kulturen (3–15 kg). Bindung am benannten Prozess statt festem Faktor macht Regionalisierung tauschbar.",
     "en": "Anchor BAFU 292423 (yeast paste from whey); freeze-drying dominates the cultures' range (3–15 kg). Binding on the named process, not a fixed factor, makes regionalisation a swap."
    },
    "bars": [
     {
      "label": {
       "de": "Hefepasten-Anker (BAFU, gemeinsame Basis)",
       "en": "Yeast-paste anchor (BAFU, shared base)"
      },
      "value": 1.07,
      "disp": {
       "de": "1,07",
       "en": "1.07"
      },
      "color": "#16a34a"
     },
     {
      "label": {
       "de": "Getrocknete Hefe – Anker + Sprühtrocknung",
       "en": "Dried yeast – anchor + spray-drying"
      },
      "value": 1.92,
      "disp": {
       "de": "1,92",
       "en": "1.92"
      },
      "color": "#84cc16"
     },
     {
      "label": {
       "de": "Gefriergetr. Milchsäurebakterien – Anker + Korrektur",
       "en": "Freeze-dried lactic-acid bacteria – anchor + correction"
      },
      "value": 8,
      "disp": {
       "de": "8,0",
       "en": "8.0"
      },
      "color": "#FFC107"
     }
    ]
   }
  },
  "lci-icbm": {
   "kicker": {
    "de": "ICBM – das Bodenkohlenstoff-Signal, das Hintergrund-Kataloge gar nicht haben",
    "en": "ICBM – the soil-carbon signal that background catalogues simply don't have"
   },
   "slide1": {
    "title": {
     "de": "Kataloge kennen kein Bodenkohlenstoff-Signal – diese Schicht liefert es",
     "en": "Catalogues carry no soil-carbon signal – this layer supplies it"
    },
    "body": {
     "de": "Referenz-Datenbanken behandeln Bodenkohlenstoff als statisch: ein fester Faktor pro Kultur, ohne Hebel für Standort, Reststoffrückführung oder Bewirtschaftung. lci-icbm ergänzt je Ackeraktivität eine signierte Korrektur pro Kilogramm Erntegut – negativ = Einlagerung, positiv = Freisetzung. Derselbe Soja ist in Québec eine Senke, in Brasilien und Indien eine Quelle.",
     "en": "Reference databases treat soil carbon as static: one fixed factor per crop, with no lever for location, residue return or management. lci-icbm adds, per crop activity, a signed correction per kilogram of harvested product – negative = sequestration, positive = release. The same soy is a sink in Québec, a source in Brazil and India."
    },
    "footnote": {
     "de": "Quelle: lci-icbm – Live-Katalog 118 Aktivitäten, 11 Kulturen, 22 Standortcodes; signierte ΔSOC-Korrektur als «CO₂, land transformation».",
     "en": "Source: lci-icbm – live catalogue of 118 activities, 11 crops, 22 location codes; signed ΔSOC correction as «CO₂, land transformation»."
    },
    "stats": [
     {
      "num": {
       "de": "118",
       "en": "118"
      },
      "label": {
       "de": "korrigierte Ackeraktivitäten – statt eines starren Faktors ein reagierendes Signal",
       "en": "corrected crop activities – a responsive signal instead of one rigid factor"
      }
     },
     {
      "num": {
       "de": "52 / 66",
       "en": "52 / 66"
      },
      "label": {
       "de": "als Boden-Senke / als Boden-Quelle ausgewiesen – das Vorzeichen, das Kataloge nicht führen",
       "en": "flagged as soil sink / soil source – the sign catalogues never carry"
      }
     },
     {
      "num": {
       "de": "22",
       "en": "22"
      },
      "label": {
       "de": "Standorte über 6 Klimaregionen – derselbe Anbau, je nach Ort Senke oder Quelle",
       "en": "locations across 6 climate regions – same crop, sink or source by place"
      }
     },
     {
      "num": {
       "de": "11",
       "en": "11"
      },
      "label": {
       "de": "Kulturen von Getreide bis Soja, Reis, Hackfrüchte und Gras",
       "en": "crops from cereals to soy, rice, root crops and grass"
      }
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Ein echtes Bodenmodell, kein Nachschlagewert – auswechselbar aufgesetzt",
     "en": "A real soil model, not a lookup – layered on, swappable"
    },
    "body": {
     "de": "Hinter jeder Korrektur steht das analytische ICBM-Zweipool-Modell: schneller Young-Pool (~1,25 a), langsamer Old-Pool (~167 a), gespeist aus Reststoff- und Wurzel-Kohlenstoff, moduliert über einen Klima-Boden-Faktor. Geeicht an Ultuna (seit 1956) und Lanna (seit 1966), trifft es die Vorräte auf ±15% im Jahr 50; Bewirtschaftung allein öffnet ~26 t C/ha. Additiv aufgesetzt – Hintergrund bleibt auswechselbar.",
     "en": "Behind every correction sits the closed-form ICBM two-pool model: a fast Young pool (~1.25 yr), a slow Old pool (~167 yr), fed by residue and root carbon, modulated by a climate–soil factor. Calibrated against Ultuna (since 1956) and Lanna (since 1966), it hits measured stocks within ±15% at year 50; management alone opens ~26 t C/ha. Layered additively – the background stays swappable."
    },
    "footnote": {
     "de": "Quelle: lci-icbm – Zweipool-Analytik (Young ~1,25 a, Old ~167 a); Ultuna/Lanna-Eichung, ±10–15% im Jahr 50; additiver Overlay (direkt-emissions-befreit); 118 Tests.",
     "en": "Source: lci-icbm – two-pool analytics (Young ~1.25 yr, Old ~167 yr); Ultuna/Lanna calibration, ±10–15% at year 50; additive overlay (direct-emission exempt); 118 tests."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 2,
      "suffix": {
       "de": " Pools",
       "en": "-pool"
      },
      "label": {
       "de": "geschlossen-analytisches ICBM-Modell – Young ~1,25 a, Old ~167 a, pro Build auditierbar",
       "en": "closed-form ICBM model – Young ~1.25 yr, Old ~167 yr, auditable on every build"
      }
     },
     {
      "n": 70,
      "suffix": {
       "de": " Jahre Eichung",
       "en": " yrs of calibration"
      },
      "label": {
       "de": "Ultuna (seit 1956) und Lanna (seit 1966) – ±15% gegen gemessene Vorräte im Jahr 50",
       "en": "Ultuna (since 1956) and Lanna (since 1966) – within ±15% of measured stocks at year 50"
      }
     },
     {
      "n": 26,
      "suffix": {
       "de": " t C/ha",
       "en": " t C/ha"
      },
      "label": {
       "de": "Spanne, die allein die Bewirtschaftung auf demselben Feld öffnet",
       "en": "spread that management alone opens on the same field"
      }
     }
    ],
    "items": [
     {
      "de": "Additiver Overlay: Energie-, Dünger- und Maschinenkette unangetastet",
      "en": "Additive overlay: background energy, fertiliser, machinery chain intact"
     },
     {
      "de": "Auswechselbar: Hintergrund-Katalog oder Wirkungsmethode tauschbar",
      "en": "Swappable: change background catalogue or impact method freely"
     }
    ]
   }
  },
  "lci-indigo-n": {
   "kicker": {
    "de": "Stickstoff-Feldemissionen",
    "en": "Field nitrogen emissions"
   },
   "slide1": {
    "title": {
     "de": "Statt eines pauschalen Weltwerts: die echte Stickstoff-Antwort des Bodens",
     "en": "Instead of one flat world default: the soil's real nitrogen response"
    },
    "body": {
     "de": "Hintergrund-Inventare setzen für gedüngte Böden einen Weltwert an (1% des Stickstoffs als Lachgas). Dieser Tributary löst die vier Feld-Emissionspfade nach Klima, Boden, Düngertyp und -menge auf – pro Kilo Ernte, mit Unsicherheitsband.",
     "en": "Background inventories apply one world default to fertilised soils (1% of nitrogen as nitrous oxide). This tributary resolves the four field-emission pathways by climate, soil, fertiliser type and rate – per kilo of harvest, with an uncertainty band."
    },
    "footnote": {
     "de": "Vier Pfade je Aktivität: direktes Lachgas (Bouwman/Stehfest), indirektes (IPCC 2019), Ammoniak (HESTIA/EMEP), Nitrat (Bockstaller 2022); 918 Kulturen, 99 Düngertypen, 175 Länder.",
     "en": "Four pathways per activity: direct nitrous oxide (Bouwman/Stehfest), indirect (IPCC 2019), ammonia (HESTIA/EMEP), nitrate (Bockstaller 2022); 918 crops, 99 fertiliser types, 175 countries."
    },
    "bullets": [
     {
      "de": "Direktes Lachgas – nach Klima, Düngerart, Boden und nichtlinearer Mengenreaktion",
      "en": "Direct nitrous oxide – by climate, fertiliser, soil and non-linear rate response"
     },
     {
      "de": "Indirektes Lachgas – über ausgewaschenen N, IPCC-2019-Kette",
      "en": "Indirect nitrous oxide – via leached nitrogen, IPCC 2019 chain"
     },
     {
      "de": "Ammoniak – vierstufige Kette je Düngerprodukt und Klima",
      "en": "Ammonia – four-tier chain per fertiliser product and climate"
     },
     {
      "de": "Nitrat – aus monatlicher Wasserbilanz statt Pauschalanteil",
      "en": "Nitrate – from a monthly water balance, not a flat fraction"
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Was der Pauschalwert verdeckt – und dieses Modell sichtbar macht",
     "en": "What the flat default hides – and this model makes visible"
    },
    "body": {
     "de": "Drei Treiber verschieben den Lachgas-Fussabdruck regional, die ein Weltwert verdeckt: die Feucht/Trocken-Klimaspaltung (0,014 gegenüber 0,005), die nichtlineare Düngermengen-Reaktion und die Auswaschung (Pauschalanteil deckt Faktor 30 ab). Alles aus offenen Quellen.",
     "en": "Three drivers shift the nitrous-oxide footprint across regions that a world default hides: the wet/dry climate split (0.014 versus 0.005), the non-linear nitrogen-rate response and leaching (flat fraction spans a factor of 30). All from open sources."
    },
    "footnote": {
     "de": "Disaggregierte direkte Emissionsfaktoren, IPCC 2019 Refinement (kg Lachgas-N je kg N). Pauschaler Auswaschungsanteil 0,01–0,73. Quellen im README.",
     "en": "Disaggregated direct emission factors, IPCC 2019 Refinement (kg nitrous-oxide N per kg N). Flat leached fraction 0.01–0.73. Sources in README."
    },
    "renderer": "wet-dry-bars",
    "wet": {
     "value": 0.014,
     "disp": {
      "de": "0,014",
      "en": "0.014"
     },
     "label": {
      "de": "Feuchtes Klima · direkter Emissionsfaktor",
      "en": "Wet climate · direct emission factor"
     }
    },
    "dry": {
     "value": 0.005,
     "disp": {
      "de": "0,005",
      "en": "0.005"
     },
     "label": {
      "de": "Trockenes Klima · direkter Emissionsfaktor",
      "en": "Dry climate · direct emission factor"
     }
    },
    "barMax": 0.016,
    "ghostValue": 0.01,
    "ghostLabel": {
     "de": "Pauschaler Weltwert (Tier 1)",
     "en": "Flat world default (Tier 1)"
    },
    "ratio": {
     "de": "Faktor 2,8 zwischen feucht und trocken",
     "en": "factor 2.8 between wet and dry"
    },
    "callout": {
     "de": "Allein die Klimaspaltung trennt feuchte von trockenen Standorten um Faktor 2,8 – beim Auswaschungsanteil deckt der Pauschalwert sogar eine Spannweite von Faktor 30 ab. Das Modell löst beides nach Standort auf.",
     "en": "The climate split alone separates wet from dry sites by a factor of 2.8 – and for the leached fraction the flat default spans a factor of 30. The model resolves both by site."
    }
   }
  },
  "lci-ingredient-amounts": {
   "kicker": {
    "de": "Fehlende Zutatenmengen aus dem Nährwertfeld rekonstruieren",
    "en": "Reconstructing missing ingredient amounts from the nutrient panel"
   },
   "slide1": {
    "title": {
     "de": "Ohne Mengen keine Ökobilanz",
     "en": "No amounts, no footprint"
    },
    "body": {
     "de": "Produkte deklarieren das Nährwertfeld, aber keine Zutatenmengen – das Gesetz verlangt Zutaten nur nach Reihenfolge, ohne Gramm. Ohne Mengen ist keine Ökobilanz eines zusammengesetzten Produkts rechenbar.",
     "en": "Products declare the nutrient panel but no ingredient amounts – the law requires ingredients only by order, without grams. Without amounts, no composite product's footprint can be computed."
    },
    "footnote": {
     "de": "Quelle: README lci-ingredient-amounts; treue Portierung des EOS-Moduls «ingredicalc» (2019–2020).",
     "en": "Source: lci-ingredient-amounts README; faithful port of the EOS «ingredicalc» module (2019–2020)."
    },
    "bullets": [
     {
      "de": "Gegeben: Nährwertfeld je 100 g plus Profile der Zutaten",
      "en": "Given: nutrient panel per 100 g plus ingredient profiles"
     },
     {
      "de": "Reihenfolge und Fix-/Min-/Max-Vorgaben machen die Mengen eindeutig",
      "en": "Order plus fixed/min/max bounds make amounts recoverable"
     },
     {
      "de": "Konvexe Optimierung trifft das Feld (STD-normalisiert)",
      "en": "Convex optimisation matches the panel (STD-normalised)"
     },
     {
      "de": "Ergebnis: geschätzte Gramm je 100 g pro Zutat",
      "en": "Result: estimated grams per 100 g per ingredient"
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Echte Rezepturen, nicht nur einfache Mischungen",
     "en": "Real recipes, not just simple blends"
    },
    "body": {
     "de": "Fehlen die Mengen, rekonstruiert diese Schicht die wahrscheinlichste Massenfraktion jeder Zutat aus dem Nährwert. Konvexe Optimierung erzwingt Reihenfolge, Summe-zu-1 und Min/Max – und berücksichtigt Trocknung statt nur lineare Mischungen.",
     "en": "When amounts are missing, this layer reconstructs each ingredient's most likely mass fraction from the nutrients. Convex optimisation enforces order, sum-to-one and min/max – and accounts for drying, not just linear blends."
    },
    "footnote": {
     "de": "Quelle: README; src/lci_ingredient_amounts/; 56 Tests; Apache-2.0 (Code) / CC-BY-4.0 (Daten).",
     "en": "Source: README; src/lci_ingredient_amounts/; 56 tests; Apache-2.0 (code) / CC-BY-4.0 (data)."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 4,
      "label": {
       "de": "Bedingungen zugleich: Reihenfolge, Summe-zu-1, Fix-%, Min-/Max-%",
       "en": "conditions at once: ordering, sum-to-1, fixed-%, min/max-%"
      }
     },
     {
      "n": 56,
      "label": {
       "de": "Tests über neun Dateien, inkl. EOS-Regressionsvektoren",
       "en": "tests across nine files, incl. EOS regression vectors"
      }
     }
    ],
    "items": [
     {
      "de": "Verschachtelte Teilrezepte: Summe-zu-1 je Ebene",
      "en": "Nested sub-recipes: sum-to-1 per level"
     },
     {
      "de": "Alkohol in Vorgär-Zucker, Kochsalz in Natrium/Chlor",
      "en": "Alcohol into pre-ferment sugar, salt into sodium/chlorine"
     },
     {
      "de": "Getrocknete Zutaten via Wassergehalt auf Frischmenge",
      "en": "Dried ingredients to fresh amount via water content"
     },
     {
      "de": "Konfidenz aus Solver-Status plus STD-Residuen",
      "en": "Confidence from solver status plus STD residuals"
     }
    ]
   }
  },
  "lci-nutrients": {
   "kicker": {
    "de": "Nährwert-Profile (Mehrländer)",
    "en": "Nutrient profiles (multi-country)"
   },
   "slide1": {
    "title": {
     "de": "Eine Nährwert-Schicht für jeden benannten Lebensmittel — 25 Behörden, eine Sprache",
     "en": "One nutrient layer for any named food — 25 agencies, one language"
    },
    "body": {
     "de": "Fussabdruck-Rechnungen brauchen pro 100 g Energie, Makros, Mineralstoffe, Vitamine und Fettsäuren zu einem frei benannten Lebensmittel. Diese Schicht liest 23 nationale plus 2 regionale Behörden in höchst unterschiedlichen Formaten ein und hebt jeden Wert auf die FAO/INFOODS-Tagnames — quellenübergreifend vergleichbar.",
     "en": "Footprint calculations need per-100 g energy, macros, minerals, vitamins and fatty acids for a free-text food name. This layer ingests 23 national plus 2 regional agencies in wildly different formats and lifts every value onto the FAO/INFOODS Tagnames — comparable across all sources."
    },
    "footnote": {
     "de": "FAO/INFOODS = Food and Agriculture Organization / Int. Network of Food Data Systems; standardisierte Nährstoff-Kürzel. Funktionale Einheit: 1 Lebensmittel, 100 g essbarer Anteil.",
     "en": "FAO/INFOODS = Food and Agriculture Organization / Int. Network of Food Data Systems; standardised nutrient identifiers. Functional unit: 1 food, 100 g edible portion."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 25,
      "label": {
       "de": "Nährwert-Behörden (23 national + 2 regional)",
       "en": "nutrient agencies (23 national + 2 regional)"
      }
     },
     {
      "n": 57176,
      "label": {
       "de": "erfasste Lebensmittel",
       "en": "foods covered"
      }
     },
     {
      "n": 2095918,
      "label": {
       "de": "(Lebensmittel, Tagname)-Werte, vereinheitlicht",
       "en": "(food, tagname) values, unified"
      }
     }
    ],
    "items": [
     {
      "de": "Formate: Excel in acht Layouts, REST-APIs, Lang-CSV, PDF, HTML — auf ein Schema",
      "en": "Formats: Excel in eight layouts, REST APIs, long CSV, PDF, HTML — onto one schema"
     },
     {
      "de": "Jede Zelle trägt die Pflicht-Quellenangabe — pro Zeile prüfbar",
      "en": "Every cell carries the required attribution — auditable per row"
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Eine Abfrage, drei Auflösungen — Herkunft entscheidet, Unsicherheit bleibt sichtbar",
     "en": "One query, three resolutions — origin decides, uncertainty stays visible"
    },
    "body": {
     "de": "Über den Caches sitzt eine einzige sediment-gestützte Schnittstelle. «Profil von Lebensmittel X aus Herkunft Y» wird je nach Herkunft auf drei Wege aufgelöst und liefert immer die Streuung zwischen den Quellen mit. Behörden weichen um bis zu ±20 % ab; die Schicht zeigt sie als (min, max, cv), statt eine Konvention als Wahrheit durchgehen zu lassen.",
     "en": "A single sediment-aware reader API sits over the caches. «Profile of food X from origin Y» resolves three ways by origin and always returns the spread between sources. Agencies disagree by up to ±20 % on the same food; the layer surfaces it as (min, max, cv) so a convention never passes as truth."
    },
    "footnote": {
     "de": "Streuung: Vollmilch liest je nach Behörde 56,5 bis 65,1 kcal/100 g. cv = Variationskoeffizient über die Quellen. Pro-Komponenten-Werte bleiben für Neu-Aggregation abrufbar.",
     "en": "Spread: whole milk reads 56.5 to 65.1 kcal/100 g depending on agency. cv = coefficient of variation across sources. Per-component values stay available for re-aggregation."
    },
    "bullets": [
     {
      "de": "Pro Land — exaktes Profil des Herkunftslands, mit Köppen-Geiger-nächstem Nachbarland als Rückfall für nicht erfasste Herkünfte",
      "en": "Per country — the origin country's exact profile, with Köppen-Geiger nearest-country fallback for uncovered origins"
     },
     {
      "de": "Regional — ein Regions-Code (z. B. RER) wird auf seine Mitgliedsländer aufgelöst, jedes erfasste Land abgefragt, zu einem Profil mit Pro-Komponenten-Herkunft aggregiert",
      "en": "Regional — a region code (e.g. RER) resolves to its member countries, each covered one is queried, aggregated into one profile with per-component provenance"
     },
     {
      "de": "Generisch — ohne Herkunft: ausreisser-bereinigte Mischung über alle erfassten Länder",
      "en": "Generic — no origin: an outlier-rejecting blend across all covered countries"
     },
     {
      "de": "Immer mitgeliefert: Cross-Country-Unsicherheit als (min, max, cv) und ein quality_flag, das jede Abdeckungslücke benennt",
      "en": "Always returned: cross-country uncertainty as (min, max, cv) and a quality_flag naming any coverage shortfall"
     }
    ]
   }
  },
  "lci-rice-ch4": {
   "kicker": {
    "de": "Methan aus Reisfeldern",
    "en": "Methane from rice paddies"
   },
   "slide1": {
    "title": {
     "de": "Aus einer flachen Regionalzahl wird eine abfragbare Methan-Schicht",
     "en": "Turning one flat regional number into a queryable methane layer"
    },
    "body": {
     "de": "Reisfelder sind eine der grössten Methanquellen der Landwirtschaft. Referenz-Datenbanken tragen dafür nur einen pauschalen Regional-Durchschnitt. Diese Schicht rechnet stattdessen das offen publizierte IPCC-Tier-2-Modell pro Kilo Reis aus vier Faktoren – Basis-Emissionsfaktor mal Wasserregime mal organische Düngung mal Anbaudauer. Jeder Faktor ist eine Eingabe, keine Konstante.",
     "en": "Rice paddies are one of agriculture's largest methane sources, yet reference databases carry only one blanket regional average. This layer instead computes the openly published IPCC Tier 2 model per kilo of rice from four factors – baseline emission factor times water regime times organic amendment times cultivation period. Every factor is an input, not a constant."
    },
    "footnote": {
     "de": "Vierfaktor-Produkt nach IPCC 2006 Gl. 5.1 / IPCC-2019-Refinement, Tab. 5.11–5.14; validiert gegen 1'068 Feldmessungen (Yan et al. 2009).",
     "en": "Four-factor product per IPCC 2006 Eq. 5.1 / IPCC 2019 Refinement, Tables 5.11–5.14; validated against 1'068 field measurements (Yan et al. 2009)."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 4,
      "label": {
       "de": "Faktoren im Modell: Emissionsfaktor, Wasserregime, Düngung, Anbaudauer",
       "en": "factors in the model: emission factor, water regime, amendment, cultivation period"
      }
     },
     {
      "n": 242,
      "label": {
       "de": "Länder-Emissionsfaktoren statt einer Regionalzahl",
       "en": "country emission factors instead of one regional number"
      }
     },
     {
      "n": 7,
      "label": {
       "de": "unterscheidbare Wasserregime – von Dauerflutung bis Trockenanbau",
       "en": "distinguishable water regimes – from continuous flood to upland"
      }
     }
    ],
    "items": [
     {
      "de": "Jeder Parameter über eine Kette aufgelöst: Override → Land → Region → global",
      "en": "Each parameter resolved via a chain: override → country → region → global"
     },
     {
      "de": "Monte-Carlo-Unsicherheitsband, Konfidenz 0,50–0,95 pro Eintrag",
      "en": "Monte Carlo uncertainty band, 0.50–0.95 confidence per entry"
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Jetzt beantwortbar: Wo und wie der Reis angebaut wird",
     "en": "Now answerable: where and how the rice is grown"
    },
    "body": {
     "de": "Weil jeder Faktor eine Eingabe ist, lassen sich zwei Fragen stellen, die eine Pauschalzahl verschluckt. Erstens das Land: derselbe Reis im Regal verursacht je nach Herkunft das 5,6-Fache an Methan. Zweitens die Bewirtschaftung – Beispiel Vietnam: frisches Stroh ins Feld einarbeiten verdreifacht den Fussabdruck fast, eine Trockenphase senkt ihn deutlich.",
     "en": "Because every factor is an input, two questions a blanket figure swallows become askable. First, the country: the same rice on the shelf causes 5.6 times more methane depending on origin. Second, the management – for Vietnam: working fresh straw into the field nearly triples the footprint, while a dry spell lowers it markedly."
    },
    "footnote": {
     "de": "Wasserregime-Reihe: identisches Produkt (1 kg gemahlen, Hof-Tor), 120 Tage, ohne Düngung; Unterschied aus Emissionsfaktor, Wasserregime und Ertrag. CO2-Äquivalent pro kg, AR6 GWP100 = 27.",
     "en": "Water-regime row: identical product (1 kg milled, farm gate), 120 days, no amendment; difference from emission factor, water regime and yield. CO2 equivalent per kg, AR6 GWP100 = 27."
    },
    "bars": [
     {
      "label": {
       "de": "Japan",
       "en": "Japan"
      },
      "value": 0.26,
      "disp": {
       "de": "0,26",
       "en": "0.26"
      }
     },
     {
      "label": {
       "de": "Italien / Spanien",
       "en": "Italy / Spain"
      },
      "value": 0.32,
      "disp": {
       "de": "0,32",
       "en": "0.32"
      }
     },
     {
      "label": {
       "de": "China",
       "en": "China"
      },
      "value": 0.38,
      "disp": {
       "de": "0,38",
       "en": "0.38"
      }
     },
     {
      "label": {
       "de": "USA",
       "en": "USA"
      },
      "value": 0.45,
      "disp": {
       "de": "0,45",
       "en": "0.45"
      }
     },
     {
      "label": {
       "de": "Vietnam",
       "en": "Vietnam"
      },
      "value": 0.96,
      "disp": {
       "de": "0,96",
       "en": "0.96"
      }
     },
     {
      "label": {
       "de": "Indien",
       "en": "India"
      },
      "value": 1.01,
      "disp": {
       "de": "1,01",
       "en": "1.01"
      }
     },
     {
      "label": {
       "de": "Thailand",
       "en": "Thailand"
      },
      "value": 1.46,
      "disp": {
       "de": "1,46",
       "en": "1.46"
      },
      "color": "#b45309"
     }
    ]
   }
  },
  "lci-rothc": {
   "kicker": {
    "de": "Bodenkohlenstoff-Modell",
    "en": "Soil carbon model"
   },
   "slide1": {
    "title": {
     "de": "Bodenkohlenstoff: aus verstreuten Gleichungen ein abfragbarer Layer",
     "en": "Soil carbon: from scattered equations to a queryable layer"
    },
    "body": {
     "de": "Referenz-Datenbanken behandeln Bodenkohlenstoff als feste Grösse – Pflug, Direktsaat, Zwischenfrucht und Hofdünger tragen denselben Faktor. Dieser Tributary baut das Fünf-Pool-Modell nach und macht den Boden-CO2-Fluss abfragbar – sensitiv auf vier Achsen zugleich.",
     "en": "Reference databases treat soil carbon as a fixed quantity – ploughing, no-till, cover crop and farmyard manure all carry the same factor. This tributary re-implements the five-pool model and makes the soil-carbon CO2 flux queryable – sensitive on four axes at once."
    },
    "footnote": {
     "de": "Fünf-Pool-Kinetik nach Coleman & Jenkinson (1996); 156 Einträge über 11 Kulturklassen und 8 Klimaregionen.",
     "en": "Five-pool kinetics after Coleman & Jenkinson (1996); 156 entries across 11 crop classes and 8 climate regions."
    },
    "bullets": [
     {
      "de": "Kultur: lignin-abgeleiteter Split labil/stabil (HESTIA, 1'018 Kulturen)",
      "en": "Crop: lignin-derived labile/stable split (HESTIA, 1,018 crops)"
     },
     {
      "de": "Klima: Temp- und Feuchte-Modifikatoren, Monatsnormalwerte, 9 Regionen",
      "en": "Climate: temp and moisture modifiers, monthly normals, 9 regions"
     },
     {
      "de": "Boden: ton-abhängig – 85 % CO2-Verlust bei 5 %, 60 % bei 50 % Ton",
      "en": "Soil: clay-dependent – 85% CO2 loss at 5%, 60% at 50% clay"
     },
     {
      "de": "Bewirtschaftung: Bearbeitung, Zwischenfrucht, 6 Dünger als Szenarien",
      "en": "Management: tillage, cover crop, 6 amendments as scenarios"
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Ein Modell, ein Vorzeichenwechsel über den Lebensmittelkorb",
     "en": "One model, a sign change across the food basket"
    },
    "body": {
     "de": "Weil dasselbe Modell auf Kultur, Klima, Boden und Bewirtschaftung reagiert, kippt der Boden-Layer vom Netto-Verlust zur Netto-Bindung: derselbe Tonboden in Ultuna (50 Jahre, Start 42 t C/ha) verliert unter Brache die Hälfte und baut unter Hofdünger auf.",
     "en": "Because the same model responds to crop, climate, soil and management, the soil layer flips from net loss to net sequestration: the same clay at Ultuna (50 years, start 42 t C/ha) loses half under bare fallow and builds up under farmyard manure."
    },
    "footnote": {
     "de": "Ultuna-Dauerversuch, Kirchmann 2004 / Kätterer 2011; einer von 8 Langzeit-Versuchen auf 5 Kontinenten.",
     "en": "Ultuna long-term experiment, Kirchmann 2004 / Kätterer 2011; one of 8 trials on 5 continents."
    },
    "renderer": "wet-dry-bars",
    "wet": {
     "value": 50,
     "disp": {
      "de": "50 t C/ha",
      "en": "50 t C/ha"
     },
     "label": {
      "de": "Mit Hofdünger – Aufbau",
      "en": "With farmyard manure – build-up"
     }
    },
    "dry": {
     "value": 21,
     "disp": {
      "de": "21 t C/ha",
      "en": "21 t C/ha"
     },
     "label": {
      "de": "Brache – Verlust",
      "en": "Bare fallow – loss"
     }
    },
    "barMax": 50,
    "ghostValue": 42,
    "ghostLabel": {
     "de": "Start 1956",
     "en": "Start 1956"
    },
    "ratio": {
     "de": "von 42 t C/ha: +8 vs. −21 in 50 Jahren",
     "en": "from 42 t C/ha: +8 vs. −21 over 50 years"
    },
    "callout": {
     "de": "Dieselbe Mechanik über den Korb: der Boden-Layer reicht von Netto-Emission (Soja, geringe Rückführung) bis Netto-Bindung (Reis, Strohrückführung) – ein Vorzeichenwechsel, den ein flacher Faktor nie zeigt.",
     "en": "The same mechanism across the basket: the soil layer spans net emission (soybean, low residue return) to net sequestration (rice, straw return) – a sign change a flat factor can never show."
    }
   }
  },
  "lci-agri-integration": {
   "kicker": {
    "de": "FELD-EMISSIONS-DIRIGENT",
    "en": "FIELD-EMISSIONS CONDUCTOR"
   },
   "slide1": {
    "title": {
     "de": "Neun Emissionspfade, eine Bilanz pro Produkt",
     "en": "Nine emission pathways, one inventory per product"
    },
    "body": {
     "de": "Ein Agrarprodukt emittiert über neun getrennte Pfade – von Bodenkohlenstoff über Feld-Lachgas bis Reis-Methan. Sechs Prozessmodelle decken je nur ein bis zwei davon ab und passen nicht zusammen. Dieser Dirigent führt sie zu einer abfragbaren Bilanz pro Aktivität zusammen – jede Zahl vom besten Modell.",
     "en": "A farm product emits through nine separate pathways – from soil carbon through field nitrous oxide to rice methane. Six process models each cover only one or two and do not compose. This conductor merges them into one queryable inventory per activity – every number from the best model."
    },
    "footnote": {
     "de": "Sechs Prozessmodelle (RothC, ICBM, Indigo-N, Reis-CH₄, Tierhaltung, SALCA), neun Pfade, sieben Biosphären-Flüsse, 447 Einträge (428 orchestriert + 19 Durchreichungen). Einheit: 1 kg Erzeugnis.",
     "en": "Six process models (RothC, ICBM, Indigo-N, rice-CH₄, livestock, SALCA), nine pathways, seven biosphere flows, 447 entries (428 orchestrated + 19 pass-through). Unit: 1 kg of product."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 6,
      "label": {
       "de": "Prozessmodelle vereint",
       "en": "process models unified"
      }
     },
     {
      "n": 9,
      "label": {
       "de": "Emissionspfade pro Produkt",
       "en": "emission pathways per product"
      }
     },
     {
      "n": 1,
      "suffix": {
       "de": " Abfrage",
       "en": " call"
      },
      "label": {
       "de": "statt sechs Einzel-Outputs",
       "en": "instead of six separate outputs"
      }
     }
    ],
    "items": [
     {
      "de": "Statt grober Länder-Pauschalen liefert jeder Pfad eine prozessbasierte Zahl.",
      "en": "Instead of coarse country lump factors, each pathway gives a process-based number."
     },
     {
      "de": "Mit Klima-, Boden- und Co-Produkt-Auflösung pro Pfad.",
      "en": "With climate, soil and co-product resolution per pathway."
     },
     {
      "de": "Deckt Schweizer Weizen wie brasilianischen Soja ab – dieselbe Bilanzform.",
      "en": "Covers Swiss wheat and Brazilian soy alike – the same inventory shape."
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Mehr als Zusammenwerfen: die Konfliktauflösung",
     "en": "More than concatenation: the conflict resolution"
    },
    "body": {
     "de": "Zwei Modelle für denselben Pfad würden doppelt zählen. Der Dirigent entscheidet pro Pfad: gleicher Pfad – das höher kalibrierte Modell gewinnt; verschiedene Pfade – additiv kombiniert. Führt die Referenz-Datenbank bereits internes Lachgas, wird der Fluss unterdrückt und dokumentiert. So vereint eine Aktivität drei Modelle ohne Doppelzählung.",
     "en": "Two models for the same pathway would double-count. The conductor decides per pathway: same pathway – the higher-calibrated model wins; different pathways – combined additively. Where the reference database already carries internal nitrous oxide, the flow is suppressed and annotated. So one activity unites three models without double counting."
    },
    "footnote": {
     "de": "Lachgas-Unterdrückung greift auf rund 100 Aktivitäten mit bereits internem Feld-Lachgas; jede wird mit Menge protokolliert. 77 handgepflegte Korrekturen überleben jeden Neubau.",
     "en": "Nitrous-oxide suppression fires on about 100 activities already carrying internal field nitrous oxide; each is logged with its amount. 77 hand-tuned fixes survive every rebuild."
    },
    "stats": [
     {
      "num": {
       "de": "höchste Stufe",
       "en": "highest tier"
      },
      "label": {
       "de": "Gleicher Pfad, zwei Modelle: das höher kalibrierte gewinnt – keine Doppelzählung",
       "en": "Same pathway, two models: the higher-calibrated one wins – no double counting"
      }
     },
     {
      "num": {
       "de": "+ additiv",
       "en": "+ additive"
      },
      "label": {
       "de": "Verschiedene Pfade werden zu einer Bilanz zusammengeführt (Faktor 1,0)",
       "en": "Different pathways merge into one inventory (factor 1.0)"
      }
     },
     {
      "num": {
       "de": "6 Pfade",
       "en": "6 pathways"
      },
      "label": {
       "de": "Für Schweizer Aktivitäten wird das Swiss-kalibrierte Modell (SALCA) auf Stufe 3 hochgestuft",
       "en": "For Swiss activities the Swiss-calibrated model (SALCA) is promoted to tier 3"
      }
     },
     {
      "num": {
       "de": "≈ 100",
       "en": "≈ 100"
      },
      "label": {
       "de": "Aktivitäten mit unterdrücktem Lachgas-Fluss – protokolliert statt still verworfen",
       "en": "activities with suppressed nitrous-oxide flow – logged, not silently dropped"
      }
     }
    ]
   }
  },
  "lci-geodata": {
   "kicker": {
    "de": "GEODATEN-DIENST",
    "en": "GEODATA SERVICE"
   },
   "slide1": {
    "title": {
     "de": "Eine geteilte Ortsschicht statt ein Dutzend unvereinbarer Raster",
     "en": "One shared place layer instead of a dozen incompatible rasters"
    },
    "body": {
     "de": "Jedes Rechenmodell braucht mehr als einen Ländernamen — Boden-Kohlenstoff will Temperatur, Niederschlag und Ton je Region, Lachgas die IPCC-Klasse und Boden-pH, der Strommix den Netzfaktor. Der Dienst reduziert ein Dutzend Roh-Raster einmalig auf ein Polygon und liefert sie über einen Auflöser für jeden Kennungstyp.",
     "en": "Every model needs more than a country name — soil-carbon wants temperature, precipitation and clay per region, nitrous-oxide the IPCC class and soil pH, the grid-mix the network factor. The service reduces a dozen raw rasters once onto one shared polygon and serves them via a resolver accepting any identifier type."
    },
    "footnote": {
     "de": "GADM = globale Verwaltungsgebiete · Quellen u.a. NASA POWER, SoilGrids 2.0, FAO GSOCmap, WRI Aqueduct · Auflöser: GADM / ISO / M49 / FAO / Name · Apache-2.0 + CC-BY-4.0",
     "en": "GADM = global administrative areas · sources incl. NASA POWER, SoilGrids 2.0, FAO GSOCmap, WRI Aqueduct · resolver: GADM / ISO / M49 / FAO / name · Apache-2.0 + CC-BY-4.0"
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 17,
      "suffix": {
       "de": "",
       "en": ""
      },
      "label": {
       "de": "Datenebenen aus unvereinbaren Roh-Rastern auf eine Schicht zusammengeführt",
       "en": "data layers from incompatible raw rasters merged into one layer"
      }
     },
     {
      "n": 5,
      "suffix": {
       "de": "",
       "en": ""
      },
      "label": {
       "de": "Kennungstypen, die der Auflöser auf dasselbe Polygon abbildet (GADM / ISO / UN / FAO / Name)",
       "en": "identifier types the resolver maps to the same polygon (GADM / ISO / UN / FAO / name)"
      }
     },
     {
      "n": 12,
      "suffix": {
       "de": "",
       "en": ""
      },
      "label": {
       "de": "Tributary-Modelle, die diese eine Schicht abfragen",
       "en": "tributary models that query this one layer"
      }
     }
    ],
    "items": [
     {
      "de": "Aggregation einmal bei der Aufnahme, nie pro Modell neu",
      "en": "Aggregation once at ingestion, never re-derived per model"
     },
     {
      "de": "Fehlt Ebene oder Region, liefert der Helfer einen Default",
      "en": "Missing layer or region returns a default, not a crash"
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "3'648 Regionen, 17 Datenebenen — Ort und Jahr sind nicht Kosmetik",
     "en": "3'648 regions, 17 data layers — place and year are not cosmetic"
    },
    "body": {
     "de": "Statt einer flachen Länderzahl liefert der Dienst je Polygon ein volles biophysikalisches Profil: 17 Ebenen über 3'648 Regionen in 237 Ländern, plus Klima-Overlays (2022–2024). Ein Zürich-Lauf zeigt es: mit dem Hitzejahr 2022 statt Durchschnitt halbiert sich die Boden-CO2-Gutschrift über 85 Kulturen, 9 kippen zu Quelle.",
     "en": "Instead of a flat country figure, the service gives a full biophysical profile per polygon: 17 layers across 3'648 regions in 237 countries, plus climate overlays (2022–2024). A Zürich run shows why: with the hot year 2022 not the average the soil-CO2 credit roughly halves across 85 crops, 9 flip from sink to source."
    },
    "footnote": {
     "de": "Basisebenen decken 92–100% der 3'648 Polygone; dünne Ebenen folgen dem Quell-Raster · Zürich (lci-rothc, 85 Kulturen): -9,91 → Hitzejahr 2022 -4,89 kg CO2",
     "en": "Base layers cover 92–100% of the 3'648 polygons; sparse layers follow the source raster · Zürich (lci-rothc, 85 crops): -9.91 → hot year 2022 -4.89 kg CO2"
    },
    "stats": [
     {
      "num": {
       "de": "3'648",
       "en": "3'648"
      },
      "label": {
       "de": "Regionsprofile (GADM L1) in 237 Ländern",
       "en": "regional profiles (GADM L1) across 237 countries"
      }
     },
     {
      "num": {
       "de": "17",
       "en": "17"
      },
      "label": {
       "de": "biophysikalische Datenebenen je Region",
       "en": "biophysical data layers per region"
      }
     },
     {
      "num": {
       "de": "2022–2024",
       "en": "2022–2024"
      },
      "label": {
       "de": "jahresspezifische Klima-Overlays neben der Klimatologie",
       "en": "year-specific climate overlays alongside the climatology"
      }
     },
     {
      "num": {
       "de": "-9,91 → -4,89",
       "en": "-9.91 → -4.89"
      },
      "label": {
       "de": "kg netto-CO2/Kultur in Zürich: Durchschnitt vs. Hitzejahr — Ort und Jahr tragen",
       "en": "kg net CO2/crop in Zürich: average vs. hot year — place and year matter"
      }
     }
    ]
   }
  },
  "lci-crops": {
   "kicker": {
    "de": "Crops LCI — Anbau-Engine bis Hoftor",
    "en": "Crops LCI — cradle-to-farm-gate engine"
   },
   "slide1": {
    "title": {
     "de": "Eine Engine für die pflanzliche Primärproduktion",
     "en": "One engine for crop primary production"
    },
    "body": {
     "de": "Jede Lebensmittel-Ökobilanz landet bei einer Frage: Was hat es physisch gebraucht, um ein Kilogramm einer Kultur in einem Land in einem Zeitraum anzubauen? lci-crops beantwortet sie pro Zelle (Kultur, Land, Jahr) und wählt Produktionsstatistik und Emissionsmodell je Zelle aus einer dokumentierten Vorrangkette — statt eines Dutzends Einzel-Assembler pro Kultur.",
     "en": "Every food LCA bottoms out in one question: what did it take, physically, to grow one kilogram of a given crop in a given country in a given period? lci-crops answers it per (commodity, country, year) cell, selecting production statistics and the direct-emission model per cell from a documented precedence chain — replacing a dozen per-commodity assemblers."
    },
    "footnote": {
     "de": "Funktionelle Einheit 1 kg am Hoftor; 5-Jahres-Mittel je Zelle; 860 Tests.",
     "en": "Functional unit 1 kg at the farm gate; 5-year-mean cells by default; 860 tests."
    },
    "stats": [
     {
      "num": {
       "de": "7'324",
       "en": "7,324"
      },
      "label": {
       "de": "Zellen (Kultur × Land × Periode) mit Ertrag und Anbaufläche",
       "en": "cells (commodity × country × period) resolving both yield and area"
      }
     },
     {
      "num": {
       "de": "128",
       "en": "128"
      },
      "label": {
       "de": "registrierte Kulturen — Obst, Gemüse, Futter, Ölsaaten, Getreide, Nüsse, Knollen, Hülsenfrüchte",
       "en": "registered commodities — fruit, vegetables, forage, oilseeds, cereals, nuts, tubers, pulses"
      }
     },
     {
      "num": {
       "de": "14'649",
       "en": "14,649"
      },
      "label": {
       "de": "publizierte Aktivitäten: je Zelle «at field» + «at storage» plus ein geteilter Diesel-Hintergrund",
       "en": "published activities: per cell «at field» + «at storage» plus one shared diesel background"
      }
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Assembler, nicht Emissionsmodell",
     "en": "Assembler, not emission model"
    },
    "body": {
     "de": "Die Engine setzt Inventare zusammen; Emissionsfaktoren rechnet sie nicht. IPCC Tier 1 lebt in lci-ipcc-tier1, Bouwman/Stehfest-N₂O in lci-indigo-n, Reis-CH₄ in Tier 2, Bodenkohlenstoff in RothC/ICBM, Landnutzungsänderung in lci-luc — jedes wird pro Zelle als gewähltes Modell aufgerufen. 25 Brückeneinträge verbinden Zellen mit der Referenzdatenbank bei Konfidenz 0,74–0,87.",
     "en": "The engine assembles inventories; it does not compute emission factors. IPCC Tier 1 lives in lci-ipcc-tier1, Bouwman/Stehfest N₂O in lci-indigo-n, rice CH₄ in Tier 2, soil carbon in RothC/ICBM, land-use change in lci-luc — each called as the selected model per cell. 25 bridge entries link cells to the reference database at confidence 0.74–0.87."
    },
    "footnote": {
     "de": "Brücken: Linse (CA), Soja (US/AR/IN), Ackerbohne (CH/CN/CA), Bohne (IN/CA), Sonnenblume (FR/HU/RU/UA), Gerste (CA). 848/860 Tests grün; 7 Upstream-Abdeckungsregressionen offen ausgewiesen.",
     "en": "Bridges: lentil (CA), soybean (US/AR/IN), fava bean (CH/CN/CA), common bean (IN/CA), sunflower (FR/HU/RU/UA), barley (CA). 848/860 tests passing; 7 upstream-coverage regressions disclosed."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 25,
      "label": {
       "de": "Brückeneinträge über 14 Zellen zur Referenzdatenbank",
       "en": "bridge entries across 14 cells into the reference database"
      }
     },
     {
      "n": 5,
      "label": {
       "de": "Emissionsmodelle, pro Zelle wählbar (Tier 1, Indigo-N, Tier 2 Reis, RothC/ICBM, LUC)",
       "en": "emission models selectable per cell (Tier 1, Indigo-N, Tier 2 rice, RothC/ICBM, LUC)"
      }
     },
     {
      "n": 860,
      "label": {
       "de": "Tests — Abdeckungslücken werden ausgewiesen, nicht versteckt",
       "en": "tests — coverage gaps are disclosed, not hidden"
      }
     }
    ],
    "items": [
     {
      "de": "Die Amortisationsform (einjährig vs. Dauerkultur) ist ein Kultur-Parameter, keine Tributär-Trennung.",
      "en": "Amortisation shape (annual vs perennial) is a per-commodity parameter, not a tributary split."
     },
     {
      "de": "Selektoren lösen Ertrag, N/P/K, Pestizid-Intensität und Bewässerungsanteil aus einer dokumentierten Vorrangkette.",
      "en": "Selectors resolve yield, N/P/K, pesticide intensity and irrigation share from a documented precedence chain."
     }
    ]
   }
  },
  "lci-meat": {
   "kicker": {
    "de": "Meat — Schlachtung und Teilstück-Allokation",
    "en": "Meat — slaughter and cut allocation"
   },
   "slide1": {
    "title": {
     "de": "Vom lebenden Tier zum Teilstück — berechnet, nie abgeschrieben",
     "en": "From the live animal to the cut — computed, never transcribed"
    },
    "body": {
     "de": "Berechnet Inventare ab Schlachthoftor aus dem lebenden Tier: Schlachtkörper, Fleisch, Teilstücke und Innereien je Art und Land. Zweistufige ökonomische Allokation (Schlachtung, dann Zerlegung) nach EC-PEFCR-Leitfaden v6.3 §7.11; nationale Zerlegeschemata füllen die Lücke, die der Leitfaden offen lässt.",
     "en": "Computes slaughterhouse-gate inventories from the live animal: carcass, meat, cuts and offal per species and country. Two-step economic allocation (slaughter, then cutting) following EC PEFCR Guidance v6.3 §7.11, with national cut schemes filling the gap the guidance leaves."
    },
    "footnote": {
     "de": "Match type meat_model; Schwester von lci-dairy. Mapping im September 2026 noch nicht befüllt.",
     "en": "Match type meat_model; sibling of lci-dairy. Mapping not yet populated (September 2026)."
    },
    "stats": [
     {
      "num": {
       "de": "2 Stufen",
       "en": "2 steps"
      },
      "label": {
       "de": "Schlacht-Split, dann Zerlege-Split — jeder schliesst exakt auf 1,0",
       "en": "slaughter split, then cutting split — each closes to exactly 1.0"
      }
     },
     {
      "num": "PEFCR 6.3",
      "label": {
       "de": "EU-Durchschnittstabellen als Rückfallstufe, wenn nationale Daten fehlen",
       "en": "EU-average default tables as the fallback tier when no national data exists"
      }
     },
     {
      "num": {
       "de": "Schwein, Huhn",
       "en": "pork, chicken"
      },
      "label": {
       "de": "zuerst; Kalb, Rind, Lamm wandern in späteren Wellen ein",
       "en": "first; veal, beef and lamb migrate in later waves"
      }
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Massen und Faktoren werden getrennt gespeichert",
     "en": "Masses and factors are stored separately"
    },
    "body": {
     "de": "Ein Ertrag ist eine physische Tatsache; ein Allokationsfaktor ein ökonomisches Ergebnis. Die Engine rechnet Faktoren beim Build aus gespeicherten Massen und Preisen neu und bricht hart ab, wenn ein Split nicht schliesst — ein Teilstück ohne Preis ist ein Build-Fehler, bis eine Entscheidung dokumentiert ist.",
     "en": "A yield is a physical fact; an allocation factor is an economic result. The engine recomputes factors from stored masses and prices at build time and hard-fails when a split does not close — a cut without a price is a build failure until a decision is recorded."
    },
    "footnote": {
     "de": "Preise treten dem Teilstück-Register per Schlüssel bei, nie per Name; jede Preiszeile nennt Quelle, Marktstufe und Jahrgang.",
     "en": "Prices join the cut registry by key, never by name; each price row records its source, market level and vintage."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 1,
      "suffix": {
       "de": ",0",
       "en": ".0"
      },
      "label": {
       "de": "Schliessung an jedem Split erzwungen — Massen- und Faktorspalte summieren je auf 1",
       "en": "closure enforced at every split — mass column and factor column each sum to 1"
      }
     },
     {
      "n": 4,
      "label": {
       "de": "deklarierte Produktstufen: Lebendgewicht, Schlachtkörper, Fleisch ohne Knochen, Teilstück wie verkauft",
       "en": "declared product levels: live weight, carcass, boneless meat, cut-as-sold"
      }
     },
     {
      "n": 1,
      "label": {
       "de": "Schlachthof-Betriebsinventar pro Art, ökonomisch über alle Outputs verteilt",
       "en": "slaughterhouse utility inventory per species, allocated economically across all outputs"
      }
     }
    ],
    "items": [
     {
      "de": "Schlachtmassen übertragen sich zwischen Ländern (Biologie); Zerlegeschemata nicht (national); Preise fallen nie zurück.",
      "en": "Slaughter masses transfer across countries (biology); cut schemes do not (national); prices never fall back."
     },
     {
      "de": "Schlachtgewicht fliesst nie stromaufwärts — die Tierproduktion bleibt in lci-livestock.",
      "en": "Carcass weight never flows upstream — live-animal production stays in lci-livestock."
     }
    ]
   }
  },
  "lci-labour-time": {
   "kicker": {
    "de": "Arbeitszeit (KAA) — ein paralleler Indikator",
    "en": "Labour time (KAA) — a parallel indicator"
   },
   "slide1": {
    "title": {
     "de": "Wie viele Minuten menschlicher Arbeit stecken in einem Lebensmittel?",
     "en": "How many minutes of human work are in a food?"
    },
    "body": {
     "de": "KAA (Kumulierter Arbeitsaufwand) berechnet die Personenminuten in einem Produkt, nach Land und Stufe — Rohproduktion, Verarbeitung, Transport, Handel — als Indikator neben dem GWP: «1,2 kg CO₂eq» und «53 Minuten menschlicher Arbeit» für dasselbe Produkt. Die Schlagzeile ist die Gesamtzeit, nie um gute Bezahlung reduziert.",
     "en": "KAA (Kumulierter Arbeitsaufwand) computes the person-minutes embodied in a product, by country and stage — raw production, processing, transport, retail — as an indicator next to GWP: «1.2 kg CO₂eq» and «53 minutes of human work» for the same product. The headline is total time, never discounted for good pay."
    },
    "footnote": {
     "de": "Datenschicht-Tributär (kein BAFU-Mapping). Lohnangemessenheit ehrlich zurückgehalten: noch kein offener Living-Wage-Benchmark.",
     "en": "Data-layer tributary (no BAFU mapping). Wage adequacy withheld honestly: no open living-wage benchmark yet."
    },
    "stats": [
     {
      "num": "100 %",
      "label": {
       "de": "Abdeckung per Konstruktion — eine gestufte Rückfallebene existiert immer, mit Band ausgewiesen",
       "en": "coverage by construction — a tiered fallback always exists, shown with its band"
      }
     },
     {
      "num": {
       "de": "~2'300",
       "en": "~2,300"
      },
      "label": {
       "de": "gemessene Hof-Zeilen über ~200 Kulturen (rund 900 echte Messungen)",
       "en": "measured farm rows across ~200 crops (about 900 true measurements)"
      }
     },
     {
      "num": "144",
      "label": {
       "de": "Länder mit ILO-Anteil informeller Arbeit",
       "en": "countries with ILO informal-labour share"
      }
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Eine Präzisionsleiter pro Stufe",
     "en": "A precision ladder per stage"
    },
    "body": {
     "de": "Herkunft aus den Zollakten des Konsumlandes mit Produzententest; Hof aus gemessenen Feldstudien → FADN-Zellen → modellierte Mischung aus monetärem Top-down (EXIOBASE × Erzeugerpreis) und preisfreiem physischem Transfer; Verarbeitung aus einer gemessenen Prozess-DB und einem Rezept-Composer; Transport als genau ein Bein pro Fluss; Handel aus gemessenen Sektorstunden.",
     "en": "Origin from the consumer country's own customs record with a producer test; farm from measured field studies → FADN cells → a modelled blend of monetary top-down (EXIOBASE × producer price) and price-free physical transfer; processing from a measured processing DB and a recipe composer; transport as exactly one leg per flow; retail from measured sector hours."
    },
    "footnote": {
     "de": "Bibliotheks-API spiegelt lci-dfu: compute_kaa(commodity, country) — schlägt nie fehl.",
     "en": "Library API mirrors lci-dfu: compute_kaa(commodity, country) — never fails."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 4,
      "label": {
       "de": "Stufen, jede mit eigenem gemessenem Anker und ausgewiesener Stufe",
       "en": "stages, each with its own measured anchor and disclosed tier"
      }
     },
     {
      "n": 83,
      "label": {
       "de": "committete Warenspezifikationen (79 Dashboard-Waren, 76 review-gestempelt)",
       "en": "committed commodity specs (79 dashboard commodities, 76 review-stamped)"
      }
     },
     {
      "n": 138,
      "label": {
       "de": "Tests",
       "en": "tests"
      }
     }
    ],
    "items": [
     {
      "de": "Handelsdrehscheiben werden rekursiv zu echten Produzenten aufgelöst — sonst der grösste Einzelfehler der Engine.",
      "en": "Trade hubs are resolved recursively to real producers — otherwise the engine's largest single error."
     },
     {
      "de": "Investitionsgüter und B2B-Dienste sind als Untergrenze ausgewiesen, nicht still weggelassen.",
      "en": "Capital goods and B2B services are disclosed as a lower bound, not silently omitted."
     }
    ]
   }
  },
  "lci-score-cache": {
   "kicker": {
    "de": "Vertraulicher Vordergrund als Systemprozess",
    "en": "Confidential foreground as system processes"
   },
   "slide1": {
    "title": {
     "de": "Den Fussabdruck veröffentlichen, das Rezept behalten",
     "en": "Publish the footprint, keep the recipe"
    },
    "body": {
     "de": "Markenprodukte unter NDA werden aus dem öffentlichen Paket zurückgehalten — was 1'344 gespeicherte Automatchings auf 17 Produkten still brach. Die branchenübliche Lösung: den vollständigen Elementarfluss-Vektor ohne Technosphären-Struktur veröffentlichen. Jede Methode bewertet ihn exakt; die Zusammensetzung lässt sich nicht rekonstruieren.",
     "en": "Brand products under NDA are withheld from the public bundle — which silently broke 1,344 stored automatchings on 17 products. The industry-standard resolution: publish the complete elementary-flow vector with no technosphere structure. Every method scores it exactly; the composition cannot be reconstructed."
    },
    "footnote": {
     "de": "Operator-Entscheid 02.09.2026. Vektoren im geschützten Basin-Projekt abgeleitet und beim Build gegen ihren gepinnten Hash verifiziert.",
     "en": "Operator ruling 2026-09-02. Vectors derived in the gated basin project, verified against their pinned sha at build time."
    },
    "stats": [
     {
      "num": "17",
      "label": {
       "de": "Produkte, 1'344 Automatchings, lösen wieder auf",
       "en": "products, 1,344 automatchings, resolve again"
      }
     },
     {
      "num": "0",
      "label": {
       "de": "Technosphären-Kanten in einem veröffentlichten Vektor — nichts zu zerlegen",
       "en": "technosphere edges in a published vector — nothing to decompose"
      }
     },
     {
      "num": "7",
      "label": {
       "de": "Fail-closed-Verweigerungsgates beim Build",
       "en": "fail-closed refusal gates at build"
      }
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Kein pauschaler Emissionsfaktor",
     "en": "Not a lumped emission factor"
    },
    "body": {
     "de": "Die 68 alten EDB-Pauschalen speichern eine charakterisierte CO₂e-Summe als einzelnen fossilen CO₂-Fluss — nur unter GWP100 korrekt. Ein Cache-Knoten trägt den vollen Vektor, eine deklarierte Klasse, eine verifizierte Ableitung, ein Band auf jedem Fluss und eine Region auf jedem Wasserfluss (das AWARE-Gate).",
     "en": "The 68 legacy EDB lumps store one characterised CO₂e total as a single fossil-CO₂ flow — correct under GWP100 only. A cache node carries the full vector, a declared class, a verified derivation, a band on every flow and a region on every water flow (the AWARE gate)."
    },
    "footnote": {
     "de": "match_type confidential_system_process, bafu_key null, Offenlegung via omitted_flows.",
     "en": "match_type confidential_system_process, bafu_key null, disclosure via omitted_flows."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 68,
      "label": {
       "de": "alte Pauschalfaktoren, die dieses Muster NICHT ist — volle Vektoren stattdessen",
       "en": "legacy lumped factors this pattern is NOT — full vectors instead"
      }
     },
     {
      "n": 2,
      "label": {
       "de": "geprüfte Hashes: Basis-Registry-SHA + Vektor-SHA-256",
       "en": "hashes checked: base registry sha + vector sha256"
      }
     },
     {
      "n": 0,
      "label": {
       "de": "Vektoren bisher geliefert — per Konstruktion leer bis zur ersten Basin-Lieferung",
       "en": "vectors delivered yet — empty by construction until the first basin delivery"
      }
     }
    ],
    "items": [
     {
      "de": "Produktidentitäten liegen nur im geschützten Projekt; dieses Repo ist öffentlich.",
      "en": "Product identities live only in the gated project; this repo is public."
     },
     {
      "de": "Der veröffentlichte Vektor ist per Konstruktion nicht vertraulich — das ist der Sinn eines Systemprozesses.",
      "en": "The published vector is by construction non-confidential — that is the point of a system process."
     }
    ]
   }
  },
  "lci-capital-goods": {
   "kicker": {
    "de": "Investitionsgüter & Infrastruktur — Framework",
    "en": "Capital goods & infrastructure — framework"
   },
   "slide1": {
    "title": {
     "de": "Die teuersten Lücken pro Einheit haben jetzt einen Besitzer",
     "en": "The highest per-unit gaps now have an owner"
    },
    "body": {
     "de": "Besitzt ISIC 25/27/28/29/30/31/33/42/43/45 im Referenzkatalog: 1'656 Hintergrund-Aktivitäten ohne getreuen offenen Ersatz — Maschinen, Fahrzeuge, Metallwaren, Bauprojekte. Ganz oben im gesamten Backlog: die Kältemaschine mit R134a (~3'783 kg CO₂e je Einheit) und die Entsorgung ausgedienter Trams.",
     "en": "Owns ISIC 25/27/28/29/30/31/33/42/43/45 in the reference catalog: 1,656 background activities with no faithful open replacement — machinery, vehicles, fabricated metal, utility construction. Rank 1 of the whole backlog: refrigeration machine production with R134a (~3,783 kg CO₂e per unit) and end-of-life treatment of trams."
    },
    "footnote": {
     "de": "Angrenzende Teilabdeckung heute: lci-transport (Schienen-/Schiffsinfrastruktur), lci-storage (Silos, Ställe), lci-fishing (Gerät).",
     "en": "Adjacent partial coverage today: lci-transport (rail/ship infrastructure), lci-storage (silos, barns), lci-fishing (gear)."
    },
    "stats": [
     {
      "num": {
       "de": "1'656",
       "en": "1,656"
      },
      "label": {
       "de": "offene Lücken-Aktivitäten, per ISIC-Zuordnung hierhin geroutet",
       "en": "open gap activities routed here by ISIC ownership"
      }
     },
     {
      "num": {
       "de": "~3'783 kg",
       "en": "~3,783 kg"
      },
      "label": {
       "de": "CO₂e je Kältemaschine (R134a) — Rang 1 im gesamten Backlog",
       "en": "CO₂e per refrigeration machine (R134a) — rank 1 in the whole backlog"
      }
     },
     {
      "num": "2",
      "label": {
       "de": "erste Einträge; Prozess-Inventare werden in das Paket hineingeschrieben",
       "en": "first entries; process inventories are authored into the package"
      }
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Prioritätsziele, nicht Stellvertreter",
     "en": "Priority targets, not proxies"
    },
    "body": {
     "de": "Eine flache Proxy-Aktivität kann Öfen, Haushaltsgeräte, Fahrzeugteile und Bauprojekte nicht gleichzeitig darstellen. Jeder Eintrag wird als Prozess-Inventar an BAFU/UVEK-Ankern gebaut, match_type capital_goods_lci, mit sediment-Identität, damit ein Versionssprung der Referenzdatenbank das Mapping nicht verwaist.",
     "en": "One flat proxy activity cannot represent ovens, domestic appliances, motor-vehicle parts and utility construction at once. Every entry is built as a process inventory on BAFU/UVEK anchors, match_type capital_goods_lci, with sediment identity so a reference-database version bump does not orphan the mapping."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 10,
      "label": {
       "de": "ISIC-rev.4-Abteilungen im Besitz (25, 27–31, 33, 42, 43, 45)",
       "en": "ISIC rev.4 divisions owned (25, 27–31, 33, 42, 43, 45)"
      }
     },
     {
      "n": 7,
      "label": {
       "de": "benannte Prioritätsziele: Kältemaschine, Tram-Entsorgung, Metallwaren, Öfen, Geräte, Fahrzeugteile, Bauprojekte",
       "en": "named priority targets: refrigeration machine, tram end-of-life, fabricated metal, ovens, appliances, vehicle parts, utility construction"
      }
     },
     {
      "n": 2,
      "label": {
       "de": "Vertrags-Smoke-Tests, die jeden Eintrag gegen den Tributär-Ausgabevertrag prüfen",
       "en": "contract smoke tests checking every entry against the tributary output contract"
      }
     }
    ],
    "items": [
     {
      "de": "ISIC-first-Routing: neue Lücken in diesen Abteilungen landen automatisch hier.",
      "en": "ISIC-first routing: new gaps in these divisions land here automatically."
     },
     {
      "de": "Spezifikation: lci-deecoinvent/docs/new_tributary_capital_goods.md.",
      "en": "Spec: lci-deecoinvent/docs/new_tributary_capital_goods.md."
     }
    ],
    "footnote": {
     "de": "Gerüst aus dem lci-deecoinvent-Katalogdurchlauf vom 22.07.2026: 25'412 Aktivitäten des Referenzkatalogs nach ISIC rev.4 klassifiziert, 17'561 ohne getreuen offenen Ersatz. Identität über sediment, nie über UUIDs.",
     "en": "Scaffolded by the lci-deecoinvent full-catalog pass of 2026-07-22: 25,412 reference-catalog activities classified by ISIC rev.4, 17,561 without a faithful open replacement. Identity via sediment, never via UUIDs."
    }
   }
  },
  "lci-chemicals": {
   "kicker": {
    "de": "Industriechemikalien — Framework",
    "en": "Industrial chemicals — framework"
   },
   "slide1": {
    "title": {
     "de": "Die grösste unbesetzte Domäne im Backlog",
     "en": "The single largest unowned domain in the backlog"
    },
    "body": {
     "de": "Besitzt ISIC 20/21/22: organische und anorganische Grundchemikalien, Kunststoffe und Polymere, die bisher auf strukturell falsche BAFU-Stellvertreter fielen — 1'864 offene Lücken-Aktivitäten. Prioritäten: Wasserstoff-Kompression (~11,5 kg CO₂e/kg), Glycin, Chromtrioxid, Acryl-Dispersionen, Glycerin, Ethanol, Methansulfonsäure, Soda.",
     "en": "Owns ISIC 20/21/22: organic and inorganic basic chemicals, plastics and polymers that used to fall through to structurally wrong BAFU proxies — 1,864 open gap activities. Priorities: hydrogen compression (~11.5 kg CO₂e/kg), glycine, chromium trioxide, acrylic dispersions, glycerine, ethanol, methylsulfonic acid, soda ash."
    },
    "footnote": {
     "de": "Angrenzend: edb_bafu.matching, lci-fermentation (Bio-Routen), lci-fertiliser (Agrarchemie).",
     "en": "Adjacent: edb_bafu.matching, lci-fermentation (bio-routes), lci-fertiliser (agri chemicals)."
    },
    "stats": [
     {
      "num": {
       "de": "1'864",
       "en": "1,864"
      },
      "label": {
       "de": "offene Lücken-Aktivitäten — die grösste unbesetzte Domäne",
       "en": "open gap activities — the largest unowned domain"
      }
     },
     {
      "num": "~11,5 kg",
      "label": {
       "de": "CO₂e/kg Wasserstoff-Kompression — erstes Ziel",
       "en": "CO₂e/kg hydrogen compression — first target"
      }
     },
     {
      "num": "8",
      "label": {
       "de": "benannte Prioritätsziele aus dem gerankten Backlog",
       "en": "named priority targets from the ranked backlog"
      }
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Stellvertreter werden ersetzt, nicht umbenannt",
     "en": "Proxies get replaced, not relabelled"
    },
    "body": {
     "de": "Ein strukturell falscher Stellvertreter (Chemikalie X auf Chemikalie Y) ist kein Mapping, sondern ein verstecktes Modell. Dieses Framework baut Prozess-Inventare je Syntheseroute an BAFU/UVEK-Ankern, match_type chemicals_lci_tributary, sediment-Identität statt UUIDs.",
     "en": "A structurally wrong proxy (chemical X standing in for chemical Y) is not a mapping, it is a hidden model. This framework authors process inventories per synthesis route on BAFU/UVEK anchors, match_type chemicals_lci_tributary, sediment identity instead of UUIDs."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 3,
      "label": {
       "de": "ISIC-Abteilungen: 20 Chemikalien, 21 Pharma, 22 Gummi & Kunststoff",
       "en": "ISIC divisions: 20 chemicals, 21 pharmaceuticals, 22 rubber & plastics"
      }
     },
     {
      "n": 2,
      "label": {
       "de": "erste Einträge im Mapping",
       "en": "first entries in the mapping"
      }
     },
     {
      "n": 2,
      "label": {
       "de": "Vertrags-Smoke-Tests",
       "en": "contract smoke tests"
      }
     }
    ],
    "items": [
     {
      "de": "Jeder Eintrag: Ausgabevertrag, Unsicherheitsband auf jedem Biosphärenfluss, Provenienz.",
      "en": "Every entry: output contract, uncertainty band on every biosphere flow, provenance."
     },
     {
      "de": "Leer per Design, bis Inventare geschrieben sind — kein Platzhalter täuscht Abdeckung vor.",
      "en": "Empty by design until inventories are authored — no placeholder fakes coverage."
     }
    ],
    "footnote": {
     "de": "Gerüst aus dem lci-deecoinvent-Katalogdurchlauf vom 22.07.2026: 25'412 Aktivitäten des Referenzkatalogs nach ISIC rev.4 klassifiziert, 17'561 ohne getreuen offenen Ersatz. Identität über sediment, nie über UUIDs.",
     "en": "Scaffolded by the lci-deecoinvent full-catalog pass of 2026-07-22: 25,412 reference-catalog activities classified by ISIC rev.4, 17,561 without a faithful open replacement. Identity via sediment, never via UUIDs."
    }
   }
  },
  "lci-construction-materials": {
   "kicker": {
    "de": "Baustoffe — Framework mit erstem Inventar",
    "en": "Construction materials — framework with a first inventory"
   },
   "slide1": {
    "title": {
     "de": "761 Lücken, zwei Drittel davon Zement und Beton",
     "en": "761 gaps, two thirds of them cement and concrete"
    },
    "body": {
     "de": "Besitzt ISIC 23/41/8: 602 Lücken in nichtmetallischen Mineralprodukten (Zement, Kalk, Gips, Glas, Ton), 84 im Hochbau, 75 im Steinbruch. 483 der 761 (63,5 %) sind Zement und Betonwaren. Ein einzelner Zement-Proxy kann das nicht tragen: EN-197-1-Zemente unterscheiden sich im Klinkeranteil um rund den Faktor zwei — und Klinker-Kalzination dominiert das CO₂, nicht der Brennstoff.",
     "en": "Owns ISIC 23/41/8: 602 gaps in non-metallic mineral products (cement, lime, plaster, glass, clay), 84 in building construction, 75 in quarrying. 483 of 761 (63.5%) are cement and concrete articles. A single cement proxy cannot absorb that: EN 197-1 cement types differ in clinker ratio by roughly a factor of two — and clinker calcination dominates CO₂, not fuel."
    },
    "footnote": {
     "de": "Abgrenzung: lci-packaging deckt bereits 53 verpackungsnahe Baumaterialien (Paletten, Lagerhüllen) — nicht diesen Backlog.",
     "en": "Boundary: lci-packaging already covers 53 packaging-adjacent construction materials (pallets, warehouse shells) — not this backlog."
    },
    "stats": [
     {
      "num": "761",
      "label": {
       "de": "Lücken-Aktivitäten (602 · 84 · 75 nach Abteilung)",
       "en": "gap activities (602 · 84 · 75 by division)"
      }
     },
     {
      "num": "63,5 %",
      "label": {
       "de": "davon Zement- und Betonwaren — dort beginnt das Authoring",
       "en": "of them cement and concrete articles — where authoring starts"
      }
     },
     {
      "num": "1 m³",
      "label": {
       "de": "Transportbeton CH: das erste geschriebene, prozessbasierte Inventar",
       "en": "Swiss ready-mix concrete: the first authored process-based inventory"
      }
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Deklarative Kompositionen statt handgeschriebener Blätter",
     "en": "Declarative compositions instead of hand-written leaves"
    },
    "body": {
     "de": "Ein Rezeptmodul deklariert seine BAFU/UVEK-Technosphärenkanten und Ressourcenkorrekturen als typisierte Datenklassen; compose_entry() leitet den Mapping-Eintrag samt Komposit-GWP100 als Summe von Menge × BAFU-GWP ab. Nichts steht auf der Zeile, was die Austausche nicht rechnen — und das Register verweigert fehlerhafte Registrierungen.",
     "en": "A recipe module declares its BAFU/UVEK technosphere edges and resource corrections as typed dataclasses; compose_entry() derives the mapping entry, including the composite GWP100, as the sum of amount × BAFU GWP. Nothing is asserted on the row that the exchanges do not compute — and the registry refuses malformed registrations."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 22,
      "label": {
       "de": "Tests in 2 Dateien (21 grün, 1 übersprungen ohne optionales Sibling)",
       "en": "tests across 2 files (21 pass, 1 skips without the optional sibling)"
      }
     },
     {
      "n": 483,
      "label": {
       "de": "Zement-/Beton-Lücken, die eine Komposition pro Zementtyp brauchen",
       "en": "cement/concrete gaps that need one composition per cement type"
      }
     },
     {
      "n": 1,
      "label": {
       "de": "geschriebenes Inventar heute — der Rest ist Gerüst, nicht Abdeckung",
       "en": "authored inventory today — the rest is scaffold, not coverage"
      }
     }
    ],
    "items": [
     {
      "de": "Feuerfestprodukte und Steinbruch sind eigene Mineralogie bzw. Prozessschritte — kein Zement-Proxy.",
      "en": "Refractories and quarrying are different mineralogy and unit operations — no cement proxy."
     },
     {
      "de": "Eine Mengenänderung ändert das Komposit-GWP proportional — prüfbar an der Zeile.",
      "en": "Changing a component amount changes the composite GWP proportionally — checkable on the row."
     }
    ],
    "footnote": {
     "de": "Gerüst aus dem lci-deecoinvent-Katalogdurchlauf vom 22.07.2026: 25'412 Aktivitäten des Referenzkatalogs nach ISIC rev.4 klassifiziert, 17'561 ohne getreuen offenen Ersatz. Identität über sediment, nie über UUIDs.",
     "en": "Scaffolded by the lci-deecoinvent full-catalog pass of 2026-07-22: 25,412 reference-catalog activities classified by ISIC rev.4, 17,561 without a faithful open replacement. Identity via sediment, never via UUIDs."
    }
   }
  },
  "lci-electronics": {
   "kicker": {
    "de": "Elektronik & ICT — Framework",
    "en": "Electronics & ICT — framework"
   },
   "slide1": {
    "title": {
     "de": "232 Lücken, 82 Referenzprodukte, kein Besitzer bisher",
     "en": "232 gaps, 82 reference products, no owner until now"
    },
    "body": {
     "de": "Besitzt ISIC 26/61/62: Halbleiter, Leiterplatten, Telekom- und Gerätebetrieb — 232 Lücken-Aktivitäten (1,3 % des Backlogs). Heute nutzt kein reales Inventar eine davon, aber das Loch ist strukturell: Wafer-Energieintensität, SMD vs. THT, bleifreies Lot und Nutzungsstrom variieren so stark, dass eine flache Proxy-Aktivität sie nicht darstellen kann.",
     "en": "Owns ISIC 26/61/62: semiconductors, printed wiring boards, telecom and device operation — 232 gap activities (1.3% of the backlog). No real inventory uses one today, but the hole is structural: wafer-fab energy intensity, surface-mount vs through-hole, lead-free solder and use-phase electricity vary too much for a flat proxy."
    },
    "footnote": {
     "de": "Gerüst, noch kein befülltes Tributär: Mapping absichtlich leer, Vertrag und Build-Pipeline erzwungen.",
     "en": "Scaffold, not yet a populated tributary: mapping intentionally empty, contract and build pipeline enforced."
    },
    "stats": [
     {
      "num": "232",
      "label": {
       "de": "Lücken-Aktivitäten über 82 Referenzprodukte",
       "en": "gap activities across 82 reference products"
      }
     },
     {
      "num": "0",
      "label": {
       "de": "davon heute von einem realen Inventar genutzt — Exposition liegt in der Zukunft",
       "en": "of them used by a real inventory today — exposure lies in the future"
      }
     },
     {
      "num": "3",
      "label": {
       "de": "ISIC-Abteilungen: 26 Elektronik, 61 Telekom, 62 IT-Dienste",
       "en": "ISIC divisions: 26 electronics, 61 telecom, 62 IT services"
      }
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Strom kommt aus lci-electricity, nie als fester Faktor",
     "en": "Electricity resolves through lci-electricity, never as a fixed factor"
    },
    "body": {
     "de": "Der Gerätebetrieb bindet an die periodenspezifischen, länderaufgelösten Netzmixe von lci-electricity statt an eine eingebrannte Zahl. Charakterisierung bleibt im Workbench-Multi-Methoden-LCA — Trennung der Zuständigkeiten wie bei lci-electricity.",
     "en": "Device operation binds to lci-electricity's period-specific, country-resolved grid mixes instead of a baked-in number. Characterisation stays in the workbench's multi-method LCA — the same separation of concerns as lci-electricity."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 82,
      "label": {
       "de": "Referenzprodukte im Lückenverzeichnis (IC, Leiterplatte, Internetzugang …)",
       "en": "reference products in the gap list (IC, printed wiring board, internet access …)"
      }
     },
     {
      "n": 1,
      "label": {
       "de": "Vertragstest, der jeden künftigen Eintrag prüft",
       "en": "contract test checking every future entry"
      }
     },
     {
      "n": 0,
      "label": {
       "de": "Einträge heute — leer per Design",
       "en": "entries today — empty by design"
      }
     }
    ],
    "items": [
     {
      "de": "Sediment-Block auf jedem Eintrag: Intent + GS1/CPC-Term + GADM-Ort.",
      "en": "Sediment block on every entry: intent + GS1/CPC term + GADM location."
     },
     {
      "de": "Methodenbericht folgt mit den ersten Inventaren — nicht vorher.",
      "en": "Methodology report follows the first inventories — not before."
     }
    ],
    "footnote": {
     "de": "Gerüst aus dem lci-deecoinvent-Katalogdurchlauf vom 22.07.2026: 25'412 Aktivitäten des Referenzkatalogs nach ISIC rev.4 klassifiziert, 17'561 ohne getreuen offenen Ersatz. Identität über sediment, nie über UUIDs.",
     "en": "Scaffolded by the lci-deecoinvent full-catalog pass of 2026-07-22: 25,412 reference-catalog activities classified by ISIC rev.4, 17,561 without a faithful open replacement. Identity via sediment, never via UUIDs."
    }
   }
  },
  "lci-forestry-wood": {
   "kicker": {
    "de": "Forst & Holzprodukte — Framework",
    "en": "Forestry & wood products — framework"
   },
   "slide1": {
    "title": {
     "de": "750 Lücken, 29 Standorte, ein Proxy reicht nicht",
     "en": "750 gaps, 29 locations, one proxy will not do"
    },
    "body": {
     "de": "Besitzt ISIC 16/2: 750 Lücken-Aktivitäten (4,3 % des Backlogs) — 421 Sägewerk, 90 Furnier und Platten, 86 Holzeinschlag, 84 Waldbau. Ein einzelner «Schnittholz»-Proxy versagt: ein Dutzend Arten und Bewirtschaftungsregime, Koppelprodukte mit eigenen Märkten, Plattenbinder mit eigener Pressenergie — und 29 Standorte von CH bis zu 13 brasilianischen Bundesstaaten.",
     "en": "Owns ISIC 16/2: 750 gap activities (4.3% of the backlog) — 421 sawmilling, 90 veneer and panels, 86 logging, 84 silviculture. A single «sawnwood» proxy fails: a dozen species and management regimes, co-products with their own markets, panel binders with their own press energy — and 29 locations from CH to 13 Brazilian states."
    },
    "footnote": {
     "de": "Heute nutzt genau eine reale Kette eine dieser Lücken (Holzschutz, Sprühtunnel, GLO) — als Nebenprodukt des EDB↔BAFU-Mappings.",
     "en": "Exactly one real chain uses one of these gaps today (wood preservation, spray tunnel, GLO) — as a byproduct of the EDB↔BAFU mapping."
    },
    "stats": [
     {
      "num": "750",
      "label": {
       "de": "Lücken-Aktivitäten (4,3 % des Gesamt-Backlogs)",
       "en": "gap activities (4.3% of the total backlog)"
      }
     },
     {
      "num": "421",
      "label": {
       "de": "davon Sägewerk und Hobelwerk — 56 % des Umfangs",
       "en": "of them sawmilling and planing — 56% of scope"
      }
     },
     {
      "num": "29",
      "label": {
       "de": "Referenz-Standorte inkl. 13 brasilianischer Bundesstaaten",
       "en": "reference locations incl. 13 Brazilian states"
      }
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Massenbilanz statt Einprodukt-Inventar",
     "en": "Mass balance instead of single-product inventories"
    },
    "body": {
     "de": "Sägewerke trennen Hauptprodukt (Schnittholz) von Koppelprodukten (Rinde, Hackschnitzel, Reste) mit eigenen nachgelagerten Märkten — aus einem Einprodukt-Inventar lässt sich das nicht schneiden, ohne die Massenbilanz zu brechen. build_entry() erzwingt den vollen Vertrag beim Konstruieren; test_every_authored_entry_conforms prüft ihn erneut.",
     "en": "Sawmills separate the primary product (sawnwood) from co-products (bark, chips, residues) that carry their own downstream markets — you cannot cut that from a single-product inventory without breaking mass balance. build_entry() enforces the full contract at construction; test_every_authored_entry_conforms re-checks it."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 7,
      "label": {
       "de": "ISIC-Klassen im Umfang (0210, 0220, 0230, 1610, 1621, 1622, 162)",
       "en": "ISIC classes in scope (0210, 0220, 0230, 1610, 1621, 1622, 162)"
      }
     },
     {
      "n": 13,
      "label": {
       "de": "brasilianische Sub-Regionen, die ein globaler Default nicht abbilden kann",
       "en": "Brazilian sub-regions a single global default cannot represent"
      }
     },
     {
      "n": 0,
      "label": {
       "de": "Inventare geschrieben — Mapping enthält {} per Design",
       "en": "inventories authored — mapping holds {} by design"
      }
     }
    ],
    "items": [
     {
      "de": "Erste Ziele: die volumenstärksten Sägewerk- und Waldbau-Aktivitäten.",
      "en": "First targets: the highest-volume sawmilling and silviculture activities."
     },
     {
      "de": "Kohlenstoffbilanzen hängen an regionalen Wachstumsraten und Landnutzungsgeschichte — Standort ist Pflicht.",
      "en": "Carbon balances depend on regional growth rates and land-use history — location is mandatory."
     }
    ],
    "footnote": {
     "de": "Gerüst aus dem lci-deecoinvent-Katalogdurchlauf vom 22.07.2026: 25'412 Aktivitäten des Referenzkatalogs nach ISIC rev.4 klassifiziert, 17'561 ohne getreuen offenen Ersatz. Identität über sediment, nie über UUIDs.",
     "en": "Scaffolded by the lci-deecoinvent full-catalog pass of 2026-07-22: 25,412 reference-catalog activities classified by ISIC rev.4, 17,561 without a faithful open replacement. Identity via sediment, never via UUIDs."
    }
   }
  },
  "lci-fuels": {
   "kicker": {
    "de": "Brennstoffe & Raffination — Framework",
    "en": "Fuels & refining — framework"
   },
   "slide1": {
    "title": {
     "de": "Förderung und Raffination: 568 Lücken, 95 Produkte",
     "en": "Extraction and refining: 568 gaps, 95 products"
    },
    "body": {
     "de": "Besitzt ISIC 19/6/9/5: Rohöl- und Gasförderung, Raffination, Kokerei, Kohlebergbau — 568 Lücken-Aktivitäten (3,2 % des Backlogs). Der offensichtliche Kurzschluss, jedes Raffinerieprodukt auf einen generischen «Raffineriebetrieb» zu legen, würde Grundöl, Petrolkoks, Wachs, Schwefel und C3/C4-Gemische mit Ausbeuten verwechseln, die stärker streuen als der Proxy-Fehler.",
     "en": "Owns ISIC 19/6/9/5: crude oil and gas extraction, refining, coke ovens, coal mining — 568 gap activities (3.2% of the backlog). The obvious shortcut, mapping every refinery product to a generic «refinery operation», would misrepresent base oil, petroleum coke, wax, sulfur and C3/C4 mixtures whose yields vary by more than the proxy error."
    },
    "footnote": {
     "de": "Abgegrenzt von lci-fuel-combustion (direkte Verbrennungsfaktoren) und lci-electricity (Netzmixe): hier nur die vorgelagerte Förderung und Raffination.",
     "en": "Distinct from lci-fuel-combustion (direct combustion factors) and lci-electricity (grid mixes): only the upstream extraction and refining live here."
    },
    "stats": [
     {
      "num": "568",
      "label": {
       "de": "Lücken-Aktivitäten (3,2 % des Backlogs)",
       "en": "gap activities (3.2% of the backlog)"
      }
     },
     {
      "num": "95",
      "label": {
       "de": "verschiedene Referenzprodukte im Lückenverzeichnis",
       "en": "distinct reference products in the gap list"
      }
     },
     {
      "num": "0",
      "label": {
       "de": "davon heute von einem realen Inventar genutzt",
       "en": "of them used by a real inventory today"
      }
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Treiber, die ein Proxy wegmittelt",
     "en": "Drivers a proxy would average away"
    },
    "body": {
     "de": "Raffineriekonfiguration (nur Fraktionierung vs. Cracken/Reformieren), Rohöl-Slate, Kohlerang und Abbaumethode (Tagebau vs. Untertage mit flüchtigem Methan), Abfackeln und Entlüften am Förderort — jeder Eintrag wird als Gate-to-Gate-Prozessinventar je Referenzprodukt gebaut.",
     "en": "Refinery configuration (fractionation only vs cracking/reforming), crude slate, coal rank and mining method (surface vs underground with fugitive methane), flaring and venting at the extraction site — every entry is built as a gate-to-gate process inventory per reference product."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 4,
      "label": {
       "de": "ISIC-Abteilungen: 19 Raffination, 6 Öl & Gas, 9 Bergbau-Dienste, 5 Kohle",
       "en": "ISIC divisions: 19 refining, 6 oil & gas, 9 mining services, 5 coal"
      }
     },
     {
      "n": 502,
      "label": {
       "de": "Lücken mit auflösbarer ISIC-Klasse im Umfang",
       "en": "gaps with a resolvable ISIC class in scope"
      }
     },
     {
      "n": 0,
      "label": {
       "de": "Einträge heute — leer per Design",
       "en": "entries today — empty by design"
      }
     }
    ],
    "items": [
     {
      "de": "Strom- und Transportbedarf lösen über lci-electricity und lci-transport auf, nie als fester Faktor.",
      "en": "Electricity and transport demand resolve through lci-electricity and lci-transport, never as a fixed factor."
     },
     {
      "de": "Charakterisierung bleibt im Workbench-Multi-Methoden-LCA.",
      "en": "Characterisation stays in the workbench's multi-method LCA."
     }
    ],
    "footnote": {
     "de": "Gerüst aus dem lci-deecoinvent-Katalogdurchlauf vom 22.07.2026: 25'412 Aktivitäten des Referenzkatalogs nach ISIC rev.4 klassifiziert, 17'561 ohne getreuen offenen Ersatz. Identität über sediment, nie über UUIDs.",
     "en": "Scaffolded by the lci-deecoinvent full-catalog pass of 2026-07-22: 25,412 reference-catalog activities classified by ISIC rev.4, 17,561 without a faithful open replacement. Identity via sediment, never via UUIDs."
    }
   }
  },
  "lci-pulp-paper": {
   "kicker": {
    "de": "Zellstoff, Papier & Karton — Framework",
    "en": "Pulp, paper & board — framework"
   },
   "slide1": {
    "title": {
     "de": "156 Lücken zwischen Wald und Verpackung",
     "en": "156 gaps between forest and packaging"
    },
    "body": {
     "de": "Besitzt ISIC 17/18: Sulfat- und Sulfitzellstoff, grafische und Verpackungspapiere, Karton, Tissue, Druckdienste — 156 Lücken-Aktivitäten, die vorher nirgendwohin geroutet wurden. Klar abgegrenzt von lci-packaging, das die Verarbeitung und das Lebensende der Verpackung besitzt: hier geht es um die Substratherstellung selbst.",
     "en": "Owns ISIC 17/18: kraft and sulfite pulp, graphic and packaging papers, board, tissue, printing services — 156 gap activities that were routed nowhere before. Clearly separated from lci-packaging, which owns packaging conversion and end-of-life: this is about the substrate manufacture itself."
    },
    "footnote": {
     "de": "Vorgesehene funktionelle Einheit: 1 kg Zellstoff/Papier/Karton; je gedruckter Einheit für Druckdienste.",
     "en": "Intended functional unit: 1 kg pulp/paper/board; per printed unit for printing services."
    },
    "stats": [
     {
      "num": "156",
      "label": {
       "de": "Lücken-Aktivitäten, identifiziert und hierhin geroutet",
       "en": "gap activities identified and routed here"
      }
     },
     {
      "num": "2",
      "label": {
       "de": "ISIC-Abteilungen: 17 Papier, 18 Druck",
       "en": "ISIC divisions: 17 paper, 18 printing"
      }
     },
     {
      "num": "0",
      "label": {
       "de": "geschriebene Inventare — reines Vertrags-Framework",
       "en": "inventories authored — a contract-only framework"
      }
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Der Vertrag steht, bevor die Daten kommen",
     "en": "The contract is in place before the data arrives"
    },
    "body": {
     "de": "Ausgabeschema, Identitätskonvention (sediment: CPC-Term, GADM-Ort, ISO-8601-Zeit) und Modul-Layout sind definiert und von der Vertrags-Testsuite geprüft — auch wenn build_mapping() heute {} liefert. Erste Ziele sind die aktivitätsstärksten Referenzprodukte beider Abteilungen.",
     "en": "Output schema, identity convention (sediment: CPC term, GADM location, ISO 8601 time) and module layout are defined and exercised by the contract test suite — even though build_mapping() returns {} today. First targets are the highest-activity-count reference products of both divisions."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 6,
      "label": {
       "de": "Vertreter-Aktivitäten: Sulfat-, Sulfitzellstoff, grafisches Papier, Verpackungspapier, Wellpappenrohpapier, Tissue",
       "en": "representative activities: kraft pulp, sulfite pulp, graphic paper, packaging paper, containerboard, tissue"
      }
     },
     {
      "n": 1,
      "label": {
       "de": "Vertragstest",
       "en": "contract test"
      }
     },
     {
      "n": 0,
      "label": {
       "de": "Einträge heute — leer per Design",
       "en": "entries today — empty by design"
      }
     }
    ],
    "items": [
     {
      "de": "Gate-to-Gate-Umfang wie die Geschwister-Tributäre.",
      "en": "Gate-to-gate scope, matching the sibling tributaries."
     },
     {
      "de": "Sediment-Schema einmal workspace-weit definiert (edb_bafu.sediment), hier nicht neu implementiert.",
      "en": "Sediment schema defined once workspace-wide (edb_bafu.sediment), not re-implemented here."
     }
    ],
    "footnote": {
     "de": "Gerüst aus dem lci-deecoinvent-Katalogdurchlauf vom 22.07.2026: 25'412 Aktivitäten des Referenzkatalogs nach ISIC rev.4 klassifiziert, 17'561 ohne getreuen offenen Ersatz. Identität über sediment, nie über UUIDs.",
     "en": "Scaffolded by the lci-deecoinvent full-catalog pass of 2026-07-22: 25,412 reference-catalog activities classified by ISIC rev.4, 17,561 without a faithful open replacement. Identity via sediment, never via UUIDs."
    }
   }
  },
  "lci-water-supply": {
   "kicker": {
    "de": "Wasserversorgung — Framework",
    "en": "Water supply — framework"
   },
   "slide1": {
    "title": {
     "de": "Die Lücke zwischen Abwasser und Bewässerung",
     "en": "The gap between wastewater and irrigation"
    },
    "body": {
     "de": "Besitzt ISIC 36: Wassergewinnung, -aufbereitung und -versorgung — 7 Lücken-Aktivitäten in drei Referenzprodukten: Meerwasser-Umkehrosmose-Module, Ultrafiltrationsmodule, gesammeltes Regenwasser. Klein nach Zahl, aber echt unbesetzt: lci-waste-treatment deckt das Abwasser danach, lci-irrigation die landwirtschaftliche Zufuhr — keines die Aufbereitung davor.",
     "en": "Owns ISIC 36: water collection, treatment and supply — 7 gap activities across three reference products: seawater reverse-osmosis modules, ultrafiltration modules, harvested rainwater. Small by count, but genuinely unowned: lci-waste-treatment covers effluent afterwards, lci-irrigation agricultural delivery — neither the treatment before."
    },
    "footnote": {
     "de": "Gerüst, noch kein befülltes Tributär: Mapping absichtlich leer.",
     "en": "Scaffold, not yet a populated tributary: mapping intentionally empty."
    },
    "stats": [
     {
      "num": "7",
      "label": {
       "de": "Lücken-Aktivitäten in ISIC 36",
       "en": "gap activities in ISIC 36"
      }
     },
     {
      "num": "3",
      "label": {
       "de": "Referenzprodukte: SWRO-Membran, UF-Membran, Regenwasser",
       "en": "reference products: SWRO membrane, UF membrane, rainwater"
      }
     },
     {
      "num": "0",
      "label": {
       "de": "davon heute von einem realen Inventar genutzt",
       "en": "of them used by a real inventory today"
      }
     }
    ]
   },
   "slide2": {
    "title": {
     "de": "Warum kein «Wasseraufbereitungs-Gerät»-Proxy",
     "en": "Why not a «water treatment equipment» proxy"
    },
    "body": {
     "de": "Spiralgewickelte Polymermembranen (Giessen und Vergiessen) und Hohlfasermembranen (Extrusion) sind andere Produktionsrouten mit anderen funktionellen Einheiten — Membranfläche für Umkehrosmose, Stückzahl für Ultrafiltration. Nur ein Inventar je Referenzprodukt bewahrt die Unterscheidung, die eine nachgelagerte Entsalzungs- oder Filtrationsbilanz braucht.",
     "en": "Spiral-wound polymer membranes (casting and potting) and hollow-fibre membranes (extrusion) are different production routes with different functional units — membrane area for reverse osmosis, discrete units for ultrafiltration. Only a per-reference-product inventory preserves the distinction a downstream desalination or filtration inventory needs."
    },
    "renderer": "bigstat",
    "figures": [
     {
      "n": 1,
      "label": {
       "de": "ISIC-Abteilung (36) — neue Lücken routen automatisch hierhin",
       "en": "ISIC division (36) — new gaps route here automatically"
      }
     },
     {
      "n": 2,
      "label": {
       "de": "Membrantechnologien mit eigener Route und Einheit",
       "en": "membrane technologies with their own route and unit"
      }
     },
     {
      "n": 0,
      "label": {
       "de": "Einträge heute — leer per Design",
       "en": "entries today — empty by design"
      }
     }
    ],
    "items": [
     {
      "de": "Umfang wächst mit der Re-Klassifikation auf Trink- und Prozesswasser-Aufbereitung und -Verteilung.",
      "en": "Scope grows with re-classification to potable and process water treatment and distribution."
     },
     {
      "de": "Keine Charakterisierungsschicht — Wirkungsfaktoren rechnet der Workbench.",
      "en": "Not a characterisation layer — impact factors are computed by the workbench."
     }
    ],
    "footnote": {
     "de": "Gerüst aus dem lci-deecoinvent-Katalogdurchlauf vom 22.07.2026: 25'412 Aktivitäten des Referenzkatalogs nach ISIC rev.4 klassifiziert, 17'561 ohne getreuen offenen Ersatz. Identität über sediment, nie über UUIDs.",
     "en": "Scaffolded by the lci-deecoinvent full-catalog pass of 2026-07-22: 25,412 reference-catalog activities classified by ISIC rev.4, 17,561 without a faithful open replacement. Identity via sediment, never via UUIDs."
    }
   }
  }
 }
};
