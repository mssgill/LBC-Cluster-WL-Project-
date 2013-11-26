# Nov 2013                                                                      
# Code JCY orig wrote to make some histos of the ellip, modified by MG                                

import numpy as np
import matplotlib.pyplot as plt
#import pylab as P

# Read in file                                                                                       
# in_file = 'singlepsf_output.py.txt'
in_file = 'singlepsf_output.redd'
dat = np.genfromtxt(in_file)

# Print e1 and e2 avgs to screen                                                                      
print np.average(dat[:,3]),np.average(dat[:,4])
print len(dat[:,3])

# Make the plot of where the objs are -- causing an illegal instruction on my Slac machine as of Nov 25,2013, but works fine locally on Ubuntu machine           
fig = plt.figure()                                                                                   
ax  = fig.add_subplot(111)
ax.plot(dat[:,1],dat[:,2], '.')                                                                      
# ax.plot(dat[:,0],dat[:,1], '.')                                                                      
plt.show()                                                                                           

# Make a histo of e1                                                                                  
plt.figure()
plt.hist(dat[:,3], 50, histtype='step', fill=True)
# plt.hist(dat[:,2], 50, histtype='step', fill=True)
plt.show()

# Make a histo of e2                                                                                  
plt.figure()                                                                                        
plt.hist(dat[:,4], 50, histtype='step', fill=True)                                                  
# plt.hist(dat[:,3], 50, histtype='step', fill=True)                                                  
plt.show()                                                                                          


