clear 
close all
format long

% Porosity
porosity_1 = importdata( 'buildD2.5e-22/porosity_liquid.dat');
porosity_2 = importdata( 'buildD2.5e-21/porosity_liquid.dat');
porosity_3= importdata( 'buildD7.5e-21/porosity_liquid.dat');
porosity_4 = importdata( 'buildD1.25e-20/porosity_liquid.dat');

%voltage 
voltage_dande_1 = importdata( 'buildD2.5e-22/total_voltage.dat');
voltage_dande_2 = importdata( 'buildD2.5e-21/total_voltage.dat');
voltage_dande_3= importdata( 'buildD7.5e-21/total_voltage.dat');
voltage_dande_4 = importdata( 'buildD1.25e-20/total_voltage.dat');
%capacity
cap_dande_1 = importdata( 'buildD2.5e-22/capacity.dat');
cap_dande_2 = importdata( 'buildD2.5e-21/capacity.dat');
cap_dande_3= importdata( 'buildD7.5e-21/capacity.dat');
cap_dande_4 = importdata( 'buildD1.25e-20/capacity.dat');



%SEI thickness
LSEI_dande_1 = importdata( 'buildD2.5e-22/SEI_thickness.dat');
LSEI_dande_2 = importdata( 'buildD2.5e-21/SEI_thickness.dat');
LSEI_dande_3= importdata( 'buildD7.5e-21/SEI_thickness.dat');
LSEI_dande_4 = importdata( 'buildD1.25e-20/SEI_thickness.dat');

time = [0, 100,200,400,800,1000,1200,1400,1600,2000, 2100,2200,2300,2400,2500,3600,3660,4000,4100, 4200,4400,4800,4900,5000,5100,5200,5300,5400,5500,5600,5700,5800,5900,6000,6090]/3600;
figure('Name', 'Dandeliion plots')


subplot(2,2,1)
ploot(voltage_dande_1.data(:,1), voltage_dande_1.data(:,2),'b',' Anode', 'Time [Min]','Porosity');hold on
ploot(voltage_dande_2.data(:,1), voltage_dande_2.data(:,2),'r',' Anode', 'Time [Min]','Porosity');hold on
ploot(voltage_dande_3.data(:,1), voltage_dande_3.data(:,2),'k',' Anode', 'Time [Min]','Porosity');hold on
ploot(voltage_dande_4.data(:,1), voltage_dande_4.data(:,2),'m',' Anode', 'Time [Min]','Voltage')
legend('D$_{sol}$ = 2.5e-22', 'D$_{sol}$ = 2.5e-21','D$_{sol}$ = 7.5e-21','D$_{sol}$ =  1.25e-20','Interpreter','latex','fontsize',10,'location','best');
subplot(2,2,2)
ploot(cap_dande_1.data(:,1),cap_dande_1.data(:,2),'b',' Total', 'Time [s]','Capacity'); hold on;
ploot(cap_dande_2.data(:,1),cap_dande_2.data(:,2),'b',' Total', 'Time [s]','Capacity'); hold on;
ploot(cap_dande_3.data(:,1),cap_dande_3.data(:,2),'b',' Total', 'Time [s]','Capacity'); hold on;
ploot(cap_dande_4.data(:,1),cap_dande_4.data(:,2),'b',' Total', 'Time [s]','Capacity')
legend('D$_{sol}$ = 2.5e-22', 'D$_{sol}$ = 2.5e-21','D$_{sol}$ = 7.5e-21','D$_{sol}$ =  1.25e-20','Interpreter','latex','fontsize',10,'location','best');

subplot(2,2,3)
ploot(time, porosity_1.data(1,2:end),'b',' Anode', 'Time [Min]','Porosity');hold on
ploot(time, porosity_2.data(1,2:end),'r',' Anode', 'Time [Min]','Porosity');hold on
ploot(time, porosity_3.data(1,2:end),'k',' Anode', 'Time [Min]','Porosity');hold on
ploot(time, porosity_4.data(1,2:end),'m',' Anode', 'Time [Min]','Porosity')
legend('D$_{sol}$ = 2.5e-22', 'D$_{sol}$ = 2.5e-21','D$_{sol}$ = 7.5e-21','D$_{sol}$ =  1.25e-20','Interpreter','latex','fontsize',10,'location','best');

subplot(2,2,4)
ploot(time, LSEI_dande_1.data(1,2:end),'b',' Anode', 'Time [Min]','Porosity');hold on
ploot(time, LSEI_dande_2.data(1,2:end),'r',' Anode', 'Time [Min]','Porosity');hold on
ploot(time, LSEI_dande_3.data(1,2:end),'k',' Anode', 'Time [Min]','Porosity');hold on
ploot(time, LSEI_dande_4.data(1,2:end),'m',' Anode', 'Time [Min]','SEI Thickness')
legend('D$_{sol}$ = 2.5e-22', 'D$_{sol}$ = 2.5e-21','D$_{sol}$ = 7.5e-21','D$_{sol}$ =  1.25e-20','Interpreter','latex','fontsize',10,'location','best');


return
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
time = [0, 100,200,400,800,1000,1200,1400,1600,2000, 2100,2200,2300,2400,2500,3600,3660,4000,4100, 4200,4400,4800,4900,5000,5100,5200,5300,5400,5500,5600,5700,5800,5900,6000,6090];
figure('Name','DandeLiion simulation')
subplot(2,2,1)
ploot(voltage_dande.data(:,1), voltage_dande.data(:,2),'b','1C C-rate', 'Time [Min]','Voltage [V]')
subplot(2,2,2)
ploot(cap_dande.data(:,1),cap_dande.data(:,2),'b',' Total', 'Time [s]','Capacity')
subplot(2,2,3)
ploot(time, porosity_dande.data(1,2:end),'b',' Anode', 'Time [Min]','Porosity')
subplot(2,2,4)
ploot(time, LSEI_dande.data(1,2:end),'b',' Anode', 'Time [Min]','Thickness of SEI [m]')


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
