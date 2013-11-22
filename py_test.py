import numpy as np
import matplotlib.pyplot as mplt
import pylab as P
import matplotlib.pyplot as plt

j_file = 'singlepsf_output.py.txt'
dat = np.genfromtxt(j_file)

print np.average(dat[:,3]),np.average(dat[:,4]) 

print len(dat[:,3])

fig = plt.figure()
ax  = fig.add_subplot(111)
ax.plot(dat[:,1],dat[:,2], '.')
plt.show()

plt.figure()
plt.hist(dat[:,3], 50, histtype='step', fill=True)
plt.show()

plt.figure()
plt.hist(dat[:,4], 50, histtype='step', fill=True)
plt.show()
