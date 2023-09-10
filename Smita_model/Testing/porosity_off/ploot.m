function ploot(x,y,colourstr,legendstr, xlabelstr,ylabelstr)
% ploot(x,y,colourstr,legendstr, xlabelstr,ylabelstr)
plot(x,y,colourstr,'LineWidth',1)
hold on
legend (legendstr,'location','best','fontsize',10);
grid on
a = get(gca,'XTickLabel'); 
set(gca, 'FontName', 'Times New Roman','fontsize',10)
set(gca,'XTickLabel',a,'fontsize',10)
set(gca,'XTickLabelMode','auto')
xlabel(xlabelstr, 'Interpreter','latex','fontsize',10);
ylabel(ylabelstr, 'Interpreter','latex','fontsize',10);
% ylim('auto')
axis padded

% saveas(gcf,'order_c', 'epsc2')

end