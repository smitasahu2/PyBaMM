import pybamm
import matplotlib.pyplot as plt
import numpy as np
import pandas as p
import bpx
import timeit
from parameters_albertus import get_parameter_values
# pybamm.set_logging_level("INFO")     # debug mode 


model = pybamm.lithium_ion.DFN({"working electrode": "positive"})
# model = pybamm.lithium_ion.DFN()
# params = pybamm.ParameterValues("Ecker2015")
# params = pybamm.ParameterValues.create_from_bpx('NMC.json')

params = pybamm.ParameterValues("Xu2019")
# exp= pybamm.Experiment(
#     ["Discharge at C/25 until 3.5 V", "Charge at C/25 until 4.2 V"]
# )
sim1 = pybamm.Simulation(model, parameter_values=params)
tend = 3600
t_eval = np.linspace(0, tend, 100)
sol1 = sim1.solve(t_eval = t_eval)

t = sol1["Time [s]"].entries
V = sol1["Voltage [V]"].entries
plt.figure()
plt.plot(t, V)
plt.xlabel("Time [s]")
plt.ylabel("Voltage [V]")
plt.grid()
plt.show()


# Here I am running a basic simple single particel model for 
# half-cell for albertus's parameters
# param = pybamm.ParameterValues(values=get_parameter_values())

# params = pybamm.ParameterValues("Chen2020") 

# model1 = pybamm.lithium_ion.DFN({"working electrode": "positive"})
# # parameter_values = pybamm.ParameterValues(values = get_parameter_values)
# tend = 3600
# t_eval = np.linspace(0, tend, 100)
# sim1 = pybamm.Simulation(model1, parameter_values=params)
# sol1 = sim1.solve(t_eval = t_eval)
# pybamm.dynamic_plot(sol1)










# model1 = pybamm.lithium_ion.SPM(
#     {"working electrode": "positive"
#     })
# # parameter_values = pybamm.ParameterValues(values = get_parameter_values)
# tend = 3600
# t_eval = np.linspace(0, tend, 100)
# sim1 = pybamm.Simulation(model1)#, parameter_values=parameter_values)
# sol1 = sim1.solve(t_eval = t_eval)
# pybamm.dynamic_plot(sol1)


# param.process_model(model1)
# param.process_geometry(geometry=)



# """
#     "working electrode": "positive", this phrase makes cell to be half-cell which is positive electode here
# """
# # tic = timeit.default_timer()
# model = pybamm.lithium_ion.SPM(
#     {
#         "working electrode": "positive",
#     }
# )


# model_spm = pybamm.lithiu_ion.SPM()
# variable  = list(model.rhs.keys())[1]
# euqation  = list(model.rhs.values())[1]
# print('RHS equation for variable \'', variable, '\' is:')
# path = example
