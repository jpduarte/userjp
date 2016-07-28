*script to generate hspice simulation using cmdp, Juan Duarte 
*Date: 07/10/2016, time: 12:11:20

.option abstol=1e-2 reltol=1e-1 post ingold numdgt=8
.option measform=1 
.temp 27 

.hdl "/users/jpduarte/research/BSIMCMG/code/bsimcmg.va" 
.include "//users/jpduarte/research/userjp/ncfet/modelcards/modelcard_nc.nmos" 

.PARAM Vd_value = 0.5 
.PARAM Vg_value = 0 
.PARAM Vs_value = 0 
.PARAM Vb_value = 0 
.PARAM L_value = 3e-08 
.PARAM alpha1_P_value = -84927000.0 
.PARAM alpha11_P_value = 611660000000.0 
.PARAM t_FE_value = 600e-09 

Vd Vdn 0.0 dc = Vd_value 
Vg Vgn 0.0 dc = Vg_value 
Vs Vsn 0.0 dc = Vs_value 
Vb Vbn 0.0 dc = Vb_value 

X1 Vdn Vgn Vsn Vbn nmos1 L = 'L_value' alpha1_P = 'alpha1_P_value' alpha11_P = 'alpha11_P_value' t_FE = 't_FE_value'

.dc Vg 0.0 1.0 0.01

.print dc X1:Ids X1:qs X1:vfes X1:vfed 
.probe dc ids2=par'-i(vd)'
.print dc par'ids2' 
.end
