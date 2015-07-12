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
fit1.updateparameter('modelcardpath',rootfolder+'/userjp/asifncfetv2/modelcards/modecardpmosfinfetasif.txt')
#add path to folder which will contain simulation files
fit1.updateparameter('fitfolder',rootfolder+'/userjp/asifncfetv2/fitdata/')
fit1.updateparameter('alldatafile','alldatatofit.txt')
fit1.updateparameter('paramtoinclude',['Vd', 'Vg', 'Vs', 'Vb','Id','Lg','Ig'])#TODO: do this automatic in case file with data is ready
fit1.updateparameter('simulationresultsfilename','initialresult.txt')
fit1.updateparameter('vartosave',['Ids'])
fit1.updateparameter('nodes',['Vd', 'Vg', 'Vs', 'Vb'])
fit1.updateparameter('dcbiases',[[-0.05,-0.5,-0.9], np.linspace(-0.9,0,100), [0], [0]]) #
fit1.updateparameter('deviceparameter',[])
fit1.updateparameter('deviceparametervalue',[])
fit1.runsim(fit1.modelcardpath)

#first cycle
fit1.updateparameter('biasrange', [[-0.04,-1],[-1,-0.4],[-0.1,0.1],[-0.1,0.1]])
fit1.updateparameter('deviceparameterrange', [[60e-9,90e-9]])
fit1.updateparameter('vartofitdata', ['Id'])
fit1.updateparameter('vartofitmodel', ['Ids'])
fit1.updateparameter('paramtofit', ['vsat','Rs','ul'])#,
fit1.updateparameter('modelcardpathfinal',rootfolder+'/userjp/asifncfetv2/modelcards/modecardpmosfinfetasifFINAL1.txt')

################################fit model 1
fit1.fitparameters()
'''
fit1.updateparameter('modelcardpath',rootfolder+'/userjp/asifncfetv2/modelcards/modecardpmosfinfetasifFINAL1.txt')
fit1.updateparameter('paramtofit', ['vsat','Rs','ul','QMFACTORCV'])#,
fit1.updateparameter('modelcardpathfinal',rootfolder+'/userjp/asifncfetv2/modelcards/modecardpmosfinfetasifFINAL2.txt')
################################fit model 2
fit1.fitparameters()'''
###############################run simulation for initial and final

#update name for results, TODO: change this name, its confusing
fit1.updateparameter('simulationresultsfilename','finalresult.txt')
fit1.runsim(fit1.modelcardpathfinal)

##############################plot results
P1 = plotgeneral.plotgeneral()

#plot experimental results
P1.updateparameter('symbol','o') 
pathandfile = fit1.fitfolder+fit1.alldatafile
P1.plotfiledata(pathandfile,'Vg','Id',1)

#plot model with initial parameters
P1.updateparameter('symbol','-') 
fit1.updateparameter('simulationresultsfilename','initialresult.txt')
pathandfile = fit1.fitfolder+fit1.simulationresultsfilename
P1.plotfiledata(pathandfile,'Vg','Ids',1)
#plot model with fitted parameters
P1.updateparameter('symbol','--')
fit1.updateparameter('simulationresultsfilename','finalresult.txt') 
pathandfile = fit1.fitfolder+fit1.simulationresultsfilename
P1.plotfiledata(pathandfile,'Vg','Ids',1)

P1.updateparameter('ylogflag',1) 
P1.updateparameter('symbol','o') 
pathandfile = fit1.fitfolder+fit1.alldatafile
P1.plotfiledata(pathandfile,'Vg','Id',2)

#plot model with initial parameters
P1.updateparameter('symbol','-') 
fit1.updateparameter('simulationresultsfilename','initialresult.txt')
pathandfile = fit1.fitfolder+fit1.simulationresultsfilename
P1.plotfiledata(pathandfile,'Vg','Ids',2)

#plot model with fitted parameters
P1.updateparameter('symbol','--')
fit1.updateparameter('simulationresultsfilename','finalresult.txt') 
pathandfile = fit1.fitfolder+fit1.simulationresultsfilename
P1.plotfiledata(pathandfile,'Vg','Ids',2)
###############################plot ends
plt.show() 
