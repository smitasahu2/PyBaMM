import pybamm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
from numpy import savetxt
import ploot 

# pybamm.set_logging_level("INFO")
# SEI_test1 = 0  # param["Outer SEI solvent diffusivity [m2.s-1]"] 2.5000000000000002e-22, pybamm's default value
# SEI_test1 = 1  # param["Outer SEI solvent diffusivity [m2.s-1]"] = 2.5e-21     
# SEI_test1 = 2  # param["Outer SEI solvent diffusivity [m2.s-1]"] = 7.5e-21 
# SEI_test1 = 3  # param["Outer SEI solvent diffusivity [m2.s-1]"] = 1.25e-20

SEI_test1 = 0

t_eval = np.linspace(0, 3600, 10000)
model_SEI = pybamm.lithium_ion.DFN({"SEI": "solvent-diffusion limited", 
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
param["Ratio of lithium moles to SEI moles"]= 2.0   # In order to match all the test with the DandeLiion this parameter has to be 2
N_cycles = 1

# standard_protocol = pybamm.Experiment(
#     ["Discharge at 1C for 60 minutes",
#     "Charge at 1C for 60 minutes",
#     ]#*5  # final capacity check
# )

standard_protocol = pybamm.Experiment(
    ["Discharge at 1C until 2.367V",
    "Charge at 1C until 4.212V",
    ]#*5  # final capacity check
)

SEI_testall = [1, 2, 3, 4]
for SEI_test1 in SEI_testall:
    if SEI_test1 == 1:
        param["Outer SEI solvent diffusivity [m2.s-1]"] = 2.5e-21
        print("Outer SEI solvent diffusivity [m2 s-1] = 2.5e-21")
        sim_SEI = pybamm.Simulation(model_SEI,experiment=standard_protocol, parameter_values=param, var_pts=var_pts)
        sol_SEI = sim_SEI.solve(t_eval)
        L_SEI = sol_SEI["Total SEI thickness [m]"].entries
        savetxt('LSEI_D2.5e-21.csv', L_SEI, delimiter=',')
        porosity = sol_SEI["Negative electrode porosity"].entries
        savetxt('porosity_D2.5e-21.csv', porosity, delimiter=',')
        sol_SEI.save_data("SEI_D2.5e-21.csv",[    
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
                        "Total lithium lost [mol]"], to_format="csv") 
        ploot.myplot(sol_SEI)
                    
    elif SEI_test1 == 2:
        param["Outer SEI solvent diffusivity [m2.s-1]"] = 7.5e-21
        print("Outer SEI solvent diffusivity [m2 s-1] = 7.5e-21")
        sim_SEI = pybamm.Simulation(model_SEI,experiment=standard_protocol, parameter_values=param, var_pts=var_pts)
        sol_SEI = sim_SEI.solve(t_eval)
        L_SEI = sol_SEI["Total SEI thickness [m]"].entries
        savetxt('LSEI_D7.5e-21.csv', L_SEI, delimiter=',')
        porosity = sol_SEI["Negative electrode porosity"].entries
        savetxt('porosity_D7.5e-21.csv', porosity, delimiter=',')
        sol_SEI.save_data("SEI_D7.5e-21.csv",
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
                        "Total lithium lost [mol]"]
                      , to_format="csv") 
        ploot.myplot(sol_SEI)
    elif SEI_test1 == 3:
        param["Outer SEI solvent diffusivity [m2.s-1]"] = 1.25e-20
        print("Outer SEI solvent diffusivity [m2 s-1] = 1.25e-20")
        sim_SEI = pybamm.Simulation(model_SEI,experiment=standard_protocol, parameter_values=param, var_pts=var_pts)
        sol_SEI = sim_SEI.solve(t_eval)
        L_SEI = sol_SEI["Total SEI thickness [m]"].entries
        savetxt('LSEI_D1.25e-20.csv', L_SEI, delimiter=',')
        porosity = sol_SEI["Negative electrode porosity"].entries
        savetxt('porosity_D1.25e-20.csv', porosity, delimiter=',')
        sol_SEI.save_data("SEI_D1.25e-20.csv",
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
                        "Total lithium lost [mol]"]
                      , to_format="csv") 
        ploot.myplot(sol_SEI)
    else:
        param["Outer SEI solvent diffusivity [m2.s-1]"] = 2.5e-22
        print("Outer SEI solvent diffusivity [m2.s-1] = 2.5000000000000002e-22, pybamm's default value")
        sim_SEI = pybamm.Simulation(model_SEI,experiment=standard_protocol, parameter_values=param, var_pts=var_pts)
        sol_SEI = sim_SEI.solve(t_eval)
        L_SEI = sol_SEI["Total SEI thickness [m]"].entries
        savetxt('LSEI_D2.5e-22.csv', L_SEI, delimiter=',')
        porosity = sol_SEI["Negative electrode porosity"].entries
        savetxt('porosity_D2.5e-22.csv', porosity, delimiter=',')
        sol_SEI.save_data("SEI_D2.5e-22.csv",
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
                        "Total lithium lost [mol]"]
                      , to_format="csv") 
        ploot.myplot(sol_SEI)
