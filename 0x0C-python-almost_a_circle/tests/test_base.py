#!/usr/bin/python3
"""Testing base class"""


import unittest
import json
from models.base import Base


class TestBase(unittest.TestCase):

    def test_docstrings(self):
        self.assertIsNotNone(Base.__doc__)
        self.assertIs(hasattr(Base, "__init__"), True)
        self.assertIsNotNone(Base.__init__.__doc__)
        self.assertIs(hasattr(Base, "create"), True)
        self.assertIsNotNone(Base.create.__doc__)
        self.assertIs(hasattr(Base, "to_json_string"), True)
        self.assertIsNotNone(Base.to_json_string.__doc__)
        self.assertIs(hasattr(Base, "from_json_string"), True)
        self.assertIsNotNone(Base.from_json_string.__doc__)
        self.assertIs(hasattr(Base, "save_to_file"), True)
        self.assertIsNotNone(Base.save_to_file.__doc__)
        self.assertIs(hasattr(Base, "load_from_file"), True)
        self.assertIsNotNone(Base.load_from_file.__doc__)

    def setUp(self):
        Base.__nb_objects = 0

    def test_init_with_id(self):
        base_instance = Base(5)
        self.assertEqual(base_instance.id, 5)

    def test_init_without_id(self):
        base_instance = Base()
        self.assertEqual(base_instance.id, 1)

    def test_to_json_string(self):
        data = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
        json_string = Base.to_json_string(data)
        expected_json_string = json.dumps(data)
        self.assertEqual(json_string, expected_json_string)

    def test_to_json_string_with_none(self):
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_from_json_string(self):
        json_string = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
        data = Base.from_json_string(json_string)
        expected_data = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
        self.assertEqual(data, expected_data)


if __name__ == '__main__':
    unittest.main()
