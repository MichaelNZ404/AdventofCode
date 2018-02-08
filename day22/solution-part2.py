#python solution.py input.txt
import sys
import math
from enum import Enum

class Virus:
    def __init__(self, offset):
        self.rotation = 0
        self.x = offset
        self.y = offset

    def turn_left(self):
        if self.rotation == 0:
            self.rotation = 270
        else:
            self.rotation = (self.rotation - 90) % 360

    def turn_right(self):
        self.rotation = (self.rotation + 90) % 360

    def move_forward(self):
        if self.rotation == 0:
            self.y -= 1
        elif self.rotation == 90:
            self.x += 1
        elif self.rotation == 180:
            self.y += 1
        elif self.rotation == 270:
            self.x -= 1

    @property
    def loc(self):
        loc = (self.y, self.x)
        return loc

class Status(Enum):
    CLEAN = 0
    WEAKENED = 1
    INFECTED = 2
    FLAGGED = 3


infection_map = {}
map_input = []
with open(sys.argv[1]) as f:
    map_input = f.readlines()
    for row_idx, row in enumerate(map_input):
        row = row.replace('\n', '')
        for col_idx, char in enumerate(row):
            if char == "#":
                infection_map[(row_idx, col_idx)] = Status.INFECTED

offset = math.floor(len(map_input) / 2)
bursts = 10000000
infections = 0

virus = Virus(offset)
for i in range(bursts):
    if virus.loc not in infection_map or infection_map[virus.loc] == Status.CLEAN:
        virus.turn_left()
    elif infection_map[virus.loc] == Status.WEAKENED:
        infections += 1
    elif infection_map[virus.loc] == Status.INFECTED:
        virus.turn_right()
    elif infection_map[virus.loc] == Status.FLAGGED:
        virus.turn_right()
        virus.turn_right()
    current_status = infection_map.get(virus.loc, Status.CLEAN)
    infection_map[virus.loc] = Status((current_status.value + 1) % 4)
    virus.move_forward()

print(f"{infections} infections caused")
