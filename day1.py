def compute_captcha(seq):
    total = 0
    for index, digit in enumerate(list(seq)):
        try:
            if digit == seq[index+1]:
                total += int(digit)
        except IndexError:
            if digit == seq[0]:
                total += int(digit)
    return total


def compute_halfway_captcha(seq):
    total = 0
    step = int((len(list(seq)))/2)
    double_seq = list(seq)*2
    for index, digit in enumerate(list(seq)):
        if digit == double_seq[index + step]:
            total += int(digit)
    return total


def main():  # pragma: no cover
    with open('day1_input.txt') as f:
        data = f.read().strip()
        result = compute_captcha(data)
        result2 = compute_halfway_captcha(data)
        print(result)
        print(result2)


if __name__ == '__main__':  # pragma: no cover
    main()
