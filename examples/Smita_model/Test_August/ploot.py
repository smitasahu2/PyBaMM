import pybamm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
from numpy import savetxt
# pybamm.set_logging_level("INFO")

def myplot(sol_SEI):
    pybamm.dynamic_plot(sol_SEI)
    Qt = sol_SEI["Throughput capacity [A.h]"].entries
    Q_SEI = sol_SEI["Loss of capacity to SEI [A.h]"].entries
    Q_plating = sol_SEI["Loss of capacity to lithium plating [A.h]"].entries
    Q_side = sol_SEI["Total capacity lost to side reactions [A.h]"].entries
    Q_LLI = sol_SEI["Total lithium lost [mol]"].entries * 96485.3 / 3600  # convert from mol to A.h
    
    plt.figure()
    plt.plot(Qt,Q_SEI,label="SEI",linestyle="dashed")
    plt.plot(Qt,Q_plating,label="Li plating",linestyle="dotted")
    plt.plot(Qt,Q_side,label="All side reactions",linestyle="dashdot")
    plt.xlabel("Throughput capacity [A.h]")
    plt.ylabel("Capacity [A.h]")
    plt.legend()
    plt.show()
    

    # LAM_neg = sol_SEI["Loss of active material in negative electrode [%]"].entries
    # LAM_pos = sol_SEI["Loss of active material in positive electrode [%]"].entries
    # plt.figure()
    # #plt.plot(Qt,LLI,label="LLI")
    # plt.plot(Qt,LAM_neg,label="LAM (negative)")
    # plt.plot(Qt,LAM_pos,label="LAM (positive)")
    # plt.xlabel("Throughput capacity [A.h]")
    # plt.ylabel("Degradation modes [%]")
    # plt.legend()
    # plt.show()
    eps_neg_avg = sol_SEI["X-averaged negative electrode porosity"].entries
    eps_neg_sep = sol_SEI["Negative electrode porosity"].entries[-1,:]
    eps_neg_CC = sol_SEI["Negative electrode porosity"].entries[0,:]
    plt.figure()
    plt.plot(Qt,eps_neg_avg,label="Average")
    plt.plot(Qt,eps_neg_sep,label="Separator",linestyle="dotted")
    plt.plot(Qt,eps_neg_CC,label="Current collector",linestyle="dashed")
    plt.xlabel("Throughput capacity [A.h]")
    plt.ylabel("Negative electrode porosity")
    plt.legend()
    plt.show()
    L_SEI=sol_SEI["Total SEI thickness [m]"].entries[-1,:]
    plt.figure()
    #plt.plot(Qt,LLI,label="LLI")
    plt.plot(Qt,L_SEI)
    plt.xlabel("Throughput capacity [A.h]")
    plt.ylabel("SEI thickness")
    plt.show()

def plating_plot(sol_SEI,LSEI,porosity,dead):
    Qt = sol_SEI["Throughput capacity [A.h]"].entries
    Q_SEI = sol_SEI["Loss of capacity to SEI [A.h]"].entries
    Q_SEI_cr = sol_SEI["Loss of capacity to SEI on cracks [A.h]"].entries
    Q_plating = sol_SEI["Loss of capacity to lithium plating [A.h]"].entries
    Q_side = sol_SEI["Total capacity lost to side reactions [A.h]"].entries
    Q_LLI = sol_SEI["Total lithium lost [mol]"].entries * 96485.3 / 3600  # convert from mol to A.h
    plt.figure()
    plt.plot(Qt,Q_SEI,label="SEI",linestyle="dashed")
    plt.plot(Qt,Q_SEI_cr,label="SEI on cracks",linestyle="dashdot")
    plt.plot(Qt,Q_plating,label="Li plating",linestyle="dotted")
    plt.plot(Qt,Q_side,label="All side reactions",linestyle=(0,(6,1)))
    plt.xlabel("Throughput capacity [A.h]")
    plt.ylabel("Capacity [A.h]")
    plt.legend()
    plt.show()
    LAM_neg = sol_SEI["Loss of active material in negative electrode [%]"].entries
    LAM_pos = sol_SEI["Loss of active material in positive electrode [%]"].entries
    plt.figure()
    plt.plot(Qt,Q_LLI,label="LLI")
    plt.plot(Qt,LAM_neg,label="LAM (negative)")
    plt.plot(Qt,LAM_pos,label="LAM (positive)")
    plt.xlabel("Throughput capacity [A.h]")
    plt.ylabel("Degradation modes [%]")
    plt.legend()
    plt.show()

    eps_neg_avg = sol_SEI["X-averaged negative electrode porosity"].entries
    eps_neg_sep = sol_SEI["Negative electrode porosity"].entries[-1,:]
    eps_neg_CC = sol_SEI["Negative electrode porosity"].entries[0,:]
    plt.figure()
    plt.plot(Qt,eps_neg_avg,label="Average")
    plt.plot(Qt,eps_neg_sep,label="Separator",linestyle="dotted")
    plt.plot(Qt,eps_neg_CC,label="Current collector",linestyle="dashed")
    plt.xlabel("Throughput capacity [A.h]")
    plt.ylabel("Negative electrode porosity")
    plt.legend()
    plt.show()

    L_SEI=sol_SEI["Total SEI thickness [m]"].entries[-1,:]
    plt.figure()
    #plt.plot(Qt,LLI,label="LLI")
    plt.plot(Qt,L_SEI)
    plt.xlabel("Throughput capacity [A.h]")
    plt.ylabel("SEI thickness")
    plt.show()

    dead = sol_SEI["Dead lithium concentration [mol.m-3]"].entries[-1,:]
    plt.figure()
    plt.plot(Qt,dead,label="Average")
    plt.xlabel("Throughput capacity [A.h]")
    plt.ylabel("Dead lithium concentration [mol.m-3]")
    plt.legend()
    plt.show()  
    C_Li = sol_SEI["Lithium plating concentration [mol.m-3]"].entries[-1,:]
    plt.figure()
    plt.plot(Qt,C_Li,label="Average")
    plt.xlabel("Throughput capacity [A.h]")
    plt.ylabel("Plated Li concentration [mol.m-3]")
    plt.legend()
    plt.show() 
    # plt.figure()
    # dead = sol_SEI["Dead lithium concentration [mol.m-3]]"].enteries
    # plt.figure()
    # plt.plot(Qt,dead,label="Average")
    # plt.xlabel("Throughput capacity [A.h]")
    # plt.ylabel("Dead lithium concentration [mol.m-3]")
    # plt.legend()
    # plt.show()    
    # plt.figure()
    # dead = sol_SEI["Dead lithium concentration [mol.m-3]]"].enteries
    # plt.figure()
    # plt.plot(Qt,dead,label="Average")
    # plt.xlabel("Throughput capacity [A.h]")
    # plt.ylabel("Dead lithium concentration [mol.m-3]")
    # plt.legend()
    # plt.show()
    pybamm.dynamic_plot(sol_SEI)

