# Time-explicit LCA with `bw_timex` — BrightCon 2026 intermediate course

Three hours, hands-on: how to put a product system in time, and what changes once you do.
The running example is a Danish *sommerhus* — built of wood, heated with a heat pump, lived in
for 50 years, then demolished.

## The material

| | | what it covers |
|---|---|---|
| 0 | [`0_slides.pptx`](0_slides.pptx) | Intro: what time-explicit LCA is for, and the ideas the notebooks then put to work. |
| 1 | [`1_quick_walkthrough.ipynb`](1_quick_walkthrough.ipynb) | The whole workflow in one sitting, on the electric-vehicle case study from the `bw_timex` docs: the product system in ordinary Brightway, a standard static LCA, temporal distributions on every exchange, then `build_timeline()` / `lci()` / `static_lcia()` and the waterfall chart over time. Nothing to solve - it is the map of where the next three notebooks go into detail. |
| 2 | [`2_sommerhus.ipynb`](2_sommerhus.ipynb) | The case study. Temporal distributions on exchanges, convolution along the supply chain, temporal evolution of an amount, background vintages and `representative_time`, the timeline and its temporal market shares, static vs time-explicit score, a first `dynamic_lcia`, and `TimexLCA.compare()` across move-in decades. Two TDs are yours to write. |
| 3 | [`3_dynamic_characterization.ipynb`](3_dynamic_characterization.ipynb) | The `dynamic_characterization` package on its own terms. The `date`/`amount`/`flow`/`activity` inventory, the `characterize()` wrapper and the `{flow_id: function}` mapping, IPCC AR6 functions, fixed vs flexible time horizons, radiative forcing vs GWP, prospective (Watanabe) characterization factors, and writing a characterization function from scratch. Seven exercises. |
| 4 | [`4_sommerhus_dynamic.ipynb`](4_sommerhus_dynamic.ipynb) | The two put together: the *sommerhus* inventory characterized dynamically. Radiative forcing over its 190 years, `fixed_time_horizon` on a system whose flows straddle the functional unit, a `TimexLCA.compare()` sweep over horizon lengths, and a characterization function of your own — a well-water flow drawn across the summer, weighted by the month it happens in, then made prospective. Five exercises. |

The product system itself is ordinary Brightway with no time in it and lives in
[`sommerhus_system.py`](sommerhus_system.py) next to the notebooks; its temporal information is
[`sommerhus_temporal.py`](sommerhus_temporal.py). Notebook 2 writes that temporal part out by
hand, notebook 4 imports it.

## Solutions and the escape hatch

[`solutions/`](solutions) has one folder per notebook, each holding that notebook's solved
version and one script per exercise, numbered in the order the exercises appear:

```
solutions/
  2_sommerhus/
    2_sommerhus_SOLVED.ipynb
    1_temporal_distributions.py
    sommerhus_system.py                     copy of the model module, so the notebook runs here
  3_dynamic_characterization/
    3_dynamic_characterization_SOLVED.ipynb
    1_characterize_inventory.py … 7_apply_water_function.py
  4_sommerhus_dynamic/
    4_sommerhus_dynamic_SOLVED.ipynb
    1_fixed_time_horizon.py · 2_time_horizon_sweep.py · 3_water_flow.py
    4_water_characterization.py · 5_water_prospective.py
    sommerhus_system.py · sommerhus_temporal.py
```

The `sommerhus_*.py` files inside those folders are generated copies of the ones next to the
notebooks — each solved notebook keeps what it imports in its own directory, so no notebook
needs to fiddle with `sys.path`. Edit the copies and the next build overwrites them.

Every exercise in the student notebooks is followed by a cell like

```python
# Stuck, or out of time? Uncomment the line below, run this cell twice,
# and you're back in sync with everyone else.
# %load solutions/2_sommerhus/1_temporal_distributions.py
```

Uncomment, run twice, and you are caught up — nothing later in the notebook depends on having
solved it yourself. (`%load` pastes the file into the cell, so the cell no longer holds the
`%load` line afterwards; re-running the build scripts restores it.)

## Generated notebooks — do not hand-edit

| generated | from |
|---|---|
| `2_sommerhus.ipynb`, `4_sommerhus_dynamic.ipynb` and the contents of `solutions/2_sommerhus/` and `solutions/4_sommerhus_dynamic/` | [`.course/build_sommerhus.py`](.course/build_sommerhus.py) |
| `3_dynamic_characterization.ipynb` and the contents of `solutions/3_dynamic_characterization/` | [`.course/build_dyncar.py`](.course/build_dyncar.py), from the authored master in `.course/sources/` |

`1_quick_walkthrough.ipynb` and the two `sommerhus_*.py` modules next to the notebooks are
hand-written; the copies under `solutions/` are not.

Each script writes the student notebook and the solved notebook from one source, so the two
cannot drift apart. Change the script (or, for notebook 3, the master in `.course/sources/`),
then run

```sh
./.course/check_all.sh
```

which rebuilds everything and executes every notebook end to end: each solved version, each
student version as a student who solved nothing would run it, and again with every escape
hatch loaded. It takes about four minutes and needs the databases below.

Further reading: the [`bw_timex` documentation](https://docs.brightway.dev/projects/bw-timex/en/latest/)
and the [`dynamic_characterization` documentation](https://dynamic-characterization.readthedocs.io).

Everything that is not course material - the build scripts and the authored master of
notebook 3 - sits in the hidden `.course/` directory, so the course folder shows only the
slides, the notebooks, `solutions/` and this README. Note that JupyterLab does not serve hidden paths
unless the server sets `ContentsManager.allow_hidden = True`, so the `.course/...` links above
open in an editor or on GitHub, not in the Jupyter file browser.

## Environment

The Python kernel is already installed on the course server. To reproduce the environment locally, first [install `uv`](https://docs.astral.sh/uv/getting-started/installation/).

Then clone this repository to a folder of your liking, navigate there in your terminal, and run:

```sh
uv sync
```

Finally, recreate the databases we use for the course as follows, plugging in your ecoinvent 
credentials and the premise key:

```python
import bw2data as bd
from bw_timex import ensure_scenario_databases

bd.projects.set_current("timex_brightcon")

ensure_scenario_databases(
	{
		"iam_model": "remind-eu",
		"pathway": "SSP2-NDC",
		"system_model": "cutoff",
		"ecoinvent_version": "3.12",
		"years": [2020, 2030, 2040, 2050],
	},
	premise_key="dummy_premise_decryption_key",
	ecoinvent_credentials=("dummy_user", "dummy_password"),
)
```

That gives the `timex_brightcon` project: ecoinvent 3.12 cutoff plus four premise vintages
(2020 / 2030 / 2040 / 2050) from REMIND-EU SSP2-NDC, each carrying the `representative_time`
metadata that `TimexLCA` reads by itself.
