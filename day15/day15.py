f = open('test_input.txt', 'r')
txt = f.read()
f.close()

rows = txt.splitlines()

graph = [[int(val) for val in row] for row in rows]

def part1(graph):

    points = []
    for y, row in enumerate(graph):
        for x, num in enumerate(row):
            points.append((x,y))

    # Create a distances dict
    distances_dict = dict(zip(points, [9999999999999] * len(points)))
    distances_dict[(0, 0)] = 0

    for y, row in enumerate(graph):
        for x, val in enumerate(row):

            current_node = (x, y)
            current_distance = distances_dict[(x, y)]

            x, y = current_node
            available_neighbours = []
            if x < len(graph[0]) - 1:
                available_neighbours.append((x + 1, y))
            if y < len(graph) - 1:
                available_neighbours.append((x, y + 1))

            for n in available_neighbours:
                if graph[n[1]][n[0]] + current_distance < distances_dict[n]:
                    distances_dict.update({n: graph[n[1]][n[0]] + current_distance})

    print(distances_dict)

    return distances_dict

# print(part1(graph))

def part2():

    # Construct graph

    def create_tile(tile):
        new_tile = []
        for row in tile:
            new_row = []
            for val in row:
                new_val = (val + 1) % 10
                new_val = new_val if new_val != 0 else 1
                new_row.append(new_val)
            new_tile.append(new_row)

        return new_tile

    # Expand downwards
    tile = graph
    tiles = dict(zip(range(5), [] * 5))

    new_graph = []
    for i in range(5):
        tiles[i] = tile
        for row in tile:
            new_graph.append(row)
        tile = create_tile(tile)

    # Expand across
    tile = new_graph
    tiles = dict(zip(range(5), [] * 5))

    for i in range(5):
        tiles[i] = tile
        tile = create_tile(tile)

    new_graph = []
    for j in range(len(tiles[0])):
        new_row = []
        for i in range(5):
            new_row += tiles[i][j]
        new_graph.append(new_row)

    return part1(new_graph)


print(part2()[(499, 499)])
# NOTE need to remove the value for 0,0