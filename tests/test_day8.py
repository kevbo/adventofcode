import unittest

from day8 import RegisterProcessor


class TestRegisterProcessor(unittest.TestCase):

    def setUp(self):
        self.input = """b inc 5 if a > 1
        a inc 1 if b < 5
        c dec -10 if a >= 1
        c inc -20 if c == 10"""
        self.rp = RegisterProcessor(self.input)

    def test_final_values(self):
        self.assertEqual(self.rp.registers['a'], 1)
        self.assertEqual(self.rp.registers['b'], 0)
        self.assertEqual(self.rp.registers['c'], -10)

    def test_highest_value(self):
        self.assertEqual(self.rp.highest_value, {'a': 1})

    def test_current_highest_value(self):
        self.assertEqual(self.rp.current_highest, 10)
