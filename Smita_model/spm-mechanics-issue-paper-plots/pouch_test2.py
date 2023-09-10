#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 11:54:03 2023

@author: smita
"""
import pybamm
from models import MSPM
from pouch_parameters2 import get_parameter_values
import matplotlib.pyplot as plt

import numpy as np
parameter_values = pybamm.ParameterValues(get_parameter_values())


"""
# Flat OCP

 Trying to use flat OCP in anode and cathode both. Charging for 900 seconds and then resting.
**Defining all the options and tweaking some parameters such as current**

"""

options_spm={
                "particle": "uniform profile",
                "intercalation kinetics": "linear",
                "current collector": "potential pair",
                "dimensionality": 2,
            }
        
options_mpm={
                "particle": "uniform profile",
                "current collector": "potential pair",
                "dimensionality": 2,
            }

# parameter_values["Current function [A]"] = -1;


output_variables = [
    "Current [A]",
    "Terminal voltage [V]",
    "Negative current collector potential [V]",
    "Positive current collector potential [V]",            
    "Current collector current density [A.m-2]",    
]

parameter_values = pybamm.ParameterValues(get_parameter_values())


t_cutoff = 900  # [s]
t_rest = 901  # [s]
tend = 1800 # [s]
t_eval = np.arange(0,tend,1)

I_typ = parameter_values["Typical current [A]"]  # current for 1C
def current(t):
    c_rate = 1;
    return - I_typ * c_rate * pybamm.EqualHeaviside(t, t_cutoff) 
parameter_values["Current function [A]"] = current



x = pybamm.linspace(0, 1, 1000)  # sto
U_n = parameter_values["Negative electrode OCP [V]"]
U_p = parameter_values["Positive electrode OCP [V]"]

fig, ax = plt.subplots(1, 3, figsize=(12, 4))
ax[0].plot(x.entries, U_n(x).entries)
ax[0].set(xlabel="sto [-]", ylabel="$U_n$ [V]")
ax[1].plot(x.entries, U_p(x).entries)
ax[1].set(xlabel="sto [-]", ylabel="$U_p$ [V]")
ax[2].plot(x.entries, U_p(x).entries - U_n(1-x).entries)
ax[2].set(xlabel="sto [-]", ylabel="$U$ [V]")
plt.tight_layout()


electrochemical_model = pybamm.lithium_ion.SPM(options=options_spm)
sim_spm = pybamm.Simulation(electrochemical_model, parameter_values=parameter_values )
sol_spm = sim_spm.solve(t_eval= t_eval)
# plt.title("I(t), V(t), - CC potential and + CC potential (SPM: Linear BV) 2C-crate")
pybamm.dynamic_plot(sol_spm, output_variables, time_unit="seconds")

CC_density_spm = sol_spm["Current collector current density [A.m-2]"]


CC_density_spm = sol_spm["Current collector current density [A.m-2]"].entries
# cathode_cc_potential = sol_spm["Current collector current density [A.m-2]"].entries
# ce = sol_spm["Current collector current density [A.m-2]"]
CC_density_spm
np.shape(CC_density_spm)

cumulative_arr_spm = np.cumsum(CC_density_spm, axis=2)
np.shape(cumulative_arr_spm)
np.shape(cumulative_arr_spm[:,:,0])
# axes[0,0].imshow(cumulative_arr[:,:,100], cmap='viridis')
# plt.show()

fig, axes = plt.subplots(nrows=2, ncols=2)

fig.set_size_inches(10, 10)

# Define the t-slices you want to plot
t_slices = [0, round(tend/4), round(tend/2), round(tend)]

# Loop over the rows and columns of the axes array
for i in range(2):
    for j in range(2):
        # Calculate the index of the current z-slice
        k = i*2 + j
        
        # Plot the image for the current z-slice
        im = axes[i,j].imshow(cumulative_arr_spm[:,:,t_slices[k]], cmap='viridis')#, vmin=0, vmax=1)
        
        # Set the title of the subplot
        axes[i,j].set_title(f"t = {t_slices[k]}")
        
        # Add a colorbar for the current subplot
        cbar = fig.colorbar(im, ax=axes[i,j])
        
# Show the plot
plt.show()
fig, axes = plt.subplots(nrows=2, ncols=2)

fig.set_size_inches(10, 10)

# Define the t-slices you want to plot
t_slices = [0, round(tend/4), round(tend/2), round(tend)]

# Loop over the rows and columns of the axes array
for i in range(2):
    for j in range(2):
        # Calculate the index of the current z-slice
        k = i*2 + j
        
        # Plot the image for the current z-slice
        im = axes[i,j].imshow(cumulative_arr_spm[:,:,t_slices[k]], cmap='viridis')#, vmin=0, vmax=1)
        
        # Set the title of the subplot
        axes[i,j].set_title(f"t = {t_slices[k]}")
        
        # Add a colorbar for the current subplot
        cbar = fig.colorbar(im, ax=axes[i,j])
        
# Show the plot
plt.show()
"""
** Solving Single particle Chemomechanical model for non-equipotential CCs**
"""

Chemomechanical_model = MSPM(options=options_mpm)
sim_mpm = pybamm.Simulation(Chemomechanical_model, parameter_values=parameter_values )
sol_mpm = sim_mpm.solve(t_eval= t_eval)
# plt.title("I(t), V(t), - CC potential and + CC potential (Chemomechanica) 2C-crate")
pybamm.dynamic_plot(sol_mpm, output_variables, time_unit="seconds")


CC_density_mech = sol_mpm["Current collector current density [A.m-2]"].entries
cumulative_arr_mech = np.cumsum(CC_density_mech, axis=2)
# np.shape(cumulative_arr_mech)
# np.shape(cumulative_arr_mech[:,:,0])
# axes[0,0].imshow(cumulative_arr[:,:,100], cmap='viridis')
# plt.show()


fig, axes = plt.subplots(nrows=2, ncols=2)
fig.set_size_inches(10, 10)

# Define the t-slices you want to plot
t_slices = [0, round(tend/4), round(tend/2), round(tend)]

# Loop over the rows and columns of the axes array
for i in range(2):
    for j in range(2):
        # Calculate the index of the current z-slice
        k = i*2 + j
        
        # Plot the image for the current z-slice
        im = axes[i,j].imshow(cumulative_arr_mech[:,:,t_slices[k]], cmap='viridis')#, vmin=0, vmax=1)
        
        # Set the title of the subplot
        axes[i,j].set_title(f"t = {t_slices[k]}")
        
        # Add a colorbar for the current subplot
        cbar = fig.colorbar(im, ax=axes[i,j])
        
# Show the plot
plt.show()
