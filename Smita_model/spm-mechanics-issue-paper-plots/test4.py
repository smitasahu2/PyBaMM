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

sols = []
sols2 =[]
A = np.array([5/5, 5,2*5,]);

for i in A:
    for model in models:
        parameter_values["Current function [A]"] = i
        sim = pybamm.Simulation(model, parameter_values=parameter_values)
        sol = sim.solve([0, 72000])
        sols.append(sol)
        output_variables1 = ["Current [A]"]
        output_variables2 = ["Terminal voltage [V]"]
##        pybamm.dynamic_plot(sols,output_variables=output_variables1)
##        pybamm.dynamic_plot(sols,output_variables=output_variables2)
##        pybamm.dynamic_plot(sols)
output_variables2 = ["Terminal voltage [V]", "Current [A]"]

pybamm.dynamic_plot(sols,output_variables=output_variables2, labels=["SPM C/5 c-rate", "Mech-SPM C/5 c-rtae","SPM 1C c-rate", "Mech-SPM 1C c-rate","SPM 2C", "Mech-SPM 2C"])




def my_current(t):
    return pybamm.sin(2 * np.pi * t / 60)

parameter_values["Current function [A]"] = my_current

for model in models:
    parameter_values["Current function [A]"] = my_current
    sim = pybamm.Simulation(model, parameter_values=parameter_values)
    sol = sim.solve([0, 3600])
    sols2.append(sol)
    pybamm.dynamic_plot(sols)
    
##        sim.plot(["Terminal voltage [V]"])
##  



##        sim.plot(["Terminal voltage [V]"])
##        plot = pybamm.QuickPlot(sols, labels=["model 1", "model 2","model 1", "model 2","model 1", "model 2"])
##plot = pybamm.QuickPlot(sols, labels=["SPM C/2", "Mech-SPM C/2","SPM 1C", "Mech-SPM 1C","SPM 2C", "Mech-SPM 2C","SPM 4C", "Mech-SPM 4C"])

##plot.dynamic_plot()


# create the models you want to plot
# solve the models
##for model in models:
##    parameter_values["Current function [A]"] = 5
##
##    sim = pybamm.Simulation(model, parameter_values=parameter_values)
##    sol = sim.solve([0, 3600])
##    sols2.append(sol)
##    pybamm.dynamic_plot(sols)
##    
####        sim.plot(["Terminal voltage [V]"])
####    
##
####plot = pybamm.QuickPlot(sols2, labels=["model 1", "model 2"])
####sim.plot([["Electrode current density", "Electrolyte current density"], "Terminal voltage [V]"])
### plot the solutions
####plot.dynamic_plot()
##output_variables = ["Terminal voltage [V]","Current [A]"]
##sim.plot(output_variables=output_variables)
##plot = pybamm.QuickPlot(sols2, labels=["model 1", "model 2"],)
##plot.dynamic_plot(output_variables=output_variables)

##sim.plot(output_variables=output_variables)
