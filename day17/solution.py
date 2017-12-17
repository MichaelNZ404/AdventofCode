#python solution.py input.txt
import sys

with open(sys.argv[1]) as f:
   row = f.readline().replace('\n', '')

step_size = int(row)
spinlist = [0]

pos = 0
for i in range(1,2018):
    pos = (pos+step_size)%len(spinlist) + 1
    spinlist.insert(pos, i)

print(spinlist[pos+1])
