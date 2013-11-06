# MSSG
# oct 2013

#### Run star choosing py code to make fits file

py choose_stars.py 

#### Pick ID,x,y columns of galcat

awk '{print $1 , $6 , $7;}' im_p4_s4_1.gal.cat > im_p4_s4_1.gal.simple.cat

#### Line to change in ini file to use fits file for psf

psf_input = psf_image_single

#### Syntax to run cmd
 
python ../../im3shape/bin/im3shape.py single_psf.ini im_p4_s4_1.fits im_p4_s4_1.gal.simple.cat star1.fits single_starpsf_output.py.txt 1 5


################################ Getting psfex working

--- Start by getting needed files locally:

cp ~/imcat/sextfilesForDES/* .

cp decam.sex psfex.sex

--- Ran the starpos.py code 

--- Altered psfex.sex file thusly:

CATALOG_TYPE    FITS_LDAC	

ASSOC_NAME         starpos.txt
ASSOC_RADIUS       2.0
ASSOC_PARAMS       2,3
ASSOC_TYPE         NEAREST
ASSOCSELEC_TYPE    MATCHED


--- Added to psfex.params

NUMBER_ASSOC  at the very end

--- Then ran:

sex -c psfex.sex im_p4_s4_1.fits  


made: decamtemp.sexcat

