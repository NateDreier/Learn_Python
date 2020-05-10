#!/usr/bin/env python3

#lis = []
#for _ in range(0, int(input())):
#  lis.append([input(), float(input())])

# [['nate', 58.6], ['emily', 100.0], ['joe', 88.0], ['bill', 90.0], ['sally', 45.0]]
def sort(lis):
  l = len(lis)
  for i in range(0, l):
    for j in range(0, l-i-1):
      if (lis[j][1] > lis[j + 1][1]):
        tempo = lis[j]
        lis[j] = lis[j + 1]
        lis[j  + 1] = tempo
  return lis

lis = [['nate', 45.0], ['emily', 100.0], ['joe', 88.0], ['bill', 90.0], ['sally', 45.0]]
lis=sort(lis)

z = min(lis[0][1])
for i in len(lis):
  while min(lis[i][1]) == z:
    lis.remove(min(lis))
#  print(min(lis))

if lis[0][1] == lis[1][1]:
  alp = []
  alp.append(lis[0][0]
  alp.append(lis[1][0]
  print(alp)
else:
  print(lis[0][0])

#lis = [['nate', 45.0], ['emily', 100.0], ['joe', 88.0], ['bill', 90.0], ['sally', 45.0]]
#print(sort(lis)) 
