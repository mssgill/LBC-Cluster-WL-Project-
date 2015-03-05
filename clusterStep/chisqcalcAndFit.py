# Mar 2015

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
def parab(x,a,b,c):
    return a*x**2 +b*x + c #Refer [1]

def linefunc(x,b,c):
    return b*x + c #Refer [1]

#############        READ IN FILES
files = ['fitDEIMOS.txt','fitFDNTnew.txt', 'fitimc.txt', 'fitESHELc.txt', 'fitim3shapef.txt', 'fitMJn.txt', 'fitPSFexg.txt'] 
whichfile = files[6]               # Pick which file to run from list above
t_data = np.genfromtxt(whichfile)  # Read in the data
X = t_data[:,0]                 # Column 1 are the x values
Y = t_data[:,1]                 # Column 2 are the y values
Yerr = t_data[:,2]              # Column 3 are the y error vals 


#############       FILL ARRAYS
lenp = len(X)
# print " lenp = " , lenp           # 96 for these data files

### Make dummy vecs
xc = np.linspace(0,lenp-1,lenp)   # Make vec from 0 to lenp-1, with lenp steps (so it will be an exact integer array in the 0 -> lenp-1 range) 
yc = parab(xc, 0.1, 1, 2*10**-6)   # Eval the parabola function with the xc vec values and the qmc values as given 
yerc = parab(xc,0.1, 1,2*10**-6)   # Doing this just to fill arrays with dummy vals to be overwritten later

for lix in range(0,lenp):          # Replace the values in the vecs by the ones read in
    xc[lix] = X[lix]
    yc[lix] = Y[lix]
    yerc[lix] = Yerr[lix]

    
############## CREATE BINS AND AVERAGE
# BIN1 
bin1 = X == 0.0    # Boolean arrays, which puts True in all the places of the array that obeys the test condition
bin2 = X == 0.03
bin3 = X == 0.06
bin4 = X == 0.09
bin5 = X == 0.15

data = np.zeros((4,5))           # Create a 4x5 array of zeroes (4 rows, 5 cols)
data[0,0] = np.average(X[bin1])  # Assign avg of X values that are 0 into 0,0 elt of data array
data[1,0] = np.average(Y[bin1])  # Assign avg of Y values where X = 0 into 1,0 elt of data array
data[2,0] = np.std(Y[bin1])      # Assign std of Y values where X = 0 into 2,0 elt of data array
data[3,0] = np.average(Yerr[bin1])  # Assign avg of Y err values where X = 0 into 3,0 elt of data array

data[0,1] = np.average(X[bin2])  # Similar to above, for other X vals
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

inputshrs = np.linspace(0,lenp-1,lenp)          ### Make dummy vecs -- all these 3 are just length 5 now
outputshrs = parab(inputshrs,0.1, 1, 2*10**-6) 
shrerr = parab(inputshrs,0.1, 1,2*10**-6)

for lix in range(0,lenp):
    inputshrs[lix] = data[0,lix]    # Fill avgs of X for dif x vals into this vector
    outputshrs[lix] = data[1,lix]   # Fill avgs of Y for dif x vals into this vector
    shrerr[lix] = data[2,lix]        # Fill avgs of std of Y for dif x vals into this vector



###################    PERFORM FITS
    
qmc_coeff, dvar_matrix = curve_fit(parab,inputshrs,outputshrs, sigma = shrerr)   # parabolic fit
mc_coeff, dvar_matrix = curve_fit(linefunc,inputshrs,outputshrs, sigma = shrerr) # lin fit

aqmc_coeff, dvar_matrix = curve_fit(parab,xc,yc, sigma = yerc)
amc_coeff, dvar_matrix = curve_fit(linefunc,xc,yc, sigma = yerc)

print 'Fit qmc params', qmc_coeff
print 'Fit mc params', mc_coeff
# print 'Fit params', aqmc_coeff
# print 'Fit params', amc_coeff

################### CREATE FUNCT FROM FITS

# Values of the parabolic curve with params extracted from fit evaluated at the inputshrs vals
parabfitvals = parab(inputshrs,qmc_coeff[0], qmc_coeff[1], qmc_coeff[2])

# Values of the line with params extracted from fit evaluated at the inputshrs vals
linefitvals = linefunc(inputshrs,mc_coeff[0], mc_coeff[1])    # Line with params extracted from fit

#print y_1 ; print y_2
######################## Calc CHI SQ for the 2 fits

### For line
lineChisqtot = 0  # Init total chisq val
# Loop over the 5 inputshr vals, summing up the chisq
for cix in range(0,len(inputshrs)):
    lineChisqtot +=  ((outputshrs[cix]- linefitvals[cix])/shrerr[cix])**2
    
# Reduced chisq -- 5 data vals, 3 fit params    
lineredChisq = lineChisqtot/(len(inputshrs)-3-1.0)
print ' line redChisq = ', lineredChisq

### For parab
parabChisqtot = 0  # Init total chisq val
# Loop over the 5 inputshr vals, summing up the chisq
for cix in range(0,len(inputshrs)):
    parabChisqtot +=  ((outputshrs[cix]- parabfitvals[cix])/shrerr[cix])**2
    
# Reduced chisq -- 5 data vals, 3 fit params    
parabredChisq = parabChisqtot/(len(inputshrs)-3-1.0)
print ' parab redChisq = ', parabredChisq

print lineredChisq, parabredChisq


############## MAKE PLOTS
############
fig = plt.figure()
ax = fig.add_subplot(111)
yplt = Y-X

plt.errorbar(X, Y-X, yerr=Yerr, ls='None', marker='o', alpha=0.05, label='all pts')  # Add this back if you want to see all points
plt.plot(inputshrs, linefitvals-inputshrs, '+', linestyle='-', label ='m,c fit')     # Plot line fit
plt.plot(inputshrs, parabfitvals-inputshrs, '+', linestyle='--', label ='q,m,c fit') # Plot parab fit
plt.errorbar(data[0,:], data[1,:]-data[0,:], yerr=data[2,:], ls='None', lw=5, marker='*', alpha=0.75, label='avrg')
ax.set_xlabel('$\gamma_m $-$\gamma_t$ ')
ax.set_ylabel('$\gamma_m $')
plt.grid()
ax.grid(True, which='both')
leg = ax.legend( loc='upper left',ncol = 2, prop={'size':12}, numpoints = 1, )
ax.set_xlim(-0.01,0.16)

plt.show()
