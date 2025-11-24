#!/usr/bin/python3
"""Rectangle class with eval-enabled representation."""


class Rectangle:
    """Defines a rectangle using width and height."""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return area of rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return perimeter of rectangle.

        If width or height is 0 → perimeter is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return printable rectangle using '#'."""
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_rows = []
        for _ in range(self.__height):
            rectangle_rows.append("#" * self.__width)

        return "\n".join(rectangle_rows)

    def __repr__(self):
        """Return string that can recreate the rectangle using eval()."""
        return f"Rectangle({self.__width}, {self.__height})"
