#!/usr/bin/python3
"""Testing square class"""


import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_init(self):
        square = Square(5, 1, 2, 7)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 2)
        self.assertEqual(square.id, 7)

    def test_size_property_and_setter(self):
        square = Square(3)
        self.assertEqual(square.size, 3)
        square.size = 7
        self.assertEqual(square.size, 7)

    def test_area(self):
        square = Square(3)
        self.assertEqual(square.area(), 9)

    def test_display(self):
        import sys
        from io import StringIO
        original_stdout = sys.stdout
        sys.stdout = StringIO()

        square = Square(2)
        square.display()
        expected_output = "##\n##\n"
        self.assertEqual(sys.stdout.getvalue(), expected_output)

        sys.stdout = original_stdout

    def test_str(self):
        square = Square(4, 1, 2, 7)
        expected_str = "[Square] (7) 1/2 - 4"
        self.assertEqual(str(square), expected_str)

    def test_update_args(self):
        square = Square(2, 1, 2, 7)
        square.update(8, 4, 3, 1)
        self.assertEqual(square.id, 8)
        self.assertEqual(square.size, 4)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 1)

    def test_update_kwargs(self):
        square = Square(2, 1, 2, 7)
        square.update(size=4, x=3, y=1, id=8)
        self.assertEqual(square.id, 8)
        self.assertEqual(square.size, 4)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 1)

    def test_update_with_args(self):
        """test update method arguments"""
        square = Square(5, 10, 0, 10)
        square.update(1, 2, 3, 4)
        self.assertEqual(1, square.id)
        self.assertEqual(2, square.size)
        self.assertEqual(3, square.x)
        self.assertEqual(4, square.y)

    def test_update_with_args_kwargs(self):
        """test update method args kwargs in this case we have to use args"""
        square = Square(5, 10, 0, 10)

        # case 1 using real attr
        square.update(1, id=2)
        self.assertEqual(1, square.id)

        # case 2 using fake attr
        square.update(1, emad=2)
        self.assertEqual(1, square.id)


if __name__ == '__main__':
    unittest.main()
