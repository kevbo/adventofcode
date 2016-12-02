import md5


def p1():
    secret_key = 'iwrupvqb'
    number = 1
    while True:
        if md5.new(secret_key + str(number)).hexdigest().startswith('00000'):
            print 'Got 5 zeroes at %s' % number
            break
        else:
            number += 1


def p2():
    secret_key = 'iwrupvqb'
    number = 1
    while True:
        if md5.new(secret_key + str(number)).hexdigest().startswith('000000'):
            print 'Got 6 zeroes at %s' % number
            break
        else:
            number += 1


if __name__ == '__main__':
    p1()
    p2()
