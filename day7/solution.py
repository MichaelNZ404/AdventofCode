#python solution.py input.txt
import re
import sys

class Tower:

    def __init__(self, name):
        self.name = name
        self.weight = None
        self.supported_by = None
        self.supports = []

    def support_tower(self, tower_name):
        self.supports.append(tower_name)
        if tower_name not in TOWERS:
                TOWERS[tower_name] = Tower(tower_name)
        TOWERS[tower_name].supported_by = self.name


with open(sys.argv[1]) as f:
   rows = f.readlines()

TOWERS = {}

for row in rows:
    row = row.replace('\n', '')
    support_list = []
    if '->' in row:
        row = row.split(' -> ')
        support_list = row[1].split(', ')
        row = row[0]
    tower_data = row.split(' ')
    tower_name = tower_data[0]
    tower_weight = re.match('\((\d*)\)', tower_data[1]).group(1)
    if tower_name not in TOWERS:
            TOWERS[tower_name] = Tower(tower_name)
    TOWERS[tower_name].weight = tower_weight
    for supported_tower in support_list:
        TOWERS[tower_name].support_tower(supported_tower)

#get random tower and follow path down
tower_name = list(TOWERS.keys())[5]
while TOWERS[tower_name].supported_by is not None:
    tower_name = TOWERS[tower_name].supported_by

print(tower_name)
