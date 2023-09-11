#!/usr/bin/python3
"""Module doc string"""


class MyInt(int):
    """MyInt doc string."""
    def __eq__(self, __value: object):
        return super().__ne__(__value)

    def __ne__(self, __value: object):
        return super().__eq__(__value)
