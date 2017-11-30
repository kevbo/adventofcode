
def get_directions():
    with open('day3_input.txt') as f:
        data = f.read()
    return data


def log_visit(houses, visited_house):
    try:
        houses[tuple(visited_house)] += 1
    except KeyError:  # First visit to this house
        houses[tuple(visited_house)] = 1
    return houses


def p1():
    houses = {}  # coords: visits
    houses[(0, 0)] = 1  # The first house gets visited
    directions = get_directions()
    coordinates = [0, 0]
    for direction in directions:
        if direction in ['^', '>', 'v', '<']:  # sanitize
            if direction == '^':
                coordinates[1] += 1
                log_visit(houses, tuple(coordinates))
            elif direction == '>':
                coordinates[0] += 1
                log_visit(houses, tuple(coordinates))
            elif direction == 'v':
                coordinates[1] -= 1
                log_visit(houses, tuple(coordinates))
            elif direction == '<':
                coordinates[0] -= 1
                log_visit(houses, tuple(coordinates))
    print len(houses)


def p2():
    houses = {}  # coords: visits
    houses[(0, 0)] = 2  # The first house gets visited (twice)
    directions = get_directions()
    santa_coordinates = [0, 0]
    robosanta_coordinates = [0, 0]
    for num, direction in enumerate(directions, start=1):
        if num % 2 == 0:
            coordinates = robosanta_coordinates
        else:
            coordinates = santa_coordinates
        if direction in ['^', '>', 'v', '<']:  # sanitize
            if direction == '^':
                coordinates[1] += 1
                log_visit(houses, tuple(coordinates))
            elif direction == '>':
                coordinates[0] += 1
                log_visit(houses, tuple(coordinates))
            elif direction == 'v':
                coordinates[1] -= 1
                log_visit(houses, tuple(coordinates))
            elif direction == '<':
                coordinates[0] -= 1
                log_visit(houses, tuple(coordinates))
    print len(houses)


if __name__ == '__main__':
    p1()
    p2()
