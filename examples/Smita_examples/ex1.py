"""
calculation state of charge 
    dx_n/dt = -I(t)/Q_n
    dx_p/dt = -I(t)/Q_p
    V(t) = Up - Un - I(t)R
    x_n(0) = xn0. x_p(0) = xpo
"""
import pybamm
import numpy as np

x_n = pybamm.Variable("Negative electrode stochiometry")
x_p = pybamm.Variable("Positive electrode stochiometry")

i = pybamm.FunctionParameter("Current function [A]", {"Time [s]": pybamm.t})
x_n_0 = pybamm.Parameter("Initial negative electrode stochiometry")
x_p_0 = pybamm.Parameter("Initial positive electrode stochiometry")
U_p = pybamm.FunctionParameter("Positive electrode OCV", {"x_p": x_p})
U_n = pybamm.FunctionParameter("Negative electrode OCV", {"x_n": x_n})
Q_n = pybamm.Parameter("Negative electrode capacity [A.h]")
Q_p = pybamm.Parameter("Positive electrode capacity [A.h]")
R = pybamm.Parameter("Electrode resistance [Ohm]")

model = pybamm.BaseModel("reservoir model")
model.rhs[x_n] = -i / Q_n
model.initial_conditions[x_n] = x_n_0
model.rhs[x_p] = i / Q_p
model.initial_conditions[x_p] = x_p_0

model.variables["Voltage [V]"] = U_p - U_n -  i * R
model.variables["Negative electrode stochiometry"] = x_n
model.variables["Positive electrode stochiometry"] = x_p
model.events = [
    pybamm.Event("Minimum negative stochiometry", x_n - 0),
    pybamm.Event("Maximum negative stochiometry", 1 - x_n),
    pybamm.Event("Minimum positive stochiometry", x_p - 0),
    pybamm.Event("Maximum positive stochiometry", 1 - x_p),
]

def current(t):
    return 2 * t
parameter_values = pybamm.ParameterValues({"Current function [A]": current})

def graphite_LGM50_ocp_Chen2020(sto):
  u_eq = (
      1.9793 * pybamm.exp(-39.3631 * sto)
      + 0.2482
      - 0.0909 * pybamm.tanh(29.8538 * (sto - 0.1234))
      - 0.04478 * pybamm.tanh(14.9159 * (sto - 0.2769))
      - 0.0205 * pybamm.tanh(30.4444 * (sto - 0.6103))
  )
  return u_eq


def nmc_LGM50_ocp_Chen2020(sto):
  u_eq = (
      -0.8090 * sto
      + 4.4875
      - 0.0428 * pybamm.tanh(18.5138 * (sto - 0.5542))
      - 17.7326 * pybamm.tanh(15.7890 * (sto - 0.3117))
      + 17.5842 * pybamm.tanh(15.9308 * (sto - 0.3120))
  )
  return u_eq


param = pybamm.ParameterValues({
    "Current function [A]": current,
    "Initial negative electrode stochiometry": 0.9,
    "Initial positive electrode stochiometry": 0.1,
    "Negative electrode capacity [A.h]": 1,
    "Positive electrode capacity [A.h]": 1,
    "Electrode resistance [Ohm]": 0.1,
    "Positive electrode OCV": nmc_LGM50_ocp_Chen2020,
    "Negative electrode OCV": graphite_LGM50_ocp_Chen2020,
})


sim = pybamm.Simulation(model, parameter_values=param)
sol = sim.solve([0, 1])
sol.plot(["Voltage [V]", "Negative electrode stochiometry", "Positive electrode stochiometry"])



"""
import numpy
# variables
x_n = pybamm.Variable("Negative electrode stochiometry")
x_p = pybamm.Variable("Positive electrode stochiometry")

x_n_0 = pybamm.Parameter("Initial negative electrode stochiometry")
x_p_0 = pybamm.Parameter("Initial positive electrode stochiometry")
U_p = pybamm.FunctionParameter("Positive electrode OCV", {"x_p": x_p})
U_n = pybamm.FunctionParameter("Negative electrode OCV", {"x_n": x_n})
Q_n = pybamm.Parameter("Negative electrode capacity [A.h]")
Q_p = pybamm.Parameter("Positive electrode capacity [A.h]")
R = pybamm.Parameter("Electrode resistance [Ohm]")
# Applied current
I = pybamm.FunctionParameter("Current function [A]", {"Time [s]": pybamm.t})


model = pybamm.BaseModel("soc")

model.rhs[x_n] = -I/Q_n
model.initial_conditions[x_n] = x_n_0

model.rhs[x_p] = -I/Q_p
model.initial_conditions[x_n] = x_p_0


model.variables["Negative electrode stochiometry"] = x_n
model.variables["Positive electrode stochiometry"] = x_p
model.variables["Voltage [V]"] = U_p - U_n -  I * R

# Expression tree
#model.rhs[x_n].visualise("x_n_rhs.png")
#model.rhs[x_p].visualise("x_p_rhs.png")
# print(model.rhs[x_n])
# model.rhs[x_n].children[1]
# model.rhs[x_n].children[0].children[0].children[0]

# event
model.events = [
    pybamm.Event("Minimum negative stochiometry", x_n - 0),
    pybamm.Event("Maximum negative stochiometry", 1 - x_n),
    pybamm.Event("Minimum positive stochiometry", x_p - 0),
    pybamm.Event("Maximum positive stochiometry", 1 - x_p),
]

# # my parameters
# param = pybamm.ParameterValues({"Q_n": 5})
# param = pybamm.ParameterValues({"Q_p": 5})
# param = pybamm.ParameterValues({"x_n_0": 0.8})
# param = pybamm.ParameterValues({"x_p_0": 0.2})


def current(t):
    return pybamm.sinh(t)


def graphite_LGM50_ocp_Chen2020(sto):
  u_eq = (
      1.9793 * pybamm.exp(-39.3631 * sto)
      + 0.2482
      - 0.0909 * pybamm.tanh(29.8538 * (sto - 0.1234))
      - 0.04478 * pybamm.tanh(14.9159 * (sto - 0.2769))
      - 0.0205 * pybamm.tanh(30.4444 * (sto - 0.6103))
  )
  return u_eq


def nmc_LGM50_ocp_Chen2020(sto):
  u_eq = (
      -0.8090 * sto
      + 4.4875
      - 0.0428 * pybamm.tanh(18.5138 * (sto - 0.5542))
      - 17.7326 * pybamm.tanh(15.7890 * (sto - 0.3117))
      + 17.5842 * pybamm.tanh(15.9308 * (sto - 0.3120))
  )
  return u_eq

param = pybamm.ParameterValues({"Current function [A]": current})

param = pybamm.ParameterValues({
    "Current function [A]": current,
    "Initial negative electrode stochiometry": 0.9,
    "Initial positive electrode stochiometry": 0.1,
    "Negative electrode capacity [A.h]": 1,
    "Positive electrode capacity [A.h]": 1,
    "Electrode resistance [Ohm]": 0.1,
    "Positive electrode OCV": nmc_LGM50_ocp_Chen2020,
    "Negative electrode OCV": graphite_LGM50_ocp_Chen2020,
})

# solve ode 
sim = pybamm.Simulation(model, parameter_values=param)
sol = sim.solve([0,1])
sol.plot(["Voltage [V]", "Negative electrode stochiometry", "Positive electrode stochiometry"])
"""
