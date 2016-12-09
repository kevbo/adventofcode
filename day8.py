import re
import unittest
from collections import deque, Counter


class Panel(object):
    def __init__(self, panel_size):
        self.panel_size = panel_size
        self.display = self.build_display()
        self.print_display()

    def build_display(self):
        columns = self.panel_size[0]
        rows = self.panel_size[1]
        display = []
        for i in range(rows):
            display.append([])
        for row in display:
            for i in range(columns):
                row.append('.')
        return display

    def print_display(self):
        print ''
        for row in self.display:
            print ''.join(row)

    def handle_rect(self, instruction):
        coords = re.search(r'(\d+x\d+)', instruction)
        coords = coords.groups()[0].split('x')
        coords = (int(coords[0]), int(coords[1]))
        for row in range(coords[1]):
            for column in range(coords[0]):
                self.display[row][column] = '#'
        self.print_display()

    def handle_rotate(self, instruction):
        if 'column' in instruction:
            results = re.search(r'x=(\d+) by (\d+)', instruction)
            col_no = int(results.groups()[0])
            rotate_by = int(results.groups()[1])
            column = [row[col_no] for row in self.display]
            column = deque(column)
            column.rotate(rotate_by)
            for i, row in enumerate(self.display):
                row[col_no] = column[i]
            self.print_display()
        if 'row' in instruction:
            results = re.search(r'y=(\d+) by (\d+)', instruction)
            row_no = int(results.groups()[0])
            rotate_by = int(results.groups()[1])
            row = self.display[row_no]
            row = deque(row)
            row.rotate(rotate_by)
            self.display[row_no] = list(row)
            self.print_display()

    def input_instructions(self, instructions):
        for instruction in instructions:
            if instruction.startswith('rect'):
                self.handle_rect(instruction)
            if instruction.startswith('rotate'):
                self.handle_rotate(instruction)

    def count_lit_pixels(self):
        count = 0
        for row in self.display:
            count += Counter(row)['#']
        return count


class TestPanel(unittest.TestCase):
    def setUp(self):
        self.instructions = ['rect 3x2',
                             'rotate column x=1 by 1',
                             'rotate row y=0 by 4',
                             'rotate column x=1 by 1']
        self.panel_size = (7, 3)  # 7x3
        self.expected_display = [
            ['.', '#', '.', '.', '#', '.', '#'],
            ['#', '.', '#', '.', '.', '.', '.'],
            ['.', '#', '.', '.', '.', '.', '.']
        ]
        self.expected_lit_pixels = 6

    def test_input(self):
        panel = Panel(self.panel_size)
        panel.input_instructions(self.instructions)
        self.assertEqual(self.expected_display, panel.display)
        self.assertEqual(self.expected_lit_pixels, panel.count_lit_pixels())


if __name__ == '__main__':
    # unittest.main()
    with open('day8_input.txt') as f:
        instructions = f.readlines()
    panel = Panel((50, 6))
    panel.input_instructions(instructions)
    panel.print_display()
    print ('There are {} lit pixels '
           'on the display'.format(panel.count_lit_pixels()))
