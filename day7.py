import re
from collections import defaultdict


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

    def disc_weight(self, disc):
        total_weight = self.get_details(disc)['weight']
        if self.get_children(disc):
            for child in self.get_children(disc):
                total_weight += self.disc_weight(child)
        return total_weight

    def find_imbalances(self, starting_disc):
        my_children = self.get_children(starting_disc)
        child_weights = [self.disc_weight(child) for child in my_children]
        if len(set(child_weights)) == 1:
            siblings = self.get_siblings(starting_disc)
            sibling_weights = [self.disc_weight(sib) for sib in siblings]
            starting_weight = self.get_details(starting_disc)['weight']
            my_full_weight = self.disc_weight(starting_disc)
            difference = abs(my_full_weight - list(set(sibling_weights))[0])
            i_should_be = abs(starting_weight - difference)
            return (starting_disc, i_should_be)
        else:
            # find the unbalanced one, and recursively find_imbalances
            kids = defaultdict(list)
            for child in my_children:
                w = self.disc_weight(child)
                kids[w].append(child)
            imbalanced_kid = [kid for _, kid in kids.items() if len(kid) == 1]
            return self.find_imbalances(imbalanced_kid[0][0])


if __name__ == '__main__':  # pragma: no cover
    with open('day7_input.txt') as f:
        raw_data = f.read()
    ds = DiscStack(raw_data)
    print('There are %s layers' % len(ds.layers))
    print('The lowest layer is:', ds.layers[0])
    imbalanced, should_be = ds.find_imbalances('uownj')
    print('%s should weigh %s!' % (imbalanced, should_be))
