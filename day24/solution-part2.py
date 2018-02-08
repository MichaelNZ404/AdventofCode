#python solution.py input.txt
import sys

with open(sys.argv[1]) as f:
    rows = [row.replace('\n', '').split('/') for row in f.readlines()]

def get_paths(end_socket, remaining_parts):
    paths = []
    if remaining_parts:
        for part in remaining_parts:
            if end_socket in part:
                b = remaining_parts[:]
                b.remove(part)
                if part[0] == end_socket:
                    remaining_chains = get_paths(part[1], b)
                elif part[1] == end_socket:
                    remaining_chains = get_paths(part[0], b)
                if remaining_chains:
                    paths += [[part] + rc for rc in remaining_chains]
                else:
                    paths.append([part])
    return paths

def get_path_strength(path):
    strength = 0
    for part in path:
        strength += part[0] + part[1]
    return strength

def get_longest_paths(paths):
    max_length = len(max(paths, key=len))
    return [path for path in paths if len(path) == max_length]

bridges = [(int(x[0]), int(x[1])) for x in rows]
strengths = {}

paths = get_paths(0, bridges)
for path in get_longest_paths(paths):
    strength = get_path_strength(path)
    strengths[strength] = path

max_strength = max(strengths)
print(max_strength, strengths[max_strength])
