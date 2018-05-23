#!usr/bin/env python
#importing modules
import thread
import base64
import socket 
import time 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#defining recieve function
def recieve():
	while 1:
		x=s.recvfrom(100)
		fmsg=base64.b64decode(x[0])	#decoding recieved msg
		print "Recieved msg  :",fmsg	#printing msg
		print "Enter msg:  "				

#defining send function		
def send():
	while 1:
		print "Enter msg:  "
		rep=raw_input()				#taking input
		s.sendto(base64.b64encode(rep),("127.0.0.1",8888))	#sending encoded msg

#starting threads
thread.start_new_thread(recieve,())
thread.start_new_thread(send,())
 
while 1:
	pass
