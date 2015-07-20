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
sim1 = hspicepython.hspicepython('inverter')
#add path to folder which will contain simulation files
sim1.updateparameter('simulationfolder',rootfolder+'/userjp/ncfet/simulations/')
#define simulation file name
sim1.updateparameter('simfilename','invertertranncfet')
#define simulation final results file 
sim1.updateparameter('simresultfilename','invertertranresultncfet.txt')

sim1.hspicetotex('x','y')
###########################################################################
##################Simulation Run###########################################
###########################################################################


#plot
P1 = plotgeneral.plotgeneral()
pathandfile = sim1.simulationfolder + sim1.simresultfilename
P1.updateparameter('symbol','o-')
P1.updateparameter('lw',2)
P1.plotfiledata(pathandfile,'sweepvar(time)','vout(voltage)',1)

P1.updateparameter('symbol','s-')
P1.updateparameter('color','r')
P1.updateparameter('lw',2)
P1.plotfiledata(pathandfile,'sweepvar(time)','vin(voltage)',2)

P1.updateparameter('color','k')
P1.plotfiledata(pathandfile,'sweepvar(time)','vinaux(voltage)',2)

P1 = plotgeneral.plotgeneral()
pathandfile = sim1.simulationfolder + 'invertertranresult.txt'
P1.updateparameter('symbol','>-')
P1.updateparameter('color','c')
P1.updateparameter('lw',2)
P1.plotfiledata(pathandfile,'sweepvar(time)','vout(voltage)',1)

P1.updateparameter('symbol','<-')
P1.updateparameter('color','g')
P1.updateparameter('lw',2)
P1.plotfiledata(pathandfile,'sweepvar(time)','vin(voltage)',2)

plt.show() 






