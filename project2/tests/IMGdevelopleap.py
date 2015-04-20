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
sim1.updateparameter('modelpath','/users/jpduarte/BSIM_CM_Matlab/BSIM_model_development_v2/DM_Verilog_Hspice/Models_Verilog/BSIMIMG/code/bsimimg.va')
#add path to model card of device under study
sim1.updateparameter('modelcardpath','/users/jpduarte/research/cmdp/userjp/project2/modelcards/leapmodelcard.nmos')
#add path to folder which will contain simulation files
sim1.updateparameter('simulationfolder',rootfolder+'/cmdp/userjp/project2/hspicesimulations/idvg/')
#define simulation file name
sim1.updateparameter('simfilename','hspicesimaux')
#define simulation final results file 
sim1.updateparameter('simresultfilename','hspicesimauxresult.txt')
#include node names in the order defined in verilog code
sim1.updateparameter('nodes',['Vd', 'Vgf', 'Vs', 'Vgb'])
#values for bias conditions of nodes
sim1.updateparameter('dcbiases',[[0.05], np.linspace(0.0,1,100), [0], [-1,0,1]])
#sim1.updateparameter('dcbiases',[np.linspace(0.1,1,10), np.linspace(1.5,1.5,1), [0], [0]])
#sim1.updateparameter('dcbiases',[np.linspace(-1,1,100), np.linspace(1,1,1), [0], [2]])
#[np.linspace(0.2,0.2,1), np.linspace(0,2,100), [0], [2]])
#
#device parameters defined to sweep in simulation
sim1.updateparameter('deviceparameter',['L'])
#device parameter values for simulation
sim1.updateparameter('deviceparametervalue',[[1000e-9]])
#add variables to save  
#sim1.updateparameter('vartosafe',['CFGFGI','CBGFGI','CDFGI','CSFGI']) #ok
sim1.updateparameter('vartosafe',['IDS','qtotd','qtots','CDDI'])#no ok: CBGSI
#sim1.updateparameter('vartosafe',['CDDI','CDFGI','CDSI','CDBGI']) #ok
#sim1.updateparameter('vartosafe',['CFGDI','CFGFGI','CFGSI','CFGBGI']) # no ok: CFGDI
#sim1.updateparameter('vartosafe',['CBGDI','CBGFGI','CBGSI','CBGBGI']) #no ok: CBGSI
#sim1.updateparameter('vartosafe',['QFGI','QBGI','QDI','QSI'])
#sim1.updateparameter('vartosafe',['qtotd','qtots','Ids','vgs_noswap'])
#sim1.updateparameter('vartosafe',['caux1','caux2','caux3','Ids'])
#sim1.updateparameter('vartosafe',['CBGSI','CFGDI','CFGFGI','Ids'])

###########################################################################
##################Simulation Excecution####################################
###########################################################################
sim1.runhspice()
Vx = 'Vgf'

#plot
P1 = plotgeneral.plotgeneral()
pathandfile = sim1.simulationfolder + sim1.simresultfilename
#plot
P1.updateparameter('ylogflag',0)
P1.updateparameter('symbol','o')
P1.updateparameter('color','b')
P1.plotfiledata(pathandfile,Vx,sim1.vartosafe[0],1)
P1.updateparameter('color','r')
P1.updateparameter('ylogflag',1)
P1.plotfiledata(pathandfile,Vx,sim1.vartosafe[0],2)
P1.updateparameter('ylogflag',0)
P1.updateparameter('symbol','o')
P1.updateparameter('color','b')
P1.plotfiledata(pathandfile,Vx,sim1.vartosafe[1],3)
P1.updateparameter('symbol','o')
P1.updateparameter('color','b')
P1.plotfiledata(pathandfile,Vx,sim1.vartosafe[2],4)


############################################################################
sim1.updateparameter('modelpath','/users/jpduarte/BSIM_CM_Matlab/BSIM_model_development_v2/DM_Verilog_Hspice/Models_Verilog/BSIMIMGref/code/bsimimg.va')
sim1.updateparameter('simulationfolder',rootfolder+'/cmdp/userjp/project2/hspicesimulations/idvgref/')
sim1.runhspice()
pathandfile = sim1.simulationfolder + sim1.simresultfilename
#plot
P1.updateparameter('ylogflag',0)
P1.updateparameter('symbol','o')
P1.updateparameter('color','k')
P1.plotfiledata(pathandfile,Vx,sim1.vartosafe[0],1)
P1.updateparameter('color','k')
P1.updateparameter('ylogflag',1)
P1.plotfiledata(pathandfile,Vx,sim1.vartosafe[0],2)
P1.updateparameter('ylogflag',0)
P1.updateparameter('symbol','o')
P1.updateparameter('color','k')
P1.plotfiledata(pathandfile,Vx,sim1.vartosafe[1],3)
P1.updateparameter('symbol','o')
P1.updateparameter('color','k')
P1.plotfiledata(pathandfile,Vx,sim1.vartosafe[2],4)

plt.show() 
