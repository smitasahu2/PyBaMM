clear 
close all
format long

%**************************************************************************
%============================ Loading DandeLiion data =====================
%**************************************************************************

% Porosity
porosity_D125e20_dande = importdata( 'buildD1.25e-20/porosity_liquid.dat');
porosity_D75e21_dande = importdata( 'buildD7.5e-21/porosity_liquid.dat');
porosity_D25e21_dande = importdata( 'buildD25e-21/porosity_liquid.dat');
porosity_D25e22_dande = importdata( 'buildD25e-22/porosity_liquid.dat');
% SEI thickness
LSEI_D125e20_dande = importdata( 'buildD1.25e-20/SEI_thickness.dat');
LSEI_D75e21_dande = importdata( 'buildD7.5e-21/SEI_thickness.dat');
LSEI_D25e21_dande = importdata( 'buildD25e-21/SEI_thickness.dat');
LSEI_D25e22_dande = importdata( 'buildD25e-22/SEI_thickness.dat');

% Total capacity
cap_D125e20_dande = importdata( 'buildD1.25e-20/capacity.dat');
cap_D75e21_dande = importdata( 'buildD7.5e-21/capacity.dat');
cap_D25e21_dande = importdata( 'buildD25e-21/capacity.dat');
cap_D25e22_dande = importdata( 'buildD25e-22/capacity.dat');
% Total capacity
voltage_D125e20_dande = importdata( 'buildD1.25e-20/total_voltage.dat');
voltage_D75e21_dande = importdata( 'buildD7.5e-21/total_voltage.dat');
voltage_D25e21_dande = importdata( 'buildD25e-21/total_voltage.dat');
voltage_D25e22_dande = importdata( 'buildD25e-22/total_voltage.dat');



time = [0, 1000, 2000, 3620];
%**************************************************************************
%============================ Loading pybamm data =========================
%**************************************************************************

% Porosity
p_D25e22  = importdata("porosity_D2.5e-22.csv");
p_D25e21  = importdata("porosity_D2.5e-21.csv");
p_D75e21  = importdata("porosity_D7.5e-21.csv");
p_D125e20 = importdata("porosity_D1.25e-20.csv");

% SEI thickness
LSEI_D25e22  = importdata("LSEI_D2.5e-22.csv");
LSEI_D25e21  = importdata("LSEI_D2.5e-21.csv");
LSEI_D75e21  = importdata("LSEI_D7.5e-21.csv");
LSEI_D125e20 = importdata("LSEI_D1.25e-20.csv");

% Time [min]	Current [A]	Terminal voltage [V]	Discharge capacity [A.h]	Loss of capacity to SEI [A.h]	Negative electrode capacity [A.h]	Positive electrode capacity [A.h]	Throughput capacity [A.h]	Total capacity lost to side reactions [A.h]	Total lithium capacity [A.h]	Loss of lithium to SEI [mol]	Total lithium in negative electrode [mol]	Total lithium in positive electrode [mol]	Loss of lithium inventory [%]	Loss of active material in negative electrode [%]
SEI_D25e22 =importdata("SEI_D2.5e-22.csv");
SEI_D25e21 =importdata("SEI_D2.5e-21.csv");
SEI_D75e21 =importdata("SEI_D7.5e-21.csv");
SEI_D125e20 =importdata("SEI_D1.25e-20.csv");

% plots porosity
figure('Name','Porosity')
ploot(time, porosity_D25e22_dande.data(1,2:end),'*b','', 'Time [Min]','')
ploot(time, porosity_D25e21_dande.data(1,2:end),'*r','', 'Time [Min]','')
ploot(time, porosity_D75e21_dande.data(1,2:end),'*m','', 'Time [Min]','')
ploot(time, porosity_D125e20_dande.data(1,2:end),'*k','', 'Time [Min]','')

ploot(SEI_D25e22.data(:,1)*60, p_D25e22(1,:),'b','', 'Time [Min]','')
ploot(SEI_D25e21.data(:,1)*60, p_D25e21(1,:),'r','', 'Time [Min]','')
ploot(SEI_D75e21.data(:,1)*60, p_D75e21(1,:),'m','', 'Time [Min]','')
ploot(SEI_D125e20.data(:,1)*60, p_D125e20(1,:),'k','', 'Time [Min]','')
legend('DandeLiion: D25e22', 'DandeLiion: D25e21','DandeLiion: D75e21','DandeLiion: D125e20','Pybamm D25e22','Pybamm D25e21','Pybamm D75e21','Pybamm D125e20')



% plots SEI Thickness
figure('Name','SEI Thickness')
ploot(time, LSEI_D25e22_dande.data(1,2:end),'*b','', 'Time [Min]','')
ploot(time, LSEI_D25e21_dande.data(1,2:end),'*r','', 'Time [Min]','')
ploot(time, LSEI_D75e21_dande.data(1,2:end),'*m','', 'Time [Min]','')
ploot(time, LSEI_D125e20_dande.data(1,2:end),'*k','', 'Time [Min]','')

ploot(SEI_D25e22.data(:,1)*60, LSEI_D25e22(1,:),'b','', 'Time [Min]','')
ploot(SEI_D25e21.data(:,1)*60, LSEI_D25e21(1,:),'r','', 'Time [Min]','')
ploot(SEI_D75e21.data(:,1)*60, LSEI_D75e21(1,:),'m','', 'Time [Min]','')
ploot(SEI_D125e20.data(:,1)*60, LSEI_D125e20(1,:),'k','', 'Time [Min]','')
legend('DandeLiion: D25e22', 'DandeLiion: D25e21','DandeLiion: D75e21','DandeLiion: D125e20','Pybamm D25e22','Pybamm D25e21','Pybamm D75e21','Pybamm D125e20')


figure('Name','Capacity')
ploot(cap_D25e22_dande.data(:,1),cap_D25e22_dande.data(:,2),'*b','', 'Time [s]','')
ploot(cap_D25e21_dande.data(:,1),cap_D25e21_dande.data(:,2),'*r','', 'Time [s]','')
ploot(cap_D75e21_dande.data(:,1),cap_D75e21_dande.data(:,2),'*m','', 'Time [s]','')
ploot(cap_D125e20_dande.data(:,1),cap_D125e20_dande.data(:,2),'*k','', 'Time [s]','Capacity [Ah]')

ploot(SEI_D25e22.data(:,1)*60, SEI_D25e22.data(:,8),'b','', 'Time [Min]','')
ploot(SEI_D25e21.data(:,1)*60, SEI_D25e21.data(:,8),'r','', 'Time [Min]','')
ploot(SEI_D75e21.data(:,1)*60, SEI_D75e21.data(:,8),'m','', 'Time [Min]','')
ploot(SEI_D125e20.data(:,1)*60, SEI_D125e20.data(:,8),'k','', 'Time [Min]','')
legend('DandeLiion: D25e22', 'DandeLiion: D25e21','DandeLiion: D75e21','DandeLiion: D125e20','Pybamm D25e22','Pybamm D25e21','Pybamm D75e21','Pybamm D125e20')

figure('Name','Discharge capacity')
ploot(SEI_D25e22.data(:,1)*60, SEI_D25e22.data(:,4),'b','', 'Time [Min]','')
ploot(SEI_D25e21.data(:,1)*60, SEI_D25e21.data(:,4),'r','', 'Time [Min]','')
ploot(SEI_D75e21.data(:,1)*60, SEI_D75e21.data(:,4),'m','', 'Time [Min]','')
ploot(SEI_D125e20.data(:,1)*60, SEI_D125e20.data(:,4),'k','', 'Time [Min]','')


figure('name','Voltage')
ploot(voltage_D125e20_dande.data(:,1), voltage_D125e20_dande.data(:,2),'*b','', 'Time [Min]','')
ploot(voltage_D75e21_dande.data(:,1), voltage_D75e21_dande.data(:,2),'*r','', 'Time [Min]','')
ploot(voltage_D25e21_dande.data(:,1), voltage_D25e21_dande.data(:,2),'*m','', 'Time [Min]','')
ploot(voltage_D25e22_dande.data(:,1), voltage_D25e22_dande.data(:,2),'*k','', 'Time [Min]','')


ploot(SEI_D25e22.data(:,1)*60, SEI_D25e22.data(:,3),'b','', 'Time [Min]','')
ploot(SEI_D25e21.data(:,1)*60, SEI_D25e21.data(:,3),'r','', 'Time [Min]','')
ploot(SEI_D75e21.data(:,1)*60, SEI_D75e21.data(:,3),'m','', 'Time [Min]','')
ploot(SEI_D125e20.data(:,1)*60, SEI_D125e20.data(:,3),'k','', 'Time [Min]','')
legend('DandeLiion: D25e22', 'DandeLiion: D25e21','DandeLiion: D75e21','DandeLiion: D125e20','Pybamm D25e22','Pybamm D25e21','Pybamm D75e21','Pybamm D125e20')

