from collections import deque

def findAreas(map):
  areas = []
  seen = set()
  
  for y in range(len(map)):
    for x in range(len(map[y])):
      node = (x,y)
      
      if node in seen: continue
      
      area = findArea(node, map)
      areas.append(area)
      seen.update(area)
  
  return areas


def inbounds(x, y, map):
  return 0 <= y < len(map) and 0 <= x < len(map[y])


def findArea(node, map):
  queue = deque()
  area = set()
  visited = set()
  
  queue.append((node[0], node[1]))
  area.add(node)
  
  visited.add(node)
  
  moves = [
    (1,0),
    (-1,0),
    (0,1),
    (0,-1)
  ]
  
  while len(queue) > 0:
    node = queue.popleft()
    
    for mx, my in moves:
      newX = node[0] + mx
      newY = node[1] + my
      
      if inbounds(newX, newY, map) and map[newY][newX] == map[node[1]][node[0]] and (newX, newY) not in visited:
        queue.append((newX, newY))
        area.add((newX, newY))
      visited.add((newX, newY))
        
  return area


def getPerimiter(area, map):
  perimiter = 0
  
  moves = [
    (1,0),
    (-1,0),
    (0,1),
    (0,-1)
  ]
  for (x,y) in area:
    for (mx, my) in moves:
      newX, newY = x + mx, y + my
      if not inbounds(newX, newY, map) or map[newY][newX] != map[y][x]:
        perimiter += 1
  
  return perimiter 


def getSides(area, map):
  processedSides = {
    (x,y): {
      "checkHor": False,
      "checkVer": False,
    } for (x,y) in area
  }

  totalSides = 0

  # Horizontal check

  for (x,y) in area:
    contains = []
    if processedSides[(x,y)]["checkHor"]: continue
    i = 0
    while (x + i, y) in area: # Process all on line to right
      processedSides[(x + i,y)]["checkHor"] = True
      contains.append((x + i, y))
      i += 1
    i = 0
    while (x - i, y) in area: # Process all on line to left
      processedSides[(x - i, y)]["checkHor"] = True
      contains.append((x - i, y))
      i += 1
    totalSides += 2
    print(contains)
  print(totalSides)
  # Vertical check
  for (x,y) in area:
    #print(x,y)
    contains = []
    if processedSides[(x,y)]["checkVer"]: continue
    i = 0
    while (x, y + i) in area: # Process all on column down
      processedSides[(x, y + i)]["checkVer"] = True
      contains.append((x, y + i))
      i += 1
    i = 0
    while (x, y - i) in area: # Process all on column up
      processedSides[(x, y - i)]["checkVer"] = True
      contains.append((x, y - i))
      i += 1
    totalSides += 2
    print(contains)
  print(totalSides)


  return totalSides


garden = []

with open("simple_test_input2.txt", 'r') as f:
  for line in f.readlines():
    garden.append(list(line.strip()))

total_sum_part1 = 0
total_sum_part2 = 0

for area in findAreas(garden):
  #total_sum_part1 += len(area) * getPerimiter(area, garden)
  sides = getSides(area, garden)
  perimiter = getPerimiter(area, garden)
  total_sum_part2 += len(area) * sides
  print(f"Sides: {sides}")
  print(f"Perimiter: {perimiter}")

print(total_sum_part1)
print(total_sum_part2)