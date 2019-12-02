#!/usr/bin/python3.6
import random

# def range():
#     print('what range do you want to guess?')
#     low_end = int(input('enter the low end of the range: '))
#     high_end = int(input('enter the high end of the range: '))
#     while True:
#         try:
#             high_end > low_end
#         except:
#             print('your high end needs to be a greater number than your low end number')
#             continue
#         else:
#             return low_end, high_end
            
def check_number():
    while True:
        try:
            guess = int(input('numba plz \n'))
        except ValueError:
            print('not a int, ya dope')
            continue
        if guess > 10 or guess < 1:
            print('the number must be in the correct range')
        else:
            return guess

def compare_numbas(n):
    while True:
        g = check_number()
        if g < n:
            print('guess is too low!')
        elif g > n:
            print('guess is too high!')
        else:
            print("wow nice guess, that's it")
            break

# low, high = range()
# number = random.randint(low, high)
number = random.randint(1, 10)


# print('I am thinking of a number between ' + str(low) + ' and ' + str(high))
print('I am thinking of a number between 1 and 10')
compare_numbas(number)