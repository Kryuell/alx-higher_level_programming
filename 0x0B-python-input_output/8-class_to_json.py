#!/usr/bin/python3
"""
8-class_to_json
Defines a class_to_json function.
"""


def class_to_json(obj):
    """
    Returns a dictionary for JSON serialization of an object.

    Args:
        obj: Instance of a class.

    Returns:
        Dictionary representation of the object.
    """
    return obj.__dict__.copy() if hasattr(obj, "__dict__") else {}
