import matplotlib.pyplot as plt
import matplotlib
matplotlib.rc('xtick', labelsize=15)
matplotlib.rc('ytick', labelsize=15)
import numpy as np
import os
import sys
cwd = os.getcwd()

utilspath = cwd + '/../utils/'
sys.path.append(utilspath)
import utils

basefolder = '/Users/romain/work/Auger/EASIER/data/meas/board/20160201/measure1/'
filename = basefolder + 'C1-25dbm00006.txt'

print filename
data = utils.readscopewf(filename)

plt.plot(data[0]*1e6,data[1])
plt.xlabel('time [us]',fontsize=15)
plt.ylabel('amplitude [V]',fontsize=15)
plt.show()
