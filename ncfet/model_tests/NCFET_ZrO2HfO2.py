#example: run hspice Id-Vg using python
#Juan Duarte, BSIM Group

rootfolder = '/home/juan/research'
#rootfolder = '/home/bsim2015/research'
#indicate path for folders containing required classes
import sys
sys.path.insert(0, rootfolder+'/cmdp/pycsimsupport')
sys.path.insert(0, rootfolder+'/cmdp/plotscripts')
#import class for python simulation
import pycsimpython
import plotgeneral
import numpy as np
import matplotlib.pyplot as plt
###########################################################################
##################Basic Definitions########################################
###########################################################################
#TODO: add simulator name, make it generic between simulators
#creates pycsimpython class
sim1 = pycsimpython.pycsimpython('idvg')
#add path to verilog code with model, TODO: include case where model is already incorporated to simulator
sim1.updateparameter('modelpath',rootfolder+'/cmdp/compactmodels/UFCM_nc_FEIS_Ids.py')
#add path to model card of device under study
sim1.updateparameter('modelcardpath',rootfolder+'/userjp/ncfet/modelcards/modecardncfet.txt')
#add path to folder which will contain simulation files
sim1.updateparameter('simulationfolder',rootfolder+'/userjp/ncfet/pythonsimulations/idvg/')
#define simulation file name
sim1.updateparameter('simfilename','pythonsimaux')
#define simulation final results file 
sim1.updateparameter('simresultfilename','pythonsimauxresult.txt')
#include node names in the order defined in verilog code
sim1.updateparameter('nodes',['Vd', 'Vg', 'Vs', 'Vb'])
#values for bias conditions of nodes
sim1.updateparameter('dcbiases',[[0.1], np.concatenate((np.linspace(0,1.0,200),np.linspace(1.0,0,200)),axis=0), [0], [0]])
#device parameters defined to sweep in simulation
sim1.updateparameter('deviceparameter',['Lg','PHIG','TFIN','HFIN','tins','alpha1_P','alpha11_P','cgsfe','t_FE','gauss_n','SSrolloff'])
#device parameter values for simulation
sim1.updateparameter('deviceparametervalue',[[30000e-9],[4.7],[1.4e-8],[3.0e-8],[0.3e-9],[-3e9],[6.1166e+11],[0],[5e-9],[100],[1.0]])#,600e-9, 0,200e-9,300e-9,400e-9,
#add variables to save  
sim1.updateparameter('vartosave',['qs','vfe','qmguess','q0','q1','q2','q3','q4','ids0'])#no ok: CBGSI

###########################################################################
##################Simulation Excecution####################################
###########################################################################
sim1.runsim()
Vx = 'Vg'

#plot
P1 = plotgeneral.plotgeneral()
pathandfile = sim1.simulationfolder + sim1.simresultfilename
#plot

P1.updateparameter('ylogflag',0)
P1.updateparameter('lw',2)
P1.updateparameter('symbol','o-')
P1.plotfiledata(pathandfile,Vx,'qs',1)

P1.updateparameter('derivativeorder',0)
P1.updateparameter('lw',2)
P1.updateparameter('symbol','^-')
P1.plotfiledata(pathandfile,Vx,'qmguess',1)

'''P1.updateparameter('derivativeorder',0)
P1.updateparameter('ylogflag',0)
P1.updateparameter('symbol','--')
P1.plotfiledata(pathandfile,Vx,'qmguess',3)
P1.updateparameter('derivativeorder',0)
P1.updateparameter('ylogflag',0)
P1.updateparameter('symbol','-.')
P1.plotfiledata(pathandfile,Vx,'qmfe',3)'''
#####################################33

P1.updateparameter('derivativeorder',0)
P1.updateparameter('ylogflag',1)
P1.updateparameter('lw',2)
P1.updateparameter('symbol','o-')
P1.plotfiledata(pathandfile,Vx,'qs',2)



P1.updateparameter('derivativeorder',0)
P1.updateparameter('ylogflag',1)
P1.updateparameter('lw',2)
P1.updateparameter('symbol','-')
P1.plotfiledata(pathandfile,Vx,'qmguess',2)



'''P1.updateparameter('derivativeorder',0)
P1.updateparameter('ylogflag',1)
P1.updateparameter('symbol','-.')
P1.plotfiledata(pathandfile,Vx,'qmfe',4)
P1.updateparameter('derivativeorder',0)
P1.updateparameter('ylogflag',1)
P1.updateparameter('symbol','--')
P1.plotfiledata(pathandfile,Vx,'qmguess',4)'''
'''P1.updateparameter('derivativeorder',0)
P1.updateparameter('ylogflag',0)
P1.updateparameter('symbol','o')
P1.plotfiledata(pathandfile,Vx,'qs0',5)
P1.updateparameter('derivativeorder',0)
P1.updateparameter('ylogflag',0)
P1.updateparameter('symbol','--')
P1.plotfiledata(pathandfile,Vx,'qs1',5)
P1.updateparameter('derivativeorder',0)
P1.updateparameter('ylogflag',0)
P1.updateparameter('symbol','-.')
P1.plotfiledata(pathandfile,Vx,'qs2',5)
P1.updateparameter('derivativeorder',0)
P1.updateparameter('ylogflag',0)
P1.updateparameter('symbol','.')
P1.plotfiledata(pathandfile,Vx,'qs3',5)
P1.updateparameter('derivativeorder',0)
P1.updateparameter('ylogflag',0)
P1.updateparameter('symbol','*')
P1.plotfiledata(pathandfile,Vx,'qmfe',5)
P1.updateparameter('derivativeorder',0)
P1.updateparameter('ylogflag',0)
P1.updateparameter('symbol','o')
P1.plotfiledata(pathandfile,Vx,'qmfe1',5)
P1.updateparameter('derivativeorder',0)
P1.updateparameter('ylogflag',0)
P1.updateparameter('symbol','>')
P1.plotfiledata(pathandfile,Vx,'qmfe3',5) 
P1.updateparameter('derivativeorder',0)
P1.updateparameter('ylogflag',0)
P1.updateparameter('symbol','>')
P1.plotfiledata(pathandfile,Vx,'qmlin',5)'''



##########################################

'''P1.updateparameter('derivativeorder',0)
P1.updateparameter('ylogflag',0)
P1.updateparameter('symbol','--')
P1.plotfiledata(pathandfile,Vx,'vfe1',6)
P1.updateparameter('derivativeorder',0)
P1.updateparameter('ylogflag',0)
P1.updateparameter('symbol','-.')
P1.plotfiledata(pathandfile,Vx,'vfe2',6)'''

P1.updateparameter('derivativeorder',0)
P1.updateparameter('ylogflag',0)
P1.updateparameter('symbol','o-')
P1.plotfiledata(pathandfile,Vx,'vfe',3)

P1.updateparameter('derivativeorder',0)
P1.updateparameter('ylogflag',0)
P1.updateparameter('lw',2)
P1.updateparameter('symbol','o-')
P1.plotfiledata(pathandfile,'vfe','qs',4)



##########################################
'''
P1.updateparameter('derivativeorder',0)
P1.updateparameter('ylogflag',0)
P1.updateparameter('symbol','--')
P1.plotfiledata(pathandfile,Vx,'delta1',7)
P1.updateparameter('derivativeorder',0)
P1.updateparameter('ylogflag',0)
P1.updateparameter('symbol','-.')
P1.plotfiledata(pathandfile,Vx,'delta2',7)
P1.updateparameter('derivativeorder',0)
P1.updateparameter('ylogflag',0)
P1.updateparameter('symbol','.')
P1.plotfiledata(pathandfile,Vx,'delta3',7)
P1.updateparameter('derivativeorder',0)
P1.updateparameter('ylogflag',0)
P1.updateparameter('symbol','.')
P1.plotfiledata(pathandfile,Vx,'qgsfe',8)'''

P1.updateparameter('ylogflag',0)
P1.updateparameter('lw',2)
P1.updateparameter('symbol','o-')
P1.plotfiledata(pathandfile,Vx,'q0',5)
P1.updateparameter('symbol','o-')
P1.plotfiledata(pathandfile,Vx,'q1',5)
P1.updateparameter('symbol','o-')
P1.plotfiledata(pathandfile,Vx,'q2',5)
P1.updateparameter('symbol','o-')
P1.plotfiledata(pathandfile,Vx,'q3',5)
P1.updateparameter('symbol','o-')
P1.plotfiledata(pathandfile,Vx,'q4',5)

P1.updateparameter('symbol','o-')
P1.plotfiledata(pathandfile,Vx,'ids0',6)

P1.updateparameter('ylogflag',1)
P1.updateparameter('symbol','o-')
P1.plotfiledata(pathandfile,Vx,'ids0',7)

plt.show() 
