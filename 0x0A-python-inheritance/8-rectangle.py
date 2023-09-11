#!/usr/bin/python3
"""Module doc string"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle doc string"""
    def __init__(self, width, height):
        """Initilaization"""
        self.integer_validator("widht", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
