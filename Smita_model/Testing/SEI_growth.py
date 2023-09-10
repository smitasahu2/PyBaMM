import pybamm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv

# pybamm.set_logging_level("INFO")
model_SEI = pybamm.lithium_ion.DFN({"SEI": "solvent-diffusion limited", 
                                    "SEI porosity change": "true",
                                    "calculate discharge energy" : "true"})

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

# Formation cycle + characterisation cycle + 1000 cycles + characterisation cycle 

N_cycles = 4

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
 
# Solvent Diffusion limited SEI

# "Outer SEI solvent diffusivity [m2.s-1]": 2.5000000000000002e-22,
# param["Outer SEI solvent diffusivity [m2.s-1]"] = 2.5e-22 
# param["Outer SEI solvent diffusivity [m2.s-1]"] = 2.5e-21
# param["Outer SEI solvent diffusivity [m2.s-1]"] = 7.5e-21 
param["Outer SEI solvent diffusivity [m2.s-1]"] = 1.25e-20
exp = pybamm.Experiment(["Hold at 4.2 V until C/100"])

# parameter_values["Current function [A]"] = 10 
# sim_SEI = pybamm.Simulation(model_SEI, parameter_values=param, experiment=exp, var_pts=var_pts)
sim_SEI = pybamm.Simulation(model_SEI, parameter_values=param, experiment=standard_protocol, var_pts=var_pts)
sol_SEI = sim_SEI.solve(calc_esoh=False)

pybamm.dynamic_plot(sol_SEI)
# sol_SEI.save("SEI_Solo_75e21.pkl")
# sol_SEI.save("SEI_Solo125e20.csv")
# sol_SEI.save("SEI_Solo25e21_long.csv")

# pybamm.dynamic_plot(sol_SEI)
# Saving data and downloading all the 'formation cycle' files with extension .csv and .mat

sol_SEI.save_data("SEI_Solo25e22_1.csv",
                            [
                        "Time [min]", 
                        "Current [A]", 
                        "Terminal voltage [V]", 
                        "Discharge capacity [A.h]",
                        "Loss of capacity to SEI [A.h]",
                        "Negative electrode capacity [A.h]",
                        "Positive electrode capacity [A.h]",
                        "Throughput capacity [A.h]",
                        "Total capacity lost to side reactions [A.h]",
                        "Total lithium capacity [A.h]",
                        "Loss of lithium to SEI [mol]",
                        "Total lithium in negative electrode [mol]",
                         "Total lithium in positive electrode [mol]",
                         "Loss of lithium inventory [%]",
                         "Loss of active material in negative electrode [%]",
                         ]
                      , to_format="csv")

# sol_SEI.save_data("SEI_Solo25e22_porosity.csv",
#                             [
#                            "Negative electrode porosity",
#                          ]
#                       , to_format="csv")

    
    
Qt = sol_SEI["Throughput capacity [A.h]"].entries
Q_SEI = sol_SEI["Loss of capacity to SEI [A.h]"].entries
Q_SEI_cr = sol_SEI["Loss of capacity to SEI on cracks [A.h]"].entries
Q_plating = sol_SEI["Loss of capacity to lithium plating [A.h]"].entries
Q_side = sol_SEI["Total capacity lost to side reactions [A.h]"].entries
Q_LLI = sol_SEI["Total lithium lost [mol]"].entries * 96485.3 / 3600  # convert from mol to A.h
plt.figure()
plt.plot(Qt,Q_SEI,label="SEI",linestyle="dashed")
plt.plot(Qt,Q_SEI_cr,label="SEI on cracks",linestyle="dashdot")
plt.plot(Qt,Q_plating,label="Li plating",linestyle="dotted")
plt.plot(Qt,Q_side,label="All side reactions",linestyle=(0,(6,1)))
plt.plot(Qt,Q_LLI,label="All LLI")
plt.xlabel("Throughput capacity [A.h]")
plt.ylabel("Capacity loss [A.h]")
plt.legend()
plt.show()

Qt = sol_SEI["Throughput capacity [A.h]"].entries
LLI = sol_SEI["Loss of lithium inventory [%]"].entries
LAM_neg = sol_SEI["Loss of active material in negative electrode [%]"].entries
LAM_pos = sol_SEI["Loss of active material in positive electrode [%]"].entries
plt.figure()
plt.plot(Qt,LLI,label="LLI")
plt.plot(Qt,LAM_neg,label="LAM (negative)")
plt.plot(Qt,LAM_pos,label="LAM (positive)")
plt.xlabel("Throughput capacity [A.h]")
plt.ylabel("Degradation modes [%]")
plt.legend()
plt.show()

eps_neg_avg = sol_SEI["X-averaged negative electrode porosity"].entries
eps_neg_sep = sol_SEI["Negative electrode porosity"].entries[-1,:]
eps_neg_CC = sol_SEI["Negative electrode porosity"].entries[0,:]
plt.figure()
plt.plot(Qt,eps_neg_avg,label="Average")
plt.plot(Qt,eps_neg_sep,label="Separator",linestyle="dotted")
plt.plot(Qt,eps_neg_CC,label="Current collector",linestyle="dashed")
plt.xlabel("Throughput capacity [A.h]")
plt.ylabel("Negative electrode porosity")
plt.legend()
plt.show()

    
# Disc_cap = sol_SEI["Discharge capacity [A.h]"].entries
# SEI_cap_loss = sol_SEI["Loss of capacity to SEI [A.h]"].entries
# A_cap_loss = sol_SEI["Negative electrode capacity [A.h]"].entries
# C_cap_loss = sol_SEI["Positive electrode capacity [A.h]"].entries
# Throughput = sol_SEI["Throughput capacity [A.h]"].entries
# Qtot_cap_loss= sol_SEI["Total capacity lost to side reactions [A.h]"].entries
# Li_cap_loss= sol_SEI["Total lithium capacity [A.h]"].entries
# I_F= sol_SEI["Current [A]"].entries
# t_F = sol_SEI["Time [min]"].entries
# V_F = sol_SEI["Terminal voltage [V]"].entries

# fig, ax = plt.subplots(2, 2, figsize=(10, 7))
# ax[0,0].plot(t_F, I_F,color="purple", linestyle="solid")
# ax[0,0].set(xlabel="Time [h]", ylabel="I [A]")
# ax[0,1].plot(t_F, V_F,color="purple", linestyle="solid")
# ax[0,1].set(xlabel="Time [h]", ylabel="$V$ [V]")
# ax[1,0].plot(t_F, Disc_cap,color="purple", linestyle="solid")
# ax[1,0].set(xlabel="Time [h]", ylabel="Discharge Capacity [A.h]")
# ax[1,1].plot(t_F, Qtot_cap_loss,color="purple", linestyle="solid")
# ax[1,1].set(xlabel="Time [h]", ylabel="Total capacity loss  [A.h]")
# plt.tight_layout()
# plt.show()

