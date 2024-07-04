clear 
format long
close all
%**************************************************************************
%============================ Loading pybamm data =========================
%**************************************************************************

% % Porosity
% LSEI_D25e22  = importdata("LSEI_D2.5e-22.csv");
% % Time [min]	Current [A]	Terminal voltage [V]	Discharge capacity [A.h]	Loss of capacity to SEI [A.h]	Negative electrode capacity [A.h]	Positive electrode capacity [A.h]	Throughput capacity [A.h]	Total capacity lost to side reactions [A.h]	Total lithium capacity [A.h]	Loss of lithium to SEI [mol]	Total lithium in negative electrode [mol]	Total lithium in positive electrode [mol]	Loss of lithium inventory [%]	Loss of active material in negative electrode [%]
% SEI_D25e22 =importdata("SEI_D2.5e-22.csv");
% % colororder({'k',"#D95319","#0072BD","#7E2F8E",'k',"#D95319","#0072BD","#7E2F8E"})% plots porosity
% figure('Name','Porosity')
% subplot(1,2,1)
% ploot(SEI_D25e22.data(:,1)*60, LSEI_D25e22(1,:),'b','pybamm', 'Time [Min]','SEI Thickness')
% subplot(1,2,2)
% ploot(SEI_D25e22.data(:,1)*60, SEI_D25e22.data(:,3),'b','pybamm',' Time [Min]','')

figure('Name','Pybamm plots')
% ̣%colororder({'k',"r","m","b"})% plots porosity
subplot(2,2,1)
hold on
for i =[2.5e-22, 2.5e-21,7.5e-21, 1.25e-20]
    SEI =    importdata(['on_SEI_D' num2str(i) '.csv']) ;
    plot(SEI.data(:,1)/60, SEI.data(:,3),'-x','LineWidth',1.5,'MarkerSize',1,'DisplayName', ['D=' num2str(i)]);
    clear
end
xlabel('Time [hrs]','Interpreter','latex','fontsize',12);
ylabel('V [V]','Interpreter','latex','fontsize',12);
legend('D$_{sol}$ = 2.5e-22', 'D$_{sol}$ = 2.5e-21','D$_{sol}$ = 7.5e-21','D$_{sol}$ =  1.25e-20','Interpreter','latex','fontsize',10,'location','best');
subplot(2,2,2)
% ̣%colororder({'k',"r","m","b"})% plots porosity
% Total capacity
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
hold on
for i =[2.5e-22, 2.5e-21,7.5e-21, 1.25e-20]
   SEI =    importdata(['on_SEI_D' num2str(i) '.csv']) ;
    LSEI =    importdata(['on_Lon_SEI_D' num2str(i) '.csv']) ;
     plot(SEI.data(:,1)/60, LSEI(1,:)/1e-9,'-x','LineWidth',1.5,'MarkerSize',1,'DisplayName', ['i=' num2str(i)]);
    clear
end
xlabel('Time [hrs]','Interpreter','latex','fontsize',12);
ylabel('Thickness of SEI [nanometer]','Interpreter','latex','fontsize',12);
legend('D$_{sol}$ = 2.5e-22', 'D$_{sol}$ = 2.5e-21','D$_{sol}$ = 7.5e-21','D$_{sol}$ =  1.25e-20','Interpreter','latex','fontsize',10,'location','best');

subplot(2,2,4)

hold on
for i =[2.5e-22, 2.5e-21,7.5e-21, 1.25e-20]
    SEI =    importdata(['on_SEI_D' num2str(i) '.csv']) ;
    por_SEI =    importdata(['on_porosity_D' num2str(i) '.csv']) ;
    plot(SEI.data(:,1)/60, por_SEI(1,:),'-x','LineWidth',1.5,'MarkerSize',1,'DisplayName', ['i=' num2str(i)]);
    clear
end
xlabel('Time [hrs]','Interpreter','latex','fontsize',12);
ylabel('Porosity in Anode','Interpreter','latex','fontsize',12);
legend('D$_{sol}$ = 2.5e-22', 'D$_{sol}$ = 2.5e-21','D$_{sol}$ = 7.5e-21','D$_{sol}$ =  1.25e-20','Interpreter','latex','fontsize',10,'location','best');

