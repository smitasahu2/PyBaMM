import pybamm
import numpy as np
import os
import matplotlib.pyplot as plt
os.chdir(pybamm.__path__[0] + "/..")


model = pybamm.lithium_ion.SPM()
variable = list(model.rhs.keys())[1]
equation = list(model.rhs.values())[1]
print("rhs equation for variable '", variable, "' is:")
print("rhs equation for variable '", equation, "' is:")
#model.rhs[equation].visualise("a.png")
geometry = model.default_geometry

print("SPM domains:")
for i, (k, v) in enumerate(geometry.items()):
    print(str(i + 1) + ".", k, "with variables:")
    for var, rng in v.items():
        if "min" in rng:
            print("  -(", rng["min"], ") <=", var, "<= (", rng["max"], ")")
        else:
            print(var, "=", rng["position"])

param = model.default_parameter_values
param.process_model(model)
param.process_geometry(geometry)
for k, t in model.default_submesh_types.items():
    print(k, "is of type", t.__name__)
for var, npts in model.default_var_pts.items():
    print(var, "has", npts, "mesh points")

mesh = pybamm.Mesh(geometry, model.default_submesh_types, model.default_var_pts)  
for k, method in model.default_spatial_methods.items():
    print(k, "is discretised using", method.__class__.__name__, "method")  

path = "examples/smita_examples/"

disc = pybamm.Discretisation(mesh, model.default_spatial_methods)
disc.process_model(model)
# model.concatenated_rhs.children[1].visualise("image.png")

model.concatenated_rhs.children[1].visualise( "a.png")


# Solve the model at the given time points (in seconds)
solver = model.default_solver
n = 250
t_eval = np.linspace(0, 3600, n)
print("Solving using", type(solver).__name__, "solver...")
solution = solver.solve(model, t_eval)
print("Finished.")



print("SPM model variables:")
for v in model.variables.keys():
    print("\t-", v)



voltage = solution["Voltage [V]"]
c_s_n_surf = solution["Negative particle surface concentration"]
c_s_p_surf = solution["Positive particle surface concentration"] 


t = solution["Time [s]"].entries
x = solution["x [m]"].entries[:, 0]
f, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(13, 4))

ax1.plot(t, voltage(t))
ax1.set_xlabel(r"$Time [s]$")
ax1.set_ylabel("Voltage [V]")

ax2.plot(
    t, c_s_n_surf(t=t, x=x[0])
)  # can evaluate at arbitrary x (single representative particle)
ax2.set_xlabel(r"$Time [s]$")
ax2.set_ylabel("Negative particle surface concentration")

ax3.plot(
    t, c_s_p_surf(t=t, x=x[-1])
)  # can evaluate at arbitrary x (single representative particle)
ax3.set_xlabel(r"$Time [s]$")
ax3.set_ylabel("Positive particle surface concentration")

plt.tight_layout()
plt.show()


c_s_n = solution["Negative particle concentration"]
c_s_p = solution["Positive particle concentration"]
r_n = solution["r_n [m]"].entries[:, 0]
r_p = solution["r_p [m]"].entries[:, 0]



c_s_n = solution["Negative particle concentration"]
c_s_p = solution["Positive particle concentration"]
r_n = solution["r_n [m]"].entries[:, 0, 0]
r_p = solution["r_p [m]"].entries[:, 0, 0]


def plot_concentrations(t):
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    (plot_c_n,) = ax1.plot(
        r_n, c_s_n(r=r_n, t=t, x=x[0])
    )  # can evaluate at arbitrary x (single representative particle)
    (plot_c_p,) = ax2.plot(
        r_p, c_s_p(r=r_p, t=t, x=x[-1])
    )  # can evaluate at arbitrary x (single representative particle)
    ax1.set_ylabel("Negative particle concentration")
    ax2.set_ylabel("Positive particle concentration")
    ax1.set_xlabel(r"$r_n$ [m]")
    ax2.set_xlabel(r"$r_p$ [m]")
    ax1.set_ylim(0, 1)
    ax2.set_ylim(0, 1)
    plt.show()


import ipywidgets as widgets

widgets.interact(
    plot_concentrations, t=widgets.FloatSlider(min=0, max=3600, step=10, value=0)
);


quick_plot = pybamm.QuickPlot(solution)
quick_plot.dynamic_plot()