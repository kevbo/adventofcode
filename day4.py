import unittest


def is_valid(passphrase):
    return len(passphrase.split()) == len(set(passphrase.split()))


class TestValidator(unittest.TestCase):
    def test_valid(self):
        self.assertTrue(is_valid('aa bb cc dd ee'))
        self.assertTrue(is_valid('aa bb cc dd aaa'))

    def test_invalid(self):
        self.assertFalse(is_valid('aa bb cc dd aa'))


def main():
    with open('day4_input.txt') as f:
        phrases = f.readlines()
    valids = [p for p in phrases if is_valid(p)]
    print(len(valids))


if __name__ == '__main__':
    # unittest.main()
    main()
