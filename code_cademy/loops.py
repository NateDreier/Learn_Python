#!/usr/bin/python3.6

# two lists, pop from populated list x times to the empty list
def poppin_lists(lst, p):
    new_lst = []
    i = 0
    while i < p:
        new_lst.append(lst[-1])
        lst.pop()
        i += 1
    return(new_lst)

# add all the elements in list

def listception(lst):
    ttl = 0
    for i in lst:
        for j in i:
            ttl += j
    return(ttl)

def cool_stuff(lst):
    new_lst = [l for l in lst if l > 2]
    return(new_lst)

print(poppin_lists([1, 2, 3, 4, 3, 2, 1], 4))
print(listception([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(cool_stuff([1, 2, 3, 4, 3, 2, 1]))
