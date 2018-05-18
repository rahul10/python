#!usr/bin/env python
import socket
import time

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while 1:
	msg=raw_input("Enter msg:   ")
	s.sendto(msg,("127.0.0.1",8888))
	rep= s.recvfrom(100)
	print "Reply:   ",rep[0] 
