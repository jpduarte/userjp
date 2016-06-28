*script to generate hspice simulation using cmdp, Juan Duarte 
*Date: 06/26/2016, time: 16:31:03

.option abstol=1e-6 reltol=1e-6 post ingold 
.option measform=1 
.temp 27 

.hdl "/users/jpduarte/research/BSIMCMG/code/bsimcmg.va" 
.include "/users/jpduarte/research/BSIMCMG/benchmark_test/modelcard.nmos" 

.PARAM Vd_value = 0.05 
.PARAM Vg_value = 0 
.PARAM Vs_value = 0 
.PARAM Vb_value = 0 
.PARAM L_value = 3e-08 
.PARAM TFIN_value = 1.5e-08 
.PARAM NFIN_value = 10 
.PARAM NRS_value = 1 
.PARAM NRD_value = 1 

Vd Vd 0.0 dc = Vd_value 
Vg Vg 0.0 dc = Vg_value 
Vs Vs 0.0 dc = Vs_value 
Vb Vb 0.0 dc = Vb_value 

X1 Vd Vg Vs Vb nmos1 L = 'L_value' TFIN = 'TFIN_value' NFIN = 'NFIN_value' NRS = 'NRS_value' NRD = 'NRD_value'

.dc Vg -0.5 1.0 0.01
.print dc X1:Ids X1:qs X1:vfe 
.end
