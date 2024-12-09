def checkBound(map,x,y):
  return 0 <= y < len(map) and 0 <= x < len(map[y])

def getAntinodes(p1, p2):
  x1,y1 = p1
  x2,y2 = p2
  
  antix1 = x1 + (x1 - x2)
  antiy1 = y1 + (y1 - y2)
  
  antix2 = x2 + (x2 - x1)
  antiy2 = y2 + (y2 - y1)
  
  return ((antix1, antiy1), (antix2, antiy2))

def getAllAntiNodesInBounds(map, p1, p2):
  x1,y1 = p1
  x2,y2 = p2
  
  p1Side = []
  p2Side = []
  
  i = 1
  while checkBound(map, x1 + (x1 - x2) * i, y1 + (y1 - y2) * i):
    p1Side.append( (x1 + (x1 - x2) * i, y1 + (y1 - y2) * i ))
    i += 1
  
  i = 1
  while checkBound(map, x2 + (x2 - x1) * i, y2 + (y2 - y1) * i):
    p2Side.append( (x2 + (x2 - x1) * i, y2 + (y2 - y1) * i ))
    i += 1
    
  return p1Side + p2Side

def pretty_map(map):
  for row in map:
    print(''.join(row))

points = {}
map = []

with open("input.txt", 'r') as f:
  for y, line in enumerate(f.readlines()):
    map.append(list(line.strip()))
    for x, c in enumerate(line.strip()):
      if c == '.': continue
      
      if c not in points:
        points[c] = [(x,y)]
      else:
        points[c].append((x,y))

count_antinodes = 0

for (char, points) in points.items():
  for i in range(0, len(points)):
    p1 = points[i]
    for j in range(i + 1, len(points)):
      p2 = points[j]
      
      for (x,y) in getAllAntiNodesInBounds(map, p1, p2):
        map[y][x] = '#'
        count_antinodes += 1

print(count_antinodes)

pretty_map(map)

new_count = 0

for row in map:
  for c in row:
    if c != '.':
      new_count += 1

print("NEW COUNT", new_count)
