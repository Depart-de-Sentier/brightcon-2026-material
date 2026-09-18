characterization_functions = {
    bd.get_node(code="CH4").id: ar6.characterize_ch4,
    bd.get_node(code="CO2").id: ar6.characterize_co2,
    bd.get_node(code="N2O").id: ar6.characterize_n2o,
} 

characterized_df = characterize(
    tlca.dynamic_inventory_df,
    metric="radiative_forcing",
    characterization_functions=characterization_functions,
    time_horizon=100,  # years (exclusive last year)
)
