#!/usr/bin/python3
"""Reclange Module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle doc string"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constractor.

        Args:
            width (int): Rectangle width.
            height (int): Rectangle height.
            x (int): x axis
            y (int): y axis
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Function that returns rectangle width value."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set reclangle width value.

        Args:
            value (int): new width value.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Return reclangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the value of rectangle height.

        Args:
            value (int): new rectangle height value.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Return x coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x coordinate of the rectangle.

        Args:
            value (int): new x coordinate value.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Return y coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y coordinate of the rectangle.

        Args:
            value (int): new y coordinate value.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of rectangle."""
        return self.__height * self.__width
