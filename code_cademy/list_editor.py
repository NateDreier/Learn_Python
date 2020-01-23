#!/usr/bin/python3.6

# replace index with index*2
def list_editor(lst, index):
    if index >= len(lst):
        return(lst)
    else:
        new_list = lst[0:index]
        new_list.append(lst[index]*2)
        new_list.append(lst[-1])
        return(new_list)

# remove items in lst from start to end (inclusive)
def remove_middle(lst, start, end):
    if start >= len(lst) or end >= len(lst):
        return(lst)
    else:
        new_list = lst[0:start]
        new_list = new_list + lst[end+1:]
        return(new_list)

# Does item show up more than n times in lst?
def more_than_n(lst, item, n):
    if lst.count(item) == n:
        return False
    elif lst.count(item) > n:
        return True
    else:
        return False

# Return which item appears the most in lst
def more_than(lst, item1, item2):
    if lst.count(item1) > lst.count(item2):
        return("item1 wins " + str(item1))
    elif lst.count(item2) > lst.count(item1):
        return("item2 wins " + str(item2))
    else:
        return("it is a tie")

# return the middle element of lst if it is odd, take the middle two elements and average them together if even
def this_is_gross(lst):
    if len(lst) % 2 != 0:
        return(lst[int(len(lst)/2)])
    else:
        dis_sux = (lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]) / 2
        return(dis_sux)

# function that takes in a list(lst), appends the sum of the last two elements and does that n times

def num_dum(lst, n):
    for i in range(n):
        lst.append((int(lst[-1]) + int(lst[-2])))
    return(lst)

# combine two lists then sort
def sortysort_sort(lst1, lst2):
    new_list = lst1 + lst2
    new_list.sort()
    return(new_list)

# function takes a number, you create a list that starts with that number and iterates by 3 to 100
def this_one_sucked(start):
    if start > 101:
        lst = []
        return(lst)
    else:
        lst = []
        for i in range(start, 101, 3):
            lst.append(i)
    return(lst)

print(list_editor([1, 2, 3, 4, -12, 6], 4))
print(remove_middle([1, 2, 3, 4 ,22, 34, 5], 1, 3))
print(more_than_n([1, 2, 3, 4, 4, 4, 5], 4, 2))
print(more_than([1, 1, 2, 2, 2, 3, 4], 1, 2))
# odd
print(this_is_gross([1, 2, 3, 4, 4, 5, 6]))
# even
print(this_is_gross([1, 2, 3, 4, 12, 5, 6, 7]))
print(num_dum([1, 2, 3], 3))
print(sortysort_sort([1, 3, 5, 7], [0, 2, 4, 6]))
print(this_one_sucked(91))