import matplotlib.pyplot as plt
import numpy as np
import os
import sys
cwd = os.getcwd()
import glob

utilspath = cwd + '/../utils/'
sys.path.append(utilspath)
import utils

basefolder = '/Users/romain/work/Auger/EASIER/data/meas/board/20160201/measure1/'
for power in range(-33,-10):
    files = glob.glob(basefolder + '*' + str(power)+ '*.txt')
    print files
    

#filename = basefolder + 'C1-25dbm00006.txt'

#print filename
#data = utils.readscopewf(filename)

#plt.plot(data[0],data[1])
#plt.show()
