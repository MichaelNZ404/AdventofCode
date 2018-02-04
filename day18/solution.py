#python solution.py input.txt
import sys

with open(sys.argv[1]) as f:
    rows = [row.replace('\n', '') for row in f.readlines()]

registers = {}
last_played_frequency = 0
i=0
while i < len(rows):
    print(rows[i])
    split = rows[i].split()
    opperation, command = split[0], split[1:]

    if len(command) > 1:
        try:
            command[1] = int(command[1])
        except:
            if command[1] in registers:
                command[1] = registers[command[1]]
            else:
                command[1] = 0

    if opperation == 'snd':
        last_played_frequency = registers[command[0]]

    elif opperation == 'set':
        registers[command[0]] = command[1]

    elif opperation == 'add':
        if command[0] not in registers:
            registers[command[0]] = command[1]
        else:
            registers[command[0]] += command[1]

    elif opperation == 'mul':
        if command[0] in registers:
            registers[command[0]] *= command[1]

    elif opperation == 'mod':
        if command[0] in registers:
            registers[command[0]] %= command[1]

    elif opperation == 'rcv':
        if command[0] in registers and registers[command[0]] > 0:
            print(f"First frequency is: {last_played_frequency}")
            break

    elif opperation == 'jgz':
        if command[0] in registers and registers[command[0]] > 0:
            i += command[1]
            continue
    else:
        raise Exception("Unknown Command")
    i += 1
