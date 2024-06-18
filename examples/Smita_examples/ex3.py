import pybamm

model = pybamm.BaseModel("my model")
x = pybamm.Variable("x")
x_n = pybamm.Variable("Negative electrode stochiometry")
x_p = pybamm.Variable("Positive electrode stochiometry")
a = pybamm.Parameter("a")
P = pybamm.FunctionParameter("Your parameter name here", {"Time [s]": pybamm.t})
model = pybamm.BaseModel("my model")
model = pybamm.BaseModel("exponential decay")
model.rhs = {x: -a * x}
model.initial_conditions = {x: 1}
model.variables = {"x": x}

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
path = "examples/smita_examples/"

model.rhs[x_n].visualise( "a.png")
print(model.rhs[x_n])
model.rhs[x_n].children[1]
model.rhs[x_n].children[0].children[0].children[0]
stop_at_t_equal_3 = pybamm.Event("Stop at t = 3", pybamm.t - 3)
model.events = [stop_at_t_equal_3]
model.events = [
    pybamm.Event("Minimum negative stochiometry", x_n - 0),
    pybamm.Event("Maximum negative stochiometry", 1 - x_n),
    pybamm.Event("Minimum positive stochiometry", x_p - 0),
    pybamm.Event("Maximum positive stochiometry", 1 - x_p),
]