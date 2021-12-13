from collections import Counter

f = open('input.txt', 'r')
txt: str = f.read()
f.close()

edges: list = txt.splitlines()

class Node:
    def __init__(self, name) -> None:
        self.name = name
        self.large = True if self.name != self.name.lower() else False
        self.visitable_neighbours = []

class Graph:
    def __init__(self, edges) -> None:
        self.nodes = []
        for edge in edges:
            nodes = edge.split('-')

            node1_exists = True if nodes[0] in [node.name for node in self.nodes] else False
            node2_exists = True if nodes[1] in [node.name for node in self.nodes] else False

            if not node1_exists:
                node1 = Node(nodes[0])
            else:
                node1 = self.find_node(nodes[0])
            if not node2_exists:
                node2 = Node(nodes[1])
            else:
                node2 = self.find_node(nodes[1])

            node1.visitable_neighbours.append(node2)
            node2.visitable_neighbours.append(node1)

            if not node1_exists:
                self.nodes.append(node1)
            if not node2_exists:
                self.nodes.append(node2)

        self.find_node('end').visitable_neighbours = []
        self.find_node('end').large = True
        self.find_node('start').large = True

    def find_node(self, node_name) -> Node:
        return self.nodes[[node.name for node in self.nodes].index(node_name)]

g = Graph(edges)

path = [g.find_node('start')]
paths = []

unfinished_paths = [path]

def part2_criterion(path):
    small_caves = []
    for node in path:
        if not node.large:
            small_caves.append(node)

    return max(Counter(small_caves).values())


def valid_neighbour(node, current_path) -> bool:
    if (node.large or node not in current_path) and node.name != 'start':
        return True
    else:
        if not node.large and part2_criterion(current_path) < 2:
            return True
        else:
            return False

while unfinished_paths:
    current_path = unfinished_paths.pop()
    if current_path[-1].name == 'end':
        paths.append(current_path)
    else:
        for node in current_path[-1].visitable_neighbours:
            if valid_neighbour(node, current_path):
                new_path = current_path.copy()
                new_path.append(node)
                unfinished_paths.append(new_path)


print(len(paths))