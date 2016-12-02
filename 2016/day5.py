from collections import Counter
from itertools import groupby


def get_words():
    with open('day5_input.txt') as f:
        strings = f.readlines()
    return strings


def p1():
    nice_strings = 0
    strings = get_words()
    for word in strings:
        bad_strings = ['ab', 'cd', 'pq', 'xy']
        if not any([baddie in word for baddie in bad_strings]):
            c = Counter(word)
            vowels = c['a'] + c['e'] + c['i'] + c['o'] + c['u']
            if vowels >= 3:
                groups = [list(group) for letter, group in groupby(word)]
                if any([len(group) >= 2 for group in groups]):
                    nice_strings += 1
    print nice_strings


def p2():
    nice_strings = 0
    strings = get_words()
    for word in strings:
        if any([word.count(word[i:i+2]) >= 2 for i in range(len(word))]):
            for c in range(len(word)-2):
                if word[c] == word[c+2]:
                    nice_strings += 1
                    break
    print nice_strings


if __name__ == '__main__':
    p1()
    p2()
