import unittest
from collections import Counter
from itertools import combinations


def is_valid(passphrase):
    return len(passphrase.split()) == len(set(passphrase.split()))


def is_valid2(passphrase):
    combos = combinations(passphrase.split(), 2)
    for combo in combos:
        if Counter(combo[0]) == Counter(combo[1]):
            return False
    return True


class TestValidator(unittest.TestCase):
    def test_valid(self):
        self.assertTrue(is_valid('aa bb cc dd ee'))
        self.assertTrue(is_valid('aa bb cc dd aaa'))

    def test_invalid(self):
        self.assertFalse(is_valid('aa bb cc dd aa'))

    def test_valid2(self):
        self.assertTrue(is_valid2('abcde fghij'))
        self.assertTrue(is_valid2('a ab abc abd abf abj'))
        self.assertTrue(is_valid2('iiii oiii ooii oooi oooo'))

    def test_invalid2(self):
        self.assertFalse(is_valid2('abcde xyz ecdab'))
        self.assertFalse(is_valid2('oiii ioii iioi iiio'))


def main():
    with open('day4_input.txt') as f:
        phrases = f.readlines()
    valids = [p for p in phrases if is_valid(p)]
    print(len(valids))
    valid2s = [p for p in phrases if is_valid2(p)]
    print(len(valid2s))


if __name__ == '__main__':
    # unittest.main()
    main()
