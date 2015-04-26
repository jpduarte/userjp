*Sample netlist for inverter

.option abstol=1e-6 reltol=1e-6 post ingold
.temp 25

.hdl "/users/jpduarte/BSIM_CM_Matlab/BSIM_model_development_v2/DM_Verilog_Hspice/Models_Verilog/BSIMIMG/code/bsimimg.va"
*.include "/users/jpduarte/research/userjp/project2/modelcards/leapmodelcard.nmos"
*.include "/users/jpduarte/research/userjp/project2/modelcards/leapmodelcard.pmos"
.include "/users/jpduarte/BSIM_CM_Matlab/BSIM_model_development_v2/DM_Verilog_Hspice/Models_Verilog/BSIMIMG/benchmark_tests/modelcard.nmos"
.include "/users/jpduarte/BSIM_CM_Matlab/BSIM_model_development_v2/DM_Verilog_Hspice/Models_Verilog/BSIMIMG/benchmark_tests/modelcard.pmos"

* --- Voltage Sources ---
.param vbgnv=0.0 vbgpv=1.0

vdd supply  0 dc=1.0
vinput vin  0 dc=1.0
vbackgaten vbgn 0 dc=vbgnv
vbackgatep vbgp 0 dc=vbgpv

* --- Inverter Subcircuit ---
.subckt img_inv vin vout vdd gnd vbgns vbgps
    Xp1 vout vin vdd vbgps pmos1 L=1000n W=10u
    Xn1 vout vin gnd vbgns nmos1 L=1000n W=10u
.ends


* --- inverter ---
Xinv1   vin  vout supply 0 vbgn vbgp img_inv
*Xinv2   v2  vout supply 0 vbgn vbgp img_inv
* --- DC Analysis ---
.dc vinput 0.0 1.0 0.01 
.print dc vinput
.print dc v(vout)
.print dc Xinv1.Xp1:Ids
.print dc Xinv1.Xn1:Ids
.end
