clear all;
figure(1)
%clf
fontsize_1=36;
fontsize_2=36;
linewidth=2;

XX=csvread('ID_VG_NCp90nm_Vdd_50mV.csv',219,1,'B219..D420');cc='c-';
XX=csvread('ID_VG_NCp90nm_Vdd_500mV.csv',219,1,'B219..D420');cc='r-';
 XX=csvread('ID_VG_NCp90nm_Vdd_900mV.csv',219,1,'B219..D420');cc='b-';


ccc='rybgkrkycm';
%XX(find(XX==0))=0/0;
V_G=XX(:,2);
I_D=XX(:,3);
I_G=XX(:,4);

N=length(V_G);
I_D_s=I_D;
V_G_s=V_G;

SS_ID_s=-diff(V_G_s)./diff(log10(abs(I_D_s)))*1e3;
SS_ID_s(length(I_D_s))=SS_ID_s(length(I_D_s)-1);

figure(1), semilogy(V_G_s, abs(I_D_s),cc, 'markersize', 12, 'linewidth', 2);hold on
set(figure(1), 'color', 'white');
set(gca,  'fontsize', fontsize_1);
ylabel('I_D (\muA/\mum)', 'fontsize', fontsize_2);
xlabel('V_G (V)', 'fontsize', fontsize_2);
% ylim([1e-12 1e-1])
% xlim([-6 3])
%set(gca, 'YTick', [1e-9 1e-6 1e-3  1 1e1 1e2 1e3 1e4 1e5])
% figure(3), plot(V_G_s, abs(I_D_s)*1e6, cc);hold on
% set(figure(3), 'color', 'white');
% set(gca,  'fontsize', fontsize_1);
% ylabel('I_D (\mu A)', 'fontsize', fontsize_2);
% xlabel('V_G (V)', 'fontsize', fontsize_2);


%figure(1), semilogy(V_G_s, abs(I_G)*1e6, 'r');hold on

%
% figure(2), semilogx( abs(I_D_s), SS_ID_s+8, cc, abs(I_D_s), 60*ones(1, length(I_D_s)));hold on
% set(figure(2), 'color', 'white');
% ylim([0 200]);
% set(gca,  'fontsize', fontsize_1);
% xlabel('I_D (A)', 'fontsize', fontsize_2);
% ylabel('SS (mV/dec)', 'fontsize', fontsize_2);
%   xlim([2e-10 2e-5])
% ylim([0 120]);

