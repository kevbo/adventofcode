
def get_final_floor():
    with open('day1_input.txt') as f:
        data = f.read()

    current_floor = 0
    for char in data:
        if char in ['(', ')']:  # stupid newlines broke my ternary
            current_floor = current_floor + 1 if char == '(' else current_floor - 1
    print current_floor


def get_first_negative_instruction():
    with open('day1_input.txt') as f:
        data = f.read()

    current_floor = 0
    for pos, char in enumerate(data, start=1):
        if char == '(':
            current_floor += 1
        elif char == ')':
            current_floor -= 1
        if current_floor < 0:
            print "I went negative at position %s" % pos
            break


if __name__ == '__main__':
    get_final_floor()
    get_first_negative_instruction()
