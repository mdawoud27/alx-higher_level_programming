#!/usr/bin/python3
"""Module doc string"""


class MyList(list):
    """MyList doc string"""

    def print_sorted(self):
        """print_sorted doc string"""
        new_list = self.copy()
        new_list.sort()
        print(new_list)
