#
# Example showing how to load and solve the DFN
#

import pybamm
import numpy as np

pybamm.set_logging_level("INFO")

# load model
model_DFN = pybamm.lithium_ion.DFN()
# create geometry
# geometry = model.default_geometry

# load parameter values and process model and geometry
parameter_values = pybamm.ParameterValues("OKane2022")
parameter_values["Current function [A]"] = 20
var_pts = {
    "x_n": 30,  # negative electrode
    "x_s": 15,  # separator 
    "x_p": 30,  # positive electrode
    "r_n": 30,  # negative particle
    "r_p": 30,  # positive particle
 }
# solve model
t_eval = np.linspace(0, 3600, 10000)
# solver = pybamm.CasadiSolver(mode="safe", atol=1e-6, rtol=1e-3)
# solution = solver.solve(model, t_eval)

sim_DFN = pybamm.Simulation(model_DFN, parameter_values=parameter_values, var_pts=var_pts)
sol_DFN = sim_DFN.solve(t_eval)


# plot
plot = pybamm.QuickPlot(
    sol_DFN,
    [
        "Negative particle concentration [mol.m-3]",
        "Electrolyte concentration [mol.m-3]",
        "Positive particle concentration [mol.m-3]",
        "Current [A]",
        "Negative electrode potential [V]",
        "Electrolyte potential [V]",
        "Positive electrode potential [V]",
        "Voltage [V]",
    ],
    time_unit="seconds",
    spatial_unit="um",
)
plot.dynamic_plot()

sol_DFN.save_data("DFN.csv",[
                        "Time [s]", 
        "Current [A]",
         "Voltage [V]",
  ]                      
  , to_format="csv")
