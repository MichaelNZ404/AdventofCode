#python solution.py input.txt
import re
import sys

with open(sys.argv[1]) as f:
   row = f.readline()

row = row.replace('\n', '')
banks = [int(i) for i in re.split('\t| ', row)]

initial_config = ','.join(str(b) for b in banks)
configs_seen = set()
configs_seen.add(initial_config)

cycle_count = 0

while True:
    max_idx = banks.index(max(banks))
    blocks_to_alloc = banks[max_idx]
    banks[max_idx] = 0
    dist_idx = max_idx + 1
    while blocks_to_alloc > 0:
        #wrap around list of banks
        if dist_idx == len(banks):
            dist_idx = 0
        banks[dist_idx] += 1
        dist_idx += 1
        blocks_to_alloc -= 1
        new_config = ','.join(str(b) for b in banks)
    cycle_count += 1
    if new_config in configs_seen:
        print(cycle_count)
        break
    else:
        configs_seen.add(new_config)
