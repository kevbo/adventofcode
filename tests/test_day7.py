import unittest

from day7 import DiscStack


class TestDiscStack(unittest.TestCase):

    def setUp(self):
        self.input = """pbga (66)
        xhth (57)
        ebii (61)
        havc (66)
        ktlj (57)
        fwft (72) -> ktlj, cntj, xhth
        qoyq (66)
        padx (45) -> pbga, havc, qoyq
        tknk (41) -> ugml, padx, fwft
        jptl (61)
        ugml (68) -> gyxo, ebii, jptl
        gyxo (61)
        cntj (57)"""

    def test_discs(self):
        stack = DiscStack(self.input)
        self.assertEqual(stack.layers[0], ['tknk'])
        self.assertEqual(len(stack.layers[1]), 3)
        self.assertIn('ugml', stack.layers[1])
        self.assertIn('padx', stack.layers[1])
        self.assertIn('fwft', stack.layers[1])
