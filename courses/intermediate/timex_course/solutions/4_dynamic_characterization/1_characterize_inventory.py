characterized_dynamic_inventory = characterize(
        simple_dynamic_inventory,
        metric="radiative_forcing",  #also available: GWP, and some prospective variants (more later)
        characterization_functions={
            1: ar6.characterize_co2, #flow_id : characterization function
            3: ar6.characterize_ch4,
        },
        time_horizon=4, #years (exclusive last year)
    )
