f = open('input.txt', 'r')
txt: str = f.read()
f.close()

lines = txt.splitlines()

def part1():

    minimums: list = []

    for i, line in enumerate(lines):
        for j, number in enumerate(line):
            if i > 0:
                up: int = int(lines[i-1][j])
            else:
                up: int = 10
            if i < len(lines) - 1:
                down: int = int(lines[i+1][j])
            else:
                down: int = 10
            if j < len(line) - 1:
                right: int = int(lines[i][j+1])
            else:
                right: int = 10
            if j > 0:
                left: int = int(lines[i][j-1])
            else:
                left: int = 10

            if int(number) < up and int(number) < down and int(number) < left and int(number) < right:
                minimums.append(int(number))

    total_risk_level: int = 0

    for minimum in minimums:
        total_risk_level += (1 + minimum)

    return total_risk_level

# print(part1())
    
class Node:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.visited = True if int(lines[y][x]) == 9 else False

def create_simplified_map():
    simplied_map: list = []
    for y, line in enumerate(lines):
        simplied_line: list = []
        for x, num in enumerate(line):
            if int(num) == 9:
                simplied_line.append(Node(x,y))
            else:
                simplied_line .append(Node(x,y))
        simplied_map.append(simplied_line)

    return simplied_map

simplified_map = create_simplified_map()

class Basin:

    def __init__(self, starting_node):
        self.to_visit = [starting_node]
        self.basin_size = 0
        while self.to_visit:
            self.explore_basin()

    def explore_basin(self):
        current_node = self.to_visit.pop()
        if current_node.visited:
            return None

        self.basin_size += 1
        current_node.visited = True
        if current_node.y - 1 >= 0 and not simplified_map[current_node.y - 1][current_node.x].visited:
            self.to_visit.append(simplified_map[current_node.y - 1][current_node.x])
        if current_node.y + 1 < len(simplified_map) and not simplified_map[current_node.y + 1][current_node.x].visited:
            self.to_visit.append(simplified_map[current_node.y + 1][current_node.x])
        if current_node.x - 1 >= 0 and not simplified_map[current_node.y][current_node.x - 1].visited:
            self.to_visit.append(simplified_map[current_node.y][current_node.x - 1])
        if current_node.x + 1 < len(simplified_map[0]) and not simplified_map[current_node.y][current_node.x + 1].visited:
            self.to_visit.append(simplified_map[current_node.y][current_node.x + 1])

def part2():

    basins = []

    for i, line in enumerate(simplified_map):
        for j, node in enumerate(line):
            if node.visited == False:
                basins.append(Basin(node))

    largest_basins: list = sorted([b.basin_size for b in basins])[-3:]

    product: int = largest_basins[0] * largest_basins[1] * largest_basins[2]

    return product

# print(part2())

