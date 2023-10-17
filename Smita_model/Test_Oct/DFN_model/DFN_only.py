# Example showing how to load and solve the DFN
import pybamm
import numpy as np
pybamm.set_logging_level("INFO")

#source .nox/dev/bin/activate
"""""
test1 = 1  # param["Current function [A]"] = 5/4, C/4 c-rate
test2 = 2  # param["Current function [A]"] = 5/2, C/2 c-rate
test3 = 3  # param["Current function [A]"] = 5, pybamm's default value 1C rate
test4 = 4  # param["Current function [A]"] = 1.5*5, 1.5C c-rate
test4 = 5  # param["Current fsource env/bin/activatenction [A]"] = 2*5, 2C c-rate
"""""
params = pybamm.ParameterValues("OKane2022")
model_DFN = pybamm.lithium_ion.DFN()
var_pts = {
    "x_n": 20,  # negative electrode
    "x_s": 15,  # separator 
    "x_p": 20,  # positive electrode
    "r_n": 20,  # negative particle
    "r_p": 20,  # positive particle
 }
testall =[5]# [1, 2, 3, 4, 5]

for test in testall:
    if test == 1:
        standard_protocol = pybamm.Experiment(
        ["Discharge at 0.25C for 240 minutes",
        "Charge at 0.25C for 240 minutes",
        ]#*5  # final capacity check
         )      
        

        # params["Current function [A]"] = 5/4
        print("Current function 5/4 [A]: C/4 c-rate")
        t_eval = np.linspace(0, 3600*8, 10000)
        sim_DFN = pybamm.Simulation(model_DFN, parameter_values=params, var_pts=var_pts, experiment=standard_protocol)
        sol_DFN = sim_DFN.solve(t_eval)
        plot = pybamm.QuickPlot(sol_DFN)
        sol_DFN.save_data("DFN_25C.csv",["Time [s]", "Current [A]", 
                    "Voltage [V]",], to_format="csv")
        #plot.dynamic_plot()
    elif test == 2:
        print("Current function 5/2 [A]: C/2 c-rate")

        standard_protocol = pybamm.Experiment(
        ["Discharge at 0.5C for 120 minutes",
        "Charge at 0.5C for 120 minutes",
        ]#*5  # final capacity check,
         )      
        t_eval = np.linspace(0, 3600*4, 10000)
        sim_DFN = pybamm.Simulation(model_DFN, parameter_values=params, var_pts=var_pts, experiment=standard_protocol)
        sol_DFN = sim_DFN.solve(t_eval)
        plot = pybamm.QuickPlot(sol_DFN)
        sol_DFN.save_data("DFN_5C.csv",["Time [s]", "Current [A]", 
                    "Voltage [V]",], to_format="csv")
        #plot.dynamic_plot() 
    if test == 3:
        print("Current function 5 [A]: 1C c-rate")
        standard_protocol = pybamm.Experiment(
        ["Discharge at 1C for 60 minutes",
        "Charge at 1C for 60 minutes",
        ]#*5  # final capacity check
         )      
        t_eval = np.linspace(0, 3600*2, 10000)
        sim_DFN = pybamm.Simulation(model_DFN, parameter_values=params, var_pts=var_pts, experiment=standard_protocol)
        sol_DFN = sim_DFN.solve(t_eval)
        plot = pybamm.QuickPlot(sol_DFN)
        sol_DFN.save_data("DFN_1C.csv",["Time [s]", "Current [A]", 
                    "Voltage [V]",], to_format="csv")
        #plot.dynamic_plot()
    if test == 4:
        print("Current function 5*1.5 [A]: 1.5C c-rate")
        standard_protocol = pybamm.Experiment(
        ["Discharge at 1.5C for 40 minutes",
        "Charge at 1.5C for 40 minutes",
        ]#*5  # final capacity check
         )      
        t_eval = np.linspace(0, 3600*2/1.5, 10000)
        sim_DFN = pybamm.Simulation(model_DFN, parameter_values=params, var_pts=var_pts, experiment=standard_protocol)
        sol_DFN = sim_DFN.solve(t_eval)
        plot = pybamm.QuickPlot(sol_DFN)
        sol_DFN.save_data("DFN_15C.csv",["Time [s]", "Current [A]", 
                    "Voltage [V]",], to_format="csv")
        plot.dynamic_plot()
    if test == 5:
        print("Current function 5*2 [A]: 2C c-rate")
        standard_protocol = pybamm.Experiment(
        ["Discharge at 2C for 28.5 minutes",
        "Charge at 2C for 28.5 minutes",
        ]#*5  # final capacity check
         )
        t_eval = np.linspace(0, 7200, 10000)
        sim_DFN = pybamm.Simulation(model_DFN, parameter_values=params, var_pts=var_pts, experiment=standard_protocol)
        sol_DFN = sim_DFN.solve(t_eval)
        plot = pybamm.QuickPlot(sol_DFN)
        sol_DFN.save_data("DFN_2C.csv",["Time [s]", "Current [A]", 
                    "Voltage [V]",], to_format="csv")
        plot.dynamic_plot()               
#

  