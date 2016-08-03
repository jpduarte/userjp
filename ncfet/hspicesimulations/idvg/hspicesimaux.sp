*script to generate hspice simulation using cmdp, Juan Duarte 
*Date: 08/02/2016, time: 23:27:06

.option abstol=1e-6 reltol=1e-6 post ingold 
.option ABSV=1e-3 
.option measform=1 
.temp 27 

.hdl "/users/jpduarte/research/BSIMCMG/code/bsimcmg.va" 
.include "/users/jpduarte/research/userjp/ncfet/modelcards/internal_14nmpmos.nmos" 

.PARAM Vd_value = 0 
.PARAM Vg_value = 0 
.PARAM Vs_value = 0 
.PARAM Vb_value = 0 
.PARAM L_value = 2e-08 
.PARAM alpha1_P_value = -3249270000.0 
.PARAM alpha11_P_value = 2.41166e+13 
.PARAM t_FE_value = 1e-08 

Vd Vd 0.0 dc = Vd_value 
Vg Vg 0.0 dc = Vg_value 
Vs Vs 0.0 dc = Vs_value 
Vb Vb 0.0 dc = Vb_value 

X1 Vd Vg Vs Vb nmos1 L = 'L_value' alpha1_P = 'alpha1_P_value' alpha11_P = 'alpha11_P_value' t_FE = 't_FE_value'

.DATA datadc Vd_value Vg_value Vs_value Vb_value L_value alpha1_P_value alpha11_P_value t_FE_value 
-0.05 0.0 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 0.0 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.00707070707071 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.00707070707071 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.0141414141414 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.0141414141414 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.0212121212121 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.0212121212121 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.0282828282828 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.0282828282828 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.0353535353535 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.0353535353535 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.0424242424242 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.0424242424242 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.0494949494949 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.0494949494949 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.0565656565657 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.0565656565657 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.0636363636364 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.0636363636364 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.0707070707071 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.0707070707071 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.0777777777778 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.0777777777778 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.0848484848485 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.0848484848485 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.0919191919192 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.0919191919192 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.0989898989899 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.0989898989899 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.106060606061 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.106060606061 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.113131313131 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.113131313131 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.120202020202 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.120202020202 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.127272727273 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.127272727273 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.134343434343 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.134343434343 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.141414141414 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.141414141414 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.148484848485 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.148484848485 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.155555555556 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.155555555556 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.162626262626 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.162626262626 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.169696969697 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.169696969697 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.176767676768 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.176767676768 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.183838383838 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.183838383838 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.190909090909 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.190909090909 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.19797979798 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.19797979798 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.205050505051 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.205050505051 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.212121212121 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.212121212121 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.219191919192 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.219191919192 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.226262626263 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.226262626263 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.233333333333 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.233333333333 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.240404040404 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.240404040404 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.247474747475 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.247474747475 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.254545454545 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.254545454545 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.261616161616 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.261616161616 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.268686868687 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.268686868687 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.275757575758 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.275757575758 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.282828282828 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.282828282828 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.289898989899 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.289898989899 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.29696969697 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.29696969697 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.30404040404 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.30404040404 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.311111111111 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.311111111111 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.318181818182 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.318181818182 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.325252525253 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.325252525253 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.332323232323 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.332323232323 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.339393939394 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.339393939394 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.346464646465 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.346464646465 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.353535353535 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.353535353535 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.360606060606 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.360606060606 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.367676767677 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.367676767677 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.374747474747 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.374747474747 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.381818181818 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.381818181818 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.388888888889 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.388888888889 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.39595959596 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.39595959596 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.40303030303 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.40303030303 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.410101010101 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.410101010101 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.417171717172 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.417171717172 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.424242424242 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.424242424242 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.431313131313 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.431313131313 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.438383838384 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.438383838384 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.445454545455 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.445454545455 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.452525252525 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.452525252525 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.459595959596 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.459595959596 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.466666666667 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.466666666667 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.473737373737 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.473737373737 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.480808080808 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.480808080808 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.487878787879 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.487878787879 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.494949494949 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.494949494949 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.50202020202 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.50202020202 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.509090909091 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.509090909091 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.516161616162 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.516161616162 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.523232323232 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.523232323232 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.530303030303 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.530303030303 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.537373737374 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.537373737374 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.544444444444 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.544444444444 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.551515151515 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.551515151515 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.558585858586 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.558585858586 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.565656565657 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.565656565657 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.572727272727 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.572727272727 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.579797979798 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.579797979798 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.586868686869 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.586868686869 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.593939393939 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.593939393939 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.60101010101 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.60101010101 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.608080808081 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.608080808081 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.615151515152 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.615151515152 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.622222222222 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.622222222222 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.629292929293 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.629292929293 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.636363636364 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.636363636364 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.643434343434 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.643434343434 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.650505050505 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.650505050505 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.657575757576 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.657575757576 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.664646464646 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.664646464646 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.671717171717 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.671717171717 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.678787878788 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.678787878788 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.685858585859 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.685858585859 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.692929292929 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.692929292929 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.05 -0.7 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
-0.7 -0.7 0 0 2e-08 -3249270000.0 2.41166e+13 1e-08 
.ENDDATA 
.dc sweep DATA = datadc 
.print dc X1:Ids X1:qm X1:vfes X1:vfed X1:vgs X1:QGI X1:qms X1:qmd X1:qmsguesss X1:qmsguessd X1:qmfe1 X1:qmfe2 X1:vgn1 X1:vgn2 X1:idsperum 
.end