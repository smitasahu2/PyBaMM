import pybamm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
from numpy import savetxt
# pybamm.set_logging_level("INFO")
import time as ttt  # Renamed "time" to "t" to avoid conflicts


import matplotlib.pyplot as plt
import pybamm

def myplot(sol_SEI):
    Qt = sol_SEI["Throughput capacity [A.h]"].entries
    Q_SEI = sol_SEI["Loss of capacity to SEI [A.h]"].entries
    Q_SEI_cr = sol_SEI["Loss of capacity to SEI on cracks [A.h]"].entries
    Q_plating = sol_SEI["Loss of capacity to lithium plating [A.h]"].entries
    Q_side = sol_SEI["Total capacity lost to side reactions [A.h]"].entries
    Q_LLI = sol_SEI["Total lithium lost [mol]"].entries * 96485.3 / 3600  # convert from mol to A.h
    LAM_neg = sol_SEI["Loss of active material in negative electrode [%]"].entries
    LAM_pos = sol_SEI["Loss of active material in positive electrode [%]"].entries
    eps_neg_avg = sol_SEI["X-averaged negative electrode porosity"].entries
    eps_neg_sep = sol_SEI["Negative electrode porosity"].entries[-1,:]
    eps_neg_CC = sol_SEI["Negative electrode porosity"].entries[0,:]
    L_SEI = sol_SEI["Total SEI thickness [m]"].entries[-1,:]
    dead = sol_SEI["Dead lithium concentration [mol.m-3]"].entries[-1,:]
    C_Li = sol_SEI["Lithium plating concentration [mol.m-3]"].entries[-1,:]

    plt.figure(figsize=(12, 6))

    # Plot capacity losses
    plt.subplot(2, 2, 1)
    plt.plot(Qt, Q_SEI, label="SEI", linestyle="dashed")
    plt.plot(Qt, Q_SEI_cr, label="SEI on cracks", linestyle="dashdot")
    plt.plot(Qt, Q_plating, label="Li plating", linestyle="dotted")
    plt.plot(Qt, Q_side, label="All side reactions", linestyle=(0, (6, 1)))
    plt.xlabel("Throughput capacity [A.h]")
    plt.ylabel("Capacity [A.h]")
    plt.legend()

    # Plot degradation modes
    plt.subplot(2, 2, 2)
    plt.plot(Qt, Q_LLI, label="LLI")
    plt.plot(Qt, LAM_neg, label="LAM (negative)")
    plt.plot(Qt, LAM_pos, label="LAM (positive)")
    plt.xlabel("Throughput capacity [A.h]")
    plt.ylabel("Degradation modes [%]")
    plt.legend()

    # Plot porosity
    plt.subplot(2, 2, 3)
    plt.plot(Qt, eps_neg_avg, label="Average")
    plt.plot(Qt, eps_neg_sep, label="Separator", linestyle="dotted")
    plt.plot(Qt, eps_neg_CC, label="Current collector", linestyle="dashed")
    plt.xlabel("Throughput capacity [A.h]")
    plt.ylabel("Negative electrode porosity")
    plt.legend()

    # Plot 4: Voltage vs. Throughput Capacity (if needed)
    plt.subplot(2, 2, 4)
    time = sol_SEI["Time [min]"].entries
    voltage = sol_SEI["Terminal voltage [V]"].entries
    plt.plot(time, voltage, label="1 Cycle")
    plt.xlabel("Time [h]")
    plt.ylabel("Total Voltage")
    plt.legend()
    plt.tight_layout()
    plt.show()
    # Wait for 5 seconds before closing the plot
    
    # Plot SEI thickness and concentration
    plt.figure(figsize=(12,6))

    plt.subplot(2, 2, 1)
    plt.plot(Qt, L_SEI, label="SEI thickness")
    plt.xlabel("Throughput capacity [A.h]")
    plt.ylabel("SEI thickness [m]]")
    plt.legend()

    plt.subplot(2, 2, 2)
    plt.plot(Qt, C_Li, label="Plated Li concentration")
    plt.xlabel("Throughput capacity [A.h]")
    plt.ylabel("Total concentration of plated lithiim [mol m^3]")
    plt.legend()

    plt.subplot(2, 2, 3)
    plt.plot(Qt, dead, label="Dead lithium concentration")
    plt.xlabel("Throughput capacity [A.h]")
    plt.ylabel("Total concentration of dead lithiim [mol m^3]")
    plt.legend()

    plt.tight_layout()
    plt.show()


    # pybamm.dynamic_plot(sol_SEI)
