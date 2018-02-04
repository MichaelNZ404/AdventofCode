#python solution.py input.txt
import sys
import re

with open(sys.argv[1]) as f:
    rows = [row.replace('\n', '') for row in f.readlines()]

class Particle:

    def __init__(self, properties, idx):
        self.id = idx

        position, velocity, accelaration = properties
        self.position = [int(pos) for pos in position.split(',')]
        self.velocity = [int(vel) for vel in velocity.split(',')]
        self.accelaration = [int(acc) for acc in accelaration.split(',')]

    @property
    def manhattan_acceleration(self):
        return sum([abs(a) for a in self.accelaration])

    @property
    def manhattan_position(self):
        return sum([abs(p) for p in self.position])

    def tick(self):
        for i in range(len(self.velocity)):
            self.velocity[i] += self.accelaration[i]

    def __lt__(self, other):
        return (
            (self.manhattan_acceleration, self.manhattan_position) <
            (other.manhattan_acceleration, other.manhattan_position))

pattern = re.compile(r"<([^>]*)>")
particles = sorted([Particle(pattern.findall(row), idx) for idx, row in enumerate(rows)])

print(particles[0].id)
