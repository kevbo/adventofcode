from itertools import permutations, islice


def get_triangles(input_file):
    with open(input_file) as f:
        triangles = f.readlines()
        triangles = [triangle.split() for triangle in triangles]
    print 'Loading {} potential triangles...'.format(len(triangles))
    return triangles


def is_triangle(triangle):
    results = []
    for p in permutations(triangle):
        if (int(p[0]) + int(p[1])) > int(p[2]):
            results.append(True)
        else:
            results.append(False)
    return all(results)


def grouper(n, iterable):
    it = iter(iterable)
    while True:
        chunk = tuple(islice(it, n))
        if not chunk:
            return
        yield chunk


if __name__ == '__main__':
    # Part 1
    triangles = get_triangles('day3_input.txt')
    counter = 0
    for triangle in triangles:
        if is_triangle(triangle):
            counter += 1
    print counter
    # Part 2
    triangles = get_triangles('day3_input.txt')
    counter = 0
    column_triangles = grouper(3, triangles)
    for group in column_triangles:
        t1 = (group[0][0], group[1][0], group[2][0])
        if is_triangle(t1):
            counter += 1
        t2 = (group[0][1], group[1][1], group[2][1])
        if is_triangle(t2):
            counter += 1
        t3 = (group[0][2], group[1][2], group[2][2])
        if is_triangle(t3):
            counter += 1
    print counter
