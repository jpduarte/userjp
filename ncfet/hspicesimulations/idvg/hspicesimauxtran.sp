*script to generate hspice simulation using cmdp, Juan Duarte 
*Date: 08/05/2016, time: 22:51:39

.option abstol=1e-6 reltol=1e-6 post ingold 
.option ABSV=1e-6 
.option measform=1 
.temp 27 

.hdl "/users/jpduarte/research/BSIMCMG/code/bsimcmg.va" 
.include "/users/jpduarte/research/userjp/ncfet/modelcards/internal_14nm.nmos" 

.PARAM Vd_value = 0.5 
*.PARAM Vg_value = 0 
.PARAM Vs_value = 0 
.PARAM Vb_value = 0 
.PARAM L_value = 2e-08 
.PARAM alpha1_P_value = -3249270000.0 
.PARAM alpha11_P_value = 2.41166e+13 
.PARAM t_FE_value = 10.0e-9 
.PARAM rhofe_value = 0.5

Vd Vd 0.0 dc = Vd_value 
Vg Vg 0.0 PULSE (0 0.5 1ns 2ns 2ns 2ns 8ns) *dc = Vg_value 
Vs Vs 0.0 dc = Vs_value 
Vb Vb 0.0 dc = Vb_value 

X1 Vd Vg Vs Vb nmos1 L = 'L_value' alpha1_P = 'alpha1_P_value' alpha11_P = 'alpha11_P_value' t_FE = 't_FE_value' rhofe = 'rhofe_value'


*.dc sweep DATA = datadc 
.tr 0.05ns 8ns
.print tr v(Vg) X1:Ids X1:qm X1:vfes X1:vfed X1:qms X1:qmd X1:idsperum X1:vgs_noswap X1:vgs_out
.end
