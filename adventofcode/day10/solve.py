from copy import deepcopy


def hasTrail(map, graph, banned, x, y):
    if map[y][x] == 9 and (x, y) not in banned:
        return True, [(x, y)]

    for neighx, neighy in graph[(x, y)]:
        found, path = hasTrail(map, graph, banned, neighx, neighy)
        if found:
            return True, [(x, y)] + path

    return False, []


def insertEdge(graph, p1, p2):
    graph[p1].append(p2)


def inbounds(map, x, y):
    return 0 <= y < len(map) and 0 <= x < len(map[y])


# Graph with each position pointing to the available neighbours
graph = {}

# Map that has the values per position
trail_map = []

y_pos = []

with open("test_input.txt", "r") as f:
    for y, line in enumerate(f.readlines()):
        trail_map.append(list(map(int, line.strip())))
        for x in range(len(line.strip())):
            graph[(x, y)] = []

for y in range(len(trail_map)):
    for x in range(len(trail_map[y])):
        if trail_map[y][x] == 0:
            y_pos.append((x, y))

        if inbounds(trail_map, x, y - 1) and trail_map[y - 1][x] - trail_map[y][x] == 1:
            insertEdge(graph, (x, y), (x, y - 1))

        if inbounds(trail_map, x, y + 1) and trail_map[y + 1][x] - trail_map[y][x] == 1:
            insertEdge(graph, (x, y), (x, y + 1))

        if inbounds(trail_map, x - 1, y) and trail_map[y][x - 1] - trail_map[y][x] == 1:
            insertEdge(graph, (x, y), (x - 1, y))

        if inbounds(trail_map, x + 1, y) and trail_map[y][x + 1] - trail_map[y][x] == 1:
            insertEdge(graph, (x, y), (x + 1, y))

count_paths = 0
paths = set()

for x, y in y_pos:
    banned = set()
    graph_copy = deepcopy(graph)
    found, path = hasTrail(trail_map, graph, banned, x, y)

    while found and str(path) not in paths:
        paths.add(str(path))
        # print(f"Number 0 as pos {y = }, {x = }")
        # print(path)
        count_paths += 1

        banned.add(path[-1])
        found, path = hasTrail(trail_map, graph_copy, banned, x, y)


print(count_paths)
