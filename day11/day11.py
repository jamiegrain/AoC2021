from typing import List

f = open('input.txt', 'r')
txt: str = f.read()
f.close()

class Octopus:

    def __init__(self, energy, x, y):
        self.energy = int(energy)
        self.x = x
        self.y = y

    def increment_energy(self):
        if self.energy == 9:
            self.energy += 1
            self.flash()
        self.energy += 1

    def flash(self):
        global n_flashes
        n_flashes += 1
        for x in (self.x - 1, self.x, self.x + 1):
            for y in (self.y - 1, self.y, self.y + 1):
                if x >= 0 and x < 10 and y >= 0 and y < 10:
                    octopodes[y][x].increment_energy()

n_flashes: int = 0

octopodes: List[List[Octopus]] = []
for y, line in enumerate(txt.splitlines()):
    line_list: list = []
    for x, energy_score in enumerate(line):
        line_list.append(Octopus(energy_score, x, y))
    octopodes.append(line_list)

def iterate():
    """
    Go through an iteration of the octopodes grid
    Add one to the energy score each of the octopodes
    If an octopus flashes, add one to its neighbours
    """
    for y, line in enumerate(octopodes):
        for x, oct in enumerate(line):
            oct.increment_energy()
    for y, line in enumerate(octopodes):
        for x, oct in enumerate(line):
            if oct.energy > 9:
                oct.energy = 0

def part1():
    for _ in range(100):
        iterate()

    print(n_flashes)

# part1()

def part2():
    iteration = 0
    while True:
        iteration += 1
        prev_n_flashes = n_flashes
        iterate()
        if n_flashes - prev_n_flashes == 100:
            return iteration

print(part2())