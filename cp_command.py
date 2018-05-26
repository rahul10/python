#!usr/bin/python
import sys
import commands				#importing sys module
srcfile=sys.argv[1]
desfile=sys.argv[2]
commands.getoutput('>>$desfile')	#creating file if doesn't exists
f1=open(srcfile,'r')			#opening srcfile
f2=open(desfile,'w')			#opening desfile
srdata=f1.read()			#reading srcfile
f2.write(srdata)			#writing to desfile
f1.close()				
f2.close()				#closing files

	
