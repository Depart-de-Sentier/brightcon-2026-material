# heat pumps: at move-in, and two replacements
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
