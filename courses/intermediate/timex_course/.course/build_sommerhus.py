"""Build the sommerhus notebooks.

    2_sommerhus.ipynb          - what the students open (exercise cells blank)
    4_sommerhus_dynamic.ipynb  - after the dynamic characterization notebook

plus, in `solutions/<notebook>/`, the solved version of each and one escape-hatch script per
exercise.

The product system lives in `sommerhus_system.py`, its temporal information in
`sommerhus_temporal.py`; each solved notebook gets a generated copy of what it imports. Notebook 2 writes the temporal part out by hand; notebook 4
imports it. Cells tagged `role="solution"` are blanked (and their source written to
`solutions/`) for the student version, `role="answer"` cells are dropped from it.

Verify with `./scripts/check_all.sh`.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from nbtools import code, for_solutions_dir, md, save  # noqa: E402

HERE = Path(__file__).resolve().parent.parent
SOLUTIONS = HERE / "solutions"
NB1 = SOLUTIONS / "2_sommerhus"
NB3 = SOLUTIONS / "4_sommerhus_dynamic"

FLOWCHART = """```mermaid
flowchart LR
    tree(🌲 timber tree):::fg-->timber
    timber(🪵 structural timber production):::fg-->construction
    glass_wool(🧵 market for glass wool mat):::ei-->construction
    construction(🏗️ sommerhus construction):::fg-->living
    heat_pump(🔥 heat pump, brine-water 10kW):::ei-->living
    grid(⚡ market group for electricity, low voltage):::ei-->living
    living(🏠 living in the sommerhus):::fg-->waste_wood(🔥 incineration of waste wood):::fg
    living-->fu(FU: 50 years of habitation)

    classDef ei color:#222832, fill:#3fb1c5, stroke:none;
    classDef fg color:#222832, fill:#9c5ffd, stroke:none;
```

<span style="color:#9c5ffd">■</span> foreground &nbsp;&nbsp;
<span style="color:#3fb1c5">■</span> background (premise vintages 2020 / 2030 / 2040 / 2050)
"""


MODULE_NOTE = "# Generated copy of ../../{name} - edit that one and re-run the build.\n"


def copy_modules(names, destination):
    """Put a copy of each model module next to a solved notebook."""
    for name in names:
        (destination / name).write_text(MODULE_NOTE.format(name=name) + (HERE / name).read_text())
        print(f"wrote {destination.relative_to(HERE)}/{name}")


def notebook(cells):
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.12"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


# ======================================================================================
# Notebook 2 - the case study
# ======================================================================================
part1 = [
    md(f"""# Time-explicit LCA of a Danish *sommerhus*

Built of wood, heated with a heat pump, lived in for 50 years.

{FLOWCHART}
"""),
    md("""## 0 | The product system

We make the following assumptions:
"""),
    code('''LIFETIME = 50  # years, EN 15978 reference service life for a building
TIMBER_VOLUME = 12  # m3 of structural timber in the frame
INSULATION_MASS = 1200  # kg of glass wool
HEAT_PUMPS = 3  # bought over the lifetime: one plus two replacements
ELECTRICITY_PER_YEAR = 1400  # kWh/a: hot water (heat-pump-assisted) plus household

BG_DATABASE = "ei_cutoff_3.12_remind-eu_SSP2-NDC_2020"
METHOD = ("IPCC 2021", "climate change", "GWP 100a, incl. H and bio CO2")
'''),
    md("""We've prepared the code to set up the sommerhus system with all its nodes and edges in [`sommerhus_system.py`](sommerhus_system.py) to save some time. Have a look if you want to see
how - but it's just normal brightway stuff."""),
    code('''from sommerhus_system import build_system

foreground = build_system(
    lifetime=LIFETIME,
    timber_volume=TIMBER_VOLUME,
    insulation_mass=INSULATION_MASS,
    heat_pumps=HEAT_PUMPS,
    electricity_per_year=ELECTRICITY_PER_YEAR,
    background_database=BG_DATABASE,
    method=METHOD,
)
[node["name"] for node in foreground]
'''),
    md("""### The functional unit, and a static LCA to compare against

50 years of living in the *sommerhus*:
"""),
    code('''import bw2calc as bc
import bw2data as bd

living = bd.get_node(database="foreground", name="living in the sommerhus")

static_lca = bc.LCA({living: 1}, METHOD)
static_lca.lci()
static_lca.lcia()

print(f"static score: {static_lca.score:,.0f} kg CO2-eq")
'''),
    # ------------------------------------------------------------------ temporal info
    md("""## 1 | When does what happen?

A `TemporalDistribution` says what **share** of an exchange happens **when**, relative to the
process consuming it.

Three of them are given below as examples: the **timber delivery**, the **tree's CO2 uptake**
and the **electricity use**. Two more are yours to write, further down.
"""),
    code('''import numpy as np
from bw_timex import TemporalDistribution, easy_timedelta_distribution

# The timber and the insulation arrive over the last nine months before move-in.
# We create this one directly from the TemporalDistribution class, specifying date and amount arrays.
td_construction = TemporalDistribution(
    date=np.array([-9, -6, -2, -1], dtype="timedelta64[M]"),  # months before the consumer
    amount=np.array([0.2, 0.3, 0.3, 0.2]),                    # shares, summing to 1
)

# The tree grows for 40 years before it is felled. Its uptake *rate* is bell-shaped (slow
# start, fast middle, tapering off), which makes the carbon stock an S-curve.
# Here, we use the easy_timedelta_distribution function that helps with more complex setups.
td_biogenic_uptake = easy_timedelta_distribution(
    start=-40, end=0, resolution="Y", steps=41, kind="normal", param=0.2
)

# Electricity is used evenly over the years of habitation.
td_electricity = easy_timedelta_distribution(
    start=0, end=LIFETIME, resolution="Y", steps=LIFETIME + 1, kind="uniform"
)
''', section="given_tds"),
    md("""Let's have a look:"""),
    code('''td_construction.graph(resolution="M")
''', section="given_tds"),
    code('''td_biogenic_uptake.graph(resolution="Y")
''', section="given_tds"),
    md("""Along a supply chain, the TDs of consecutive exchanges are **convolved** together: the dates are shifted against one another, the amounts multiply. Have a look, and try to grasp what's going on. You can also create some TDs yourself to test if your intuition is right."""),
    code('''(td_construction * td_biogenic_uptake).graph(resolution="M")
''', section="convolution"),
    md("""A TD belongs on an **exchange**.
[`add_temporal_distribution_to_exchange`](https://docs.brightway.dev/projects/bw-timex/en/latest/content/api/bw_timex/utils/index.html)
finds the exchange for you - give it enough to identify producer and consumer unambiguously:
"""),
    code('''from bw_timex.utils import add_temporal_distribution_to_exchange

add_temporal_distribution_to_exchange(
    td_construction,
    input_name="structural timber production, carbon split",
    output_name="sommerhus construction, wood",
)

add_temporal_distribution_to_exchange(
    td_construction,
    input_name="market for glass wool mat",  # a background node, so pin it down further
    input_location="GLO",
    input_database=BG_DATABASE,
    output_name="sommerhus construction, wood",
)

add_temporal_distribution_to_exchange(
    td_biogenic_uptake,
    input_name="Carbon dioxide, in air",  # a biosphere flow works just the same
    output_name="timber tree",
)

add_temporal_distribution_to_exchange(
    td_electricity,
    input_name="market group for electricity, low voltage",
    input_location="GLO",
    input_database=BG_DATABASE,
    output_name="living in the sommerhus",
)

''', section="given_tds"),
    # ------------------------------------------------------------------- student slot
    md("""### 🛠️ Your turn: the last two

Two exchanges in the product system above still carry to TD. If we leave it like that, `bw_timex` will assume they are instant - but we don't want that. Come up with TDs for the remaining exchanges and attach them.

> The heat pump is a background node (`"heat pump production, brine-water, 10kW"`, location `"RoW"`), the incineration is in the foreground.
"""),
    code('''# heat pumps: at move-in, and two replacements
td_heat_pumps = TemporalDistribution(
    date=np.array([0, 17, 34], dtype="timedelta64[Y]"), amount=np.array([1 / 3, 1 / 3, 1 / 3])
)

# demolition, three months after the lifetime is up
td_eol = TemporalDistribution(
    date=np.array([LIFETIME * 12 + 3], dtype="timedelta64[M]"), amount=np.array([1])
)

add_temporal_distribution_to_exchange(
    td_heat_pumps,
    input_name="heat pump production, brine-water, 10kW",
    input_location="RoW",
    input_database=BG_DATABASE,
    output_name="living in the sommerhus",
)

add_temporal_distribution_to_exchange(
    td_eol,
    input_name="incineration of waste wood",
    output_name="living in the sommerhus",
)
''', section="student_tds", file="1_temporal_distributions.py", role="solution", todo='''# TODO: write td_heat_pumps and td_eol (see the table above) and attach them with
#       add_temporal_distribution_to_exchange(...)
'''),
    code('''# CHECKPOINT - all six exchanges should carry a temporal distribution now
from bw_timex.utils import get_exchange

CONSTRUCTION = "sommerhus construction, wood"
LIVING = "living in the sommerhus"

for label, kwargs in [
    ("timber -> construction",
     dict(input_name="structural timber production, carbon split", output_name=CONSTRUCTION)),
    ("insulation -> construction",
     dict(input_name="market for glass wool mat", input_location="GLO",
          input_database=BG_DATABASE, output_name=CONSTRUCTION)),
    ("CO2 uptake of the tree",
     dict(input_name="Carbon dioxide, in air", output_name="timber tree")),
    ("electricity -> living",
     dict(input_name="market group for electricity, low voltage", input_location="GLO",
          input_database=BG_DATABASE, output_name=LIVING)),
    ("heat pumps -> living",
     dict(input_name="heat pump production, brine-water, 10kW", input_location="RoW",
          input_database=BG_DATABASE, output_name=LIVING)),
    ("living -> incineration",
     dict(input_name="incineration of waste wood", output_name=LIVING)),
]:
    exchange = get_exchange(**kwargs)
    print(f"{label:<28} {'ok' if 'temporal_distribution' in exchange else 'MISSING'}")
''', section="checkpoint"),
    md("""### Amounts that change over time

A TD is only about distributing *when* an exchange happens. By itself, it doesn't change the (total) amount of that exchange. For that there is **temporal
evolution factors**: factors at given dates, linearly interpolated in between, held constant outside.

For our *sommerhus*, we assume that we, as habitants, reduce our electricity demand by 1% of the original demand per year.

It goes on the very exchange that already carries the electricity TD - *when* an exchange
happens and *how much* of it happens are two separate pieces of information on one edge.
"""),
    code('''from datetime import datetime

from bw_timex.utils import add_temporal_evolution_to_exchange

add_temporal_evolution_to_exchange(
    temporal_evolution_factors={
        datetime(2025, 1, 1): 1.0,
        datetime(2075, 1, 1): 0.5,  # -1% of the 2025 demand per year after interpolation
    },
    input_name="market group for electricity, low voltage",
    input_location="GLO",
    input_database=BG_DATABASE,
    output_name="living in the sommerhus",
)
'''),
    md("""The factor is looked up at each point in time the exchange occurs. This is what it
looks like over the lifetime of the house:
"""),
    code('''from bw_timex import get_temporal_evolution_factor

factors = {datetime(2025, 1, 1): 1.0, datetime(2075, 1, 1): 0.5}
years = range(2020, 2091)

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 3))
plt.plot(list(years), [get_temporal_evolution_factor(factors, datetime(y, 1, 1)) for y in years])
plt.ylabel("factor on the grid draw")
plt.xlabel("year")
plt.ylim(0, 1.1)
plt.tight_layout()
plt.show()
'''),
    # ------------------------------------------------------------ background databases
    md("""## 2 | The background, in several vintages

So far everything referred to one background database, the 2020 vintage. But the project holds
four, built with [premise](https://github.com/polca/premise) from the **REMIND-EU SSP2-NDC**
scenario on top of **ecoinvent 3.12 cutoff**: 2020, 2030, 2040 and 2050.
"""),
    code('''[name for name in bd.databases if name.startswith("ei_cutoff")]
'''),
    md("""What makes them usable for us is their metadata. premise writes the point in time each
database represents into the database itself:
"""),
    code('''dict(bd.databases[BG_DATABASE])
'''),
    md("""`representative_time` is the key part. `TimexLCA` reads it by itself, so we never have
to tell it which database is which year - and for every process it places in time, it sources
from the vintage(s) nearest to that moment. (If your databases do not carry the metadata, you
can set it with `bw_timex.set_database_metadata`, or pass `database_dates` to `TimexLCA`.)
"""),
    code('''for name in sorted(n for n in bd.databases if n.startswith("ei_cutoff")):
    print(f"{name:<45} {bd.databases[name]['representative_time']}")
'''),
    # ---------------------------------------------------------------------- timeline
    md("""## 3 | The timeline

Which process happens when, and which background vintage(s) it is sourced from
(`temporal_market_shares`).
"""),
    code('''from bw_timex import TimexLCA

tlca = TimexLCA({living: 1}, METHOD)
tlca.build_timeline(starting_datetime="2025-01-01", temporal_grouping="month")
'''),
    code('''electricity_rows = tlca.timeline[
    tlca.timeline["producer_name"] == "market group for electricity, low voltage"
]
electricity_rows[
    ["date_producer", "amount", "temporal_evolution_factor", "temporal_market_shares"]
].head(10)
'''),
    md("""### 🔍 Explore

1. How many electricity rows are there, and what differs between them?
2. Pick a row in the 2040s and look at its `temporal_market_shares`. Why is it split over two
   databases - and what would a row in 2030 look like?
3. Find the earliest row in the whole timeline. Which process is it, and why that one?
4. In `.build_timeline`, we implicitly use the default setting graph_traversal="priority". Test the other option, have a look at the computation time, and think about the differences.
""", role="explore"),
    md("""One row per year of the lifetime. The TD is uniform, so the *base* amount is the same
everywhere, but each row shows it already scaled by that year's evolution factor - so the
amounts fall from 1400 kWh towards 700. What also differs is the background vintage behind
each row. A row in 2045 sits halfway between the 2040 and
2050 vintages and takes half from each, a row in 2030 sits exactly on the 2030 vintage and
takes all of it. That interpolation is what `bw_timex` calls a **temporal market**.

The earliest row is the timber delivery in 2024, not the tree: the tree's uptake sits on a
*biosphere* exchange, and the timeline only tracks technosphere producer/consumer pairs. It
shows up once the dynamic inventory is built.
""", role="answer"),
    md("""## 4 | Time-explicit inventory and score"""),
    code('''tlca.lci()
tlca.static_lcia()

print(f"static:        {static_lca.score:,.0f} kg CO2-eq")
print(f"time-explicit: {tlca.static_score:,.0f} kg CO2-eq")
'''),
    # -------------------------------------------------------------------------- LCIA
    md("""## 5 | Dynamic characterization

The inventory still knows *when* each emission happens, so it can be characterized
dynamically instead of with one static factor for everything.
"""),
    code('''tlca.dynamic_lcia(metric="GWP", time_horizon=100)
print(f"dynamic GWP100: {tlca.dynamic_score:,.0f} kg CO2-eq")
'''),
    code('''from bw_timex.utils import plot_characterized_inventory_as_waterfall

# one bar per year over a century is a lot of labels, so label every fifth one
plot_characterized_inventory_as_waterfall(tlca, xtick_interval=5)
'''),
    md("""*How that characterization works, and what else it can do, is the next notebook.*"""),
    # ----------------------------------------------------------------------- compare
    md("""## 6 | Same house, different decade

`TimexLCASettings` bundles one run, `TimexLCA.compare()` runs a list of them. Here: the same
*sommerhus*, moved into in 2025, 2035 and 2045.
"""),
    code('''from dataclasses import replace

from bw_timex import TimexLCASettings

settings_2025 = TimexLCASettings(
    demand={living: 1},
    method=METHOD,
    timeline={"starting_datetime": "2025-01-01", "temporal_grouping": "month"},
    lcia={"metric": "GWP", "time_horizon": 100},
    label="move in 2025",
)

comparison = TimexLCA.compare(
    [
        settings_2025,
        replace(settings_2025, starting_datetime="2035-01-01", label="move in 2035"),
        replace(settings_2025, starting_datetime="2045-01-01", label="move in 2045"),
    ]
)
comparison.summary[["label", "dynamic_score"]]
'''),
    md("""## Time for a break, mh? ☕"""),
]


HATCH = (
    "# Stuck, or out of time? Uncomment the line below, run this cell twice,\n"
    "# and you're back in sync with everyone else.\n"
    "# %load {file}\n"
)


def student_version(cells, solutions_dir):
    """Blank the solution cells, drop the answers, write the escape hatches.

    `solutions_dir` is the notebook's own folder under `solutions/`; it holds both the escape
    hatch scripts and the solved notebook.
    """
    solutions_dir.mkdir(parents=True, exist_ok=True)
    here = solutions_dir.relative_to(solutions_dir.parent.parent)
    out = []
    for cell in cells:
        meta = cell.get("metadata", {}).get("brightcon", {})
        role = meta.get("role")
        if role == "answer":
            continue
        if role == "solution":
            todo = meta.get("todo")
            assert todo, "a solution cell needs `todo` text for the student version"
            name = meta.get("file", f"{meta.get('section', 'exercise')}.py")
            (solutions_dir / name).write_text("".join(cell["source"]).rstrip() + "\n")
            print(f"wrote {here}/{name}")
            keep = {k: v for k, v in meta.items() if k not in ("todo", "file")}
            out.append(code(todo, **keep))
            out.append(
                code(
                    HATCH.format(file=f"{here}/{name}"),
                    section=meta.get("section"),
                    role="hatch",
                )
            )
            continue
        out.append(cell)
    return out


students = student_version(part1, NB1)
save(notebook(students), HERE / "2_sommerhus.ipynb")
print(f"wrote 2_sommerhus.ipynb with {len(students)} cells (student version)")

save(notebook(for_solutions_dir(part1)), NB1 / "2_sommerhus_SOLVED.ipynb")
print(f"wrote solutions/2_sommerhus/2_sommerhus_SOLVED.ipynb with {len(part1)} cells")
copy_modules(["sommerhus_system.py"], NB1)


# ======================================================================================
# Notebook 4 - dynamic characterization of the same house
# ======================================================================================
part3 = [
    md(f"""# The *sommerhus*, characterized dynamically

Notebook 2 gave the house a **timeline**. This notebook asks what the timing of its emissions
does to the **impact**, with the dynamic characterization from the previous session - now on a
real inventory instead of a handful of dummy rows.

Two things are yours to work out: how the **time horizon** is counted (section 3), and a
**characterization function of your own** (section 4).

{FLOWCHART}
"""),
    md("""## 0 | The model from notebook 2

System and temporal information are imported rather than retyped -
[`sommerhus_system.py`](sommerhus_system.py) and
[`sommerhus_temporal.py`](sommerhus_temporal.py) hold exactly what you wrote by hand before.
"""),
    code('''import bw2data as bd

from sommerhus_system import build_system
from sommerhus_temporal import add_temporal_information

LIFETIME = 50
BG_DATABASE = "ei_cutoff_3.12_remind-eu_SSP2-NDC_2020"
METHOD = ("IPCC 2021", "climate change", "GWP 100a, incl. H and bio CO2")

build_system(
    lifetime=LIFETIME,
    timber_volume=12,
    insulation_mass=1200,
    heat_pumps=3,
    electricity_per_year=1400,
    background_database=BG_DATABASE,
    method=METHOD,
)
add_temporal_information(lifetime=LIFETIME, background_database=BG_DATABASE)

living = bd.get_node(database="foreground", name="living in the sommerhus")
'''),
    code('''from bw_timex import TimexLCA

tlca = TimexLCA({living: 1}, METHOD)
tlca.build_timeline(starting_datetime="2025-01-01", temporal_grouping="month")
tlca.lci()
tlca.static_lcia()

print(f"time-explicit, static characterization: {tlca.static_score:,.0f} kg CO2-eq")
'''),
    md("""## 1 | The inventory, before any characterization

`tlca.dynamic_inventory_df` is the `date` / `amount` / `flow` / `activity` dataframe you
already know - only this one comes out of a real supply chain. The tree's uptake sits decades
before the house exists. (Positive here means *taken out of the air*: this is a natural
resource flow, and the sign flips once it is characterized.)
"""),
    code('''import matplotlib.pyplot as plt

uptake_flow = bd.get_node(
    database=bd.config.biosphere,
    name="Carbon dioxide, in air",
    categories=("natural resource", "in air"),
)
uptake_over_time = (
    tlca.dynamic_inventory_df[tlca.dynamic_inventory_df["flow"] == uptake_flow.id]
    .groupby("date")["amount"]
    .sum()
    .sort_index()
)

fig, ax = plt.subplots(figsize=(13, 3))
ax.plot(uptake_over_time.index, uptake_over_time.values, marker="o", linestyle="none")
ax.axhline(0, color="black", linewidth=0.8)
ax.set_ylabel("kg CO2 taken up")
plt.tight_layout()
plt.show()
'''),
    md("""## 2 | Radiative forcing over time

`metric="radiative_forcing"` characterizes each emission from the moment it happens, without
integrating anything away. `bw_timex` maps the IPCC AR6 functions to the biosphere flows of
`METHOD` by itself, so there is no `characterization_functions` dict to pass here - we are on
ecoinvent flows.
"""),
    code('''# instantaneous, one series per emitting activity
tlca.dynamic_lcia(metric="radiative_forcing", time_horizon=100)
tlca.plot_dynamic_characterized_inventory(sum_emissions_within_activity=True)
'''),
    md("""The same characterization, now summed over all activities and **accumulated** - the
warming the house has caused up to each point in time, rather than in each single year:
"""),
    code('''tlca.plot_dynamic_characterized_inventory(sum_activities=True, cumsum=True)
'''),
    md("""The house life cycle spends its first decades **cooling**: the tree's uptake is characterized
before anything is emitted. The curve crosses zero only years after the house's construction.
"""),
    # ------------------------------------------------------------- exercise 1: horizons
    md("""## 3 | 🛠️ Your turn: fixed or flexible time horizon?

Both options say "100 years", and they mean different things:

| | window for one emission |
|---|---|
| `fixed_time_horizon=False` (default) | 100 years starting **at that emission** |
| `fixed_time_horizon=True` (Levasseur) | up to the **functional unit's date + 100 years**, whoever emits |

This system is the interesting case, because its flows are spread over more than a century:
the tree takes up CO2 up to 40 years *before* the functional unit, the incineration happens
50 years *after* it.

**Predict first, then run:** does `fixed_time_horizon=True` give a higher or a lower GWP100
than the default - and why?
"""),
    code('''for fixed in (False, True):
    tlca.dynamic_lcia(metric="GWP", time_horizon=100, fixed_time_horizon=fixed)
    print(f"fixed_time_horizon={fixed!s:<5}  GWP100: {tlca.dynamic_score:,.0f} kg CO2-eq")
''', section="student_fixed_horizon", file="1_fixed_time_horizon.py", role="solution", todo='''# TODO: compute the GWP100 of this system both ways and print the two scores.
#       One call each: tlca.dynamic_lcia(metric=..., time_horizon=..., fixed_time_horizon=...),
#       and read the result off tlca.dynamic_score.
'''),
    md("""**Lower**, and by a lot: about 13,700 instead of 24,700 kg CO2-eq.

The uptake is what moves. With the fixed horizon, the CO2 the tree took up 40 years before
move-in is counted towards a window that ends in 2125, so it is credited for ~140 years
instead of 100 - the cooling contribution grows. The incineration in 2075, on the other hand,
gets only its remaining ~50 years instead of a full century, so its warming shrinks. Both
effects push the score down.

Neither number is "the right one". `False` is what conventional LCIA does and what published
GWP factors mean; `True` is the consistent choice when you want one common cut-off date for
the whole study - and the one to use when you compare systems whose emissions sit at
different points in time.
""", role="answer"),
    md("""The same two variants as **radiative forcing over time**, in two panels because the
two quantities differ by a factor of ~70 and would hide each other on one axis:

- **top**: the radiative forcing *in* each year - the instantaneous warming effect of
  everything emitted so far, as it decays.
- **bottom**: the running sum of the top panel. This is the area a GWP integrates into its
  single number, which is why the two curves end where the two GWP100 scores were.

The dotted lines are move-in (2025) and the common cut-off the fixed horizon uses
(2125 = functional unit + 100 years):
"""),
    code('''import pandas as pd

series = {}
for fixed in (False, True):
    tlca.dynamic_lcia(metric="radiative_forcing", time_horizon=100, fixed_time_horizon=fixed)
    rf = tlca.characterized_inventory.groupby("date")["amount"].sum().sort_index()
    series[fixed] = rf.resample("YS").sum()  # monthly resolution is noise at this scale

# flexible drawn solid and underneath, fixed dashed on top: wherever the two agree, the
# dashes sit straight on the blue line
STYLES = {
    False: dict(color="tab:blue", linewidth=2.2, linestyle="-",
                label="flexible: 100 years from each emission"),
    True: dict(color="tab:orange", linewidth=1.6, linestyle="--",
               label="fixed: everything counted until 2125"),
}

fig, (ax_year, ax_cum) = plt.subplots(2, 1, figsize=(13, 8), sharex=True)

for fixed, style in STYLES.items():
    rf = series[fixed]
    ax_year.plot(rf.index, rf.values, **style)
    ax_cum.plot(rf.index, rf.cumsum().values, **style)

ax_year.set_title("instantaneous - radiative forcing in each year")
ax_cum.set_title("cumulative - the running sum, i.e. what a GWP integrates")

for ax in (ax_year, ax_cum):
    ax.axhline(0, color="black", linewidth=0.8)
    bottom = ax.get_ylim()[0]
    for year, label in [(2025, "move-in"), (2125, "FU + 100 a")]:
        date = pd.Timestamp(f"{year}-01-01")
        ax.axvline(date, color="grey", linestyle=":", linewidth=1)
        ax.text(date, bottom, f" {label}", color="grey", fontsize=9, va="bottom")
    ax.set_ylabel("W/m2")
    ax.legend(loc="upper left", framealpha=0.9)

plt.tight_layout()
plt.show()
'''),
    md("""For most of the century the dashes sit straight on the solid line: every flow is
still inside both windows, so both runs characterize it identically. They come apart around
2100 in two steps.

First the dashed line drops **below** the solid one. That is the tree: its uptake is negative
forcing, the flexible run closes the 100-year window on it around 2085, and the fixed run
keeps counting it to 2125 - about 140 years of credit instead of 100. Then, at 2125, the
fixed run stops altogether, while the flexible one carries the 2075 incineration on to 2174.

Cooling counted longer, warming counted shorter: that is the whole of the 24,711 vs 13,704
gap. This value corresponds to the integral of the curve in the bottom panel.

"""),
    md("""### 🛠️ Your turn: how much does the horizon length itself matter?

Use [`TimexLCA.compare()`](https://docs.brightway.dev/projects/bw-timex/en/latest/content/api/bw_timex/timex_lca/index.html)
to characterize the sommerhus inventory with GWP over **20, 50, 100 and 500 years, each with `fixed_time_horizon` False and True**.

**Predict first, then run:** which of the eight numbers comes out **negative**, and what
happens to the gap between the two columns as the horizon grows?
"""),
    code('''from dataclasses import replace

from bw_timex import TimexLCASettings

base = TimexLCASettings(
    demand={living: 1},
    method=METHOD,
    timeline={"starting_datetime": "2025-01-01", "temporal_grouping": "month"},
    # the static score does not depend on the horizon, so don't pay for it eight times
    lcia={"metric": "GWP", "static_lcia_enabled": False},
)

comparison = TimexLCA.compare(
    [
        replace(
            base,
            time_horizon=horizon,
            fixed_time_horizon=fixed,
            label=f"GWP{horizon}, {'fixed' if fixed else 'flexible'}",
        )
        for horizon in (20, 50, 100, 500)
        for fixed in (False, True)
    ]
)

comparison.summary.pivot(
    index="time_horizon", columns="fixed_time_horizon", values="dynamic_score"
)
''', section="student_horizon_sweep", file="2_time_horizon_sweep.py", role="solution", todo='''# TODO: run TimexLCA.compare() with different TimexLCASettings:
#       time_horizon 20 / 50 / 100 / 500, each with fixed_time_horizon False and True.
#       Start from one base TimexLCASettings (demand={living: 1}, method=METHOD,
#       starting_datetime="2025-01-01", temporal_grouping="month", metric="GWP") and
#       dataclasses.replace() it per run. See also the last part of the 2_sommerhus.ipynb notebook.
'''),
    md("""Read the `fixed_time_horizon=True` column downwards and watch the warning `bw_timex`
printed: with a fixed horizon of 20 years, everything after 2045 lies **outside** the window
and is dropped entirely - the grid draw of the 2050s, the incineration, all of it. What is
left is mostly the tree, so the score turns negative. It is not a claim that the house is
climate positive; it is the honest answer to the question "what happens between 2025 and
2045", and a good reason to state your horizon and its start whenever you report a dynamic
score.

The two columns converge towards long horizons: a 500-year window makes a 40-year offset in
the timing almost irrelevant.
""", role="answer"),
    # ----------------------------------------------- exercise 2: your own char. function
    md("""## 4 | 🛠️ Your turn: a characterization function of your own

Nothing in `characterize()` is climate-specific - it applies whatever function you map onto a
flow. So let us give the *sommerhus* something that climate metrics cannot see.

A Danish summer house draws its water from **its own well**, and it is lived in during the
**summer** - exactly when the groundwater is under most pressure. Static LCIA has one factor per flow and cannot express that, but a dynamic characterization
function can.

**(a) Add a water flow to the model.** 60 m3 of `"Water, well, in ground"` per year of
habitation, drawn **April to September** - the house fills up and the garden needs watering -
with the peak in **July and August**. Say:

| Apr | May | Jun | Jul | Aug | Sep |
|---|---|---|---|---|---|
| 7% | 12% | 20% | 27% | 24% | 10% |

Then rebuild the `TimexLCA` so the inventory contains it.

> The flow lives in `bd.config.biosphere`, categories `("natural resource", "in water")`.
> A biosphere edge is `living.new_edge(input=..., amount=..., type="biosphere")`, and its
> `temporal_distribution` works exactly like the ones on technosphere edges: months relative
> to the consumer, shares that sum to 1 **over the whole exchange**. 
"""),
    code('''import numpy as np
from bw_timex import TemporalDistribution

WATER_PER_YEAR = 60  # m3/a, drawn from the house's own well

# looked up again, so this cell also works if `foreground` was rebuilt in between
living = bd.get_node(database="foreground", name="living in the sommerhus")
water_flow = bd.get_node(
    database=bd.config.biosphere,
    name="Water, well, in ground",
    categories=("natural resource", "in water"),
)

# drop a previous attempt, so running this cell twice does not draw the water twice
for edge in list(living.biosphere()):
    if edge.input.id == water_flow.id:
        edge.delete()

# the season, as months after a January move-in: April ... September
SEASON_MONTHS = np.array([3, 4, 5, 6, 7, 8])
SEASON_SHARES = np.array([0.07, 0.12, 0.20, 0.27, 0.24, 0.10])  # peak in July/August

# ... repeated for every year of habitation, each year taking 1/50 of the total
year_offsets = np.repeat(np.arange(LIFETIME) * 12, len(SEASON_MONTHS))
td_water = TemporalDistribution(
    date=(np.tile(SEASON_MONTHS, LIFETIME) + year_offsets).astype("timedelta64[M]"),
    amount=np.tile(SEASON_SHARES, LIFETIME) / LIFETIME,
)

water_edge = living.new_edge(
    input=water_flow, amount=WATER_PER_YEAR * LIFETIME, type="biosphere"
)
water_edge["temporal_distribution"] = td_water
water_edge.save()
bd.Database("foreground").process()

tlca = TimexLCA({living: 1}, METHOD)
tlca.build_timeline(starting_datetime="2025-01-01", temporal_grouping="month")
tlca.lci()
''', section="student_water_flow", file="3_water_flow.py", role="solution", todo='''# TODO: add the water flow to `living` (see the hints above), give it a temporal
#       distribution that spreads each year's withdrawal over the season, and rebuild
#       the TimexLCA:
#       TimexLCA(...) -> build_timeline(starting_datetime="2025-01-01",
#       temporal_grouping="month") -> lci()
'''),
    md("""**(b) Characterize it.** You already wrote this function: `characterize_water_scarcity`
from [`3_dynamic_characterization.ipynb`](3_dynamic_characterization.ipynb), with
`water_stress_index_by_month`. Copy both across - nothing about them changes here. The only new part is what you point it at.

> Call `characterize()` on `tlca.dynamic_inventory_df` directly, with
> `characterization_functions={water_flow.id: characterize_water_scarcity}`.
"""),
    code('''from dynamic_characterization import characterize
from dynamic_characterization.classes import CharacterizedRow

# straight from the dynamic-characterization notebook, unchanged
water_stress_index_by_month = [0.2, 0.3, 0.4, 0.5, 0.7, 0.9, 1.0, 1.0, 0.8, 0.6, 0.4, 0.3]


def characterize_water_scarcity(series, period: int = 1) -> CharacterizedRow:
    """A toy seasonal water scarcity characterization function"""
    month = series.date.month
    weight = water_stress_index_by_month[month - 1]
    impact = series.amount * weight

    return CharacterizedRow(
        date=np.array([series.date.to_datetime64()], dtype="datetime64[s]"),
        amount=np.array([impact], dtype="float64"),
        flow=series.flow,
        activity=series.activity,
    )


# ... and now pointed at a real supply chain instead of three dummy rows
water_rows = tlca.dynamic_inventory_df.query("flow == @water_flow.id")
water_scarcity = characterize(
    tlca.dynamic_inventory_df,
    characterization_functions={water_flow.id: characterize_water_scarcity},
)

print(f"withdrawn:  {water_rows['amount'].sum():,.0f} m3 over {len(water_rows)} withdrawals")
print(f"weighted:   {water_scarcity['amount'].sum():,.0f} stress-m3")
''', section="student_water_cf", file="4_water_characterization.py", role="solution", todo='''# TODO: bring `characterize_water_scarcity` and `water_stress_index_by_month` over from the
#       3_dynamic_characterization.ipynb - they work here unchanged - and apply them to
#       tlca.dynamic_inventory_df.
'''),
    md("""The season sits on the high half of the index: weighted by the withdrawal curve it
averages 0.89, against an annual mean of 0.61. So the seasonal indicator comes out about
**1.5x** the season-blind one (2,679 against 1,786 stress-m3) - a factor built on the annual
average would report this house a third lower. Nothing about the inventory changed, only the
question the characterization function asks of it.

Two details worth noticing:

- the water is slightly *more* than your 3,000 m3. The same flow occurs in the **background**
  too: glass wool, heat pumps and electricity all draw well water, and those withdrawals sit
  in the inventory with their own dates. Your own edge is the dominant part, not all of it.
- the month only survives because the characterization ran on `dynamic_inventory_df`.
  Through `dynamic_lcia()` every withdrawal would have landed on 1 January and the index
  would always have read 0.2.
""", role="answer"),
    # ------------------------------------------------ outlook: prospective water scarcity
    md("""## 5 | 🚀 Outlook, for the ambitious: make it prospective

The index you just used is a snapshot of *today's* summer. It will not hold for 2075: drier
summers, a lower water table, more neighbours on the same aquifer. The climate functions have
the same problem, and the Watanabe pCFs from the previous notebook solve it by letting the
characterization factor depend on the **year** of the emission as well as the substance.

Do the same for the water. Write `characterize_water_scarcity_prospective(series, period=1)`
that keeps the month lookup and multiplies it by a trend read off the year - say stress rises
by 60% between 2025 and 2075 and is held flat outside that range - then characterize the same
inventory with it and compare.

> `np.interp(year, [2025, 2075], [1.0, 1.6])` gives you the trend and clamps outside the
> range, exactly like the temporal evolution factors in notebook 2. The month must survive:
> `series.date` still carries it, so keep reading `series.date.month` and do **not** route
> this through `dynamic_lcia()`.
>
> Worth asking yourself afterwards: this house draws the same 60 m3 every summer for 50 years.
> Under a rising index, is its *late* water worth more than its early water - and what would
> that mean for a house built in 2045 instead?
"""),
    code('''def characterize_water_scarcity_prospective(series, period: int = 1) -> CharacterizedRow:
    """Seasonal weight, times a scarcity trend read off the year of the withdrawal."""
    month = series.date.month
    weight = water_stress_index_by_month[month - 1]
    trend = np.interp(series.date.year, [2025, 2075], [1.0, 1.6])  # flat outside the range

    return CharacterizedRow(
        date=np.array([series.date.to_datetime64()], dtype="datetime64[s]"),
        amount=np.array([series.amount * weight * trend], dtype="float64"),
        flow=series.flow,
        activity=series.activity,
    )


water_scarcity_prospective = characterize(
    tlca.dynamic_inventory_df,
    characterization_functions={water_flow.id: characterize_water_scarcity_prospective},
)

print(f"today's index:     {water_scarcity['amount'].sum():,.0f} stress-m3")
print(f"rising index:      {water_scarcity_prospective['amount'].sum():,.0f} stress-m3")
''', section="student_water_prospective", file="5_water_prospective.py", role="solution", todo='''# TODO: write characterize_water_scarcity_prospective(series, period=1) - the same month
#       lookup, times np.interp(series.date.year, [2025, 2075], [1.0, 1.6]) - and
#       characterize tlca.dynamic_inventory_df with it.
'''),
    code('''if "water_scarcity_prospective" in globals():
    per_year = {
        "today's index": water_scarcity.assign(year=water_scarcity["date"].dt.year)
        .groupby("year")["amount"].sum(),
        "rising index": water_scarcity_prospective.assign(
            year=water_scarcity_prospective["date"].dt.year
        ).groupby("year")["amount"].sum(),
    }

    fig, ax = plt.subplots(figsize=(11, 3.5))
    for label, series_ in per_year.items():
        ax.plot(series_.index, series_.values, marker="o", markersize=3, label=label)
    ax.set_xlabel("year of withdrawal")
    ax.set_ylabel("stress-weighted m3 per year")
    ax.legend()
    plt.tight_layout()
    plt.show()
else:
    print("nothing to compare yet - section 5 is still open")
'''),
    md("""Same water, same months, same inventory: only the year the withdrawal happens in now
matters. The early summers are unchanged and the later ones weigh up to 60% more, which adds
up to **2,679 -> 3,465 stress-m3**, +29% over the lifetime. The house's water burden is
**back-loaded** - the water version of exactly the point the dynamic climate metrics make, and
a house built in 2045 would draw all of its water on the expensive part of that curve.
""", role="answer"),
    md("""## 6 | Where to go from here

- **Prospective characterization factors** (Watanabe et al. 2026): same call, `metric="pGWP"`
  or `"prospective_radiative_forcing"` after `prospective.set_scenario(...)`. On a system whose
  emissions run to 2125, the scenario-dependent radiative efficiencies are not a detail.
- **`fixed_time_horizon` in a comparison**: two houses built decades apart are exactly the case
  where the choice changes the ranking, not just the number.
- **Your own metric**: the water function above is 8 lines. Anything that depends on *when* -
  seasonal water, noise at night, harvest timing - fits the same shape.
"""),
]

students3 = student_version(part3, NB3)
save(notebook(students3), HERE / "4_sommerhus_dynamic.ipynb")
print(f"wrote 4_sommerhus_dynamic.ipynb with {len(students3)} cells (student version)")

save(notebook(for_solutions_dir(part3)), NB3 / "4_sommerhus_dynamic_SOLVED.ipynb")
print(f"wrote solutions/4_sommerhus_dynamic/4_sommerhus_dynamic_SOLVED.ipynb with {len(part3)} cells")
copy_modules(["sommerhus_system.py", "sommerhus_temporal.py"], NB3)
