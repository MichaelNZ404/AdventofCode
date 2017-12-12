#python solution.py input.txt
from functools import reduce
import sys

with open(sys.argv[1]) as f:
   row = f.readline()

row = row.replace('\n', '')
string_hash = [i for i in range(0, 256)]
current_pos = 0
skip_size = 0
special_sequence = [17, 31, 73, 47, 23]
#convert to ascii
lengths = [ord(c) for c in row] + special_sequence

for i in range(64):
    for length in lengths:
        #shift list such that current_pos becomes 0
        string_hash = string_hash[current_pos:] + string_hash[:current_pos]
        end_pos = int(length)
        twist = string_hash[:end_pos]
        twist = twist[::-1]
        string_hash = twist + string_hash[end_pos:]
        #shift list back
        string_hash =  string_hash[-current_pos:] + string_hash[:-current_pos]
        current_pos = (current_pos + int(length) + skip_size) % len(string_hash)
        skip_size += 1

#split list into lists of 16 to compute dense hash
chunks = [string_hash[x:x+16] for x in range(0, 16)]
dense_hash = [x for x in map(lambda x: reduce(lambda y,z: y^z, x), chunks)]
output = ('').join(['{0:02x}'.format(x) for x in dense_hash])
print(output, len(output))
import pdb; pdb.set_trace()
