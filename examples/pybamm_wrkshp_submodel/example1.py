import pybamm
model = pybamm.lithium_ion.DFN(
    options = {
        "particle mechanics": "swelling only"
    }
)
model.submodels
param = pybamm.ParameterValues("Ai2020")
experiment = pybamm.Experiment(
    [
        (
            "Discharge at 1C until 3.7V",
            "Charge at 0.3C for 3600 seconds (3 minute period)"
        )
    ]
    * 1,
)

sim = pybamm.Simulation(
    model,
    experiment=experiment,
    parameter_values=param,
)
solution = sim.solve(calc_esoh=False)
sim.plot(["Terminal voltage [V]", "Volume-averaged cell temperature [K]", "Cell thickness change [m]"])
