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
sim1.updateparameter('modelcardpath',rootfolder+'/userjp/project4/modelcards/modelcardsimplev2.pmos')
#add path to folder which will contain simulation files
sim1.updateparameter('simulationfolder',rootfolder+'/userjp/project4/hspicesimulations/idvg/')
#define simulation file name
sim1.updateparameter('simfilename','hspicesimaux')
#define simulation final results file
sim1.updateparameter('simresultfilename','hspicesimauxresult.txt')
#include node names in the order defined in verilog code
sim1.updateparameter('nodes',['Vd', 'Vgf', 'Vs', 'Vgb'])
#values for bias conditions of nodes
sim1.updateparameter('dcbiases',[ np.linspace(-5,-5,1), np.arange(-5,5,0.1), [0],  np.linspace(-5,5,11)])
#sim1.updateparameter('dcbiases',[np.linspace(0.1,1,10), np.linspace(1.5,1.5,1), [0], [0]])
#sim1.updateparameter('dcbiases',[np.linspace(-1,1,100), np.linspace(1,1,1), [0], [2]])
#[np.linspace(0.2,0.2,1), np.linspace(0,2,100), [0], [2]])
#
#device parameters defined to sweep in simulation
sim1.updateparameter('deviceparameter',['L'])
#device parameter values for simulation
sim1.updateparameter('deviceparametervalue',[[50e-9]]) #TODO: fix parameter sweep, it is not working, seems it must be declare in the device part
#add variables to save
sim1.updateparameter('vartosave',['aux6qi','aux5qi','aux1qi','aux2qi','aux3qi','aux4qi','phisolution','phibsnew','phisats','xg1s','xg2s','IDS','qicores','qicoresaux','f1s','df1s','qsqrt1s','qicore1s','qicore2s','qsqrt2s','qsqrt3s','qsqrt4s','qsqrt5s','qsqrt0s','qicored','qicoreguessd','differenceaux','xg1','xg2','phisguesssf','phisguesssb','phifsnew'])#no ok: CBGSI ,'phifdnew','vbgs'
#sim1.updateparameter('vartosave',['qsqrtaux1s','qsqrtaux2s','qsqrtaux3s','qsqrtaux4s',])#no ok: CBGSI ,'phifdnew','vbgs'
###########################################################################
##################Simulation Excecution####################################
###########################################################################
sim1.runsim()
Vx = 'Vgf'

#plot
P1 = plotgeneral.plotgeneral()
pathandfile = sim1.simulationfolder + sim1.simresultfilename
#plot



P1.updateparameter('ylogflag',0)
P1.updateparameter('symbol','-')
P1.plotfiledata(pathandfile,Vx,'IDS',1)

P1.updateparameter('ylogflag',1)
P1.updateparameter('symbol','-')
P1.plotfiledata(pathandfile,Vx,'IDS',2)

P1.updateparameter('ylogflag',0)
P1.updateparameter('symbol','-')
P1.plotfiledata(pathandfile,Vx,'qicores',3)

P1.updateparameter('ylogflag',0)
P1.updateparameter('symbol','--')
P1.plotfiledata(pathandfile,Vx,'qicored',3)

P1.updateparameter('ylogflag',1)
P1.updateparameter('symbol','-')
P1.plotfiledata(pathandfile,Vx,'qicores',4)

P1.updateparameter('ylogflag',1)
P1.updateparameter('symbol','--')
P1.plotfiledata(pathandfile,Vx,'qicored',4)



P1.updateparameter('ylogflag',0)
P1.updateparameter('symbol','-')
P1.updateparameter('color','k')
P1.plotfiledata(pathandfile,Vx,'qsqrt0s',7)
P1.updateparameter('ylogflag',0)
P1.updateparameter('symbol','-')
P1.updateparameter('color','r')
P1.plotfiledata(pathandfile,Vx,'qsqrt1s',7)
P1.updateparameter('ylogflag',0)
P1.updateparameter('symbol','-')
P1.updateparameter('color','b')
P1.plotfiledata(pathandfile,Vx,'qsqrt2s',7)
P1.updateparameter('ylogflag',0)
P1.updateparameter('symbol','-')
P1.updateparameter('color','g')
P1.plotfiledata(pathandfile,Vx,'qsqrt3s',7)
P1.updateparameter('ylogflag',0)
P1.updateparameter('symbol','--')
P1.updateparameter('color','k')
P1.plotfiledata(pathandfile,Vx,'qsqrt4s',7)
P1.updateparameter('ylogflag',0)
P1.updateparameter('symbol','--')
P1.updateparameter('color','r')
P1.plotfiledata(pathandfile,Vx,'qsqrt5s',7)



P1.updateparameter('ylogflag',0)
P1.updateparameter('symbol','--')
P1.updateparameter('color','r')
P1.plotfiledata(pathandfile,Vx,'phisguesssf',8)


P1.updateparameter('ylogflag',0)
P1.updateparameter('symbol','-.')
P1.updateparameter('color','b')
P1.plotfiledata(pathandfile,Vx,'phisguesssb',8)

P1.updateparameter('ylogflag',0)
P1.updateparameter('symbol','-')
P1.updateparameter('color','r')
P1.plotfiledata(pathandfile,Vx,'phifsnew',8)


P1.updateparameter('ylogflag',0)
P1.updateparameter('symbol','-')
P1.updateparameter('color','b')
P1.plotfiledata(pathandfile,Vx,'phibsnew',8)

P1.updateparameter('ylogflag',0)
P1.updateparameter('symbol','.')
P1.plotfiledata(pathandfile,Vx,'phisolution',8)



plt.show()


'''xg2=100,xg1=-25
xg2=7 xg1= -14
xg1min =  ((-14+25)/(7-100))*(xg2-7)-14 '''
