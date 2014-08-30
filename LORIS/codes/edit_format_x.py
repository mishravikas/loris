# LORIS version 1.0
# Copyright (c) ABC Lab, BITS Pilani - K.K. Birla Goa Campus, India.
# All Rights Reserved.
# We advise the users to exercise the following code as it is.
# Any alteration(s) made to the below given code may result in
# the improper functioning of the software.
# LORIS recommends Python 2.7.4 and above.
# ============================ CODE BEGINS ==================================

import os, sys

inp=sys.argv[1]
outdir=sys.argv[2]

newF=open(outdir+inp, 'w')

allval=[]
f=open(inp, 'r')
for line in f:
    allval.append(line.rstrip().split())
f.close()

newF.write('%%MatrixMarket matrix array real general'+'\n')
newF.write(str(len(allval))+' '+str(len(allval[0]))+'\n')

c=0
while c < len(allval[0]):
    r=0
    while r < len(allval):
        newF.write(allval[r][c]+'\n')
        r=r+1
    c=c+1
newF.close()

# ============================= END OF CODE ==================================

# For any assistance please feel free to mail us at suku@goa.bits-pilani.ac.in

