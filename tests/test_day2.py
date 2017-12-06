import unittest

from day2 import checksum, checksum2


class TestChecksum(unittest.TestCase):
    def test_checksum(self):
        test_data = [
                [5, 1, 9, 5],
                [7, 5, 3],
                [2, 4, 6, 8]]
        self.assertEqual(checksum(test_data), 18)

    def test_checksum2(self):
        test_data = [
                [5, 9, 2, 8],
                [9, 4, 7, 3],
                [3, 8, 6, 5]]
        self.assertEqual(checksum2(test_data), 9)

