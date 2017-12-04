import unittest


def checksum(matrix):
    total = 0
    for row in matrix:
        total += (max(row) - min(row))
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


class TestChecksum(unittest.TestCase):
    def test_checksum(self):
        test_data = [
                [5, 1, 9, 5],
                [7, 5, 3],
                [2, 4, 6, 8]]
        self.assertEqual(checksum(test_data), 18)


if __name__ == '__main__':
    # unittest.main()
    main()
