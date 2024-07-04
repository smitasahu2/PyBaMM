clear 
close all
format long

%
%============================ Loading DandeLiion data =====================
%

% Porosity
porosity_dande = importdata( 'build/porosity_liquid.dat');
% SEI thickness
LSEI_dande = importdata( 'build/SEI_thickness.dat');
% Total capacity
cap_dande = importdata( 'build/capacity.dat');
% Total voltage
voltage_dande = importdata( 'build/total_voltage.dat');
% Li metal
C_metal_dande =  importdata( 'build/concentrtion_Li_metal.dat'); 

% Dead Li metal
C_dead_dande = importdata( 'build/concentrtion_dead_Li.dat');
% time = [0 100 200 300 400 500 600 800 900 1000 1200 1400 1600 2000 3620];
time = [0 100 200 300 400 500 600 800 900 1000 1200 1400 1600 2000 4000 6160];
figure('Name','Porosity')
subplot(2,2,1)
ploot(time, porosity_dande.data(1,2:end),'b',' Anode', 'Time [Min]','Porosity')
subplot(2,2,2)
ploot(time, LSEI_dande.data(1,2:end),'b',' Anode', 'Time [Min]','Thickness of SEI [m]')
subplot(2,2,3)
ploot(cap_dande.data(:,1),cap_dande.data(:,2),'b',' Total', 'Time [s]','Capacity')
subplot(2,2,4)
ploot(voltage_dande.data(:,1), voltage_dande.data(:,2),'b','1C C-rate', 'Time [Min]','Voltage [V]')
figure(2)
subplot(2,2,1)
ploot(time, C_metal_dande.data(1,2:end),'b','at $x=0$', 'Time [Min]','plated Li-metal')

subplot(2,2,2)
ploot(time,C_dead_dande.data(1,2:end),'b','at $x=0$', 'Time [Min]','Dead Li')

subplot(2,2,3)
ploot(C_metal_dande.data(:,1), C_metal_dande.data(:,end),'b',' at $t=t_f$', '$x$ [m]','Li-metal')

subplot(2,2,4)
ploot(C_dead_dande.data(:,1), C_dead_dande.data(:,end),'b','at $t=t_f$ ', '$x$ [m]','Dead Li')









% clear 
% format long
% 
% %**************************************************************************
% %============================ Loading DandeLiion data =====================
% %**************************************************************************
% 
% % Porosity
% porosity_D25e22_dande = importdata( 'porosity_liquid.dat');
% % SEI thickness
% LSEI_D25e22_dande = importdata( 'SEI_thickness.dat');
% 
% % Total capacity
% cap_D25e22_dande = importdata( 'capacity.dat');
% % Total capacity
% voltage_D25e22_dande = importdata( 'total_voltage.dat');
% 
% 
% 
% time = [0, 100,200,300,400,500,600,800,900,1000,1200,1400,1600,2000, 3620]  ;
% %**************************************************************************
% %============================ Loading pybamm data =========================
% %**************************************************************************
% 
% % Porosity
% p_D25e22  = importdata("porosity_D2.5e-22.csv");
% LSEI_D25e22  = importdata("LSEI_D2.5e-22.csv");
% 
% % Time [min]	Current [A]	Terminal voltage [V]	Discharge capacity [A.h]	Loss of capacity to SEI [A.h]	Negative electrode capacity [A.h]	Positive electrode capacity [A.h]	Throughput capacity [A.h]	Total capacity lost to side reactions [A.h]	Total lithium capacity [A.h]	Loss of lithium to SEI [mol]	Total lithium in negative electrode [mol]	Total lithium in positive electrode [mol]	Loss of lithium inventory [%]	Loss of active material in negative electrode [%]
% SEI_D25e22 =importdata("SEI_D2.5e-22.csv");
% 
% % plots porosity
% figure('Name','Porosity')
% ploot(time, porosity_D25e22_dande.data(1,2:end),'*b','', 'Time [Min]','')
% 
% ploot(SEI_D25e22.data(:,1)*60, p_D25e22(1,:),'r','', 'Time [Min]','Porosity')
% legend('DandeLiion: D25e22', 'Pybamm D25e22')
% 
% 
% 
% % plots SEI Thickness
% figure('Name','SEI Thickness')
% ploot(time, LSEI_D25e22_dande.data(1,2:end),'*b','', 'Time [Min]','')
% 
% ploot(SEI_D25e22.data(:,1)*60, LSEI_D25e22(1,:),'r','', 'Time [Min]','SEI Thickness')
% legend('DandeLiion: D25e22','Pybamm D25e22')
% 
% 
% % figure('Name','Capacity')
% % ploot(cap_D25e22_dande.data(:,1),cap_D25e22_dande.data(:,2),'*b','', 'Time [s]','')
% % ploot(SEI_D25e22.data(:,1)*60, SEI_D25e22.data(:,8),'r','', 'Time [Min]','')
% % legend('DandeLiion: D25e22','Pybamm D25e22')
% 
% figure('Name','Voltage')
% ploot(SEI_D25e22.data(:,1)*60, SEI_D25e22.data(:,3),'b','', 'Time [Min]','')
% ploot(voltage_D25e22_dande.data(:,1), voltage_D25e22_dande.data(:,2),'*k','', 'Time [Min]','Voltage')
% 
