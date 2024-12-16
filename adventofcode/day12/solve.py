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
      "sideAbove": False,
      "sideBelow": False,
      "sideRight": False,
      "sideLeft" : False
    } for (x,y) in area
  }

  totalSides = 0
  
  sortedX = sorted(list(area), key=lambda a: a[0]) 
  sortedY = sorted(list(area), key=lambda a: a[1]) 
  
  # Horizontal check
  for (x,y) in sortedX:
    # Above
    if not inbounds(x,y-1,map) or map[y - 1][x] != map[y][x]:
      # If part of a side
      if (x-1, y) in processedSides and  processedSides[(x-1, y)]["sideAbove"]:
        processedSides[(x, y)]["sideAbove"] = True
      else:
        totalSides += 1
        processedSides[(x, y)]["sideAbove"] = True
    
    # Below
    if not inbounds(x,y+1,map) or map[y + 1][x] != map[y][x]:
      # If part of side
      if (x-1, y) in processedSides and processedSides[(x-1, y)]["sideBelow"]:
        processedSides[(x,y)]["sideBelow"] = True
      else:
        totalSides += 1
        processedSides[(x,y)]["sideBelow"] = True
  
  # Vertical check
  for (x,y) in sortedY:
    # Left
    if not inbounds(x-1, y, map) or map[y][x-1] != map[y][x]:
      if (x,y-1) in processedSides and processedSides[(x,y-1)]["sideLeft"]:
        processedSides[(x,y)]["sideLeft"] = True
      else:
        totalSides += 1
        processedSides[(x,y)]["sideLeft"] = True
      

    # Right
    if not inbounds(x+1, y, map) or map[y][x+1] != map[y][x]:
      if (x,y-1) in processedSides and processedSides[(x,y-1)]["sideRight"]:
        processedSides[(x,y)]["sideRight"] = True
      else:
        totalSides += 1
        processedSides[(x,y)]["sideRight"] = True

  return totalSides


garden = []

with open("input.txt", 'r') as f:
  for line in f.readlines():
    garden.append(list(line.strip()))

total_sum_part1 = 0
total_sum_part2 = 0

for area in findAreas(garden):
  #total_sum_part1 += len(area) * getPerimiter(area, garden)
  sides = getSides(area, garden)
  perimiter = getPerimiter(area, garden)
  total_sum_part2 += len(area) * sides

print(total_sum_part1)
print(total_sum_part2)