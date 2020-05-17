#!/usr/bin/env python3

x = int(input())
y = int(input())
z = int(input())
n = int(input())
def func(x, y, z, n):
  p = 0
  ar = []
  for i in range(x+1):
    for j in range(y+1):
      for k in range(z+1):
        if i+j+k != n:
          ar.append([])
          ar[p] = [i, j, k]
          p += 1
  return(ar)

print(func(x, y, z, n))

