#python solution.py input.txt
import sys
import re

with open(sys.argv[1]) as f:
    rows = [row.replace('\n', '') for row in f.readlines()]

class Particle:

    def __init__(self, properties, idx):
        self.id = idx

        position, velocity, accelaration = properties
        self._position = [int(pos) for pos in position.split(',')]
        self._velocity = [int(vel) for vel in velocity.split(',')]
        self._accelaration = [int(acc) for acc in accelaration.split(',')]

    @property
    def manhattan_acceleration(self):
        return sum([abs(a) for a in self._accelaration])

    @property
    def manhattan_position(self):
        return sum([abs(p) for p in self._position])

    @property
    def position(self):
        return ','.join(str(p) for p in self._position)

    def tick(self):
        for i in range(len(self._velocity)):
            self._velocity[i] += self._accelaration[i]
            self._position[i] += self._velocity[i]

    def __lt__(self, other):
        return (
            (self.manhattan_acceleration, self.manhattan_position) <
            (other.manhattan_acceleration, other.manhattan_position))

pattern = re.compile(r"<([^>]*)>")
particles = {idx: Particle(pattern.findall(row), idx) for idx, row in enumerate(rows)}

i = 0
while i < 100:
    to_delete = set()
    seen = {}
    for key, p in particles.items():
        if p.position not in seen:
            seen[p.position] = p.id
            p.tick()
        else:
            to_delete.add(p.id)
            to_delete.add(seen[p.position])

    if len(to_delete) > 0:
        i = 0
    else:
        i += 1
    for pid in to_delete:
        print(f"---{pid} destroyed by collision---")
        particles.pop(pid, None)

print(len(particles))
