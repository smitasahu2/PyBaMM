import pybamm
import os
import numpy as np
import matplotlib.pyplot as plt

# Lets import the parameters we are going to use in Li plating model
tend = 3600
t_eval = np.arange(0,tend,1)
parameter_values = pybamm.ParameterValues("OKane2022")


# Lets choose a lithium plating models from pybamm
# opt = {"lithium plating": ["reversible"]}
# model_2022 = pybamm.lithium_ion.DFN(options = opt)
# sim_model2022 = pybamm.Simulation(model_2022, parameter_values = parameter_values)
# sol_model2022 = sim_model2022.solve(t_eval = t_eval)
# pybamm.dynamic_plot(sol_model2022)

# choose models
plating_options = ["reversible"]#, "irreversible", "partially reversible"]
models = {option: pybamm.lithium_ion.DFN(options={"lithium plating": option}, name=option) 
          for option in plating_options}
tend = 3600
t_eval = np.arange(0,tend,1)
sol_all = []
# pick parameters
parameter_values = pybamm.ParameterValues("OKane2022")
sim_simon = []
#A = np.array([ 5, 2.5]);
A = np.array([ 268.15, 278.15,288.15, 298.15,300.15])
for i in A:
  parameter_values["Ambient temperature [K]"] =i    

  for model in models.values():
    #parameter_values["Current function [A]"] = i
    sim_simon = pybamm.Simulation(model, parameter_values=parameter_values)
    sol_simon = sim_simon.solve(t_eval=t_eval)
    model.set_initial_conditions_from(sol_simon)
    sol_all.append(sol_simon)
pybamm.dynamic_plot(sol_all)

Smita = 5/(0.1027 * 8.52e-5)
print(Smita)

C_rates = ["2C", "1C", "C/2", "C/4", "C/8"]
experiments = {}
for C_rate in C_rates:
    experiments[C_rate] = pybamm.Experiment(
    [
        (f"Charge at {C_rate} until 4.2 V",
        "Hold at 4.2 V until C/20",
        "Rest for 1 hour")
    ]
)


def define_and_solve_sims(model, experiments, parameter_values):
    sims = {}
    for C_rate, experiment in experiments.items():
        sim = pybamm.Simulation(model, experiment=experiment, parameter_values=parameter_values)
        sim.solve(calc_esoh=False)
        sims[C_rate] = sim
    return sims

