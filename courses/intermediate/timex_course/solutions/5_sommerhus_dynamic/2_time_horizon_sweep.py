from dataclasses import replace

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
