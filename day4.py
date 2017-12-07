from collections import Counter
from itertools import combinations


def is_valid(passphrase):
    return len(passphrase.split()) == len(set(passphrase.split()))


def is_valid2(passphrase):
    combos = combinations(passphrase.split(), 2)
    for combo in combos:
        if Counter(combo[0]) == Counter(combo[1]):
            return False
    return True


def main():  # pragma: no cover
    with open('day4_input.txt') as f:
        phrases = f.readlines()
    valids = [p for p in phrases if is_valid(p)]
    print(len(valids))
    valid2s = [p for p in phrases if is_valid2(p)]
    print(len(valid2s))


if __name__ == '__main__':  # pragma: no cover
    main()
