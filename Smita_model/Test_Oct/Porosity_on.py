import pybamm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
from numpy import savetxt
import ploot
# pybamm.set_logging_level("INFO")
#source env/bin/activate

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
model_SEI = pybamm.lithium_ion.DFN({"SEI": "solvent-diffusion limited", 
                                    "SEI porosity change": "true",
                                    "calculate discharge energy" : "true"})

param = pybamm.ParameterValues("OKane2022") 
print(param)
var_pts = {
    "x_n": 20,  # negative electrode
    "x_s": 15,  # separator 
    "x_p": 20,  # positive electrode
    "r_n": 20,  # negative particle
    "r_p": 20,  # positive particle
 }
param["Current function [A]"] = 2.5 
param["Ratio of lithium moles to SEI moles"]= 2.0
N_cycles = 1
standard_protocol = pybamm.Experiment(
    ["Discharge at 0.5C for 7190 seconds",
        "Charge at 0.5C for 6220 seconds",
        ]
)
standard_protocol = pybamm.Experiment(
    ["Discharge at 0.5C for 7190 seconds",
        "Charge at 0.5C for 6220 seconds",
        ]
)
SEI_testall = [1];# [1, 2, 3, 4]
for SEI_test1 in SEI_testall:
    if SEI_test1 == 1:
        param["Outer SEI solvent diffusivity [m2.s-1]"] = 2.5e-21
        print("Outer SEI solvent diffusivity [m2 s-1] = 2.5e-21")
        sim_SEI = pybamm.Simulation(model_SEI,experiment=standard_protocol, parameter_values=param, var_pts=var_pts)
        sol_SEI = sim_SEI.solve()
        L_SEI = sol_SEI["Total SEI thickness [m]"].entries
        savetxt('LSEI_D25e-21.csv', L_SEI, delimiter=',')
        porosity = sol_SEI["Negative electrode porosity"].entries
        savetxt('porosity_D25e-21.csv', porosity, delimiter=',')
        sol_SEI.save_data("SEI_D2.5e-21.csv",
                            [    
                        "Time [min]", 
                        "Current [A]", 
                        "Terminal voltage [V]", 
                        "Discharge capacity [A.h]",
                        "Loss of capacity to SEI [A.h]",
                        "Negative electrode capacity [A.h]",
                        "Throughput capacity [A.h]",
                        "Total capacity lost to side reactions [A.h]",
                        "Total lithium capacity [A.h]",
                        "Loss of lithium to SEI [mol]",
                        "Total lithium in negative electrode [mol]",
                         "Loss of lithium inventory [%]",
                         "Loss of active material in negative electrode [%]",
                         ]
                      , to_format="csv") 
        # ploot.myplot(sol_SEI)
        print(param)

    elif SEI_test1 == 2:
        param["Outer SEI solvent diffusivity [m2.s-1]"] = 7.5e-21
        print("Outer SEI solvent diffusivity [m2 s-1] = 7.5e-21")

        sim_SEI = pybamm.Simulation(model_SEI,experiment=standard_protocol, parameter_values=param, var_pts=var_pts)
        sol_SEI = sim_SEI.solve()
        L_SEI = sol_SEI["Total SEI thickness [m]"].entries
        savetxt('LSEI_D75e-21.csv', L_SEI, delimiter=',')
        porosity = sol_SEI["Negative electrode porosity"].entries
        savetxt('porosity_D75e-21.csv', porosity, delimiter=',')
        sol_SEI.save_data("SEI_D75e-21.csv",
                            [    
                        "Time [min]", 
                        "Current [A]", 
                        "Terminal voltage [V]", 
                        "Discharge capacity [A.h]",
                        "Loss of capacity to SEI [A.h]",
                        "Negative electrode capacity [A.h]",
                        "Throughput capacity [A.h]",
                        "Total capacity lost to side reactions [A.h]",
                        "Loss of lithium inventory [%]",
                         "Loss of active material in negative electrode [%]",
                         ]
                      , to_format="csv") 
        ploot.myplot(sol_SEI)
    elif SEI_test1 == 3:
        param["Outer SEI solvent diffusivity [m2.s-1]"] = 1.25e-20
        print("Outer SEI solvent diffusivity [m2 s-1] = 1.25e-20")

        sim_SEI = pybamm.Simulation(model_SEI,experiment=standard_protocol, parameter_values=param, var_pts=var_pts)
        sol_SEI = sim_SEI.solve()
        L_SEI = sol_SEI["Total SEI thickness [m]"].entries
        savetxt('LSEI_D125e-20.csv', L_SEI, delimiter=',')
        porosity = sol_SEI["Negative electrode porosity"].entries
        savetxt('porosity_D125e-20.csv', porosity, delimiter=',')
        sol_SEI.save_data("SEI_D125e-20.csv",
                         [    "Time [min]", 
                        "Current [A]", 
                        "Terminal voltage [V]", 
                        "Discharge capacity [A.h]",
                        "Loss of capacity to SEI [A.h]",
                        "Negative electrode capacity [A.h]",
                        "Throughput capacity [A.h]",
                        "Total capacity lost to side reactions [A.h]",
                        "Total lithium capacity [A.h]",
                        "Loss of lithium to SEI [mol]",
                        "Total lithium in negative electrode [mol]",
                         "Loss of lithium inventory [%]",
                         "Loss of active material in negative electrode [%]",]
                      , to_format="csv") 
        ploot.myplot(sol_SEI)
    else:
        param["Outer SEI solvent diffusivity [m2.s-1]"] = 2.5e-22
        print("Outer SEI solvent diffusivity [m2.s-1] = 2.5000000000000002e-22, pybamm's default value")
        sim_SEI = pybamm.Simulation(model_SEI,experiment=standard_protocol, parameter_values=param, var_pts=var_pts)
        sol_SEI = sim_SEI.solve()
        L_SEI = sol_SEI["Total SEI thickness [m]"].entries
        savetxt('LSEI_D25e-22.csv', L_SEI, delimiter=',')
        porosity = sol_SEI["Negative electrode porosity"].entries
        savetxt('porosity_D25e-22.csv', porosity, delimiter=',')
        sol_SEI.save_data("SEI_D25e-22.csv",
                                                [    "Time [min]", 
                        "Current [A]", 
                        "Terminal voltage [V]", 
                        "Discharge capacity [A.h]",
                        "Loss of capacity to SEI [A.h]",
                        "Negative electrode capacity [A.h]",
                        "Throughput capacity [A.h]",
                        "Total capacity lost to side reactions [A.h]",
                        "Total lithium capacity [A.h]",
                        "Loss of lithium to SEI [mol]",
                        "Total lithium in negative electrode [mol]",
                         "Loss of lithium inventory [%]",
                         "Loss of active material in negative electrode [%]",]
        , to_format="csv") 
        ploot.myplot(sol_SEI)
#         #
# model_SEI.print_parameter_info()
# {k: v for k,v in model_SEI.default_parameter_values.items() if k in model_SEI._parameter_info}
