import unittest

from day6 import MemoryController


class TestMemoryController(unittest.TestCase):

    def test_infinite_loop_prevention(self):
        controller = MemoryController(banks=[0, 2, 7, 0])
        controller.reallocate()
        self.assertEqual(controller.banks, [2, 4, 1, 2])
        self.assertEqual(len(controller.redistributions), 5)
        self.assertEqual(controller.redistributions,
                         [[0, 2, 7, 0], [2, 4, 1, 2], [3, 1, 2, 3],
                          [0, 2, 3, 4], [1, 3, 4, 1]])

    def test_infinite_loop_additional_cycle(self):
        controller = MemoryController(banks=[0, 2, 7, 0])
        controller.reallocate(repeat_cycle=True)
        self.assertEqual(controller.banks, [2, 4, 1, 2])
        self.assertEqual(len(controller.redistributions), 4)
