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
P1 = plotgeneral.plotgeneral()
pathandfile = '/users/jpduarte/research/userjp/ncfet/hspicesimulations/idvg/hspicesimauxtranresultFE10nmFGrho025.txt'
P1.updateparameter('symbol','>-')
P1.updateparameter('lw',2)
P1.plotfiledata(pathandfile,'sweepvar','idsperum',1)

P1.plotfiledata(pathandfile,'sweepvar','vgs_noswap',2)

P1.plotfiledata(pathandfile,'vgs_out','idsperum',3)


P1.plotfiledata(pathandfile,'sweepvar','vgs_out',2)

P1 = plotgeneral.plotgeneral()
pathandfile = '/users/jpduarte/research/userjp/ncfet/hspicesimulations/idvg/hspicesimauxtranresultFE10nmFGrho05_2.txt'
P1.updateparameter('symbol','<-')
P1.updateparameter('lw',2)
P1.plotfiledata(pathandfile,'sweepvar','idsperum',1)

P1.plotfiledata(pathandfile,'sweepvar','vgs_noswap',2)

P1.plotfiledata(pathandfile,'vgs_out','idsperum',3)


P1.plotfiledata(pathandfile,'sweepvar','vgs_out',2)


P1 = plotgeneral.plotgeneral()
pathandfile = '/users/jpduarte/research/userjp/ncfet/hspicesimulations/idvg/hspicesimauxtranresultnominal.txt'
P1.updateparameter('symbol','o-')
P1.updateparameter('lw',2)
P1.plotfiledata(pathandfile,'sweepvar','idsperum',1)

P1.plotfiledata(pathandfile,'sweepvar','vgs_noswap',2)

P1.plotfiledata(pathandfile,'vgs_noswap','idsperum',3)


P1.plotfiledata(pathandfile,'sweepvar','vgs_noswap',2)

P1 = plotgeneral.plotgeneral()
pathandfile = '/users/jpduarte/research/userjp/ncfet/hspicesimulations/idvg/hspicesimauxtranresultFE10nmFG2.txt'
P1.updateparameter('symbol','s-')
P1.updateparameter('lw',2)
P1.plotfiledata(pathandfile,'sweepvar','idsperum',1)

P1.plotfiledata(pathandfile,'sweepvar','vgs_noswap',2)

P1.plotfiledata(pathandfile,'vgs_out','idsperum',3)


P1 = plotgeneral.plotgeneral()
pathandfile = '/users/jpduarte/research/userjp/ncfet/hspicesimulations/idvg/hspicesimauxtranresultFE10nm.txt'
P1.updateparameter('symbol','*-')
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
