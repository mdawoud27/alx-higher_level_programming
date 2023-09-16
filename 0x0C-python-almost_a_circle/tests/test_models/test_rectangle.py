#!/usr/bin/python3
"""Testing rectangle class"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_init(self):
        rectangle = Rectangle(5, 10, 1, 2, 7)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 1)
        self.assertEqual(rectangle.y, 2)
        self.assertEqual(rectangle.id, 7)

    def test_area(self):
        rectangle = Rectangle(3, 4)
        self.assertEqual(rectangle.area(), 12)

    def test_display(self):
        import sys
        from io import StringIO
        original_stdout = sys.stdout
        sys.stdout = StringIO()

        rectangle = Rectangle(2, 2)
        rectangle.display()
        expected_output = "##\n##\n"
        self.assertEqual(sys.stdout.getvalue(), expected_output)

        sys.stdout = original_stdout

    def test_str(self):
        rectangle = Rectangle(4, 5, 1, 2, 7)
        expected_str = "[Rectangle] (7) 1/2 - 4/5"
        self.assertEqual(str(rectangle), expected_str)

    def test_update_args(self):
        rectangle = Rectangle(2, 3, 1, 2, 7)
        rectangle.update(8, 4, 5, 3, 1, 9)
        self.assertEqual(rectangle.id, 8)
        self.assertEqual(rectangle.width, 4)
        self.assertEqual(rectangle.height, 5)
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 1)

    def test_update_kwargs(self):
        rectangle = Rectangle(2, 3, 1, 2, 7)
        rectangle.update(width=4, height=5, x=3, y=1, id=8)
        self.assertEqual(rectangle.id, 8)
        self.assertEqual(rectangle.width, 4)
        self.assertEqual(rectangle.height, 5)
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 1)

    def test_to_dictionary(self):
        rectangle = Rectangle(4, 5, 1, 2, 7)
        expected_dict = {'id': 7, 'width': 4, 'height': 5, 'x': 1, 'y': 2}
        self.assertEqual(rectangle.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
