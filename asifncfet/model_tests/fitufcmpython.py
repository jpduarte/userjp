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
fit1.updateparameter('modelcardpath',rootfolder+'/userjp/asifncfet/modelcards/modecardpmosfinfetasif.txt')
#add path to folder which will contain simulation files
fit1.updateparameter('fitfolder',rootfolder+'/userjp/asifncfet/fitdata/')
fit1.updateparameter('alldatafile','alldatatofit.txt')
fit1.updateparameter('paramtoinclude',['Vd', 'Vg', 'Vs', 'Vb','Id','Lg','Ig'])#TODO: do this automatic in case file with data is ready
fit1.updateparameter('fitresultfilename','initialresult.txt')
fit1.updateparameter('vartosave',['Ids'])
fit1.updateparameter('nodes',['Vd', 'Vg', 'Vs', 'Vb'])
fit1.updateparameter('dcbiases',[[-0.05,-0.5,-0.9], np.linspace(-0.9,0,100), [0], [0]]) #
fit1.updateparameter('deviceparameter',[])
fit1.updateparameter('deviceparametervalue',[])
fit1.updateparameter('modelcardpathfinal',rootfolder+'/userjp/asifncfet/modelcards/modecardpmosfinfetasifFINAL.txt')

'''#uncomment this to load data to a single file, this is done only once
fit1.resetdata()
datapathandfile = rootfolder+'/userjp/asifncfet/data/ID_VG_NCp90nm_Vdd_50mV.txt'
fit1.adddata(datapathandfile, ['Vs','Vb','Lg','Vd'], ['0.0','0.0','70e-9','-0.05'])
datapathandfile = rootfolder+'/userjp/asifncfet/data/ID_VG_NCp90nm_Vdd_500mV.txt'
fit1.adddata(datapathandfile, ['Vs','Vb','Lg','Vd'], ['0.0','0.0','70e-9','-0.5'])
datapathandfile = rootfolder+'/userjp/asifncfet/data/ID_VG_NCp90nm_Vdd_900mV.txt'
fit1.adddata(datapathandfile, ['Vs','Vb','Lg','Vd'], ['0.0','0.0','70e-9','-0.9'])
'''
fit1.updateparameter('biasrange', [[-0.04,-0.06],[-1,-0.6],[-0.1,0.1],[-0.1,0.1]])
fit1.updateparameter('deviceparameterrange', [[60e-9,90e-9]])
fit1.updateparameter('vartofitdata', ['Id'])
fit1.updateparameter('vartofitmodel', ['Ids'])
fit1.updateparameter('paramtofit', ['tins','Lg'])

################################fit model
fit1.fitparameters()

###############################run simulation for initial and final
fit1.runsim(fit1.modelcardpath)
#update name for results, TODO: change this name, its confusing
fit1.updateparameter('fitresultfilename','finalresult.txt')
fit1.runsim(fit1.modelcardpathfinal)

##############################plot results
P1 = plotgeneral.plotgeneral()

#plot experimental results
P1.updateparameter('symbol','o') 
pathandfile = fit1.fitfolder+fit1.alldatafile
P1.plotfiledata(pathandfile,'Vg','Id',1)

#plot model with initial parameters
P1.updateparameter('symbol','-') 
pathandfile = fit1.fitfolder+fit1.fitresultfilename
P1.plotfiledata(pathandfile,'Vg','Ids',1)

#plot model with fitted parameters
P1.updateparameter('symbol','--') 
pathandfile = fit1.fitfolder+fit1.fitresultfilename
P1.plotfiledata(pathandfile,'Vg','Ids',1)
###############################plot ends
plt.show() 
