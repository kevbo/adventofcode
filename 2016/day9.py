import re
import unittest


def decompress_v1(compressed_data):
    buffer = []
    while True:
        markers = re.search(r'(\(\d+x\d+\))', compressed_data)
        if not markers:
            if buffer:
                output = ''.join(buffer) + compressed_data
                return (output, len(output))
            else:
                return (compressed_data, len(compressed_data))
        print 'Processing marker:', markers.groups()[0]
        chars, times = markers.groups()[0].strip('()').split('x')
        chars, times = int(chars), int(times)
        to_buffer = compressed_data[:markers.end() + chars]
        compressed_data = compressed_data[markers.end() + chars:]
        to_replace = to_buffer[markers.start():markers.end() + chars]
        to_buffer = re.sub(re.escape(to_replace), to_buffer[markers.end():] * times, to_buffer)
        buffer.append(to_buffer)


class TestDecompressV1(unittest.TestCase):
    def test_no_change(self):
        uncompressed = decompress_v1('ADVENT')
        self.assertEqual(uncompressed[0], 'ADVENT')
        self.assertEqual(uncompressed[1], 6)

    def test_single_expansion(self):
        uncompressed = decompress_v1('A(1x5)BC')
        self.assertEqual(uncompressed[0], 'ABBBBBC')
        self.assertEqual(uncompressed[1], 7)

    def test_3_x_3(self):
        uncompressed = decompress_v1('(3x3)XYZ')
        self.assertEqual(uncompressed[0], 'XYZXYZXYZ')
        self.assertEqual(uncompressed[1], 9)

    def test_2_expands(self):
        uncompressed = decompress_v1('A(2x2)BCD(2x2)EFG')
        self.assertEqual(uncompressed[0], 'ABCBCDEFEFG')
        self.assertEqual(uncompressed[1], 11)

    def test_marker_in_data(self):
        uncompressed = decompress_v1('(6x1)(1x3)A')
        self.assertEqual(uncompressed[0], '(1x3)A')
        self.assertEqual(uncompressed[1], 6)

    def test_marker_in_data_2(self):
        uncompressed = decompress_v1('X(8x2)(3x3)ABCY')
        self.assertEqual(uncompressed[0], 'X(3x3)ABC(3x3)ABCY')
        self.assertEqual(uncompressed[1], 18)


'''
(3x3)XYZ still becomes XYZXYZXYZ, as the decompressed section contains no markers.
X(8x2)(3x3)ABCY becomes XABCABCABCABCABCABCY, because the decompressed data from the (8x2) marker is then further decompressed, thus triggering the (3x3) marker twice for a total of six ABC sequences.
(27x12)(20x12)(13x14)(7x10)(1x12)A decompresses into a string of A repeated 241920 times.
(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN becomes 445 characters long.
Unfortunately, the computer you brought probably doesn't have enough memory to actually decompress the file; you'll have to come up with another way to get its decompressed length.

X(8x2)(3x3)ABCY becomes XABCABCABCABCABCABCY

register = 0
data = 'X(8x2)(3x3)ABCY'

drop the X and add 1 to the register:

register = 1
data = '(8x2)(3x3)ABCY'

expand the first match and drop that from the data:

register = 1
data = '(3x3)ABC(3x3)ABCY'

nothing to drop, so register stays the same and we expand again:

register = 1
data = 'ABCABCABC(3x3)ABCY'

drop the leading data

register = 10
data = '(3x3)ABCY'

expand, register stays the same

register = 10
data = 'ABCABCABCY'

drop the leading (all) data:

register = 20
data = ''
'''


def decompress_v2(compressed_data):
    register = 0
    for character in compressed_data:
        if character != '(':
            register += 1
        else:
            marker = re.match(r'(\(\d+x\d+\))', compressed_data[register:])
            if marker:
                chars, times = marker.group().strip('()').split('x')


            






class TestDecompressV2(unittest.TestCase):
    def test_single_expansion(self):
        length = decompress_v2('(3x3)XYZ')
        self.assertEqual(length, 9)

    def test_double_expansion(self):
        length = decompress_v2('X(8x2)(3x3)ABCY')
        self.assertEqual(length, 20)






if __name__ == '__main__':
    unittest.main()
    with open('day9_input.txt') as f:
        compressed_data = f.read().strip()
    print len(compressed_data)
    uncompressed, length = decompress_v1(compressed_data)
    print length
    # print uncompressed
