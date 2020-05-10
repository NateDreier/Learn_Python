#!/usr/bin/env python3

import sys

num = int(input("Enter a numebr: "))

#if num % 2 != 0:
#  print("Weird")
#elif (num % 2 == 0) and (6 <= num <= 20):
#  print("Weird")
#else:
#  print("Not Weird")


check = {True: "Not Weird", False: "Weird"}
print(check[
  num % 2 == 0 and (
    num in range(2,6) or
    num > 10)
  ])
