#python solution.py input.txt
import re
import sys

with open(sys.argv[1]) as f:
   rows = f.readlines()
xsum = 0
for row in rows:
    row = row.replace('\n', '')
    nums = [int(i) for i in re.split('\t| ', row)]
    nums.sort(reverse=True)
    for idx, num in enumerate(nums):
        matches = [int(num/x) for x in nums[idx+1:] if num % x == 0]
        if len(matches) > 0:
            xsum = xsum + matches[0]
            break
print(xsum)
