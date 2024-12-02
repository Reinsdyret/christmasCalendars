
lines = []
with open("day9Input.txt", 'r') as f:
    lines = f.readlines()

locations = set()

headLocation = {
        "x": 0,
        "y": 0,
        }

tailLocation = {
        "x": 0,
        "y": 0,
        }


def tailIsCloseEnough(headLocation, tailLocation):
    if abs(headLocation["x"] - tailLocation["x"]) > 1 or abs(headLocation["y"] - tailLocation["y"]) > 1:
        return False
    return True

def updateTailLocation(direction):
    if tailIsCloseEnough(headLocation,tailLocation): return
    match direction:
        case "L":
            tailLocation["x"] = headLocation["x"] + 1
            tailLocation["y"] = headLocation["y"]
        case "R":
            tailLocation["x"] = headLocation["x"] - 1
            tailLocation["y"] = headLocation["y"]
        case "U":
            tailLocation["y"] = headLocation["y"] - 1
            tailLocation["x"] = headLocation["x"]
        case "D":
            tailLocation["y"] = headLocation["y"] + 1
            tailLocation["x"] = headLocation["x"]


def addNextLocationAndPrint(direction):
    updateTailLocation(direction)
    locations.add((tailLocation["x"], tailLocation["y"]))
    print(f"{tailLocation['x']=}, {tailLocation['y']=}")

print(lines)

for line in lines:
    direction, amount = line.split(" ")
    print(f"{direction=}, {amount=}")
    match direction:
        case "L":
            for i in range(0,int(amount)): 
                headLocation["x"] -= 1
                addNextLocationAndPrint(direction)
        case "R":
            for i in range(0,int(amount)): 
                headLocation["x"] += 1
                addNextLocationAndPrint(direction)
        case "U":
            for i in range(0,int(amount)): 
                headLocation["y"] += 1
                addNextLocationAndPrint(direction)
        case "D":
            for i in range(0,int(amount)): 
                headLocation["y"] -= 1
                addNextLocationAndPrint(direction)

locationsList = list(locations)
print(len(locations))

