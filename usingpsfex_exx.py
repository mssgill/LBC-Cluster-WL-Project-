#Stolen from Barney Rowe.
#
# the psfex object that's the input to this function is loaded with:
# psfex = galsim.des.DES_PSFEx(psf_path)
#

import numpy
import os
import galsim
import galsim.des
import pylab
import pyfits

def getPSFExarray(psfex, x_image, y_image, nsidex=32, nsidey=32, upsampling=1, offset=None):
    """Return an image of the PSFEx model of the PSF as a NumPy array.

    Arguments
    ---------
    psfex       A galsim.des.PSFEx instance opened using, for example,
                `psfex = galsim.des.DES_PSFEx(psfex_file_name)`.
    x_image     Floating point x position on image [pixels]
    y_image     Floating point y position on image [pixels]

    nsidex      Size of PSF image along x [pixels]
    nsidey      Size of PSF image along y [pixels]
    upsampling  Upsampling (see Zuntz et al 2013)

    Returns a NumPy array with shape (nsidey, nsidex) - note the reversal of y and x to match the
    NumPy internal [y, x] style array ordering.  This is to ensure that `pyfits.writeto()` using the
    ouput array creates FITS-compliant output.
    """
    import galsim
    image = galsim.ImageD(nsidex, nsidey)
    psf = psfex.getPSF(galsim.PositionD(x_image, y_image), pixel_scale=1.)
    psf.draw(image, dx=1. / upsampling, offset=offset)
    return image.array

############################ Main code

os.system('rm star_from_psfex.fits')

# First gal -- obj #4
x = 1448
y = 15

psfex =  galsim.des.DES_PSFEx('decamtemp.psf')

psfatgal = getPSFExarray(psfex, x, y )

pyfits.writeto("star_from_psfex.fits",psfatgal)

# f = pyfits.open("staratxy.fits")

numpy.set_printoptions(threshold='nan')

psfatgal  # Display the contents of the fits table file

# pylab.imshow(psfatgal) ;  pylab.colorbar() ; pylab.show()  # Show the star


