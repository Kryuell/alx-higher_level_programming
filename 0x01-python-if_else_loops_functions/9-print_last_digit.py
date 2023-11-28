#!/usr/bin/python3
def print_last_digit(n):
    n = abs(n) % 10
    print(n, end="")
    return n
