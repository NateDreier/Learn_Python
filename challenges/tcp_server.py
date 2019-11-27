#!/usr/bin/python3.6
# thnks realpython.org/socket-something...
# now I need to figure out a way to write it on my own.....
import socket

HOST = ''
PORT = 2289

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))
	s.listen()
	conn, addr = s.accept()  # Need to understand this line better
	while conn:
		print('Connected by ' + str(addr))
		while True:
			data = conn.recv(1024)
			if not True:
				break
			conn.sendall(data.upper())

