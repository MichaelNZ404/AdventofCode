#python solution.py input.txt
import sys

with open(sys.argv[1]) as f:
   rows = f.readlines()
rows = [row.replace('\n', '').split() for row in rows]

division_number = 2147483647
def GeneratorA(x=int(rows[0][4])):
    factor = 16807
    while True:
        x = (x*factor)%division_number
        if x%4 == 0:
            yield x
def GeneratorB(x=int(rows[1][4])):
    factor = 48271
    while True:
        x = (x*factor)%division_number
        if x%8 == 0:
            yield x

genA = GeneratorA()
genb = GeneratorB()

iterations = 5000000
matches = 0
for i in range(iterations):
    if bin(next(genA))[-16:] == bin(next(genb))[-16:]:
        matches += 1

print(f"matches: {matches}")
