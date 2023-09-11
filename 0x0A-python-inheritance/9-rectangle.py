#!/usr/bin/python3
"""Module doc string"""


BaseGeometry = __import__('7-base_geometry').BasGeometry


class Rectangle(BaseGeometry):
    """Rectangle doc string"""
    def __init__(self, width, height):
        """Initilaization"""
        self.integer_validator("widht", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Area function."""
        return self.__width * self.__height
    
    def __str__(self):
        """__str__ magic function."""
        return f"[Rectangle] {self.__width}/{self.__height}"
