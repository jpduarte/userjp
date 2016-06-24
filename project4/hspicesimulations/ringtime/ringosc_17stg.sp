*Sample netlist for BSIM-IMG
*17-stage ring oscillator

.options abstol=1e-6 reltol=1e-6 post

.hdl "/users/jpduarte/research/BSIMIMG/code/bsimimg.va" 
.include "/users/jpduarte/research/userjp/project4/modelcards/modelcard.nmos" 
.include "/users/jpduarte/research/userjp/project4/modelcards/modelcard.pmos" 
*.hdl "/users/jpduarte/research/BSIMCMG/workingcode/bsimcmg.va" 
*.include "/users/jpduarte/research/BSIMCMG/benchmark_test/modelcard.pmos" 
*.include "/users/jpduarte/research/BSIMCMG/benchmark_test/modelcard.nmos" 

.param vbgnv=0.0 vbgpv=1.0

* --- Voltage Sources ---
vdd supply  0 dc=1.0
vbackgaten vbgn 0 dc=vbgnv
vbackgatep vbgp 0 dc=vbgpv

* --- Inverter Subcircuit ---
.subckt img_inv vin vout vdd gnd vbgns vbgps
    Xp1 vout vin vdd vbgps pmos1 L=55n W=10u
    Xn1 vout vin gnd vbgns nmos1 L=55n W=10u  
.ends

* --- 17 Stage Ring oscillator ---
Xinv1   1  2 supply 0 vbgn vbgp img_inv
Xinv2   2  3 supply 0 vbgn vbgp img_inv
Xinv3   3  4 supply 0 vbgn vbgp img_inv
Xinv4   4  5 supply 0 vbgn vbgp img_inv
Xinv5   5  6 supply 0 vbgn vbgp img_inv
Xinv6   6  7 supply 0 vbgn vbgp img_inv
Xinv7   7  8 supply 0 vbgn vbgp img_inv
Xinv8   8  9 supply 0 vbgn vbgp img_inv
Xinv9   9 10 supply 0 vbgn vbgp img_inv
Xinv10 10 11 supply 0 vbgn vbgp img_inv
Xinv11 11 12 supply 0 vbgn vbgp img_inv
Xinv12 12 13 supply 0 vbgn vbgp img_inv
Xinv13 13 14 supply 0 vbgn vbgp img_inv
Xinv14 14 15 supply 0 vbgn vbgp img_inv
Xinv15 15 16 supply 0 vbgn vbgp img_inv
Xinv16 16 17 supply 0 vbgn vbgp img_inv
Xinv17 17  1 supply 0 vbgn vbgp img_inv

* --- Initial Condition ---
.ic  1=1 2=0 3=1 4=0 5=1 6=0 7=1 8=0 9=1 10=0 11=1 12=0 13=1 14=0 15=1 16=0 17=1

.tran 10p 100n 

*.print tran v(1)

.end
