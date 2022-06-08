import unittest

from aoc.d01 import process_data_a
from aoc.d01 import process_data_b


class TestUtils(unittest.TestCase):
    def test_d01a_testdata(self):
        self.assertEqual(7, process_data_a("d01.testdata.txt"))

    def test_d01a_realdata(self):
        self.assertEqual(1477, process_data_a("d01.realdata.txt"))

    def test_d01b_testdata(self):
        self.assertEqual(5, process_data_b("d01.testdata.txt"))

    def test_d01b_realdata(self):
        self.assertEqual(1523, process_data_b("d01.realdata.txt"))


if __name__ == '__main__':
    unittest.main()
