#!/usr/bin/env python3

# The list comprehension way:
# x, y, z, n = int(input()), int(input()), int(input()), int(input())
x, y, z, n = (int(input()) for _ in range(4))
print ([[a, b, c] for a in range(x + 1) for b in range(y + 1) for c in range(z + 1) if a+b+c != n ])



#x = int(input())
#y = int(input())
#z = int(input())
#n = int(input())
#def func(x, y, z, n):
#  p = 0
#  ar = []
#  for i in range(x+1):
#    for j in range(y+1):
#      for k in range(z+1):
#        if i+j+k != n:
#          ar.append([])
#          ar[p] = [i, j, k]
#          p += 1
#  return(ar)
#
#print(func(x, y, z, n))

