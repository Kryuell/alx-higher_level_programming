#!/usr/bin/python3
"""Check if object is an instance of a specific class"""

def is_same_class(obj, a_class):
    """Return True if object is an instance of the specified class, else False"""
    return type(obj) == a_class
