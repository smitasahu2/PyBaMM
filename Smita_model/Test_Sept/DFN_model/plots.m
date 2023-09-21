clear 
close all
figure('Name','Voltage1')
Data1=importdata("DFN1c.csv");
Data=Data1.data;
time_data=Data(:,1); %units: seconds
Voltage_data=Data(:,3) ; % units: Volts
Current_data=Data(:,2) ; %units: Amps
vv = importdata('total_voltage1c.dat');
ii = importdata('total_current1c.dat');
subplot(1,2,1)
colororder({'b','k'})
yyaxis left
ploot(time_data, Voltage_data,'k','CV: Hold 4.2V and 4 hours rest', 'Time [Min]','Voltage [V]')
hold on
ploot(vv.data(:,1), vv.data(:,2),'r','', 'Time [s]','Voltage [V]')
yyaxis right
ploot(time_data,- Current_data,'k','', 'Time [s]','Voltage [V]')
hold on 
ploot(ii.data(:,1), ii.data(:,2),'r','1C c-rate ', 'Time [s]','Current [A]')
hold on 
subtitle('1C c-rate')
legend('PyBaMM', 'DandeLiion')
Data1=importdata("DFNby2.csv");
Data=Data1.data;
time_data=Data(:,1); %units: seconds
Voltage_data=Data(:,3) ; % units: Volts
Current_data=Data(:,2) ; %units: Amps
vv = importdata('total_voltageby2.dat');
ii = importdata('total_currentby2.dat');
subplot(1,2,2)
colororder({'b','k'})
yyaxis left
ploot(time_data, Voltage_data,'k','', 'Time [Min]','Voltage [V]')
hold on
ploot(vv.data(:,1), vv.data(:,2),'r','', 'Time [s]','Voltage [V]')
yyaxis right
ploot(time_data,- Current_data,'k','', 'Time [s]','Voltage [V]')
hold on 
ploot(ii.data(:,1), ii.data(:,2),'r',' ', 'Time [s]','Current [A]')
hold on 
subtitle('C/2 c-rate')
legend('PyBaMM', 'DandeLiion')
saveas(gcf,'v1', 'pdf')

%%%%%%%%%
figure('Name','Voltage2')
subplot(2,2,1)
Data1=importdata("DFN15.csv");
Data=Data1.data;
time_data=Data(:,1); %units: seconds
Voltage_data=Data(:,3) ; % units: Volts
Current_data=Data(:,2) ; %units: Amps
vv = importdata('total_voltage15.dat');
ii = importdata('total_current15.dat');
colororder({'b','k'})
yyaxis left
ploot(time_data, Voltage_data,'k','', 'Time [Min]','Voltage [V]')
hold on
ploot(vv.data(:,1), vv.data(:,2),'r','', 'Time [s]','Voltage [V]')
yyaxis right
ploot(time_data,- Current_data,'k','', 'Time [s]','Voltage [V]')
hold on 
ploot(ii.data(:,1), ii.data(:,2),'r',' ', 'Time [s]','Current [A]')
hold on 
subtitle('1.5C c-rate')
legend('PyBaMM', 'DandeLiion')

Data1=importdata("DFN2c.csv");
Data=Data1.data;
time_data=Data(:,1); %units: seconds
Voltage_data=Data(:,3) ; % units: Volts
Current_data=Data(:,2) ; %units: Amps
vv = importdata('total_voltage2c.dat');
ii = importdata('total_current2c.dat'); 
subplot(2,2,2)
colororder({'b','k'})
yyaxis left
ploot(time_data, Voltage_data,'k','', 'Time [Min]','Voltage [V]')
hold on
ploot(vv.data(:,1), vv.data(:,2),'r','', 'Time [s]','Voltage [V]')
yyaxis right
ploot(time_data,- Current_data,'k','', 'Time [s]','Voltage [V]')
hold on 
ploot(ii.data(:,1), ii.data(:,2),'r','', 'Time [s]','Current [A]')
hold on 
subtitle('2C c-rate')
legend('PyBaMM', 'DandeLiion')
subplot(2,2,3)
Data1=importdata("DFN3c.csv");
Data=Data1.data;
time_data=Data(:,1); %units: seconds
Voltage_data=Data(:,3) ; % units: Volts
Current_data=Data(:,2) ; %units: Amps
vv = importdata('total_voltage3c.dat');
ii = importdata('total_current3c.dat'); 
colororder({'b','k'})
yyaxis left
ploot(time_data, Voltage_data,'k','', 'Time [Min]','Voltage [V]')
hold on
ploot(vv.data(:,1), vv.data(:,2),'r','', 'Time [s]','Voltage [V]')
yyaxis right
ploot(time_data,- Current_data,'k','', 'Time [s]','Voltage [V]')
hold on 
ploot(ii.data(:,1), ii.data(:,2),'r',' ', 'Time [s]','Current [A]')
hold on 
subtitle('3C c-rate')
legend('PyBaMM', 'DandeLiion')
Data1=importdata("DFN4c.csv");
Data=Data1.data;
time_data=Data(:,1); %units: seconds
Voltage_data=Data(:,3) ; % units: Volts
Current_data=Data(:,2) ; %units: Amps
vv = importdata('total_voltage4c.dat');
ii = importdata('total_current4c.dat');
subplot(2,2,4)
colororder({'b','k'})
yyaxis left
ploot(time_data, Voltage_data,'k','', 'Time [Min]','Voltage [V]')
hold on
ploot(vv.data(:,1), vv.data(:,2),'r','', 'Time [s]','Voltage [V]')
yyaxis right
ploot(time_data,- Current_data,'k','', 'Time [s]','Voltage [V]')
hold on 
ploot(ii.data(:,1), ii.data(:,2),'r',' ', 'Time [s]','Current [A]')
hold on 
subtitle('4C c-rate')
legend('PyBaMM', 'DandeLiion')
saveas(gcf,'v2', 'pdf')




figure('Name','Voltage2')
Data1=importdata("DFNby10.csv");
Data=Data1.data;
time_data=Data(:,1); %units: seconds
Voltage_data=Data(:,3) ; % units: Volts
Current_data=Data(:,2) ; %units: Amps
vv = importdata('total_voltageby10.dat');
ii = importdata('total_currentby10.dat');  
subplot(1,2,1)
colororder({'b','k'})
yyaxis left
ploot(time_data, Voltage_data,'k','', 'Time [Min]','Voltage [V]')
hold on
ploot(vv.data(:,1), vv.data(:,2),'r','', 'Time [s]','Voltage [V]')
yyaxis right
ploot(time_data,- Current_data,'k','', 'Time [s]','Voltage [V]')
hold on 
ploot(ii.data(:,1), ii.data(:,2),'r','', 'Time [s]','Current [A]')
hold on 
subtitle('C/10 c-rate')
legend('PyBaMM', 'DandeLiion')

Data1=importdata("DFN100.csv");
Data=Data1.data;
time_data=Data(:,1); %units: seconds
Voltage_data=Data(:,3) ; % units: Volts
Current_data=Data(:,2) ; %units: Amps
vv = importdata('total_voltage100.dat');
ii = importdata('total_current100.dat');
subplot(1,2,2)
colororder({'b','k'})
yyaxis left
ploot(time_data, Voltage_data,'k','', 'Time [Min]','Voltage [V]')
hold on
ploot(vv.data(:,1), vv.data(:,2),'r','', 'Time [s]','Voltage [V]')
yyaxis right
ploot(time_data,- Current_data,'k','', 'Time [s]','Voltage [V]')
hold on 
ploot(ii.data(:,1), ii.data(:,2),'r',' ', 'Time [s]','Current [A]')
hold on 
subtitle('C/100 c-rate')
legend('PyBaMM', 'DandeLiion')
Data1=importdata("DFN100.csv");
Data=Data1.data;
time_data=Data(:,1); %units: seconds
Voltage_data=Data(:,3) ; % units: Volts
Current_data=Data(:,2) ; %units: Amps
vv = importdata('total_voltage100.dat');
ii = importdata('total_current100.dat');
subplot(1,2,2)
colororder({'b','k'})
yyaxis left
ploot(time_data, Voltage_data,'k','', 'Time [Min]','Voltage [V]')
hold on
ploot(vv.data(:,1), vv.data(:,2),'r','', 'Time [s]','Voltage [V]')
yyaxis right
ploot(time_data,- Current_data,'k','', 'Time [s]','Voltage [V]')
hold on 
ploot(ii.data(:,1), ii.data(:,2),'r',' ', 'Time [s]','Current [A]')
hold on 
subtitle('C/100 c-rate')
legend('PyBaMM', 'DandeLiion')
saveas(gcf,'v3', 'pdf')








