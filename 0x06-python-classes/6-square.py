#!/usr/bin/python3

"""This is a define for the square class."""


class Square:
    """This is an empty class that defines a square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            size (int): The size of the square.
            position (int, int): The coordinates of the square.
        """
        self.__size = size
        self.__position = position

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

        @property
        def position(self):
            """Return the coordinates of the square."""
            return self.__position

        @position.setter
        def position(self, value):
            """Set the coordinates of the square.

            Args:
                value (int, int): The coordinates to set
            """
            if not isinstance(value, tuple) or \
               len(value) != 2 or \
               not all(isinstance(num, int) for num in value) or \
               not all(num > 0 for num in value):
                raise TypeError('position must be a tuple of 2 \
                                positive integers')
            self.__position = value

    def area(self):
        """Calculate the area of the square.

        Return:
            Square area.
        """
        return self.__size * self.__size

    def my_print(self):
        """Prints the square."""
        [print() for i in range(0, self.__position[1])]
        if self.__size == 0:
            print()
            return
        for i in range(0, self.__size):
            for k in range(0, self.__position[0]):
                print(' ', end='')
            for j in range(0, self.__size):
                print('#', end='')
            print()
