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

print(poppin_lists([1, 2, 3, 4, 3, 2, 1], 4))