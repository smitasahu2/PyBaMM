import json
import numpy as np

N = 5001  # Number of points
file_name = "parameters.json"

print("-- Creating", file_name, "for testing...")

x = np.linspace(0, 1, N)


#################### Cell ####################

cell = {}

cell["A"] = 0.1027
cell["Ncells"] = 1
cell["T0"] = 298.15
cell["tplus"] = 0.2594
cell["T_ref"] = 298.15
cell["E_act_diff"] = 17100
cell["E_act_cond"] = 17100
cell["c0"] = 1000
cell["t_max"] = 3750.0
cell["V_min"] = 2.5
cell["V_max"] = 4.2
cell["current"] = -5

# Pouch cell related parameters
cell["Nx"] = 1
cell["Ny"] = 1
cell["Nz"] = 1  # Not used yet (used Ncells instead)
cell["Lx"] = 0.042
cell["Ly"] = 0.140
cell["Lz"] = 0.0114
cell["kx"] = 60.5
cell["ky"] = 60.5
cell["kz"] = 0.914
cell["rho"] = 2586
cell["Cp"] = 1361
cell["TempBC"] = "Zero Heat Source"

# Current collector #1
cc1 = {}
cc1["x0"] = 0.25
cc1["x1"] = 0.75
cc1["len"] = 0.014
cc1["side"] = "Top"

# Current collector #2
cc2 = cc1.copy()
cc2["side"] = "Bottom"

cell["CC1"] = cc1
cell["CC2"] = cc2

# Output times
t_output = [0, 2000, 1000, 4000, 1000]  # Tricky unsorted list with duplicates

cell["t_output"] = t_output

# Conductivity in the electrolyte
cm = np.linspace(0, 2, N)
kappa = (
    0.1297 * cm * cm * cm - 2.51 * cm * np.sqrt(cm) + 3.329 * cm
)  # sqrt function from numpy module

# Diffusivity in the electrolyte
cm[0] = 1.0  # Avoid division by 0
De = 8.794e-11 * cm * cm - 3.972e-10 * cm + 4.862e-10
De[0] = 2 * De[1] - De[2]  # Linear extrapolation
cm[0] = 0

diffusivity = {}
conductivity = {}
json_eval = {}

json_eval["x"] = list(cm * 1000)
json_eval["y"] = list(De)

diffusivity["eval"] = json_eval.copy()

json_eval["y"] = list(kappa)

conductivity["eval"] = json_eval.copy()

cell["conductivity"] = conductivity.copy()
cell["diffusivity"] = diffusivity.copy()


#################### Anode ####################

anode = {}

anode["N"] = 30
anode["M"] = 30
anode["L"] = 8.52e-05
anode["R"] = 5.86e-06
anode["el"] = 0.25
anode["B"] = 0.1250
anode["bet"] = 383959
anode["cmax"] = 33133
anode["sigma_s"] = 215
anode["E_act_Ds"] = 3.03e4
anode["E_act_k0"] = 35000
anode["k0"] = 0.0672e-10  # 3.358e-12
anode["cs0"] = 29866

# Diffusivity in Anode
y = 3.3e-14 * np.ones_like(x)

json_eval["x"] = list(x)
json_eval["y"] = list(y)

diffusivity["eval"] = json_eval.copy()

anode["diffusivity"] = diffusivity.copy()

# U_eq in Anode
a = 1.9793
b = 39.028
c = 0.2482
d = 0.0909
e = 29.8538
g = 0.1234
h = 0.04478
i = 14.9159
j = 0.2769
k = 0.0205
m = 30.4444
n = 0.6103
y = (
    a * np.exp(-b * x)
    + c
    - d * np.tanh(e * (x - g))
    - h * np.tanh(i * (x - j))
    - k * np.tanh(m * (x - n))
)

json_eval["x"] = list(x)
json_eval["y"] = list(y)

eqm_potential = {}
eqm_potential["eval"] = json_eval.copy()

# Derivative of U_eq in Anode
a = 1.9793
b = 39.028
c = 0.2482
d = 0.0909
e = 29.8538
g = 0.1234
h = 0.04478
i1 = 14.9159
j1 = 0.2769
k1 = 0.0205
m = 30.4444
n = 0.6103

y = (
    -a * b * np.exp(-b * x)
    - d * e * (1 - np.tanh(e * (x - g)) ** 2)
    - h * i1 * (1 - np.tanh(i1 * (x - j1)) ** 2)
    - k1 * m * (1 - np.tanh(m * (x - n)) ** 2)
)
# y = y / 33133.0

json_eval["x"] = list(x)
json_eval["y"] = list(y)

eqm_potential["derivative_eval"] = json_eval.copy()

# Integral of U_eq in Anode
a = 1.9793
b = 39.028
c = 0.2482
d = 0.0909
e = 29.8538
g = 0.1234
h = 0.04478
i1 = 14.9159
j1 = 0.2769
k = 0.0205
m = 30.4444
n = 0.6203

y = (
    -a / b * np.exp(-b * x)
    + c * x
    + d / e * np.log(np.cosh(e * (x - g)))
    + h / i1 * np.log(np.cosh(i1 * (x - j1)))
    + k / m * np.log(np.cosh(m * (x - n)))
)
# y = y * 33133.0

# json_eval['x'] = list(x)
# json_eval['y'] = list(y)

# eqm_potential['integral_eval'] = json_eval.copy()

anode["eqm_potential"] = eqm_potential.copy()


#################### Cathode ####################

cathode = {}

cathode["N"] = 30
cathode["M"] = 30
cathode["L"] = 7.56e-05
cathode["R"] = 5.22e-06
cathode["el"] = 0.335
cathode["B"] = 0.1939
cathode["bet"] = 382184
cathode["cmax"] = 63104.0
cathode["sigma_s"] = 0.18
cathode["E_act_Ds"] = 25000
cathode["E_act_k0"] = 17800
cathode["k0"] = 3.5446e-11  # 1..7723e-11
cathode["cs0"] = 17038.0

# Diffusivity in Cathode
y = 4e-15 * np.ones_like(x)

json_eval["x"] = list(x)
json_eval["y"] = list(y)

diffusivity["eval"] = json_eval.copy()

cathode["diffusivity"] = diffusivity.copy()

# U_eq in Cathode

a = -0.8090
c = 4.4875
d = 0.0428
e = 18.5138
g = 0.5542
h = 17.7326
i = 15.7890
j = 0.3117
k = 17.5842
m = 15.9308
n = 0.3120

y = (
    a * x
    + c
    - d * np.tanh(e * (x - g))
    - h * np.tanh(i * (x - j))
    + k * np.tanh(m * (x - n))
)


json_eval["x"] = list(x)
json_eval["y"] = list(y)

eqm_potential = {}
eqm_potential["eval"] = json_eval.copy()

# Derivative of U_eq in Cathode
a = -0.8090
c = 4.4875
d = 0.0428
e = 18.5138
g = 0.5542
h = 17.7326
i = 15.7890
j = 0.3117
k = 17.5842
m = 15.9308
n = 0.3120

y = (
    a
    - d * e * (1 - np.tanh(e * (x - g)) ** 2)
    - h * i * (1 - np.tanh(i * (x - j)) ** 2)
    + k * m * (1 - np.tanh(m * (x - n)) ** 2)
)
# y = y / 63104.0

json_eval["x"] = list(x)
json_eval["y"] = list(y)

eqm_potential["derivative_eval"] = json_eval.copy()

# Integral of U_eq in Cathode
a = -0.8090
c = 4.4875
d = 0.0428
e = 18.5138
g = 0.5542
h = 17.7326
i = 15.7890
j = 0.3117
k = 17.5842
m = 15.9308
n = 0.3120

y = (
    0.5 * a * x * x
    + c * x
    + d / e * np.log(np.cosh(e * (x - g)))
    + h / i * np.log(np.cosh(i * (x - j)))
    - k / m * np.log(np.cosh(m * (x - n)))
)
# y = y * 63104.0

# json_eval['x'] = list(x)
# json_eval['y'] = list(y)

# eqm_potential['integral_eval'] = json_eval.copy()

cathode["eqm_potential"] = eqm_potential.copy()


#################### Separator ####################

separator = {}

separator["N"] = 30
separator["L"] = 1.2e-5
separator["el"] = 0.47
separator["B"] = 0.3222


#################### Write ####################

p = {}
params = {}

params["cell"] = cell
params["anode"] = anode
params["cathode"] = cathode
params["separator"] = separator

p["params"] = params

# print(json.dumps(p, indent=4))

with open(file_name, "w", encoding="utf-8") as f:
    json.dump(p, f, ensure_ascii=False, indent=4)
