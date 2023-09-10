import pybamm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
from numpy import savetxt
# pybamm.set_logging_level("INFO")

"""""
SEI_test1 = 0  # param["Outer SEI solvent diffusivity [m2.s-1]"] 2.5000000000000002e-22, pybamm's default value
SEI_test1 = 1  # param["Outer SEI solvent diffusivity [m2.s-1]"] = 2.5e-21     
SEI_test1 = 2  # param["Outer SEI solvent diffusivity [m2.s-1]"] = 7.5e-21 
SEI_test1 = 3  # param["Outer SEI solvent diffusivity [m2.s-1]"] = 1.25e-20
"""""
SEI_test1 = 0

# param["Outer SEI solvent diffusivity [m2.s-1]"] = 2.5e-22    
#param["Outer SEI solvent diffusivity [m2.s-1]"] = 2.5e-21
# param["Outer SEI solvent diffusivity [m2.s-1]"] = 7.5e-21 
# param["Outer SEI solvent diffusivity [m2.s-1]"] = 1.25e-20




t_eval = np.linspace(0, 3600, 10000)
model_plating = pybamm.lithium_ion.DFN({"lithium plating": "partially reversible",
                                           "SEI": "solvent-diffusion limited",
                                           "SEI porosity change": "true",
                                           "calculate discharge energy" : "true"})
param = pybamm.ParameterValues("OKane2022")
var_pts = {
    "x_n": 30,  # negative electrode
    "x_s": 15,  # separator 
    "x_p": 30,  # positive electrode
    "r_n": 30,  # negative particle
    "r_p": 30,  # positive particle
}
param["Current function [A]"] = 5 
param["Outer SEI solvent diffusivity [m2.s-1]"] = 25e-22
param["Lithium plating kinetic rate constant [m.s-1]"]= 1e-10

SEI_testall = [1]#, 2, 3, 4]
for SEI_test1 in SEI_testall:
    if SEI_test1 == 1:
        param["Dead lithium decay constant [s-1]"] = 1e-06
        sim_plating= pybamm.Simulation(model_plating, parameter_values=param, var_pts=var_pts)
        sol_plating= sim_plating.solve(t_eval)
        L_SEI = sol_plating["Total SEI thickness [m]"].entries
        savetxt('LSEI_gamma_1e6.csv', L_SEI, delimiter=',')
        porosity = sol_plating["Negative electrode porosity"].entries
        savetxt('porosity__gamma_1e6.csv', porosity, delimiter=',')
        sol_plating.save_data("SEI__gamma_1e6.csv",
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
        print("Dead lithium decay constant [s-1] = 1e-06")
    elif SEI_test1 == 2:
        param["Outer SEI solvent diffusivity [m2.s-1]"] = 7.5e-21
        sim_plating = pybamm.Simulation(model_plating, parameter_values=param, var_pts=var_pts)
        sol_plating = sim_plating.solve(t_eval)
        L_SEI = sol_plating["Total SEI thickness [m]"].entries
        savetxt('LSEI_D7.5e-21.csv', L_SEI, delimiter=',')
        porosity = sol_plating["Negative electrode porosity"].entries
        savetxt('porosity_D7.5e-21.csv', porosity, delimiter=',')
        sol_plating.save_data("SEI_D7.5e-21.csv",
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
        print("Outer SEI solvent diffusivity [m2 s-1] = 7.5e-21")
    elif SEI_test1 == 3:
        param["Outer SEI solvent diffusivity [m2.s-1]"] = 1.25e-20
        sim_plating = pybamm.Simulation(model_plating, parameter_values=param, var_pts=var_pts)
        sol_plating = sim_plating.solve(t_eval)
        L_SEI = sol_plating["Total SEI thickness [m]"].entries
        savetxt('LSEI_D1.25e-20.csv', L_SEI, delimiter=',')
        porosity = sol_plating["Negative electrode porosity"].entries
        savetxt('porosity_D1.25e-20.csv', porosity, delimiter=',')
        sol_plating.save_data("SEI_D1.25e-20.csv",
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
        print("Outer SEI solvent diffusivity [m2 s-1] = 1.25e-20")
    else:

        print("Outer SEI solvent diffusivity [m2.s-1] = 2.5000000000000002e-22, pybamm's default value")
        sim_plating = pybamm.Simulation(model_plating, parameter_values=param, var_pts=var_pts)
        sol_plating = sim_plating.solve(t_eval)
        L_SEI = sol_plating["Total SEI thickness [m]"].entries
        savetxt('LSEI_D2.5e-22.csv', L_SEI, delimiter=',')
        porosity = sol_plating["Negative electrode porosity"].entries
        savetxt('porosity_D2.5e-22.csv', porosity, delimiter=',')
        sol_plating.save_data("SEI_D2.5e-22.csv",
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

Qt = sol_plating["Throughput capacity [A.h]"].entries
Q_SEI = sol_plating["Loss of capacity to SEI [A.h]"].entries
Q_SEI_cr = sol_plating["Loss of capacity to SEI on cracks [A.h]"].entries
Q_plating = sol_plating["Loss of capacity to lithium plating [A.h]"].entries
Q_side = sol_plating["Total capacity lost to side reactions [A.h]"].entries
Q_LLI = sol_plating["Total lithium lost [mol]"].entries * 96485.3 / 3600  # convert from mol to A.h
plt.figure()
plt.plot(Qt,Q_SEI,label="SEI",linestyle="dashed")
plt.plot(Qt,Q_SEI_cr,label="SEI on cracks",linestyle="dashdot")
plt.plot(Qt,Q_plating,label="Li plating",linestyle="dotted")
plt.plot(Qt,Q_side,label="All side reactions",linestyle=(0,(6,1)))
LAM_neg = sol_plating["Loss of active material in negative electrode [%]"].entries
LAM_pos = sol_plating["Loss of active material in positive electrode [%]"].entries
plt.figure()
plt.plot(Qt,Q_LLI,label="LLI")
plt.plot(Qt,LAM_neg,label="LAM (negative)")
plt.plot(Qt,LAM_pos,label="LAM (positive)")
plt.xlabel("Throughput capacity [A.h]")
plt.ylabel("Degradation modes [%]")
plt.legend()
plt.show()

eps_neg_avg = sol_plating["X-averaged negative electrode porosity"].entries
eps_neg_sep = sol_plating["Negative electrode porosity"].entries[-1,:]
eps_neg_CC = sol_plating["Negative electrode porosity"].entries[0,:]
plt.figure()
plt.plot(Qt,eps_neg_avg,label="Average")
plt.plot(Qt,eps_neg_sep,label="Separator",linestyle="dotted")
plt.plot(Qt,eps_neg_CC,label="Current collector",linestyle="dashed")
plt.xlabel("Throughput capacity [A.h]")
plt.ylabel("Negative electrode porosity")
plt.legend()
plt.show()

pybamm.dynamic_plot(sol_plating)




 
# # Solvent Diffusion limited SEI

# # "Outer SEI solvent diffusivity [m2.s-1]": 2.5000000000000002e-22,
# # param["Outer SEI solvent diffusivity [m2.s-1]"] = 2.5e-22    
# param["Outer SEI solvent diffusivity [m2.s-1]"] = 2.5e-21
# # param["Outer SEI solvent diffusivity [m2.s-1]"] = 7.5e-21 
# # param["Outer SEI solvent diffusivity [m2.s-1]"] = 1.25e-20


# sim_plating = pybamm.Simulation(model_plating, parameter_values=param, experiment=exp, var_pts=var_pts)

# sim_plating = pybamm.Simulation(model_plating, parameter_values=param, experiment=standard_protocol, var_pts=var_pts)

# pybamm.dynamic_plot(sol_plating)
# print(param)
# model_plating.variables.search("thickness")
# L_SEI = sol_plating["Total SEI thickness [m]"].entries
# # print(L_SEI)
# savetxt('L_D2.5e-22.csv', L_SEI, delimiter=',')
# # savetxt('L_D2.5e-21.csv', L_SEI, delimiter=',')
# # savetxt('L_D7.5e-21.csv', L_SEI, delimiter=',')
# #savetxt('L_D1.25e-20.csv', L_SEI, delimiter=',')
# # print(L_SEI)
# savetxt('po_D2.5e-22.csv', porosity, delimiter=',')
# # savetxt('po_D2.5e-21.csv', porosity, delimiter=',')
# # savetxt('po_D7.5e-21.csv', porosity, delimiter=',')
# #savetxt('po_D1.25e-20.csv', porosity, delimiter=',')


# sol_plating.save_data("SEI_D2.5e-22.csv",
# # sol_plating.save_data("SEI_D2.5e-21.csv",
# # sol_plating.save_data("SEI_D7.5e-21.csv",
# # sol_plating.save_data("SEI_D1.25e-20.csv",
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
#                          "Total lithium in positive electrode [mol]",
#                          "Loss of lithium inventory [%]",
#                          "Loss of active material in negative electrode [%]",
#                          ]
#                       , to_format="csv")

# sol_plating.save_data("porosity_D2.5e-22.csv", 
# # sol_plating.save_data("porosity_D2.5e-21.csv", 
# # sol_plating.save_data("porosity_D7.5e-21.csv", 
# # sol_plating.save_data("porosity_D1.25e-20.csv", 
#                             [
# # "Negative electrode porosity",
# # "Negative electrode porosity"
#                          ]
#                       , to_format="csv")    
    
# Qt = sol_plating["Throughput capacity [A.h]"].entries
# Q_SEI = sol_plating["Loss of capacity to SEI [A.h]"].entries
# Q_SEI_cr = sol_plating["Loss of capacity to SEI on cracks [A.h]"].entries
# Q_plating = sol_plating["Loss of capacity to lithium plating [A.h]"].entries
# Q_side = sol_plating["Total capacity lost to side reactions [A.h]"].entries
# Q_LLI = sol_plating["Total lithium lost [mol]"].entries * 96485.3 / 3600  # convert from mol to A.h
# plt.figure()
# plt.plot(Qt,Q_SEI,label="SEI",linestyle="dashed")
# plt.plot(Qt,Q_SEI_cr,label="SEI on cracks",linestyle="dashdot")
# plt.plot(Qt,Q_plating,label="Li plating",linestyle="dotted")
# plt.plot(Qt,Q_side,label="All side reactions",linestyle=(0,(6,1)))
# plt.plot(Qt,Q_LLI,label="All LLI")
# plt.xlabel("Throughput capacity [A.h]")
# plt.ylabel("Capacity loss [A.h]")
# plt.legend()
# plt.show()

# Qt = sol_plating["Throughput capacity [A.h]"].entries
# LLI = sol_plating["Loss of lithium inventory [%]"].entries
# LAM_neg = sol_plating["Loss of active material in negative electrode [%]"].entries
# LAM_pos = sol_plating["Loss of active material in positive electrode [%]"].entries
# plt.figure()
# plt.plot(Qt,LLI,label="LLI")
# plt.plot(Qt,LAM_neg,label="LAM (negative)")
# plt.plot(Qt,LAM_pos,label="LAM (positive)")
# plt.xlabel("Throughput capacity [A.h]")
# plt.ylabel("Degradation modes [%]")
# plt.legend()
# plt.show()

# eps_neg_avg = sol_plating["X-averaged negative electrode porosity"].entries
# eps_neg_sep = sol_plating["Negative electrode porosity"].entries[-1,:]
# eps_neg_CC = sol_plating["Negative electrode porosity"].entries[0,:]
# plt.figure()
# plt.plot(Qt,eps_neg_avg,label="Average")
# plt.plot(Qt,eps_neg_sep,label="Separator",linestyle="dotted")
# plt.plot(Qt,eps_neg_CC,label="Current collector",linestyle="dashed")
# plt.xlabel("Throughput capacity [A.h]")
# plt.ylabel("Negative electrode porosity")
# plt.legend()
# plt.show()
