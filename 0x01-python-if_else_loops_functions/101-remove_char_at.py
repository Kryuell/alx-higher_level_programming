#!/usr/bin/python3
def remove_char_at(str, n):
    newstr = ""
    for n, c in enumerate(str):
        if n != n:
            newstr += c
    return newstr
