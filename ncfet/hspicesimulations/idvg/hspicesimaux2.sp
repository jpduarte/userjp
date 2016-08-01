*script to generate hspice simulation using cmdp, Juan Duarte 
*Date: 07/27/2016, time: 13:51:00

.option abstol=1e-6 reltol=1e-6 post ingold 
.option ABSV=1e-6 
.option measform=1 
.temp 27 

.hdl "/users/jpduarte/research/BSIMCMG/code/bsimcmg.va" 
.include "//users/jpduarte/research/userjp/ncfet/modelcards/modelcard_nc.nmos" 

.PARAM Vd_value = 0 
.PARAM Vg_value = 0 
.PARAM Vs_value = 0 
.PARAM Vb_value = 0 
.PARAM L_value = 3e-08 
.PARAM alpha1_P_value = -84927000.0 
.PARAM alpha11_P_value = 611660000000.0 
.PARAM t_FE_value = 0 

Vd Vd 0.0 dc = Vd_value 
Vg Vg 0.0 dc = Vg_value 
Vs Vs 0.0 dc = Vs_value 
Vb Vb 0.0 dc = Vb_value 

X1 Vd Vg Vs Vb nmos1 L = 'L_value' alpha1_P = 'alpha1_P_value' alpha11_P = 'alpha11_P_value' t_FE = 't_FE_value'

.DATA datadc Vd_value Vg_value Vs_value Vb_value L_value alpha1_P_value alpha11_P_value t_FE_value 
0.5 0.0 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.0204081632653 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.0408163265306 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.0612244897959 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.0816326530612 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.102040816327 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.122448979592 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.142857142857 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.163265306122 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.183673469388 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.204081632653 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.224489795918 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.244897959184 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.265306122449 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.285714285714 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.30612244898 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.326530612245 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.34693877551 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.367346938776 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.387755102041 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.408163265306 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.428571428571 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.448979591837 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.469387755102 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.489795918367 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.510204081633 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.530612244898 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.551020408163 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.571428571429 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.591836734694 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.612244897959 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.632653061224 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.65306122449 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.673469387755 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.69387755102 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.714285714286 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.734693877551 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.755102040816 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.775510204082 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.795918367347 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.816326530612 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.836734693878 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.857142857143 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.877551020408 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.897959183673 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.918367346939 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.938775510204 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.959183673469 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.979591836735 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 1.0 0 0 3e-08 -84927000.0 611660000000.0 0.0 
0.5 0.0 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.0204081632653 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.0408163265306 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.0612244897959 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.0816326530612 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.102040816327 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.122448979592 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.142857142857 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.163265306122 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.183673469388 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.204081632653 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.224489795918 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.244897959184 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.265306122449 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.285714285714 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.30612244898 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.326530612245 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.34693877551 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.367346938776 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.387755102041 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.408163265306 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.428571428571 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.448979591837 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.469387755102 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.489795918367 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.510204081633 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.530612244898 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.551020408163 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.571428571429 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.591836734694 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.612244897959 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.632653061224 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.65306122449 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.673469387755 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.69387755102 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.714285714286 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.734693877551 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.755102040816 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.775510204082 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.795918367347 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.816326530612 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.836734693878 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.857142857143 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.877551020408 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.897959183673 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.918367346939 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.938775510204 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.959183673469 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.979591836735 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 1.0 0 0 3e-08 -84927000.0 611660000000.0 1e-07 
0.5 0.0 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.0204081632653 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.0408163265306 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.0612244897959 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.0816326530612 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.102040816327 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.122448979592 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.142857142857 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.163265306122 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.183673469388 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.204081632653 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.224489795918 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.244897959184 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.265306122449 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.285714285714 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.30612244898 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.326530612245 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.34693877551 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.367346938776 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.387755102041 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.408163265306 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.428571428571 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.448979591837 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.469387755102 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.489795918367 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.510204081633 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.530612244898 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.551020408163 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.571428571429 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.591836734694 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.612244897959 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.632653061224 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.65306122449 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.673469387755 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.69387755102 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.714285714286 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.734693877551 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.755102040816 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.775510204082 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.795918367347 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.816326530612 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.836734693878 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.857142857143 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.877551020408 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.897959183673 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.918367346939 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.938775510204 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.959183673469 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.979591836735 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 1.0 0 0 3e-08 -84927000.0 611660000000.0 2e-07 
0.5 0.0 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 0.0204081632653 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 0.0408163265306 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 0.0612244897959 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 0.0816326530612 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 0.102040816327 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 0.122448979592 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 0.142857142857 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 0.163265306122 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 0.183673469388 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 0.204081632653 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 0.224489795918 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 0.244897959184 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 0.265306122449 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 0.285714285714 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 0.30612244898 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 0.326530612245 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 0.34693877551 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 0.367346938776 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 0.387755102041 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 0.408163265306 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 0.428571428571 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 0.448979591837 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 0.469387755102 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 0.489795918367 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 0.510204081633 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 0.530612244898 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 0.551020408163 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 0.571428571429 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 0.591836734694 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 0.612244897959 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 0.632653061224 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 0.65306122449 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 0.673469387755 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 0.69387755102 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 0.714285714286 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 0.734693877551 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 0.755102040816 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 0.775510204082 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 0.795918367347 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 0.816326530612 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 0.836734693878 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 0.857142857143 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 0.877551020408 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 0.897959183673 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 0.918367346939 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 0.938775510204 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 0.959183673469 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 0.979591836735 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
0.5 1.0 0 0 3e-08 -84927000.0 611660000000.0 3e-07 
.ENDDATA 
.dc sweep DATA = datadc 
.print dc X1:ids X1:qis X1:vfes X1:vfed X1:vgs 
.end