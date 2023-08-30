#!/usr/bin/python3

"""This is a define for the square class."""


class Square:
    """This is an empty class that defines a square."""
    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """Get the current size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size value to set.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Calculate the area of the square.

        Return:
            Square area.
        """
        return self.__size * self.__size

    def my_print(self):
        """Prints the square."""
        if self.__size == 0:
            print()
            return
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print('#', end='')
            print()
