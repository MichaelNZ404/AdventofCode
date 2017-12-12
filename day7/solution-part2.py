#python solution.py input.txt
import re
import sys
from collections import Counter

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

def find_imbalance(tower_name):
    support_weights = {}
    if len(TOWERS[tower_name].supports) == 0:
        return TOWERS[tower_name].weight

    for s in TOWERS[tower_name].supports:
        support_weights[s] = find_imbalance(s)
    if len(set(support_weights.values())) == 1: #children balanced
        #return weight of all children + weight of self
        return(sum(support_weights.values()) + TOWERS[tower_name].weight)
    else: #need to correct imbalance
        sup_count = Counter(support_weights.values()).most_common()
        invalid_weight = sup_count[-1][0]
        target_weight = sup_count[0][0]
        print(f"tower {s} has invalid child weight {invalid_weight} - should be {target_weight}")
        correction = target_weight-invalid_weight
        for i in support_weights.items():
            if i[1] == invalid_weight:
                TOWERS[i[0]].weight += correction
                support_weights[s] = target_weight
                print(f"correction of {correction} made to {i[0]}")
                print(f"{i[0]} now weighs {TOWERS[i[0]].weight}")
        return(sum(support_weights.values()) + TOWERS[tower_name].weight)


#MAIN
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
    tower_weight = int(re.match('\((\d*)\)', tower_data[1]).group(1))
    if tower_name not in TOWERS:
            TOWERS[tower_name] = Tower(tower_name)
    TOWERS[tower_name].weight = tower_weight
    for supported_tower in support_list:
        TOWERS[tower_name].support_tower(supported_tower)

#get random tower and follow path down
bottom_tower = list(TOWERS.keys())[5]
while TOWERS[bottom_tower].supported_by is not None:
    bottom_tower = TOWERS[bottom_tower].supported_by

print(f"Bottom tower is: {bottom_tower}")
find_imbalance(bottom_tower)
