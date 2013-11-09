
# Main Readme for the LBC Cluster WL project

# MSSG, JCY, and JM (Josh Meyers)
# start: oct 2013
# 

################## To get git repo set up, and then use it

edit and add a .gitignore file
git remote add origin https://github.com/mssgill/LBC-Cluster-WL-Project-.git
git add [several file names]
git commit                 # To actually commit to repo
git push -u origin master  # This requires username + passwd on git

--> Note that this will make an original git repo in the current dir, whatever you named it on github

### To clone from github:

git clone https://github.com/mssgill/LBC-Cluster-WL-Project-.git

And after this, the cloned dir can be used to do updates back to the
original repo, for the owner and approved members in this dir, using
git add, commit, and push

To update, as normal, use git pull, and to check anytime the status of
the local files vs. what was last pulled, do a git status.


######################### Isolating stars

############ Run star choosing py code to make fits file

py choose_stars.py 

#### Pick ID,x,y columns of galcat

awk '{print $1 , $6 , $7;}' im_p4_s4_1.gal.cat > im_p4_s4_1.gal.simple.cat

#### Line to change in ini file to use fits file for psf

psf_input = psf_image_single

#### Syntax to run cmd
 
python ../../im3shape/bin/im3shape.py single_psf.ini im_p4_s4_1.fits im_p4_s4_1.gal.simple.cat star1.fits single_starpsf_output.py.txt 1 5


################## Getting psfex working

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


made: decamtemp.sexcat  --> 


############################## Current:

-- MSSG: to try to output the 4 params im3shape needs: fwhm, beta, x, y at the pos's of the galaxies, now that psfex  is working and making an interpl'd psf over the whole field from stars

- Put files of first successful im3shape run in the repo

- email to JoeZ about what's going on with the x and y posns

- try to get Erin Sheldon psfex code from github running

-- JCY: to check pos of stars from the im3shape output file, figure
   out if they are RA/DEC even though they say 20.xxxx, 20.xxxx

- work with Daniel on photoz's of the Max8 cluster



Next GH: Mon Nov 11, 12.30pm PST
