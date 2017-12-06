import unittest

from day4 import is_valid, is_valid2


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
