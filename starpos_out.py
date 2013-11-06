# Nov 2013
# MSSG

# Code to write out *just* the x and y pos of stars into an ascii
# file, to then be used in assoc mode for SE

import pyfits

st = pyfits.open('stars.fits')  # Open fits table file on disk

d = st[1].data  # Get the data 

f = open('starpos','w')  # Open ascii file to write out to

for i in range( 543 ):  # Hard coded the length because i knew it for this file
           f.write( str(d[i]['NUMBER'])+'  ')
           f.write( str(d[i]['X_IMAGE'])+'  ')
           f.write( str(d[i]['Y_IMAGE'])+'   \n')

f.close() # Have to close the file at the end

