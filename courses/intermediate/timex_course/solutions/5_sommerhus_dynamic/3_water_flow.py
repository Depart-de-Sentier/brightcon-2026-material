import numpy as np
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
