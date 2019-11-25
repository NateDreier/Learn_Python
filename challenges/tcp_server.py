#!/usr/bin/python3.6

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 100.26.199.197, temp ec2
serversocket.bind(('localhost', 2289))
serversocket.listen(5)

(clientsocket, address) = serversocket.accept()

#add recv
#need 2 loops
#one loop to recv the MSGLEN and the second to get the actual data.
#send all that was being recv.upper
