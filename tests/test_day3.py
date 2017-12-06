import unittest

from day3 import Walker


class TestMatrixDistance(unittest.TestCase):
    def test_matrix_distance(self):
        w = Walker(1)
        self.assertEqual(w.get_current_distance(), 0)
        w = Walker(12)
        self.assertEqual(w.get_current_distance(), 3)
        w = Walker(23)
        self.assertEqual(w.get_current_distance(), 2)
        w = Walker(1024)
        self.assertEqual(w.get_current_distance(), 31)

    def test_tabulation(self):
        w = Walker(1)
        self.assertEqual(w.get_current_value(), 1)
        w = Walker(12)
        self.assertEqual(w.get_current_value(), 57)
