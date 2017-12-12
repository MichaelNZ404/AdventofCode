#python solution.py input.txt
import re
import sys

with open(sys.argv[1]) as f:
   rows = f.readlines()
xsum = 0
for row in rows:
    row = row.replace('\n', '')
    nums = [int(i) for i in re.split('\t| ', row)]
    xsum = xsum + (max(nums) - min(nums))
print(xsum)
