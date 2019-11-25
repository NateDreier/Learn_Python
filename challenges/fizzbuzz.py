#!/usr/bin/python3.6

'''
FizzBuzz, print numbers zero through thirty. If the number is divisible by 3 print 'Fizz' if the number is divisible by 5 print 'Buzz', if it is divisible by both, print 'FizzBuzz'.
'''

num = 0
for num in range(31):
	if num == 0:
		print(num)
	elif num % 3 == 0 and num % 5 == 0:
		print('Fizzbuzz')
	elif num % 3 == 0:
		print('Fizz')
	elif num % 5 == 0:
		print('Buzz')
	else:
		print(num)
