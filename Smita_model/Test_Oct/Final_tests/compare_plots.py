import pybamm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
from numpy import savetxt
import ploot
import os  # Import the os module

def run_SEI_test(Choice, diffusivity):
    main_folder = "SEI"
    diffusivity_str = f"{diffusivity:.2e}"
    subfolder = f"{diffusivity:.2e}"
    output_folder = os.path.join(main_folder, subfolder)
    try:
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        
        param = pybamm.ParameterValues("OKane2022") 
        DandeLiion_current = pd.read_csv(os.path.join(output_folder, "total_current.csv"), comment="#", header=None).to_numpy()
        current_interpolant = pybamm.Interpolant(DandeLiion_current[:, 0], -DandeLiion_current[:, 1], pybamm.t)
        param["Current function [A]"] = current_interpolant

        var_pts = {
            "x_n": 20,  # negative electrode
            "x_s": 15,  # separator 
            "x_p": 20,  # positive electrode
            "r_n": 20,  # negative particle
            "r_p": 20,  # positive particle
        }    

        model_SEI = pybamm.lithium_ion.DFN({
            "SEI": "solvent-diffusion limited", 
            "SEI porosity change": "true",
            "calculate discharge energy": "true"
        })

        param["Ratio of lithium moles to SEI moles"] = 2.0
        param["Upper voltage cut-off [V]"] = 4.5
        param["Lower voltage cut-off [V]"] = 2.7
        param["Outer SEI solvent diffusivity [m2.s-1]"] = diffusivity

        sim_SEI = pybamm.Simulation(model_SEI, parameter_values=param, var_pts=var_pts)
        sol_SEI = sim_SEI.solve()

        L_SEI = sol_SEI["Total SEI thickness [m]"].entries
        np.savetxt(os.path.join(output_folder, f"LSEI_D{diffusivity_str}.csv"), L_SEI, delimiter=',')
        porosity = sol_SEI["Negative electrode porosity"].entries
        np.savetxt(os.path.join(output_folder, f"porosity_D{diffusivity_str}.csv"), porosity, delimiter=',')
        sol_SEI.save_data(os.path.join(output_folder, f"SEI_D{diffusivity_str}.csv"), [
            "Time [min]", 
            "Current [A]", 
            "Terminal voltage [V]", 
            "Discharge capacity [A.h]",
            "Loss of capacity to SEI [A.h]",
            "Negative electrode capacity [A.h]",
            "Throughput capacity [A.h]",
            "Total capacity lost to side reactions [A.h]",
            "Total lithium capacity [A.h]",
            "Loss of lithium to SEI [mol]",
            "Total lithium in primary phase in negative electrode [mol]",
            "Loss of lithium inventory [%]",
            "Loss of lithium due to loss of active material in negative electrode [mol]",
        ], to_format="csv")
        if Choice == 1 or Choice == 3:
            # DandeLiion data processing
            t_output = np.genfromtxt(os.path.join(output_folder,"time.dat")) / 60
            capacity = np.genfromtxt(os.path.join(output_folder,"capacity.dat"))
            sei_thickness = np.genfromtxt(os.path.join(output_folder,"SEI_thickness.dat"))
            porosity_liquid = np.genfromtxt(os.path.join(output_folder,"porosity_liquid.dat"))
            total_voltage = np.genfromtxt(os.path.join(output_folder,"total_voltage.dat"))
            total_current = np.genfromtxt(os.path.join(output_folder,"total_current_estimated.dat"))
            jtot_anode = np.genfromtxt(os.path.join(output_folder,"jtot_anode.dat"))
            jtot_cons = np.genfromtxt(os.path.join(output_folder,"jtot_cons.dat"))
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

        if Choice == 2 :
            # PyBaMM data processing
            LSEI = pd.read_csv(os.path.join(output_folder,f"LSEI_D{diffusivity_str}.csv"))
            data1 = pd.read_csv(os.path.join(output_folder,f"SEI_D{diffusivity_str}.csv"))
            porosity_pybamm = pd.read_csv(os.path.join(output_folder,f"porosity_D{diffusivity_str}.csv"))

            time_pybamm = data1.iloc[:, 0]
            voltage_pybamm = data1.iloc[:, 2]
            discharge_capacity = data1.iloc[:, 3]
            throughput_capacity = data1.iloc[:, 7]
            current = data1.iloc[:, 1]
            LSEI = LSEI.iloc[1, :]
            porosity_pybamm = porosity_pybamm.iloc[1, :]
            fig, axs = plt.subplots(2, 3, figsize=(12, 8))
    
            # PyBaMM SEI thickness plot
            axs[0, 0].plot(time_pybamm, LSEI, '-', linewidth=1, color='r', label='PyBaMM')
            # PyBaMM Porosity plot
            axs[0, 1].plot(time_pybamm, porosity_pybamm, '-', linewidth=1, color='r', label='PyBaMM')
            # PyBaMM Voltage plot
            axs[1, 1].plot(time_pybamm, voltage_pybamm, '-', linewidth=1, color='r', label='PyBaMM')
            # PyBaMM capacity plot
            axs[1, 0].plot(throughput_capacity, discharge_capacity,'-', linewidth=1, color='r', label='PyBaMM')
            # PyBaMM Voltage plot
            axs[1, 2].plot(time_pybamm, current, '-', linewidth=1, color='r', label='PyBaMM')
   
        if Choice == 3:
            t_output = np.genfromtxt(os.path.join(output_folder,"time.dat")) / 60
            capacity = np.genfromtxt(os.path.join(output_folder,"capacity.dat"))
            sei_thickness = np.genfromtxt(os.path.join(output_folder,"SEI_thickness.dat"))
            porosity_liquid = np.genfromtxt(os.path.join(output_folder,"porosity_liquid.dat"))
            total_voltage = np.genfromtxt(os.path.join(output_folder,"total_voltage.dat"))
            total_current = np.genfromtxt(os.path.join(output_folder,"total_current_estimated.dat"))
            jtot_anode = np.genfromtxt(os.path.join(output_folder,"jtot_anode.dat"))
            jtot_cons = np.genfromtxt(os.path.join(output_folder,"jtot_cons.dat"))
    

            LSEI = pd.read_csv(os.path.join(output_folder,f"LSEI_D{diffusivity_str}.csv"))
            data1 = pd.read_csv(os.path.join(output_folder,f"SEI_D{diffusivity_str}.csv"))
            porosity_pybamm = pd.read_csv(os.path.join(output_folder,f"porosity_D{diffusivity_str}.csv"))

            time_pybamm = data1.iloc[:, 0]
            voltage_pybamm = data1.iloc[:, 2]
            discharge_capacity = data1.iloc[:, 3]
            throughput_capacity = data1.iloc[:, 7]
            current = data1.iloc[:, 1]
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
            axs[1, 0].plot(throughput_capacity, discharge_capacity,'-', linewidth=1, color='r', label='PyBaMM')
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
        
        print(f"Output folder and files created successfully: {output_folder}")
        ploot.myplot(sol_SEI)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

Choice = [1,2,3]
diffusivity_values = [1.25e-20]
for i, SEI_test1 in enumerate(Choice):
     run_SEI_test(1, diffusivity_values[0])
