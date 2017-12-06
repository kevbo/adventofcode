import unittest

from day5 import OffsetHandler


class TestOffsetHandler(unittest.TestCase):

    def test_standard_offsets(self):
        offsets = [0, 3, 0, 1, -3]
        o = OffsetHandler(offsets)
        o.run()
        self.assertEqual(o.offsets, [2, 5, 0, 1, -2])
        self.assertEqual(o.steps, 5)

    def test_offsets_with_decreases(self):
        offsets = [0, 3, 0, 1, -3]
        o = OffsetHandler(offsets, decrease_over_three=True)
        o.run()
        self.assertEqual(o.offsets, [2, 3, 2, 3, -1])
        self.assertEqual(o.steps, 10)
