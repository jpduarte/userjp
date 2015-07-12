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
sim1.updateparameter('modelcardpath',rootfolder+'/cmdp/userjp/project1/modelcards/modecartsmc900nm.txt')
#add path to folder which will contain simulation files
sim1.updateparameter('simulationfolder',rootfolder+'/cmdp/userjp/project1/pythonsimulations/idvg/')
#define simulation file name
sim1.updateparameter('simfilename','pythonsimaux')
#define simulation final results file 
sim1.updateparameter('simresultfilename','pythonsimauxresult.txt')
#include node names in the order defined in verilog code
sim1.updateparameter('nodes',['Vd', 'Vg', 'Vs', 'Vb'])
#values for bias conditions of nodes
sim1.updateparameter('dcbiases',[np.linspace(0.0,0.0,1), np.linspace(0.0,1,100), [0], [0]])
#device parameters defined to sweep in simulation
sim1.updateparameter('deviceparameter',['QMFACTORCV'])
#device parameter values for simulation
sim1.updateparameter('deviceparametervalue',[[0,0.75]])
sim1.updateparameter('vartosave',['Qg','qd'])#no ok: CBGSI

###########################################################################
##################Simulation Excecution####################################
###########################################################################
sim1.runsim()
Vx = 'Vg'

#plot
P1 = plotgeneral.plotgeneral()
pathandfile = sim1.simulationfolder + sim1.simresultfilename
#plot
P1.updateparameter('derivativeorder',1)
P1.plotfiledata(pathandfile,Vx,sim1.vartosave[1],2)
#plot derivative, 1 indicates derivative order
P1.updateparameter('symbol','-') 
P1.updateparameter('derivativeorder',1)
P1.updateparameter('lw',3)
P1.plotfiledata(pathandfile,Vx,sim1.vartosave[0],1)


pathfile = '/home/juan/research/cmdp/userjp/project1/data/tsmc900pmos/vgscgg900pmos.txt'
P1.updateparameter('derivativeorder',0)
P1.updateparameter('symbol','o') 
P1.updateparameter('lw',2)
P1.plotfiledata(pathfile,'Vgs','Cgg',1)

ax = plt.gca()
ax.set_ylabel('Cgg',fontsize=18) 
ax.set_xlabel('Vg',fontsize=18) 
plt.xticks(fontsize = 15)
plt.yticks(fontsize = 15)
plt.legend(['QM model: Off', 'QM model: On', 'Measurement'],loc=2)

ax.set_xlim([0,1])
ax.yaxis.set_ticklabels([])
plt.savefig('CggQMvsCL.png', dpi=300, bbox_inches='tight')
#ax.set_ylim([ymin,ymax])

plt.show() 
