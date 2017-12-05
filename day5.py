import unittest


def load_offsets(filename):
    with open(filename) as f:
        offsets = f.readlines()
    return [int(offset) for offset in offsets]


class OffsetHandler(object):

    def __init__(self, offsets):
        self.offsets = offsets
        self.steps = 0
        self.current_index = 0
        self.next_index = 0

    def run(self):
        while True:
            try:
                self.next_index = self.current_index + self.offsets[self.current_index]
                self.offsets[self.current_index] += 1
                self.current_index = self.next_index
                self.steps += 1
            except IndexError:
                break


class TestOffsetHandler(unittest.TestCase):

    def setUp(self):
        self.offsets = [0, 3, 0, 1, -3]

    def test_offset_jumps(self):
        offsets = [0, 3, 0, 1, -3]
        o = OffsetHandler(offsets)
        o.run()
        self.assertEqual(o.offsets, [2, 5, 0, 1, -2])
        self.assertEqual(o.steps, 5)


if __name__ == '__main__':
    # unittest.main()
    o = OffsetHandler(load_offsets('day5_input.txt'))
    o.run()
    print(o.steps)
