#!/usr/bin/python3
"""Module doc string"""


def read_file(filename=""):
    """Function that reads a text file (UTF8)
    and prints it to stdout
    """
    with open(filename) as fn:
        print(fn.read(), end='')
