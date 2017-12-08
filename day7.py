import re
from collections import defaultdict


class Tree(object):
    def __init__(self):
        self.tree = {}
        self.directory = {}

    def add_child(self, name, weight, parent=None):
        if not parent:
            # root case
            self.tree[name] = {'weight': weight}
            self.directory[name] = self.tree[name]
            return self.tree[name]
        else:
            parent = self.directory[parent]
            parent[name] = {'weight': weight}
            self.directory[name] = parent[name]
            return parent[name]


class DiscStack(object):

    def __init__(self, raw_data):
        self.raw_data = raw_data
        self.discs = self._parse_discs()

    def _parse_discs(self):
        discs = []
        raw_list = [i.strip() for i in self.raw_data.split('\n')]
        for disc in raw_list:
            if disc:
                matches = re.search(r'^(\w+) \((\d+)\)', disc)
                discs.append({'name': matches.group(1),
                              'weight': int(matches.group(2))})
        for disc in raw_list:
            if '->' in disc:
                matches = re.search('(\w+).*->(.*)', disc)
                p = matches.group(1)
                c = [d.strip() for d in matches.group(2).split(',')]
                [d for d in discs if d['name'] == p][0]['children'] = c
                for child in c:
                    [d for d in discs if d['name'] == child][0]['parent'] = p
        return discs

    def get_details(self, disc_name):
        return [d for d in self.discs if d['name'] == disc_name][0]

    def get_parent(self, disc_name):
        return self.get_details(disc_name).get('parent')

    def get_children(self, disc_name):
        return [d['name'] for d in self.discs if d.get('parent') == disc_name]

    def get_siblings(self, disc_name):
        parent = self.get_parent(disc_name)
        if not parent:
            return []
        siblings = [d['name'] for d in self.discs if d.get('parent') == parent]
        siblings.remove(disc_name)
        return(siblings)

    @property
    def layers(self):
        layers = []
        next_layer = set([d['name'] for d in self.discs
                         if 'children' not in d])
        layers.append(next_layer)
        while True:
            # keep digging for parents until none are found
            next_layer = [d.get('parent') for d in self.discs
                          if d['name'] in next_layer]
            next_layer = [d for d in next_layer if d is not None]
            if next_layer:
                layers.append(set(next_layer))
            else:
                break
        return [list(l) for l in reversed(layers)]

    @property
    def tree(self):
        t = Tree()
        for layer in self.layers:
            for disc in layer:
                weight = self.get_details(disc)['weight']
                t.add_child(disc, weight, self.get_parent(disc))
        return t.tree

    def disc_weight(self, disc):
        total_weight = self.get_details(disc)['weight']
        if self.get_children(disc):
            for child in self.get_children(disc):
                total_weight += self.disc_weight(child)
        return total_weight

        # top layer weights
        # next layer down, including layer before
        # weights_by_layer = defaultdict(dict)
        # top_layer = [self.get_details(d)['weight'] for d in list(reversed(self.layers))[0]]
        # print('top layer', top_layer)
        # for i, layer in enumerate(reversed(self.layers)):
            # for disc in layer:
                # pass
            # print(layer)
        # parent_weight = self.get_details(disc)['weight']
        # child_weights = []
        # if self.get_children(disc):
            # for child in self.get_children(disc):
                # child_weights.append(self.disc_weight(child))
        # print('Parent (%s) weight: %s. Children (%s) weights: %s' % (disc, parent_weight, self.get_children(disc), child_weights)) 
        # return parent_weight, child_weights
        # # get the total weights of all the second layer items
        # # whichever one doesn't match, move up that tree

    def stack_weight(self):
        layer_sizes = []
        for layer in self.layers:
            sizes = {}
            for disc in layer:
                sizes[disc] = self.disc_weight(disc)
            layer_sizes.append(sizes)
        return layer_sizes
        # this can be the originator
        # do the top level here?
        # I'm the root. Give me just my children.
        # Then I'll look at their children
        # and recursively look deeper. always returning just kids and their weights.
        # I'll need to kick off the next iteration

    def find_imbalances(self, starting_disc):
        my_children = self.get_children(starting_disc)
        child_weights = [self.disc_weight(child) for child in my_children]
        if len(set(child_weights)) == 1:
            print('My children are balanced. I am the problem: %s' % starting_disc)
            siblings = self.get_siblings(starting_disc)
            sibling_weights = [self.disc_weight(sib) for sib in siblings]
            print('The total weights of my siblings are:', sibling_weights)
            print('But my total weight is:', self.disc_weight(starting_disc))
            starting_weight = self.get_details(starting_disc)['weight']
            my_full_weight = self.disc_weight(starting_disc)
            print('My starting weight was:', starting_weight)
            difference = abs(my_full_weight - list(set(sibling_weights))[0])
            i_should_be = abs(starting_weight - difference)
            print(difference)
            print('%s should weigh %s!' % (starting_disc, i_should_be))
            return (starting_disc, i_should_be)
        else:
            print('My children are unbalanced; digging deeper')
            # find the unbalanced one, and recursively find_imbalances
            kids = defaultdict(list)
            for child in my_children:
                w = self.disc_weight(child)
                kids[w].append(child)
            imbalanced_kid = [kid for w,kid in kids.items() if len(kid) == 1]
            print('%s is unbalanced. Asking it to balance' % imbalanced_kid)
            return self.find_imbalances(imbalanced_kid[0][0])

        # print(child_weights)
        # layer = self.stack_weight()[1]
        # for disc, weight in layer.items():
            # print(disc, weight)
        # node to start with
        # are my children balanced?
        # if a child isn't, look recursively through its children to find one that doesn't balance
        # if the children are all balanced, it's actually the parent that needs to change




if __name__ == '__main__':  # pragma: no cover
    with open('day7_input.txt') as f:
        raw_data = f.read()
    ds = DiscStack(raw_data)
    print('There are %s layers' % len(ds.layers))
    print('The lowest layer is:', ds.layers[0])
    imbalanced, its_weight, sibling_weights, starting_weight = ds.find_imbalances('uownj')
