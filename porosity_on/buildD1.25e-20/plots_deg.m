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

% time = [0, 100,200,400,800,1000,1200,1400,1600,2000, 2270];
time = [0, 100,200,400,800,1000,1200,1290];

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

