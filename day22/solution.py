#python solution.py input.txt
import sys
import math

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

infection_map = set()
map_input = []
with open(sys.argv[1]) as f:
    map_input = f.readlines()
    for row_idx, row in enumerate(map_input):
        row = row.replace('\n', '')
        for col_idx, char in enumerate(row):
            if char == "#":
                infection_map.add((row_idx, col_idx))

offset = math.floor(len(map_input) / 2)
bursts = 10000
infections = 0

virus = Virus(offset)
for i in range(bursts):
    if virus.loc in infection_map:
        infection_map.remove(virus.loc)
        virus.turn_right()
    else:
        infection_map.add(virus.loc)
        infections += 1
        virus.turn_left()
    virus.move_forward()

print(f"{infections} infections caused")
