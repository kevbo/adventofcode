class Keypad(object):
    def __init__(self, pad_number, start_position):
        # start_position is row, column, 0-indexed. [2,2] = button 5
        self.current_position = start_position
        self.pad1 = [
                ['X', 'X', 'X', 'X'],
                ['X', 1, 2, 3, 'X'],
                ['X', 4, 5, 6, 'X'],
                ['X', 7, 8, 9, 'X'],
                ['X', 'X', 'X', 'X']
                ]
        self.pad2 = [
                ['X', 'X', 'X', 'X', 'X', 'X', 'X'],
                ['X', 'X', 'X', 1, 'X', 'X', 'X'],
                ['X', 'X', 2, 3, 4, 'X', 'X'],
                ['X', 5, 6, 7, 8, 9, 'X'],
                ['X', 'X', 'A', 'B', 'C', 'X', 'X'],
                ['X', 'X', 'X', 'D', 'X', 'X', 'X'],
                ['X', 'X', 'X', 'X', 'X', 'X', 'X']
                ]
        if pad_number == 1:
            self.pad = self.pad1
        elif pad_number == 2:
            self.pad = self.pad2

    @property
    def current_key(self):
        return self.pad[self.current_position[0]][self.current_position[1]]

    def process_instruction(self, direction):
            if direction == 'U':
                self.current_position[0] -= 1
                if self.current_key == 'X':
                    self.current_position[0] += 1
            if direction == 'D':
                self.current_position[0] += 1
                if self.current_key == 'X':
                    self.current_position[0] -= 1
            if direction == 'L':
                self.current_position[1] -= 1
                if self.current_key == 'X':
                    self.current_position[1] += 1
            if direction == 'R':
                self.current_position[1] += 1
                if self.current_key == 'X':
                    self.current_position[1] -= 1


def load_instructions(input_file):
    with open(input_file) as f:
        instructions = f.readlines()
    return instructions


if __name__ == '__main__':
    # Part 1
    k = Keypad(pad_number=1, start_position=[2, 2])
    print "My starting key is:", k.current_key
    instructions = load_instructions('day2_input.txt')
    for key in instructions:
        for step in key:
            k.process_instruction(step)
        print 'I just pressed {}!'.format(k.current_key)
    # Part 2
    k = Keypad(pad_number=2, start_position=[3, 0])
    print "My starting key is:", k.current_key
    instructions = load_instructions('day2_input.txt')
    for key in instructions:
        for step in key:
            k.process_instruction(step)
        print 'I just pressed {}!'.format(k.current_key)
