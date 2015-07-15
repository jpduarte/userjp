*script to generate hspice simulation using cmdp, Juan Duarte 
*Date: 07/12/2015, time: 21:10:31

.option abstol=1e-6 reltol=1e-6 post ingold 
.option measform=1 
.temp 27 

.hdl "/users/jpduarte/BSIM_CM_Matlab/BSIM_model_development_v2/DM_Verilog_Hspice/Models_Verilog/BSIMCMG109.0.0beta2/BSIMCMG/workingcode/bsimcmg.va" 
.include "/users/jpduarte/research/userjp/ncfet/modelcards/modelcard.nmos" 

.PARAM Vd_value = 0 
.PARAM Vg_value = 0 
.PARAM Vs_value = 0 
.PARAM Vb_value = 0 
.PARAM L_value = 5e-08 

Vd Vd 0.0 dc = Vd_value 
Vg Vg 0.0 dc = Vg_value 
Vs Vs 0.0 dc = Vs_value 
Vb Vb 0.0 dc = Vb_value 

X1 Vd Vg Vs Vb nmos1 L = 'L_value'

.DATA datadc Vd_value Vg_value Vs_value Vb_value L_value 
0.05 0.0 0 0 5e-08 
1.0 0.0 0 0 5e-08 
0.05 0.010101010101 0 0 5e-08 
1.0 0.010101010101 0 0 5e-08 
0.05 0.020202020202 0 0 5e-08 
1.0 0.020202020202 0 0 5e-08 
0.05 0.030303030303 0 0 5e-08 
1.0 0.030303030303 0 0 5e-08 
0.05 0.040404040404 0 0 5e-08 
1.0 0.040404040404 0 0 5e-08 
0.05 0.0505050505051 0 0 5e-08 
1.0 0.0505050505051 0 0 5e-08 
0.05 0.0606060606061 0 0 5e-08 
1.0 0.0606060606061 0 0 5e-08 
0.05 0.0707070707071 0 0 5e-08 
1.0 0.0707070707071 0 0 5e-08 
0.05 0.0808080808081 0 0 5e-08 
1.0 0.0808080808081 0 0 5e-08 
0.05 0.0909090909091 0 0 5e-08 
1.0 0.0909090909091 0 0 5e-08 
0.05 0.10101010101 0 0 5e-08 
1.0 0.10101010101 0 0 5e-08 
0.05 0.111111111111 0 0 5e-08 
1.0 0.111111111111 0 0 5e-08 
0.05 0.121212121212 0 0 5e-08 
1.0 0.121212121212 0 0 5e-08 
0.05 0.131313131313 0 0 5e-08 
1.0 0.131313131313 0 0 5e-08 
0.05 0.141414141414 0 0 5e-08 
1.0 0.141414141414 0 0 5e-08 
0.05 0.151515151515 0 0 5e-08 
1.0 0.151515151515 0 0 5e-08 
0.05 0.161616161616 0 0 5e-08 
1.0 0.161616161616 0 0 5e-08 
0.05 0.171717171717 0 0 5e-08 
1.0 0.171717171717 0 0 5e-08 
0.05 0.181818181818 0 0 5e-08 
1.0 0.181818181818 0 0 5e-08 
0.05 0.191919191919 0 0 5e-08 
1.0 0.191919191919 0 0 5e-08 
0.05 0.20202020202 0 0 5e-08 
1.0 0.20202020202 0 0 5e-08 
0.05 0.212121212121 0 0 5e-08 
1.0 0.212121212121 0 0 5e-08 
0.05 0.222222222222 0 0 5e-08 
1.0 0.222222222222 0 0 5e-08 
0.05 0.232323232323 0 0 5e-08 
1.0 0.232323232323 0 0 5e-08 
0.05 0.242424242424 0 0 5e-08 
1.0 0.242424242424 0 0 5e-08 
0.05 0.252525252525 0 0 5e-08 
1.0 0.252525252525 0 0 5e-08 
0.05 0.262626262626 0 0 5e-08 
1.0 0.262626262626 0 0 5e-08 
0.05 0.272727272727 0 0 5e-08 
1.0 0.272727272727 0 0 5e-08 
0.05 0.282828282828 0 0 5e-08 
1.0 0.282828282828 0 0 5e-08 
0.05 0.292929292929 0 0 5e-08 
1.0 0.292929292929 0 0 5e-08 
0.05 0.30303030303 0 0 5e-08 
1.0 0.30303030303 0 0 5e-08 
0.05 0.313131313131 0 0 5e-08 
1.0 0.313131313131 0 0 5e-08 
0.05 0.323232323232 0 0 5e-08 
1.0 0.323232323232 0 0 5e-08 
0.05 0.333333333333 0 0 5e-08 
1.0 0.333333333333 0 0 5e-08 
0.05 0.343434343434 0 0 5e-08 
1.0 0.343434343434 0 0 5e-08 
0.05 0.353535353535 0 0 5e-08 
1.0 0.353535353535 0 0 5e-08 
0.05 0.363636363636 0 0 5e-08 
1.0 0.363636363636 0 0 5e-08 
0.05 0.373737373737 0 0 5e-08 
1.0 0.373737373737 0 0 5e-08 
0.05 0.383838383838 0 0 5e-08 
1.0 0.383838383838 0 0 5e-08 
0.05 0.393939393939 0 0 5e-08 
1.0 0.393939393939 0 0 5e-08 
0.05 0.40404040404 0 0 5e-08 
1.0 0.40404040404 0 0 5e-08 
0.05 0.414141414141 0 0 5e-08 
1.0 0.414141414141 0 0 5e-08 
0.05 0.424242424242 0 0 5e-08 
1.0 0.424242424242 0 0 5e-08 
0.05 0.434343434343 0 0 5e-08 
1.0 0.434343434343 0 0 5e-08 
0.05 0.444444444444 0 0 5e-08 
1.0 0.444444444444 0 0 5e-08 
0.05 0.454545454545 0 0 5e-08 
1.0 0.454545454545 0 0 5e-08 
0.05 0.464646464646 0 0 5e-08 
1.0 0.464646464646 0 0 5e-08 
0.05 0.474747474747 0 0 5e-08 
1.0 0.474747474747 0 0 5e-08 
0.05 0.484848484848 0 0 5e-08 
1.0 0.484848484848 0 0 5e-08 
0.05 0.494949494949 0 0 5e-08 
1.0 0.494949494949 0 0 5e-08 
0.05 0.505050505051 0 0 5e-08 
1.0 0.505050505051 0 0 5e-08 
0.05 0.515151515152 0 0 5e-08 
1.0 0.515151515152 0 0 5e-08 
0.05 0.525252525253 0 0 5e-08 
1.0 0.525252525253 0 0 5e-08 
0.05 0.535353535354 0 0 5e-08 
1.0 0.535353535354 0 0 5e-08 
0.05 0.545454545455 0 0 5e-08 
1.0 0.545454545455 0 0 5e-08 
0.05 0.555555555556 0 0 5e-08 
1.0 0.555555555556 0 0 5e-08 
0.05 0.565656565657 0 0 5e-08 
1.0 0.565656565657 0 0 5e-08 
0.05 0.575757575758 0 0 5e-08 
1.0 0.575757575758 0 0 5e-08 
0.05 0.585858585859 0 0 5e-08 
1.0 0.585858585859 0 0 5e-08 
0.05 0.59595959596 0 0 5e-08 
1.0 0.59595959596 0 0 5e-08 
0.05 0.606060606061 0 0 5e-08 
1.0 0.606060606061 0 0 5e-08 
0.05 0.616161616162 0 0 5e-08 
1.0 0.616161616162 0 0 5e-08 
0.05 0.626262626263 0 0 5e-08 
1.0 0.626262626263 0 0 5e-08 
0.05 0.636363636364 0 0 5e-08 
1.0 0.636363636364 0 0 5e-08 
0.05 0.646464646465 0 0 5e-08 
1.0 0.646464646465 0 0 5e-08 
0.05 0.656565656566 0 0 5e-08 
1.0 0.656565656566 0 0 5e-08 
0.05 0.666666666667 0 0 5e-08 
1.0 0.666666666667 0 0 5e-08 
0.05 0.676767676768 0 0 5e-08 
1.0 0.676767676768 0 0 5e-08 
0.05 0.686868686869 0 0 5e-08 
1.0 0.686868686869 0 0 5e-08 
0.05 0.69696969697 0 0 5e-08 
1.0 0.69696969697 0 0 5e-08 
0.05 0.707070707071 0 0 5e-08 
1.0 0.707070707071 0 0 5e-08 
0.05 0.717171717172 0 0 5e-08 
1.0 0.717171717172 0 0 5e-08 
0.05 0.727272727273 0 0 5e-08 
1.0 0.727272727273 0 0 5e-08 
0.05 0.737373737374 0 0 5e-08 
1.0 0.737373737374 0 0 5e-08 
0.05 0.747474747475 0 0 5e-08 
1.0 0.747474747475 0 0 5e-08 
0.05 0.757575757576 0 0 5e-08 
1.0 0.757575757576 0 0 5e-08 
0.05 0.767676767677 0 0 5e-08 
1.0 0.767676767677 0 0 5e-08 
0.05 0.777777777778 0 0 5e-08 
1.0 0.777777777778 0 0 5e-08 
0.05 0.787878787879 0 0 5e-08 
1.0 0.787878787879 0 0 5e-08 
0.05 0.79797979798 0 0 5e-08 
1.0 0.79797979798 0 0 5e-08 
0.05 0.808080808081 0 0 5e-08 
1.0 0.808080808081 0 0 5e-08 
0.05 0.818181818182 0 0 5e-08 
1.0 0.818181818182 0 0 5e-08 
0.05 0.828282828283 0 0 5e-08 
1.0 0.828282828283 0 0 5e-08 
0.05 0.838383838384 0 0 5e-08 
1.0 0.838383838384 0 0 5e-08 
0.05 0.848484848485 0 0 5e-08 
1.0 0.848484848485 0 0 5e-08 
0.05 0.858585858586 0 0 5e-08 
1.0 0.858585858586 0 0 5e-08 
0.05 0.868686868687 0 0 5e-08 
1.0 0.868686868687 0 0 5e-08 
0.05 0.878787878788 0 0 5e-08 
1.0 0.878787878788 0 0 5e-08 
0.05 0.888888888889 0 0 5e-08 
1.0 0.888888888889 0 0 5e-08 
0.05 0.89898989899 0 0 5e-08 
1.0 0.89898989899 0 0 5e-08 
0.05 0.909090909091 0 0 5e-08 
1.0 0.909090909091 0 0 5e-08 
0.05 0.919191919192 0 0 5e-08 
1.0 0.919191919192 0 0 5e-08 
0.05 0.929292929293 0 0 5e-08 
1.0 0.929292929293 0 0 5e-08 
0.05 0.939393939394 0 0 5e-08 
1.0 0.939393939394 0 0 5e-08 
0.05 0.949494949495 0 0 5e-08 
1.0 0.949494949495 0 0 5e-08 
0.05 0.959595959596 0 0 5e-08 
1.0 0.959595959596 0 0 5e-08 
0.05 0.969696969697 0 0 5e-08 
1.0 0.969696969697 0 0 5e-08 
0.05 0.979797979798 0 0 5e-08 
1.0 0.979797979798 0 0 5e-08 
0.05 0.989898989899 0 0 5e-08 
1.0 0.989898989899 0 0 5e-08 
0.05 1.0 0 0 5e-08 
1.0 1.0 0 0 5e-08 
.ENDDATA 
.dc sweep DATA = datadc 
.print dc X1:Ids X1:qs 
.end