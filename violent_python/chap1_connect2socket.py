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

def checkVulns(banner):
	f = open('vuln_banners.txt','r')
	for line in f.readlines():
		if line.strip('\n') in banner:
			print('[+] Server is vulnerable: ' + banner.strip('\n'))


def main():
	portList = [80]
	for x in range(196, 198):
		ip = '100.26.199.' + str(x)
		for port in portList:
			banner = str(retBanner(ip, port))
			if banner:
				print('[+] ' + str(ip) + ': ' + str(banner))
				checkVulns(banner)

# the below link explains pretty well why you need and would want the below code
# https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/
if __name__ == '__main__':
  main()
