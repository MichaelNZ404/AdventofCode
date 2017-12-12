#python solution.py input.txt
import re
import sys

with open(sys.argv[1]) as f:
   rows = f.readlines()

valid_rows = 0
for row in rows:
    row = row.replace('\n', '')
    phrases = [i for i in re.split('\t| ', row)]
    phrase_set = set(phrases)
    if len(phrases) is len(phrase_set):
        valid_rows = valid_rows + 1
print(valid_rows)
