#python solution.py input.txt
import sys

with open(sys.argv[1]) as f:
   row = f.readline()

row = row.replace('\n', '')

lengths = row.split(',')
string_hash = [i for i in range(0, 256)]
current_pos = 0
skip_size = 0

for length in lengths:
    #shift list such that current_pos becomes 0
    string_hash = string_hash[current_pos:] + string_hash[:current_pos]
    end_pos = int(length)
    twist = string_hash[:end_pos]
    twist = twist[::-1]
    #print(f"reversed to sequence {twist}")
    string_hash = twist + string_hash[end_pos:]
    #shift list back
    string_hash =  string_hash[-current_pos:] + string_hash[:-current_pos]

    current_pos = (current_pos + int(length) + skip_size) % len(string_hash)
    skip_size += 1
    print(string_hash, current_pos, skip_size)

ans = string_hash[0] * string_hash[1]
print(f"the multiple of the first two numbers is {ans}")
