import pybamm
from models import MSPM
from pouch_parameters import get_parameter_values

models = [
    pybamm.lithium_ion.SPM(
        options={
            "particle": "uniform profile",
            "intercalation kinetics": "linear",
            "current collector": "potential pair",
            "dimensionality": 1,
        }
    ),
    MSPM(
        options={
            "particle": "uniform profile",
            "current collector": "potential pair",
            "dimensionality": 1,
        }
    ),
]

parameter_values = pybamm.ParameterValues(get_parameter_values())

sols = []
for model in models:
    sim = pybamm.Simulation(model, parameter_values=parameter_values)
    sol = sim.solve([0, 3600])
    sols.append(sol)

output_variables = [
    "Current [A]",
    "Terminal voltage [V]",
    "Negative current collector potential [V]",
    "Positive current collector potential [V]",
]
pybamm.dynamic_plot(sols, output_variables)
