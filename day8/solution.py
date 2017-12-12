#python solution.py input.txt
import re
import sys
import operator

REGISTERS = {}
OPPERATION = {
    '<': operator.lt,
    '<=': operator.le,
    '==': operator.eq,
    '!=': operator.ne,
    '>=': operator.ge,
    '>': operator.gt,
    'dec': operator.sub,
    'inc': operator.add,
}

def evaluate_opperation(left, right, opp):
    if left not in REGISTERS:
        REGISTERS[left] = 0
    return OPPERATION[opp](REGISTERS[left], right)

with open(sys.argv[1]) as f:
   rows = f.readlines()

for row in rows:
    row = row.replace('\n', '')
    opperation, condition = row.split(' if ')
    left, opp, right = condition.split(' ')
    if evaluate_opperation(left, int(right), opp):
        left, opp, right = opperation.split(' ')
        REGISTERS[left] = evaluate_opperation(left, int(right), opp)

print(f"Largest value is {max(REGISTERS.values())}")
