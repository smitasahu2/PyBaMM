clear 
format long
close all
%============================ Loading pybamm data =========================
voltage_dande = importdata( 'build/total_voltage.dat');% Total voltage
time = [0, 100,200,400,800,1000,1200,1400,1600,2000, 2100,2200,2300,2400,2500,3600,3660,4000,4100, 4200,4400,4800,4900,5000,5100,5200,5300,5400,5500,5600,5700,5800,5900,6000,6090];
%**************************************************************************
%============================ Loading pybamm data =========================
figure('Name','Pybamm and DandeLiion comparison')
% ̣%colororder({'k',"r","m","b"})% plots porosity
subplot(2,2,1)
plot(voltage_dande.data(:,1)/3600, voltage_dande.data(:,2),'-k','LineWidth',1.5,'MarkerSize',1);
hold on
for i =[2.5e-22, 2.5e-21,7.5e-21, 1.25e-20]
    SEI =    importdata(['on_SEI_D' num2str(i) '.csv']) ;
    plot(SEI.data(:,1)/60, SEI.data(:,3),'-x','LineWidth',1.5,'MarkerSize',1,'DisplayName', ['D=' num2str(i)]);
    clear
end
hold on
xlabel('Time [hrs]','Interpreter','latex','fontsize',12);
ylabel('V [V]','Interpreter','latex','fontsize',12);
hold on
legend('DandeLiion','D$_{sol}$ = 2.5e-22', 'D$_{sol}$ = 2.5e-21','D$_{sol}$ = 7.5e-21','D$_{sol}$ =  1.25e-20','Interpreter','latex','fontsize',10,'location','best');


subplot(2,2,2)
% ̣%colororder({'k',"r","m","b"})% plots porosity
% Total capacity
%============================ Loading pybamm data =========================
cap_dande = importdata( 'build/capacity.dat');% Total capacity
time = [0, 100,200,400,800,1000,1200,1400,1600,2000, 2100,2200,2300,2400,2500,3600,3660,4000,4100, 4200,4400,4800,4900,5000,5100,5200,5300,5400,5500,5600,5700,5800,5900,6000,6090];
%**************************************************************************

hold on
for i =[2.5e-22, 2.5e-21,7.5e-21, 1.25e-20]
    SEI =    importdata(['on_SEI_D' num2str(i) '.csv']) ;
    plot(SEI.data(:,1)/60,SEI.data(:,8),'-x','LineWidth',1.5,'MarkerSize',1,'DisplayName', ['i=' num2str(i)]);
    clear
end
xlabel('Time [hrs]','Interpreter','latex','fontsize',12);
ylabel('Capacity [mAh]','Interpreter','latex','fontsize',12);
legend('D$_{sol}$ = 2.5e-22', 'D$_{sol}$ = 2.5e-21','D$_{sol}$ = 7.5e-21','D$_{sol}$ =  1.25e-20','Interpreter','latex','fontsize',10,'location','best');

subplot(2,2,3)
%============================ Loading pybamm data =========================
LSEI_dande = importdata( 'build/SEI_thickness.dat');% SEI thickness
time = [0, 100,200,400,800,1000,1200,1400,1600,2000, 2100,2200,2300,2400,2500,3600,3660,4000,4100, 4200,4400,4800,4900,5000,5100,5200,5300,5400,5500,5600,5700,5800,5900,6000,6090];
%**************************************************************************

hold on
ploot(time/3600, LSEI_dande.data(1,2:end)/1e-9,'-k',' Anode', 'Time [Min]','Thickness of SEI [m]')
hold on
for i =[2.5e-22, 2.5e-21,7.5e-21, 1.25e-20]
   SEI =    importdata(['on_SEI_D' num2str(i) '.csv']) ;
    LSEI =    importdata(['on_Lon_SEI_D' num2str(i) '.csv']) ;
     plot(SEI.data(:,1)/60, LSEI(1,:)/1e-9,'-x','LineWidth',1.5,'MarkerSize',1,'DisplayName', ['i=' num2str(i)]);
    clear
end
xlabel('Time [hrs]','Interpreter','latex','fontsize',12);
ylabel('Thickness of SEI [nanometer]','Interpreter','latex','fontsize',12);
legend('DandeLiion','D$_{sol}$ = 2.5e-22', 'D$_{sol}$ = 2.5e-21','D$_{sol}$ = 7.5e-21','D$_{sol}$ =  1.25e-20','Interpreter','latex','fontsize',10,'location','best');

subplot(2,2,4)
%============================ Loading pybamm data =========================
porosity_dande = importdata( 'build/porosity_liquid.dat'); % Porosity
time = [0, 100,200,400,800,1000,1200,1400,1600,2000, 2100,2200,2300,2400,2500,3600,3660,4000,4100, 4200,4400,4800,4900,5000,5100,5200,5300,5400,5500,5600,5700,5800,5900,6000,6090];
%**************************************************************************

ploot(time/3600, porosity_dande.data(1,2:end),'-k',' Anode', 'Time [Min]','Porosity')
hold on
for i =[2.5e-22, 2.5e-21,7.5e-21, 1.25e-20]
    SEI =    importdata(['on_SEI_D' num2str(i) '.csv']) ;
    por_SEI =    importdata(['on_porosity_D' num2str(i) '.csv']) ;
    plot(SEI.data(:,1)/60, por_SEI(1,:),'-x','LineWidth',1.5,'MarkerSize',1,'DisplayName', ['i=' num2str(i)]);
    clear
end
xlabel('Time [hrs]','Interpreter','latex','fontsize',12);
ylabel('Porosity in Anode','Interpreter','latex','fontsize',12);
legend('DandeLiion','D$_{sol}$ = 2.5e-22', 'D$_{sol}$ = 2.5e-21','D$_{sol}$ = 7.5e-21','D$_{sol}$ =  1.25e-20','Interpreter','latex','fontsize',10,'location','best');

