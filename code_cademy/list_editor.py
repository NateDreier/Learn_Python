#!/usr/bin/python3.6

def list_editor(lst, index):
    if index >= len(lst):
        return(lst)
    else:
        new_list = lst[0:index]
        new_list.append(lst[index]*2)
        new_list.append(lst[-1])
        return(new_list)

def remove_middle(lst, start, end):
    if start >= len(lst) or end >= len(lst):
        return(lst)
    else:
        new_list = lst[0:start]
        new_list = new_list + lst[end+1:]
        print(new_list)
        return(new_list)
    

print(list_editor([1, 2, 3, 4, -12, 6], 4))
print(remove_middle([1, 2, 3, 4 ,22, 34, 5], 1, 3))