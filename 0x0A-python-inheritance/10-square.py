#!/usr/bin/python3
"""Module doc string"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square doc string."""
    def __init__(self, size):
        """Instantiation function."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Square area function."""
        return self.__size * self.__size
