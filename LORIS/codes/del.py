# LORIS version 1.0
# Copyright (c) ABC Lab, BITS Pilani - K.K. Birla Goa Campus, India.
# All Rights Reserved.
# We advise the users to exercise the following code as it is.
# Any alteration(s) made to the below given code may result in
# the improper functioning of the software.
# LORIS recommends Python 2.7.4 and above.
# =========================== CODE BEGINS =====================================

import shutil
import os
import glob
n=os.getcwd()
os.chdir(n)
os.chdir('..')
n=os.getcwd()
i=0;x=0;y=0;
for i in range (4):
	i+=1
	a='/Output'+str(i)
	shutil.rmtree(n+a)	

# =========================== END OF CODE =====================================

# For any assistance please feel free to mail us at suku@goa.bits-pilani.ac.in

