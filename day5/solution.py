#python solution.py input.txt
import re
import sys

with open(sys.argv[1]) as f:
   rows = f.readlines()

instructions = [int(row.replace('\n', '')) for row in rows]
index = 0
step_count = 0

while True:
    try:
        new_index = index + instructions[index]
        instructions[index] = instructions[index] + 1
        index = new_index
        step_count = step_count + 1
    except:
        print(step_count)
        break
