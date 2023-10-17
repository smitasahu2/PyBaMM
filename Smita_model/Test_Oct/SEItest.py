import pybamm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
from numpy import savetxt
import ploot
# pybamm.set_logging_level("INFO")
#source env/bin/activate
def run_SEI_test(SEI_test1, diffusivity):
    standard_protocol = pybamm.Experiment(
    ["Discharge at 0.5C for 7190 seconds",
        "Charge at 0.5C for 6220 seconds",
        ]
    )
    var_pts = {
    "x_n": 20,  # negative electrode
    "x_s": 15,  # separator 
    "x_p": 20,  # positive electrode
    "r_n": 20,  # negative particle
    "r_p": 20,  # positive particle
      }
    param = pybamm.ParameterValues("OKane2022") 
    param["Current function [A]"] = 2.5 
    param["Ratio of lithium moles to SEI moles"]= 2.0
    model_SEI = pybamm.lithium_ion.DFN({"SEI": "solvent-diffusion limited", 
                                    "SEI porosity change": "true",
                                    "calculate discharge energy" : "true"})
    param["Outer SEI solvent diffusivity [m2.s-1]"] = diffusivity
    diffusivity_str = f"{diffusivity:.2e}"
    print(f"Outer SEI solvent diffusivity [m2 s-1] = {diffusivity_str}")
    sim_SEI = pybamm.Simulation(model_SEI, experiment=standard_protocol, parameter_values=param, var_pts=var_pts)
    sol_SEI = sim_SEI.solve()
    
    L_SEI = sol_SEI["Total SEI thickness [m]"].entries
    savetxt(f'LSEI_D{diffusivity_str}.csv', L_SEI, delimiter=',')
    
    porosity = sol_SEI["Negative electrode porosity"].entries
    savetxt(f'porosity_D{diffusivity_str}.csv', porosity, delimiter=',')
    
    sol_SEI.save_data(f"SEI_D{diffusivity_str}.csv",
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
                      ],
                      to_format="csv")
    ploot.myplot(sol_SEI)
    print(param)

SEI_test1_values = [1, 2, 3, 4]  # Add all the test cases you want to run
diffusivity_values = [2.5e-21, 7.5e-21, 1.25e-20, 2.5e-22]  # Corresponding diffusivity values

for i, SEI_test1 in enumerate(SEI_test1_values):
    run_SEI_test(SEI_test1, diffusivity_values[i])
