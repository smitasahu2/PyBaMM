import pybamm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
from numpy import savetxt
import ploot_plate
# pybamm.set_logging_level("INFO")
#source env/bin/activate
def run_all_test(all_test1, kpe):
    standard_protocol = pybamm.Experiment(
    ["Discharge at 1C for 3490 seconds",
        "Charge at 1C for 2510 seconds",
        ]*10
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
    model_all = pybamm.lithium_ion.DFN({"lithium plating": "partially reversible",
                                    "SEI": "solvent-diffusion limited", 
                                    "SEI porosity change": "true",
                                    "calculate discharge energy" : "true"})
    param["Lithium plating kinetic rate constant [m.s-1]"] = kpe
    kpe_str = f"{kpe:.2e}"
    print(f"Lithium plating kinetic rate constant [m.s-1 = {kpe_str}")
    param["Dead lithium decay constant [s-1]"] =  1e-06
    sim_all = pybamm.Simulation(model_all, experiment=standard_protocol, parameter_values=param, var_pts=var_pts)
    sol_all = sim_all.solve()
    
    L_SEI = sol_all["Total SEI thickness [m]"].entries
    savetxt(f'LSEI_kpe{kpe_str}.csv', L_SEI, delimiter=',')
    
    porosity = sol_all["Negative electrode porosity"].entries
    savetxt(f'porosity_kpe{kpe_str}.csv', porosity, delimiter=',')
    
    C_Li=sol_all["Lithium plating concentration [mol.m-3]"].entries
    savetxt(f'cli_kpe{kpe_str}.csv', C_Li, delimiter=',')

    Dead = sol_all["Dead lithium concentration [mol.m-3]"].entries
    savetxt(f'dli_kpe{kpe_str}.csv', Dead, delimiter=',')

    sol_all.save_data(f"plate_D{kpe_str}.csv",
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
    ploot_plate.myplot(sol_all)
    
    print(param)

all_test1_values = [1, 2]  # Add all the test cases you want to run
kpe_values = [1e-10, 1e-9]  # Corresponding diffusivity values

for i, all_test1 in enumerate(all_test1_values):
    run_all_test(all_test1, kpe_values[i])
