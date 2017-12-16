#python solution.py input.txt
import sys

with open(sys.argv[1]) as f:
   rows = f.readlines()
rows = [row.replace('\n', '').split() for row in rows]

generatorA = int(rows[0][4])
generatorB = int(rows[1][4])

generatorAFactor = 16807
generatorBFactor = 48271
division_number = 2147483647
iterations = 40000000

matches = 0
for i in range(iterations):
    generatorA = (generatorA*generatorAFactor)%division_number
    generatorB = (generatorB*generatorBFactor)%division_number
    if bin(generatorA)[-16:] == bin(generatorB)[-16:]:
        matches += 1

print(f"matches: {matches}")
