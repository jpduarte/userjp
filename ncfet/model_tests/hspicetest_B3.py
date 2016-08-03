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
sim1.updateparameter('modelpath','/users/jpduarte/research/BSIMCMG/code/bsimcmg.va')
#add path to model card of device under study
sim1.updateparameter('modelcardpath','/users/jpduarte/research/userjp/ncfet/modelcards/modelcard_nc.nmos')
#add path to folder which will contain simulation files
sim1.updateparameter('simulationfolder',rootfolder+'/userjp/ncfet/hspicesimulations/idvg/')
#define simulation file name
sim1.updateparameter('simfilename','hspicesimaux')
#define simulation final results file 
sim1.updateparameter('simresultfilename','hspicesimauxresult.txt')
#include node names in the order defined in verilog code
sim1.updateparameter('nodes',['Vd', 'Vg', 'Vs', 'Vb'])
#values for bias conditions of nodes
sim1.updateparameter('dcbiases',[[0.5],np.concatenate((np.linspace(0,1.0,100),np.linspace(1.0,0,100)),axis=0) , [0], [0]])#np.linspace(0,1.0,100)
#device parameters defined to sweep in simulation
sim1.updateparameter('deviceparameter',['L','alpha1_P','alpha11_P','t_FE','EOT','PHIG'])#,'TFIN','NFIN','NRS','NRD'])#TFIN=15n L=30n NFIN=10 NRS=1 NRD=1
#device parameter values for simulation
sim1.updateparameter('deviceparametervalue',[[30000e-9*5],[-5.1e9],[6.1166e+11],[1.0e-9],[0.9e-9],[4.41]])#
#sim1.updateparameter('deviceparametervalue',[[30000e-9*6],[-5.1e9],[6.1166e+11],[5e-9],[0.9e-9],[4.41]])#,[15e-9],[10],[1],[1]]) 100e-9,200e-9,300e-9
#add variables to save
sim1.updateparameter('vartosave',['idsnomal','qm','vfes','vfed','vgs','QGI'])#,'I1aux','I2aux','I3aux','Ib1aux','Ib2aux','Ib3aux','I4aux','Ib4aux'])

sim1.updateparameter('abstol','1e-6')
sim1.updateparameter('reltol','1e-2')
sim1.updateparameter('absv','1e-1')
###########################################################################
##################Simulation Run###########################################
###########################################################################
sim1.runsim()
sim1.hspicetotex('x','y')

P1 = plotgeneral.plotgeneral()
pathandfile = '/users/jpduarte/research/userjp/ncfet/FE-HZOvd0p1V.txt'
P1.updateparameter('ylogflag',1)
P1.updateparameter('lw',2)
P1.updateparameter('symbol','o')
P1.plotfiledata(pathandfile,'vg','id',2)

#plot
P1 = plotgeneral.plotgeneral()
pathandfile = sim1.simulationfolder + sim1.simresultfilename



P1.updateparameter('symbol','-')
P1.updateparameter('lw',5)
P1.updateparameter('ylogflag',1)
P1.plotfiledata(pathandfile,'Vg','idsnomal',2)


plt.show() 
