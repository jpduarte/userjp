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
sim1.updateparameter('modelpath','/users/jpduarte/research/userjp/project3/models/res.va')
#add path to model card of device under study
sim1.updateparameter('modelcardpath','/users/jpduarte/research/userjp/project3/model_cards/modelcardR.res')
#add path to folder which will contain simulation files
sim1.updateparameter('simulationfolder',rootfolder+'/userjp/project3/hspicesimulations/IV/')
#define simulation file name
sim1.updateparameter('simfilename','resistancesimaux')
#define simulation final results file 
sim1.updateparameter('simresultfilename','resistancesimresultaux.txt')
#include node names in the order defined in verilog code
sim1.updateparameter('nodes',['Vp', 'Vn'])
#values for bias conditions of nodes
sim1.updateparameter('dcbiases',[np.linspace(0.0,1,10), [0.0]])
#device parameters defined to sweep in simulation
sim1.updateparameter('deviceparameter',['L'])
#device parameter values for simulation
sim1.updateparameter('deviceparametervalue',[[1000e-9]])
#add variables to save  
#sim1.updateparameter('vartosafe',['xfinal1','xdirect1','xfinal2','xdirect1'])
sim1.updateparameter('vartosave',['dxfinaldVp1','dxdirectdVp1','dxfinaldVp2','dxdirectdVp2'])

###########################################################################
##################Simulation Excecution####################################
###########################################################################
print sim1
sim1.runsim()
Vx = 'Vp'

#plot
P1 = plotgeneral.plotgeneral()
pathandfile = sim1.simulationfolder + sim1.simresultfilename
#plot
P1.updateparameter('ylogflag',0)
P1.updateparameter('symbol','s')
P1.updateparameter('color','b')
P1.plotfiledata(pathandfile,Vx,sim1.vartosafe[0],1)
P1.updateparameter('symbol','-')
P1.plotfiledata(pathandfile,Vx,sim1.vartosafe[1],1)
P1.updateparameter('symbol','>')
P1.updateparameter('color','g')
P1.plotfiledata(pathandfile,Vx,sim1.vartosafe[2],1)
P1.updateparameter('symbol','o')
P1.updateparameter('color','c')
P1.plotfiledata(pathandfile,Vx,sim1.vartosafe[3],1)
#P1.plotfiledata(pathandfile,Vx,sim1.vartosafe[2],1)

plt.show() 
