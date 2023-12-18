#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    printed = 0

    for i in range(x):
        try:
            # Check if the current index is within the valid range of the list
            if 0 <= i < len(my_list):
                print("{:d}".format(my_list[i]), end="")
                printed += 1
        except ValueError:
            continue

    print()
    return printed
