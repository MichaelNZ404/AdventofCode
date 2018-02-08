#python solution.py input.txt
import sys

with open(sys.argv[1]) as f:
    rows = [row.replace('\n', '') for row in f.readlines()]

registers = {
    'a': 0,
    'b': 0,
    'c': 0,
    'd': 0,
    'e': 0,
    'f': 0,
    'g': 0,
    'h': 0
}

pointer = 0
mul_count = 0
while pointer < len(rows):
    split = rows[pointer].split(' ')
    command, values = split[0], split[1:]

    if command == 'set':
        registers[values[0]] = int(registers.get(values[1], values[1]))
    elif command == 'sub':
        registers[values[0]] = registers.get(values[0], 0) - int(registers.get(values[1],values[1]))
    elif command == 'mul':
        mul_count += 1
        registers[values[0]] = registers.get(values[0], 0) * int(registers.get(values[1], values[1]))
    elif command == 'jnz':
        if registers.get(values[0], values[0]) != 0:
            pointer += int(values[1])
            continue
    pointer += 1

print(f"mul called {mul_count} times")
