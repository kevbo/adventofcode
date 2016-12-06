from collections import Counter

with open('day6_input.txt') as f:
    data = f.readlines()

word = []

for i in range(len(data[0])):
    col = [row[i] for row in data]
    c = Counter(col)
    let = c.most_common(1)[0][0]
    word.append(let)
print ''.join(word)


word = []

for i in range(len(data[0])):
    col = [row[i] for row in data]
    c = Counter(col)
    letters = c.most_common()
    reversi = [(letter[1], letter[0]) for letter in letters]
    word.append(sorted(reversi)[0][1])
print ''.join(word)
