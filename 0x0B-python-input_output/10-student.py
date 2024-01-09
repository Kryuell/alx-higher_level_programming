#!/usr/bin/python3
"""
Defines a class Student
"""


class Student:
    """
    Defines a student with first_name, last_name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with specified attributes.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


def to_json(self, attrs=None):
    """
    Retrieves a dictionary representation of a Student instance
    based on provided attributes.
    If attrs is a list of strings, only those attributes are retrieved.
    Otherwise, all attributes are retrieved.

    Args:
        attrs (list): List of strings representing the attributes to retrieve.

    Returns:
        dict: Dictionary representation of the Student instance.
    """
    if attrs is None:
        return self.__dict__

    return {
        attr: getattr(self, attr)
        for attr in attrs
        if isinstance(attr, str) and hasattr(self, attr)
    }
