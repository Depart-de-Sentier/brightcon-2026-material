# Dis-aggregating BAFU-2026 system processes

Brightcon 2026 hackathon project for
[brightcon-2026-material#38](https://github.com/Depart-de-Sentier/brightcon-2026-material/issues/38):
turn the aggregated *system processes* of the Swiss BAFU-2026 database back into *unit
processes*, and check flow by flow that the result still matches the original.

A system process stores the cumulative elementary flows of a whole supply chain on the product,
with no inputs. It gives the right score but can't be inspected, regionalised or updated. What we
found and did:

- **138 system processes in BAFU-2026.** 101 carry the ecoSpold `type=2` flag. 37 more carry no
  flag and were found by structure: the APME / PlasticsEurope-era eco-profiles.
- **51 of them dis-aggregated** into unit processes that link to the rest of BAFU:
  - by route: 1 transcription (S1), 11 template transfer (S2), 39 top-down model (S3);
  - 32 completely opened; 19 still link to a system process we did not rebuild.
  - For the other 87 we found too little information for the fit to have a chance.
- **A benchmark with a known answer.** 100 BAFU unit processes are aggregated by us and then
  dis-aggregated again:
  - Given the right input list, the fit recovers 772 of 786 input amounts within ±20 %.
  - Given no list, it matches 100 % of the elementary flows with a process made of the wrong
    inputs. So the input list has to come from evidence.
- **Everything is shareable.** The rebuilt unit processes are exported as documented JSON and
  import into any Brightway project that holds BAFU-2026.

## Where to read what

| | |
|---|---|
| [artifacts/presentation/dis-aggregating-system-processes.pdf](artifacts/presentation/dis-aggregating-system-processes.pdf) | The deck as presented at Brightcon 2026 |
| [artifacts/method-explainer.html](artifacts/method-explainer.html) | The method: why fitting alone fails, the algorithm, the routes, the benchmark |
| [artifacts/system-processes.html](artifacts/system-processes.html) | The 138 system processes: families, what their reports print, who entered them, what we rebuilt |
| [artifacts/rebuilt-inventories.html](artifacts/rebuilt-inventories.html) | One tab per rebuild: inputs, direct flows, agreement with the original, the checks |
| [artifacts/flow-parity.html](artifacts/flow-parity.html) | Original against rebuilt elementary flows, for every rebuild |
| [artifacts/calibration-benchmark.html](artifacts/calibration-benchmark.html) | The benchmark case by case |
| [artifacts/replacement-priority.html](artifacts/replacement-priority.html) | The 138 ranked by how much of BAFU depends on them |
| [artifacts/code-walkthrough.html](artifacts/code-walkthrough.html) | For developers: where each decision is made in the code |
| [exports/README.md](exports/README.md) | Using the rebuilds in your own project, and their quality limits dataset by dataset |

The HTML pages are self-contained: download one and open it in a browser.

The rest of this README reproduces everything from scratch:

| Step | What it does | Produces |
|---|---|---|
| 1 | Setup | – |
| 2 | Import BAFU-2026 into Brightway | – |
| 3 | Find the system processes | `results/system_terminated*.csv`, `sources.csv`, `dois.csv` |
| 4 | Make the specs | `specs/`, `results/drafting_status.csv` |
| 5 | Rebuild every spec | `results/rebuild_status.csv`, `results/checks/` |
| 6 | Benchmark | `results/benchmark/` |
| 7 | Export and import | `exports/` |
| 8 | Regenerate the pages and figures | – |

## 1. Setup

Needs [uv](https://docs.astral.sh/uv/) and `pdftotext` / `pdfinfo` (Debian/Ubuntu:
`apt install poppler-utils`), which the drafting steps use to read the report PDFs. Python 3.12
is picked up automatically.

```bash
uv sync                         # sentier-brightway (pinned commit), bw2data 4, bw2calc 2, numpy, scipy, jsonschema
uv sync --extra llm             # optional: the anthropic SDK, for `reverse-bafu draft-all` against the API
```

### The BAFU files

Download **both** of these from openLCA Nexus, <https://nexus.openlca.org/downloads>. You need a
free account and must accept BAFU's terms of use. Both stay out of the repository (citation at
the end).

| Nexus download | Zip you get | Unzip to | Needed by |
|---|---|---|---|
| **BAFU:2026 Version 1 - ecoSpold1** | `BAFU-2026 v1_ecoSpold v1.zip` (11,948 `process_<uuid>.xml`) | `data/ecospold/`. The zip's inner folder is `ecoSpold files/`; rename it. | Steps 3 and 4: the ecoSpold metadata, including the `type=2` flag the Brightway import drops |
| **BAFU:2026 Version 1 - Documentation** | `BAFU-2026 v1_Documentation.zip` (114 LCI report PDFs) | `BAFU-2026 v1_Documentation/` next to this README, keeping the inner `BAFU-2026 v1_Documentation/BAFU-2026 v1 LCI Reports/` layout | Step 3 (the `pdf` column) and step 4 |

```bash
unzip "BAFU-2026 v1_ecoSpold v1.zip" -d data/ && mv "data/ecoSpold files" data/ecospold
unzip "BAFU-2026 v1_Documentation.zip"
```

Step 2, the Brightway import, reads **neither** zip. `sentier-brightway` downloads its own copy
of the BAFU inventory: parquet files in the Sentier data repos, already converted from the
ecoSpold XML and pinned by commit and SHA-256. The zips are needed for what that conversion does
not carry: the ecoSpold metadata (the `type=2` flag, comments, sources) and the report PDFs.
Other locations can be given with `--ecospold <folder>` and `--reports <folder>`.

## 2. Import BAFU-2026 into Brightway 2.5

```bash
uv run sentier-brightway coverage                  # downloads ~40 MB of pinned Sentier parquet (cached in ~/.cache/sentier-brightway)
uv run sentier-brightway db --project bafu-2026    # ~3-4 min; --overwrite replaces a previous install
```

`./run_bafu.sh` does both. The project `bafu-2026` then holds:

- database `bafu-2026` (11,947 processes);
- `ef-3.1-biosphere` (EF 3.1 flows, with 95.8 % of BAFU's emissions relinked to them);
- `bafu-2026-residual` (the 113 flows without an EF counterpart);
- the 25 methods `("sentier", "EF v3.1", <category>)`.

Every command below uses this project by default; pass `--project <name>` if you chose another
name. The methods are handy for a smoke test, but the pipeline never uses them. Every rebuild is
judged against the original's elementary flows directly, so no characterisation method and no
weighting between impact categories enters the result.

Smoke test:

```python
import bw2data as bd, bw2calc as bc
bd.projects.set_current("bafu-2026")
act = bd.Database("bafu-2026").get("c4a92617-9f99-3d7b-95c0-15fb110b80ad")   # Electricity, low voltage, at grid | CH
lca = bc.LCA({act: 1}, ("sentier", "EF v3.1", "Climate change")); lca.lci(); lca.lcia()
print(lca.score)   # 0.0969623 kg CO2 eq per kWh
```

`uv run sentier-brightway backtest --out output/backtest --xlsx <BAFU LCIA results>` compares
every process with BAFU's own openLCA results.

## 3. Find the system processes and their sources

```bash
uv run python scripts/list_system_terminated.py   # -> results/system_terminated.csv (the 101 flagged, ~15 s)
uv run python scripts/list_sources.py             # -> results/sources.csv, results/dois.csv
uv run python scripts/find_system_processes.py    # -> results/system_terminated_extended.csv (all 138)
```

**`system_terminated.csv`** lists the **101** datasets whose ecoSpold `dataSetInformation@type` is
2 ("system terminated": the cumulative LCI, no supplier links;
[schema](https://github.com/brightway-lca/pyecospold/blob/main/pyecospold/schemas/v1/EcoSpold01MetaInformation.xsd#L26-L60)).
Each row carries:

- the dataset's inputs, flows and consumers in Brightway;
- its data-origin `family`;
- the same-product unit process (`unit_sibling`), where one exists;
- the people and representativeness fields from the metadata.

A 102nd flagged dataset has no exchanges and is skipped.

**`sources.csv`** lists the 129 distinct source citations, with the report PDF for 112 of them.
**`dois.csv`** lists the 36 DOIs embedded in dataset comments.

**The 37 the flag misses.** The `type=2` flag is reliable but not complete. BAFU-2026 also carries
the APME / PlasticsEurope-era eco-profiles, which were never marked. They are found by structure:
no production input at all (the only technosphere exchanges are waste-treatment services) but a
full elementary-flow vector. There are **37**: benzene, toluene, styrene, propylene, butadiene,
butene, pentane, acetone, hydrogen cyanide, the chloromethanes, epoxy resin, the nylons, ABS,
SAN, GPPS, HIPS, polycarbonate, the PMMAs, polybutadiene, PVDC, polyols, MDI, TDI, methyl
methacrylate, acetone cyanohydrin, naphtha APME mix and the ethylene/propylene pipeline-system
datasets. All 37 say so in their own metadata, which the structural test never reads:

- *"Aggregated data for all processes from raw material extraction until delivery at plant"*
- *"The data source for this process is a system inventory from Boustead."*

**Why the 37 matter.** They sit in the middle of the database, not at its edge:

- 466 BAFU-2026 datasets consume at least one of them; 936 consume one of the 101
  (`scripts/ecoprofile_consumers.py`).
- `Ethyl benzene, at plant` consumes `Benzene, at plant`.
- `Glass fibre, at plant` consumes `Nylon 6, at plant`.

138 is a lower bound: a partly aggregated dataset passes both tests unseen.

**`system_terminated_extended.csv`** lists all 138 with `detected_by` (flag | structure) and
`n_flows`. It has a shorter set of columns than `system_terminated.csv`.

Which list is used where:

- `resolve` and `check` use all 138 (`db.aggregated_codes_all()`), so a rebuild that links one of
  them is reported as the dependency it is.
- `db.aggregated_codes()` stays flag-based. The benchmark uses it to choose its test cases, and
  widening it would move every published benchmark number.

## 4. Make the specs

A **spec** is one JSON file per system process holding the evidence-derived unit process:

- the target;
- the route (`strategy`);
- the evidence;
- the inputs, with `free` / `bounds` / `sandbox` / nested `node` flags;
- the direct emissions and resources.

The format is in the docstring of [src/reverse_bafu/spec.py](src/reverse_bafu/spec.py), with
examples in [specs/](specs/). One command drafts them for every system process in
`results/system_terminated_extended.csv`:

```bash
uv run reverse-bafu draft-all                     # API route (uv sync --extra llm + an Anthropic API key or `ant auth login`)
uv run reverse-bafu draft-all --dry-run           # no model: writes the pending prompts, records where each dataset stands
```

Or, inside Claude Code, run `/draft-all`: the session answers the prompts itself and loops until
nothing is pending ([.claude/commands/draft-all.md](.claude/commands/draft-all.md)).

Useful options:

- `--only <codes>` restricts the run.
- `--no-fallback` stops after the report route.

Nothing else is typed by hand: the report comes from the `pdf` column of `results/sources.csv`,
and the pipeline locates the pages.

The result is `results/drafting_status.csv`, one row per dataset. Its `status` is one of:

- `drafted`: the spec is written, and `route` says which of the three routes below produced it;
- `no-usable-evidence`: neither a report, a same-product unit process nor the metadata names the
  inputs;
- `pages-not-found` / `no-pdf`: only with `--no-fallback`; the report has no inventory table, or
  there is no report;
- a pending `prompt-<n>-written`;
- `error`.

Each drafted dataset also gets a `specs/<code8>-<slug>.draft.json`. Reruns are incremental: every
response already on disk is reused, so a batch can be continued after an interruption or a fix.
With `--only`, just those rows of the status file are replaced.

### The report route, step by step

For each dataset the batch runs these stages. Every stage leaves its files under
`specs/evidence/<code>/`, so each number in the spec can be traced back to a quoted line.

1. **Locate** (one model prompt).
   - Every table and figure caption of the report PDF is extracted with its PDF page number.
     This is deterministic and cached in `.cache/pdftext/`.
   - The captions go into `prompt-0-locate.md` ([prompts/locate_pages.md](prompts/locate_pages.md)),
     together with the dataset's name, category and metadata.
   - The model names the caption(s) holding the dataset's inventory table and returns the PDF page
     range (at most four pages), or `found: false` with the reason.
   - The reports are in German or French and the dataset names in English. The match is by
     meaning, which is why this is a model step and not a text search.
2. **Evidence** (deterministic). It writes three files:
   - `report-p<a>-<b>.txt`: `pdftotext -layout` of those pages;
   - `target.json`: the dataset's ecoSpold metadata, plus the resource flows of its aggregated
     vector, largest first, as candidates for the process's own direct resources;
   - `manifest.json`: SHA-256 of the PDF, the text and the XML, plus the pdftotext version.
3. **Extract** (one model prompt). `prompt-1-extract.md` ([prompts/draft_spec.md](prompts/draft_spec.md))
   holds the metadata, the resource candidates and the excerpt. The model returns one line item
   per table row:
   - a verbatim `quote`;
   - `raw_value` and `raw_unit` as printed, and the table's basis (`per`);
   - an optional conversion `factor` with its `factor_source` (e.g. litres of diesel to MJ);
   - `kind` (input / emission / resource / co-product / ignore);
   - a `search` phrase for the supplying dataset or flow;
   - a `confidence`.

   It also returns `basis_amount`, `allocation`, `mass_sum` and `gaps` (what the excerpt does not
   cover). The rules forbid inventing inputs the excerpt does not mention and converting beyond a
   stated factor. A range in the table becomes a `free` input with `bounds`.
4. **Map** (deterministic candidates, then one model prompt).
   - For each line item, a keyword search over the 11,947 dataset names (inputs) or the EF 3.1
     flow list (emissions, resources) writes `candidates-2-map.json`.
   - `prompt-2-map.md` ([prompts/map_inputs.md](prompts/map_inputs.md)) asks the model to pick one
     candidate or none per item, with a one-sentence reason.
5. **Assemble** (deterministic).
   - `amount = raw_value × factor / basis_amount`, with unit names normalised.
   - A dependency on another system process is linked to its rebuilt node when one exists.
   - Every entry carries a `derivation`: quote, raw value, factor with source, search phrase,
     mapping reason, author, and `reviewed_by: null`.
   - The spec carries a `provenance` block with model, prompt hashes and authors.
   - The file gets `"variant": "draft"`, so its nodes never collide with an interactive spec of
     the same dataset.

### When no report prints the inventory: the template and metadata routes

Most system processes have no report that prints their inventory. For those, `draft-all` hands
over to two more routes, in this order, with the same audit trail:

- **Template route (S2), prompt 3.**
  - A deterministic name search lists the BAFU unit processes of the *same product*
    (`candidates-3-template.json`). The first segment of the product name must match exactly:
    "Benzene, at refinery" qualifies for "Benzene, at plant"; "Ethyl benzene" never does.
  - `prompt-3-template.md` ([prompts/draft_from_template.md](prompts/draft_from_template.md)) asks
    the model to:
    - pick one candidate or none;
    - list the differences;
    - name the main inputs whose amounts may differ;
    - say whether to switch the electricity to the target's grid.
  - The template's inputs and direct flows are copied, and the named inputs are fitted within
    0.5–2× of the template.
- **Metadata route (S3), prompts 4 and 5.**
  - `prompt-4-metadata.md` ([prompts/draft_from_metadata.md](prompts/draft_from_metadata.md))
    gives the model the dataset's own ecoSpold metadata and name.
  - Every input must quote the phrase that names it, and every amount has one basis:
    - `stoichiometry`: a balanced equation with the arithmetic written out;
    - `mass-balance`: an addition polymer carries 1 kg of monomer per kg;
    - `composition-split`: shares fitted under a mass constraint;
    - `named-only`: fitted;
    - `implied`: low confidence.
  - `prompt-5-map.md` maps the inputs.
  - For a chemical, the code adds the utility block every ecoinvent-v2 organic chemical in BAFU
    carries, as free inputs: electricity, heat, rail and lorry transport, and a chemical-plant
    share.

Two checks, each answered by a Claude Code session:

- **White packaging glass, template route:** the same score as the interactive spec, 53 of 1,146
  flows within ±10 %.
- **Polycarbonate, metadata route:** reproduces the interactive spec's stoichiometric amounts to
  the last digit (0.89777 kg bisphenol A, 0.38897 kg phosgene, 0.31459 kg NaOH).

Both drafts are in `specs/` with their evidence.

The per-dataset commands behind the batch are for debugging one dataset:

- `reverse-bafu locate|evidence|draft|assemble <code>`;
- `reverse-bafu draft <code> --dry-run` / `--from-response …`;
- `/draft-spec <code> --report … --pages …`.

### How the committed specs were made

The 51 rebuilds come from two sources:

- **7 from the report route.** Their prompts were answered by a Claude Code session and labelled
  so in their provenance.
- **44 interactive specs** (the files without `.draft`). An LLM wrote them in interactive Claude
  sessions guided by the team, before the automated routes existed.
  - They were written from the report, the dataset's own metadata, a same-product unit process,
    or reaction stoichiometry.
  - The 11 PlasticsEurope specs were generated by
    [scripts/build_plasticseurope_specs.py](scripts/build_plasticseurope_specs.py) and then
    calibrated.
  - Their `strategy.note`, `evidence` and the reports in `results/checks/` record the sources and
    the arithmetic. They have no per-input `derivation`; the template and metadata routes above
    make the same recipes reproducible.

Where both exist for a dataset, the interactive spec is the one counted, and the draft shows how
close the automated route gets.

The route labels:

| | |
|---|---|
| **S1**, transcription | The report prints this dataset's own inventory, one number per input. |
| **S2**, template transfer | A unit process of the same product exists (another site, grade or vintage). Its structure is reused and its amounts calibrated. |
| **S3**, top-down model | Something names the inputs but not every amount: printed ranges, a process description, stoichiometry, published comparison data. The calibration sets what the evidence leaves open. |

## 5. Rebuild the datasets from the specs

```bash
uv run reverse-bafu run-all             # every specs/*.json: resolve → calibrate → build → check
uv run reverse-bafu run-all --apply     # same, and calibrate writes the fitted amounts into the specs
```

`run-all` orders the specs so that one linking a rebuilt node runs after the spec that builds it
(e.g. cement links the rebuilt burnt shale). A spec whose inputs do not all resolve is recorded
as `unresolved` and does not stop the batch.

It writes `results/rebuild_status.csv`, with per spec:

- the status;
- how many of the 50 largest kilogram flows are within ±10 %;
- how much of the total kilogram mass is;
- how many of all flows are;
- the median deviation.

The committed specs already carry their calibrated amounts, so `run-all` without `--apply`
reproduces `results/checks/`, up to the round-off caveat under *Known limitations*. The nodes land in the Brightway database `reverse-bafu-sandbox`;
the original datasets are never touched.

The four steps, per spec (`uv run reverse-bafu run|resolve|calibrate|build|check specs/<spec>.json`
for one dataset):

| Step | Does | Writes |
|---|---|---|
| resolve | Maps every input name to a BAFU dataset: *unit* (link), *aggregated* (link, flag as dependency), *missing* (stop, suggest names). Checks units. | Codes into the spec; exit 2 on anything missing |
| calibrate | Bounded least squares for the inputs marked `free`, with the input list held fixed. See the notes below. | Prints spec vs fitted amounts; `--apply` writes them into the spec |
| build | The explicit node `<code>-disagg` and the hybrid `<code>-hybrid` (explicit + residual flows = the original, exactly) | `reverse-bafu-sandbox` |
| check | Flow-by-flow agreement: deviation buckets, the largest flows per unit, the worst deviations, kilogram mass covered, structural checks | `results/checks/<code>.md` |

How calibrate fits:

- One equation per elementary flow, weighted by 1/max(\|target\|, \|model\|), so the error counts
  as a relative error.
- Each (unit, compartment) group of flows counts equally.
- Round-off flows get weight 0.
- It is solved with an active-set solver (NNLS/BVLS) on the column-scaled system.

## 6. Benchmark: how well does the method recover a known unit process?

```bash
uv run reverse-bafu benchmark --n 100 --seed 7 --scenarios oracle,bounded,partial,distractors --name flow-n100-seed7
uv run reverse-bafu benchmark --n 100 --seed 7 --scenarios blind --name blind-n100-seed7
uv run reverse-bafu benchmark --n 100 --seed 7 --scenarios blind-all --name blind-all-n100-seed7   # ~1 h
```

**Two modes.**

- `--mode calibration` (the default) tests the calibrate step alone: the least-squares recovery
  of input *amounts* from an aggregated flow vector, given an input *list*. Its ground truth is
  free, so it runs without any model.
- `--mode extraction` (end of this section) tests the whole route from the PDF to the checked
  node. It needs the model.

**How it works.**

1. *Test set.* BAFU unit processes with 3–30 technosphere inputs, not among the 101 flagged,
   name not starting with `xx`. They are drawn round-robin over BAFU's top-level categories with
   a fixed seed, so 100 cases span transport, chemicals, agriculture and the rest. Their real
   inputs and amounts are the answer key.
2. *Synthetic system process.* For each case the cumulative inventory `B·A⁻¹·e` is computed. That
   is exactly what an ecoSpold `type=2` export of that process would contain, and it becomes the
   target.
3. *Evidence packages.* The same fit is run with candidate lists of decreasing quality:

   | Scenario | Candidate inputs | Bounds | Stands for |
   |---|---|---|---|
   | `oracle` | exactly the true inputs, amounts unknown | 0…∞ | a complete, correct table |
   | `bounded` | the true inputs | 0.5×–2× the true amount | a table with ranges |
   | `partial` | the true inputs minus the 30 % that explain the fewest flows | 0…∞ | a report that omits minor lines |
   | `distractors` | the true inputs plus 10 random processes used ≥ 30 times in BAFU | 0…∞ | an over-proposed list |
   | `blind` | every process used ≥ 30 times (~675), no direct flows | 0…∞ | no evidence, a restricted pool |
   | `blind-all` | every dataset in BAFU (~12,000), no direct flows | 0…∞ | no evidence at all |

4. *Fit.* Exactly the calibration of step 5, with no impact assessment. Above 2,000 candidates
   the NNLS runs on a working set (`lci.nnls_working_set`), about 30 s per case.
5. *Metrics per case and scenario* (`results/benchmark/<name>.csv`; `<name>.md` holds the medians):
   - the share of the target's flows reproduced within ±10 %;
   - the share of *material* inputs fitted within ±20 %: those that supply ≥ 1 % of some flow of
     the target;
   - false positives (wrong candidates given a material amount) and false negatives.

**Results** (`results/benchmark/flow-n100-seed7.md`, `blind-n100-seed7.md`,
`blind-all-n100-seed7.md`; the same 100 cases):

| Scenario | Flows within ±10 % (median) | Input amounts within ±20 % | Wrong inputs used (median) |
|---|---|---|---|
| `oracle` | 100 % | 772 / 786 | 0 |
| `bounded` | 100 % | 780 / 786 | 0 |
| `partial` | 99 % | 538 / 596 | 0 (1 material input lost) |
| `distractors` | 100 % | 770 / 786 | 0 |
| `blind` | 97 % | 264 / 599 | 96 |
| `blind-all` | 100 % | 149 / 786 | 71 |

**How to read it.**

- **With the right inputs on the list, the fit recovers the amounts.** The misses are mostly
  pairs of inputs whose cumulative inventories are (near-)identical, e.g. inert waste and gravel
  to the same landfill, where any split gives the same flows.
- **Ten wrong candidates are set to zero.** This is optimistic: a synthetic target is reproduced
  exactly by its true inputs, so a wrong candidate has nothing left to absorb. Real originals were
  computed on older background data.
- **With no list, the fit reproduces the flows with a made-up process** of 71–96 wrong inputs.
  This is the identifiability trap: a near-perfect inventory fit with the wrong structure.
  Blind-all shows it at its clearest. With every dataset on offer, the fit replaces crude oil from
  Libya by a mix of Algerian and Egyptian crude, and hard-coal electricity by coal CHP heat plus
  waste-incineration electricity.

### What the flow score counts

The flow score covers about 1,670 of the ~1,790 flows per target. The other ~120 are left out
because they are round-off.

**Why round-off exists.** A cumulative inventory solves for how much of each of the ~12,000
processes is needed. Supply chains loop, so that scaling vector spans up to 58 orders of
magnitude. A double keeps about 16 significant digits relative to its largest entry. Flows fed
only by entries below that floor come out of the sparse solve as round-off.

**How the round-off flows are found.** `lci.determined_flows` detects them directly: it takes one
step of iterative refinement and keeps the flows that barely move. The kept flows move by
~1e-10, the excluded ones by ~100 %. The threshold (`tol`) gives identical results at 1e-2 and
1e-3.

**Why not a size cutoff.** A cutoff on small amounts would drop named trace pollutants (dioxins
at 1e-17 kg, benzo[a]pyrene, mercury) and keep noise such as thorium-232 at −4e-26. The
refinement test keeps 640 of 650 named trace pollutants.

**The exclusion hides no real errors.** Doubling an input's amount in an otherwise perfect model
drops the score from 100 % to 0.7–58 %. Every CSV and check report prints the excluded count
next to the score.

Nothing is excluded for a system process without inputs. Those that keep waste-treatment links
(the PlasticsEurope and APME eco-profiles) exclude about 100–120 flows, as in the benchmark.

### Extraction mode: the whole route, including the PDF

```bash
uv run reverse-bafu benchmark --mode extraction --n 100 --seed 7 --name n100-seed7            # API route
uv run reverse-bafu benchmark --mode extraction --n 100 --seed 7 --name n100-seed7 --dry-run  # writes the pending prompts
```

Or run `/benchmark-extraction --n 100 --seed 7` inside Claude Code
([.claude/commands/benchmark-extraction.md](.claude/commands/benchmark-extraction.md)).

This mode tests everything steps 4 and 5 do, on cases with a known answer:

- The cases are BAFU *unit processes* whose cited report is in the documentation bundle.
- Each is treated exactly like a system process: locate → evidence → extract → map → assemble →
  resolve → calibrate → build → check.
- It uses the same state machine as `draft-all`, with files under
  `results/benchmark/extraction/`.
- The drafted spec is then compared with the process's real exchanges.

Metrics:

| Metric | Meaning |
|---|---|
| `inputs_matched` / `inputs_missed` / `inputs_extra` | true inputs recovered *and mapped to the right dataset*; true inputs absent; drafted inputs that are not in the process |
| `input_amounts_within_20pct` | of the matched inputs, how many amounts (after calibration) are within ±20 % of the real ones |
| `direct_flows_matched` | direct emissions and resources recovered (by substance and compartment) |
| `top_flows_within_10pct`, `kg_mass_covered_pct`, `flows_within_10pct` | the rebuilt node against the real process |

Results on 100 unit processes (seed 7, `results/benchmark/extraction-n100-seed7.md`; the prompts
were answered by a Claude Code session, labelled so in the provenance):

- For 42 of the 100, the locate step found no inventory table in the report.
- The other 58 were scored:
  - true inputs recovered and mapped to the right dataset: 56 % (recall); 71 % of the drafted
    inputs are true inputs (precision);
  - of the matched inputs, 233 of 262 amounts are within ±20 % after calibration;
  - direct flows recovered: 45 %;
  - the rebuilt node against the real process: median 76 % of flows within ±10 %.

## 7. Share the rebuilds: export and import

The rebuilt unit processes live in the Brightway sandbox of whoever ran `run-all`. To let
someone else add them to *their* BAFU-2026 project:

```bash
uv run python scripts/export_disaggregated.py                                    # -> exports/
uv run python scripts/import_disaggregated.py --project <their-project> --dry-run  # resolve, write nothing
uv run python scripts/import_disaggregated.py --project <their-project>            # add one new database
uv run python scripts/verify_import_roundtrip.py                                  # import into a scratch copy and compare
```

**The export** is a plain documented JSON, plus a flat CSV of the explicit exchanges. Per
dataset it holds:

- the name, location, unit and reference product;
- the BAFU code it replaces, and the route;
- every technosphere exchange, with its supplier's BAFU code;
- every elementary flow, with its EF 3.1 code and database;
- the residual block;
- the provenance, where the pipeline recorded it.

**The importer** links by code and creates one new database. It **refuses to write anything** if
a referenced code is missing in the target project, and names every one.

**Which node to use.** Import the `*-hybrid` nodes if you need results that match BAFU-2026;
they reproduce the originals to within 1e-6. Import the `*-disagg` nodes only if you want the
evidence-only model. Their agreement with the originals varies widely, and
[exports/README.md](exports/README.md) explains, dataset by dataset, where it can and cannot be
trusted.

## 8. Regenerate the pages and the deck's figures

The pages and figures are generated from the committed results. After `run-all`:

```bash
uv run python scripts/flow_comparison.py          # -> results/flow_comparison.json (original vs rebuilt, every flow)
uv run python scripts/build_flow_parity.py        # -> artifacts/flow-parity.html
uv run python scripts/climate_comparison.py       # -> results/climate_comparison.csv (EF 3.1 climate change, a cross-check)
uv run python scripts/ecoprofile_agreement.py     # -> results/ecoprofile_agreement.csv (the eco-profiles against their declared flows)
uv run python scripts/replacement_priority.py     # -> results/replacement_priority.{csv,md}
uv run python scripts/build_replacement_page.py   # -> artifacts/replacement-priority.html
uv run python scripts/render_pages.py             # -> artifacts/rebuilt-inventories.html
uv run python scripts/dump_calibration_detail.py  # -> results/benchmark/flow-n100-seed7-detail.json (feeds the benchmark page and plots)
```

The deck's plots are made by `scripts/slide_*.py`, and `scripts/slide_deck_pdf.py` prints the
deck to PDF (see [artifacts/presentation/README.md](artifacts/presentation/README.md); these need
google-chrome).

Some files have no generator:

- `results/usable_information.csv` is hand-curated: the classification behind "51 of 138" on the
  deck, with the reason for each dataset.
- The method explainer, the system-processes page, the code walkthrough and the calibration
  benchmark page are written by hand.

## Known limitations

- **The 44 interactive specs carry no per-input `derivation`.** Their sources and arithmetic are
  in `strategy.note`, `evidence` and the check reports. The drafted specs are fully traceable.
- **The flow score means little for 12 APME eco-profiles.** These originals declare only ~130
  flows themselves. The other ~1,500 reach them as trace amounts through eight waste-treatment
  links, and a rebuild on ecoinvent chemicals overshoots those traces by about ×150. The 12 are
  the worst matches in the pooled parity plot. `results/ecoprofile_agreement.csv` scores them
  against their declared flows instead.
- **Direct emissions without a sub-compartment** resolve to EF 3.1's "unspecified" one, where
  BAFU rarely books them. Row by row this moves some flows (NOₓ) between air sub-compartments.
  Summed over compartments, as in `flow_comparison.json`'s headline emissions, it cancels. The
  template route keeps the template's exact compartment.
- **Which flows count as round-off depends slightly on the whole matrix.** The matrix includes
  every node in the sandbox, so rebuilding after other specs were added moves a dataset's "flows
  within ±10 %" by up to ~1 % of its flows. The 50 largest flows and the kilogram mass do not
  move. The committed results are the ones presented; a rerun reproduces them to within this.
- **One wrong bound.** The anthraquinone draft's sulphuric-acid lower bound is 0.78336 kg (the
  48 % concentration applied twice); it should be 1.632.
- **The benchmark's synthetic targets are reproduced exactly by their true inputs.** That favours
  the `distractors` scenario (see above).

## Layout

```
src/reverse_bafu/   the pipeline: cli, spec, db, lci, resolve, calibrate, build, check, runall, draft, benchmark
scripts/            step 3: list_system_terminated, list_sources, find_system_processes, ecoprofile_consumers
                    step 7: export_disaggregated, import_disaggregated, verify_import_roundtrip
                    step 8: flow_comparison, build_flow_parity, climate_comparison, ecoprofile_agreement,
                            replacement_priority, build_replacement_page, render_pages, dump_calibration_detail,
                            slide_*.py (the deck), templates/
                    specs: build_plasticseurope_specs (the 11 PlasticsEurope specs' starting values)
                    diagnostics behind statements in exports/README.md: transcription_vs_truth,
                            plasticseurope_infrastructure_diagnostic, verify_determined_flows
prompts/            the LLM prompt templates: locate_pages, draft_spec (extract), map_inputs,
                    draft_from_template, draft_from_metadata; and concept_flow_based_error_diagnosis,
                    a proposal for tracing a rebuild's deviations back to its inputs (not implemented)
specs/              one JSON per rebuild; specs/evidence/<code>/ = the drafting records
results/            system_terminated.csv (101), system_terminated_extended.csv (138), sources.csv, dois.csv,
                    usable_information.csv, drafting_status.csv, rebuild_status.csv, checks/,
                    flow_comparison.json, climate_comparison.csv, ecoprofile_agreement.csv,
                    replacement_priority.{csv,md}, benchmark/
exports/            the shareable export of the rebuilds + its README (format, import, quality limits)
artifacts/          the documentation pages (see "Where to read what") and presentation/, the deck
references.txt      the two papers referenced, with their role for this project
LICENSE, NOTICE     Apache-2.0, for the code (see Licence and citation)
.claude/commands/   /draft-all, /draft-spec, /benchmark-extraction
```

## Licence and citation

The repository holds four kinds of material, under different terms:

| What | Where | Terms |
|---|---|---|
| Code | `src/`, `scripts/`, `prompts/`, `.claude/commands/` | [Apache-2.0](LICENSE) (see also [NOTICE](NOTICE)) |
| Text written by the contributors: this README, the documentation pages, the presentation | `*.md`, `artifacts/` | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| BAFU-2026 data and data derived from it: the export, the results, the numbers in the specs and those shown in the pages | `exports/`, `results/`, `specs/`, `artifacts/` | the [BAFU:2026 Terms of Use](https://www.bafu.admin.ch/dam/en/sd-web/-9ZObeMCZy8A/BAFU_2025_TermOfUse_EN_Webpage.pdf) |
| Quotations from the BAFU documentation reports: page excerpts, quoted lines, table and figure captions, the report screenshots in the deck | `specs/evidence/`, `results/benchmark/extraction/evidence/`, `artifacts/presentation/screenshots/` | the copyright of the reports' authors |

**BAFU-2026 data.** The rebuilt unit processes are *modified data* in the sense of the BAFU Terms
of Use, so they are shared on the same terms (section 3.4):

- free to use, process and analyse, e.g. in LCA studies;
- not to be sold, resold, or distributed separately or as part of another database;
- labelled as modified, never presented as the original datasets;
- not presented as endorsed by BAFU.

The changes are documented dataset by dataset in [exports/README.md](exports/README.md) and the
specs, as section 3.2 requires. Any use must credit the source:

> Source: Life Cycle Inventory database of the Swiss Federal Administration, BAFU:2026.

**Report quotations.** The excerpts of the reports are included so that every number can be traced
to the line it came from, each with its source (report, page, table). They remain the work of the
reports' authors. The Apache-2.0 and CC BY licences above do not cover them.

**What is not here.** The BAFU files themselves stay out of the repository (`.gitignore`: `*.zip`,
`data/`, `BAFU-2026 v1_Documentation/`); download them from openLCA Nexus as described in step 1.
