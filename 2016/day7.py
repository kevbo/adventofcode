import re
import unittest


def get_addresses(path):
    with open(path) as f:
        return f.readlines()


def get_hypernet_sequences(address):
    results = re.findall(r'\[(.*?)\]', address)
    if not results:
        raise Exception('no hypernet sequences found in {}'.format(address))
    return results


def get_supernet_sequence(address):
    supernet = re.sub(r'(\[.*?\])', '-', address)
    return supernet


def get_abbas(address):
    doubles = []
    for i in range(len(address)-4):
        if (address[i] == address[i+3] and
                address[i+1] == address[i+2] and
                address[i] != address[i+1]):
            if not any([char in address[i:i+4] for char in '[]-']):
                doubles.append(address[i:i+4])
    return doubles


def get_abas(address):
    abas = []
    supernet = get_supernet_sequence(address)
    for i in range(len(supernet)-3):
        if supernet[i] == supernet[i+2] and supernet[i] != supernet[i+1]:
            if not any([char in supernet[i:i+3] for char in '[]-']):
                abas.append(supernet[i:i+3])
    return abas


def supports_tls(address):
    abbas = get_abbas(address)
    if not abbas:
        return False
    hypernets = get_hypernet_sequences(address)
    for abba in abbas:
        if any([abba in net for net in hypernets]):
            return False
    return True


def supports_ssl(address):
    abas = get_abas(address)
    if not abas:
        return False
    hypernets = get_hypernet_sequences(address)
    for aba in abas:
        bab = aba[1] + aba[0] + aba[1]
        if any([bab in net for net in hypernets]):
            return True
    return False


class Test_TLS(unittest.TestCase):
    def test_is_tls(self):
        self.assertTrue(supports_tls('abba[mnop]qrst'))
        self.assertTrue(supports_tls('ioxxoj[asdfgh]zxcvbn'))

    def test_is_not_tls(self):
        self.assertFalse(supports_tls('abcd[bddb]xyyx'))
        self.assertFalse(supports_tls('aaaa[qwer]tyui'))

    def test_valid_and_invalid(self):
        '''for when there's a valid letter doubling outside brackets as well
        as inside. For example: "xyyx[bddb]xyyx"'''
        self.assertFalse(supports_tls('xyyx[bddb]xyyx'))

    def test_supernet(self):
        address = 'abcd[bddb]xyyx'
        self.assertEqual('abcd-xyyx', get_supernet_sequence(address))

    def test_is_ssl(self):
        self.assertTrue(supports_ssl('aba[bab]xyz'))

    def test_is_not_ssl(self):
        self.assertFalse(supports_ssl('xyx[xyx]xyx'))


if __name__ == '__main__':
    # unittest.main()
    # Part 1
    addresses = get_addresses('day7_input.txt')
    have_tls = []
    for address in addresses:
        if supports_tls(address):
            have_tls.append(address)
    print 'There are {} addresses that support TLS'.format(len(have_tls))
    # Part 2
    addresses = get_addresses('day7_input.txt')
    have_ssl = []
    for address in addresses:
        if supports_ssl(address):
            have_ssl.append(address)
    print 'There are {} addresses that support SSL'.format(len(have_ssl))
