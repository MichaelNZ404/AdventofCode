#python solution.py input.txt
#TODO: optimize this solution to speed up runtime?
import sys

with open(sys.argv[1]) as f:
   rows = f.readlines()

rows = [row.replace('\n', '') for row in rows]
layers = {}

for row in rows:
    scan_depth, scan_range = row.split(': ')
    layers[int(scan_depth)] = int(scan_range)

depth = max(layers.keys())

passed = False
delay = 0

while passed == False:
    picosecond_timer = delay
    passed = True
    for position in range(depth+1):
        if position in layers:
            scanner_pos = picosecond_timer % ((layers[position]-1)*2)
            if scanner_pos == 0:
                delay += 1
                passed = False
                print(f"Caught at: {position}...({position}*{layers[position]})")
                break
        picosecond_timer += 1

print(f"passed at: {delay} delay")
