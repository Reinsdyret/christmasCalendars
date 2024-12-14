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
  sidesX = set()
  sidesY = set()

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
        if newX == x:
          sidesY.add((newX, newY, my))
        else:
          sidesX.add((newX, newY, mx))
  
  allSides = list(sidesX.union(sidesY))
  countSides = 0
  besideEachOther = [(0,1,0),(1,0,0),(-1,0,0),(0,-1,0)]
  
  for i in range(len(allSides)):
    found = False
    for j in range(i + 1, len(allSides)):
      a = allSides[i]
      b = allSides[j]
      c = (a[0] - b[0], a[1] - b[1], a[2] - b[2])
      if c in besideEachOther:
        found = True
    
    if not found: countSides += 1
  
  print(countSides)
  return countSides


garden = []

with open("simple_test_input2.txt", 'r') as f:
  for line in f.readlines():
    garden.append(list(line.strip()))

total_sum_part1 = 0
total_sum_part2 = 0

for area in findAreas(garden):
  #total_sum_part1 += len(area) * getPerimiter(area, garden)
  total_sum_part2 += len(area) * getSides(area, garden)

print(total_sum_part1)
print(total_sum_part2)