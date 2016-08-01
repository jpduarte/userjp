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
sim1.updateparameter('modelcardpath','//users/jpduarte/research/userjp/ncfet/modelcards/modelcard_nc.nmos')
#add path to folder which will contain simulation files
sim1.updateparameter('simulationfolder',rootfolder+'/userjp/ncfet/hspicesimulations/idvg/')
#define simulation file name
sim1.updateparameter('simfilename','hspicesimaux')
#define simulation final results file 
sim1.updateparameter('simresultfilename','hspicesimauxresult.txt')
#include node names in the order defined in verilog code
sim1.updateparameter('nodes',['Vd', 'Vg', 'Vs', 'Vb'])
#values for bias conditions of nodes
sim1.updateparameter('dcbiases',[[0.5],np.concatenate((np.linspace(0,1.0,50),np.linspace(1.0,0,50)),axis=0) , [0], [0]])#np.linspace(0,1.0,100)
#device parameters defined to sweep in simulation
sim1.updateparameter('deviceparameter',['L','alpha1_P','alpha11_P','t_FE',])#,'TFIN','NFIN','NRS','NRD'])#TFIN=15n L=30n NFIN=10 NRS=1 NRD=1
#device parameter values for simulation
sim1.updateparameter('deviceparametervalue',[[30e-9],[-8.4927e+07],[6.1166e+11],[900e-9]])#,[15e-9],[10],[1],[1]]) 100e-9,200e-9,300e-9
#add variables to save
sim1.updateparameter('vartosave',['Ids','qs','vfes','vfed','vgs','QGI'])#,'I1aux','I2aux','I3aux','Ib1aux','Ib2aux','Ib3aux','I4aux','Ib4aux'])

sim1.updateparameter('abstol','1e-6')
sim1.updateparameter('reltol','1e-6')
sim1.updateparameter('absv','1e-3')
###########################################################################
##################Simulation Run###########################################
###########################################################################
sim1.runsim()
sim1.hspicetotex('x','y')
#plot
P1 = plotgeneral.plotgeneral()
pathandfile = sim1.simulationfolder + sim1.simresultfilename
P1.updateparameter('symbol','-')
P1.updateparameter('lw',2)
P1.plotfiledata(pathandfile,'Vg','Ids',1)


P1.updateparameter('symbol','-')
P1.updateparameter('lw',2)
P1.updateparameter('ylogflag',1)
P1.plotfiledata(pathandfile,'Vg','Ids',2)

P1.updateparameter('ylogflag',0)
P1.updateparameter('symbol','-')
P1.updateparameter('lw',2)
P1.plotfiledata(pathandfile,'Vg','qs',3)


P1.updateparameter('symbol','-')
P1.updateparameter('lw',2)
P1.plotfiledata(pathandfile,'Vg','vfes',4)

P1.updateparameter('symbol','-')
P1.updateparameter('lw',2)
P1.plotfiledata(pathandfile,'Vg','vfed',5)

P1.updateparameter('symbol','-')
P1.updateparameter('lw',2)
P1.plotfiledata(pathandfile,'Vg','QGI',6)

'''P1.updateparameter('symbol','o')
P1.updateparameter('lw',2)
P1.plotfiledata(pathandfile,'Vg','I1aux',4)


P1.updateparameter('symbol','-')
P1.updateparameter('lw',2)
P1.plotfiledata(pathandfile,'Vg','I2aux',4)


P1.updateparameter('symbol','-.')
P1.updateparameter('lw',2)
P1.plotfiledata(pathandfile,'Vg','I3aux',4)



P1.updateparameter('symbol','o')
P1.updateparameter('lw',2)
P1.plotfiledata(pathandfile,'Vg','Ib1aux',5)


P1.updateparameter('symbol','-')
P1.updateparameter('lw',2)
P1.plotfiledata(pathandfile,'Vg','Ib2aux',5)


P1.updateparameter('symbol','-.')
P1.updateparameter('lw',2)
P1.plotfiledata(pathandfile,'Vg','Ib3aux',5)

P1.updateparameter('symbol','s')
P1.updateparameter('lw',2)
P1.plotfiledata(pathandfile,'Vg','I4aux',6)
P1.updateparameter('symbol','o')
P1.updateparameter('lw',2)
P1.plotfiledata(pathandfile,'Vg','Ib4aux',6)'''


plt.show() 
