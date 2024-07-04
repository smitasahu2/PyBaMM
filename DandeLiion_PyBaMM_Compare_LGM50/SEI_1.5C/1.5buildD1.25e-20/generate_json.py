import json
import numpy as np

N = 5001  # Number of points
file_name = "parameters.json"

print("-- Creating", file_name, "for testing...")

x = np.linspace(0, 1, N)


#################### Cell ####################

cell = {}

cell["A"] = 8.585e-3
cell["Ncells"] = 1
cell["T0"] = 298.15
cell["tplus"] = 0.26
cell["T_ref"] = 296
cell["E_act_diff"] = 17100
cell["E_act_cond"] = 17100
cell["c0"] = 1000
cell["t_max"] = 3750.0
cell["V_min"] = 2.5
cell["V_max"] = 4.15
cell["current"] = -0.15625

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
kappa = 0.2667 * cm * cm * cm - 1.2983 * cm * cm + 1.7919 * cm + 0.1726

# Diffusivity in the electrolyte
cm[0] = 1.0  # Avoid division by 0
De = 2.646e-10 * kappa / cm
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

anode["N"] = 75
anode["M"] = 51
anode["L"] = 74.0e-6
anode["R"] = 1.37e-5
anode["el"] = 0.329
anode["B"] = 0.1620689655
anode["bet"] = 81548.54
anode["cmax"] = 31920
anode["sigma_s"] = 14
anode["E_act_Ds"] = 30300
anode["E_act_k0"] = 53400
anode["k0"] = 1.995e-10
anode["cs0"] = 26120.05

# Diffusivity in Anode
y = 8.4e-13 * np.exp(-11.3 * x) + 8.2e-15

json_eval["x"] = list(x)
json_eval["y"] = list(y)

diffusivity["eval"] = json_eval.copy()

anode["diffusivity"] = diffusivity.copy()

# U_eq in Anode
a = 0.716502
b = 369.028
c = 0.12193
d = 35.6478
e = 0.0530947
g = 0.0169644
h = 27.1365
i = 0.312832
j = 0.0199313
k = 28.5697
m = 0.614221
n = 0.931153
o = 36.328
p = 1.10743
q = 0.140031
r = 0.0189193
s = 21.1967
t = 0.196176
y = (
    a * np.exp(-b * x)
    + c * np.exp(-d * (x - e))
    - r * np.tanh(s * (x - t))
    - g * np.tanh(h * (x - i))
    - j * np.tanh(k * (x - m))
    - n * np.exp(o * (x - p))
    + q
)

json_eval["x"] = list(x)
json_eval["y"] = list(y)

eqm_potential = {}
eqm_potential["eval"] = json_eval.copy()

# Derivative of U_eq in Anode
a = 0.716502
b = 369.028
c = 0.12193
d = 35.6478
e = 0.0530947
g = 0.0169644
h = 27.1365
i = 0.312832
j = 0.0199313
k = 28.5697
m = 0.614221
n = 0.931153
o = 36.328
p = 1.10743
r = 0.0189193
s = 21.1967
t = 0.196176
y = (
    -a * b * np.exp(-b * x)
    - c * d * np.exp(-d * (x - e))
    - r * s / (np.cosh(s * (x - t))) ** 2.0
    - g * h / (np.cosh(h * (x - i))) ** 2.0
    - j * k / (np.cosh(k * (x - m))) ** 2.0
    - n * o * np.exp(o * (x - p))
)
# y = y / 31920.0

json_eval["x"] = list(x)
json_eval["y"] = list(y)

eqm_potential["derivative_eval"] = json_eval.copy()

# Integral of U_eq in Anode
a = 0.716502
b = 369.028
c = 0.12193
d = 35.6478
e = 0.0530947
g = 0.0169644
h = 27.1365
i = 0.312832
j = 0.0199313
k = 28.5697
m = 0.614221
n = 0.931153
o = 36.328
p = 1.10743
q = 0.140031
r = 0.0189193
s = 21.1967
t = 0.196176
y = (
    -a / b * np.exp(-b * x)
    - c / d * np.exp(-d * (x - e))
    - r / s * np.log(np.cosh(s * (x - t)))
    - g / h * np.log(np.cosh(h * (x - i)))
    - j / k * np.log(np.cosh(k * (x - m)))
    - n / o * np.exp(o * (x - p))
    + q * x
)
# y = y * 31920.0

# json_eval['x'] = list(x)
# json_eval['y'] = list(y)

# eqm_potential['integral_eval'] = json_eval.copy()

anode["eqm_potential"] = eqm_potential.copy()


#################### Cathode ####################

cathode = {}

cathode["N"] = 55
cathode["M"] = 51
cathode["L"] = 54.0e-6
cathode["R"] = 6.5e-6
cathode["el"] = 0.296
cathode["B"] = 0.1525773
cathode["bet"] = 188455.38
cathode["cmax"] = 48580
cathode["sigma_s"] = 68.1
cathode["E_act_Ds"] = 80600
cathode["E_act_k0"] = 43600
cathode["k0"] = 5.196e-11
cathode["cs0"] = 12630.8

# Diffusivity in Cathode
y = 3.7e-13 - 3.4e-13 * np.exp(-12 * (x - 0.62) * (x - 0.62))

json_eval["x"] = list(x)
json_eval["y"] = list(y)

diffusivity["eval"] = json_eval.copy()

cathode["diffusivity"] = diffusivity.copy()

# U_eq in Cathode
a = -2.35211
c = 0.0747061
d = 31.886
e = 0.0219921
g = 0.640243
h = 5.48623
i = 0.439245
j = 3.82383
k = 4.12167
m = 0.176187
n = 0.0542123
o = 18.2919
p = 0.762272
q = 4.23285
r = -6.34984
s = 2.66395
t = 0.174352
y = (
    a * x
    - c * np.tanh(d * (x - e))
    - r * np.tanh(s * (x - t))
    - g * np.tanh(h * (x - i))
    - j * np.tanh(k * (x - m))
    - n * np.tanh(o * (x - p))
    + q
)

json_eval["x"] = list(x)
json_eval["y"] = list(y)

eqm_potential = {}
eqm_potential["eval"] = json_eval.copy()

# Derivative of U_eq in Cathode
a = -2.35211
c = 0.0747061
d = 31.886
e = 0.0219921
g = 0.640243
h = 5.48623
i = 0.439245
j = 3.82383
k = 4.12167
m = 0.176187
n = 0.0542123
o = 18.2919
p = 0.762272
r = -6.34984
s = 2.66395
t = 0.174352
y = (
    a
    - c * d / (np.cosh(d * (x - e))) ** 2.0
    - r * s / (np.cosh(s * (x - t))) ** 2.0
    - g * h / (np.cosh(h * (x - i))) ** 2.0
    - j * k / (np.cosh(k * (x - m))) ** 2.0
    - n * o / (np.cosh(o * (x - p))) ** 2.0
)
# y = y / 48580.0

json_eval["x"] = list(x)
json_eval["y"] = list(y)

eqm_potential["derivative_eval"] = json_eval.copy()

# Integral of U_eq in Cathode
a = -2.35211
c = 0.0747061
d = 31.886
e = 0.0219921
g = 0.640243
h = 5.48623
i = 0.439245
j = 3.82383
k = 4.12167
m = 0.176187
n = 0.0542123
o = 18.2919
p = 0.762272
q = 4.23285
r = -6.34984
s = 2.66395
t = 0.174352
y = (
    0.5 * a * x * x
    - c / d * np.log(np.cosh(d * (x - e)))
    - r / s * np.log(np.cosh(s * (x - t)))
    - g / h * np.log(np.cosh(h * (x - i)))
    - j / k * np.log(np.cosh(k * (x - m)))
    - n / o * np.log(np.cosh(o * (x - p)))
    + q * x
)
# y = y * 48580.0

# json_eval['x'] = list(x)
# json_eval['y'] = list(y)

# eqm_potential['integral_eval'] = json_eval.copy()

cathode["eqm_potential"] = eqm_potential.copy()


#################### Separator ####################

separator = {}

separator["N"] = 21
separator["L"] = 20.0e-6
separator["el"] = 0.508
separator["B"] = 0.3041916


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
