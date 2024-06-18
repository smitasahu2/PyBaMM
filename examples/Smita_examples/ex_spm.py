import pybamm
import numpy as np
import matplotlib.pyplot as plt

"""
jn = I/(an dn F A ) 
"""
model = pybamm.BaseModel()

def current(t):
    return pybamm.tanh(t)

F = pybamm.constants.F
D_n = pybamm.Parameter(f" negative diffusivity [m2.s-1]")
D_p = pybamm.Parameter(f" positive diffusivity [m2.s-1]")
R_n = pybamm.Parameter(f" negative particle radius [m]")
R_p = pybamm.Parameter(f" positive particle radius [m]")
c0_n = pybamm.Parameter(f"Initial concentration in negative electrode [mol.m-3]") 
c0_p = pybamm.Parameter(f"Initial concentration in positive electrode [mol.m-3]") 

A = pybamm.Parameter("Electrode width [m]") * pybamm.Parameter("Electrode height [m]")  # PyBaMM takes the width and height of the electrodes (assumed rectangular) rather than the total area
epsilon_n = pybamm.Parameter(f"negative electrode active material volume fraction") 
epsilon_p = pybamm.Parameter(f"positive electrode active material volume fraction") 

bet_a = 3* epsilon_n/R_n
bet_c = 3* epsilon_p/R_p


param = pybamm.ParameterValues(
    {
        "Current function [A]": current

    }
)

# Domain
c_n = pybamm.Variable("Negative particle concentration [mol.m-3]", domain="negative particle")
c_p = pybamm.Variable("Positive particle concentration [mol.m-3]", domain="positive particle")


"""

# anode
N = -pybamm.grad(c_n)  
dcdt = -pybamm.div(N)
model.rhs = {c_n: dcdt}  
# cathode
N = -pybamm.grad(c_p)  
dcdt = -pybamm.div(N)  
model.rhs = {c_p: dcdt}  

#model.initial_conditions = {cp: pybamm.Scalar(1)}

#BC
lbc = pybamm.Scalar(0)
rbc = pybamm.Scalar(2)

model.boundary_conditions ={c_n: {"left": (lbc, "Neumann"), "right": (rbc, "Neumann")}}
model.boundary_conditions ={c_p: {"left": (lbc, "Neumann"), "right": (rbc, "Neumann")}}

model.variables= {"Concentration": c_n, "Flux": N}


r = pybamm.SpatialVariable(
    "r", domain = ['negative particle'], coord_sys="spherical polar"
)

geometry = {"negative particle": {r: {"min": pybamm.Scalar(0), "max": pybamm.Scalar(1)}}}

submesh_types = {"negative particle": pybamm.Uniform1DSubMesh}
var_pts = {r: 30}
mesh = pybamm.Mesh(geometry, submesh_types, var_pts)

# numerical method
NM = {"negative particle": pybamm.FiniteVolume()}
disc = pybamm.Discretisation(mesh, NM)
disc.process_model(model)


solver = pybamm.ScipySolver()
t = np.linspace(0,1,100)
solution = solver.solve(model,t)
c = solution["Concentration"]



# plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 4))

ax1.plot(solution.t, c(solution.t, r=1))
ax1.set_xlabel("t")
ax1.set_ylabel("Surface concentration")
r = np.linspace(0, 1, 100)
ax2.plot(r, c(t=0.5, r=r))
ax2.set_xlabel("r")
ax2.set_ylabel("Concentration at t=0.5")
plt.tight_layout()
plt.show()
"""