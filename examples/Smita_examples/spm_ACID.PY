# variables
import pybamm

epsilon_s_p = pybamm.Variable("Positive electrode active material volume fraction")

# parameters
epsilon_s_p_0 = pybamm.Parameter("Positive electrode active material volume fraction")
i_0_diss = pybamm.Parameter("Dissolution exchange-current density [A.m-2]")
U_diss = pybamm.Parameter("Dissolution open-circuit potential [V]")
F = pybamm.constants.F
R = pybamm.constants.R
T = 295

# model
depsdt = - i_0_diss * pybamm.exp(F / (R * T) * (U_p_plus_eta - U_diss)) / (c_i_max[1] * delta_i[1] * F)
self.rhs[epsilon_s_p] = depsdt

self.initial_conditions[epsilon_s_p] = epsilon_s_p_0