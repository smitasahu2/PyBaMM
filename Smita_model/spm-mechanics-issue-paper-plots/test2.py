#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 17:01:34 2023

@author: smita
"""

import pybamm
from models import MSPM
from parameters import get_parameter_values
import numpy as np
import matplotlib.pyplot as plt
import ploot_voltage_effect


models = [
    pybamm.lithium_ion.SPM(
        options={"particle": "uniform profile", "intercalation kinetics": "linear"}
    ),
    MSPM(options={"particle": "uniform profile"})
]

parameter_values = pybamm.ParameterValues(get_parameter_values())

"""
[1] SPM and chemomechanical model: 1C C-rate charge
"""
sols1 =[]
for model in models:
    parameter_values["Current function [A]"] = -5
    sim1 = pybamm.Simulation(model, parameter_values=parameter_values)
    sol1 = sim1.solve([0, 3600])
    sols1.append(sol1)
pybamm.dynamic_plot(sols1)

"""
[2] Solving SPM and MPM (chemomechanical model): for C/5, 1C and 2C C-rates charge
"""

sols2 =[]
A = np.array([5/5, 5, 2*5]);
for i in A:
    for model in models:
        parameter_values["Current function [A]"] = -i
        sim = pybamm.Simulation(model, parameter_values=parameter_values)
        sol2 = sim.solve([0, 72000])
        sols2.append(sol2)
        output_variables1 = ["Current [A]"]
        output_variables2 = ["Terminal voltage [V]"]
##        pybamm.dynamic_plot(sols,output_variables=output_variables1)
##        pybamm.dynamic_plot(sols,output_variables=output_variables2)
##        pybamm.dynamic_plot(sols)
output_variables2 = ["Terminal voltage [V]", "Current [A]"]
pybamm.dynamic_plot(sols2,output_variables=output_variables2, labels=["SPM C/5 c-rate", "Mech-SPM C/5 c-rate","SPM 1C c-rate", "Mech-SPM 1C c-rate","SPM 2C", "Mech-SPM 2C"])

"""
[3] SPM and chemomechanical model: Charge for half an hour with 1C C-rate and then rest for half an hour cahrge

"""

tend = 3600 # [s]
t_cutoff = tend / 2  # [s]
t_rest = t_cutoff + 1  # [s]

t_eval = np.arange(0,tend,1)
I_typ = parameter_values["Typical current [A]"]  # current for 1C
def current(t):
    c_rate = 1;
    return - I_typ * c_rate * pybamm.EqualHeaviside(t, t_cutoff) 

parameter_values["Current function [A]"] = current
sols3=[]
for model in models:
    sim3 = pybamm.Simulation(model, parameter_values=parameter_values)
    sol3 = sim3.solve([0, 3600])
    sols3.append(sol3)
pybamm.dynamic_plot(sols3)
 




# experiment = pybamm.Experiment(
#     [
#         ("Discharge at C/10 for 10 hours or until 3.3 V",
#         "Rest for 1 hour",
#         "Charge at 1 A until 4.1 V",
#         "Hold at 4.1 V until 50 mA",
#         "Rest for 1 hour"),
#     ] * 10
# )


#
t_cutoff = 1200  # [s]
t_rest = 1201  # [s]
I_typ = parameter_values["Typical current [A]"]  # current for 1C
	
def current(t):
    return I_typ * 2 * pybamm.EqualHeaviside(t, t_cutoff)
 

sols = []
for model in models:
    parameter_values["Current function [A]"] = current
    sim = pybamm.Simulation(model, parameter_values=parameter_values )
    sol = sim.solve([0, 3600])
    sols.append(sol)

pybamm.dynamic_plot(sols)


t_cutoff = 2400  # [s]
t_rest = 2402  # [s]
I_typ = parameter_values["Typical current [A]"]  # current for 1C
	
def current(t):
    return I_typ/2* pybamm.EqualHeaviside(t, t_cutoff)
 

sols = []
for model in models:
    parameter_values["Current function [A]"] = current
    sim = pybamm.Simulation(model, parameter_values=parameter_values )
    sol = sim.solve([0, 7200])
    sols.append(sol)

pybamm.dynamic_plot(sols)





# A = np.array([5/5, 5,2*5,]);

# for i in A:
#     for model in models:
#         parameter_values["Current function [A]"] = i
#         sim = pybamm.Simulation(model, parameter_values=parameter_values)
#         sol = sim.solve([0, 72000])
#         sols.append(sol)
#         output_variables1 = ["Current [A]"]
#         output_variables2 = ["Terminal voltage [V]"]
# ##        pybamm.dynamic_plot(sols,output_variables=output_variables1)
# ##        pybamm.dynamic_plot(sols,output_variables=output_variables2)
# ##        pybamm.dynamic_plot(sols)
# output_variables2 = ["Terminal voltage [V]", "Current [A]"]

# pybamm.dynamic_plot(sols,output_variables=output_variables2, labels=["SPM C/5 c-rate", "Mech-SPM C/5 c-rtae","SPM 1C c-rate", "Mech-SPM 1C c-rate","SPM 2C", "Mech-SPM 2C"])




# def my_current(t):
#     return pybamm.sin(2 * np.pi * t / 60)

# # def my_current(t):
# #     return 10 if t < 1200 else 0



# parameter_values["Current function [A]"] = my_current

# for model in models:
#     parameter_values["Current function [A]"] = my_current
#     sim = pybamm.Simulation(model, parameter_values=parameter_values)
#     sol = sim.solve([0, 1800])
#     sols2.append(sol)
#     pybamm.dynamic_plot(sols2)


# fig, ax = plt.subplots()
# solutions = [sim.solution, new_sim.solution]
# for sol in solutions:
#     dcap = sol['Discharge Capacity [A.h]'].data
#     V = sol['Terminal Voltage [V]'].data
#     ax.plot(dcap, V)









    
##        sim.plot(["Terminal voltage [V]"])
##  
