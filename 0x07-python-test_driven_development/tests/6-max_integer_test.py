#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """class test for the max_integer func"""
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_max_first(self):
        self.assertEqual(max_integer([9, 2, 0, 7]), 9)

    def test_max_end(self):
        self.assertEqual(max_integer([9, 0, -3, 11]), 11)

    def test_max_mid(self):
        self.assertEqual(max_integer([8, 0, 12, 10, -54]), 12)

    def test_max_minus(self):
        self.assertEqual(max_integer([-2, -12, 0, -5]), 0)

    def test_one_arg(self):
        self.assertEqual(max_integer([27]), 27)


if __name__ == '__main__':
    unittest.main()
