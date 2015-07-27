%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%Landau-Devonshire post-processor for Negative Capacitance FET
%Calculates the I_D-V_G characteristics of Negative Capacitance FET
%Written by Asif Khan, UC Berkeley
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clear all;
%close all;

%Base-line MOSFET dimensions
L=100e-9;           %Channel length (m)
W=1e-6;             %Width (m)

%Drain voltage
V_D=500;            %Drain voltage 

%Input file containing the I_D-V_G and Q-_V_G curves of the base-line
%MOSFET without the ferroelectric
file=['5e17_5A_', num2str(V_D), 'mV_100nm_27C.txt'];
X=dlmread(file);

%Fetching the characteristics of the Baseline MOSFET pre-simulated using TCAD
%Sentaurus (2-D electrostatics, drift-diffusion transport)
V_g=X(:,1); Q=X(:,2); I_D=X(:,3);
Q=Q/L/W;            %Charge per unit area of the channel
I_D=I_D/W;          %Current per width area of the channel

%Ferroelectric definition
t_FE=100e-9;            %Ferroelectric thickness, this thickness results in no hysteresis
%t_FE=230e-9;            %Ferroelectric thickness, this thickness result in a hysteresis

fundamental_constants;  %Routine for fetching the fundamental constants
ferroelectric;          %Routine for fetching the anisotropy constants of the ferroelectric

%Calculation of the voltage across the ferroelectric
E_FE=2*alpha1_P*Q+4*alpha11_P*Q.^3+6*alpha111_P*Q.^5+8*alpha1111_P*Q.^7;    %Electric field across the ferroelectric
V_FE=E_FE*t_FE;         %Voltage across the ferroelectric
V_G=V_g+E_FE*t_FE;      %Voltage at the outer gate
figure(1), plot(Q*L*W,V_FE,'k' ,  'linewidth', 4);
hysteresis;             %Routine for separating the hysteresis branches of the ferroelectric

%Plotting
cc_Hi='b';              %Color for NCFET hysteresis upper branch
cc_Lo='r';              %Color for NCFET hysteresis upper branch
cc_internal='m:';       %Color for plotting the internal instability
cc_baseline='k';        %Color for Baseline MOSFET
%Capacitance
C_MOS=diff(Q)./diff(V_g); C_MOS(length(V_g))=C_MOS(length(V_g)-1);
C_NC=diff(Q)./diff(V_G); C_NC(length(V_g))=C_NC(length(V_g)-1);
C_FE=diff(Q)./diff(V_FE); C_FE(length(V_g))=C_FE(length(V_g)-1);

SS_baseline=diff(V_g)./diff(log10(I_D))*1e3;SS_baseline(length(V_g))=SS_baseline(length(V_g)-1);
SS_NC=diff(V_G)./diff(log10(I_D))*1e3;SS_NC(length(V_g))=SS_NC(length(V_g)-1);


% %Q-V_G curves
% figure(1); semilogy(V_G, abs(Q)/q/1e4, cc_internal,  'linewidth', 4);hold on; %plots the Q-V_G curve of NCFET showing the instability
% figure(1); semilogy(V_G_L, abs(Q_L)/q/1e4, cc_Lo,V_G_H, abs(Q_H)/q/1e4, cc_Hi,  'linewidth', 4);hold on;%plots the Q-V_G hysteresis curve of NCFET 
% figure(1); semilogy(V_g, abs(Q)/q/1e4, cc_baseline,  'linewidth', 4);hold on;%plots the Q-V_g  curve of baseline MOSFET (no ferroelectric) 
% 
% 
% 
% 
% set(figure(1), 'color', 'white');
% xlabel('V_G (V)', 'fontsize', 35);ylabel('Charge Density (/cm^2)', 'fontsize', 35);
% title(['Comparison of Q-V_G characteristics \newline of NCFET and Baseline MOSFET\newline Ferroelectric Thickness=', num2str(t_FE*1e9), 'nm' ,'\newline V_D=', num2str(V_D), 'mV']);
% legend('NCFET Instability','NCFET positive sweep', 'NCFET negative sweep', 'Baseline MOSFET');
% xlim([-.2 1])
% ylim([1e10 2e15])
% set(gca, 'fontsize', 24);
% h1=figure(1);set(h1,'position', [100, 1000, 600, 800]);
% 
%I_D-V_G curves
% figure(2); semilogy(V_G_L, I_D_L, 'k',V_G_H, I_D_H, 'k', 'linewidth', 8);hold on;%plots the I_D-V_G hysteresis curve of NCFET 
% semilogy(V_g, I_D, 'k--', 'linewidth', 8);hold on;%plots the I_D-V_g  curve of baseline MOSFET (no ferroelectric) 
% %semilogy(V_G, I_D, 'r', 'linewidth', 3);hold on;%plots the I_D-V_g  curve of baseline MOSFET (no ferroelectric) 
% 
% xlabel('V_G (V)', 'fontsize', 35);ylabel('I_D (\muA/\mum)', 'fontsize', 35);
% % title(['Comparison of I_D-V_G characteristics \newline of NCFET and Baseline MOSFET\newline Ferroelectric Thickness=', num2str(t_FE*1e9), 'nm','\newline V_D=', num2str(V_D), 'mV']);
% % legend('NCFET positive sweep', 'NCFET negative sweep', 'Baseline MOSFET', 'location', 'southwest');
% 
% set(figure(2), 'color', 'white');
% set(gca, 'fontsize', 24);
% xlim([-.2 1]);
% ylim([1e-6 1e4])
% 
% set(gca, 'YTick', [1e-4 1e-3 1e-2 1e-1 1 1e1 1e2 1e3]);
% grid off;
% h1=figure(2);set(h1,'position', [760, 1000, 600, 800]);
% 
%Capacitance 
figure(3), plot(V_g, C_MOS*100,'k' ,  'linewidth', 4);
set(figure(3), 'color', 'white');
set(gca, 'fontsize', 24);

xlim([-.2 3]);
xlabel('V_g (V)', 'fontsize', 35);ylabel('Capacitance (\muF/cm^2)', 'fontsize', 35);

% figure(4),  semilogy( C_MOS*100,Q/q/1e4, 'k' ,abs(C_FE(find(C_FE<0)))*100,Q(find(C_FE<0))/q/1e4, 'r' , 'linewidth', 4);hold on;
% set(figure(4), 'color', 'white');
% set(gca, 'fontsize', 24);
% xlabel('Capacitance (\muF/cm^2)', 'fontsize', 35);ylabel('Charge Density (/cm^2)', 'fontsize', 35);
% 
% xlim([0 20]);

%Q-V_G curves
% figure(10); subplot(122), semilogy(V_G, abs(Q)/q/1e4, 'r',  'linewidth', 4);hold on; %plots the Q-V_G curve of NCFET showing the instability
% %figure(1); semilogy(V_G_L, abs(Q_L)/q/1e4, cc_Lo,V_G_H, abs(Q_H)/q/1e4, cc_Hi,  'linewidth', 4);hold on;%plots the Q-V_G hysteresis curve of NCFET 
% figure(10); semilogy(V_g, abs(Q)/q/1e4, 'k',  'linewidth', 4);hold on;%plots the Q-V_g  curve of baseline MOSFET (no ferroelectric) 
% 
% set(figure(10), 'color', 'white');
% xlabel('V_G (V)', 'fontsize', 35);ylabel('Charge Density (/cm^2)', 'fontsize', 35);
% %title(['Comparison of Q-V_G characteristics \newline of NCFET and Baseline MOSFET\newline Ferroelectric Thickness=', num2str(t_FE*1e9), 'nm' ,'\newline V_D=', num2str(V_D), 'mV']);
% %legend('NCFET Instability','NCFET positive sweep', 'NCFET negative sweep', 'Baseline MOSFET');
% xlim([-.2 1])
% ylim([4e10 4e14])
% set(gca, 'fontsize', 24);
%figure(10),subplot(121),  semilogy( C_MOS*100,Q/q/1e4, 'k' ,abs(C_FE(find(C_FE<0)))*100,Q(find(C_FE<0))/q/1e4, 'r' , 'linewidth', 4);hold on;
figure(10),  semilogy( C_MOS*100,Q/q/1e4, 'k' , 'linewidth', 4);hold on;

set(gca, 'fontsize', 24);
xlabel('Capacitance (\muF/cm^2)', 'fontsize', 35);ylabel('Charge Density (/cm^2)', 'fontsize', 35);
xlim([0 10]);
ylim([4e10 4e14]);
set(gca, 'YTick', [1e11 1e12 1e13 1e14]);

%SS
% figure(12),  semilogx( I_D,SS_baseline, 'k--' , I_D,SS_NC, 'k' , 'linewidth', 4);hold on;
% set(figure(12), 'color', 'white');
% set(gca, 'fontsize', 24);
% xlabel('SS (mV/dec)', 'fontsize', 35);ylabel('I_D (\muA/\mum)', 'fontsize', 35);
% 
% xlim([0 10]);
% ylim([0 200]);
