#!usr/bi/env  python

import socket
recIP="192.168.10.60"
recPort=9990
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((recIP,recPort))
print s.recvfrom(100)

