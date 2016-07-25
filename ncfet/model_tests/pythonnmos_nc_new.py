#example: run hspice Id-Vg using python
#Juan Duarte, BSIM Group

rootfolder = '/home/bsim2015/research'

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
sim1.updateparameter('modelpath',rootfolder+'/cmdp/compactmodels/UFCM_nc_newguess.py')
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
sim1.updateparameter('dcbiases',[[0.05], np.linspace(0.0,1.5,100), [0], [0]])
#device parameters defined to sweep in simulation
sim1.updateparameter('deviceparameter',['Lg','a0','b0','c0','cgsfe'])
#device parameter values for simulation

sim1.updateparameter('deviceparametervalue',[[100e-9],[-0.99],[0.01],[0.0],[3.0]])#[0.0],[0.00],[0.000]])#,0.005
#add variables to save  
sim1.updateparameter('vartosave',['qs','qs0','qs1','qs2','qs3','vfe1','vfe2','vfe3','delta1','delta2','delta3','qmfe','qmlin','qmfe1','qmfe3','qmguess','qgsfe','vfe'])#no ok: CBGSI


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
P1.updateparameter('symbol','-')
P1.plotfiledata(pathandfile,Vx,'qs',3)

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
P1.updateparameter('symbol','-')
P1.plotfiledata(pathandfile,Vx,'qs',4)


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
P1.updateparameter('symbol','.')
P1.plotfiledata(pathandfile,Vx,'vfe3',6)

##########################################

P1.updateparameter('derivativeorder',0)
P1.updateparameter('ylogflag',0)
P1.updateparameter('symbol','.')
P1.plotfiledata(pathandfile,Vx,'qgsfe',7)



P1.updateparameter('derivativeorder',0)
P1.updateparameter('ylogflag',0)
P1.updateparameter('symbol','.')
<<<<<<< HEAD
P1.plotfiledata(pathandfile,Vx,'vfe',8)
=======
P1.plotfiledata(pathandfile,Vx,'qgsfe',8)
>>>>>>> 746792a0db4e7c44cfb758df04441e86cb80b1bc


plt.show() 
