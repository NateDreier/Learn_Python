#!/usr/bin/env python3

import socket
import threading
import pickle

PORT = 6969
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
#print(SERVER)
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "gbye"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
  message = msg.encode(FORMAT)
  msg_length = len(message)
#  send_length = str(msg_length).encode(FORMAT)
  send_length = pickle.dumps(msg_length)
  send_length += b' ' * (HEADER - len(send_length))
  client.send(send_length)
  client.send(message)

  server_msg = pickle.loads(client.recv(2048))
  print(server_msg)

try: 
  while True:
    send(input())
except KeyboardInterrupt:
  send(DISCONNECT_MESSAGE)
  exit() 

