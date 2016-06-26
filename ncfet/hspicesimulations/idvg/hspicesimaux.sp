*script to generate hspice simulation using cmdp, Juan Duarte 
*Date: 06/25/2016, time: 18:54:24

.option abstol=1e-6 reltol=1e-6 post ingold 
.option measform=1 
.temp 27 

.hdl "/users/jpduarte/research/BSIMCMG/code/bsimcmg.va" 
.include "/users/jpduarte/research/userjp/ncfet/modelcards/modelcard_nc.nmos" 

.PARAM Vd_value = 0 
.PARAM Vg_value = 0 
.PARAM Vs_value = 0 
.PARAM Vb_value = 0 
.PARAM L_value = 3e-08 

Vd Vd 0.0 dc = Vd_value 
Vg Vg 0.0 dc = Vg_value 
Vs Vs 0.0 dc = Vs_value 
Vb Vb 0.0 dc = Vb_value 

X1 Vd Vg Vs Vb nmos1 L = 'L_value'

.DATA datadc Vd_value Vg_value Vs_value Vb_value L_value 
0.05 0.0 0 0 3e-08 
0.05 0.0344827586207 0 0 3e-08 
0.05 0.0689655172414 0 0 3e-08 
0.05 0.103448275862 0 0 3e-08 
0.05 0.137931034483 0 0 3e-08 
0.05 0.172413793103 0 0 3e-08 
0.05 0.206896551724 0 0 3e-08 
0.05 0.241379310345 0 0 3e-08 
0.05 0.275862068966 0 0 3e-08 
0.05 0.310344827586 0 0 3e-08 
0.05 0.344827586207 0 0 3e-08 
0.05 0.379310344828 0 0 3e-08 
0.05 0.413793103448 0 0 3e-08 
0.05 0.448275862069 0 0 3e-08 
0.05 0.48275862069 0 0 3e-08 
0.05 0.51724137931 0 0 3e-08 
0.05 0.551724137931 0 0 3e-08 
0.05 0.586206896552 0 0 3e-08 
0.05 0.620689655172 0 0 3e-08 
0.05 0.655172413793 0 0 3e-08 
0.05 0.689655172414 0 0 3e-08 
0.05 0.724137931034 0 0 3e-08 
0.05 0.758620689655 0 0 3e-08 
0.05 0.793103448276 0 0 3e-08 
0.05 0.827586206897 0 0 3e-08 
0.05 0.862068965517 0 0 3e-08 
0.05 0.896551724138 0 0 3e-08 
0.05 0.931034482759 0 0 3e-08 
0.05 0.965517241379 0 0 3e-08 
0.05 1.0 0 0 3e-08 
.ENDDATA 
.dc sweep DATA = datadc 
.print dc X1:Ids X1:qs 
.end