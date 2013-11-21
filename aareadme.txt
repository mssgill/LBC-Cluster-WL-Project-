# Main Readme for the LBC Cluster WL project

# MSSG, JCY, and JM (Josh Meyers)
# start: oct 2013
# 

################## To get git repo set up, and then use it

edit and add a .gitignore file

# Connect repo to remote one on github:
git remote add origin https://github.com/mssgill/LBC-Cluster-WL-Project-.git

# Add some files
git add [several file names]

git commit                 # To actually commit to repo

# Put them into remote repo
git push -u origin master  # This requires username + passwd on git

--> Note that this will make an original git repo in the current dir, with whatever you named it on github

### To clone from github:

git clone https://github.com/mssgill/LBC-Cluster-WL-Project-.git

And after this, the cloned dir can be used to do updates back to the
original repo, for the owner and approved members in this dir, using
git add, commit, and push

To update, as normal, use git pull, and to check anytime the status of
the local files vs. what was last pulled, do a git status.


######################### Using a single star as psf in an im3shape run

[Nov 20 2013]

---- To get im3shape working in a mode where it's using a single star
     image as the psf (which is fine for this particular clusterstep
     image because it's constant psf and const shr across the whole),
     run as so from the clusterStepData dir:
     
python ../im3shape/bin/im3shape.py singlepsf.ini im_p4_s4_1.fits clusterStepData/im_p4_s4_1.gal.simple.cat clusterStepData/star1.fits singlepsf_output.py.txt 0 2480

Where:

--- singlepsf.ini is a modified ini param file where the position of
the star and its pixel extent has been changed, and the padding param
too (i think).

Also needed to alter line in file to use fits file for psf:

  psf_input = psf_image_single

--- im_p4_s4_1.fits is the orig fits file 

--- im_p4_s4_1.gal.simple.cat is a straight gal catalog with just the
  IDs,x,y of the galaxies in it and nothing else (this was
  simplified down from an ascii gal cat that Julia passed on to me),
  Used: 
    awk '{print $1 , $6 , $7;}' im_p4_s4_1.gal.cat > im_p4_s4_1.gal.simple.cat
  it's currently in the clusterStepData dir

--- star1.fits is a fits table file of the first star from the star
  cat, which was written out using choose_star.py (just: py
  choose_stars.py)

  it's currently in the clusterStepData dir also.


- singlepsf_output.py.txt is the file we want to write to

- The numbers 0 2480 are the objects we want to run over (to do a
  test, just change to e.g. 1 5 )
 

################## Getting psfex working to make .psf file for im3shape input

--- Start by getting needed files locally:

 cp ~/imcat/sextfilesForDES/* .

 cp decam.sex psfex.sex

--- Run the starpos.py code to put out the x,y of all stars

--- Alter psfex.sex file thusly:

CATALOG_TYPE    FITS_LDAC	

ASSOC_NAME         starpos.txt
ASSOC_RADIUS       2.0
ASSOC_PARAMS       2,3
ASSOC_TYPE         NEAREST
ASSOCSELEC_TYPE    MATCHED


--- Add to psfex.params:

NUMBER_ASSOC  at the very end (so it doesn't output all columns, only needed ones)

--- Then run:

sex -c psfex.sex im_p4_s4_1.fits  

  This will make: decamtemp.sexcat   


############################## Current:

-- MSSG: to try to output the 4 params im3shape needs: fwhm, beta, x, y at the pos's of the galaxies, now that psfex  is working and making an interpl'd psf over the whole field from stars

- Put files of first successful im3shape run in the repo

- email to JoeZ about what's going on with the x and y posns

- try to get Erin Sheldon psfex code from github running

-- JCY: to check pos of stars from the im3shape output file, figure
   out if they are RA/DEC even though they say 20.xxxx, 20.xxxx

- work with Daniel on photoz's of the Max8 cluster



Next GH: Mon Nov 11, 12.30pm PST
