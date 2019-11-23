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
         print('[-] Error ' + str(e))

def main():
    portList = [21,22,25,53,80,443,3389] 
    for x in range(1, 255):
      ip = '192.168.101.' + str(x)
      for port in portList:
          banner = retBanner(ip, port)
          if banner:
              print('[+] ' + ip + ': ' + banner)

# the below link explains pretty well why you need and would want the below code
# https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/
if __name__ == '__main__':
  main()

####
# Things to improve:
# if running a scan against a range, add a block of code to see which IP addresses are
# able to be hit and which aren't. I don't actually know if that is a good idea or not
