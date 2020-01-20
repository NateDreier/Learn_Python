#!/usr/bin/python3.6

listy = [1, 2, 3, 11, 5]

with listy(listy) as l:
    l[3] = l[3] * 2
    print(l[len()])