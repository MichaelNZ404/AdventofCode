#python solution.py input.txt
import re
import sys
from collections import Counter
import json

with open(sys.argv[1]) as f:
   rows = f.readlines()

valid_rows = 0
for row in rows:
    row = row.replace('\n', '')
    phrases = [i for i in re.split('\t| ', row)]
    phrase_set = set([str(sorted(Counter(i).items())) for i in phrases])
    if len(phrases) is len(phrase_set):
        valid_rows = valid_rows + 1
print(valid_rows)
