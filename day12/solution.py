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
    nodes[name].add(x) for x in connections

visited_nodes = []
for node in nodes.keys():
    if node
