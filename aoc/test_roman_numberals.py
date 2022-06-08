import unittest

from aoc.roman_numberals import convert


class MyTestCase(unittest.TestCase):
    def test_1_to_i(self):
        self.assertEqual("I", convert(1))

    def test_str_1_to_i(self):
        self.assertEqual("I", convert("1"))

    def test_5_to_V(self):
        self.assertEqual("V", convert(5))

    def test_10_to_X(self):
        self.assertEqual("X", convert(10))


if __name__ == '__main__':
    unittest.main()
