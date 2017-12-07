from itertools import permutations


def checksum(matrix):
    total = 0
    for row in matrix:
        total += (max(row) - min(row))
    return total


def checksum2(matrix):
    total = 0
    for row in matrix:
        pairs = permutations(row, 2)
        for pair in pairs:
            if not pair[0] == pair[1]:
                if pair[0] % pair[1] == 0:
                    total += (pair[0] / pair[1])
    return total


def create_matrix(lines):  # pragma: no cover
    matrix = []
    for row in lines:
        matrix.append([int(i) for i in row.split()])
    return matrix


def main():  # pragma: no cover
    with open('day2_input.txt') as f:
        matrix = create_matrix(f.readlines())
        print(checksum(matrix))
        print(checksum2(matrix))


if __name__ == '__main__':  # pragma: no cover
    main()
