#!/usr/bin/env python3

n = int(input())
mod = []

for _ in range(n):
  line = input().split()
  act, index, element = line[0], line[1], line[2]
  action = eval(act)
  mod.action(index, element)
