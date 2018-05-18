#!usr/bin/env python

import socket 
import time 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("127.0.0.1",8888))
while 1:
	x=s.recvfrom(100)
	print x[0]
	print "Enter reply:  "
	rep=raw_input()
	s.sendto(rep,x[1])
