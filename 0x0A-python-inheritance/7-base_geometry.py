"""
Class BaseGeometry with public instance methods area() and integer_validator().
"""


class BaseGeometry:
    """ Class BaseGeometry """
    def area(self):
        """
        Raises an Exception with the message "area() is not implemented."
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value:
            - If not an integer, raises a TypeError exception with the message "<name> must be an integer."
            - If less or equal to 0, raises a ValueError exception with the message "<name> must be greater than 0."
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
