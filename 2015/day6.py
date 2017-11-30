import re
import itertools


def get_instructions():
    instructions = []
    with open('day6_input.txt') as f:
        data = f.readlines()
    for instruction in data:
        regex = '(turn on|turn off|toggle) (\d+,\d+) through (\d+,\d+)'
        matches = re.match(regex, instruction)
        command = matches.groups()[0]
        start = matches.groups()[1].split(',')
        start = tuple([int(start[0]), int(start[1])])
        end = matches.groups()[2].split(',')
        end = tuple([int(end[0]), int(end[1])])
        instructions.append((command, start, end))
    return instructions


def expand_rectangle(corner1, corner2):
    """Takes 2 sets of coordinates, which define
    opposing corners of a rectangle on a 1000x1000
    grid. Returns a list of all coordinates within
    that rectangle (inclusive).
    """
    points = []
    # assuming 0,0 - 2,2
    minX = corner1[0]
    minY = corner1[1]
    maxX = corner2[0]
    maxY = corner2[1]
    valid_x_coords = range(minX, maxX + 1)
    valid_y_coords = range(minY, maxY + 1)
    return itertools.product(valid_x_coords, valid_y_coords)


def handle_instruction(instruction, lights):
    """Take in one set of instructions and perform them on
    the array of lights
    """
    points = expand_rectangle(instruction[1], instruction[2])
    for point in points:
        if instruction[0] == 'turn on':
            lights[point] = 'on'
        elif instruction[0] == 'turn off':
            lights[point] = 'off'
        elif instruction[0] == 'toggle':
            if lights[point] == 'off':
                lights[point] = 'on'
            elif lights[point] == 'on':
                lights[point] = 'off'
    return lights


def handle_brightness_instruction(instruction, lights):
    """Take in one set of instructions and perform them on
    the array of lights
    """
    points = expand_rectangle(instruction[1], instruction[2])
    for point in points:
        if instruction[0] == 'initialize':
            lights[point] = 0
        elif instruction[0] == 'turn on':
            lights[point] += 1
        elif instruction[0] == 'turn off':
            if lights[point] == 0:
                pass
            else:
                lights[point] -= 1
        elif instruction[0] == 'toggle':
            lights[point] += 2
    return lights


def p1():
    # initialize lights
    lights = {}
    instruction = ('turn off', (0, 0), (999, 999))
    lights = handle_instruction(instruction, lights)
    instructions = get_instructions()
    for instruction in instructions:
        handle_instruction(instruction, lights)
    # Fetch powered lights
    powered_lights = {bulb: 'on' for bulb in lights if lights[bulb] == 'on'}
    print len(powered_lights)


def p2():
    # initialize lights
    lights = {}
    instruction = ('initialize', (0, 0), (999, 999))
    lights = handle_brightness_instruction(instruction, lights)
    instructions = get_instructions()
    for instruction in instructions:
        handle_brightness_instruction(instruction, lights)
    print sum(lights.itervalues())

if __name__ == '__main__':
    p1()
    p2()
