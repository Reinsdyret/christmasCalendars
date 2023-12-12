steps = {}

pipe_map = []

with open('input.txt','r') as f:
    for line in f:
        pipe_map.append(line.strip())


# Find s starting point
for row in range(len(pipe_map)):
    for column in range(len(pipe_map[row])):
        if pipe_map[row][column] == "S":
            start = (row,column)


step = 0
currY = start[0] - 1
currX = start[1]
cpyY = currY
cpX = currX
prevY = start[0]
prevX = start[1]
path = []
found = False
#print(pipe_map[126][87])
while not found:
    current = pipe_map[currY][currX]
    path.append((currY, currX))
    cpY = currY
    cpX = currX
    match current:
        case "|":
            # Check above and under
            if prevY > currY:
                # Go up
                currY -= 1
            elif prevY < currY:
                # go down
                currY += 1
        case "-":
            # Check left and right
            if prevX > currX:
                # Go left
                currX -= 1
            elif prevX < currX:
                # Go right
                currX += 1
        case "L":
            # Check right and over
            if prevY < currY:
                # Go right
                currX += 1
            elif prevX > currX:
                # Go up
                currY -= 1
        case "J":
            # Check left and over
            if prevY < currY:
                # Go left
                currX -= 1
            elif prevX < currX:
                # Go up
                currY -= 1
        case "7":
            # Check under and left
            if prevY > currY:
                # Go left
                currX -= 1
            elif prevX < currX:
                # Go down
                currY += 1
        case "F":
            # Check right and under
            if prevY > currY:
                # Go right
                currX += 1
            elif prevX > currX:
                # Go down
                currY += 1
        case ".":
            raise Exception(f"Kom til punktum loser, coordinat er {currY = }, {currX = } og kom fra {prevY = }, {prevX = }. Forrige bokstav er {pipe_map[prevY][prevX]}")
        case "S":
            found = True

    prevY = cpY
    prevX = cpX

  
print(len(path) // 2)



