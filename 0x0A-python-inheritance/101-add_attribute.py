#!/usr/bin/python3
"""Function add_attribute adds a new attribute to an object if possible."""


def add_attribute(obj, attribute, value):
    """Adds a new attribute to the object."""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
