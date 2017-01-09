import numpy as np
####################################
########     reading      ##########
####################################
#reads a ascii file: time amplitude
#header 5 lines
def readscopewf(inname):
    f = open(inname,'r')
    x = np.array([])
    y = np.array([])
    counter = 0
    header = 6
    for l in f:
#        print l
        if counter < header:
            counter +=1
            continue
        lsplit = l.split()
        x = np.append(x,float(lsplit[0]))
        y = np.append(y,float(lsplit[1]))
 #       print x, ' ' , y
    f.close()
    return [x,y]

