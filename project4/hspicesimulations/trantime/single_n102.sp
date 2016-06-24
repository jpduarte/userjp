*** HSPICE netlist ***

.option post ingold numdgt=10
.model lvtnfet bsimimg 

.hdl "/users/jpduarte/research/BSIMIMG/code/bsimimg.va" 
.include "/users/jpduarte/research/userjp/project4/modelcards/modelcard.nmos" 

xn dd gg ss ss lvtnfet L=5.5e-08 W=2e-07 NF=1 

vdd dd 0 dc=0.1
vgg gg 0 pulse 0.3 1 0 100000u 1n 10u 20u
vss ss 0 dc=0

.tran 10p 100000u

.end
