#!/usr/bin/python3

class MyList(list):
    """
    MyList class inherits from list and includes a public method print_sorted().
    """


    def __init__(self):
        """
        Initializes an empty MyList.
        """
        super().__init__()

    def print_sorted(self):
        """
        Prints the list, but sorted in ascending order.
        """
        print(sorted(self))
