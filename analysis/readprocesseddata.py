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

baseprocdata = '/Users/romain/work/Auger/EASIER/LPSC/measboard/data/20160201/measure1/'
pinarray = np.array([],dtype=int)
pinarray= np.append(pinarray,np.array([-40,-38,-36,-34]))
pinarray = np.append(pinarray,np.arange(-33,-9,1))
pinarray.astype(int)
meanarray = np.array([])
stdarray = np.array([])
parray = np.array([])
for pin in pinarray:
    files = glob.glob(baseprocdata + '*' + str(pin)+ '*.wf')
    for f in files[:4]:
        thewf = pickle.load(open(f, "r" ) )
        meanarray = np.append(meanarray,thewf.mean)
        stdarray = np.append(stdarray,thewf.std)
        parray = np.append(parray,thewf.pin)

#plt.plot(parray,meanarray,'o')
plt.plot(parray,stdarray,'o')
plt.show()



