#!/usr/bin/python3
"""Module doc string"""


class BaseGeometry:
    """BaseGeometry class doc string"""

    def area(self):
        """Function doc string"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function doc string"""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle doc string"""
    def __init__(self, width, height):
        """Initilaization"""
        self.integer_validator("widht", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
