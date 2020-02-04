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

# function that takes two lists, sums the total of the elements in each list and returns which list is greater if tied return lst1
def summ(lst1, lst2):
    a = sum(lst1)
    b = sum(lst2)
    if a > b:
        return(lst1)
    elif b > a:
        return(lst2)
    else:
        return(lst1)
#orr....
def larger_sum(lst1, lst2):
    if sum(lst1) > sum(lst2):
        return(lst1)
    elif sum(lst2) > sum(lst1):
        return(lst2)
    else:
        return(lst1)

# function that takes in a list and sums it up to one thousand and stops. returns that number. if list never reaches 1000, return 0.
def one_thou(lst):
    sum = 0
    for i in lst:
        if sum > 9000:
            break
        else:
            sum += i
    if sum < 9000:
        return(0)
    else:
        return(sum)


print(div_by_ten([10, 15, 20, 10, 30, 45, 32]))
print(namuh([nate, sophie, lily, emma]))
print(delete_even([2, 2, 30, 4, 5, 6, 7])
print(odd_indicies[1, 2, 3, 4, 5, 6, 7])
print(exponents([1, 2, 3], [4, 5, 6]))
print(summ([1, 4, 7, 4], [12, 0, 3, 2]))
print(one_thou([800, 20, 30, 46, 100, 150, 100, 200]))
