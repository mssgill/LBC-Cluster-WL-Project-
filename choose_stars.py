# Very simple py code to cut out stars
# From JCY, Oct 2013
# Altered by MSSG

import pyfits
import numpy as np

f = pyfits.open('im_p4_s4_1.fits') # open a FITS file
scidata = f[0].data # assume the first extension is an image
print scidata[1,4] # get the pixel value at x=5, y=2

# Pick a star with center = 54, 171, +/- 7 pixels in x and y dirs
st1 = scidata[47:61, 164:178]

print st1 # To see values

pyfits.writeto("star1.fits", st1) # Write out to cutout fits file


