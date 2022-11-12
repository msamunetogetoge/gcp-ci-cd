import unittest
from main import add_two_number
class TestStringMethods(unittest.TestCase):
    def test_add_two_int_number(self):
        self.assertEqual(5, add_two_number(2,3))
    def test_add_int_and_float(self):
        with self.assertRaises(TypeError):
            add_two_number(1,0.1)
    