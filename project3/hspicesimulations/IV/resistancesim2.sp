*script to generate hspice simulation using cmdp, Juan Duarte 
*Date: 11/02/2015, time: 13:58:12

.option abstol=1e-6 reltol=1e-6 post ingold 
.option measform=1 
.temp 27 

.hdl "/users/jpduarte/research/userjp/project3/models/resIMG.va" 
.include "/users/jpduarte/research/userjp/project3/model_cards/modelcardRimg.res" 

.PARAM Vp_value = 0 
.PARAM Vn_value = 0 
.PARAM L_value = 1e-06 

Vp Vp 0.0 dc = Vp_value 
Vn Vn 0.0 dc = Vn_value 

X1 Vp Vn res1 L = 'L_value'

.DATA datadc Vp_value Vn_value L_value 
-2.5 0 1e-06 
-2.36206896552 0 1e-06 
-2.22413793103 0 1e-06 
-2.08620689655 0 1e-06 
-1.94827586207 0 1e-06 
-1.81034482759 0 1e-06 
-1.6724137931 0 1e-06 
-1.53448275862 0 1e-06 
-1.39655172414 0 1e-06 
-1.25862068966 0 1e-06 
-1.12068965517 0 1e-06 
-0.98275862069 0 1e-06 
-0.844827586207 0 1e-06 
-0.706896551724 0 1e-06 
-0.568965517241 0 1e-06 
-0.431034482759 0 1e-06 
-0.293103448276 0 1e-06 
-0.155172413793 0 1e-06 
-0.0172413793103 0 1e-06 
0.120689655172 0 1e-06 
0.258620689655 0 1e-06 
0.396551724138 0 1e-06 
0.534482758621 0 1e-06 
0.672413793103 0 1e-06 
0.810344827586 0 1e-06 
0.948275862069 0 1e-06 
1.08620689655 0 1e-06 
1.22413793103 0 1e-06 
1.36206896552 0 1e-06 
1.5 0 1e-06 
.ENDDATA 
.dc sweep DATA = datadc 
.print dc X1:qicores X1:qicoreguess X1:phisguesss X1:phifsnew X1:deltaaux1s X1:qicore1 X1:qicore2 X1:qicore3 X1:qicore4 X1:qicore5 X1:qicores2 
.end