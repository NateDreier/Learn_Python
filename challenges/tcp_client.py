#!/usr/bin/python3.6

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('python.org', 80))    #this will need to be to the server.`

#for this project they will both need to be 'servers', sending and receiving.
