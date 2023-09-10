import pybamm

# creating a basic pybamm model
model = pybamm.lithium_ion.DFN()
simulation = pybamm.Simulation(model)
simulation.solve([0,3600])
#simulation.plot()
# comparing models
models = [
    pybamm.lithium_ion.SPM(),
    pybamm.lithium_ion.SPMe(),
    pybamm.lithium_ion.DFN()
]
simulations = []

for model in models:
    simulation = pybamm.Simulation(model)
    simulation.solve([0,3600])
    simulations.append(simulation)

#pybamm.dynamic_plot(simulations) 

#basic plotting

output_variables = ["Voltage [V]", "Current [A]"]
#simulation.plot(output_variables = output_variables)

# same plot with nestisng list
output_variables = ["Voltage [V]", ["Electrode current density [A.m-2]", "Electrolyte current density [A.m-2]"]]
#simulation.plot(output_variables=output_variables)

#model.variable_names()
#model.variables.search("electrolyte")

# changing the parameters
parameter_values = pybamm.ParameterValues("Chen2020")
simulation = pybamm.Simulation(model, parameter_values = parameter_values)

# Running some experiements

# experiment = [
#     "Discharge at 1C for 0.5 hour",
#     "Rest for 1 hour",
#     "Charge at C/3 untill 4.2 V",
#     ] *3 + ["Charge at 0.5C for 45 minutes"]

model = pybamm.lithium_ion.SPM()

# Exercise 2: Long experiment
long_experiment = [
    "Discharge at 1C for 1 hour",
    "Rest for 1 hour",
    "Charge at 1C until 4.212V",
      ]  *1      
simulation = pybamm.Simulation(model, experiment = long_experiment)
simulation.solve()

simulation.plot()
# Need to check pybamm.plot_summary_variables()#solutions, output_variables=None, labels=None, testing=False, **kwargs_fig)
# bathstudy

dfn = pybamm.lithium_ion.DFN()
spm = pybamm.lithium_ion.SPM()
spme = pybamm.lithium_ion.SPMe()

models = {
    "dfn": dfn,
    "spm": spm,
    "SPMe": spme,
}
#creating batchstudy object
batch_study = pybamm.BatchStudy(models = models)
# solving and ploting the comparison

batch_study.solve(t_eval = [0,3600])
#batch_study.plot()

#passing parameter values as a dictionary
parameter_values = {"Chen2020": pybamm.ParameterValues("Chen2020")}

#creating a Batchstudy objectc and solving the simulation
batch_study = pybamm.BatchStudy(models=models, parameter_values=parameter_values,permutations = True)
batch_study.solve(t_eval=[0,3600])
batch_study.plot()
                  
