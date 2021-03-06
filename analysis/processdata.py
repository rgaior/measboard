import matplotlib.pyplot as plt
import numpy as np
import pickle
import os
import sys
cwd = os.getcwd()
import glob

utilspath = cwd + '/../utils/'
sys.path.append(utilspath)
import utils
classpath = cwd + '/../classes/'
sys.path.append(classpath)
import wf

basefolder = '/Users/romain/work/Auger/EASIER/data/meas/board/20160201/measure1/'
baseout = '/Users/romain/work/Auger/EASIER/LPSC/measboard/data/20160201/measure1/'
meanarray = np.array([])
pinarray = np.array([],dtype=int)
pinarray = np.append(pinarray,np.array([-40,-38,-36,-34]))
pinarray = np.append(pinarray,np.arange(-33,-9,1))
pinarray.astype(int)
print pinarray
for pin in pinarray:
    files = glob.glob(basefolder + '*' + str(pin)+ 'dbm0*'+ '*.txt')
#    print files
    for f in files:
        print f
        thewf = wf.Wf(f)
        thewf.process()
        thewf.pin = pin
        outname = baseout + 'pin_'+str(pin)+'_' +str(thewf.fileit) + '.wf'
        pickle.dump(thewf, open( outname, "w" ) )






