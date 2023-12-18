#!/usr/bin/python3

def safe_print_list_integers(my_list=None, x=0):
    count = 0
    if my_list is None:
        my_list = []
    
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (TypeError, ValueError):
            pass
    
    print("")
    return count
