# LORIS version 1.0
# Copyright (c) ABC Lab, BITS Pilani - K.K. Birla Goa Campus, India.
# All Rights Reserved.
# We advise the users to exercise the following code as it is.
# Any alteration(s) made to the below given code may result in
# the improper functioning of the software.
# LORIS recommends Python 2.7.4 and above.
# =============================================== CODE BEGINS ==================================================
import os
import time
import random
import datetime
import sys
today=datetime.datetime.today()
hydro=dict((('A',1.8),('L',3.8),('R',-4.5),('K',-3.9),('N',-3.5),('M',1.9),('D',-3.5),('F',2.8),('C',2.5),('P',-1.6),('Q',-3.5),('S',-0.8),('E',-3.5),('T',-0.7),('G',-0.4),('W',-0.9),('H',-3.2),('Y',-1.3),('I',4.5),('V',4.2)))
os.system('clear')
n=os.getcwd()
os.chdir('..')
m=os.getcwd()
os.chdir(m+"/input_pssm")
a=[];icount=[];b=[];pcount=[];h=[];hy=[];fn=[];s=[];name=[]
z=datetime.datetime.now().strftime("%a, %d-%b-%Y, %H:%M:%S")
# ==============================================================================================================
for i in range(1000):
	b.append('');
	name.append('');
	s.append('')
	h.append(0);
	icount.append(1);
	hy.append(0);
i=0;k=0;
print '\033[1m' + 'Running LORIS v1.0 ...\n'+z+'\n'
for files in os.listdir("."):
	i+=1
os.chdir(m+"/input_prsa")
for files in os.listdir("."):
	k+=1
if(i!=k):
	print("Error: Number of files not equal in both the folders!\nPlease ensure that the number of files in the folders input_prsa and input_pssm are equal.\n")
	print 'LORIS version 1.0'
	print 'Designed & Developed by ABC Lab at BITS Pilani-K.K. Birla Goa Campus, India\nFor any assistance please feel free to mail us at suku@goa.bits-pilani.ac.in\n'
	print ' ________________________________________________'
	print '|						 |'
	print '| ABC: "Annotate Biomolecules Computationally"   |'
	print '|________________________________________________|\n'
	sys.exit()
i=0;k=0;
os.chdir(n)
os.system('chmod 755 *')
os.system('python new.py')
os.chdir(m+"/input_prsa")
# ==============================================================================================================
for files in os.listdir("."):
	infile=files
	x=infile.split('.')[0]
	infile=x+'.prsa'
	name[k]=infile
	with open(infile, 'r') as file:
		for line in file:
			i+=1
			if i>=3:
				icount[k]+=1
	icount[k]-=1
	k+=1
	i=0
os.chdir(m+"/input_pssm")
k=0;i=0;
# ==============================================================================================================
for files in os.listdir("."):
	infile=name[k]
	x=infile.split('.')[0]
	infile=x+'.pssm'
	i=0
	with open(infile, 'r') as file:
		count=0
		for line in file:
			count+=1
			if count>=4 and count<=(icount[k]+4):
				b[k]+=line
				i+=1
	k+=1;
i=0;l=0;k=0;v=' ';p=0;t=m;
# ==============================================================================================================
for files in os.listdir("."):
	infile=name[k]
	x=infile.split('.')[0]
	path=t+'/input_prsa/'
	infile=x+'.pssm'
	with open(infile, 'r') as psfile:
		count=0
		for line in psfile:
			count+=1
			if (count>=8) and (count<=icount[k]-1):
				m=count-4	
				g=0
				l=0
				d=0
				x=''
				y=' '
				for x in b[i].split('\n'):
					if(x!=''):
						l+=1;
						if(l>=m-3) and (l<=m+5):
							hy[d]=hydro[x[6]]
							x=x[10:69] + ' '
							y+=x
							d+=1		
				y+=str(hy[4]) + ' '
				r=(hy[3]+hy[4]+hy[5])/3
				r=round(r,1)
				y+=str(r) +' '
				r=(hy[2]+hy[3]+hy[4]+hy[5]+hy[6])/5
				r=round(r,1)
				y+=str(r) +' '
				r=(hy[1]+hy[2]+hy[3]+hy[4]+hy[5]+hy[6]+hy[7])/7
				r=round(r,1)
				y+=str(r) +' '
				r=(hy[0]+hy[1]+hy[2]+hy[3]+hy[4]+hy[5]+hy[6]+hy[7]+hy[8])/9
				r=round(r,1)
				y+=str(r) +' '
				c=0
				infile=infile.split('.')[0]+'.prsa'
				with open(path+infile,'r') as prfile:
					for line1 in prfile:
						c+=1
						if(c==count-1):
							y=y+line1[11:17]+'\n'
							s[i]+=line1[5]+'       '+line1[7]+'\n'	
				of=t+'/Output1/'
				ofilename=(of + infile.split('.')[0] + '.txt')
				with open(ofilename,"a+") as ofile:
					ofile.write(y)
		k+=1
		i+=1
k=0;m=t;
import os
os.chdir(n)
os.system('python expo.py')
# ==============================================================================================================
os.chdir(m+"/Output2")
for files in os.listdir("."):
    infile=name[k]
    x=infile.split('.')[0]
    infile=x+'.txt'
    k+=1
    prog_name=m+"/codes/edit_format_x.py"

    os.system('python %s %s %s' % (prog_name, infile, m+"/Output3/"))
# ==============================================================================================================
k=0;
os.chdir(m+"/Output3")
for files in os.listdir("."):
    infile=name[k]
    x=infile.split('.')[0]
    testX=x+'.txt'
    prog_name=m+"/codes/l1_logreg_classify"
    k+=1
    os.system('%s %s %s %s' % (prog_name, m+"/codes/model", testX, m+"/Output4/"+testX))
# ==============================================================================================================
os.chdir(m+"/Output4")
of=m+'/Output/'
r=0;k=0;e=0;
for files in os.listdir("."):
    infile=name[e]
    e+=1
    x=infile.split('.')[0]
    infile=x+'.txt'
    k=0
    j=0
    with open(infile, 'r') as file:
        for line in file:
		if(line[0]!='%'):
			j+=1
			if(j>1):
				h[k]=int(line)
				if(h[k]==1):
					h[k]='+'
				elif(h[k]==-1):
					h[k]='-'
				k+=1    
    j=0        
    infile=infile.split('.')[0]
    y='# =============================== LORIS v1.0 ==============================\n# PPIs Prediction by LORIS\n# Copyrights (c) 2013 ABC Lab @ BITS, Pilani - K.K. Birla Goa Campus, India\n# All Rights Reserved.\n'
    t=y
    y+='# '+z+'\n# File name: '+infile+'.vloris'+'\n# PRED  Pos\tClass\tName\tE/I/B\n'
    for item in s[r].split('\n'):
	if(item!=''):
	   	y+='  PRED'+'  '+str(j+5)+'\t'+str(h[j])+'\t'+str(item)+'\n'
		j+=1
    c=1
    k=0
    x=0
    t+='# '+z+'\n# File name: '+infile+'.hloris'+'\n#\n#\n'+str(c+4)+':\t'
    for item in s[r].split('\n'):
	if(c<=50):
		t+=item.split(' ')[0]
		if(c%10==0):
			t+=' '
		c+=1
	if(c==51):	
		t+='\nPRED'+'\t'
		for p in range(50):
			if((p+k)==j):
				break
			t+=str(h[p+k])
			if((p+1)%10==0):
				t+=' '
		k+=50
		t+='\n'+str(k+5)+':\t'
		c=1
	elif((k+c)==(j+1)):
		t+='\nPRED'+'\t'
		for p in range(50):
			if((p+k)==j):
				break
			t+=str(h[p+k])
			if((p+1)%10==0):
				t+=' '
		break
    y+='#\n#  Column 1: Record Name\n#  Column 2: Residue Number\n#  Column 3: + = Interface & - = Non-Interface\n#  Column 4: Residue Name(1 letter code)\n#  Column 5: E = Exposed Residue, I = Intermediate Residue and B = Buried Residue\n#'
    y+='\n#  END OF FILE\n#'
    t+='\n#\n#\n#  END OF FILE\n#'
    with open(of+infile+'.vloris','w') as ofile:
	ofile.write(y)
    with open(of+infile+'.hloris','w') as ofile:
	ofile.write(t)
    r+=1
# ==============================================================================================================
os.system('clear')
print '\nProgram execution over.\n'+'Please check the "Output" folder.\nPath to the Output folder: '+m+'/Output/\nThank you for using LORIS.\n\n'
print 'LORIS version 1.0'
print 'Designed & Developed by ABC Lab at BITS Pilani-K.K. Birla Goa Campus, India\nFor any assistance please feel free to mail us at suku@goa.bits-pilani.ac.in\n'
print ' ________________________________________________'
print '|						 |'
print '| ABC: "Annotate Biomolecules Computationally"   |'
print '|________________________________________________|\n'
os.chdir(n)
os.system('python del.py')
#
# ============================================ END OF CODE =====================================================
#
# For any assistance please feel free to mail us at suku@goa.bits-pilani.ac.in
#
