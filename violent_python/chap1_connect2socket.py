#!/usr/bin/python3.6

import socket

def retBanner(ip, port):
     try:
         socket.setdefaulttimeout(2)
         s = socket.socket()
         s.connect((ip, port))
         banner = s.recv(1024)         
         return banner
     except Exception as e:
         print('[-] Error' + str(e))

def main():
    ip1 = '127.0.0.1'
    ip2 = '192.168.101.129'
    port = 22
    
    banner1 = retBanner(ip1, port)
    banner2 = retBanner(ip1, port)

    if banner1:
       print('[+] ' + str(ip1) + ': ' + str(banner1))
    if banner2: 
       print('[+] ' + str(ip2) + ': ' + str(banner2))

if __name__ == '__main__':
  main()
