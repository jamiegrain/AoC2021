#Extract the input
f = open('input.txt', 'r')
txt: str = f.read()
f.close()

directions: list = txt.splitlines()

# Part 1

horz: int = 0
vert: int = 0

for d in directions:
    if d[:-2] == 'forward':
        horz += int(d[-1])
    elif d[:-2] == 'down':
        vert += int(d[-1])
    if d[:-2] == 'up':
        vert -= int(d[-1])

print(horz * vert)

# Part 2

horz: int = 0
vert: int = 0
aim: int = 0

for d in directions:
    if d[:-2] == 'forward':
        horz += int(d[-1])
        vert += int(d[-1]) * aim
    elif d[:-2] == 'down':
        aim += int(d[-1])
    if d[:-2] == 'up':
        aim -= int(d[-1])

print(horz * vert)