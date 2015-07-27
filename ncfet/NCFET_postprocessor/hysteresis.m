%Calculation of hysteresis
try
Flag1=0;Flag2=0;
for ii=2:length(V_G),
    if (V_G(ii)<V_G(ii-1)) && (Flag1==0),
        Vc_1=V_G(ii);
        N_1=ii;
        Flag1=1;
    end
    
end
[dummy, N_2]=min(V_G(N_1+1:length(V_G)));
Vc_2=V_G(N_2+N_1);
disp([Vc_1, Vc_2, Vc_1-Vc_2])

%low state
V_G_1_2_=V_G((N_1+N_2):length(V_G));     I_D_1_2=I_D((N_1+N_2):length(V_G));Q_1_2=Q((N_1+N_2):length(V_G));
V_G_1_2=V_G_1_2_(find(V_G_1_2_>Vc_1));    I_D_1_2=I_D_1_2(find(V_G_1_2_>Vc_1));Q_1_2=Q_1_2(find(V_G_1_2_>Vc_1));

V_G_1_1=V_G(1:N_1);
I_D_1_1=I_D(1:N_1);
Q_1_1=Q(1:N_1);

V_G_L=[V_G_1_1; V_G_1_2];
I_D_L=[I_D_1_1; I_D_1_2];
Q_L=[Q_1_1; Q_1_2];

%high state
V_G_2_2=V_G((N_1+N_2):length(V_G));     I_D_2=I_D((N_1+N_2):length(V_G));Q_2_2=Q((N_1+N_2):length(V_G));

V_G_2_1_=V_G(1:N_1);I_D_1=I_D(1:N_1);Q_2_1=Q(1:N_1);
V_G_2_1=V_G_2_1_(find(V_G_2_1_<Vc_2)); I_D_1=I_D_1(find(V_G_2_1_<Vc_2));Q_2_1=Q_2_1(find(V_G_2_1_<Vc_2));

V_G_H=[V_G_2_1; V_G_2_2];
I_D_H=[I_D_1; I_D_2];
Q_H=[Q_2_1; Q_2_2];

catch ME,
    1
     V_G_H=V_G; V_G_L=V_G;
     I_D_H=I_D;I_D_L=I_D;
          Q_H=Q;Q_L=Q;

end
