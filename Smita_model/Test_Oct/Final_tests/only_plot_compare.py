import pybamm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
from numpy import savetxt
import ploot
import os  # Import the os module
pybamm.set_logging_level("INFO")
#source env/bin/activate

def plot_SEI_test(SEI_test1, diffusivity):
    main_folder = "SEI"
    diffusivity_str = f"{diffusivity:.2e}"
    subfolder = f"{diffusivity:.2e}"
    output_folder = os.path.join(main_folder, subfolder)
    try:
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        #ploot.myplot(sol_SEI)

        # DandeLiion data processing
        t_output = np.genfromtxt(os.path.join(output_folder,"time.dat")) 
        capacity = np.genfromtxt(os.path.join(output_folder,"capacity.dat"))
        sei_thickness = np.genfromtxt(os.path.join(output_folder,"SEI_thickness.dat"))
        porosity_liquid = np.genfromtxt(os.path.join(output_folder,"porosity_liquid.dat"))
        total_voltage = np.genfromtxt(os.path.join(output_folder,"total_voltage.dat"))
        total_current = np.genfromtxt(os.path.join(output_folder,"total_current_estimated.dat"))
        jtot_anode = np.genfromtxt(os.path.join(output_folder,"jtot_anode.dat"))
        jtot_cons = np.genfromtxt(os.path.join(output_folder,"jtot_cons.dat"))
    
        # PyBaMM data processing
        LSEI = pd.read_csv(os.path.join(output_folder,f"LSEI_D{diffusivity_str}.csv"))
        data1 = pd.read_csv(os.path.join(output_folder,f"SEI_D{diffusivity_str}.csv"))
        porosity_pybamm = pd.read_csv(os.path.join(output_folder,f"porosity_D{diffusivity_str}.csv"))
        time_pybamm = data1.iloc[:, 0]
        current = data1.iloc[:, 1]
        voltage_pybamm = data1.iloc[:, 2]
        discharge_capacity = data1.iloc[:, 3]
        Loss_of_capacity_to_SEI= data1.iloc[:, 4]
        throughput_capacity = data1.iloc[:, 6]
        LSEI = LSEI.iloc[1, :]
        porosity_pybamm = porosity_pybamm.iloc[1, :]

        # Plotting
        fig, axs = plt.subplots(2, 3, figsize=(12, 8))
        # DandeLiion plots
        axs[0, 0].plot(t_output, sei_thickness[-1, :], '-', linewidth=1, color='b', label='DandeLiion')
        axs[0, 1].plot(t_output, porosity_liquid[1,:], '-', linewidth=1, color='b', label='DandeLiion')
        axs[0, 2].plot(capacity[:, 1] , capacity[:, 2], '-', linewidth=1, color='b', label='DandeLiion')
        #axs[1, 0].plot(t_output, capacity[:, 2]- 3.84e5* sei_thickness[-1, :] , '-', linewidth=1, color='b', label='DandeLiion')
        axs[1, 1].plot(total_voltage[:, 0] , total_voltage[:, 1], '-', linewidth=1, color='b', label='DandeLiion')
        axs[1, 2].plot(total_current[:, 0] , -total_current[:, 1], '-', linewidth=1, color='b', label='DandeLiion')
            
        
        # PyBaMM plots
        axs[0, 0].plot(time_pybamm, LSEI, '--', linewidth=1, color='r', label='PyBaMM')
        axs[0, 1].plot(time_pybamm, porosity_pybamm, '--', linewidth=1, color='r', label='PyBaMM')
        axs[0, 2].plot(throughput_capacity, discharge_capacity,'--', linewidth=1, color='r', label='PyBaMM')
        axs[1,0].plot(time_pybamm, Loss_of_capacity_to_SEI,'--', linewidth=1, color='r', label='PyBaMM')
        axs[1, 1].plot(time_pybamm, voltage_pybamm, '--', linewidth=1, color='r', label='PyBaMM')
        axs[1, 2].plot(time_pybamm, current, '--', linewidth=1, color='r', label='PyBaMM')
   
        
        for i in range(2):
            for j in range(3):
                axs[i, j].set_xlabel('Time [seconds]', fontsize=12)
                axs[i, j].grid(True)
        axs[0, 2].set_xlabel('Total Throughput capacity [Ah]', fontsize=12)
        # Set labels and legends specific to DandeLiion plots
        axs[0, 0].set_ylabel('SEI Thickness [m]', fontsize=12)
        axs[0, 1].set_ylabel('Porosity in anode', fontsize=12)
        axs[0, 2].set_ylabel('Total capacity [Ah]', fontsize=12)
        axs[1, 0].set_ylabel('Loss of capacity to SEI [A.h]', fontsize=12)
        axs[1, 1].set_ylabel('Total Voltage [V]', fontsize=12)
        axs[1, 2].set_ylabel('Current [A]', fontsize=12)
        for i in range(2):
            for j in range(3):
                axs[i, j].legend()

        # Set labels and legends specific to PyBaMM plots
        axs[0, 0].set_ylabel('SEI Thickness [m] ($x = L_a$)', fontsize=12)
        axs[0, 1].set_ylabel('Porosity in anode ($x = L_a$)', fontsize=12)
        axs[1, 1].set_ylabel('Total Voltage [V]', fontsize=12)
        
        for i in range(2):
            for j in range(3):
                axs[i, j].legend()
        # plt.title(f"{diffusivity_str}")
        plt.suptitle("DandeLiion vs. PyBaMM Comparison $D_{sol}$ = " f"{diffusivity_str}")
        
        plt.tight_layout()
        # Add a super-title to the entire figure
        plt.savefig(f"Dsol{diffusivity_str}.pdf")
        plt.savefig(f"Dsol{diffusivity_str}.eps")
        plt.savefig(f"Dsol{diffusivity_str}.jpg")
        plt.show()
        
        print(f"Output folder and files created successfully: {output_folder}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


SEI_test1_values = [1, 2, 3, 4]  # Add all the test cases you want to run
diffusivity_values = [2.5e-22, 2.5e-21, 7.5e-21, 1.25e-20]  # Corresponding diffusivity values

for i, SEI_test1 in enumerate(SEI_test1_values):
    plot_SEI_test(SEI_test1, diffusivity_values[i])