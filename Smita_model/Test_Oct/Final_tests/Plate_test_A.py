import pybamm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
from numpy import savetxt
import ploot_plate
import os  # Import the os module
#pybamm.set_logging_level("INFO")
#source env/bin/activate

def run_plate_test(plate_test1, kpe, Gamma):    
    # Define the main folder where you want to save the output files
    main_folder = "Plate"
    kpe_str = f"{kpe:.1e}"
    Gamma_str = f"{Gamma:.1e}"
 
    # Create the subfolder based on the kpe_Gamma_str variable
    kpe_Gamma_str =  f"kpe{kpe:.1e}Gamma{Gamma:.1e}"
    subfolder = f"kpe{kpe:.1e}Gamma{Gamma:.1e}"
    output_folder = os.path.join(main_folder, subfolder)
    # Check if the subfolder exists, and create it if it doesn't
    try:
      
      if not os.path.exists(output_folder):
        os.makedirs(output_folder)

      param = pybamm.ParameterValues("OKane2022") 
      DandeLiion_current = pd.read_csv(os.path.join(output_folder,"total_current.csv"), comment="#", header=None).to_numpy() #standard_protocol = pybamm.Experiment(["Discharge at 0.5C until 2.7V (1 minute period)","Charge at 0.5C until 4.2V (1 minute period)",]*5) # param["Current function [A]"] = 2.5
   
    # create interpolant
      current_interpolant = pybamm.Interpolant(DandeLiion_current[:, 0], -DandeLiion_current[:, 1], pybamm.t)
    # set drive cycle
      param["Current function [A]"] = current_interpolant
      var_pts = {
      "x_n": 20,  # negative electrode
      "x_s": 15,  # separator 
      "x_p": 20,  # positive electrode
      "r_n": 20,  # negative particle
      "r_p": 20,  # positive particle
        }    

      model_plate = pybamm.lithium_ion.DFN({"lithium plating": "partially reversible",
                                            "SEI": "solvent-diffusion limited", 
                                            "SEI porosity change": "true",
                                            "calculate discharge energy" : "true"})
      
      param["Ratio of lithium moles to SEI moles"]= 2.0
      param["Upper voltage cut-off [V]"] = 4.5
      param["Lower voltage cut-off [V]"] = 2.7
      param["Lithium plating kinetic rate constant [m.s-1]"] = kpe
      param["Dead lithium decay constant [s-1]"] =  Gamma

     
      print(f"Lithium plating kinetic rate constant [m.s-1] = {kpe_str}")
      print(f"Dead lithium decay constant [s-1] = {Gamma_str}")

      sim_plate = pybamm.Simulation(model_plate,  parameter_values=param, var_pts=var_pts)
      sol_plate = sim_plate.solve()
    
      # Save to a CSV file
      L_SEI = sol_plate["Total SEI thickness [m]"].entries
      porosity = sol_plate["Negative electrode porosity"].entries
      C_Li= sol_plate["Lithium plating concentration [mol.m-3]"].entries[1,:]
      Dead = sol_plate["Dead lithium concentration [mol.m-3]"].entries[1,:]
      sol_plate.save_data(os.path.join(output_folder, f"Plate{kpe_Gamma_str}.csv"),
                      [
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
                        "Total lithium in negative electrode [mol]",
                        "Loss of lithium inventory [%]",
                        "Loss of active material in negative electrode [%]",
                        
                      ],
                      to_format="csv")

      np.savetxt(os.path.join(output_folder, f"LSEI{kpe_Gamma_str}.csv"), L_SEI, delimiter=',')
      np.savetxt(os.path.join(output_folder, f"porosity{kpe_Gamma_str}.csv"), porosity, delimiter=',')
      np.savetxt(os.path.join(output_folder, f"CLi{kpe_Gamma_str}.csv"), C_Li, delimiter=',')
      np.savetxt(os.path.join(output_folder, f"Dead{kpe_Gamma_str}.csv"), Dead, delimiter=',')
      ploot_plate.myplot(sol_plate)
      print(f"Output folder and files created successfully: {output_folder}")

      #Plotting
      # PyBaMM data processing
      LSEI = pd.read_csv(os.path.join(output_folder,f"LSEI{kpe_Gamma_str}.csv"))
      data1 = pd.read_csv(os.path.join(output_folder,f"Plate{kpe_Gamma_str}.csv"))
      porosity_pybamm = pd.read_csv(os.path.join(output_folder,f"porosity{kpe_Gamma_str}.csv"))
      time_pybamm = data1.iloc[:, 0]
      current = data1.iloc[:, 1]
      voltage_pybamm = data1.iloc[:, 2]
      discharge_capacity = data1.iloc[:, 3]
      Loss_of_capacity_to_SEI= data1.iloc[:, 4]
      throughput_capacity = data1.iloc[:, 6]
      LSEI = LSEI.iloc[1, :]
      porosity_pybamm = porosity_pybamm.iloc[1, :]
      CLi= pd.read_csv(os.path.join(output_folder,f"CLi{kpe_Gamma_str}.csv"))
      Dead= pd.read_csv(os.path.join(output_folder,f"Dead{kpe_Gamma_str}.csv"))
      
      # Plotting
      fig, axs = plt.subplots(2, 3, figsize=(12, 8))
       # PyBaMM plots
      axs[0, 0].plot(time_pybamm, LSEI, '--', linewidth=1, color='r', label='PyBaMM')
      axs[0, 1].plot(time_pybamm, porosity_pybamm, '--', linewidth=1, color='r', label='PyBaMM')
      axs[0, 2].plot(throughput_capacity, discharge_capacity,'.-', linewidth=1, color='r', label='PyBaMM')
      axs[1,0].plot(time_pybamm, Loss_of_capacity_to_SEI,'--', linewidth=1, color='r', label='PyBaMM')
      axs[1, 1].plot(time_pybamm, voltage_pybamm, '--', linewidth=1, color='r', label='PyBaMM')
      axs[1, 2].plot(time_pybamm, current, '--', linewidth=1, color='r', label='PyBaMM')

      # DandeLiion data processing
      t_output = np.genfromtxt(os.path.join(output_folder,"time.dat")) /60
      capacity = np.genfromtxt(os.path.join(output_folder,"capacity.dat"))
      sei_thickness = np.genfromtxt(os.path.join(output_folder,"SEI_thickness.dat"))
      porosity_liquid = np.genfromtxt(os.path.join(output_folder,"porosity_liquid.dat"))
      total_voltage = np.genfromtxt(os.path.join(output_folder,"total_voltage.dat"))
      total_current = np.genfromtxt(os.path.join(output_folder,"total_current_estimated.dat"))
      jtot_anode = np.genfromtxt(os.path.join(output_folder,"jtot_anode.dat"))
      jtot_cons = np.genfromtxt(os.path.join(output_folder,"jtot_cons.dat"))
      dead_dande = np.genfromtxt(os.path.join(output_folder,"concentrtion_dead_Li.dat"))
      plate_dande = np.genfromtxt(os.path.join(output_folder,"concentrtion_Li_metal.dat"))

 
      axs[0, 0].plot(t_output, sei_thickness[-1, :], '-', linewidth=1, color='b', label='DandeLiion')
      axs[0, 1].plot(t_output, porosity_liquid[1,:], '-', linewidth=1, color='b', label='DandeLiion')
      axs[0, 2].plot(capacity[:, 1] , capacity[:, 2], '-', linewidth=1, color='b', label='DandeLiion')
      #axs[1, 0].plot(t_output, capacity[:, 2]- 3.84e5* sei_thickness[-1, :] , '-', linewidth=1, color='b', label='DandeLiion')
      axs[1, 1].plot(total_voltage[:, 0]/60 , total_voltage[:, 1], '-', linewidth=1, color='b', label='DandeLiion')
      axs[1, 2].plot(total_current[:, 0]/60 , -total_current[:, 1], '-', linewidth=1, color='b', label='DandeLiion')
            


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
      axs[0, 0].set_ylabel('SEI Thickness [m] ($x = L_a$)', fontsize=12)
      axs[0, 1].set_ylabel('Porosity in anode ($x = L_a$)', fontsize=12)
      axs[1, 1].set_ylabel('Total Voltage [V]', fontsize=12)
      for i in range(2):
        for j in range(3):
            axs[i, j].legend()
      plt.suptitle("DandeLiion vs. PyBaMM Comparison $D_{sol}$ = " f"{kpe_Gamma_str}")
      plt.tight_layout()
      plt.savefig(f"plate{kpe_Gamma_str}.pdf")
      plt.savefig(f"plate{kpe_Gamma_str}.eps")
      plt.savefig(f"plate{kpe_Gamma_str}.jpg")
      plt.show()
      
      # fig, axs = plt.subplots(2, 2, figsize=(8, 8))
      # Dead = sol_plate["Dead lithium concentration [mol.m-3]"].entries[-1,:]
      # plate = sol_plate["Lithium plating concentration [mol.m-3]"].entries[-1,:]
      # plt.subplot(1, 2, 1).plot(throughput_capacity, plate, label="Plated Li concentration")
      # #plt.subplot(1, 2, 1).plot(t_output/60, dead_dande[1,:], label="Dead Li concentration")
      # #axs[0, 0].xlabel("Throughput capacity [A.h]")
      # #axs[0, 0].legend()

      # plt.subplot(1, 2, 2).plot(throughput_capacity, Dead, label="Dead lithium concentration")
      # #plt.subplot(1, 2, 1).plot(t_output/60, dead_dande[1,:], label="Dead Li concentration")

      # #plt.subplot(1, 2, 2).ylabel("Total concentration of dead lithiim [mol m^3]")

      # plt.tight_layout()
      # plt.show()



    except Exception as e:
      print(f"An error occurred: {str(e)}")
    
    #print(param)




all_test1_values = [1]#, 2]  # Add all the test cases you want to run
kpe_values = [1e-9]#, 1e-9]  # Corresponding diffusivity values
Gamma_values = [2.5e-6]#[4e-7, 1e-6, 2.5e-6]
for i, all_test1 in enumerate(all_test1_values):
    run_plate_test(all_test1, kpe_values[i], Gamma_values[0])