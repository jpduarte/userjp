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
fit1.updateparameter('modelcardpath',rootfolder+'/userjp/asifncfetv2/modelcards/modecard250nmNFIT2.txt')
#add path to folder which will contain simulation files
fit1.updateparameter('fitfolder',rootfolder+'/userjp/asifncfetv2/fitdata/')
fit1.updateparameter('alldatafile','alldatatofit250nm.txt')
fit1.updateparameter('inputfileformat','asifdata')
fit1.updateparameter('paramtoinclude',['VG', 'VD', 'IG', 'ID', 'IS', 'VS','VB','Lg'])#TODO: do this automatic in case file with data is ready
fit1.updateparameter('simulationresultsfilename','simulation250nm.txt')
fit1.updateparameter('vartosave',['Ids','Qg'])
fit1.updateparameter('nodes',['VD', 'VG', 'VS', 'VB'])
fit1.updateparameter('dcbiases',[[-0.05,-0.2,-0.3,-0.5,-0.7,-0.95], np.linspace(-2,0,100), [0], [0]]) #
fit1.updateparameter('deviceparameter',[])
fit1.updateparameter('deviceparametervalue',[])
fit1.runsim(fit1.modelcardpath)

#uncomment this to load data to a single file, this is done only once
fit1.resetdata()
pathallfiles = '/home/juan/research/userjp/asifncfetv2/data/250nm/'
fit1.addalldatainfolder(pathallfiles, ['VS','VB','Lg'], ['0.0','0.0','250e-9'])


#first cycle
fit1.updateparameter('biasrange', [[-0.04,-1],[-2,-0.4],[-0.1,0.1],[-0.1,0.1]])
fit1.updateparameter('deviceparameterrange', [[60e-9,90e-9]])
fit1.updateparameter('vartofitdata', ['ID'])
fit1.updateparameter('vartofitmodel', ['Ids'])
fit1.updateparameter('paramtofit', ['vsat','Rs','ul'])#,
fit1.updateparameter('modelcardpathfinal',rootfolder+'/userjp/asifncfetv2/modelcards/modecard250nmNFIT2.txt')

##############################plot results
P1 = plotgeneral.plotgeneral()

#plot experimental results
P1.updateparameter('symbol','o') 
P1.updateparameter('lw',3) 
pathandfile = fit1.fitfolder+fit1.alldatafile
P1.plotfiledata(pathandfile,'VG','ID',1)

#plot model with initial parameters
P1.updateparameter('symbol','-') 
fit1.updateparameter('simulationresultsfilename','simulation250nm.txt')
pathandfile = fit1.fitfolder+fit1.simulationresultsfilename
P1.plotfiledata(pathandfile,'VG','Ids',1)

P1.updateparameter('symbol','-') 
fit1.updateparameter('simulationresultsfilename','simulation250nm.txt')
pathandfile = fit1.fitfolder+fit1.simulationresultsfilename
P1.plotfiledata(pathandfile,'VG','Qg',3)
#################################################################log scales
P1.updateparameter('ylogflag',1) 
P1.updateparameter('symbol','o') 
pathandfile = fit1.fitfolder+fit1.alldatafile
P1.plotfiledata(pathandfile,'VG','ID',2)

#plot model with initial parameters
P1.updateparameter('symbol','-') 
fit1.updateparameter('simulationresultsfilename','simulation250nm.txt')
pathandfile = fit1.fitfolder+fit1.simulationresultsfilename
P1.plotfiledata(pathandfile,'VG','Ids',2)

###############################plot ends
plt.show() 
