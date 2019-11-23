#!/usr/bin/python3.6

import socket

socket.setdefaulttimeout(2)
s = socket.socket()
ip = '127.0.0.1'
port = '21'

try:
    s.connect((str(ip),int(port)))
except Exception as e:
    print('[-] Error = ' + str(e))

