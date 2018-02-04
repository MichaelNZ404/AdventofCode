#python solution.py input.txt
import sys

with open(sys.argv[1]) as f:
   rows = [row.replace('\n', '') for row in f.readlines()]

shared_buffer = {
    0: [],
    1: []
}
class Program:
    def __init__(self, idx, id_in, instructions):
        self.idx = idx
        self.id_in = id_in
        self.registers = {'p': int(idx)}
        self.pointer = 0
        self.instructions = instructions
        self.halted = False
        self.send_counter = 0

    def run(self):
        split = self.instructions[self.pointer].split()
        print(self.idx, self.halted, self.pointer, split, self.registers)
        opperation, command = split[0], split[1:]

        if opperation == 'snd':
            shared_buffer[self.idx].append(self.registers.get(command[0], 0))
            self.send_counter += 1
            programA.halted = False
            programB.halted = False

        elif opperation == 'set':
            self.registers[command[0]] = int(self.registers.get(command[1], command[1]))

        elif opperation == 'add':
            if command[0] not in self.registers:
                self.registers[command[0]] = int(self.registers.get(command[1], command[1]))
            else:
                self.registers[command[0]] += int(self.registers.get(command[1], command[1]))

        elif opperation == 'mul':
            if command[0] in self.registers:
                self.registers[command[0]] *= int(self.registers.get(command[1], command[1]))
            else:
                self.registers[command[0]] = 0 * int(self.registers.get(command[1], command[1]))

        elif opperation == 'mod':
            if command[0] in self.registers:
                self.registers[command[0]] %= int(self.registers.get(command[1], command[1]))
            else:
                self.registers[command[0]] = 0 % int(self.registers.get(command[1], command[1]))

        elif opperation == 'rcv':
            if shared_buffer[self.id_in]:
                self.registers[command[0]] = shared_buffer[self.id_in].pop(0)
            else:
                self.halted = True
                return

        elif opperation == 'jgz':
            if int(self.registers.get(command[0], command[0])) > 0:
                self.pointer += int(self.registers.get(command[1], command[1]))
                return
        else:
            raise Exception("Unknown Command")
        self.pointer += 1

programA = Program(0, 1, rows)
programB = Program(1, 0, rows)

while(programA.halted is False or programB.halted is False):
    while programA.halted is False:
        programA.run()
    while programB.halted is False:
        programB.run()

print(f"Program 1 sent {programB.send_counter} values")
