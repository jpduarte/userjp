#example: run hspice Id-Vg using python
#Juan Duarte, BSIM Group

rootfolder = '/users/jpduarte/research'

#indicate path for folders containing required classes
import sys
import os
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
sim1.updateparameter('modelcardpath','/users/jpduarte/research/userjp/ncfet/modelcards/internal_14nmpmos.nmos')
#add path to folder which will contain simulation files
sim1.updateparameter('simulationfolder',rootfolder+'/userjp/ncfet/hspicesimulations/idvg/')
#define simulation file name
sim1.updateparameter('simfilename','hspicesimauxtran')
#define simulation final results file 
sim1.updateparameter('simresultfilename','hspicesimauxtranresultFE10nmFGrho05_2.txt')
#include node names in the order defined in verilog code
sim1.updateparameter('nodes',['Vd', 'Vg', 'Vs', 'Vb'])
#values for bias conditions of nodes
sim1.updateparameter('dcbiases',[[-0.7],np.linspace(0,-0.7,100), [0], [0]])#np.linspace(0,1.0,100)
#device parameters defined to sweep in simulation
sim1.updateparameter('deviceparameter',['L','alpha1_P','alpha11_P','t_FE'])#,'TFIN','NFIN','NRS','NRD'])#TFIN=15n L=30n NFIN=10 NRS=1 NRD=1
#device parameter values for simulation
sim1.updateparameter('deviceparametervalue',[[20e-9],[-32.4927e+08],[24.1166e+12],[00.0e-9]])#,[15e-9],[10],[1],[1]]) 100e-9,200e-9,300e-9
#add variables to save
sim1.updateparameter('vartosave',['Ids','qm','vfes','vfed','vgs','QGI','qms','qmd','qmsguesss','qmsguessd','qmfe1','qmfe2', 'vgn1','vgn2','idsperum'])#

sim1.updateparameter('abstol','1e-6')
sim1.updateparameter('reltol','1e-6')
sim1.updateparameter('absv','1e-3')
###########################################################################
##################Simulation Run###########################################
###########################################################################

#sim1.runsim()
os.system('hspice ' + sim1.simulationfolder +sim1.simfilename+'.sp -o ' + sim1.simulationfolder+sim1.simfilename)
simfilename ='/users/jpduarte/research/userjp/ncfet/hspicesimulations/idvg/hspicesimauxtran.lis'
simresultfilename ='/users/jpduarte/research/userjp/ncfet/hspicesimulations/idvg/'+sim1.simresultfilename
sim1.hspicetotex2('x','y', simfilename,simresultfilename)
#plot
P1 = plotgeneral.plotgeneral()
pathandfile = simresultfilename
P1.updateparameter('symbol','o')
P1.updateparameter('lw',2)
P1.plotfiledata(pathandfile,'sweepvar','idsperum',1)

P1.plotfiledata(pathandfile,'sweepvar','vgs_noswap',2)

P1.plotfiledata(pathandfile,'vgs_noswap','idsperum',3)


P1.plotfiledata(pathandfile,'sweepvar','vgs_out',2)

pathandfile ="/users/jpduarte/research/userjp/ncfet/hspicesimulations/idvg/ULPLg14nmFE0nmvds05.txt"
P1.updateparameter('symbol','-')
P1.updateparameter('lw',2)
P1.plotfiledata(pathandfile,'Vg','idsperum',3)

plt.show() 
