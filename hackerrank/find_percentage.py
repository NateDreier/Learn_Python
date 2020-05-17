#!/usr/bin/env python3

#lst[0], lst[1] = (input() for _ in range(int(n)))
#x = [arr.append(i) for i in input().split()]
scores = {}
for _ in range(int(input())):
  line = input().split()
  scores[line[0]] = list(map(float, line[1:]))
print(f'{(sum(scores[input()])/3):.2f}')
