#!/usr/bin/python3.6

import socket

HOST = '127.0.0.1'
PORT = 2289

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	s.sendall(b'Hello friends')
	data = s.recv(8)  # What are pros and cons of bigger or smaller

print('Received ' + str(data))
