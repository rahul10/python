#!/usr/bin/env python

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.sendto("Hello",("192.168.10.177",9999))




