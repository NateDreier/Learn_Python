#!/usr/bin/python3.6
# @ me robert.
# Chapter 1 went over basic print statements, operators, assignments, and data types.
from datetime import datetime
from dateutil import relativedelta

print('[+] Hello friend, what is your name?')
yourName = input()

print('[+]Your name is ' + yourName) 
lengthOfName = len(yourName)

print('[+] Super fun fact, your name is ' + str(lengthOfName) + ' characters long')

print('[+] How old are you?')
age = input()

print('[+] Cool age bro, you\'ll be ' + str(int(age) + 1) + ' in a year')


#print('when is your birthday?')
#birthdayMonth = input()

#print('there are ' + str(monthsTill) + ' months until you turn ' + str(int(age) + 1) + ' years old')

# Something fun would be to ask what month their birthday is in then print out how many months until their birthday
