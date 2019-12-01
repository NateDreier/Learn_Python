#!/usr/bin/python3.6
import random

number = random.randint(1, 10)
def is_numba_numba():
    while True:
        try:
            guess = int(input('numba plz \n'))
        except ValueError:
            print('not a int, ya dope')
            continue
        else:
            return guess

def compare_numbas(n):
    while True:
        g = is_numba_numba()
        if g < n:
            print('guess is too low!')
        elif g > n:
            print('guess is too high!')
        else:
            print("wow nice guess, that's it")
            break

print('I am thinking of a number between 1 and 10')
compare_numbas(number)