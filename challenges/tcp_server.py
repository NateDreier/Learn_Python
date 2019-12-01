#!/usr/bin/python3.6
import socket

HOST = ''
PORT = 2289

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))
	s.listen()
	conn, addr = s.accept()  # Need to understand this line better
	while conn:
		full_msg =b''
		print('Connected by ' + str(addr))
		while True:
			data = conn.recv(8)
			full_msg += data
			if not True:
				break
			conn.sendall(full_msg.upper())

