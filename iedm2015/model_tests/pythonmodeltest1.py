#example: run hspice Id-Vg using python
#Juan Duarte, BSIM Group

rootfolder = '/home/juan/research'

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
sim1.updateparameter('modelpath',rootfolder+'/cmdp/compactmodels/UFCM.py')
#add path to model card of device under study
sim1.updateparameter('modelcardpath',rootfolder+'/userjp/iedm2015/modelcards/modecardintel14nm.txt')
#add path to folder which will contain simulation files
sim1.updateparameter('simulationfolder',rootfolder+'/userjp/iedm2015/pythonsimulations/idvg/')
#define simulation file name
sim1.updateparameter('simfilename','pythonsimaux')
#define simulation final results file 
sim1.updateparameter('simresultfilename','pythonsimauxresult.txt')
#include node names in the order defined in verilog code
sim1.updateparameter('nodes',['Vd', 'Vg', 'Vs', 'Vb'])
#values for bias conditions of nodes
sim1.updateparameter('dcbiases',[np.linspace(0.05,0.7,2), np.linspace(0.0,0.7,100), [0], [0]])
#sim1.updateparameter('dcbiases',[np.linspace(-0.05,0.7,100), np.linspace(0.7,0.7,1), [0], [0]])
#device parameters defined to sweep in simulation
sim1.updateparameter('deviceparameter',['Lg'])
#device parameter values for simulation
sim1.updateparameter('deviceparametervalue',[[20e-9]])#10e-9,15e-9,20e-9,30e-9,50e-9,100e-9
#add variables to save  
sim1.updateparameter('vartosave',['Ids','qs','qd','vedrain','vesource','qdsat','vedrainsat'])#no ok: CBGSI

###########################################################################
##################Simulation Excecution####################################
###########################################################################
sim1.runsim()
Vx = 'Vg'

#plot
P1 = plotgeneral.plotgeneral()
pathandfile = sim1.simulationfolder + sim1.simresultfilename
#plot
P1.updateparameter('symbol','-') 
P1.updateparameter('lw',5)
P1.plotfiledata(pathandfile,Vx,sim1.vartosave[0],1)

P1.updateparameter('ylogflag',0)
P1.updateparameter('derivativeorder',0)
P1.updateparameter('lw',2)
P1.plotfiledata(pathandfile,Vx,sim1.vartosave[1],3)
P1.updateparameter('symbol','-')
P1.plotfiledata(pathandfile,Vx,sim1.vartosave[2],7)

P1.updateparameter('ylogflag',1)
P1.plotfiledata(pathandfile,Vx,sim1.vartosave[0],5)

P1.updateparameter('ylogflag',0)
P1.plotfiledata(pathandfile,Vx,sim1.vartosave[3],6)
P1.updateparameter('symbol','--')
P1.plotfiledata(pathandfile,Vx,sim1.vartosave[4],6)

P1.updateparameter('ylogflag',0)
P1.updateparameter('symbol','--')
P1.plotfiledata(pathandfile,Vx,sim1.vartosave[5],7)

P1.updateparameter('ylogflag',0)
P1.updateparameter('symbol','--')
P1.plotfiledata(pathandfile,Vx,sim1.vartosave[1],8)

plt.show() 
