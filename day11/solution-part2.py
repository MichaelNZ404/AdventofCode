#python solution.py input.txt
import sys
from collections import Counter

def copy_counter(counter):
    copy = Counter([x for x in counter.elements()])
    for key in ['n', 'ne', 'nw', 's', 'se', 'sw']:
        if key not in copy:
            copy[key] = 0
    return copy

def calc_distance(counter, max_dist):
    old_counter = None
    while old_counter != counter:
        count_order = [x[0] for x in counter.most_common()[::-1]]
        old_counter = copy_counter(counter)

        for direction in count_order:
            step_num = counter[direction]
            if direction == 'nw':
                if counter['se'] >= step_num:
                    counter['se'] -= counter[direction]
                    counter[direction] = 0
                elif counter['ne'] >= step_num:
                    counter['ne'] -= counter[direction]
                    counter['n'] += counter[direction]
                    counter[direction] = 0
                elif counter['s'] >= step_num:
                    counter['s'] -= counter[direction]
                    counter['sw'] += counter[direction]
                    counter[direction] = 0


            if direction == 'ne':
                if counter['sw'] >= step_num:
                    counter['sw'] -= counter[direction]
                    counter[direction] = 0
                elif counter['nw'] >= step_num:
                    counter['nw'] -= counter[direction]
                    counter['n'] += counter[direction]
                    counter[direction] = 0
                elif counter['s'] >= step_num:
                    counter['s'] -= counter[direction]
                    counter['se'] += counter[direction]
                    counter[direction] = 0


            if direction == 'sw':
                if counter['ne'] >= step_num:
                    counter['ne'] -= counter[direction]
                    counter[direction] = 0
                elif counter['se'] >= step_num:
                    counter['se'] -= counter[direction]
                    counter['s'] += counter[direction]
                    counter[direction] = 0
                elif counter['n'] >= step_num:
                    counter['n'] -= counter[direction]
                    counter['nw'] += counter[direction]
                    counter[direction] = 0


            if direction == 'se':
                if counter['nw'] >= step_num:
                    counter['nw'] -= counter[direction]
                    counter[direction] = 0
                elif counter['sw'] >= step_num:
                    counter['sw'] -= counter[direction]
                    counter['s'] += counter[direction]
                    counter[direction] = 0
                elif counter['n'] >= step_num:
                    counter['n'] -= counter[direction]
                    counter['ne'] += counter[direction]
                    counter[direction] = 0


            if direction == 's':
                if counter['n'] >= step_num:
                    counter['n'] -= counter[direction]
                    counter[direction] = 0
                if counter['nw'] >= step_num:
                    counter['nw'] -= counter[direction]
                    counter['sw'] += counter[direction]
                    counter[direction] = 0
                if counter['ne'] >= step_num:
                    counter['ne'] -= counter[direction]
                    counter['se'] += counter[direction]
                    counter[direction] = 0

            if direction == 'n':
                if counter['s'] >= step_num:
                    counter['s'] -= counter[direction]
                    counter[direction] = 0
                if counter['sw'] >= step_num:
                    counter['sw'] -= counter[direction]
                    counter['nw'] += counter[direction]
                    counter[direction] = 0
                if counter['se'] >= step_num:
                    counter['se'] -= counter[direction]
                    counter['ne'] += counter[direction]
                    counter[direction] = 0

    total = 0
    for key in counter.keys():
        total += counter[key]
    if max_dist < total:
        max_dist = total
    return max_dist

with open(sys.argv[1]) as f:
   row = f.readline()

row = row.replace('\n', '')
steps = row.split(',')

max_dist = 0
for i in range(len(steps)):
    counter = Counter(steps[:i])
    for key in ['n', 'ne', 'nw', 's', 'se', 'sw']:
        if key not in counter:
            counter[key] = 0
    max_dist = calc_distance(counter, max_dist)
print(f"max distance was {max_dist}")
