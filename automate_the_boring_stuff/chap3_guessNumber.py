#!/usr/bin/python3.6
import random

def number_guess():
    number = random.randint(1, 10)
    guess = 0
    while isinstance(guess, int):
        print('I\'m thinking of a number between 1 and 10, what is it?')
        guess = int(input())
        if guess < number:
            print('guess is too low!')
        elif guess > number:
            print('guess is too high!')
        else:
            print("wow nice guess, that's it")
            break
    else:
        print('please input an integer')

number_guess()

         