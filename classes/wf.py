import utils
import numpy as np

class Wf:
    def __init__(self, fname=''):
        self.fname = fname
        
        self.fileit = 0
        self.pin = 0
        self.mean = 0
        self.std = 0
        self.deltat = 0
        self.data = []

    def filldata(self):
        self.data = utils.readscopewf(self.fname)

    def setmean(self):
        self.mean = np.mean(self.data[1])

    def setstd(self):
        self.std = np.std(self.data[1])

    def emptydata(self):
        self.data = []
    def setfileit(self):
        self.fileit = int(self.fname[-9:-4])
    def process(self):
        self.filldata()
        self.setmean()
        self.setstd()
        self.setfileit()
        self.deltat = self.data[0][1] - self.data[0][0]
        self.emptydata()

