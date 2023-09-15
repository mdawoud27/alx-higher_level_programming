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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
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
        self.__x = value

    @property
    def y(self):
        """Return y coordinate of the rectangle."""
        return self.__y

    @x.setter
    def x(self, value):
        """Set y coordinate of the rectangle.

        Args:
            value (int): new y coordinate value.
        """
        self.__y = value
