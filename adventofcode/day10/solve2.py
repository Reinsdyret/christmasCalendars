from copy import deepcopy

total_path_count = 0


def countPaths(map, graph, x, y):
    global total_path_count
    if map[y][x] == 9:
        total_path_count += 1

    for neighx, neighy in graph[(x, y)]:
        countPaths(map, graph, neighx, neighy)


def insertEdge(graph, p1, p2):
    graph[p1].append(p2)


def inbounds(map, x, y):
    return 0 <= y < len(map) and 0 <= x < len(map[y])


# Graph with each position pointing to the available neighbours
graph = {}

# Map that has the values per position
trail_map = []

y_pos = []

with open("input.txt", "r") as f:
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


for x, y in y_pos:
    countPaths(trail_map, graph, x, y)

print(total_path_count)
