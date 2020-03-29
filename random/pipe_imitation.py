#!/usr/bin/env python3

import os
import sys

#for line in sys.stdin:
#    try:
#        print(line, end='')
#    except:
#        #pass
#        devnull = os.open(os.devnull, os.O_WRONLY)
#        dup2 = (devnull, sys.stdout.fileno())

for line in sys.stdin:
    try:
        print(line, end='')
    except BrokenPipeError:
        sys.stderr.close()
