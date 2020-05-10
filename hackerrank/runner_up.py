#!/usr/bin/env python3

#if __name__ == '__main__':
#  n = int(input())
#  arr = map(int, input().split())
#
#sorted_list = sorted(arr)
#uniq_list = []
#
#for i in sorted_list:
#  if i not in uniq_list:
#    uniq_list.append(i)
#
#print(uniq_list[-2])

"""
Below is the improved version (thanks to someone)
Above I take the time to sort, then create a second 
list that only holds unique values, and finally prints the second from the end.

In the improved version, it creates a list of integers (not characters like above)
notes what the max number is, removes the max number while the max number exists
prints the new max number.
"""
if __name__ == '__main__':
  n = int(input())
  lis = list(map(int,input().strip().split()))[:n]

z = max(lis)
while max(lis) == z:
  lis.remove(max(lis))
print(max(lis))
