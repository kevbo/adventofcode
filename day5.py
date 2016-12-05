import hashlib


def part1(code):
    output = []
    idx = 0
    while True:
        h = hashlib.md5(code + str(idx))
        if h.hexdigest().startswith('00000'):
            output.append(h.hexdigest()[5])
            print ''.join(output)
            idx += 1
        else:
            idx += 1
        if len(output) == 8:
            break


def part2(code):
    output = ['!', '!', '!', '!', '!', '!', '!', '!']
    idx = 0
    while '!' in output:
        h = hashlib.md5(code + str(idx))
        if h.hexdigest().startswith('00000'):
            if h.hexdigest()[5].isdigit():
                if int(h.hexdigest()[5]) <= 7:
                    if output[int(h.hexdigest()[5])] == '!':
                        output[int(h.hexdigest()[5])] = h.hexdigest()[6]
                        print ''.join(output)
        idx += 1


if __name__ == '__main__':
    print 'Attempting door 1...'
    part1('cxdnnyjw')
    print 'Attempting door 2...'
    part2('cxdnnyjw')
