#!/usr/bin/python3

"""This is a define of Rectangle"""


class Rectangle:
    """Rectangle"""
    def __init__(self, width=0, height=0):
        """Initalize the rectangle.

        Args:
            width (int): rectangle width
            height (int): rectangle height"""
        self.__width = width
        self.__height = height

    @property
    def height(self):
        """Return the rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the rectangle height.

        Args:
            value (int): Rectangle new height.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Return the width value."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the rectangle width

        Args:
            value (int): rectangle width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
