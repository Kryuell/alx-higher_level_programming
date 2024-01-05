#!/usr/bin/python3

def magic_string(string=None):
    if string is None:
        string = ["BestSchool"]
    else:
        string.append("BestSchool")
    return ", ".join(string)
