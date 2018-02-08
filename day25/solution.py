#python solution.py input.txt
import sys
import re

with open(sys.argv[1]) as f:
    rows = [row.replace('\n', '') for row in f.readlines()]

current_state = re.match(r'Begin in state (.)', rows.pop(0)).group(1)
diagnostic_count = int(re.match(r'Perform a diagnostic checksum after (\d+) steps.', rows.pop(0)).group(1))
state_machine = {}
tape = set()
cursor = 0

rows.pop(0)
while rows:
    state = re.match(r'In state (.):', rows.pop(0)).group(1)
    rows.pop(0)
    zero_value = re.match(r'- Write the value (.)', rows.pop(0).lstrip()).group(1)
    zero_direction = re.match(r'- Move one slot to the (\w+)', rows.pop(0).lstrip()).group(1)
    zero_continue = re.match(r'- Continue with state (\w)', rows.pop(0).lstrip()).group(1)
    rows.pop(0)
    one_value = re.match(r'- Write the value (.)', rows.pop(0).lstrip()).group(1)
    one_direction = re.match(r'- Move one slot to the (\w+)', rows.pop(0).lstrip()).group(1)
    one_continue = re.match(r'- Continue with state (\w)', rows.pop(0).lstrip()).group(1)
    if rows:
        rows.pop(0)

    state_machine[state] = {
        0: {
            'value': int(zero_value),
            'direction': zero_direction,
            'continue': zero_continue
        },
        1: {
            'value': int(one_value),
            'direction': one_direction,
            'continue': one_continue
        }
    }

for i in range(diagnostic_count):
    if cursor in tape: #tape is 1
        if state_machine[current_state][1]['value'] == 0:
            tape.remove(cursor)
        if state_machine[current_state][1]['direction'] == 'left':
            cursor -= 1
        else:
            cursor += 1
        current_state = state_machine[current_state][1]['continue']

    else: #tape is zero
        if state_machine[current_state][0]['value'] == 1:
            tape.add(cursor)
        if state_machine[current_state][0]['direction'] == 'left':
            cursor -= 1
        else:
            cursor += 1
        current_state = state_machine[current_state][0]['continue']

print(len(tape))
