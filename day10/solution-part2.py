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

dense = []
for x in range(0,16):
    subslice = string_hash[16*x:16*x+16]
    dense.append('%02x'%reduce((lambda x,y: x ^ y),subslice))
print(''.join(dense))
