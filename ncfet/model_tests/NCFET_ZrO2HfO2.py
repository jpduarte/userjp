#example: run hspice Id-Vg using python
#Juan Duarte, BSIM Group

rootfolder = '/home/bsim2015/research'
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
sim1.updateparameter('dcbiases',[[0.1], np.concatenate((np.linspace(0,1.0,100),np.linspace(1.0,0,100)),axis=0), [0], [0]])
#device parameters defined to sweep in simulation
sim1.updateparameter('deviceparameter',['Lg','PHIG','Nch','TFIN','HFIN','tins','alpha1_P','alpha11_P','cgsfe','t_FE','gauss_n','SSrolloff','ul','QMFACTORCV'])
#device parameter values for simulation
sim1.updateparameter('deviceparametervalue',[[30000e-9],[4.57],[1e17],[3e-8],[3.0e-8],[0.9e-9],[-5.1e9],[6.1166e+11],[0.0],[5e-9],[10],[0.2],[50],[0.5]])
#sim1.updateparameter('deviceparametervalue',[[30000e-9],[4.57],[1e17],[3e-8],[3.0e-8],[0.9e-9],[-5.1e9],[6.1166e+11],[0.0],[5e-9],[50],[0.2],[50],[0.5]])
#add variables to save  
sim1.updateparameter('vartosave',['qs','vfe','qmguess','q0','q1','q2','q3','q4','ids0'])#no ok: CBGSI

###########################################################################
##################Simulation Excecution####################################
###########################################################################
sim1.runsim()
Vx = 'Vg'

P1 = plotgeneral.plotgeneral()
pathandfile = '/home/bsim2015/research/userjp/ncfet/FE-HZOvd0p1V.txt'
P1.updateparameter('ylogflag',1)
P1.updateparameter('lw',2)
P1.updateparameter('symbol','o')
P1.plotfiledata(pathandfile,'vg','id',7)
#plot
P1 = plotgeneral.plotgeneral()
pathandfile = sim1.simulationfolder + sim1.simresultfilename
#plot
'''
P1.updateparameter('ylogflag',0)
P1.updateparameter('lw',2)
P1.updateparameter('symbol','o-')
P1.plotfiledata(pathandfile,Vx,'qs',1)

P1.updateparameter('derivativeorder',0)
P1.updateparameter('lw',2)
P1.updateparameter('symbol','^-')
P1.plotfiledata(pathandfile,Vx,'qmguess',1)

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



P1.updateparameter('derivativeorder',0)
P1.updateparameter('ylogflag',0)
P1.updateparameter('symbol','o-')
P1.plotfiledata(pathandfile,Vx,'vfe',3)

P1.updateparameter('derivativeorder',0)
P1.updateparameter('ylogflag',0)
P1.updateparameter('lw',2)
P1.updateparameter('symbol','o-')
P1.plotfiledata(pathandfile,'vfe','qs',4)

'''
P1.updateparameter('symbol','-')
P1.updateparameter('lw',5)
P1.plotfiledata(pathandfile,Vx,'ids0',6)

P1.updateparameter('ylogflag',1)
P1.updateparameter('symbol','-')
P1.updateparameter('lw',5)
P1.plotfiledata(pathandfile,Vx,'ids0',7)

plt.show() 
