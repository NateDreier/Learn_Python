#!/usr/bin/python3.6

'''
FizzBuzz, print numbers zero through thirty. If the number is divisible by 3 print 'Fizz' if the number is divisible by 5 print 'Buzz', if it is divisible by both, print 'FizzBuzz'.
'''

import time
start_time = time.time()

num = 0
for num in range(31):
	if num == 0:
		print(num)
#	elif num % 3 == 0 and num % 5 == 0:
#		print('Fizzbuzz')
	if num % 3 == 0:
		print('Fizz')
	if num % 5 == 0:
		print('Buzz')
	else:
		print(num)
print('%s seconds ' % (time.time() - start_time))

'''
import time
start_time = time.time()

def fizzbuzz(start, end):
	def int_to_fizzbuzz(i):
		entry = ''
		if i % 3 == 0 and i % 5 == 0:
			entry += "fizzbuzz"
		if i % 3 == 0:
			entry += "fizz"
		if i % 5 == 0:
			entry += "buzz"
		if i % 3 != 0 and i % 5 != 0:
			entry += str(i)
		return entry
	return [int_to_fizzbuzz(i) for i in range(start, end+1)]

#print('%s seconds ' % (time.time() - start_time()))

if __name__ == "__main__":
	start = int(input("starting #: "))
	end = int(input("ending #: "))
	for i in fizzbuzz(start, end):
		print(i)
	print('%s seconds ' % (time.time() - start_time))
'''
