*Sample netlist for inverter

.option abstol=1e-6 reltol=1e-6 post ingold
.temp 25

.hdl "/users/jpduarte/BSIM_CM_Matlab/BSIM_model_development_v2/DM_Verilog_Hspice/Models_Verilog/BSIMCMG109.0.0beta2/BSIMCMG/workingcode/bsimcmg.va"
.include "../modelcards/modelcard.nmos"
.include "../modelcards/modelcard.pmos"

* --- Voltage Sources ---
vdd supply  0 dc=0.5
*vinput vin  0 dc=0.5

* --- inverter ---
X1 vout vin 0 0 nmos1 L=50e-9 NFIN=1 DEVTYPE=1
X2 vout vin supply supply pmos1 L=50e-9 NFIN=2 DEVTYPE=0

CLOAD vout 0 .75f
* --- DC Analysis ---
*.dc vinput 0.0 0.4 0.01 
vinput vin 0 0 PULSE .2 4.8 2N 1N 1N 5N 20N
.TRAN 200P 20N
.print tran v(vin)
.print tran v(X1.d)
.print tran v(vout)
.print tran i(X1.d)
.print tran X1:Ids 
.print tran time
.end
