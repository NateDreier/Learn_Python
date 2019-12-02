#!/usr/bin/python3.6

import socket
import sys
import os

def check_file():
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		if not os.path.isfile(filename):
			print('[-] ' + filename + ' does not exist.')
			exit(0)
		if not os.access(filename, os.R_OK):
			print('[-] ' + filename + ' access denied.')
		print('[+] Reading vulnerabilities from ' + filename)	

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
	check_file()
	portList = [22]
	for x in range(128, 130):
		ip = '192.168.101.' + str(x)
		for port in portList:
			banner = str(retBanner(ip, port))
			if banner:
				print('[+] ' + str(ip) + ': ' + str(banner))
				checkVulns(banner)

if __name__ == '__main__':
  main()
