#python solution.py input.txt
import re
import sys

with open(sys.argv[1]) as f:
   row = f.readline()

row = row.replace('\n', '')
CURRENT_LEVEL = 0
GARBAGE_MODE = False
ESCAPE_MODE = False
SCORE = 0
GARBAGE_COUNT = 0

for token in row:
    if ESCAPE_MODE:
        ESCAPE_MODE = False
        continue
    if token == '!':
        ESCAPE_MODE = True
        continue
    if GARBAGE_MODE:
        if token == '>':
            GARBAGE_MODE = False
            continue
        else:
            GARBAGE_COUNT += 1
            continue
    if token == '<':
        GARBAGE_MODE = True
        continue
    if token == '{':
        CURRENT_LEVEL += 1
        continue
    if token == '}':
        SCORE += CURRENT_LEVEL
        print(f"{CURRENT_LEVEL} added to score")
        CURRENT_LEVEL -= 1
        continue

print(f"Final score is {SCORE}")
print(f"Garbage collected: {GARBAGE_COUNT}")
