%Anisotropy constants of the ferroelectric 
um=0;                   %Epitaxial strain in ferroelectric
x=0.5; %Ti
T0=462.63+843.4*x-2105.5*x^2+4041.8*x^3-3828.3*x^4+1337.8*x^5;
C0=(2.1716/(1+500.5*(x-.5)^2)+0.131*x+2.01)*1e5;
Q_12=0.026568/(1+200*(x-0.5)^2)+0.01209*x-0.013386;
c_11=8.2e-12;
c_12=-2.6e-12;

alpha1_P=(T-T0)/(2*eps_0*C0)-2*Q_12/(c_11+c_12)*um
alpha11_P=(10.612-22.655*x+10.95*x^2)*1e13/C0+4*Q_12^2/(c_11+c_12)
alpha111_P=(12.026-17.296*x+9.179*x^2)*1e13/C0
alpha1111_P=0;

