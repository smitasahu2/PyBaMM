import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define your Choice variable (1, 2, or 3)
Choice = 3 # Change this to 1, 2, or 3 as needed

if Choice == 1:
    # Loading DandeLiion data
    t_output = np.genfromtxt("time.dat") /60
    capacity = np.genfromtxt("capacity.dat")
    sei_thickness = np.genfromtxt("SEI_thickness.dat")
    porosity_liquid = np.genfromtxt("porosity_liquid.dat")
    total_voltage = np.genfromtxt("total_voltage.dat")
    total_current = np.genfromtxt("total_current_estimated.dat")
    jtot_anode = np.genfromtxt("jtot_anode.dat")
    jtot_cons = np.genfromtxt("jtot_cons.dat")

    fig, axs = plt.subplots(2, 3, figsize=(12, 8))
    
    # DandeLiion SEI thickness plot
    axs[0, 0].plot(t_output, sei_thickness[-1, :], '-', linewidth=1, color='b', label='DandeLiion')
    # DandeLiion Porosity plot
    axs[0, 1].plot(t_output, porosity_liquid[len(porosity_liquid) // 3], '-', linewidth=1, color='b', label='DandeLiion')
    # DandeLiion Capacity plot
    axs[0, 2].plot(capacity[:, 0] / 3600, capacity[:, 1], '-', linewidth=1, color='b', label='DandeLiion')
    # DandeLiion Capacity plot
    axs[1, 0].plot(capacity[:, 1], capacity[:, 2], '-', linewidth=1, color='b', label='DandeLiion')
    # DandeLiion Voltage plot
    axs[1, 1].plot(total_voltage[:, 0] / 3600, total_voltage[:, 1], '-', linewidth=1, color='b', label='DandeLiion')
    # DandeLiion Current plot
    axs[1, 2].plot(total_current[:, 0] / 3600, -total_current[:, 1], '-', linewidth=1, color='b', label='DandeLiion')

if Choice == 2:
    # Loading PyBaMM data
    LSEI = pd.read_csv('LSEI_D2.50e-22.csv')
    data1 = pd.read_csv('SEI_D2.50e-22.csv')
    time_pybamm = data1.iloc[:, 0]
    voltage_pybamm = data1.iloc[:, 2]
    discharge_capacity = data1.iloc[:, 3]
    throuhput_capacity = data1.iloc[:, 7]
    porosity_pybamm = pd.read_csv('porosity_D2.50e-22.csv')
    LSEI = LSEI.iloc[1, :]
    current = data1.iloc[:, 1]

    porosity_pybamm = porosity_pybamm.iloc[1, :]

    fig, axs = plt.subplots(2, 3, figsize=(12, 8))
    
    # PyBaMM SEI thickness plot
    axs[0, 0].plot(time_pybamm, LSEI, '-', linewidth=1, color='r', label='PyBaMM')
    # PyBaMM Porosity plot
    axs[0, 1].plot(time_pybamm, porosity_pybamm, '-', linewidth=1, color='r', label='PyBaMM')
    # PyBaMM Voltage plot
    axs[1, 1].plot(time_pybamm, voltage_pybamm, '-', linewidth=1, color='r', label='PyBaMM')
    # PyBaMM capacity plot
    axs[1, 0].plot( throuhput_capacity, discharge_capacity,'-', linewidth=1, color='r', label='PyBaMM')
    # PyBaMM Voltage plot
    axs[1, 2].plot(time_pybamm, current, '-', linewidth=1, color='r', label='PyBaMM')
   

if Choice == 3:
    # Loading DandeLiion data
    t_output = np.genfromtxt("time.dat") /60
    capacity = np.genfromtxt("capacity.dat")
    sei_thickness = np.genfromtxt("SEI_thickness.dat")
    porosity_liquid = np.genfromtxt("porosity_liquid.dat")
    total_voltage = np.genfromtxt("total_voltage.dat")
    total_current = np.genfromtxt("total_current_estimated.dat")
    jtot_anode = np.genfromtxt("jtot_anode.dat")
    jtot_cons = np.genfromtxt("jtot_cons.dat")

    # Loading PyBaMM data
    LSEI = pd.read_csv('LSEI_D2.50e-22.csv')
    data1 = pd.read_csv('SEI_D2.50e-22.csv')
    time_pybamm = data1.iloc[:, 0]
    voltage_pybamm = data1.iloc[:, 2]
    discharge_capacity = data1.iloc[:, 3]
    throuhput_capacity = data1.iloc[:, 7]
    current = data1.iloc[:, 1]
    porosity_pybamm = pd.read_csv('porosity_D2.50e-22.csv')
    LSEI = LSEI.iloc[1, :]
    porosity_pybamm = porosity_pybamm.iloc[1, :]
    
    fig, axs = plt.subplots(2, 3, figsize=(12, 8))

    # DandeLiion SEI thickness plot
    axs[0, 0].plot(t_output, sei_thickness[-1, :], '-', linewidth=1, color='b', label='DandeLiion')
    # DandeLiion Porosity plot
    axs[0, 1].plot(t_output, porosity_liquid[len(porosity_liquid) // 3], '*', linewidth=1, color='b', label='DandeLiion')
    # DandeLiion Capacity plot
    axs[0, 2].plot(capacity[:, 0] / 3600, capacity[:, 1], '-', linewidth=1, color='b', label='DandeLiion')
    # DandeLiion Capacity plot
    axs[1, 0].plot(capacity[:, 1], capacity[:, 2], '-', linewidth=1, color='b', label='DandeLiion')
    # DandeLiion Voltage plot
    axs[1, 1].plot(total_voltage[:, 0] / 60, total_voltage[:, 1], '-', linewidth=1, color='b', label='DandeLiion')
    # DandeLiion Current plot
    axs[1, 2].plot(total_current[:, 0] / 60, -total_current[:, 1], '-', linewidth=1, color='b', label='DandeLiion')
    # PyBaMM SEI thickness plot
    axs[0, 0].plot(time_pybamm, LSEI, '-', linewidth=1, color='r', label='PyBaMM')
    # PyBaMM Porosity plot
    axs[0, 1].plot(time_pybamm, porosity_pybamm, '-', linewidth=1, color='r', label='PyBaMM')
    # PyBaMM Voltage plot
    axs[1, 1].plot(time_pybamm, voltage_pybamm, '-', linewidth=1, color='r', label='PyBaMM')
   # PyBaMM capacity plot
    axs[1, 0].plot( throuhput_capacity, discharge_capacity,'-', linewidth=1, color='r', label='PyBaMM')
   # PyBaMM Voltage plot
    axs[1, 2].plot(time_pybamm, current, '-', linewidth=1, color='r', label='PyBaMM')


# Set common labels, legends, and grid for all plots
for i in range(2):
    for j in range(3):
        axs[i, j].set_xlabel('Time [hours]', fontsize=14)
        axs[i, j].grid(True)

# Set labels and legends specific to DandeLiion plots
if Choice == 1 or Choice == 3:
    axs[0, 0].set_ylabel('SEI Thickness [m] ($x = L_a$)', fontsize=14)
    axs[0, 1].set_ylabel('Porosity in anode ($x = L_a$)', fontsize=14)
    axs[0, 2].set_ylabel('Total capacity [Ah]', fontsize=14)
    axs[1, 0].set_ylabel('Total discharge capacity [Ah]', fontsize=14)
    axs[1, 1].set_ylabel('Total Voltage [V]', fontsize=14)
    axs[1, 2].set_ylabel('Current [A]', fontsize=14)
    for i in range(2):
        for j in range(3):
            axs[i, j].legend()

# Set labels and legends specific to PyBaMM plots
if Choice == 2 or Choice == 3:
    axs[0, 0].set_ylabel('SEI Thickness [m] ($x = L_a$)', fontsize=14)
    axs[0, 1].set_ylabel('Porosity in anode ($x = L_a$)', fontsize=14)
    axs[1, 1].set_ylabel('Total Voltage [V]', fontsize=14)
    for i in range(2):
        for j in range(3):
            axs[i, j].legend()

plt.tight_layout()
plt.show()

data1 = pd.read_csv('SEI_D2.50e-22.csv')
time_pybamm = data1.iloc[:, 0]
discharge_capacity = data1.iloc[:, 3]
throuhput_capacity = data1.iloc[:, 6]
plt.plot(capacity[:, 1], capacity[:, 2], '-', linewidth=1, color='b', label='DandeLiion')
plt.plot( throuhput_capacity, discharge_capacity,'*', linewidth=1, color='r', label='PyBaMM')
plt.legend()
plt.tight_layout()
plt.show()
