import re


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


if __name__ == '__main__':  # pragma: no cover
    with open('day7_input.txt') as f:
        raw_data = f.read()
    d = DiscStack(raw_data)
    print(d.layers[0])
