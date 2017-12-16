#python solution.py input.txt
import sys

#group name is a hardcoded arg that defines membership of the group
group_name = '0'

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

matching_groups = []
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

for name in nodes.keys():
    visited_nodes = set()
    membership = check_node(name)
    if membership:
        matching_groups.append(membership)

print(f"Membership is {matching_groups}")
print(f"Membership count is {len(matching_groups)}")
