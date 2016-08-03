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
vmax=0.5
vmaxi=0.15
sim1.updateparameter('dcbiases',[np.concatenate((np.linspace(0,-vmaxi,50),np.linspace(0,vmaxi,50),np.linspace(vmax,-vmax,50),np.linspace(-vmax,vmax,50)),axis=0) , [0]])
#device parameters defined to sweep in simulation
sim1.updateparameter('deviceparameter',['area','alpha1_P','alpha11_P','t_FE','r'])#,'TFIN','NFIN','NRS','NRD'])#TFIN=15n L=30n NFIN=10 NRS=1 NRD=1
#device parameter values for simulation
sim1.updateparameter('deviceparametervalue',[[1e-12],[-8.4927e+07],[6.1166e+11],[300e-9],[50e3]])#,[15e-9],[10],[1],[1]])
#add variables to save
sim1.updateparameter('vartosave',['Qfe','Vfe','Pfe','Efe','Ufe'])

sim1.updateparameter('abstol','1e-6')
sim1.updateparameter('reltol','1e-6')
sim1.updateparameter('absv','1e-6')
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
P1.plotfiledata(pathandfile,'Vp','Qfe',1)

P1.updateparameter('symbol','o-')
P1.updateparameter('lw',2)
P1.plotfiledata(pathandfile,'Vfe','Qfe',2)

P1.updateparameter('symbol','o-')
P1.updateparameter('lw',2)
P1.plotfiledata(pathandfile,'Vfe','Pfe',3)

P1.updateparameter('symbol','o')
P1.updateparameter('lw',2)
P1.plotfiledata(pathandfile,'Efe','Pfe',4)

P1.updateparameter('symbol','o')
P1.updateparameter('lw',2)
P1.plotfiledata(pathandfile,'Pfe','Ufe',5)

plt.show() 
