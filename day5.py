import unittest


def load_offsets(filename):
    with open(filename) as f:
        offsets = f.readlines()
    return [int(offset) for offset in offsets]


class OffsetHandler(object):

    def __init__(self, offsets, decrease_over_three=False):
        self.offsets = offsets
        self.steps = 0
        self.current_index = 0
        self.next_index = 0
        self.decrease_over_three = decrease_over_three

    def run(self):
        while True:
            try:
                self.next_index = (self.current_index +
                                   self.offsets[self.current_index])
                if (self.decrease_over_three and
                        self.offsets[self.current_index] >= 3):
                        self.offsets[self.current_index] -= 1
                else:
                    self.offsets[self.current_index] += 1
                self.current_index = self.next_index
                self.steps += 1
            except IndexError:
                break


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


if __name__ == '__main__':
    # unittest.main()
    # Part 1
    o = OffsetHandler(load_offsets('day5_input.txt'))
    o.run()
    print(o.steps)
    # Part 2
    o = OffsetHandler(load_offsets('day5_input.txt'), decrease_over_three=True)
    o.run()
    print(o.steps)
