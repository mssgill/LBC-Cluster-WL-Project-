import sys
import os
import subprocess
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from pylab import *
import scipy.linalg
from matplotlib.font_manager import FontProperties
import numpy as np
import scipy
import random

def func(x,a,b,c):
    return a*x**2 +b*x + c #Refer [1]

def funclin(x,b,c):
    return b*x + c #Refer [1]

#j_file = 'dadimc.txt'
j_file = 'dadDEIMOS.txt'
t_data = np.genfromtxt(j_file)
X = t_data[:,0]
Y = t_data[:,1]
Yerr = t_data[:,2]

print X

lenp = len(X)
xc = np.linspace(0,lenp-1,lenp)   
yc = func(xc,0.1, 1, 2*10**-6) 
yerc = func(xc,0.1, 1,2*10**-6)
for lix in range(0,lenp):
    xc[lix] = X[lix]
    yc[lix] = Y[lix]
    yerc[lix] = Yerr[lix]
    
coeff, var_matrix = curve_fit(func,xc,yc, sigma = yerc)
inv_variance = np.diagonal(linalg.inv(var_matrix))
SE = np.sqrt(inv_variance)
for i in range(len(SE)):
    SE[i] = 1./SE[i]


xp = xc  
yp = func(xp,coeff[0], coeff[1], coeff[2])

Chit = 0
for cix in range(0,lenp):
    Chit +=  ((Y[cix]-yp[cix])/Yerr[cix])**2
    Chi = Chit/(lenp-len(SE)-1.0)

print Chit, Chi


fig = plt.figure()
ax = fig.add_subplot(111)
yplt = Y-X
print "Y = ", Y
print "X = ", X

plt.errorbar(X, yplt, yerr=Yerr, ls='None', marker='o', alpha=0.5, label='I3')
plt.plot(xp, Y-yp, '--', label ='q,m,c fit')
#plt.plot(xplot,yplot,'k-')
ax.set_xlabel('$\gamma_t$ ')
ax.set_ylabel('$\gamma_m $')
plt.grid()
ax.grid(True, which='both')
leg = ax.legend( loc='upper left',ncol = 2, prop={'size':12}, numpoints = 1, )
ax.set_xlim(-0.01,0.16)

plt.show()
