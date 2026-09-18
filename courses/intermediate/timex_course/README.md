# Time-explicit LCA with `bw_timex` — BrightCon 2026 intermediate course

Three hours, hands-on: how to put a product system in time, and what changes once you do.
The running example is a Danish *sommerhus* — built of wood, heated with a heat pump, lived in
for 50 years, then demolished.

## The material

| | | what it covers |
|---|---|---|
| 0 | [`0_start_here.ipynb`](0_start_here.ipynb) | Welcome, schedule, and the one-time setup that fetches the Brightway project. **Start here.** |
| 1 | [`1_intro.pdf`](1_intro.pdf) | Why time matters in LCA, and the ideas the notebooks put to work. |
| 2 | [`2_quick_walkthrough.ipynb`](2_quick_walkthrough.ipynb) | The whole workflow start to finish on a small electric-vehicle case: from a static LCA to a time-explicit one. Just a showcase. |
| 3 | [`3_sommerhus.ipynb`](3_sommerhus.ipynb) | Time-explicit case study on a danish *sommerhus*: When each process happens, how timing propagates along the supply chain, which background database a process is served from, and how much that changes the score. |
| 4 | [`4_dynamic_characterization.ipynb`](4_dynamic_characterization.ipynb) | Impacts as functions of time instead of single numbers: emissions characterized by when they occur, radiative forcing vs. GWP, the choice of time horizon, and writing your own characterization function. |
| 5 | [`5_sommerhus_dynamic.ipynb`](5_sommerhus_dynamic.ipynb) | Both together: the *sommerhus* characterized dynamically over its 190 year life cycle. What the time horizon does to a long-lived system, and your own characterization function applied to it. |

The product system itself is ordinary Brightway with no time in it and lives in
[`sommerhus_system.py`](sommerhus_system.py) next to the notebooks; its temporal information is
[`sommerhus_temporal.py`](sommerhus_temporal.py). Notebook 3 writes that temporal part out by
hand, notebook 5 imports it. Nothing you need to worry about.

## Solutions and the escape hatch

[`solutions/`](solutions) has one folder per notebook, holding that notebook's solved version
and one script per exercise.

Every exercise in the student notebooks is followed by a cell like

```python
# Stuck, or out of time? Uncomment the line below, run this cell twice,
# and you're back in sync with everyone else.
# %load solutions/3_sommerhus/1_temporal_distributions.py
```

Uncomment, run twice, and you are caught up — the solution code snippet is added in for you.

## Further infos

Package documentations:
* [`bw_timex` documentation](https://docs.brightway.dev/projects/bw-timex/en/latest/)
* [`dynamic_characterization` documentation](https://dynamic-characterization.readthedocs.io)

Papers:
* [IJLCA Paper on time-explicit LCA in general](https://link.springer.com/article/10.1007/s11367-025-02539-3)
* [JOSS Paper on `bw_timex`](https://joss.theoj.org/papers/10.21105/joss.09621)

## Environment

The Python kernel is already installed on the course server, and the `timex_brightcon` project is
restored from a backup in [`0_start_here.ipynb`](0_start_here.ipynb) — that is all you need during
the course. To build the project from scratch instead:

To reproduce the environment locally, first [install `uv`](https://docs.astral.sh/uv/getting-started/installation/).

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
