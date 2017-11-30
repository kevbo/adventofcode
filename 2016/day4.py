import re
import string
from itertools import cycle
from collections import Counter


def get_room_names(input_file):
    with open(input_file) as f:
        rooms = f.readlines()
    return rooms


def calculate_checksum(room):
    checksum = []
    d = {}
    c = Counter(room)
    c.pop('-')
    for k, v in c.most_common():
        try:
            d[v] = d[v] + k
        except KeyError:
            d[v] = k
    counts = sorted(d, reverse=True)
    for num in counts:
        checksum = checksum + sorted(d[num])
    checksum = ''.join(checksum)
    return checksum[0:5]


def is_real(room):
    provided_checksum = get_provided_checksum(room)
    room_name = get_room_name(room)
    if get_provided_checksum(room) == calculate_checksum(room_name):
        return True
    else:
        return False


def get_provided_checksum(room):
    return re.search(r'\[(.*)\]', room).groups()[0]


def get_room_name(room):
    return re.search(r'(.*)-\d+\[.*\]', room).groups()[0]


def get_sector_id(room):
    return int(re.search(r'.*-(\d+)\[.*\]', room).groups()[0])


def unencrypt_room_name(name, sector):
    unencrypted = []
    for letter in name:
        if letter == '-':
            unencrypted.append(' ')
        else:
            idx = string.lowercase.index(letter)
            c = cycle(string.lowercase)
            for i in range(sector+idx+1):
                new_letter = c.next()
                if i == sector + idx:
                    unencrypted.append(str(new_letter))
    return ''.join(unencrypted)


if __name__ == '__main__':
    # Part 1
    all_rooms = get_room_names('day4_input.txt')
    real_rooms = [room for room in all_rooms if is_real(room)]
    total = 0
    for room in real_rooms:
        total += get_sector_id(room)
    print total
    # Part 2
    for room in real_rooms:
        room_name = get_room_name(room)
        sector_id = get_sector_id(room)
        unencrypted = unencrypt_room_name(room_name, sector_id)
        if 'north' in unencrypted:
            print unencrypted, sector_id
