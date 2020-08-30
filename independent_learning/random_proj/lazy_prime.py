#!/usr/bin/env python3.8


how_many_prime = int(input("How many prime numbers would you like to see? "))

def natural_num(num: int)-> int:
    yield num
    yield from natural_num(num+1)

def sieve(s: int)-> int:
    n = next(s)
    yield n
    yield from sieve(i for i in s if i%n!=0)

p = sieve(natural_num(2))
for _ in range(how_many_prime):
    print(next(p))
