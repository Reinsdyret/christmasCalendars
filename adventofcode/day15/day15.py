

def calculateCrossingYaxis(x, y, x1, y1, ytoCheck):
    x = int(x)
    y = int(y)
    x1 = int(x1)
    y1 = int(y1)

    euclidean_distance = abs(x-x1) + abs(y-y1)

    if (y < ytoCheck):
        if ((y + euclidean_distance) < ytoCheck):
            return None

    if (y > ytoCheck):
        if ((y - euclidean_distance) > ytoCheck):
            return None

    difference = abs(ytoCheck - y)
    amount = (euclidean_distance * 2) - (2 * difference) + 1
    coords = []
    for i in range((x - (amount // 2)), (x + (amount // 2))):
        coords.append((i, ytoCheck))

    return coords


lines = []
grid = dict()
for i in range(4000001):
    grid[i] = dict()
print("done making dict")

with open('day15Input.txt', 'r') as f:
    lines = f.readlines()


coordsCrossing = set()


for line in lines:
    line = line.replace(":", "")
    line = line.replace(",", "")
    line = line.replace("\n", "")
    line = line.replace("=", "")
    line = line.replace("x", "")
    line = line.replace("y", "")
    _, _, x, y, _, _, _, _, x1, y1 = line.split(" ")
    for i in range(4000001):
        coords = calculateCrossingYaxis(x, y, x1, y1, i)
        if ((coords) == (None)):
            continue
        for x, y in coords:
            if (y in grid[x].keys()):
                continue

            grid[x][y] = "x"
    print("done line")
    
print(len(coordsCrossing))

