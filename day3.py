import unittest


class Walker(object):

    def __init__(self, steps):
        self.orientation = 'S'
        self.coords = (0, 0)
        self.steps = steps
        self.next_step = 2
        self.points = {(0, 0): 1}
        for i in range(steps)[1:]:
            if self.can_i_go_left():
                self.turn_left()
                self.step_forward()
            else:
                self.step_forward()

    def get_current_distance(self):
        return abs(self.coords[0]) + abs(self.coords[1])

    def can_i_go_left(self):
        if self.orientation == 'S':
            target = (self.coords[0] + 1, self.coords[1])
        if self.orientation == 'E':
            target = (self.coords[0], self.coords[1] + 1)
        if self.orientation == 'N':
            target = (self.coords[0] - 1, self.coords[1])
        if self.orientation == 'W':
            target = (self.coords[0], self.coords[1] - 1)
        if target in self.points:
            return False
        else:
            return True

    def turn_left(self):
        if self.orientation == 'S':
            self.orientation = 'E'
        elif self.orientation == 'E':
            self.orientation = 'N'
        elif self.orientation == 'N':
            self.orientation = 'W'
        elif self.orientation == 'W':
            self.orientation = 'S'

    def step_forward(self):
        if self.orientation == 'S':
            self.coords = (self.coords[0], self.coords[1] - 1)
            self.points[self.coords] = self.next_step
            self.next_step += 1
        if self.orientation == 'E':
            self.coords = (self.coords[0] + 1, self.coords[1])
            self.points[self.coords] = self.next_step
            self.next_step += 1
        if self.orientation == 'N':
            self.coords = (self.coords[0], self.coords[1] + 1)
            self.points[self.coords] = self.next_step
            self.next_step += 1
        if self.orientation == 'W':
            self.coords = (self.coords[0] - 1, self.coords[1])
            self.points[self.coords] = self.next_step
            self.next_step += 1


def main(steps):
    w = Walker(312051)
    print(w.get_current_distance())


class TestMatrixDistance(unittest.TestCase):
    def test_matrix_distance(self):
        w = Walker(1)
        self.assertEqual(w.get_current_distance(), 0)
        w = Walker(12)
        print(w.points)
        self.assertEqual(w.get_current_distance(), 3)
        w = Walker(23)
        self.assertEqual(w.get_current_distance(), 2)
        w = Walker(1024)
        self.assertEqual(w.get_current_distance(), 31)


if __name__ == '__main__':
    # unittest.main()
    main(312051)
