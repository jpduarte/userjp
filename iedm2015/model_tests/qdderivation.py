from sympy import *

qdsat = Symbol('qdsat')
qms = Symbol('qms')
x1 = Symbol('x1')
x2 = Symbol('x2')
mulow1 = Symbol('mulow1')
mulow2 = Symbol('mulow2')
Lg = Symbol('Lg')
qmd = Symbol('qmd')
ids = Symbol('ids')
 
vsat = Symbol('vsat')
vt = Symbol('vt')

     
q1 = (qmd-qms)*(x1+1.0)/2.0 + qms
q2 = (qmd-qms)*(x2+1.0)/2.0 + qms
    
ids1 = -q1*(1.0-1.0/q1)*mulow1
ids2 = -q2*(1.0-1.0/q2)*mulow2   
   
#ids = 0.5*(qmd-qms)*(ids1+ids2) 

sol1 = solve(ids -0.5*(qmd-qms)*(ids1+ids2), qmd)

print sol1
print latex((mulow1*qms*x1 + mulow1 + mulow2*qms*x2 + mulow2 - sqrt(-4.0*ids*mulow1*x1 - 4.0*ids*mulow1 - 4.0*ids*mulow2*x2 - 4.0*ids*mulow2 + mulow1**2*qms**2 - 2.0*mulow1**2*qms + mulow1**2 + 2.0*mulow1*mulow2*qms**2 - 4.0*mulow1*mulow2*qms + 2.0*mulow1*mulow2 + mulow2**2*qms**2 - 2.0*mulow2**2*qms + mulow2**2))/(mulow1*x1 + mulow1 + mulow2*x2 + mulow2))

"""
[(mulow1*qms*x1 + mulow1 + mulow2*qms*x2 + mulow2 - sqrt(-4.0*ids*mulow1*x1 - 4.0*ids*mulow1 - 4.0*ids*mulow2*x2 - 4.0*ids*mulow2 + mulow1**2*qms**2 - 2.0*mulow1**2*qms + mulow1**2 + 2.0*mulow1*mulow2*qms**2 - 4.0*mulow1*mulow2*qms + 2.0*mulow1*mulow2 + mulow2**2*qms**2 - 2.0*mulow2**2*qms + mulow2**2))/(mulow1*x1 + mulow1 + mulow2*x2 + mulow2), (mulow1*qms*x1 + mulow1 + mulow2*qms*x2 + mulow2 + sqrt(-4.0*ids*mulow1*x1 - 4.0*ids*mulow1 - 4.0*ids*mulow2*x2 - 4.0*ids*mulow2 + mulow1**2*qms**2 - 2.0*mulow1**2*qms + mulow1**2 + 2.0*mulow1*mulow2*qms**2 - 4.0*mulow1*mulow2*qms + 2.0*mulow1*mulow2 + mulow2**2*qms**2 - 2.0*mulow2**2*qms + mulow2**2))/(mulow1*x1 + mulow1 + mulow2*x2 + mulow2)]

"""
