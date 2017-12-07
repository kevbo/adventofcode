def load_offsets(filename):  # pragma: no cover
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


if __name__ == '__main__':  # pragma: no cover
    # Part 1
    o = OffsetHandler(load_offsets('day5_input.txt'))
    o.run()
    print(o.steps)
    # Part 2
    o = OffsetHandler(load_offsets('day5_input.txt'), decrease_over_three=True)
    o.run()
    print(o.steps)
