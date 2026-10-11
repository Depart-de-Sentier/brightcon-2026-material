# Dis-aggregated BAFU-2026 system processes — export and import

This folder holds a machine-readable export of the unit processes the `reverse-bafu` project
rebuilt for BAFU-2026's **system processes**: datasets that ship with no production inputs, only
the cumulative elementary flows of their whole supply chain on the product. We found 138 (101
carry the ecoSpold `type=2` flag, 37 were found by structure) and dis-aggregated 51; the export
holds those 51, plus the alternative variants of some of them (`"variant"`, see below).

The point of the export is that you can enrich **your own** Brightway project with them: the
rebuilt processes are added as a new database whose exchanges link, by code, to the BAFU-2026 and
EF 3.1 biosphere databases you already have.

> **Read [Known quality limits](#known-quality-limits) before using any of this in a study.**
> Several of these rebuilds reproduce only a few per cent of the original dataset's flows.

---

## Files

| file | what it is |
|---|---|
| `disaggregated_bafu2026.json` | the export. Plain, documented JSON — one object per rebuilt dataset, with every exchange, its supplier's BAFU code, every elementary flow with its EF 3.1 code **and** database, the residual block, and the provenance (report, page, quoted line) wherever the pipeline recorded it. |
| `disaggregated_bafu2026_exchanges.csv` | the **explicit** exchanges flattened to one row each, for reading in a spreadsheet. It is a *view*; the JSON is the source of truth (the CSV drops the derivation detail, the gaps, the evidence list and the residual rows, which outnumber the explicit ones more than a hundred to one). |
| `README.md` | this file. |

Both files are generated — never hand-edited — by:

```bash
uv run python scripts/export_disaggregated.py
```

which reads `results/rebuild_status.csv`, the specs under `specs/`, and the Brightway sandbox
`reverse-bafu-sandbox` that `reverse-bafu run-all` built.

---

## Importing into your project

```bash
uv run python scripts/import_disaggregated.py --project <your-project>
```

That creates one new database, `bafu-2026-disaggregated`, and touches nothing else. Your
BAFU system processes stay exactly as they are; the new unit processes link *to* them for their
supply chain.

Useful flags:

| flag | |
|---|---|
| `--dry-run` | resolve every reference and report, write nothing. Run this first. |
| `--database NAME` | name of the new database (default `bafu-2026-disaggregated`) |
| `--bafu-db NAME` | your BAFU-2026 database, if it is not called `bafu-2026` |
| `--biosphere NAME` | biosphere database to resolve flows in; repeat for several (default `ef-3.1-biosphere` and `bafu-2026-residual`) |
| `--include explicit\|hybrid\|both` | which nodes to import — see below (default `both`) |
| `--overwrite` | replace the target database if it already exists |

**It fails loudly.** If a referenced supplier code or elementary-flow code does not exist in your
project, the importer prints every missing reference — with the dataset and the exchange that
wanted it — and exits with code 2 **before writing anything**. The usual cause is that your
BAFU-2026 or EF 3.1 release differs from the one the export was made against
(`links_against` in the JSON records which that was).

### Explicit vs hybrid — which node to use

Each rebuilt dataset produces up to two nodes:

* **`<bafu-code>-disagg`, "… , disaggregated"** — the *explicit* model: only the exchanges the
  evidence supports. Transparent, but incomplete: its cumulative inventory does **not** equal the
  original system process.
* **`<bafu-code>-hybrid`, "… , hybrid"** — the same exchanges **plus a residual block** of
  elementary flows equal to *(original cumulative inventory − explicit cumulative inventory)*,
  flow by flow. By construction the hybrid reproduces the original dataset **exactly**, while the
  part that is explained by a real supply chain is visible as named technosphere exchanges. It
  is what you want if you care about not changing your results.

Use the **hybrid** if you need results that match BAFU-2026. Use the **explicit** node only when
you deliberately want the incomplete, evidence-only model — for example to substitute a different
electricity mix into the part of the chain that *is* explicit.

The residual can contain negative amounts (where the explicit model overshoots the original). That
is expected and is what makes the hybrid exact.

> **Note on the residual and redistribution.** A residual block is *the original BAFU-2026
> cumulative flow vector minus the explicit model*, flow by flow. It therefore carries BAFU's
> numbers. If you are passing this export on and may not redistribute BAFU data, regenerate it
> with `scripts/export_disaggregated.py --no-residual`: the explicit nodes still export in full
> (they are derived from the public reports), and the recipient can rebuild the hybrids themselves
> from their own BAFU-2026 copy.
>
> **Note on release drift.** The residual was computed against the BAFU-2026 release named in
> `links_against`. If your copy differs, the hybrid will no longer be exactly equal to *your*
> original — it will be exactly equal to the one the export was made from. The importer cannot
> detect this; it only checks that the codes exist.

---

## Round-trip verification

`scripts/verify_import_roundtrip.py` imports this export into a scratch project and checks it, so
the claims above are measured rather than asserted:

```bash
uv run python scripts/verify_import_roundtrip.py --source bafu-2026 --scratch import-test
```

The run behind the numbers in this file:

```
STEP 1  refuse to import into a project that has no BAFU-2026
        OK   refused with: database 'bafu-2026' not found in project 'import-test-empty'

STEP 2  scratch project 'import-test', copied from 'bafu-2026'
        databases: ['bafu-2026', 'bafu-2026-residual', 'ef-3.1-biosphere']   (build sandbox removed)

STEP 3  dry run:  resolved every reference: 120 nodes, 92034 exchanges
STEP 4  import:   wrote 120 nodes to 'bafu-2026-disaggregated'

STEP 5  technosphere exchanges: 986 (of which 972 link into bafu-2026)
        biosphere exchanges:  90928 (of which residual: 90478)
        dangling references:      0

STEP 6  LCA per imported dataset, cumulative inventory compared flow by flow with the original:
        60 datasets checked
        worst hybrid deviation:   4.277e-07        <- numerical noise
        explicit deviation range: 8.7 % to 1611.5 %

RESULT: PASS
```

That last block is the whole story in two numbers: **the hybrid nodes reproduce the originals; the
explicit nodes do not.** If your own run shows a hybrid deviation well above 1e-6, your BAFU-2026
release is not the one this export was generated against.

---

## What the strategies mean

| | |
|---|---|
| **S1** | **transcription** — the report prints *this dataset's own* inventory, and every technosphere input carries one printed number. We copy it; the only arithmetic we add is unit conversion (litres to MJ, distances to tkm). A printed range is not enough, and neither is a table the report itself calls comparison data or literature |
| **S2** | **template transfer** — no usable inventory, but a *unit process of the same product* already exists: at another site, in another grade, as an older ecoinvent version, or as BAFU's own dis-aggregated twin. Its input structure is reused, site-specific inputs such as the electricity grid are switched, and the amounts are calibrated, usually within 0.5–2× of the template |
| **S3** | **top-down model** — something names the inputs, but not every amount: the dataset's own process description, a partial table, printed ranges, or published comparison data. The main feedstock comes from the reaction equation or a mass balance, utilities from BAFU's generic chemicals module, and the calibration sets whatever the evidence leaves open |

Fitting the flow vector alone is never a route: without evidence for the input list it produces a
good-looking inventory with the wrong structure (the no-list rows of the benchmark in the project
README §6). Every rebuild, whatever its route, also has the hybrid node described above.

"Calibrated" amounts are fitted by bounded least squares against the dataset's own aggregated flow
vector, with the input list held fixed. The export marks them: every technosphere exchange carries
`"calibrated": true/false`, and `"bounds"` when the fit was bounded. A `false` there means the
amount was read off the report.

---

## JSON format

```jsonc
{
  "schema": "reverse-bafu/disaggregated-bafu-2026",
  "schema_version": "1.0",          // major version bump = breaking change
  "generated_at": "...", "git_commit": "...", "source_project": "bafu-2026",
  "links_against": {                 // which databases the codes below refer to
    "inventory_database": "bafu-2026",
    "biosphere_databases": ["ef-3.1-biosphere", "bafu-2026-residual"]
  },
  "strategies": { "S1": "...", ... },
  "citation": "...",
  "datasets": [
    {
      "bafu_code": "<uuid>",             // the system process this replaces
      "bafu_name": "...",
      "replaces": {"database": "bafu-2026", "code": "<uuid>", "name": "..."},
      "variant": "" | "draft" | "chained", // "" = the spec written in an interactive session; "draft" =
                                         // produced by the automated drafting routes; "chained" = links a
                                         // rebuilt node instead of a system process
      "spec": "specs/....json",          // the spec it was generated from, in this repo
      "strategy": {"code": "S1", "label": "...", "note": "..."},
      "evidence": [{"source": "<report pdf>", "where": "pages 845-847 -> report-p845-847.txt"}],
      "quality": { ... },                // the agreement figures, copied from results/rebuild_status.csv
      "provenance": { "pipeline": ..., "extraction": ..., "mapping": ...,
                      "gaps_reported_by_model": [...], "skipped_items": [...] },
      "main_node_code": "<uuid>-disagg",
      "nodes": [
        {
          "node_code": "<uuid>-disagg",
          "name": "..., disaggregated", "location": "RER", "unit": "kilogram",
          "reference_product": "..., disaggregated",
          "technosphere": [
            {
              "supplier_code": "<uuid>",            // <- the BAFU-2026 code to link to
              "supplier_database_role": "bafu",     //    "bafu" = your bafu-2026;
                                                    //    "this-export" = another node in this file
              "supplier_name": "Cement, unspecified, at plant",
              "supplier_location": "CH",
              "amount": 215.0, "unit": "kilogram",
              "calibrated": true, "bounds": [180.0, 250.0],
              "comment": "...",
              "provenance": {                       // present where the pipeline recorded it
                "evidence": "report-p97-99.txt",
                "quote": "Portland Cement  ...  cement, unspecified, at plant  2.15E+02 kg",
                "raw_value": 215.0, "raw_unit": "kg", "per": "per m3 wood wool board",
                "factor": 1.0, "factor_source": "", "scale_to_unit": 1.0,
                "mapping_reason": "...", "confidence": "high",
                "by": "claude-code:...", "reviewed_by": null
              }
            }
          ],
          "biosphere": [
            {
              "flow_code": "<ef-3.1 uuid>",         // <- the elementary-flow code to link to
              "flow_database": "ef-3.1-biosphere",  // <- and the database it lives in
              "flow_name": "Waste Heat",
              "categories": ["air"],
              "kind": "emission" | "resource",
              "amount": 32.9, "unit": "megajoule",
              "comment": "...", "provenance": { ... }
            }
          ]
        }
      ],
      "residual": {                      // null if no hybrid was built
        "node_code": "<uuid>-hybrid",
        "name": "..., hybrid", "n_flows": 1289,
        "note": "Hybrid node: ... equals the original BAFU system process exactly ...",
        "flows": [{"flow_code": "...", "flow_database": "...", "flow_name": "...",
                   "categories": [...], "amount": -1.2e-3, "unit": "kilogram"}]
      }
    }
  ]
}
```

Conventions worth knowing:

* **Codes, not names.** Every link is a code. Names are carried alongside for humans and are never
  used for matching.
* **`flow_database` matters.** Most elementary flows are EF 3.1, but BAFU-2026 also uses flows
  that have no EF 3.1 equivalent; those live in a second biosphere database (here
  `bafu-2026-residual`). The importer tries the named database first and then the others you gave
  it, so it still works if you keep them under different names.
* **`provenance.reviewed_by` is `null` everywhere.** Nothing in this export has been reviewed by a
  human LCA practitioner. Treat `"confidence": "low"` entries with particular suspicion.
* **`provenance.gaps_reported_by_model`** lists, per dataset, what the report did *not* cover.
  Read it — it is the honest part.

---

## Known quality limits

These are reconstructions, not the original data. The headline number per dataset is **what share
of the original's elementary flows the explicit model reproduces within ±10 %**, and for many of
them it is small. The route is the one the spec carries (S1 transcription, S2 template transfer,
S3 top-down model).

| BAFU dataset | strategy | flows within +-10 % | of the 50 largest kg flows | kg mass covered | median deviation |
|---|---|---|---|---|---|
| Polyvinylchloride, suspension polymerised, at plant | S3 | 1403/1667 (84%) | 36/50 | 34.1 % | 1.7 % |
| Purified terephthalic acid, at plant | S3 | 1332/1667 (80%) | 24/50 | 6.1 % | 2.4 % |
| Polyethylene, LLDPE, granulate, at plant | S3 | 1299/1667 (78%) | 26/50 | 7.7 % | 1.1 % |
| Polyethylene, HDPE, granulate, at plant | S3 | 1296/1667 (78%) | 26/50 | 7.6 % | 1.1 % |
| Polyethylene, LDPE, granulate, at plant | S3 | 1259/1667 (76%) | 23/50 | 6.5 % | 2.2 % |
| Polypropylene, granulate, at plant | S3 | 1245/1667 (75%) | 21/50 | 6.3 % | 3.9 % |
| Polyvinylchloride, emulsion polymerised, at plant | S3 | 268/1667 (16%) | 14/50 | 25.9 % | 79.6 % |
| Cement ZN, D, at plant | S3 | 213/1326 (16%) | 11/50 | 5.3 % | 27.9 % |
| Cement ZN, D, at plant (draft) | S3 | 192/1326 (14%) | 16/50 | 4.0 % | 25.8 % |
| Particle board, cement bonded, at plant (draft) | S3 | 140/1149 (12%) | 8/50 | 42.7 % | 63.0 % |
| Polyethylene terephthalate, granulate, bottle grade, at plant | S2 | 127/1679 (8%) | 9/50 | 4.7 % | 69.6 % |
| Titanium dioxide at plant, sulphate process, at plant (draft) | S3 | 117/1148 (10%) | 11/50 | 13.3 % | 75.2 % |
| xxx Wood wool boards, cement bonded, at plant (draft) | S3 | 111/1149 (10%) | 7/50 | 30.6 % | 63.0 % |
| Ethylene glycol, at plant | S2 | 105/1668 (6%) | 8/50 | 4.6 % | 180.3 % |
| Burnt shale, at plant | S1 | 97/1326 (7%) | 5/50 | 99.5 % | 66.1 % |
| Burnt shale, at plant (draft) | S1 | 81/1326 (6%) | 3/50 | 30.4 % | 144.5 % |
| xx Packaging glass, white, at regional storage | S3 | 76/1146 (7%) | 5/50 | 0.1 % | 88.5 % |
| xx Packaging glass, green, at regional storage | S3 | 74/1146 (6%) | 4/50 | 0.1 % | 90.0 % |
| xx Packaging glass, brown, at regional storage | S3 | 73/1146 (6%) | 3/50 | 0.1 % | 86.5 % |
| Anthraquinone, at plant (draft) | S3 | 64/1149 (6%) | 4/50 | 7.7 % | 78.5 % |
| Gypsum plaster board, at plant | S2 | 64/1171 (5%) | 2/50 | 1.0 % | 99.9 % |
| Xylene, at plant | S3 | 60/1664 (4%) | 2/50 | 0.6 % | 120.7 % |
| xx Packaging glass, brown, at plant | S2 | 54/1146 (5%) | 3/50 | 0.1 % | 130.7 % |
| xx Packaging glass, white, at plant | S2 | 53/1146 (5%) | 4/50 | 0.2 % | 152.3 % |
| xx Packaging glass, white, at plant (draft) | S2 | 53/1146 (5%) | 7/50 | 10.6 % | 173.4 % |
| Gypsum fibre board, at plant | S2 | 52/1172 (4%) | 4/50 | 1.4 % | 86.3 % |
| xx Packaging glass, green, at plant | S2 | 45/1146 (4%) | 4/50 | 0.6 % | 177.8 % |
| Titanium dioxide, chloride process, at plant (draft) | S3 | 42/1147 (4%) | 5/50 | 38.2 % | 70.7 % |
| Vinyl chloride, at plant | S3 | 32/1665 (2%) | 0/50 | 0.0 % | 191.2 % |
| Wood preservative, inorganic salt, containing Cr, at plant (draft) | S3 | 31/1148 (3%) | 1/50 | 0.0 % | 89.2 % |
| xxx Wood wool boards, cement bonded, at plant | S2 | 25/1149 (2%) | 2/50 | 0.0 % | 70.3 % |
| Polystyrene, expandable, at plant (chained) | S3 | 24/1670 (1%) | 0/50 | 0.0 % | 103.0 % |
| Wood preservative, organic salt, Cr-free, at plant (draft) | S3 | 18/1149 (2%) | 0/50 | 0.0 % | 91.8 % |
| Polystyrene, expandable, at plant | S3 | 17/1670 (1%) | 0/50 | 0.0 % | 100.0 % |

Sorted best-first; `(draft)` is the spec the automated route produced, `(chained)` a variant that
links a rebuilt node instead of a system process. "flows within ±10 %" counts the elementary flows of the original aggregated
system process that the **explicit** node reproduces within ±10 %, out of the flows the solve determines.
Source: `results/rebuild_status.csv`, and the per-dataset report named in each dataset's
`quality.report`.

This table is the 29 datasets of the flag-based survey. A second family — the 37 APME
eco-profiles the `type=2` flag never marked — is rebuilt too and has its own table below, under
*The APME eco-profiles the ecoSpold type=2 flag missed*; `results/rebuild_status.csv` holds both.

Two notes on the rows:

* The route follows what the evidence gave, not the fact that a report was read: a report that
  prints ranges, or only comparison data, makes an S3 model, not an S1 transcription (cement ZN/D,
  both titanium dioxides). For the drafted specs the rule is applied in code: S1 only if no input
  had to be fitted. An S3 dataset carries `"calibrated": true` on most of its technosphere
  exchanges.
* Rows appearing twice (burnt shale, cement ZN/D, wood wool board, white packaging glass at plant)
  are the same BAFU dataset rebuilt two ways: in an interactive session and by the automated drafting
  routes (`"variant": "draft"`). They have different node codes and both are importable; pick one.
  The interactive one is the one counted in the project's totals.

Read that column as: *the explicit node is a partial model.* The S2 rebuilds in particular — the
packaging glass at plant, the gypsum boards, the wood wool board — reproduce only a few per cent of
the original's flows, because the template unit process they borrow their structure from is a
different plant with a different supply chain, and calibration can only move amounts, not add or
remove inputs. The `kg_mass_covered` column shows the same thing from the mass side: for several
of them well under 1 % of the original's kilogram mass is explained.

### The PlasticsEurope family, and why its numbers are not comparable with the rest

Twelve of the rows above (the polyolefins, the two PVCs, EPS, PET bottle grade, vinyl chloride,
PTA, xylene, ethylene glycol) are the PlasticsEurope eco-profiles that BAFU-2026 carries as system
processes. They hold both the best and the worst scores in the table, and the spread has almost
nothing to do with how good the evidence behind each one is. Three things drive it, and all three
are properties of BAFU-2026 rather than of the rebuilds:

1. **One exchange dominates three quarters of every vector.** ESU added `4.0E-10 units of
   Chemical plant, organics` to each of the 14 datasets when implementing them ("the standard
   amount for production of chemicals", Rajabihamedani et al. 2025 sec. 3.6). That one exchange
   supplies more than 90 % of the value of 1244–1464 of the 1790 flows in their cumulative
   inventories — PET bottle grade is the clean control, since it has *no other* technosphere
   exchange at all and still has 1790 cumulative flows against the 393 it declares. Run
   `scripts/plasticseurope_infrastructure_diagnostic.py` to see it per dataset. The practical
   consequence for a rebuild: ESU added one chemical plant per *dataset*, i.e. one per
   cradle-to-gate chain, so a rebuilt unit process that links to a precursor which already carries
   one and then adds its own doubles ~1300 flows. Every spec in this family therefore carries the
   infrastructure as a free input bounded by `[0, 4.0E-10]`, and the fit drives it to zero or close to
   it in all but two (polypropylene sits at the bound, PTA at 40 % of it). Getting this one exchange
   right moved HDPE from 4 % to 76 % (78 % with the current fit).
2. **A high score here mostly means "the precursor is another PlasticsEurope dataset".** Five of
   the six best rows — S-PVC, LLDPE, HDPE, LDPE, PP — are all a monomer at 1 kg per kg of polymer plus
   calibrated energy, and the monomer is itself a PlasticsEurope (or APME-derived) aggregate, so
   the two vectors share a background by construction. That is a genuine disaggregation — the
   polymer's burden is now traceable to its monomer's dataset — but 84 % is not a statement about
   the quality of the polymerisation model, whose fitted electricity and steam come out at
   essentially zero.
3. **Sub-compartments split across data vintages.** The 2025 PlasticsEurope implementations put
   CO₂ in `Emissions to air, unspecified`; the older ecoinvent-v2-nomenclature datasets they link
   to (Styrene, Propylene, Benzene, Toluene) put it in `Emissions to urban air close to ground`.
   These are different EF 3.1 flows, so a model whose substance total is within 10 % can score two
   entries at −98 % and +6370 %. Polypropylene and expandable polystyrene are both affected;
   EPS, at 1 %, is the extreme case.

Two of the fourteen — **Ethylene, average** and **Pyrolysis gasoline** — are deliberately absent
from the export. Both are steam-cracker products, the cracker is a multi-output process whose
allocation nothing in the documentation bundle quantifies, and no report in the bundle prints a
yield or an energy figure for it. `results/drafting_status.csv` records the reason.

Specific things to keep in mind:

1. **Only the hybrid node reproduces the original.** If you swap an aggregated dataset for the
   explicit `-disagg` node your results will change, often by a lot. That change is not an
   improvement in accuracy — it is the part of the supply chain the rebuild does not yet cover
   going missing. Use `-hybrid` unless you know exactly why you want otherwise.
2. **A good flow agreement does not prove a correct structure.** The project's calibration
   benchmark (project README §6) shows it explicitly: offered every dataset in the database and no
   input list, the fit reproduces 100 % of the flows within ±10 % with a process made of ~71 inputs
   that are not in the real one. Inventory agreement and structural correctness are different things.
3. **Calibrated amounts are fits, not measurements.** Where a report printed "confidential", the
   input is in the list because the report names it, and the amount comes from the least-squares
   fit within the stated bounds. Those entries carry `"calibrated": true` and, usually,
   `"confidence": "low"` in their provenance. Several of them sit *on* their bound after the fit,
   which means the data wanted to go further and the bound stopped it.
4. **Nothing here has been reviewed by a person.** The drafted (`"variant": "draft"`) datasets
   come from the automated routes — locate the table in the PDF, transcribe it, map each line to a
   dataset or flow — with every step recorded and every number quoted; `reviewed_by` is `null`
   throughout. The other specs were written by an LLM in interactive sessions guided by the team,
   with their sources and arithmetic in `strategy.note`.
5. **Coverage is limited by the evidence.** Of the 138 system processes, 51 are rebuilt. For the
   other 87 we found too little: no report in the documentation bundle (53), or a report that
   prints no usable inventory — often it says outright that the unit-process data are
   confidential. They are deliberately absent from this export rather than invented;
   `results/usable_information.csv` gives the reason for each one.

### The APME eco-profiles the ecoSpold type=2 flag missed

BAFU-2026 carries a second family of aggregated datasets that the `type=2` flag does not mark.
`scripts/find_system_processes.py` finds them by structure — a dataset with no production input at
all (only waste-treatment services) but a real elementary-flow vector — and there are **37** of
them: benzene, toluene, styrene, propylene, butadiene, butene, pentane, acetone, hydrogen cyanide,
the chloromethanes, epoxy resin, the nylons, ABS, SAN, GPPS, HIPS, polycarbonate, the two PMMAs,
polybutadiene, PVDC, polyols, MDI, TDI, methyl methacrylate, acetone cyanohydrin, naphtha APME mix,
and the ethylene and propylene pipeline-system datasets.

These are not a curiosity at the edge of the database. **466 BAFU-2026 datasets consume at least
one of the 37** — against 936 that consume one of the 101 flagged ones — so the unflagged system
processes sit inside the database's own unit processes, not only at the top of a survey: `Ethyl
benzene, at plant` consumes `Benzene, at plant`, `Cumene, at plant` consumes benzene and propylene,
`Acrylonitrile from Sohio process` consumes propylene, and `Glass fibre, at plant` consumes
`Nylon 6, at plant`. The most-consumed are epoxy resin (82 consumers), ABS (68), toluene and
hydrogen cyanide (60 each), polycarbonate (55) and acetone (53). Only the four `xx`-marked
datasets have no consumer at all. (`scripts/ecoprofile_consumers.py`.)

They are not a guess either. All 37 say so in their own metadata, which the structural test never reads:
`includedProcesses` = *"Aggregated data for all processes from raw material extraction until
delivery at plant"*, or the comment *"The data source for this process is a system inventory from
Boustead. Due to the cumulated form of this data only the ressources and emissions included in the
data source were considered."* Their own chapters in ecoinvent report No. 8 say it a third time:
*"Due to the fact that this dataset is cumulated it was not possible to use the other processes
modelled in econvent to obtain a transparent process chain."*

**22 of the 37 are rebuilt** (25 specs — acetone, epoxy resin and polycarbonate each have an
interactive and a drafted one — plus two `-chained` variants that re-point an existing rebuild at
the rebuilt styrene). The remaining 15 are listed with a reason in `results/usable_information.csv`.

Only acetone, hydrogen cyanide and epoxy resin have a report that prints unit-process data, so
`results/drafting_status.csv` reads `pages-not-found` for most of the 37 (the report route, run
with `--no-fallback`). That is not the same as "not rebuilt". The other rebuilds are S3 models
written from the dataset's own ecoSpold `technology` field plus reaction stoichiometry, and S2
transfers from a sibling unit process BAFU already contains; their evidence is in the spec, not in
a PDF page range. The drafted polycarbonate shows the metadata route doing the same automatically.

| BAFU dataset | route | flows within ±10 % | of the 50 largest kg flows | kg mass | median \|Δ\| | of the flows the eco-profile itself declares |
|---|---|---|---|---|---|---|
| Acrylonitrile-butadiene-styrene copolymer, ABS, at plant | S3 | 1507/1667 (90%) | 12/50 | 3.9 % | 2.7 % | 13/137 (9.5 %) |
| xx Acetone cyanohydrin, at plant | S3 | 1395/1667 (84%) | 16/50 | 1.3 % | 5.3 % | 10/135 (7.4 %) |
| Polystyrene, high impact, HIPS, at plant | S3 | 1366/1668 (82%) | 9/50 | 0.5 % | 2.4 % | 4/136 (2.9 %) |
| Nylon 66, glass-filled, at plant | S3 | 1136/1679 (68%) | 22/50 | 89.2 % | 6.8 % | 14/134 (10.4 %) |
| Polymethyl methacrylate, beads, at plant | S3 | 1071/1667 (64%) | 24/50 | 96.5 % | 6.7 % | 26/135 (19.3 %) |
| Polymethyl methacrylate, sheet, at plant | S3 | 694/1668 (42%) | 4/50 | 0.2 % | 17.1 % | 25/138 (18.1 %) |
| xx Nylon 6, glass-filled, at plant | S3 | 456/1668 (27%) | 2/50 | 85.1 % | 16.6 % | 9/139 (6.5 %) |
| Polybutadiene, at plant | S3 | 237/1666 (14%) | 2/50 | 0.0 % | 41.3 % | 14/128 (10.9 %) |
| Styrene, at plant | S3 | 55/1666 (3%) | 2/50 | 2.4 % | 123.8 % | 5/135 (3.7 %) |
| Polystyrene, general purpose, GPPS, at plant | S3 | 25/1668 (1%) | 8/50 | 2.3 % | 4633.1 % | 14/137 (10.2 %) |
| Methyl methacrylate, at plant | S3 | 18/1666 (1%) | 2/50 | 0.4 % | 2942.3 % | 10/135 (7.4 %) |
| Nylon 66, at plant | S3 | 11/1678 (1%) | 2/50 | 0.1 % | 21538.9 % | 6/134 (4.5 %) |
| Acetone, liquid, at plant | S3 | 8/1667 (0%) | 2/50 | 0.1 % | 13689.2 % | 3/132 (2.3 %) |
| Epoxy resin, liquid, at plant (draft) | S1 | 8/1667 (0%) | 3/50 | 75.0 % | 105811.4 % | 6/102 (5.9 %) |
| Polystyrene, general purpose, GPPS, at plant (chained) | S3 | 8/1668 (0%) | 0/50 | 0.0 % | 10123.3 % | — |
| Polyols, at plant | S3 | 7/1666 (0%) | 0/50 | 0.0 % | 8640.6 % | 5/137 (3.6 %) |
| Epoxy resin, liquid, at plant | S2 | 6/1667 (0%) | 3/50 | 75.0 % | 105836.1 % | 4/102 (3.9 %) |
| Hydrogen cyanide, at plant (draft) | S3 | 6/1678 (0%) | 1/50 | 0.1 % | 11380.3 % | 4/131 (3.1 %) |
| Methylene diphenyl diisocyanate, at plant | S3 | 6/1668 (0%) | 2/50 | 12.6 % | 38831.4 % | 4/135 (3.0 %) |
| Toluene diisocyanate, at plant | S3 | 6/1678 (0%) | 0/50 | 0.0 % | 24967.9 % | 6/134 (4.5 %) |
| Naphtha, APME mix, at refinery | S2 | 4/1679 (0%) | 0/50 | 0.0 % | 30857.6 % | 4/110 (3.6 %) |
| Polycarbonate, at plant (draft) | S3 | 4/1665 (0%) | 0/50 | 0.0 % | 30649.3 % | — |
| Styrene-acrylonitrile copolymer, SAN, at plant | S3 | 3/1668 (0%) | 2/50 | 1.1 % | 132.9 % | 3/135 (2.2 %) |
| Acetone, liquid, at plant (draft) | S1 | 1/1666 (0%) | 1/50 | 0.0 % | 36139.8 % | 1/132 (0.8 %) |
| Benzene, at plant | S2 | 1/1664 (0%) | 0/50 | 0.0 % | 9145.4 % | 0/133 (0.0 %) |
| Polycarbonate, at plant | S3 | 0/1665 (0%) | 0/50 | 0.0 % | 26053.5 % | 0/135 (0.0 %) |

Sorted by the third column. `(draft)` is the spec the LLM route produced, `(chained)` a variant
that links a rebuilt node instead of an aggregated one. The last column comes from
`results/ecoprofile_agreement.csv`; read the next section before reading the table.

#### The three numbers disagree, and the disagreement is the finding

Read the table with the last column next to the third, because they say opposite things. ABS
reproduces **90 %** of the target's determined flows — the best in the family — and **9.5 %** of
the flows the eco-profile itself declares, with 0 % of the declared kilogram mass. Polymethyl
methacrylate beads reproduce 64 % of all flows, 19 % of the declared flows, and **97.5 %** of the
declared kilogram mass. Those are not small differences in emphasis; they are three different
questions.

The arithmetic behind it: these datasets are not pure system processes. Each carries seven to nine
explicit `Disposal, …` exchanges (34 of the 37 carry exactly eight), and those waste chains, not
the eco-profile, generate about 92 % of the ~1780 flows the harness compares — the eco-profile
itself declares only 78 to 139 substances, 4 to 8 % of the total. So:

* **"flows within ±10 %" is mostly a measure of the waste-treatment background.** A model that
  links another dataset of the same APME family inherits that dataset's disposal chains, which have
  the same shape as the target's, and the long tail agrees. That is why ABS, HIPS and the
  glass-filled nylons score high — and it is also why the fit, left free, chooses the composition
  that matches the waste chains rather than the chemistry (see the identifiability trap below).
* **"of the flows the eco-profile itself declares" is a measure of the chemistry**, and on this
  family it is hard: 0–18 %. Part of that is real modelling gap; part of it is structural. These
  datasets put their air emissions in *Emissions to urban air close to ground* and their water
  emissions in *Emissions to fresh water*, while `resolve` maps a spec's flow by name and
  top-level compartment only and prefers the *unspecified* sub-compartment, so a substance total
  that is exactly right can still be counted as two large deviations.
* **The declared kilogram mass is the number to quote** when the question is "does this node carry
  the right burden?" (`kg_mass_declared_pct` in `results/ecoprofile_agreement.csv`): 97.5 % (PMMA
  beads), 95.8 % (acetone cyanohydrin), 90.0 and 86.9 % (the glass-filled nylons), 76.3 % (epoxy
  resin).

The control that fixes the scale is **epoxy resin**, the one dataset of the family where BAFU ships
both versions. Chapter 31 of `2007 - LCI chemicals - Althaus.pdf` prints Tab. 31.1 (the cumulative
inventory = the aggregated dataset) and Tab. 31.2 (*"Disaggregated life cycle inventory for the
production of liquid epoxy resin"*), and BAFU-2026 carries the second as
`Epoxy resin, liquid, disaggregated data, at plant` [RER]. Substituting BAFU's own disaggregated
dataset for BAFU's own aggregated one, 1 kg for 1 kg, with no modelling at all, gives:

| | |
|---|---|
| fossil CO₂ | **+1.5 %** |
| rock salt (resource) | +3.6 % |
| chloride to water | +11.2 % |
| sodium to water | +11.8 % |
| suspended solids | −13.7 % |
| calcium to water | +18.4 % |
| calcite (resource) | +53.2 % |
| kilogram mass covered | **75 %** |
| **share of all determined flows within ±10 %** | **0 %** (6 of 1669) |

That row is what a perfect answer looks like on this metric. Nothing in the table above should be
read as a verdict on a rebuild before it is read against it.

#### Two findings about the data itself

**`Styrene, at plant` declares 0.5615 kg of hazardous waste to incineration per kg of styrene.**
Its own feedstock benzene declares 0.0022 kg, toluene 0.0017, butadiene 0.0020, propylene 0.0021 —
and its own polymer, `Polystyrene, general purpose, GPPS`, which contains a kilogram of styrene per
kilogram of product, declares 0.0070 kg. A cradle-to-gate polymer profile cannot carry 80× less
waste than its monomer, so one of the two is wrong, and the rest of the family says it is the
styrene figure. `2010 - Changes in ecoinvent v2.1 and v2.2 - Althaus.pdf` sec. 2.5.1 documents
exactly this shape of error for the neighbouring dataset — *"especially in case of the ABS dataset
(DS ID 1817) where the amount of 'regulated chemical waste' had grown for a factor more than 20
compared to the former data used"* — and prints the mg→kg mapping rule (*"1 mg regulated chemical
waste → 10⁻⁶ kg disposal, hazardous waste, 25 % water, to hazardous waste incineration"*) whose
slip by a factor 1000 would produce it. ABS (0.2393 kg) and SAN (0.2398 kg) carry the same
signature. Consequence: any rebuild that links styrene inherits that waste chain, which is why GPPS
scores 1 % of flows while its fossil CO₂, methane, biogenic CO₂, SO₂, NOₓ and NMVOC are all within
2–29 %.

**The identifiability trap, measured on real data.** Five specs here give the calibrator a free
composition under a 1 kg mass constraint, because no report in the bundle prints one. In all five
the fit produced a composition that is chemically impossible:

| dataset | what the fit did | inventory agreement it bought |
|---|---|---|
| ABS | acrylonitrile → 1.3e-7 kg; 0.560 kg butadiene / 0.440 kg styrene | **90 %** of flows, median \|Δ\| 2.7 % — the best in the family |
| SAN | acrylonitrile → 0 kg; 1.000 kg styrene | 0 % |
| HIPS | styrene → 1.9e-3 kg; 0.998 kg polybutadiene | 82 % |
| Nylon 66, glass-filled | glass fibre → 1.9e-6 kg | 68 %, 89 % of the kg mass |
| xx Nylon 6, glass-filled | glass fibre → 0 kg | 27 %, 85 % of the kg mass |

The mechanism is not random. Under a mass constraint, when one candidate is another dataset of the
same APME family and the other is an ecoinvent unit process, the fit empties the ecoinvent one:
it drags a ~1670-flow background into a target that reports 78–139 substances, and every extra flow
counts against it. Among same-family candidates the fit then follows the waste-treatment exchanges
rather than the chemistry — which is why it prefers polybutadiene (0.0078 kg hazardous waste) to
styrene (0.5615) in HIPS. **The amounts of those five nodes reproduce the target's inventory and
must not be quoted as compositions.** Each spec says so in its own `strategy.note`.

#### How accurate is the LLM extraction route? Here it has an answer key

The drafted epoxy-resin spec is a transcription of Tab. 31.2 produced by the locate → extract → map
route, and BAFU-2026 contains the dataset that table describes. So for once the route can be scored
against a ground truth rather than against a cumulative vector. Comparing
`c80b8e9e-…-draft-disagg` with `Epoxy resin, liquid, disaggregated data, at plant` exchange by
exchange:

* **Technosphere: 9 of 9 amounts exactly right** — 4.0E-10 units of chemical plant, 0.298 and
  0.0058 kg of the two disposal services, 11 MJ heavy fuel oil, 13 kg tap water, 60.6 tkm lorry,
  1.74 tkm rail, 2.19 kWh electricity, 57.7 MJ natural gas, all to the printed digits. Two of the
  nine were mapped to a near-synonym of the dataset BAFU itself chose: *Electricity, medium
  voltage, production **RER**, at grid* instead of *…production ENTSO-E…*, and *Natural gas, burned
  in industrial furnace **1MW*** instead of *…1MWth*. Same amount, neighbouring dataset.
* **Elementary flows: 34 matched by (name, compartment), and all 34 within 1 %** — in fact to the
  printed digits; the largest deviation among them is +0.1 % on natural gas, from the 36.0 MJ/Nm³
  conversion.
* The remaining ~22 flows on each side are the *same substances in a different sub-compartment*
  (nitrogen oxides, ammonium, cyanide, iron, chromium, …), which is `resolve_flow`'s
  name-plus-top-level-compartment matching, not a transcription error — plus the three items the
  candidate search could not offer at all (water of unspecified natural origin, hydrogen fluoride
  to air, CFC-13), which the map step recorded as unmapped rather than guessing.

So on the one case in this batch where the answer is knowable: the reading of the PDF is exact, and
everything that is lost is lost in the mapping from a report's substance name to an EF 3.1 flow.
(`scripts/transcription_vs_truth.py` reproduces this comparison.)

#### Three measurements of how far two databases are apart

Three of the rebuilds are pure S2 transfers with nothing calibrated — one BAFU dataset substituted
for another, 1 kg for 1 kg. They contain no modelling at all, so what their check reports is not a
verdict on this project's method but a measurement of the distance between two inventories of the
same product. All three are worth having on record.

| substitution | fossil CO₂ | other headline flows | kg mass covered |
|---|---|---|---|
| **Epoxy resin**: BAFU's own *disaggregated* epoxy for BAFU's aggregated epoxy | **+1.5 %** | rock salt +3.6 %, chloride to water +11.2 %, sodium +11.8 %, suspended solids −13.7 % | 75 % |
| **Benzene**: ecoinvent's `Benzene, at refinery` [CH] for PlasticsEurope's `Benzene, at plant` [RER] | **−84.8 %** | methane −99.6 %, SO₂ −97.2 %, NOₓ −95.9 % | 0 % |
| **Naphtha**: ecoinvent's `Naphtha, at refinery` [RER] for `Naphtha, APME mix, at refinery` [RER] | −15.9 % | methane −98.9 %, NMVOC −98.3 %, NOₓ −84.8 %, CO −82.3 % | 0 % |

The epoxy row is the same product modelled twice by the same people, and it agrees. The other two
are the same product modelled by two different industries, and they do not: ecoinvent spreads a
refinery's burden over its whole product slate, the APME profiles charge the aromatics extraction
and reforming to the aromatics, and the gap between the two is roughly the size of that one
decision. Both nodes are legitimate disaggregations and neither is a drop-in replacement — which is
also the honest answer to the BTX allocation problem that blocks the rest of the family: the data
to resolve it are not missing, the *decision* is, and two databases made it differently.

#### Chaining a rebuild onto another rebuild changes almost nothing

`Polystyrene, expandable, at plant` was one of the rebuilds recorded as "still terminates on an
aggregated ancestor", with styrene as the blocker. Styrene is now rebuilt, so the blocker is gone.
The `-chained` variant that links the rebuilt styrene instead of the aggregated one scores 24 of
1670 flows within ±10 % (median |Δ| 103.0 %) against the committed spec's 17 of 1670 (median
100.0 %). For general-purpose polystyrene the same substitution makes it **worse**: 8 of 1668
against 25 of 1668. Removing an aggregated ancestor is a gain in transparency — the burden becomes
traceable to ethylbenzene dehydrogenation — and not a gain in agreement, because the target's
background was an industry survey and never ecoinvent's chain. Both variants are in the export;
pick on that basis, not on the score.

#### What is still impossible, and why

Fifteen of the 37 have no rebuild, and the reasons are two.

*Thirteen are products of a multi-output reactor whose allocation nothing in the bundle states*:
eight steam-cracker and reformate products (toluene, propylene, butadiene, butene, pentane, hydrogen
cracking APME, and the ethylene and propylene pipeline-system datasets) and five
chloromethanes/chloroethylenes (carbon tetrachloride, dichloromethane, methyl chloride,
tetrachloroethylene, trichloroethylene). The reports are
explicit about it: *"Little is given on toluene production alone as most information pertains to
benzene or BTX production plants"* (Althaus sec. 86.5.3); Tab. 86.1 prints the toluene yield of a
reformate plant as *"0 – 0.3"* tons per ton of feedstock, a range that includes zero; *"There was no
information in those cumulated inventory data about the share of the two processes considered. Also
the used allocation method … was unclear"* (sec. 24.5.2); *"All these production routes can be found
in Europe … but there is no information available how the distribution between these different
processes is"* (sec. 84.5.1). This is the same wall that blocks `Ethylene, average` and
`Pyrolysis gasoline`.

*Two have a precursor BAFU-2026 does not contain*: nylon 6 (no caprolactam, and no adiponitrile or
hexanedinitrile either) and polyvinylidene chloride (no vinylidene chloride). A third, nylon 66,
has the same problem — BAFU has no hexamethylenediamine — but its spec is published anyway with
56 % of the monomer mass and a prominent warning, because the adipic-acid half is exact and the
missing half is named, quantified and one line away from being added.

One more thing worth recording, because it cost time and will cost the next person time too: the
report's own index is wrong. Althaus Tab. 1.1 lists `benzene, at plant`, `pentane, at plant` and
`acetone cyanohydrin, at plant` as *"Reported in: Part II"*, and the 957-page report contains no
chapter for any of the three. The pentane case even leaves a trace of the mix-up: sec. 84.5.3, in
the *tetrachloromethane* chapter, reads *"Tab. 84.2 and Tab. 84.3 summarize the resulting data of
the average pentane production in Europe"*, while those tables are captioned *"Input data of the
dataset 'tetrachloromethane, at plant (RER)'"*.

---

## Licence and citation

The underlying data are BAFU's. Anything derived from them must carry:

> Source: Life Cycle Inventory database of the Swiss Federal Administration, BAFU:2026.

The disaggregation is a reconstruction by this project from the public LCI reports; it is not part
of BAFU-2026 and carries no endorsement by BAFU. Please say so when you pass these datasets on.

The export is *modified data* in the sense of the
[BAFU:2026 Terms of Use](https://www.bafu.admin.ch/dam/en/sd-web/-9ZObeMCZy8A/BAFU_2025_TermOfUse_EN_Webpage.pdf),
and it is shared on the same terms (their section 3.4). You may use, process and analyse it freely,
e.g. in LCA studies. You may not sell or resell it, or distribute it separately or as part of
another database. Pass it on only under these same terms, together with this file, which documents
the changes (section 3.2). The code that produced it is licensed under Apache-2.0; see the project README.
