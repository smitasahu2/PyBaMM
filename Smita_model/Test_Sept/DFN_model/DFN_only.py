# Example showing how to load and solve the DFN
import pybamm
import numpy as np
pybamm.set_logging_level("INFO")


"""""
test1 = 1  # param["Current function [A]"] = 5/4, C/4 c-rate
test2 = 2  # param["Current function [A]"] = 5/2, C/2 c-rate
test3 = 3  # param["Current function [A]"] = 5, pybamm's default value 1C rate
test4 = 4  # param["Current function [A]"] = 1.5*5, 1.5C c-rate
test4 = 5  # param["Current function [A]"] = 2*5, 2C c-rate
"""""
params = pybamm.ParameterValues("OKane2022")
model_DFN = pybamm.lithium_ion.DFN()
var_pts = {
    "x_n": 30,  # negative electrode
    "x_s": 15,  # separator 
    "x_p": 30,  # positive electrode
    "r_n": 30,  # negative particle
    "r_p": 30,  # positive particle
 }
testall = [1]#, 2, 3, 4, 5]

for test in testall:
    if test == 1:
        params["Current function [A]"] = 5/4
        print("Current function 5/4 [A]: C/4 c-rate")
        t_eval = np.linspace(0, 3600*4, 10000)
        sim_DFN = pybamm.Simulation(model_DFN, parameter_values=params, var_pts=var_pts)
        sol_DFN = sim_DFN.solve(t_eval)
        plot = pybamm.QuickPlot(sol_DFN)
        sol_DFN.save_data("DFN_C_by4.csv",["Time [s]", "Current [A]", 
                    "Voltage [V]",], to_format="csv")
        plot.dynamic_plot()
    elif test == 2:
        params["Current function [A]"] = 5/2
        print("Current function 5/2 [A]: C/2 c-rate")
        t_eval = np.linspace(0, 3600*2, 10000)
        sim_DFN = pybamm.Simulation(model_DFN, parameter_values=params, var_pts=var_pts)
        sol_DFN = sim_DFN.solve(t_eval)
        plot = pybamm.QuickPlot(sol_DFN)
        sol_DFN.save_data("DFN_C_by2.csv",["Time [s]", "Current [A]", 
                    "Voltage [V]",], to_format="csv")
        plot.dynamic_plot() 
    if test == 3:
        params["Current function [A]"] = 5
        print("Current function 5 [A]: 1C c-rate")
        t_eval = np.linspace(0, 3600, 10000)
        sim_DFN = pybamm.Simulation(model_DFN, parameter_values=params, var_pts=var_pts)
        sol_DFN = sim_DFN.solve(t_eval)
        plot = pybamm.QuickPlot(sol_DFN)
        sol_DFN.save_data("DFN_1C.csv",["Time [s]", "Current [A]", 
                    "Voltage [V]",], to_format="csv")
        plot.dynamic_plot()
    if test == 4:
        params["Current function [A]"] = 5*1.5
        print("Current function 5*1.5 [A]: 1.5C c-rate")
        t_eval = np.linspace(0, 3600/1.5, 10000)
        sim_DFN = pybamm.Simulation(model_DFN, parameter_values=params, var_pts=var_pts)
        sol_DFN = sim_DFN.solve(t_eval)
        plot = pybamm.QuickPlot(sol_DFN)
        sol_DFN.save_data("DFN_C_by3by2.csv",["Time [s]", "Current [A]", 
                    "Voltage [V]",], to_format="csv")
        plot.dynamic_plot()
    if test == 5:
        params["Current function [A]"] = 5*2
        print("Current function 5*2 [A]: 2C c-rate")
        t_eval = np.linspace(0, 3600/2, 10000)
        sim_DFN = pybamm.Simulation(model_DFN, parameter_values=params, var_pts=var_pts)
        sol_DFN = sim_DFN.solve(t_eval)
        plot = pybamm.QuickPlot(sol_DFN)
        sol_DFN.save_data("DFN_2C.csv",["Time [s]", "Current [A]", 
                    "Voltage [V]",], to_format="csv")
        plot.dynamic_plot()               


  