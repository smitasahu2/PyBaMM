import pybamm
from models import MSPM
from parameters import get_parameter_values

models = [
    pybamm.lithium_ion.SPM(
        options={"particle": "uniform profile", "intercalation kinetics": "linear"}
    ),
    MSPM(options={"particle": "uniform profile"}),
]

parameter_values = pybamm.ParameterValues(get_parameter_values())

sols = []
for model in models:
    sim = pybamm.Simulation(model, parameter_values=parameter_values)
    sol = sim.solve([0, 3600])
    sols.append(sol)

pybamm.dynamic_plot(sols)
