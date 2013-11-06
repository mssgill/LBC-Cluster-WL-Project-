# mssg
# oct 2013

################### Code to read in a sexcat table, look at it, person
################### to make cuts on star column by hand, then rewrite
################### those stars out as a fits file

import pyfits
import matplotlib
import pylab as pl

## Read in sexcat with hardcoded name
sexcat = pyfits.open('decamtemp.sexcat')

## Data is in HDU2
dat = sexcat[2].data

## Set limits for plot
sizemin = 1
sizemax = 4
magmin = 8
magmax = 20

# Assign size and mag to vars
objsize = dat.field('FLUX_RADIUS')
objmag = dat.field('MAG_AUTO')


 ###### Plot mag vs. size of the objs 
pl.figure()
pl.plot(objsize,objmag, 'k.')
pl.plot()
pl.ylim(magmax,magmin)
pl.xlim(sizemin,sizemax)
pl.xlabel('$objsize$')
pl.ylabel('$mag$')
pl.title('Objects,')
pl.savefig('mag_vs_size.png')   

## Remove comment to show plot
# pl.show()

 #################### Cut on star column

# These were chosen by hand after examining the plot
sizemin = 1.4
sizemax = 1.5
magmin = 11
magmax = 17

# Make a boolean array for each edge of rectangle
starindex1 = objsize > sizemin
starindex2 = objsize < sizemax
starindex3 = objmag < magmax
starindex4 = objmag > magmin

# Combine all boolean arrays into one with 'and's
starindex = starindex1 & starindex2 & starindex3 & starindex4

# To see how many obey each condition
ntrue1 = (starindex1 == True).sum()
ntrue2 = (starindex2 == True).sum()
ntrue3 = (starindex3 == True).sum()
ntrue4 = (starindex4 == True).sum()

# Total num stars
ntrue = (starindex == True).sum()
nfalse = (starindex == False).sum()

# Show stats
ntrue1
ntrue2
ntrue
nfalse

#### Make data array of just stars using above total boolean array
stars = dat[starindex]

## Set limits for plot
sizemin = 1
sizemax = 4
magmin = 8
magmax = 20

# Reassign size and mag to vars
objsize = stars.field('FLUX_RADIUS')
objmag = stars.field('MAG_AUTO')


 ###### Plot the objs
pl.figure()
pl.plot(objsize,objmag, 'k.')
pl.plot()
pl.ylim(magmax,magmin)
pl.xlim(sizemin,sizemax)
pl.xlabel('$objsize$')
pl.ylabel('$mag$')
pl.title('Objects,')
pl.savefig('mag_vs_size.png')   

## Remove comments to show plot
# pl.show()

############# Write stars out to disk

# Make subtable of just stars
starhdu = pyfits.BinTableHDU(stars)

# Write out to a fits file
starhdu.writeto('stars.fits')


