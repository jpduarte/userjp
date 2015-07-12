from sympy import *

qdsat = Symbol('qdsat')
qms = Symbol('qms')
x1 = Symbol('x1')
x2 = Symbol('x2')
mulow1 = Symbol('mulow1')
mulow2 = Symbol('mulow2')
Lg = Symbol('Lg')
 
vsat = Symbol('vsat')
vt = Symbol('vt')

     
q1 = (qdsat-qms)*(x1+1.0)/2.0 + qms
q2 = (qdsat-qms)*(x2+1.0)/2.0 + qms
    
ids1 = -q1*(1.0-1.0/q1)*mulow1
ids2 = -q2*(1.0-1.0/q2)*mulow2   
   
ids = 0.5*(qdsat-qms)*(ids1+ids2) 

sol1 = solve(-vsat*qdsat*Lg/vt-ids, qdsat)

print sol1

"""
[(2.0*Lg*vsat + mulow1*qms*vt*x1 + mulow1*vt + mulow2*qms*vt*x2 + mulow2*vt - sqrt(4.0*Lg**2*vsat**2 + 4.0*Lg*mulow1*qms*vsat*vt*x1 + 4.0*Lg*mulow1*vsat*vt + 4.0*Lg*mulow2*qms*vsat*vt*x2 + 4.0*Lg*mulow2*vsat*vt + mulow1**2*qms**2*vt**2 - 2.0*mulow1**2*qms*vt**2 + mulow1**2*vt**2 + 2.0*mulow1*mulow2*qms**2*vt**2 - 4.0*mulow1*mulow2*qms*vt**2 + 2.0*mulow1*mulow2*vt**2 + mulow2**2*qms**2*vt**2 - 2.0*mulow2**2*qms*vt**2 + mulow2**2*vt**2))/(mulow1*vt*x1 + mulow1*vt + mulow2*vt*x2 + mulow2*vt), 
 (2.0*Lg*vsat + mulow1*qms*vt*x1 + mulow1*vt + mulow2*qms*vt*x2 + mulow2*vt + sqrt(4.0*Lg**2*vsat**2 + 4.0*Lg*mulow1*qms*vsat*vt*x1 + 4.0*Lg*mulow1*vsat*vt + 4.0*Lg*mulow2*qms*vsat*vt*x2 + 4.0*Lg*mulow2*vsat*vt + mulow1**2*qms**2*vt**2 - 2.0*mulow1**2*qms*vt**2 + mulow1**2*vt**2 + 2.0*mulow1*mulow2*qms**2*vt**2 - 4.0*mulow1*mulow2*qms*vt**2 + 2.0*mulow1*mulow2*vt**2 + mulow2**2*qms**2*vt**2 - 2.0*mulow2**2*qms*vt**2 + mulow2**2*vt**2))/(mulow1*vt*x1 + mulow1*vt + mulow2*vt*x2 + mulow2*vt)]
"""
