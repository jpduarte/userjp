#example: run hspice Id-Vg using python
#Juan Duarte, BSIM Group

rootfolder = '/users/jpduarte/research'

#indicate path for folders containing required classes
import sys
sys.path.insert(0, rootfolder+'/cmdp/hspicesupport')
sys.path.insert(0, rootfolder+'/cmdp/plotscripts')
#import class for hspice-python simulation
import hspicepython
import plotgeneral
import numpy as np
import matplotlib.pyplot as plt
###########################################################################
##################Basic Definitions########################################
###########################################################################
#TODO: add simulator name, make it generic between simulators
#creates hspice python class
sim1 = hspicepython.hspicepython('idvg')
#add path to verilog code with model, TODO: include case where model is already incorporated to simulator
sim1.updateparameter('modelpath','/users/jpduarte/research/BSIMIMG/code/bsimimg.va')
#add path to model card of device under study
#sim1.updateparameter('modelcardpath','/users/jpduarte/research/cmdp/userjp/project4/modelcards/leapmodelcard.nmos')
sim1.updateparameter('modelcardpath',rootfolder+'/userjp/project4/modelcards/modelcardsimple.nmos')
#add path to folder which will contain simulation files
sim1.updateparameter('simulationfolder',rootfolder+'/userjp/project4/hspicesimulations/idvg/')
#define simulation file name
sim1.updateparameter('simfilename','hspicesimaux')
#define simulation final results file
sim1.updateparameter('simresultfilename','hspicesimauxresult.txt')
#include node names in the order defined in verilog code
sim1.updateparameter('nodes',['Vd', 'Vgf', 'Vs', 'Vgb'])
#values for bias conditions of nodes
sim1.updateparameter('dcbiases',[ np.arange(0,1,0.01), np.linspace(1,1,1), [0],  np.linspace(0,0,1)])
#sim1.updateparameter('dcbiases',[np.linspace(0.1,1,10), np.linspace(1.5,1.5,1), [0], [0]])
#sim1.updateparameter('dcbiases',[np.linspace(-1,1,100), np.linspace(1,1,1), [0], [2]])
#[np.linspace(0.2,0.2,1), np.linspace(0,2,100), [0], [2]])
#
#device parameters defined to sweep in simulation
sim1.updateparameter('deviceparameter',['L'])
#device parameter values for simulation
sim1.updateparameter('deviceparametervalue',[[1000e-9,500e-9,100e-9,55e-9,24e-9]]) #TODO: fix parameter sweep, it is not working, seems it must be declare in the device part
#add variables to save
sim1.updateparameter('vartosave',['IDS','vds'])#no ok: CBGSI ,'phifdnew','vbgs'
#sim1.updateparameter('vartosave',['qsqrtaux1s','qsqrtaux2s','qsqrtaux3s','qsqrtaux4s',])#no ok: CBGSI ,'phifdnew','vbgs'
###########################################################################
##################Simulation Excecution####################################
###########################################################################
sim1.runsim()
Vx = 'Vd'

#plot
P1 = plotgeneral.plotgeneral()
pathandfile = sim1.simulationfolder + sim1.simresultfilename
#plot
P1.updateparameter('ylogflag',0)
P1.updateparameter('symbol','-')
P1.plotfiledata(pathandfile,Vx,sim1.vartosave[0],1)
P1.updateparameter('ylogflag',1)
P1.updateparameter('symbol','-')
P1.plotfiledata(pathandfile,Vx,sim1.vartosave[0],2)
P1.updateparameter('ylogflag',0)
P1.updateparameter('symbol','-')
P1.plotfiledata(pathandfile,Vx,sim1.vartosave[1],2)

plt.show()

'''xg2=100,xg1=-25
xg2=7 xg1= -14
xg1min =  ((-14+25)/(7-100))*(xg2-7)-14 '''
