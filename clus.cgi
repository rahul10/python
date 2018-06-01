#!/usr/bin/python
import cgi
import commands,time			#importing modules

print "Content-type:text/html"
print ""				#header
data=cgi.FieldStorage()
n=data.getvalue('c')			#getting value of c entered by user
c1=int(n)				#converting to int

for i in range(c1):
	print "<p>"
	print "Creating vm",i
	print "</p>"
	print commands.getoutput('sudo qemu-img create -f qcow2 -b /var/lib/libvirt/images/rhvmdnd.qcow2 /var/lib/libvirt/images/dnimg'+str(i)+'.qcow2')
	print "<p>"
	print "Starting vm",i
	print "</p>"
	print commands.getoutput('/var/www/cgi-bin/vminstall.py '+str(i))
	
	
	
