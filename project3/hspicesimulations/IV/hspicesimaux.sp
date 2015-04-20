*script to generate hspice simulation using cmdp, Juan Duarte 
*Date: 03/27/2015, time: 14:49:02

.option abstol=1e-6 reltol=1e-6 post ingold 
.option measform=1 
.temp 27 

.hdl "/users/jpduarte/research/cmdp/userjp/project3/models/resitance.va" 
.include "/users/jpduarte/research/cmdp/userjp/project3/model_cards/modelcardR.res" 

.PARAM Vp_value = 0 
.PARAM Vn_value = 0 
.PARAM L_value = 1e-06 

Vp Vp 0.0 dc = Vp_value 
Vn Vn 0.0 dc = Vn_value 

X1 Vp Vn res1 L = 'L_value'

.DATA datadc Vp_value Vn_value L_value 
0.0 0 1e-06 
-0.010101010101 0 1e-06 
-0.020202020202 0 1e-06 
-0.030303030303 0 1e-06 
-0.040404040404 0 1e-06 
-0.0505050505051 0 1e-06 
-0.0606060606061 0 1e-06 
-0.0707070707071 0 1e-06 
-0.0808080808081 0 1e-06 
-0.0909090909091 0 1e-06 
-0.10101010101 0 1e-06 
-0.111111111111 0 1e-06 
-0.121212121212 0 1e-06 
-0.131313131313 0 1e-06 
-0.141414141414 0 1e-06 
-0.151515151515 0 1e-06 
-0.161616161616 0 1e-06 
-0.171717171717 0 1e-06 
-0.181818181818 0 1e-06 
-0.191919191919 0 1e-06 
-0.20202020202 0 1e-06 
-0.212121212121 0 1e-06 
-0.222222222222 0 1e-06 
-0.232323232323 0 1e-06 
-0.242424242424 0 1e-06 
-0.252525252525 0 1e-06 
-0.262626262626 0 1e-06 
-0.272727272727 0 1e-06 
-0.282828282828 0 1e-06 
-0.292929292929 0 1e-06 
-0.30303030303 0 1e-06 
-0.313131313131 0 1e-06 
-0.323232323232 0 1e-06 
-0.333333333333 0 1e-06 
-0.343434343434 0 1e-06 
-0.353535353535 0 1e-06 
-0.363636363636 0 1e-06 
-0.373737373737 0 1e-06 
-0.383838383838 0 1e-06 
-0.393939393939 0 1e-06 
-0.40404040404 0 1e-06 
-0.414141414141 0 1e-06 
-0.424242424242 0 1e-06 
-0.434343434343 0 1e-06 
-0.444444444444 0 1e-06 
-0.454545454545 0 1e-06 
-0.464646464646 0 1e-06 
-0.474747474747 0 1e-06 
-0.484848484848 0 1e-06 
-0.494949494949 0 1e-06 
-0.505050505051 0 1e-06 
-0.515151515152 0 1e-06 
-0.525252525253 0 1e-06 
-0.535353535354 0 1e-06 
-0.545454545455 0 1e-06 
-0.555555555556 0 1e-06 
-0.565656565657 0 1e-06 
-0.575757575758 0 1e-06 
-0.585858585859 0 1e-06 
-0.59595959596 0 1e-06 
-0.606060606061 0 1e-06 
-0.616161616162 0 1e-06 
-0.626262626263 0 1e-06 
-0.636363636364 0 1e-06 
-0.646464646465 0 1e-06 
-0.656565656566 0 1e-06 
-0.666666666667 0 1e-06 
-0.676767676768 0 1e-06 
-0.686868686869 0 1e-06 
-0.69696969697 0 1e-06 
-0.707070707071 0 1e-06 
-0.717171717172 0 1e-06 
-0.727272727273 0 1e-06 
-0.737373737374 0 1e-06 
-0.747474747475 0 1e-06 
-0.757575757576 0 1e-06 
-0.767676767677 0 1e-06 
-0.777777777778 0 1e-06 
-0.787878787879 0 1e-06 
-0.79797979798 0 1e-06 
-0.808080808081 0 1e-06 
-0.818181818182 0 1e-06 
-0.828282828283 0 1e-06 
-0.838383838384 0 1e-06 
-0.848484848485 0 1e-06 
-0.858585858586 0 1e-06 
-0.868686868687 0 1e-06 
-0.878787878788 0 1e-06 
-0.888888888889 0 1e-06 
-0.89898989899 0 1e-06 
-0.909090909091 0 1e-06 
-0.919191919192 0 1e-06 
-0.929292929293 0 1e-06 
-0.939393939394 0 1e-06 
-0.949494949495 0 1e-06 
-0.959595959596 0 1e-06 
-0.969696969697 0 1e-06 
-0.979797979798 0 1e-06 
-0.989898989899 0 1e-06 
-1.0 0 1e-06 
.ENDDATA 
.dc sweep DATA = datadc 
.print dc X1:aux1 
.end