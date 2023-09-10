clear 
format long
close all

%voltage 
voltage_dande_1 = importdata( 'buildD2.5e-22/total_voltage.dat');
voltage_dande_2 = importdata( 'buildD2.5e-21/total_voltage.dat');
voltage_dande_3= importdata( 'buildD7.5e-21/total_voltage.dat');
voltage_dande_4 = importdata( 'buildD1.25e-20/total_voltage.dat');
time = [0, 100,200,400,800,1000,1200,1400,1600,2000, 2100,2200,2300,2400,2500,3600,3660,4000,4100, 4200,4400,4800,4900,5000,5100,5200,5300,5400,5500,5600,5700,5800,5900,6000,6090]/3600;


figure('Name','Voltage')
ploot(voltage_dande_1.data(:,1)/3600, voltage_dande_1.data(:,2),'b',' Anode', 'Time [Min]','Porosity');hold on
ploot(voltage_dande_2.data(:,1)/3600, voltage_dande_2.data(:,2),'r',' Anode', 'Time [Min]','Porosity');hold on
ploot(voltage_dande_3.data(:,1)/3600, voltage_dande_3.data(:,2),'k',' Anode', 'Time [Min]','Porosity');hold on
ploot(voltage_dande_4.data(:,1)/3600, voltage_dande_4.data(:,2),'m',' Anode', 'Time [Min]','Voltage')
hold on
for i =[2.5e-22, 2.5e-21,7.5e-21, 1.25e-20]
    SEI =    importdata(['SEI_D' num2str(i) '.csv']) ;
    plot(SEI.data(:,1)/60, SEI.data(:,3),'-x','LineWidth',1.5,'MarkerSize',1,'DisplayName', ['D=' num2str(i)]);
    clear
end
hold on
xlabel('Time [hrs]','Interpreter','latex','fontsize',12);
ylabel('V [V]','Interpreter','latex','fontsize',12);
hold on
legend('DandeLiion D$_{sol}$ = 2.5e-22', ' DandeLiion D$_{sol}$ = 2.5e-21',' DandeLiion D$_{sol}$ = 7.5e-21','DandeLiion D$_{sol}$ =  1.25e-20',...
    'pybamm D$_{sol}$ = 2.5e-22', 'pybamm D$_{sol}$ = 2.5e-21','pybamm D$_{sol}$ = 7.5e-21','pybamm D$_{sol}$ =  1.25e-20',...
    'Interpreter','latex','fontsize',10,'location','best');


clear
LSEI_dande_1 = importdata( 'buildD2.5e-22/SEI_thickness.dat');
LSEI_dande_2 = importdata( 'buildD2.5e-21/SEI_thickness.dat');
LSEI_dande_3= importdata( 'buildD7.5e-21/SEI_thickness.dat');
LSEI_dande_4 = importdata( 'buildD1.25e-20/SEI_thickness.dat');
time = [0, 100,200,400,800,1000,1200,1400,1600,2000, 2100,2200,2300,2400,2500,3600,3660,4000,4100, 4200,4400,4800,4900,5000,5100,5200,5300,5400,5500,5600,5700,5800,5900,6000,6090]/3600;
figure('Name', 'SEI thickness')
ploot(time, LSEI_dande_1.data(1,2:end)/1e-9,'*b',' Anode', 'Time [Min]','Porosity');hold on
ploot(time, LSEI_dande_2.data(1,2:end)/1e-9,'*r',' Anode', 'Time [Min]','Porosity');hold on
ploot(time, LSEI_dande_3.data(1,2:end)/1e-9,'*k',' Anode', 'Time [Min]','Porosity');hold on
ploot(time, LSEI_dande_4.data(1,2:end)/1e-9,'*m',' Anode', 'Time [Min]','SEI Thickness')
hold on
for i =[2.5e-22, 2.5e-21,7.5e-21, 1.25e-20]
   SEI =    importdata(['SEI_D' num2str(i) '.csv']) ;
    LSEI =    importdata(['LSEI_D' num2str(i) '.csv']) ;
     plot(SEI.data(:,1)/60, LSEI(1,:)/1e-9,'-x','LineWidth',1.5,'MarkerSize',1,'DisplayName', ['i=' num2str(i)]);
    clear
end
xlabel('Time [hrs]','Interpreter','latex','fontsize',12);
ylabel('Thickness of SEI [nanometer]','Interpreter','latex','fontsize',12);
legend('DandeLiion D$_{sol}$ = 2.5e-22', ' DandeLiion D$_{sol}$ = 2.5e-21',' DandeLiion D$_{sol}$ = 7.5e-21','DandeLiion D$_{sol}$ =  1.25e-20',...
    'pybamm D$_{sol}$ = 2.5e-22', 'pybamm D$_{sol}$ = 2.5e-21','pybamm D$_{sol}$ = 7.5e-21','pybamm D$_{sol}$ =  1.25e-20',...
    'Interpreter','latex','fontsize',10,'location','best');
clear
%capacity
cap_dande_1 = importdata( 'buildD2.5e-22/capacity.dat');
cap_dande_2 = importdata( 'buildD2.5e-21/capacity.dat');
cap_dande_3= importdata( 'buildD7.5e-21/capacity.dat');
cap_dande_4 = importdata( 'buildD1.25e-20/capacity.dat');

figure('Name','Capacity')
ploot(cap_dande_1.data(:,1)/3600,cap_dande_1.data(:,2),'b',' Total', 'Time [s]','Capacity'); hold on;
ploot(cap_dande_2.data(:,1)/3600,cap_dande_2.data(:,2),'r',' Total', 'Time [s]','Capacity'); hold on;
ploot(cap_dande_3.data(:,1)/3600,cap_dande_3.data(:,2),'k',' Total', 'Time [s]','Capacity'); hold on;
ploot(cap_dande_4.data(:,1)/3600,cap_dande_4.data(:,2),'m',' Total', 'Time [s]','Capacity')
time = [0, 100,200,400,800,1000,1200,1400,1600,2000, 2100,2200,2300,2400,2500,3600,3660,4000,4100, 4200,4400,4800,4900,5000,5100,5200,5300,5400,5500,5600,5700,5800,5900,6000,6090];
%**************************************************************************
hold on
for i =[2.5e-22, 2.5e-21,7.5e-21, 1.25e-20]
    SEI =    importdata(['SEI_D' num2str(i) '.csv']) ;
    plot(SEI.data(:,1)/60,SEI.data(:,8),'-x','LineWidth',1.5,'MarkerSize',1,'DisplayName', ['i=' num2str(i)]);
    clear
end
xlabel('Time [hrs]','Interpreter','latex','fontsize',12);
ylabel('Capacity [mAh]','Interpreter','latex','fontsize',12);
legend('DandeLiion D$_{sol}$ = 2.5e-22', ' DandeLiion D$_{sol}$ = 2.5e-21',' DandeLiion D$_{sol}$ = 7.5e-21','DandeLiion D$_{sol}$ =  1.25e-20',...
    'pybamm D$_{sol}$ = 2.5e-22', 'pybamm D$_{sol}$ = 2.5e-21','pybamm D$_{sol}$ = 7.5e-21','pybamm D$_{sol}$ =  1.25e-20',...
    'Interpreter','latex','fontsize',10,'location','best');
clear
time = [0, 100,200,400,800,1000,1200,1400,1600,2000, 2100,2200,2300,2400,2500,3600,3660,4000,4100, 4200,4400,4800,4900,5000,5100,5200,5300,5400,5500,5600,5700,5800,5900,6000,6090]/3600;
%**************************************************************************

% Porosity
porosity_1 = importdata( 'buildD2.5e-22/porosity_liquid.dat');
porosity_2 = importdata( 'buildD2.5e-21/porosity_liquid.dat');
porosity_3= importdata( 'buildD7.5e-21/porosity_liquid.dat');
porosity_4 = importdata( 'buildD1.25e-20/porosity_liquid.dat');
figure('Name','Porosity')
ploot(time, porosity_1.data(1,2:end),'b',' Anode', 'Time [Min]','Porosity');hold on
ploot(time, porosity_2.data(1,2:end),'r',' Anode', 'Time [Min]','Porosity');hold on
ploot(time, porosity_3.data(1,2:end),'k',' Anode', 'Time [Min]','Porosity');hold on
ploot(time, porosity_4.data(1,2:end),'m',' Anode', 'Time [Min]','Porosity'); hold on;
for i =[2.5e-22, 2.5e-21,7.5e-21, 1.25e-20]
    SEI =    importdata(['SEI_D' num2str(i) '.csv']) ;
    por_SEI =    importdata(['porosity_D' num2str(i) '.csv']) ;
    plot(SEI.data(:,1)/60, por_SEI(1,:),'-x','LineWidth',1.5,'MarkerSize',1,'DisplayName', ['i=' num2str(i)]);
    clear
end
xlabel('Time [hrs]','Interpreter','latex','fontsize',12);
ylabel('Porosity in Anode','Interpreter','latex','fontsize',12);
legend('DandeLiion D$_{sol}$ = 2.5e-22', ' DandeLiion D$_{sol}$ = 2.5e-21',' DandeLiion D$_{sol}$ = 7.5e-21','DandeLiion D$_{sol}$ =  1.25e-20',...
    'pybamm D$_{sol}$ = 2.5e-22', 'pybamm D$_{sol}$ = 2.5e-21','pybamm D$_{sol}$ = 7.5e-21','pybamm D$_{sol}$ =  1.25e-20',...
    'Interpreter','latex','fontsize',10,'location','best');



% figure(100)
% voltage_dande_1 = importdata( 'buildD2.5e-22/total_voltage.dat');

% ploot(voltage_dande_1.data(:,1)/3600, voltage_dande_1.data(:,2),'b',' Anode', 'Time [Min]','');hold on
% hold on
% for i =[2.5e-22]%, 2.5e-21,7.5e-21, 1.25e-20]
%     SEI =    importdata(['SEI_D' num2str(i) '.csv']) ;
%     plot(SEI.data(:,1)/60, SEI.data(:,3),'-x','LineWidth',1.5,'MarkerSize',1,'DisplayName', ['D=' num2str(i)]);
%     clear
% end
% hold on
% xlabel('Time [hrs]','Interpreter','latex','fontsize',12);
% ylabel('V [V]','Interpreter','latex','fontsize',12);
% hold on
% legend('DandeLiion D$_{sol}$ = 2.5e-22', 'pybamm D$_{sol}$ = 2.5e-22',...
%     'Interpreter','latex','fontsize',10,'location','best');


