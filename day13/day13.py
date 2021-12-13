f = open('input.txt', 'r')
txt: str = f.read()
f.close()

lines: list = txt.splitlines()

points: list = lines[:lines.index('')]

instructions: list = lines[lines.index('') + 1:]

class Point:
    def __init__(self, coordinates) -> None:
        x, y = coordinates.split(',')
        self.x = int(x)
        self.y = int(y)

    def y_fold(self, y_coordinate) -> None:
        if self.y < y_coordinate:
            pass
        else:
            self.y = y_coordinate - (self.y - y_coordinate)

    def x_fold(self, x_coordinate) -> None:
        if self.x < x_coordinate:
            pass
        else:
            self.x = x_coordinate - (self.x - x_coordinate)

points = [Point(p) for p in points]


def part1():

    points_after_x_fold = []

    for p in points:
        p.x_fold(655)
        points_after_x_fold.append(p)

    return points_after_x_fold

# print(len(set([(p.x, p.y) for p in part1()])))

def parse_instructions():
    parsed_instructions = []
    for i in instructions:
        fold, along, instr = i.split()
        x_y, coordinate = instr.split('=')
        parsed_instructions.append((x_y, int(coordinate)))
    return parsed_instructions

def part2(ps):

    instructions = parse_instructions()

    for i in instructions:
        points_post_fold = []
        for p in ps:
            if i[0] == 'y':
                p.y_fold(i[1])
            else:
                p.x_fold(i[1])
            points_post_fold.append(p)
        ps = points_post_fold


    final_points = set([(p.x, p.y) for p in ps])

    out = open('output.txt', 'w')

    for y in range(6):
        row = []
        for x in range(40):
            if (x, y) in final_points:
                out.write('x')
            else:
                out.write(' ')
        out.write('\n')

part2(points)