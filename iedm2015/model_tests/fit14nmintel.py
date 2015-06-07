#example: run hspice Id-Vg using python
#Juan Duarte, BSIM Group

rootfolder = '/home/juan/research'

#indicate path for folders containing required classes
import sys
sys.path.insert(0, rootfolder+'/cmdp/pycsimsupport')
sys.path.insert(0, rootfolder+'/cmdp/plotscripts')
sys.path.insert(0, rootfolder+'/cmdp/fittingsupport')
#import class for python simulation
import pycsimpython
import plotgeneral
import numpy as np
import matplotlib.pyplot as plt
import fitmodel
####################################################################
#add data
##############################################################################
fit1 = fitmodel.fitmodelclass('fitexample')
fit1.updateparameter('modelpath',rootfolder+'/cmdp/compactmodels/UFCM.py')
fit1.updateparameter('modelcardpath',rootfolder+'/userjp/iedm2015/modelcards/modecardintel14nm.txt')
#add path to folder which will contain simulation files
fit1.updateparameter('fitfolder',rootfolder+'/userjp/iedm2015/fitdata/')
fit1.updateparameter('alldatafile','intel14nmdata.txt')
fit1.updateparameter('paramtoinclude',['Vd', 'Vg', 'Vs', 'Vb','Idnorm','Lg'])#TODO: do this automatic in case file with data is ready
fit1.updateparameter('simulationresultsfilename','initialresult.txt')
fit1.updateparameter('vartosave',['Idnorm'])
fit1.updateparameter('nodes',['Vd', 'Vg', 'Vs', 'Vb'])
fit1.updateparameter('dcbiases',[[0.05,0.7], np.linspace(0,0.7,100), [0], [0]]) #
fit1.updateparameter('deviceparameter',[])
fit1.updateparameter('deviceparametervalue',[])
fit1.runsim(fit1.modelcardpath)

#uncomment this to load data to a single file, this is done only once
fit1.resetdata()
datapathandfile = rootfolder+'/userjp/iedm2015/data/intel14nm/idvg14nmintel.txt'
fit1.adddata(datapathandfile, ['Vs','Vb','Lg'], ['0.0','0.0','20e-9'])

#first cycle
fit1.updateparameter('biasrange', [[0.04,1],[0.2,1],[-0.1,0.1],[-0.1,0.1]])
fit1.updateparameter('deviceparameterrange', [[60e-9,90e-9]])
fit1.updateparameter('vartofitdata', ['Idnorm'])
fit1.updateparameter('vartofitmodel', ['Idnorm'])
fit1.updateparameter('paramtofit', ['vsat','Rs','QMFACTORCV','PHIG'])#,
fit1.updateparameter('modelcardpathfinal',rootfolder+'/userjp/iedm2015/modelcards/modecardintel14nmFINAL1.txt')

################################fit model
fit1.fitparameters()

###############################run simulation for initial and final


#update name for results, TODO: change this name, its confusing
fit1.updateparameter('simulationresultsfilename','finalresult.txt')
fit1.runsim(fit1.modelcardpathfinal)

##############################plot results
P1 = plotgeneral.plotgeneral()

#plot experimental results
P1.updateparameter('symbol','o') 
pathandfile = fit1.fitfolder+fit1.alldatafile
P1.plotfiledata(pathandfile,'Vg','Idnorm',1)

P1.updateparameter('ylogflag',1) 
P1.plotfiledata(pathandfile,'Vg','Idnorm',2)

#plot model with initial parameters
P1.updateparameter('ylogflag',0) 
P1.updateparameter('symbol','-') 
fit1.updateparameter('simulationresultsfilename','initialresult.txt')
pathandfile = fit1.fitfolder+fit1.simulationresultsfilename
P1.plotfiledata(pathandfile,'Vg','Idnorm',1)
P1.updateparameter('ylogflag',1) 
P1.plotfiledata(pathandfile,'Vg','Idnorm',2)
#plot model with fitted parameters
P1.updateparameter('ylogflag',0) 
P1.updateparameter('symbol','--')
fit1.updateparameter('simulationresultsfilename','finalresult.txt') 
pathandfile = fit1.fitfolder+fit1.simulationresultsfilename
P1.plotfiledata(pathandfile,'Vg','Idnorm',1)

P1.updateparameter('ylogflag',1) 
P1.plotfiledata(pathandfile,'Vg','Idnorm',2)
###############################plot ends
plt.show() 
