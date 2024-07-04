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

electrochemical_model = pybamm.lithium_ion.SPM(options=options)
sim = pybamm.Simulation(electrochemical_model, parameter_values=parameter_values )

sol1 = sim.solve(t_eval=[0, 3600])
plt.figure()
I_cc = sim.solution['Current collector current density [A.m-2]'].entries
plt.imshow(I_cc[:, :, -1])
plt.title("Current collector current density [A.m-2] (SPM: Linear BV)")
plt.show()



output_variables = [
    "Current [A]",
    "Terminal voltage [V]",
    "Negative current collector potential [V]",
    "Positive current collector potential [V]",            
    "Current collector current density [A.m-2]",
]
pybamm.dynamic_plot(sol1, output_variables)
plt.title("I(t), V(t), - CC potential and + CC potential (SPM: Linear BV) 2C-crate")




t_cutoff = 1200 *5 # [s]
t_rest = 1201*5  # [s]

def currentlow(t):
    return I_typ/5 * pybamm.EqualHeaviside(t, t_cutoff)



electrochemical_model = pybamm.lithium_ion.SPM(options=options)
parameter_values["Current function [A]"] = currentlow

sim = pybamm.Simulation(electrochemical_model, parameter_values=parameter_values )

sol1 = sim.solve(t_eval=[0, 3600*5])
plt.figure()
I_cc = sim.solution['Current collector current density [A.m-2]'].entries
plt.imshow(I_cc[:, :, -1])
plt.title("Current collector current density [A.m-2] (SPM: Linear BV)")
plt.show()



output_variables = [
    "Current [A]",
    "Terminal voltage [V]",
    "Negative current collector potential [V]",
    "Positive current collector potential [V]",            
    "Current collector current density [A.m-2]",
]
pybamm.dynamic_plot(sol1, output_variables)
plt.title("I(t), V(t), - CC potential and + CC potential (SPM: Linear BV) C/5 c-rate")


