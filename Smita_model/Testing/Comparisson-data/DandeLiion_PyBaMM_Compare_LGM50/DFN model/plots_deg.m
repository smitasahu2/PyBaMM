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
vd = importdata('total_voltaged.dat');
id = importdata('total_current_estimatedd.dat');
v_new = importdata('total_voltage_new.dat');
i_new = importdata('total_current_estimated_new.dat');

subplot(1,2,1)
colororder({'b','k'})
yyaxis left
ploot(time_data, Voltage_data,'k','CV: Hold 4.2V and 4 hours rest', 'Time [Min]','Voltage [V]')
hold on
ploot(vv.data(:,1), vv.data(:,2),'r','', 'Time [s]','Voltage [V]')
hold on 
ploot(vd.data(:,1), vd.data(:,2),'b','', 'Time [s]','Voltage [V]')
hold on 
ploot(v_new.data(:,1), v_new.data(:,2),'g','', 'Time [s]','Voltage [V]')
subtitle('1C c-rate')
legend('PyBaMM', 'Master','Deg', 'Deg ctol')
return
yyaxis right
ploot(time_data,- Current_data,'k','', 'Time [s]','Voltage [V]')
hold on 
ploot(ii.data(:,1), ii.data(:,2),'k','1C c-rate ', 'Time [s]','Current [A]')
hold on 
ploot(id.data(:,1), id.data(:,2),'k',' ', 'Time [s]','Current [A]')
hold on 
hold on 
ploot(i_new.data(:,1), i_new.data(:,2),'k',' ', 'Time [s]','Current [A]')
hold on 
subtitle('1C c-rate')
legend('PyBaMM', 'Master','Deg', 'Deg ctol')
return
Data1=importdata("DFNby2.csv");
Data=Data1.data;
time_data=Data(:,1); %units: seconds
Voltage_data=Data(:,3) ; % units: Volts
Current_data=Data(:,2) ; %units: Amps
vv = importdata('total_voltageby2.dat');
ii = importdata('total_currentby2.dat');
vd = importdata('total_voltage05d.dat');
id = importdata('total_current_estimated05d.dat');

subplot(1,2,2)
colororder({'b','k'})
yyaxis left
ploot(time_data, Voltage_data,'k','', 'Time [Min]','Voltage [V]')
hold on
ploot(vv.data(:,1), vv.data(:,2),'r','', 'Time [s]','Voltage [V]')
ploot(vd.data(:,1), vd.data(:,2),'b','', 'Time [s]','Voltage [V]')

yyaxis right
ploot(time_data,- Current_data,'k','', 'Time [s]','Current [A]')
hold on 
ploot(ii.data(:,1), ii.data(:,2),'r',' ', 'Time [s]','Current [A]')
hold on 
ploot(id.data(:,1), id.data(:,2),'b',' ', 'Time [s]','Current [A]')
subtitle('C/2 c-rate')
legend('PyBaMM', 'Master','Deg')
saveas(gcf,'v1', 'pdf')
 





%%%%%%%%%
figure('Name','Voltage2')
subplot(1,2,1)
Data1=importdata("DFN15.csv");
Data=Data1.data;
time_data=Data(:,1); %units: seconds
Voltage_data=Data(:,3) ; % units: Volts
Current_data=Data(:,2) ; %units: Amps
vv = importdata('total_voltage15.dat');
ii = importdata('total_current15.dat');
vd = importdata('total_voltage75d.dat');
id = importdata('total_current_estimated75d.dat');

colororder({'b','k'})
yyaxis left
ploot(time_data, Voltage_data,'k','', 'Time [Min]','Voltage [V]')
hold on
ploot(vv.data(:,1), vv.data(:,2),'r','', 'Time [s]','Voltage [V]')
ploot(vd.data(:,1), vd.data(:,2),'b','', 'Time [s]','Voltage [V]')

yyaxis right
ploot(time_data,- Current_data,'k','', 'Time [s]',' ')
hold on 
ploot(ii.data(:,1), ii.data(:,2),'r',' ', 'Time [s]','Current [A]')
hold on 
ploot(id.data(:,1), id.data(:,2),'b',' ', 'Time [s]','Current [A]')

subtitle('1.5C c-rate')
legend('PyBaMM', 'Master','Deg')

Data1=importdata("DFN2c.csv");
Data=Data1.data;
time_data=Data(:,1); %units: seconds
Voltage_data=Data(:,3) ; % units: Volts
Current_data=Data(:,2) ; %units: Amps
vv = importdata('total_voltage2c.dat');
ii = importdata('total_current2c.dat'); 

vd = importdata('total_voltage2d.dat');
id = importdata('total_current_estimated2d.dat');

subplot(1,2,2)

colororder({'b','k'})
yyaxis left
ploot(time_data, Voltage_data,'k','', 'Time [Min]','Voltage [V]')
hold on
ploot(vv.data(:,1), vv.data(:,2),'r','', 'Time [s]','Voltage [V]')
ploot(vd.data(:,1), vd.data(:,2),'b','', 'Time [s]','Voltage [V]')

yyaxis right
ploot(time_data,- Current_data,'k','', 'Time [s]',' ')
hold on 
ploot(ii.data(:,1), ii.data(:,2),'r',' ', 'Time [s]','Current [A]')
hold on 
ploot(id.data(:,1), id.data(:,2),'b',' ', 'Time [s]','Current [A]')
subtitle('2C c-rate')
legend('PyBaMM', 'Master','Deg')
saveas(gcf,'v2', 'pdf')


figure('Name','Voltage3')

subplot(1,2,1)
Data1=importdata("DFN3c.csv");
Data=Data1.data;
time_data=Data(:,1); %units: seconds
Voltage_data=Data(:,3) ; % units: Volts
Current_data=Data(:,2) ; %units: Amps
vv = importdata('total_voltage3c.dat');
ii = importdata('total_current3c.dat'); 
vd = importdata('total_voltage3d.dat');
id = importdata('total_current_estimated3d.dat');
colororder({'b','k'})
yyaxis left
ploot(time_data, Voltage_data,'k','', 'Time [Min]','Voltage [V]')
hold on
ploot(vv.data(:,1), vv.data(:,2),'r','', 'Time [s]','Voltage [V]')
ploot(vd.data(:,1), vd.data(:,2),'b','', 'Time [s]','Voltage [V]')

yyaxis right
ploot(time_data,- Current_data,'k','', 'Time [s]',' ')
hold on 
ploot(ii.data(:,1), ii.data(:,2),'r',' ', 'Time [s]','Current [A]')
hold on 
ploot(id.data(:,1), id.data(:,2),'b',' ', 'Time [s]','Current [A]')
subtitle('3C c-rate')
legend('PyBaMM', 'Master','Deg')
subplot(1,2,2)
Data1=importdata("DFN4c.csv");
Data=Data1.data;
time_data=Data(:,1); %units: seconds
Voltage_data=Data(:,3) ; % units: Volts
Current_data=Data(:,2) ; %units: Amps
vv = importdata('total_voltage4c.dat');
ii = importdata('total_current4c.dat');
vd = importdata('total_voltage4d.dat');
id = importdata('total_current_estimated4d.dat');
colororder({'b','k'})
yyaxis left
ploot(time_data, Voltage_data,'k','', 'Time [Min]','Voltage [V]')
hold on
ploot(vv.data(:,1), vv.data(:,2),'r','', 'Time [s]','Voltage [V]')
ploot(vd.data(:,1), vd.data(:,2),'b','', 'Time [s]','Voltage [V]')

yyaxis right
ploot(time_data,- Current_data,'k','', 'Time [s]',' ')
hold on 
ploot(ii.data(:,1), ii.data(:,2),'r',' ', 'Time [s]','Current [A]')
hold on 
ploot(id.data(:,1), id.data(:,2),'b',' ', 'Time [s]','Current [A]')
subtitle('4C c-rate')

legend('PyBaMM', 'Master','Deg')
saveas(gcf,'v3', 'pdf')
 


figure('Name','Voltage4')
subplot(1,2,1)
Data1=importdata("DFNby10.csv");
Data=Data1.data;
time_data=Data(:,1); %units: seconds
Voltage_data=Data(:,3) ; % units: Volts
Current_data=Data(:,2) ; %units: Amps
vv = importdata('total_voltageby10.dat');
ii = importdata('total_currentby10.dat');
vd = importdata('total_voltageby10d.dat');
id = importdata('total_current_estimatedby10d.dat');
colororder({'b','k'})
yyaxis left
ploot(time_data, Voltage_data,'k','', 'Time [Min]','Voltage [V]')
hold on
ploot(vv.data(:,1), vv.data(:,2),'r','', 'Time [s]','Voltage [V]')
ploot(vd.data(:,1), vd.data(:,2),'b','', 'Time [s]','Voltage [V]')

yyaxis right
ploot(time_data,- Current_data,'k','', 'Time [s]',' ')
hold on 
ploot(ii.data(:,1), ii.data(:,2),'r',' ', 'Time [s]','Current [A]')
hold on 
ploot(id.data(:,1), id.data(:,2),'b',' ', 'Time [s]','Current [A]')
subtitle('C/10 c-rate')
legend('PyBaMM', 'Master','Deg')


subplot(1,2,2)

Data1=importdata("DFN100.csv");
Data=Data1.data;
time_data=Data(:,1); %units: seconds
Voltage_data=Data(:,3) ; % units: Volts
Current_data=Data(:,2) ; %units: Amps
vv = importdata('total_voltage100.dat');
ii = importdata('total_current100.dat');
vd = importdata('total_voltage100d.dat');
id = importdata('total_current_estimated100d.dat');
colororder({'b','k'})
yyaxis left
ploot(time_data, Voltage_data,'k','', 'Time [Min]','Voltage [V]')
hold on
ploot(vv.data(:,1), vv.data(:,2),'r','', 'Time [s]','Voltage [V]')
ploot(vd.data(:,1), vd.data(:,2),'b','', 'Time [s]','Voltage [V]')

yyaxis right
ploot(time_data,- Current_data,'k','', 'Time [s]',' ')
hold on 
ploot(ii.data(:,1), ii.data(:,2),'r',' ', 'Time [s]','Current [A]')
hold on 
ploot(id.data(:,1), id.data(:,2),'b',' ', 'Time [s]','Current [A]')
subtitle('C/100 c-rate')
legend('PyBaMM', 'Master','Deg')
saveas(gcf,'v4', 'pdf')










