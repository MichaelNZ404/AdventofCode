#python solution.py input.txt
import sys

with open(sys.argv[1]) as f:
    maze = [row.replace('\n', '') for row in f.readlines()]

dist_from_top = 0
dist_from_left = 0
current_direction = None
seen_chars = []

while True:
    if maze[0][dist_from_left] is '|':
        current_direction = 'DOWN'
        dist_from_top = 1
        break
    else:
        dist_from_left += 1

while True:
    segment = maze[dist_from_top][dist_from_left]

    if current_direction is 'DOWN' or current_direction is 'UP':
        if segment is '+':
            if maze[dist_from_top][dist_from_left + 1] is not ' ':
                current_direction = 'RIGHT'
                dist_from_left += 1
                continue
            else:
                current_direction = 'LEFT'
                dist_from_left -= 1
                continue

        if current_direction is 'DOWN':
            dist_from_top += 1
        else:
            dist_from_top -= 1

    elif current_direction is 'LEFT' or current_direction is 'RIGHT':
        segment = maze[dist_from_top][dist_from_left]
        if segment is '+':
            if maze[dist_from_top + 1][dist_from_left] is not ' ':
                current_direction = 'DOWN'
                dist_from_top += 1
                continue
            else:
                current_direction = 'UP'
                dist_from_top -= 1
                continue

        if current_direction is 'LEFT':
            dist_from_left -= 1
        else:
            dist_from_left += 1

    if segment == ' ':
        break
    if segment != '|' and segment != '-':
        seen_chars.append(segment)

print(''.join(seen_chars))
