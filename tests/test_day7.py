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
        self.stack = DiscStack(self.input)

    def test_weights(self):
        self.assertTrue(all([d.get('weight') for d in self.stack.discs]))

    def test_layers(self):
        self.assertEqual(len(self.stack.layers[1]), 3)
        self.assertEqual(self.stack.layers[0], ['tknk'])
        self.assertIn('ugml', self.stack.layers[1])
        self.assertIn('padx', self.stack.layers[1])
        self.assertIn('fwft', self.stack.layers[1])

    def test_get_details(self):
        padx = {'name': 'padx',
                'weight': 45,
                'children': ['pbga', 'havc', 'qoyq'],
                'parent': 'tknk'}
        self.assertEqual(self.stack.get_details('padx'), padx)

    def test_get_children(self):
        self.assertEqual(len(self.stack.get_children('tknk')), 3)
        self.assertIn('ugml', self.stack.get_children('tknk'))
        self.assertIn('padx', self.stack.get_children('tknk'))
        self.assertIn('fwft', self.stack.get_children('tknk'))


    def test_get_parent(self):
        self.assertEqual(self.stack.get_parent('ugml'), 'tknk')
        self.assertEqual(self.stack.get_parent('gyxo'), 'ugml')

    def test_get_siblings(self):
        self.assertEqual(self.stack.get_siblings('tknk'), [])
        self.assertEqual(self.stack.get_siblings('xhth'), ['ktlj', 'cntj'])

    def test_disc_weight(self):
        self.assertEqual(self.stack.disc_weight('tknk'), 778)
        self.assertEqual(self.stack.disc_weight('xhth'), 57)
        self.assertEqual(self.stack.disc_weight('padx'), 243)

    def test_stack_weight(self):
        # print(self.stack.stack_weight())
        pass

    def test_find_imbalances(self):
        imbalanced, should_be = self.stack.find_imbalances('tknk')
        self.assertEqual(imbalanced, 'ugml')
        self.assertEqual(should_be, 60)

    # def test_tree(self):
        # print(self.stack.tree)
