import pybamm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
from numpy import savetxt
# pybamm.set_logging_level("INFO")
import pybamm
import numpy as np
import matplotlib.pyplot as plt

def myplot(sol_SEI):
    plt.figure(figsize=(12, 6))

    # Plot 1: Capacity vs. Throughput Capacity
    plt.subplot(2, 2, 1)
    Qt = sol_SEI["Throughput capacity [A.h]"].entries
    Q_SEI = sol_SEI["Loss of capacity to SEI [A.h]"].entries
    Q_plating = sol_SEI["Loss of capacity to lithium plating [A.h]"].entries
    Q_side = sol_SEI["Total capacity lost to side reactions [A.h]"].entries
    Q_LLI = sol_SEI["Total lithium lost [mol]"].entries * 96485.3 / 3600
    plt.plot(Qt, Q_SEI, label="SEI", linestyle="dashed")
    plt.plot(Qt, Q_plating, label="Li plating", linestyle="dotted")
    plt.plot(Qt, Q_side, label="All side reactions", linestyle="dashdot")
    plt.xlabel("Throughput capacity [A.h]")
    plt.ylabel("Capacity [A.h]")
    plt.legend()

    # Plot 2: Porosity vs. Throughput Capacity
    plt.subplot(2, 2, 2)
    eps_neg_avg = sol_SEI["X-averaged negative electrode porosity"].entries
    eps_neg_sep = sol_SEI["Negative electrode porosity"].entries[-1, :]
    eps_neg_CC = sol_SEI["Negative electrode porosity"].entries[0, :]
    plt.plot(Qt, eps_neg_avg, label="Average")
    plt.plot(Qt, eps_neg_sep, label="Separator", linestyle="dotted")
    plt.plot(Qt, eps_neg_CC, label="Current collector", linestyle="dashed")
    plt.xlabel("Throughput capacity [A.h]")
    plt.ylabel("Negative electrode porosity")
    plt.legend()

    # Plot 3: SEI Thickness vs. Throughput Capacity
    plt.subplot(2, 2, 3)
    L_SEI = sol_SEI["Total SEI thickness [m]"].entries[-1, :]
    plt.plot(Qt, L_SEI)
    plt.xlabel("Throughput capacity [A.h]")
    plt.ylabel("SEI thickness")

    # Plot 4: LAM vs. Throughput Capacity (if needed)
    plt.subplot(2, 2, 4)
    time = sol_SEI["Time [min]"].entries
    voltage = sol_SEI["Terminal voltage [V]"].entries
    plt.plot(time, voltage, label="1 Cycle")
    plt.xlabel("Time [h]")
    plt.ylabel("Total Voltage")
    plt.legend()
    plt.tight_layout()
    plt.show()


    # Plot 4: LAM vs. Throughput Capacity (if needed)
    # LAM_neg = sol_SEI["Loss of active material in negative electrode [%]"].entries
    # LAM_pos = sol_SEI["Loss of active material in positive electrode [%]"].entries
    # plt.subplot(2, 2, 4)
    # plt.plot(Qt, LAM_neg, label="LAM (negative)")
    # plt.plot(Qt, LAM_pos, label="LAM (positive)")
    # plt.xlabel("Throughput capacity [A.h]")
    # plt.ylabel("Degradation modes [%]")
    # plt.legend()

# SEI_test1 =1
# if SEI_test1 == 1:
#     run_SEI_test(SEI_test1, 2.5e-21)
# elif SEI_test1 == 2:
#     run_SEI_test(SEI_test1, 7.5e-21)
# elif SEI_test1 == 3:
#     run_SEI_test(SEI_test1, 1.25e-20)
# else:
#     run_SEI_test(SEI_test1, 2.5e-22)
