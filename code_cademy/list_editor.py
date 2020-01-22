#!/usr/bin/python3.6

def list_editor(lst, index):
    if index >= len(lst):
        return(lst)
    else:
        new_list = lst[0:index]
        new_list.append(lst[index]*2)
        new_list.append(lst[-1])
        return(new_list)

print(list_editor([1, 2, 3, 4, -12, 6], 4))