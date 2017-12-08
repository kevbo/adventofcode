import re
from collections import defaultdict


class RegisterProcessor(object):

    def __init__(self, instructions):
        self.registers = defaultdict(int)
        self.instructions = self.parse_instructions(instructions)
        self.current_highest = 0
        for i in self.instructions:
            self.handle_instruction(i)

    def parse_instructions(self, instructions):
        out = []
        instructions = instructions.strip().split('\n')
        instructions = [i.strip() for i in instructions]
        for line in instructions:
            rgx = re.compile('^(\w+) (inc|dec) (-?\d+) if (\w+) (.*) (-?\d+)$')
            matches = rgx.search(line)
            out.append(matches.groups())
        return out

    def handle_instruction(self, instruction):
        target = instruction[0]
        operation = instruction[1]
        num = instruction[2]
        eval_target = instruction[3]
        eval_comparator = instruction[4]
        eval_against = instruction[5]
        if eval('self.registers["%s"] %s %s' % (eval_target,
                                                eval_comparator,
                                                eval_against)):
            if operation == 'inc':
                self.registers[target] += int(num)
            elif operation == 'dec':
                self.registers[target] -= int(num)
        if self.registers[target] > self.current_highest:
            self.current_highest = self.registers[target]

    @property
    def highest_value(self):
        max_int = [{k: v} for k, v in self.registers.items()
                   if v == max(self.registers.values())]
        return max_int[0]


if __name__ == '__main__':  # pragma: no cover
    with open('day8_input.txt') as f:
        data = f.read()
    rp = RegisterProcessor(data)
    print('Highest value found in any register:', rp.highest_value)
    print('Highest value ever reached during processing:', rp.current_highest)
