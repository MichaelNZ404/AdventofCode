#python solution.py input.txt
import sys

dancers = [c for c in 'abcdefghijklmnop']

with open(sys.argv[1]) as f:
   row = f.readline().replace('\n', '')
dance_moves = row.split(',')

def perform_dance_moves(dancers, dance_moves):
    for dance_move in dance_moves:
        command = dance_move[0]
        if command == 's': #spin!
            group_size = int(dance_move[1:])
            dancers = dancers[-group_size:]+dancers[:-group_size]
        if command == 'x': #exchange!
            swap1pos, swap2pos = [int(x) for x in dance_move[1:].split('/')]
            dancers[swap1pos], dancers[swap2pos] = dancers[swap2pos], dancers[swap1pos]
        if command == 'p': #partner!
            swap1name, swap2name = dance_move[1:].split('/')
            swap1pos, swap2pos = dancers.index(swap1name), dancers.index(swap2name)
            dancers[swap1pos], dancers[swap2pos] = dancers[swap2pos], dancers[swap1pos]
    return dancers

loop_size = 0
for i in range(1000000000):
    dancers = perform_dance_moves(dancers, dance_moves)
    if dancers == [c for c in 'abcdefghijklmnop']:
        print(f"dancers realigned in {i+1} iterations")
        loop_size = 1000000000%(i+1)
        break

for i in range(loop_size):
    dancers = perform_dance_moves(dancers, dance_moves)

print(''.join(dancers))
