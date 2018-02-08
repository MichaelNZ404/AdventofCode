#python solution.py input.txt
import sys

with open(sys.argv[1]) as f:
    rules = [row.replace('\n', '') for row in f.readlines()]

rules = [(x.split(' => ')[0], x.split(' => ')[1]) for x in rules]

def test_mask(mask, square):
    def flip_h(square):
        return square[::-1]

    def flip_v(square):
        return [x[::-1] for x in square]

    def rotate_clockwise(square):
        return [''.join(x) for x in list(zip(*square[::-1]))]

    for i in range(4):
        if (mask == square or
                mask == flip_h(square) or
                mask == flip_v(square) or
                mask == flip_h(flip_v(square))):
            return True
        square = rotate_clockwise(square)
    return False

class Square:

    def __init__(self):
        self.shape = ['.#.','..#','###']

    def tick(self):
        rows = []
        if len(self.shape) % 2 == 0:
            for i in range(int(len(self.shape) / 2)):
                columns = ['', '', '']
                for j in range(int(len(self.shape) / 2)):
                    square = [
                        self.shape[2*i][2*j:2*j+2],
                        self.shape[2*i+1][2*j:2*j+2]
                    ]
                    mapped_sq = self.apply_rule(square, 2)
                    columns[0] += mapped_sq[0]
                    columns[1] += mapped_sq[1]
                    columns[2] += mapped_sq[2]
                rows += columns

        elif len(self.shape) % 3 == 0:
            for i in range(int(len(self.shape) / 3)):
                columns = ['', '', '', '']
                for j in range(int(len(self.shape) / 3)):
                    square = [
                        self.shape[3*i][3*j:3*j+3],
                        self.shape[3*i+1][3*j:3*j+3],
                        self.shape[3*i+2][3*j:3*j+3]
                    ]
                    mapped_sq = self.apply_rule(square, 3)
                    columns[0] += mapped_sq[0]
                    columns[1] += mapped_sq[1]
                    columns[2] += mapped_sq[2]
                    columns[3] += mapped_sq[3]
                rows += columns
        else:
            raise Exception(f"{self.shape} Not divisible by 2 or 3")
        self.shape = rows

    def apply_rule(self, square, size):
        for rule in rules:
            if len(rule[0].split('/')) != size:
                continue

            mask = rule[0].split('/')
            if test_mask(mask, square):
                return rule[1].split('/')
        raise Exception(f"No rule found for {square}")

    @property
    def on_pixels(self):
        pixels = 0
        for row in self.shape:
            pixels += row.count('#')
        return pixels


sq = Square()
for i in range(5):
    sq.tick()
print(sq.on_pixels)
