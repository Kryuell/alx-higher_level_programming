#!/usr/bin/python3
"""Rectangle class, inherits from Base."""
from models.base import Base

class Rectangle(Base):
    """Rectangle class, inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Rectangle instance with widthht, x, y, and id."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter method for width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width attribute."""
        self.validate_integer("width", value)
        self.validate_positive("width", value)
        self.__width = value

    @property
    def height(self):
        """Getter method for height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height attribute."""
        self.validate_integer("height", value)
        self.validate_positive("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter method for x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for x attribute."""
        self.validate_integer("x", value)
        self.validate_non_negative("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter method for y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for y attribute."""
        self.validate_integer("y", value)
        self.validate_non_negative("y", value)
        self.__y = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """Print the Rectangle instance with the character #."""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Return a string representation of the Rectangle instance."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )

    def validate_integer(self, name, value):
        """Validate if the value is an integer."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

    def validate_positive(self, name, value):
        """Validate if the value is positive (> 0)."""
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def validate_non_negative(self, name, value):
        """Validate if the value is non-negative (>= 0)."""
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def update(self, *args, **kwargs):
        """Assign arguments to attributes."""
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)


    def to_dictionary(self):
        """Return dictionary representation of Rectangle."""
        return {key: getattr(self, key) for key in ('id', 'width', 'height', 'x', 'y')}

    