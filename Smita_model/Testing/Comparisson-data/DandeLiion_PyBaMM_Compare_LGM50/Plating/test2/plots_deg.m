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
% Porosity
porosity_dande2 = importdata( 'build2/porosity_liquid.dat');
% SEI thickness
LSEI_dande2 = importdata( 'build2/SEI_thickness.dat');
% Total capacity
cap_dande2 = importdata( 'build2/capacity.dat');
% Total voltage
voltage_dande2 = importdata( 'build2/total_voltage.dat');
% Li metal
C_metal_dande2 =  importdata( 'build2/concentrtion_Li_metal.dat'); 
% Dead Li metal
C_dead_dande2 = importdata( 'build2/concentrtion_dead_Li.dat');

% Porosity
porosity_dande3 = importdata( 'build3/porosity_liquid.dat');
% SEI thickness
LSEI_dande3 = importdata( 'build3/SEI_thickness.dat');
% Total capacity
cap_dande3 = importdata( 'build3/capacity.dat');
% Total voltage
voltage_dande3 = importdata( 'build3/total_voltage.dat');
% Li metal
C_metal_dande3 =  importdata( 'build3/concentrtion_Li_metal.dat'); 

% Dead Li metal
C_dead_dande3 = importdata( 'build3/concentrtion_dead_Li.dat');


time = [0, 100,200,400,800,1000,1200,1400,1600,2000, 2270];
time2 = [0, 100,200,400,800,1000,1200,1400,1580];
time3 = [0, 100,200,400,800,1000,1200,1290];

figure('Name','Porosity')
subplot(2,2,1)
ploot(time, porosity_dande.data(1,2:end),'b',' Anode', 'Time [Min]','Porosity')
ploot(time2, porosity_dande2.data(1,2:end),'r',' Anode', 'Time [Min]','Porosity')
ploot(time3, porosity_dande3.data(1,2:end),'m',' Anode', 'Time [Min]','Porosity')
legend('$T= 25^\circ$C','$T= 5^\circ$C','$T= 0^\circ$C','Interpreter','latex','fontsize',10);


subplot(2,2,2)
ploot(time, LSEI_dande.data(1,2:end),'b',' Anode', 'Time [Min]','Thickness of SEI [m]')
ploot(time2, LSEI_dande2.data(1,2:end),'r',' Anode', 'Time [Min]','Thickness of SEI [m]')
ploot(time3, LSEI_dande3.data(1,2:end),'m',' Anode', 'Time [Min]','Thickness of SEI [m]')
legend('$T= 25^\circ$C','$T= 5^\circ$C','$T= 0^\circ$C','Interpreter','latex','fontsize',10);

subplot(2,2,3)
ploot(cap_dande.data(:,1),cap_dande.data(:,2),'b',' Total', 'Time [s]','Capacity')
ploot(cap_dande2.data(:,1),cap_dande2.data(:,2),'r',' Total', 'Time [s]','Capacity')
ploot(cap_dande3.data(:,1),cap_dande3.data(:,2),'m',' Total', 'Time [s]','Capacity')
legend('$T= 25^\circ$C','$T= 5^\circ$C','$T= 0^\circ$C','Interpreter','latex','fontsize',10);


subplot(2,2,4)
ploot(voltage_dande.data(:,1), voltage_dande.data(:,2),'b','1C C-rate', 'Time [Min]','Voltage [V]')
ploot(voltage_dande2.data(:,1), voltage_dande2.data(:,2),'r','1C C-rate', 'Time [Min]','Voltage [V]')
ploot(voltage_dande3.data(:,1), voltage_dande3.data(:,2),'m','1C C-rate', 'Time [Min]','Voltage [V]')
legend('$T= 25^\circ$C','$T= 5^\circ$C','$T= 0^\circ$C','Interpreter','latex','fontsize',10);

figure(2)
subplot(2,2,1)
ploot(time, C_metal_dande.data(1,2:end),'b','at $x=0$', 'Time [Min]','plated Li-metal')
ploot(time2, C_metal_dande2.data(1,2:end),'r','at $x=0$', 'Time [Min]','plated Li-metal')
ploot(time3, C_metal_dande3.data(1,2:end),'m','at $x=0$', 'Time [Min]','plated Li-metal')
legend('$T= 25^\circ$C','$T= 5^\circ$C','$T= 0^\circ$C','Interpreter','latex','fontsize',10);

subplot(2,2,2)
ploot(time,C_dead_dande.data(1,2:end),'b','at $x=0$', 'Time [Min]','Dead Li')
ploot(time2,C_dead_dande2.data(1,2:end),'r','at $x=0$', 'Time [Min]','Dead Li')
ploot(time3,C_dead_dande3.data(1,2:end),'m','at $x=0$', 'Time [Min]','Dead Li')
legend('$T= 25^\circ$C','$T= 5^\circ$C','$T= 0^\circ$C','Interpreter','latex','fontsize',10);

subplot(2,2,3)
ploot(C_metal_dande.data(:,1), C_metal_dande.data(:,end),'b',' at $t=t_f$', '$x$ [m]','Li-metal')
ploot(C_metal_dande2.data(:,1), C_metal_dande2.data(:,end),'r',' at $t=t_f$', '$x$ [m]','Li-metal')
ploot(C_metal_dande3.data(:,1), C_metal_dande3.data(:,end),'m',' at $t=t_f$', '$x$ [m]','Li-metal')
legend('$T= 25^\circ$C','$T= 5^\circ$C','$T= 0^\circ$C','Interpreter','latex','fontsize',10);

subplot(2,2,4)
ploot(C_dead_dande.data(:,1), C_dead_dande.data(:,end),'b','at $t=t_f$ ', '$x$ [m]','Dead Li')
ploot(C_dead_dande2.data(:,1), C_dead_dande2.data(:,end),'r','at $t=t_f$ ', '$x$ [m]','Dead Li')
ploot(C_dead_dande3.data(:,1), C_dead_dande3.data(:,end),'m','at $t=t_f$ ', '$x$ [m]','Dead Li')
legend('$T= 25^\circ$C','$T= 5^\circ$C','$T= 0^\circ$C','Interpreter','latex','fontsize',10);
