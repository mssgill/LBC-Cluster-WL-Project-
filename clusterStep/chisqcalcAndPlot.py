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

################### SETUP FUNCTIONS
##############
def func(x,a,b,c):
    return a*x**2 +b*x + c #Refer [1]

def funclin(x,b,c):
    return b*x + c #Refer [1]

#############        READ IN FILES
################
files = ['fitDEIMOS.txt','fitFDNTnew.txt', 'fitimc.txt', 'fitESHELc.txt', 'fitim3shapef.txt', 'fitMJn.txt', 'fitPSFexg.txt'] 
j_file = files[0]
t_data = np.genfromtxt(j_file)
X = t_data[:,0]
Y = t_data[:,1]
Yerr = t_data[:,2]


#############       FILL ARRAYS
###################
lenp = len(X)
xc = np.linspace(0,lenp-1,lenp)   
yc = func(xc,0.1, 1, 2*10**-6) 
yerc = func(xc,0.1, 1,2*10**-6)
for lix in range(0,lenp):
    xc[lix] = X[lix]
    yc[lix] = Y[lix]
    yerc[lix] = Yerr[lix]

#######################################
######## CREATE BINS AND AVERAGE
# BIN1
bin1 = X == 0.0
bin2 = X == 0.03
bin3 = X == 0.06
bin4 = X == 0.09
bin5 = X == 0.15

data = np.zeros((4,5))
data[0,0] = np.average(X[bin1])
data[1,0] = np.average(Y[bin1])
data[2,0] = np.std(Y[bin1])
data[3,0] = np.average(Yerr[bin1])

data[0,1] = np.average(X[bin2])
data[1,1] = np.average(Y[bin2])
data[2,1] = np.std(Y[bin2])
data[3,1] = np.average(Yerr[bin2])

data[0,2] = np.average(X[bin3])
data[1,2] = np.average(Y[bin3])
data[2,2] = np.std(Y[bin3])
data[3,2] = np.average(Yerr[bin3])

data[0,3] = np.average(X[bin4])
data[1,3] = np.average(Y[bin4])
data[2,3] = np.std(Y[bin4])
data[3,3] = np.average(Yerr[bin4])

data[0,4] = np.average(X[bin5])
data[1,4] = np.average(Y[bin5])
data[2,4] = np.std(Y[bin5])
data[3,4] = np.average(Yerr[bin5])

lenp = len(data[0,:])
dxc = np.linspace(0,lenp-1,lenp)   
dyc = func(dxc,0.1, 1, 2*10**-6) 
dyerc = func(dxc,0.1, 1,2*10**-6)

for lix in range(0,lenp):
    dxc[lix] = data[0,lix]
    dyc[lix] = data[1,lix]
    dyerc[lix] = data[2,lix]


###################    PERFORM FITS
##############################
    
qmc_coeff, dvar_matrix = curve_fit(func,dxc,dyc, sigma = dyerc)
mc_coeff, dvar_matrix = curve_fit(funclin,dxc,dyc, sigma = dyerc)
aqmc_coeff, dvar_matrix = curve_fit(func,xc,yc, sigma = yerc)
amc_coeff, dvar_matrix = curve_fit(funclin,xc,yc, sigma = yerc)

dxp = dxc  
dyp = func(dxp,qmc_coeff[0], qmc_coeff[1], qmc_coeff[2])

print 'Fit qmc params', qmc_coeff
print 'Fit mc params', mc_coeff
print 'Fit params', aqmc_coeff
print 'Fit params', amc_coeff

############## MAKE PLOTS
############
fig = plt.figure()
ax = fig.add_subplot(111)
yplt = Y-X

plt.errorbar(X, Y-X, yerr=Yerr, ls='None', marker='o', alpha=0.05, label='all pts')
plt.plot(dxp, dyp-dxp, '+', linestyle='--', label ='q,m,c fit')
plt.errorbar(data[0,:], data[1,:]-data[0,:], yerr=data[2,:], ls='None', lw=5, marker='*', alpha=0.75, label='avrg')
ax.set_xlabel('$\gamma_m $-$\gamma_t$ ')
ax.set_ylabel('$\gamma_m $')
plt.grid()
ax.grid(True, which='both')
leg = ax.legend( loc='upper left',ncol = 2, prop={'size':12}, numpoints = 1, )
ax.set_xlim(-0.01,0.16)

plt.show()
