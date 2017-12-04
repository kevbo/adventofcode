import unittest
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


def create_matrix(lines):
    matrix = []
    for row in lines:
        matrix.append([int(i) for i in row.split()])
    return matrix


def main():
    with open('day2_input.txt') as f:
        matrix = create_matrix(f.readlines())
        print(checksum(matrix))
        print(checksum2(matrix))


class TestChecksum(unittest.TestCase):
    def test_checksum(self):
        test_data = [
                [5, 1, 9, 5],
                [7, 5, 3],
                [2, 4, 6, 8]]
        self.assertEqual(checksum(test_data), 18)

    def test_checksum2(self):
        test_data = [
                [5, 9, 2, 8],
                [9, 4, 7, 3],
                [3, 8, 6, 5]]
        self.assertEqual(checksum2(test_data), 9)


if __name__ == '__main__':
    # unittest.main()
    main()
