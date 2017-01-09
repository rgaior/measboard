import matplotlib.pyplot as plt
import matplotlib
matplotlib.rc('xtick', labelsize=15)
matplotlib.rc('ytick', labelsize=15)
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

#fit part:
pmin = -34
pmax = -9
newparray = parray[ (parray > pmin) & (parray < pmax) ]
newmeanarray = meanarray[ (parray > pmin) & (parray < pmax) ]
xfit = np.arange(pmin,pmax,1)
fit = np.polyfit(newparray,newmeanarray,1)
p = np.poly1d(fit)
pfit = p(xfit)
fig = plt.figure(figsize=(8,8))
ax = plt.subplot(111)
ax.plot(parray,meanarray,'o')
ax.plot(xfit, pfit,'k',lw=2)
xline = np.arange(parray[0],parray[-1],1)
ax.plot(xline,np.zeros(len(xline)),'r--')
ax.plot(xline,-2*np.ones(len(xline)),'r--')

ax.text(0.95, 0.90, 'fit: f = ' + str("%.4f" % fit[0]) + '*P_dBm' + ' + ' + str("%.2f" % fit[1]) + 'V',
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='black', fontsize=15)

#plt.plot(parray,stdarray,'o')
ax.set_xlabel('input power [dBm]',fontsize=15)
ax.set_ylabel('output amp. [V]',fontsize=15)
plt.show()



