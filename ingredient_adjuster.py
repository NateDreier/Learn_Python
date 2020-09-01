#!/usr/bin/env python3

# One batch calls for 1.5 cups of sugar / 48 is 0.03125
sugar = 0.03125 
# ONe batch calls for 1 cup of butter / 48 is 0.0208
butter = 0.0208
# One batch calls for 2.74 cups of flour / 48 is 0.05729
flour = 0.05729

# Ask the user how many cookies they want
num = int(input("How many cookies would you like? "))

# Finally, print the total number of ingredients - I am printing using f-strings, and the \n is for new line 
print(f'{sugar*num} cups of sugar\n{butter*num} cups of butter \n{flour*num} cups of flour')
