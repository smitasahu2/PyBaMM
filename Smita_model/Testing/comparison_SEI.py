import pybamm
import matplotlib.pyplot as plt


SEI_Solo_25e22 = pybamm.load("SEI_Solo_25e22.pkl")
SEI_Solo_25e21 = pybamm.load("SEI_Solo_25e21.pkl")
SEI_Solo_75e20 = pybamm.load("SEI_Solo_75e20.pkl")
SEI_Solo_125e20 = pybamm.load("SEI_Solo_125e20.pkl")

Li_cap_loss_25e22= SEI_Solo_25e22["Total lithium capacity [A.h]"].entries
Li_cap_loss_25e21= SEI_Solo_25e21["Total lithium capacity [A.h]"].entries
Li_cap_loss_75e20= SEI_Solo_75e20["Total lithium capacity [A.h]"].entries
Li_cap_loss_125e20= SEI_Solo_125e20["Total lithium capacity [A.h]"].entries

t_25e22= SEI_Solo_25e22["Time [min]"].entries
t_25e21= SEI_Solo_25e21["Time [min]"].entries
t_75e20= SEI_Solo_75e20["Time [min]"].entries
t_125e21= SEI_Solo_125e20["Time [min]"].entries


fig, ax = plt.subplots(2, 2, figsize=(10, 7))
ax[0,0].plot(t_25e22, Li_cap_loss_25e22,color="purple", linestyle="solid")
ax[0,0].set(xlabel="Time [h]", ylabel="I [A]")
ax[0,0].plot(t_25e22, Li_cap_loss_25e21,color="purple", linestyle="solid")
ax[0,1].set(xlabel="Time [h]", ylabel="$V$ [V]")
ax[0,0].plot(t_25e22, Li_cap_loss_75e20,color="purple", linestyle="solid")
ax[1,0].set(xlabel="Time [h]", ylabel="Discharge Capacity [A.h]")
ax[0,0].plot(t_125e21, Li_cap_loss_125e20,color="purple", linestyle="solid")
ax[1,1].set(xlabel="Time [h]", ylabel="Total capacity loss  [A.h]")
plt.tight_layout()
plt.show()