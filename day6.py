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


def main(repeat_cycle=False):
    controller = MemoryController(banks=[14, 0, 15, 12, 11, 11, 3, 5, 1, 6,
                                         8, 4, 9, 1, 8, 4])
    controller.reallocate(repeat_cycle=repeat_cycle)
    print(len(controller.redistributions))


if __name__ == '__main__':
    main()
    main(repeat_cycle=True)
