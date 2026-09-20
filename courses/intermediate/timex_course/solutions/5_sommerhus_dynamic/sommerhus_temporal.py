# Generated copy of ../../sommerhus_temporal.py - edit that one and re-run the build.
"""Temporal information for the *sommerhus* system.

Everything `bw_timex` needs on top of the plain Brightway model in `sommerhus_system.py`:
temporal distributions (*when* does an exchange happen) and temporal evolution (*how much*,
as a function of calendar time).

    from sommerhus_system import build_system
    from sommerhus_temporal import add_temporal_information

    build_system(...)
    add_temporal_information(lifetime=50, background_database=...)

Notebook 3 writes this out by hand; the later notebooks import it.
"""

from datetime import datetime

import numpy as np
from bw_timex import TemporalDistribution, easy_timedelta_distribution
from bw_timex.utils import (
    add_temporal_distribution_to_exchange,
    add_temporal_evolution_to_exchange,
)

from sommerhus_system import (
    CONSTRUCTION,
    LIVING,
    STRUCTURAL_TIMBER,
    TIMBER_TREE,
    WOOD_INCINERATION,
)

#: The habitants reduce their electricity demand by 1% of the original demand per year.
#: Absolute dates: this follows calendar time, not the building's age.
ELECTRICITY_EVOLUTION = {
    datetime(2025, 1, 1): 1.0,
    datetime(2075, 1, 1): 0.5,
}


def temporal_distributions(lifetime):
    """The five TDs of the sommerhus model, by name."""
    return {
        # materials arrive over the last nine months before move-in
        "construction": TemporalDistribution(
            date=np.array([-9, -6, -2, -1], dtype="timedelta64[M]"),
            amount=np.array([0.2, 0.3, 0.3, 0.2]),
        ),
        # the tree grows for 40 years: bell-shaped uptake rate, i.e. an S-shaped carbon stock
        "biogenic_uptake": easy_timedelta_distribution(
            start=-40, end=0, resolution="Y", steps=41, kind="normal", param=0.2
        ),
        # electricity, evenly over the lifetime
        "electricity": easy_timedelta_distribution(
            start=0, end=lifetime, resolution="Y", steps=lifetime + 1, kind="uniform"
        ),
        # heat pumps: at move-in, and two replacements
        "heat_pumps": TemporalDistribution(
            date=np.array([0, 17, 34], dtype="timedelta64[Y]"),
            amount=np.array([1 / 3, 1 / 3, 1 / 3]),
        ),
        # demolition, three months after the lifetime is up
        "eol": TemporalDistribution(
            date=np.array([lifetime * 12 + 3], dtype="timedelta64[M]"),
            amount=np.array([1]),
        ),
    }


def add_temporal_information(
    lifetime, background_database, electricity_evolution=ELECTRICITY_EVOLUTION
):
    """Attach TDs and temporal evolution to the system from `build_system()`."""
    tds = temporal_distributions(lifetime)

    add_temporal_distribution_to_exchange(
        tds["construction"], input_name=STRUCTURAL_TIMBER, output_name=CONSTRUCTION
    )
    add_temporal_distribution_to_exchange(
        tds["construction"],
        input_name="market for glass wool mat",
        input_location="GLO",
        input_database=background_database,
        output_name=CONSTRUCTION,
    )
    add_temporal_distribution_to_exchange(
        tds["biogenic_uptake"],
        input_name="Carbon dioxide, in air",
        output_name=TIMBER_TREE,
    )
    add_temporal_distribution_to_exchange(
        tds["electricity"],
        input_name="market group for electricity, low voltage",
        input_location="GLO",
        input_database=background_database,
        output_name=LIVING,
    )
    add_temporal_distribution_to_exchange(
        tds["heat_pumps"],
        input_name="heat pump production, brine-water, 10kW",
        input_location="RoW",
        input_database=background_database,
        output_name=LIVING,
    )
    add_temporal_distribution_to_exchange(
        tds["eol"], input_name=WOOD_INCINERATION, output_name=LIVING
    )

    # the same exchange that carries the electricity TD: *when* it happens and *how much*
    # of it happens are two separate pieces of information on one edge
    add_temporal_evolution_to_exchange(
        temporal_evolution_factors=electricity_evolution,
        input_name="market group for electricity, low voltage",
        input_location="GLO",
        input_database=background_database,
        output_name=LIVING,
    )

    return tds
