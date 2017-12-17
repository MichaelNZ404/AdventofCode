#python solution.py input.txt
import sys

with open(sys.argv[1]) as f:
   row = f.readline().replace('\n', '')

step_size = int(row)
spinlist = [0]

pos = 0
for i in range(1,50000001):
    pos = (pos+step_size)%i + 1
    if pos==1:
     answer = i

print(answer)
