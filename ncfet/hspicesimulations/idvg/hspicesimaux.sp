*script to generate hspice simulation using cmdp, Juan Duarte 
*Date: 07/30/2015, time: 14:14:21

.option abstol=1e-6 reltol=1e-6 post ingold 
.option measform=1 
.temp 27 

.hdl "/users/jpduarte/research/BSIMCMG/workingcode/bsimcmg.va" 
.include "/users/jpduarte/research/userjp/ncfet/modelcards/modelcard2.nmos" 

.PARAM Vd_value = 0 
.PARAM Vg_value = 0 
.PARAM Vs_value = 0 
.PARAM Vb_value = 0 
.PARAM L_value = 41 

Vd Vd 0.0 dc = Vd_value 
Vg Vg 0.0 dc = Vg_value 
Vs Vs 0.0 dc = Vs_value 
Vb Vb 0.0 dc = Vb_value 

X1 Vd Vg Vs Vb nmos1 L = 'L_value'

.DATA datadc Vd_value Vg_value Vs_value Vb_value L_value 
0.02 0.0 0 0 41 
0.5 0.0 0 0 41 
0.02 0.0416666666667 0 0 41 
0.5 0.0416666666667 0 0 41 
0.02 0.0833333333333 0 0 41 
0.5 0.0833333333333 0 0 41 
0.02 0.125 0 0 41 
0.5 0.125 0 0 41 
0.02 0.166666666667 0 0 41 
0.5 0.166666666667 0 0 41 
0.02 0.208333333333 0 0 41 
0.5 0.208333333333 0 0 41 
0.02 0.25 0 0 41 
0.5 0.25 0 0 41 
0.02 0.291666666667 0 0 41 
0.5 0.291666666667 0 0 41 
0.02 0.333333333333 0 0 41 
0.5 0.333333333333 0 0 41 
0.02 0.375 0 0 41 
0.5 0.375 0 0 41 
0.02 0.416666666667 0 0 41 
0.5 0.416666666667 0 0 41 
0.02 0.458333333333 0 0 41 
0.5 0.458333333333 0 0 41 
0.02 0.5 0 0 41 
0.5 0.5 0 0 41 
0.02 0.541666666667 0 0 41 
0.5 0.541666666667 0 0 41 
0.02 0.583333333333 0 0 41 
0.5 0.583333333333 0 0 41 
0.02 0.625 0 0 41 
0.5 0.625 0 0 41 
0.02 0.666666666667 0 0 41 
0.5 0.666666666667 0 0 41 
0.02 0.708333333333 0 0 41 
0.5 0.708333333333 0 0 41 
0.02 0.75 0 0 41 
0.5 0.75 0 0 41 
0.02 0.791666666667 0 0 41 
0.5 0.791666666667 0 0 41 
0.02 0.833333333333 0 0 41 
0.5 0.833333333333 0 0 41 
0.02 0.875 0 0 41 
0.5 0.875 0 0 41 
0.02 0.916666666667 0 0 41 
0.5 0.916666666667 0 0 41 
0.02 0.958333333333 0 0 41 
0.5 0.958333333333 0 0 41 
0.02 1.0 0 0 41 
0.5 1.0 0 0 41 
.ENDDATA 
.dc sweep DATA = datadc 
.print dc X1:Ids X1:Qg X1:E_FE X1:V_FE 
.end