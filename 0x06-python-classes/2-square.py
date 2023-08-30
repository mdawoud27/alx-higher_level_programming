#!/usr/bin/python3

"""This is a define for the square class."""


class Square:
    """This is an empty class that defines a square."""
    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
