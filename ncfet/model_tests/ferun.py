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
sim1.updateparameter('modelpath','/users/jpduarte/research/userjp/ncfet/models/fecm.va')
#add path to model card of device under study
sim1.updateparameter('modelcardpath','/users/jpduarte/research/userjp/ncfet/modelcards/modelcard_fe.fe')
#add path to folder which will contain simulation files
sim1.updateparameter('simulationfolder',rootfolder+'/userjp/ncfet/hspicesimulations/idvg/')
#define simulation file name
sim1.updateparameter('simfilename','hspicesimaux')
#define simulation final results file 
sim1.updateparameter('simresultfilename','hspicesimauxresult.txt')
#include node names in the order defined in verilog code
sim1.updateparameter('nodes',['Vp', 'Vn'])
#values for bias conditions of nodes
sim1.updateparameter('dcbiases',[np.concatenate((np.linspace(0,10.0,50),np.linspace(10.0,-10,50),np.linspace(-10,10.0,50)),axis=0) , [0]])
#device parameters defined to sweep in simulation
sim1.updateparameter('deviceparameter',['r','a0','b0'])
#device parameter values for simulation
sim1.updateparameter('deviceparametervalue',[[1],[-1],[0.1]])
#add variables to save
sim1.updateparameter('vartosave',['qfe','vfe'])

sim1.updateparameter('abstol','1e-6')
sim1.updateparameter('reltol','1e-6')
sim1.updateparameter('absv','1e-2')
###########################################################################
##################Simulation Run###########################################
###########################################################################
sim1.runsim()
sim1.hspicetotex('x','y')#,sim1.allvaldc)

#plot
P1 = plotgeneral.plotgeneral()
pathandfile = sim1.simulationfolder + sim1.simresultfilename
P1.updateparameter('symbol','o-')
P1.updateparameter('lw',2)
P1.plotfiledata(pathandfile,'Vp','qfe',1)

P1.updateparameter('symbol','o-')
P1.updateparameter('lw',2)
P1.plotfiledata(pathandfile,'vfe','qfe',2)


plt.show() 
