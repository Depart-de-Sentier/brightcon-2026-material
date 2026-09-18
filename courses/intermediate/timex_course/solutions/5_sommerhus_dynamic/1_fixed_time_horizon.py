for fixed in (False, True):
    tlca.dynamic_lcia(metric="GWP", time_horizon=100, fixed_time_horizon=fixed)
    print(f"fixed_time_horizon={fixed!s:<5}  GWP100: {tlca.dynamic_score:,.0f} kg CO2-eq")
