import unittest
from copy import copy


class MemoryController(object):

    def __init__(self, banks):
        self.banks = banks
        self.redistributions = [copy(banks)]

    def reallocate(self, repeat_cycle=False):
        while True:
            starting_bank = self.banks.index(max(self.banks))
            to_distribute = self.banks[starting_bank]
            self.banks[starting_bank] = 0
            for i in range(to_distribute):
                starting_bank += 1
                try:
                    self.banks[starting_bank] += 1
                except IndexError:
                    starting_bank -= len(self.banks)
                    self.banks[starting_bank] += 1
            if self.banks in self.redistributions:
                if repeat_cycle:
                    self.redistributions = [copy(self.banks)]
                    repeat_cycle = False
                else:
                    break
            else:
                self.redistributions.append(copy(self.banks))


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


def main(repeat_cycle=False):
    controller = MemoryController(banks=[14, 0, 15, 12, 11, 11, 3, 5, 1, 6,
                                         8, 4, 9, 1, 8, 4])
    controller.reallocate(repeat_cycle=repeat_cycle)
    print(len(controller.redistributions))


if __name__ == '__main__':
    # unittest.main()
    main()
    main(repeat_cycle=True)
