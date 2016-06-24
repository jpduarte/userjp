#derivative leti g3 approach
from sympy import *
Vg_local_N = Symbol('Vg_local_N')
a0 = Symbol('a0')
qm = Symbol('qm')
b0 = Symbol('b0')
vth_N_Sub = Symbol('vth_N_Sub')
nss = Symbol('nss')
A0 = Symbol('A0')
vt = Symbol('vt')



vfe = -(a0*qm+b0*qm**3.0)
Vov         = (Vg_local_N-vfe-vth_N_Sub)*0.5/nss
qmaux      = exp((Vg_local_N-vfe-vth_N_Sub)*0.5/nss)
f =  qm   - 2.0*(1.0-sqrt(1.0+(log(1.0+qmaux))**2.0))

df = f.diff(qm)


print (df)

