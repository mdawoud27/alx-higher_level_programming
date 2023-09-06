#!/usr/bin/python3
"""Module doc string."""


def print_square(size):
    """Function that prints a square.

    Args:
        size (int): the size length of the square.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    size = int(size)
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
