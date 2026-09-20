"""The *sommerhus* product system - ordinary Brightway, no temporal information.

A Danish summer house: built of wood, insulated with glass wool, heated with a heat pump,
lived in for 50 years, then demolished and the wood incinerated.

    from sommerhus_system import build_system
    build_system(lifetime=50, electricity_per_year=1400, ...)

Writes the `foreground` database and nothing else: no functional unit, no method, no
calculation - those are the notebook's job. Nor does it process the database: `TimexLCA`
(like `bw2calc`) reprocesses anything that was modified before it calculates. Temporal distributions and temporal evolution
live in `sommerhus_temporal.py`.
"""

import bw2calc as bc
import bw2data as bd
import numpy as np

FOREGROUND = "foreground"

# node names, so the notebooks can look their exchanges up by name
TIMBER_TREE = "timber tree"
STRUCTURAL_TIMBER = "structural timber production, carbon split"
CONSTRUCTION = "sommerhus construction, wood"
LIVING = "living in the sommerhus"
WOOD_INCINERATION = "incineration of waste wood"


def build_system(
    lifetime,
    timber_volume,
    insulation_mass,
    heat_pumps,
    electricity_per_year,
    background_database,
    method,
):
    """(Re)build the `foreground` database from the given assumptions.

    `method` is only used to size the biogenic carbon split below - the study's own
    calculations happen in the notebook.
    """
    bd.projects.set_current("timex_brightcon")

    if FOREGROUND in bd.databases:
        del bd.databases[FOREGROUND]
    foreground = bd.Database(FOREGROUND)
    foreground.register()

    bg = bd.Database(background_database)
    glass_wool = bg.get(name="market for glass wool mat", location="GLO")
    heat_pump = bg.get(name="heat pump production, brine-water, 10kW", location="RoW")
    grid = bg.get(name="market group for electricity, low voltage", location="GLO")
    timber_bg = bg.get(name="structural timber production", location="RER", unit="cubic meter")

    # ---------------------------------------------------------------- biogenic carbon
    # A tree takes up its CO2 over decades of growth, long before the timber is delivered.
    # To be able to time that uptake separately, ecoinvent's timber is split into an uptake
    # node and a processing node that together reproduce its original score.
    timber_lca = bc.LCA({timber_bg: 1}, method)
    timber_lca.lci()
    timber_lca.lcia()

    biosphere = bd.Database(bd.config.biosphere)
    co2_uptake_flow = biosphere.get(
        name="Carbon dioxide, in air", categories=("natural resource", "in air")
    )
    # CF = -1, so this amount doubles as its score, with the opposite sign
    uptake_amount = np.asarray(timber_lca.inventory.sum(axis=1)).flatten()[
        timber_lca.dicts.biosphere[co2_uptake_flow.id]
    ]
    co2_air_flow = next(  # CF = +1
        exc.input
        for exc in timber_bg.biosphere()
        if exc.input["name"] == "Carbon dioxide, non-fossil"
        and exc.input.get("categories") == ("air",)
    )

    timber_tree = foreground.new_node(name=TIMBER_TREE, unit="cubic meter")
    timber_tree["reference product"] = "standing timber, biogenic carbon uptake"
    timber_tree.save()
    timber_tree.new_edge(input=timber_tree, amount=1, type="production").save()
    timber_tree.new_edge(
        input=co2_uptake_flow, amount=uptake_amount, type="biosphere"
    ).save()

    structural_timber = foreground.new_node(name=STRUCTURAL_TIMBER, unit="cubic meter")
    structural_timber["reference product"] = "structural timber"
    structural_timber.save()
    structural_timber.new_edge(input=structural_timber, amount=1, type="production").save()
    structural_timber.new_edge(
        input=co2_air_flow,
        amount=timber_lca.score + uptake_amount,  # everything but the tree's credit
        type="biosphere",
    ).save()
    structural_timber.new_edge(input=timber_tree, amount=1, type="technosphere").save()

    wood_incineration = foreground.new_node(name=WOOD_INCINERATION, unit="cubic meter")
    wood_incineration["reference product"] = "waste wood incineration"
    wood_incineration.save()
    wood_incineration.new_edge(input=wood_incineration, amount=1, type="production").save()
    wood_incineration.new_edge(
        input=co2_air_flow, amount=uptake_amount, type="biosphere"
    ).save()  # what the tree took up comes back out

    # --------------------------------------------------------------------- the house
    construction = foreground.new_node(name=CONSTRUCTION, unit="unit")
    construction["reference product"] = "sommerhus shell"
    construction.save()
    construction.new_edge(input=construction, amount=1, type="production").save()
    construction.new_edge(
        input=structural_timber, amount=timber_volume, type="technosphere"
    ).save()
    construction.new_edge(
        input=glass_wool, amount=insulation_mass, type="technosphere"
    ).save()

    living = foreground.new_node(name=LIVING, unit=f"{lifetime} years of habitation")
    living["reference product"] = "sommerhus use"
    living.save()
    living.new_edge(input=living, amount=1, type="production").save()
    living.new_edge(input=construction, amount=1, type="technosphere").save()
    living.new_edge(input=heat_pump, amount=heat_pumps, type="technosphere").save()
    living.new_edge(
        input=grid, amount=electricity_per_year * lifetime, type="technosphere"
    ).save()
    living.new_edge(
        input=wood_incineration, amount=timber_volume, type="technosphere"
    ).save()

    return foreground
