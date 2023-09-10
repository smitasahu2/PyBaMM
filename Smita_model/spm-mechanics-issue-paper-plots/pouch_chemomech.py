#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 23:42:58 2023

@author: smita
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 11:54:03 2023

@author: smita
"""
import pybamm
from models import MSPM
from pouch_parameters import get_parameter_values
import matplotlib.pyplot as plt
import sys
import pickle
import matplotlib
import numpy as np
parameter_values = pybamm.ParameterValues(get_parameter_values())

t_cutoff = 1200  # [s]
t_rest = 1201  # [s]
I_typ = parameter_values["Typical current [A]"]  # current for 1C
	
def current(t):
    return I_typ * 2 * pybamm.EqualHeaviside(t, t_cutoff)

parameter_values["Current function [A]"] = current

#
options = {
              "cell geometry": "pouch",
               "particle": "uniform profile",
               "intercalation kinetics": "linear",
              "current collector": "potential pair",
              "dimensionality": 2
            }





options={
            "particle": "uniform profile",
            "current collector": "potential pair",
            "dimensionality": 2,
        }

parameter_values = pybamm.ParameterValues(get_parameter_values())

parameter_values["Current function [A]"] = current

Chemomechanical_model = MSPM(options=options)
sim = pybamm.Simulation(Chemomechanical_model, parameter_values=parameter_values )
sol1 = sim.solve(t_eval=[0, 3600])
plt.figure()
I_cc = sim.solution['Current collector current density [A.m-2]'].entries
plt.imshow(I_cc[:, :, -1])
plt.title("Current collector current density [A.m-2] in Chemomechanical_model) 2C-crate")
plt.show()


output_variables = [
    "Current [A]",
    "Terminal voltage [V]",
    "Negative current collector potential [V]",
    "Positive current collector potential [V]",            
    "Current collector current density [A.m-2]",
]
pybamm.dynamic_plot(sol1, output_variables)
plt.title("I(t), V(t), - CC potential and + CC potential Chemomechenical 2C c-rate")




t_cutoff = 1200 *5 # [s]
t_rest = 1201*5  # [s]

def currentlow(t):
    return I_typ/5 * pybamm.EqualHeaviside(t, t_cutoff)





options={
            "particle": "uniform profile",
            "current collector": "potential pair",
            "dimensionality": 2,
        }

parameter_values = pybamm.ParameterValues(get_parameter_values())

parameter_values["Current function [A]"] = currentlow

Chemomechanical_model = MSPM(options=options)
sim = pybamm.Simulation(Chemomechanical_model, parameter_values=parameter_values )
sol1 = sim.solve(t_eval=[0, 3600*5])
plt.figure()
I_cc = sim.solution['Current collector current density [A.m-2]'].entries
plt.imshow(I_cc[:, :, -1])

plt.title("Current collector current density [A.m-2] in C(hemomechanical_model) C/5 c-rate")
plt.show()

output_variables = [
    "Current [A]",
    "Terminal voltage [V]",
    "Negative current collector potential [V]",
    "Positive current collector potential [V]",            
    "Current collector current density [A.m-2]",
]
pybamm.dynamic_plot(sol1, output_variables)
plt.title("I(t), V(t), - CC potential and + CC potential Chemomechenical C/5 c-rate")
np.savetxt("chemoc5.csv", I_cc[:, :, -1], delimiter=",")



I = sim.solution['Current [A]'].entries
V = sim.solution['Terminal voltage [V]'].entries
CCn = sim.solution['Negative current collector potential [V]'].entries
CCp= sim.solution['Positive current collector potential [V]'].entries
CCI = sim.solution['Current collector current density [A.m-2]'].entries

np.savetxt("I.csv", I, delimiter=",")
np.savetxt("V.csv", V, delimiter=",")
##np.savetxt("CCn.csv", CCn, delimiter=",")
##np.savetxt("CCp.csv", CCp, delimiter=",")
np.savetxt("CCI.csv", CCI, delimiter=",")


# models = [
#     pybamm.lithium_ion.SPM(
#         options={
#             "particle": "uniform profile",
#             "intercalation kinetics": "linear",
#             "current collector": "potential pair",
#             "dimensionality": 2,
#         }
#     ),
#     MSPM(
#         options={
#             "particle": "uniform profile",
#             "current collector": "potential pair",
#             "dimensionality": 2,
#         }
#     ),
# ]


# sols = []
# for model in models:
#     sim = pybamm.Simulation(model, parameter_values=parameter_values)
#     sol = sim.solve([0, 3600])
#     sols.append(sol)


# output_variables = [
#     "Terminal voltage [V]",
# ]
# pybamm.dynamic_plot(sols, output_variables)
