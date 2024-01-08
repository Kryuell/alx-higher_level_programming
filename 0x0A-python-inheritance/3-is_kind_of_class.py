#!/usr/bin/python3
"""Check if an object is an instance of, or inherited from,
 a specified class."""


def is_kind_of_class(obj, a_class):
    """Return True if the object is an instance of the specified class
    or its subclass; False otherwise.
    """
    return isinstance(obj, a_class)
