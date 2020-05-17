#!/usr/bin/python3.6

import socket # Look into the socket module: page 781 of py book.
import threading # Look into the threading module
import pickle # Simpler way to handle encode/decode. Pickle handles serializing and de-serializing object structs


PORT = 6969
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
#print(SERVER)
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "gbye"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
  print(f"[+] New Connection {addr} connected.")
  connected = True
  while connected:
    msg_length = conn.recv(HEADER).decode(FORMAT)
#    msg_length = conn.recv(HEADER)
#    message = pickle.loads(msg_length)
#    msg_length = pickle.loads(conn.recv(HEADER))
#    msg_length = conn.recv(pickle.loads(HEADER))
    if msg_length:
      msg_length = int(msg_length)
#      msg = conn.recv(msg_length).decode(FORMAT)
#      msg_length = int(message)
      msg = conn.recv(pickle.dumps(msg_length))
      if msg == DISCONNECT_MESSAGE:
        connected = False
      print(f"[+] {addr}: {msg}")
#      conn.send("got the message compadre".encode(FORMAT))
#      pickle.dumps(conn.send("got the message compadre"))
      conn.send(pickle.dumps("got message"))
      message2 = "got the message compadre"
      messagep = pickle.dumps(message2)
      conn.send(messagep)
  conn.close()
  print(f"[-] Connection dropped, Connection Count: {threading.activeCount() - 2}")
 
    

def start():
  server.listen()
  print(f"[+] Server is listening on {SERVER}:{PORT}")
  while True: 
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr)) 
    thread.start()
    print(f"[+] Active Connections:  {threading.activeCount() - 1}")

try: 
  print("[+] Server starting")
  start()
except KeyboardInterrupt:
  exit()
