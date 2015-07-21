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
sim1.updateparameter('modelpath','/users/jpduarte/research/BSIMCMG/workingcode/bsimcmg.va')
#add path to model card of device under study
sim1.updateparameter('modelcardpath',rootfolder+'/userjp/ncfet/modelcards/modelcard.nmos')
#add path to folder which will contain simulation files
sim1.updateparameter('simulationfolder',rootfolder+'/userjp/ncfet/hspicesimulations/idvg/')
#define simulation file name
sim1.updateparameter('simfilename','hspicesimauxnc')
#define simulation final results file 
sim1.updateparameter('simresultfilename','hspicesimauxresultnc.txt')
#include node names in the order defined in verilog code
sim1.updateparameter('nodes',['Vd', 'Vg', 'Vs', 'Vb'])
#values for bias conditions of nodes
sim1.updateparameter('dcbiases',[np.linspace(0.05,0.3,2), np.linspace(0.0,0.3,100), [0], [0]])
#device parameters defined to sweep in simulation
sim1.updateparameter('deviceparameter',['L'])
#device parameter values for simulation
sim1.updateparameter('deviceparametervalue',[[1000e-9]])
#add variables to save
sim1.updateparameter('vartosave',['Ids','Qg','E_FE','V_FE'])

###########################################################################
##################Simulation Run###########################################
###########################################################################
sim1.runsim()
sim1.updateparameter('simresultfilename','hspicesimauxresultnc.txt')
#plot
P1 = plotgeneral.plotgeneral()
pathandfile = sim1.simulationfolder + sim1.simresultfilename
P1.updateparameter('symbol','o')
P1.updateparameter('lw',2)
P1.plotfiledata(pathandfile,'Vg','Ids',1)
P1.updateparameter('ylogflag',1)
P1.plotfiledata(pathandfile,'Vg','Ids',2)

P1.updateparameter('ylogflag',0)
P1.plotfiledata(pathandfile,'Vg','Qg',3)

P1.plotfiledata(pathandfile,'Vg','E_FE',4)

P1.plotfiledata(pathandfile,'Qg','E_FE',5)

P1.plotfiledata(pathandfile,'Vg','V_FE',6)

P1.plotfiledata(pathandfile,'Qg','V_FE',7)

sim1.updateparameter('simresultfilename','hspicesimauxresult.txt')
pathandfile = sim1.simulationfolder + sim1.simresultfilename
P1.updateparameter('symbol','-')
P1.updateparameter('lw',2)
P1.plotfiledata(pathandfile,'Vg','Ids',1)
P1.updateparameter('ylogflag',1)
P1.plotfiledata(pathandfile,'Vg','Ids',2)

P1.updateparameter('ylogflag',0)
P1.plotfiledata(pathandfile,'Vg','Qg',3)

P1.plotfiledata(pathandfile,'Vg','E_FE',4)

P1.plotfiledata(pathandfile,'Qg','E_FE',5)

P1.plotfiledata(pathandfile,'Vg','V_FE',6)

P1.plotfiledata(pathandfile,'Qg','V_FE',7)

plt.show() 
