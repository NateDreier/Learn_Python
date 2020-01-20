#!/usr/bin/python3.6

import crypt
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
            exit(0)

def hack_a_pass(passpass):

def main():
    file = check_file()
    f = open(filename, r)
        
