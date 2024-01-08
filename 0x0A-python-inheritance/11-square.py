#!/usr/bin/python3
"""
Class Square inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Initializes a Square instance with size."""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)

    """Returns a string representation of the Square instance."""
    def __str__(self):
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)
