import matplotlib.pyplot as plt
import numpy as np
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
meanarray = np.array([])
pinarray = np.array([])
for power in range(-33,-10):
    files = glob.glob(basefolder + '*' + str(power)+ '*.txt')
    thewf = wf.Wf(files[0])
    thewf.filldata()
    meanarray = np.append(meanarray, thewf.getmean())
    pinarray = np.append(pinarray,power)
    


plt.plot(pinarray,meanarray)
plt.show()


