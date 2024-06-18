import pybamm
import numpy as np
import matplotlib.pyplot as plt

model = pybamm.BaseModel()

c = pybamm.Variable("Concentration", domain="negative particle")
N = -pybamm.grad(c)  
dcdt = -pybamm.div(N)  
model.rhs = {c: dcdt}  
model.initial_conditions = {c: pybamm.Scalar(1)}

#BC
lbc = pybamm.Scalar(0)
rbc = pybamm.Scalar(2)

model.boundary_conditions ={c: {"left": (lbc, "Neumann"), "right": (rbc, "Neumann")}}
model.variables= {"Concentration": c, "Flux": N}


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
