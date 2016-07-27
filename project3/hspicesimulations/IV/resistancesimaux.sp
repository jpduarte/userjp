*script to generate hspice simulation using cmdp, Juan Duarte 
*Date: 12/10/2015, time: 07:14:09

.option abstol=1e-6 reltol=1e-6 post ingold 
.option measform=1 
.temp 27 

.hdl "/users/jpduarte/research/userjp/project3/models/res.va" 
.include "/users/jpduarte/research/userjp/project3/model_cards/modelcardR.res" 

.PARAM Vp_value = 0 
.PARAM Vn_value = 0 
.PARAM L_value = 1e-06 

Vp Vp 0.0 dc = Vp_value 
Vn Vn 0.0 dc = Vn_value 

X1 Vp Vn res1 L = 'L_value'

.DATA datadc Vp_value Vn_value L_value 
0.0 0.0 1e-06 
0.111111111111 0.0 1e-06 
0.222222222222 0.0 1e-06 
0.333333333333 0.0 1e-06 
0.444444444444 0.0 1e-06 
0.555555555556 0.0 1e-06 
0.666666666667 0.0 1e-06 
0.777777777778 0.0 1e-06 
0.888888888889 0.0 1e-06 
1.0 0.0 1e-06 
.ENDDATA 
.dc sweep DATA = datadc 
.print dc X1:dxfinaldVp1 X1:dxdirectdVp1 X1:dxfinaldVp2 X1:dxdirectdVp2 
.end