import pybamm
import numpy as np
import matplotlib.pyplot as plt

# pybamm.set_logging_level("INFO")
model_DFN = pybamm.lithium_ion.DFN()

param = pybamm.ParameterValues("OKane2022")
var_pts = {
    "x_n": 30,  # negative electrode
    "x_s": 15,  # separator 
    "x_p": 30,  # positive electrode
    "r_n": 30,  # negative particle
    "r_p": 30,  # positive particle
    # "x_n": 5,  # negative electrode
    # "x_s": 5,  # separator 
    # "x_p": 5,  # positive electrode
    # "r_n": 30,  # negative particle
    # "r_p": 30,  # positive particle
}

N_cycles = 4

standard_protocol = pybamm.Experiment(
    ["Hold at 4.2 V until C/100 (5 minute period)",
    "Rest for 4 hours (5 minute period)",
    "Discharge at 0.1C until 2.5 V (5 minute period)",  # initial capacity check
    "Charge at 0.3C until 4.2 V (5 minute period)",
    "Hold at 4.2 V until C/100 (5 minute period)",]
    + [("Discharge at 1C until 2.5 V",  # ageing cycles
    "Charge at 0.3C until 4.2 V (5 minute period)",
    "Hold at 4.2 V until C/100 (5 minute period)",)] * N_cycles
    + ["Discharge at 0.1C until 2.5 V (5 minute period)"]  # final capacity check
)
sims_standard = []
# model_DFN.variables.search("current")
# exp = pybamm.Experiment(["Hold at 4.2 V until C/100", "Rest for 1 hour", "Discharge at 1C until 2.5 V"])
# t_eval = np.linspace(0, 2e5, 100)
# param["Current function [A]"] = 10

sim = pybamm.Simulation(model_DFN, parameter_values= param, experiment=standard_protocol, var_pts=var_pts)
# sim = pybamm.Simulation(model_DFN, parameter_values= param, var_pts=var_pts)
sol = sim.solve([0, 3600])
sim.plot()
sol.save_data("DFN.csv",
                            [
                        "Time [min]", 
                        "Current [A]", 
                        "Terminal voltage [V]", 
                       ]
                      , to_format="csv")







# exp = pybamm.Experiment(["Charge at 1C until 4.2 V"])#["Hold at 4.2 V until C/20", "Rest for 1 hour"])
# sim_DFN = pybamm.Simulation(model_DFN, parameter_values=param,t_eval, var_pts=var_pts)
# sol_DFN = sim_DFN.solve(calc_esoh=False)
# pybamm.dynamic_plot(sol)

# sim_SEI = pybamm.Simulation(model_SEI, parameter_values=param, experiment=exp, var_pts=var_pts)
# sol_SEI = sim_SEI.solve(calc_esoh=False)
# model_DFN.variables.search("Voltage")
# pybamm.dynamic_plot(sol_SEI)


# t_DFN = sol_DFN["Time [s]"].entries
# V_DFN = sol_DFN["Terminal voltage [V]"].entries
# No_SEI = sol_DFN["Loss of lithium to SEI [mol]"].entries
# lithium_neg_DFN = sol_DFN["Total lithium in negative electrode [mol]"].entries
# lithium_pos_DFN = sol_DFN["Total lithium in positive electrode [mol]"].entries
# t_SEI = sol_SEI["Time [s]"].entries
# V_SEI = sol_SEI["Terminal voltage [V]"].entries
# SEI = sol_SEI["Loss of lithium to SEI [mol]"].entries
# lithium_neg_SEI = sol_SEI["Total lithium in negative electrode [mol]"].entries
# lithium_pos_SEI = sol_SEI["Total lithium in positive electrode [mol]"].entries
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18,4))
# ax1.plot(t_DFN,V_DFN,label="No SEI (Standard DFN mnodel) ")
# ax1.plot(t_SEI,V_SEI,label="SEI Diffusion limited SEI model")
# ax1.set_xlabel("Time [s]")
# ax1.set_ylabel("Voltage [V]")
# ax1.legend()
# ax2.plot(t_DFN,No_SEI,label="No SEI")
# ax2.plot(t_SEI,SEI,label="SEI formation")
# ax2.set_xlabel("Time [s]")
# ax2.set_ylabel("Loss of lithium to SEI [mol]")
# ax2.legend()
# plt.show()

# fig, ax = plt.subplots()
# ax.plot(t_SEI,lithium_neg_SEI+lithium_pos_SEI)
# ax.plot(t_SEI,lithium_neg_SEI[0]+lithium_pos_SEI[0]-SEI,linestyle="dashed")
# ax.set_xlabel("Time [s]")
# ax.set_ylabel("Total lithium in electrodes [mol]")
# plt.show()


# # Formation cycle + characterisation cycle + 1000 cycles + characterisation cycle


# N_cycles = 5

# standard_protocol = pybamm.Experiment(
#     [
#         "Hold at 4.2 V until C/100",
#         "Rest for 4 hour",
#         "Discharge at C/10 until 2.5 V",
#         "Charge at 0.3C until 4.2 V",
#          "Hold at 4.2 V until C/100",
#         ("Discharge at 1C until 2.5 V",
#         "Charge at 0.3C until 4.2 V",
#          "Hold at 4.2 V until C/100"
#          )* N_cycles,
#         "Discharge at C/10 until 2.5 V",
#         "Charge at 0.3C until 4.2 V",
#          "Hold at 4.2 V until C/100",
#     ]
# )
# sims_standard = []
# # Default value
# # "Outer SEI solvent diffusivity [m2.s-1]": 2.5000000000000002e-22, 
# # Values we are tetsing for
# # param["Outer SEI solvent diffusivity [m2.s-1]"] = 2.5e-21
# # param["Outer SEI solvent diffusivity [m2.s-1]"] = 7.5e-21
# # param["Outer SEI solvent diffusivity [m2.s-1]"] = 1.25e-21



# param["Outer SEI solvent diffusivity [m2.s-1]"] = 2.5000000000000002e-21
# sim_DFN = pybamm.Simulation(model_DFN, parameter_values=param, experiment=standard_protocol, var_pts=var_pts)
# sol_DFN = sim_DFN.solve(calc_esoh=False)

# sol_DFN.save_data("DFN_sol_standard.csv",
#                             [
#                         "Time [min]", 
#                         "Current [A]", 
#                         "Terminal voltage [V]", 
#                         "Discharge capacity [A.h]",
#                         "Loss of capacity to SEI [A.h]",
#                         "Negative electrode capacity [A.h]",
#                         "Positive electrode capacity [A.h]",
#                         "Throughput capacity [A.h]",
#                         "Total capacity lost to side reactions [A.h]",
#                         "Total lithium capacity [A.h]",
#                         "Loss of lithium to SEI [mol]",
#                         "Total lithium in negative electrode [mol]",
#                          "Total lithium in positive electrode [mol]"
#                          ]
#                       , to_format="csv")

# t_DFN = sol_DFN["Time [s]"].entries
# V_DFN = sol_DFN["Terminal voltage [V]"].entries
# No_SEI = sol_DFN["Loss of lithium to SEI [mol]"].entries
# lithium_neg_DFN = sol_DFN["Total lithium in negative electrode [mol]"].entries
# lithium_pos_DFN = sol_DFN["Total lithium in positive electrode [mol]"].entries
# t_SEI = sol_SEI["Time [s]"].entries
# V_SEI = sol_SEI["Terminal voltage [V]"].entries
# SEI = sol_SEI["Loss of lithium to SEI [mol]"].entries
# lithium_neg_SEI = sol_SEI["Total lithium in negative electrode [mol]"].entries
# lithium_pos_SEI = sol_SEI["Total lithium in positive electrode [mol]"].entries

# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8,4))
# ax1.plot(t_DFN,V_DFN,label="No SEI (Standard DFN mnodel) ")
# ax1.plot(t_SEI,V_SEI,label="SEI Diffusion limited SEI model")
# ax1.set_xlabel("Time [s]")
# ax1.set_ylabel("Terminal voltage [V]")
# ax1.legend()
# ax2.plot(t_DFN,No_SEI,label="No SEI")
# ax2.plot(t_SEI,SEI,label="SEI formation")
# ax2.set_xlabel("Time [s]")
# ax2.set_ylabel("Loss of lithium to SEI [mol]")
# ax2.legend()
# plt.show()
