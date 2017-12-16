#python solution.py input.txt
import sys

with open(sys.argv[1]) as f:
   rows = f.readlines()

rows = [row.replace('\n', '') for row in rows]
nodes = {}

for row in rows:
    name, connections = row.split(' <-> ')
    connections = connections.split(', ')
    if name not in nodes:
        nodes[name] = set()
    nodes[name].update(connections)

total_groups = []
visited_nodes = set()

def check_node(name):
    visited_nodes.add(name)
    if name == group_name:
        return name
    elif group_name in nodes[name]:
        return name
    elif any([check_node(x) for x in nodes[name] if x not in visited_nodes]):
        return name
    else:
        return False

while len(nodes.keys()) > 0:
    group_name = list(nodes.keys())[0]
    matching_groups = []
    for name in nodes.keys():
        visited_nodes = set()
        membership = check_node(name)
        if membership:
            matching_groups.append(membership)
    total_groups.append(matching_groups)
    print(f"groups for {group_name}: {matching_groups}")
    for name in matching_groups:
        del nodes[name]

print(f"Group count is {len(total_groups)}")
