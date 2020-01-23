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
    

print(list_editor([1, 2, 3, 4, -12, 6], 4))
print(remove_middle([1, 2, 3, 4 ,22, 34, 5], 1, 3))
print(more_than_n([1, 2, 3, 4, 4, 4, 5], 4, 2))