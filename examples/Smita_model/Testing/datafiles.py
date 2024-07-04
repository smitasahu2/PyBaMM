import pybamm
import matplotlib.pyplot as plt

SEI_Solo_75e21 = pybamm.load("SEI_Solo_75e21.pkl")
SEI_Solo_25e21 = pybamm.load("SEI_Solo_25e21.pkl")
# pybamm.dynamic_plot(SEI_Solo_25e22)
# Saving data and downloading all the 'formation cycle' files with extension .csv and .mat
#  it took approximately 3 hours 55 minutes  to run SEI model with the default value of pybamm 
# #  it took approximately three hours 35 minutes to run SEI model with the default value of pybamm 

SEI_Solo_25e21.save_data("SEI_sol_standard.csv",
                            [
                        "Time [min]", 
                        "Current [A]", 
                        "Terminal voltage [V]", 
                        "Discharge capacity [A.h]",
                        "Loss of capacity to SEI [A.h]",
                        "Negative electrode capacity [A.h]",
                        "Positive electrode capacity [A.h]",
                        "Throughput capacity [A.h]",
                        "Total capacity lost to side reactions [A.h]",
                        "Total lithium capacity [A.h]",
                        "Loss of lithium to SEI [mol]",
                        "Total lithium in negative electrode [mol]",
                         "Total lithium in positive electrode [mol]"
                         ]
                      , to_format="csv")

Disc_cap = SEI_Solo_25e21["Discharge capacity [A.h]"].entries
SEI_cap_loss = SEI_Solo_25e21["Loss of capacity to SEI [A.h]"].entries
A_cap_loss = SEI_Solo_25e21["Negative electrode capacity [A.h]"].entries
C_cap_loss = SEI_Solo_25e21["Positive electrode capacity [A.h]"].entries
Throughput = SEI_Solo_25e21["Throughput capacity [A.h]"].entries
Qtot_cap_loss= SEI_Solo_25e21["Total capacity lost to side reactions [A.h]"].entries
Li_cap_loss= SEI_Solo_25e21["Total lithium capacity [A.h]"].entries
I_F= SEI_Solo_25e21["Current [A]"].entries
t_F = SEI_Solo_25e21["Time [min]"].entries
V_F = SEI_Solo_25e21["Terminal voltage [V]"].entries

fig, ax = plt.subplots(2, 2, figsize=(10, 7))
ax[0,0].plot(t_F, I_F,color="purple", linestyle="solid")
ax[0,0].set(xlabel="Time [h]", ylabel="I [A]")
ax[0,1].plot(t_F, V_F,color="purple", linestyle="solid")
ax[0,1].set(xlabel="Time [h]", ylabel="$V$ [V]")
ax[1,0].plot(t_F, Disc_cap,color="purple", linestyle="solid")
ax[1,0].set(xlabel="Time [h]", ylabel="Discharge Capacity [A.h]")
ax[1,1].plot(t_F, Qtot_cap_loss,color="purple", linestyle="solid")
ax[1,1].set(xlabel="Time [h]", ylabel="Total capacity loss  [A.h]")
plt.tight_layout()
plt.show()

# Save output to CSV files
# sim_SEI.solution.to_csv("output.csv")

# # Open CSV file for writing
# with open('output.csv', 'w', newline='') as f:
#     writer = csv.writer(f)

#     # Write data to CSV file
#     writer.writerows(sol_SEI)


# import os
# os.remove("SPMe.pkl")
# os.remove("SPMe_sol.pkl")
# os.remove("sol_data.pkl")
# os.remove("sol_data.csv")
# os.remove("sol_data.mat")





SEI_Solo_25e22 = pybamm.load("SEI_Solo_25e22.pkl")
pybamm.dynamic_plot(SEI_Solo_25e22)
# Saving data and downloading all the 'formation cycle' files with extension .csv and .mat

SEI_Solo_25e22.save_data("SEI_sol_standard.csv",
                            [
                        "Time [min]", 
                        "Current [A]", 
                        "Terminal voltage [V]", 
                        "Discharge capacity [A.h]",
                        "Loss of capacity to SEI [A.h]",
                        "Negative electrode capacity [A.h]",
                        "Positive electrode capacity [A.h]",
                        "Throughput capacity [A.h]",
                        "Total capacity lost to side reactions [A.h]",
                        "Total lithium capacity [A.h]",
                        "Loss of lithium to SEI [mol]",
                        "Total lithium in negative electrode [mol]",
                         "Total lithium in positive electrode [mol]"
                         ]
                      , to_format="csv")

Disc_cap = SEI_Solo_25e22["Discharge capacity [A.h]"].entries
SEI_cap_loss = SEI_Solo_25e22["Loss of capacity to SEI [A.h]"].entries
A_cap_loss = SEI_Solo_25e22["Negative electrode capacity [A.h]"].entries
C_cap_loss = SEI_Solo_25e22["Positive electrode capacity [A.h]"].entries
Throughput = SEI_Solo_25e22["Throughput capacity [A.h]"].entries
Qtot_cap_loss= SEI_Solo_25e22["Total capacity lost to side reactions [A.h]"].entries
Li_cap_loss= SEI_Solo_25e22["Total lithium capacity [A.h]"].entries
I_F= SEI_Solo_25e22["Current [A]"].entries
t_F = SEI_Solo_25e22["Time [min]"].entries
V_F = SEI_Solo_25e22["Terminal voltage [V]"].entries

fig, ax = plt.subplots(2, 2, figsize=(10, 7))
ax[0,0].plot(t_F, I_F,color="purple", linestyle="solid")
ax[0,0].set(xlabel="Time [h]", ylabel="I [A]")
ax[0,1].plot(t_F, V_F,color="purple", linestyle="solid")
ax[0,1].set(xlabel="Time [h]", ylabel="$V$ [V]")
ax[1,0].plot(t_F, Disc_cap,color="purple", linestyle="solid")
ax[1,0].set(xlabel="Time [h]", ylabel="Discharge Capacity [A.h]")
ax[1,1].plot(t_F, Qtot_cap_loss,color="purple", linestyle="solid")
ax[1,1].set(xlabel="Time [h]", ylabel="Total capacity loss  [A.h]")
plt.tight_layout()
plt.show()

# Save output to CSV files
# sim_SEI.solution.to_csv("output.csv")

# # Open CSV file for writing
# with open('output.csv', 'w', newline='') as f:
#     writer = csv.writer(f)

#     # Write data to CSV file
#     writer.writerows(sol_SEI)


# import os
# os.remove("SPMe.pkl")
# os.remove("SPMe_sol.pkl")
# os.remove("sol_data.pkl")
# os.remove("sol_data.csv")
# os.remove("sol_data.mat")

