import pybamm

model = pybamm.lithium_ion.DFN(
    options = {
        "particle mechanics": "swelling only",
        "thermal":"lumped",
    }
)

param_Ai2020 = pybamm.ParameterValues("Ai2020")

exp_Ai2020 = pybamm.Experiment(
    [
        (
            "Discharge at 0.5C until  3.7V",
            "Charge at 0.2C for 7200 seconds (3 minute period)"
        )*5
    ]
)

sim_Ai2020 = pybamm.Simulation(
    model, 
    experiment = exp_Ai2020, 
    parameter_values = param_Ai2020
)

sol_Ai2020 = sim_Ai2020.solve(calc_esoh=False)
sim_Ai2020.plot(["Terminal voltage [V]",
                 "Volume-averaged cell temperature [K]",
                 "Cell thickness change [m]"])