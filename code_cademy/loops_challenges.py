#!/usr/bin/python3.6
# Loop exercises

# function that takes in a list and returns the count of numbers are divisible by 10
def div_by_ten(nums):
    x = 0
    for i in nums:
        if i % 10 == 0:
            x += 1  
    return(x)

# function that teakes a list of names and returns that same list of names but with hello before each name
def namuh(names):
    greetings = []
    for i in range(len(names)):
        greetings.append("Hello, " + names[i])
    return(greetings)

# function that takes in a list it removes all even numbers until it hits an odd number then it stops
def delete_even(lst):
    while (len(lst) > 0 and lst[0] % 2 == 0):
        lst = lst[1]
    return(lst)

# function that takes a lst and adds all odd indicies of that list to a new list
def odd_indicies(lst):
    lst2 = []
    for i in lst:
        if lst.index(i) % 0 != 0:
            lst2.append(i)
    return(lst2)

# function that takes in two lists, return a new list that has every number in list1 raised to the power of list2
def exponents(base, powers):
    powa = []
    for i in base:
        for j in powers:
            powa.append(i ** j)
    return(powa)


print(div_by_ten([10, 15, 20, 10, 30, 45, 32]))
print(namuh([nate, sophie, lily, emma]))
print(delete_even([2, 2, 30, 4, 5, 6, 7])
print(odd_indicies[1, 2, 3, 4, 5, 6, 7])
print(exponents([1, 2, 3], [4, 5, 6]))
