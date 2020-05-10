#!/usr/bin/env python3

#a = int(input())
#b = int(input())
#c = int(input())
#d = int(input())

#result = (a**b) + (c**d)
#print(result)

a, b, c, d = (int(input()) for _ in range(4))
print(pow(a,b)+pow(c,d))
