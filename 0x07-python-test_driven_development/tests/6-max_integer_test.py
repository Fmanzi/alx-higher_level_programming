#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from parameterized import parameterized
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    @parameterized.expand([
        ([1, 2, 3, 4], 4),
        ([1, 3, 4, 2], 4),
        ([1, 1, 1, 1], 1),
        ([-1, -2, -3, -4], -1),
        ([1], 1),
        ([-1], -1),
        ([], None)
    ])
    def test_max_integer(self, arr, result):
        self.assertEqual(max_integer(arr), result)

    def test_max_integer_exception(self):
        with self.assertRaises(TypeError):
            max_integer(None)

if __name__ == '__main__':
    unittest.main()

