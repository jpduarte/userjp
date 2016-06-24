*Sample netlist for BSIM-IMG
*Id-Vd Characteristics for NMOS

.option abstol=1e-6 reltol=1e-6 post ingold
.temp 27 

.hdl "/users/jpduarte/research/BSIMIMG/code/bsimimg.va" 
.include "/users/jpduarte/research/userjp/project4/modelcards/modelcardsimple.nmos" 


* --- Voltage Sources ---
vds drain  0 dc=0
vfgs fgate  0 dc=1.0
vbgs bgate  0 dc=0.0

* --- Transistor ---
X1 drain fgate 0 bgate nmos1 L=55n W=10u

* --- DC Analysis ---
.dc vds 0 2 0.001 vfgs -2.0 2.0 0.005
*.print dc i(X1.d)
*.probe dc par`-i(vds)`

.end
