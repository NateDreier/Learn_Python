#!/usr/bin/env python3.8


how_many_prime = int(input("How many prime numbers would you like to see? "))

def nat(n):
    yield n
    yield from nat(n+1)

def sieve(s):
    n = next(s)
    yield n
    yield from sieve(i for i in s if i%n!=0)

p = sieve(nat(2))
for _ in range(how_many_prime):
    print(next(p))
