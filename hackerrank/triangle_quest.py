#!/usr/bin/env python3

n = int(input())
#10**1 = 10, 10//9 = 1, 1*1 = 1
#10**2 = 100, 100//9 = 11, 11*2 = 22
#10**3 = 1000, 1000//9 = 111, 111*3 = 333
#10**4 = 10000, 10000//9 = 1111, 1111*4 = 4444
#...
for i in range(n):
  print((10**(i)//9)*i)
