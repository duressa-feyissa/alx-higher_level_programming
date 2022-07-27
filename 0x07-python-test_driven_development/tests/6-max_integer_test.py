#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_is_list(self):
        self.assertRaises(TypeError, max_integer, [1, 'a', '3', '6'])
        self.assertRaises(TypeError, max_integer, 3)
        self.assertRaises(TypeError, max_integer, 7, 8)

    def test_Max_int(self):
        self.assertEqual(max_integer([1, 2, 5, 4]), 5)
        self.assertEqual(max_integer([-20, -100, -1, -49]), -1)
        self.assertEqual(max_integer([-20, 0, -1, 49, -100]), 49)
        self.assertEqual(max_integer(), None)


if __name__ == '__main__':
    unittest.main()
