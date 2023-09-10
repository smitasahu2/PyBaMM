clear 
format long

%**************************************************************************
%============================ Loading DandeLiion data =====================
%**************************************************************************

% Porosity
porosity_D25e22_dande = importdata( 'porosity_liquid.dat');
% SEI thickness
LSEI_D25e22_dande = importdata( 'SEI_thickness.dat');

% Total capacity
cap_D25e22_dande = importdata( 'capacity.dat');
% Total capacity
voltage_D25e22_dande = importdata( 'total_voltage.dat');



time = [0, 100,200,300,400,500,600,800,900,1000,1200,1400,1600,2000, 3620]  ;
%**************************************************************************
%============================ Loading pybamm data =========================
%**************************************************************************

% Porosity
p_D25e22  = importdata("porosity_D2.5e-22.csv");
LSEI_D25e22  = importdata("LSEI_D2.5e-22.csv");

% Time [min]	Current [A]	Terminal voltage [V]	Discharge capacity [A.h]	Loss of capacity to SEI [A.h]	Negative electrode capacity [A.h]	Positive electrode capacity [A.h]	Throughput capacity [A.h]	Total capacity lost to side reactions [A.h]	Total lithium capacity [A.h]	Loss of lithium to SEI [mol]	Total lithium in negative electrode [mol]	Total lithium in positive electrode [mol]	Loss of lithium inventory [%]	Loss of active material in negative electrode [%]
SEI_D25e22 =importdata("SEI_D2.5e-22.csv");

% plots porosity
figure('Name','Porosity')
ploot(time, porosity_D25e22_dande.data(1,2:end),'*b','', 'Time [Min]','')

ploot(SEI_D25e22.data(:,1)*60, p_D25e22(1,:),'r','', 'Time [Min]','Porosity')
legend('DandeLiion: D25e22', 'Pybamm D25e22')



% plots SEI Thickness
figure('Name','SEI Thickness')
ploot(time, LSEI_D25e22_dande.data(1,2:end),'*b','', 'Time [Min]','')

ploot(SEI_D25e22.data(:,1)*60, LSEI_D25e22(1,:),'r','', 'Time [Min]','SEI Thickness')
legend('DandeLiion: D25e22','Pybamm D25e22')


% figure('Name','Capacity')
% ploot(cap_D25e22_dande.data(:,1),cap_D25e22_dande.data(:,2),'*b','', 'Time [s]','')
% ploot(SEI_D25e22.data(:,1)*60, SEI_D25e22.data(:,8),'r','', 'Time [Min]','')
% legend('DandeLiion: D25e22','Pybamm D25e22')

figure('Name','Voltage')
ploot(SEI_D25e22.data(:,1)*60, SEI_D25e22.data(:,3),'b','', 'Time [Min]','')
ploot(voltage_D25e22_dande.data(:,1), voltage_D25e22_dande.data(:,2),'*k','', 'Time [Min]','Voltage')

