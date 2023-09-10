import pybamm
import matplotlib.pyplot as plt
import numpy as np
import pandas as p
import timeit
from parameters_albertus import get_parameter_values
pybamm.set_logging_level("INFO")     # debug mode 


"""
    "working electrode": "positive", this phrase makes cell to be half-cell which is positive electode here
    "particle phases": ("1", "2"), this phrase makes positive electrode to have two active materials
    "particle phases": ("1", "2"), loads the composite/belnded positive electrode particle model by specifying that there are two particle phases (LMO and NCA)
"""
tic = timeit.default_timer()
model = pybamm.lithium_ion.DFN(
    {
        "working electrode": "positive",
        "particle phases": ("1","2"),
        "open circuit potential": ("single", ("single", "current sigmoid"))
    }
)
"""
   Here I am defining all the parameters from Albertus paper
    Primary active material is NCA
    Secondary active material is LMO
"""
param = pybamm.ParameterValues(values=get_parameter_values())

# Plots of OCPs
pts = 1000
x = pybamm.linspace(0, 1, pts)  # sto
U_NCA = param["Primary: Positive electrode OCP [V]"]
U_LMO_L = param["Secondary: Positive electrode lithiation OCP [V]"]
U_LMO_D = param["Secondary: Positive electrode delithiation OCP [V]"]

fig, ax = plt.subplots(1, 3, figsize=(12, 3))
ax[0].plot(x.entries, U_NCA(x).entries)#plot(x.entries, U_Graphite(x).entries)
ax[0].set(xlabel="sto [-]", ylabel="$U_{NCA}$ NCA [V]")
ax[0].grid()
ax[1].plot(x.entries, U_LMO_L(x).entries)
ax[1].set(xlabel="sto [-]", ylabel="$U_{LMO}$ LMO Lithiated [V]")
ax[1].grid()
ax[2].plot(x.entries, U_LMO_D(x).entries)
ax[2].set(xlabel="sto [-]", ylabel="$U_{LMO}$ LMO Delithiated [V]")
ax[2].grid()
plt.show()

"""
    "working electrode": "positive", this phrase makes cell to be half-cell which is positive electode here
    "particle phases": ("1", "2"), this phrase makes positive electrode to have two active materials
    "particle phases": ("1", "2"), loads the composite/belnded positive electrode particle model by specifying that there are two particle phases (LMO and NCA)
"""
tic = timeit.default_timer()
model = pybamm.lithium_ion.DFN(
    {
        "working electrode": "positive",
        "particle phases": ("1","2"),
        "open circuit potential": ("single", ("single", "current sigmoid"))
    }
)

v = 0.5
param = pybamm.ParameterValues(values=get_parameter_values())
total_am_volume_fraction = 0.75
solution=[]
param.update({
        "Primary: Positive electrode active material volume fraction": (1-v) * total_am_volume_fraction, #primary
        "Secondary: Positive electrode active material volume fraction": v * total_am_volume_fraction,
})

sim = pybamm.Simulation( model,
parameter_values=param,
solver=pybamm.CasadiSolver(dt_max = 5))
solution = sim.solve(t_eval = [0, 3600])



# Electrolyte parameters
# Diff_Ele = param["Electrolyte diffusivity [m2.s-1]"]
# Conduct_Ele = param["Electrolyte conductivity [S.m-1]"]
# Diff_cathode  = param["Positive electrode diffusivity [m2.s-1]"]
# fig, ax = plt.subplots(1, 2, figsize=(12, 4))
# ax[0].plot(x.entries, Diff_Ele(x,0).entries)
# ax[0].set(xlabel="sto [-]", ylabel="Electrolyte diffusivity [m2.s-1]")
# ax[1].plot(x.entries, Conduct_Ele(x,0).entries)
# ax[1].set(xlabel="sto [-]", ylabel="Electrolyte conductivity [S.m-1]")
# plt.tight_layout()


# Diff_LMO = param["Secondary: Negative electrode diffusivity [m2.s-1]"]
# Diff_NCA = param["Primary: Negative electrode diffusivity [m2.s-1]"]
# Diff_cathode  = param["Positive electrode diffusivity [m2.s-1]"]
# Temperature = param["Reference temperature [K]"]
# fig, ax = plt.subplots(1, 4, figsize=(12, 4))
# ax[0].plot(x.entries, Diff_LMO(x).entries)
# ax[0].set(xlabel="sto [-]", ylabel="$U_G$ Diffusivity LMO [m2.s-1]")
# ax[1].plot(x.entries, Diff_NCA(x).entries)
# ax[1].set(xlabel="sto [-]", ylabel="$U_S$ Diffusivity NCA [m2.s-1]")
# ax[2].plot(x.entries, Diff_cathode(x).entries)
# ax[2].set(xlabel="sto [-]", ylabel="$U$ Diffusivity cathode")



