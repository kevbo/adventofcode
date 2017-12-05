import unittest


class Walker(object):

    def __init__(self, steps):
        self.orientation = 'S'
        self.coords = (0, 0)
        self.steps = steps
        self.next_step = 2
        self.points = {(0, 0): {'step': 1, 'value': 1}}
        self.tabulator = [1]
        for i in range(steps)[1:]:
            if self.can_i_go_left():
                self.turn_left()
                self.step_forward()
            else:
                self.step_forward()

    def get_current_distance(self):
        return abs(self.coords[0]) + abs(self.coords[1])

    def get_current_value(self):
        return self.points[self.coords]['value']

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

    def sum_value_of_neighbors(self):
        sum_neighbors = 0
        # N
        if (self.coords[0], self.coords[1] + 1) in self.points:
            sum_neighbors += self.points[(self.coords[0], self.coords[1] + 1)]['value']
        # E
        if (self.coords[0] + 1, self.coords[1]) in self.points:
            sum_neighbors += self.points[(self.coords[0] + 1, self.coords[1])]['value']
        # S
        if (self.coords[0], self.coords[1] - 1) in self.points:
            sum_neighbors += self.points[(self.coords[0], self.coords[1] - 1)]['value']
        # W
        if (self.coords[0] - 1, self.coords[1]) in self.points:
            sum_neighbors += self.points[(self.coords[0] - 1, self.coords[1])]['value']
        # NE
        if (self.coords[0] + 1, self.coords[1] + 1) in self.points:
            sum_neighbors += self.points[(self.coords[0] + 1, self.coords[1] + 1)]['value']
        # SE
        if (self.coords[0] + 1, self.coords[1] - 1) in self.points:
            sum_neighbors += self.points[(self.coords[0] + 1, self.coords[1] - 1)]['value']
        # SW
        if (self.coords[0] - 1, self.coords[1] - 1) in self.points:
            sum_neighbors += self.points[(self.coords[0] - 1, self.coords[1] - 1)]['value']
        # NW
        if (self.coords[0] - 1, self.coords[1] + 1) in self.points:
            sum_neighbors += self.points[(self.coords[0] - 1, self.coords[1] + 1)]['value']
        return sum_neighbors

    def step_forward(self):
        if self.orientation == 'S':
            self.coords = (self.coords[0], self.coords[1] - 1)
            self.points[self.coords] = {'step': self.next_step, 'value': self.sum_value_of_neighbors()}
            self.next_step += 1
        elif self.orientation == 'E':
            self.coords = (self.coords[0] + 1, self.coords[1])
            self.points[self.coords] = {'step': self.next_step, 'value': self.sum_value_of_neighbors()}
            self.next_step += 1
        elif self.orientation == 'N':
            self.coords = (self.coords[0], self.coords[1] + 1)
            self.points[self.coords] = {'step': self.next_step, 'value': self.sum_value_of_neighbors()}
            self.next_step += 1
        elif self.orientation == 'W':
            self.coords = (self.coords[0] - 1, self.coords[1])
            self.points[self.coords] = {'step': self.next_step, 'value': self.sum_value_of_neighbors()}
            self.next_step += 1


def main(steps):
    w = Walker(steps)
    print(w.get_current_distance())
    for step in range(steps)[1:]:
        w = Walker(step)
        if w.get_current_value() > steps:
            print('First value bigger than %s: %s' % (steps, w.get_current_value()))
            break


class TestMatrixDistance(unittest.TestCase):
    def test_matrix_distance(self):
        w = Walker(1)
        self.assertEqual(w.get_current_distance(), 0)
        w = Walker(12)
        self.assertEqual(w.get_current_distance(), 3)
        w = Walker(23)
        self.assertEqual(w.get_current_distance(), 2)
        w = Walker(1024)
        self.assertEqual(w.get_current_distance(), 31)

    def test_tabulation(self):
        w = Walker(1)
        self.assertEqual(w.get_current_value(), 1)
        w = Walker(12)
        self.assertEqual(w.get_current_value(), 57)


if __name__ == '__main__':
    # unittest.main()
    main(312051)