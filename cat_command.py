#!usr/bin/python
import sys				#import sys module
file=sys.argv[1]			#inline argument
f=open(file)				#opening file
print f.read()				#printing file
f.close()				#closing file
