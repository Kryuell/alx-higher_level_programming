#!/usr/bin/python3
""" MyList class inherits from list and includes a public method print_sorted()."""
class MyList(list):
    """A class that inherits from list"""
    def print_sorted(self):
        """ Prints the list, but sorted in ascending order."""
        print(sorted(self))
