from copy import copy


class Walker(object):
    def __init__(self, instructions):
        self.instructions = instructions
        self.coords = [0,0]
        self.path = [[0,0]]
        self.orientation = 0
        self.steps = self.load_instructions()
        self.multiple_visits = []

    def load_instructions(self):
        with open(self.instructions) as f:
            steps = f.read()
        steps = steps.split(',')
        steps = [step.strip() for step in steps]
        return steps

    def walk(self):
        for step in self.steps:
            direction = step[0]
            number_of_steps = int(step[1:])
            self.change_orientation(step[0])
            self.move(number_of_steps)

    def move(self, number_of_steps):
        for i in range(number_of_steps):
            if self.orientation == 90:
                self.coords[1] += 1
            if self.orientation == 180:
                self.coords[0] -= 1
            if self.orientation == 0 or self.orientation == 360:
                self.coords[0] += 1
            if self.orientation == 270:
                self.coords[1] -=1
            if self.coords in self.path:
                 self.multiple_visits.append(copy(self.coords))
            self.path.append(copy(self.coords))

    def change_orientation(self, direction):
        if direction == 'L':
            self.orientation = self.orientation - 90
            if self.orientation < 0:
                self.orientation = 270
        if direction == 'R':
            self.orientation = self.orientation + 90
            if self.orientation > 360:
                self.orientation = 90


if __name__ == '__main__':
    w = Walker('day1_input.txt')
    w.walk()
    print 'Final Coordinates:', w.coords
    total_blocks_from_start = abs(w.coords[0]) + abs(w.coords[1])
    print "I'm {} blocks away from (0,0)".format(total_blocks_from_start)
    print w.multiple_visits[0]
    total_blocks_from_start = abs(w.multiple_visits[0][0]) + abs(w.multiple_visits[0][1])  
    print "I was {} blocks away from (0,0) when I first crossed my path".format(total_blocks_from_start)
