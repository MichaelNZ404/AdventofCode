#python solution.py input.txt
import sys

with open(sys.argv[1]) as f:
   rows = f.readlines()

rows = [row.replace('\n', '') for row in rows]
layers = {}

for row in rows:
    scan_depth, scan_range = row.split(': ')
    layers[int(scan_depth)] = int(scan_range)

depth = max(layers.keys())
picosecond_timer = 0
severity = 0

for position in range(depth+1):
    if position in layers:
        scanner_pos = picosecond_timer % ((layers[position]-1)*2)
        if scanner_pos == 0:
            #we are caught! =(
            severity += (layers[position] * position)
            print(f"Caught at: {position}...({position}*{layers[position]})")
    picosecond_timer += 1

print(f"Total trip severity: {severity}")
