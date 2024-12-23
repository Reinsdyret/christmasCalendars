from collections import deque


def inBounds(x,y,map):
  return 0 < y < len(map) - 1 and 0 < x < len(map[y]) - 1


def shortest_path(x,y,gx,gy,map):
  goal = (gx,gy)
  visited = set()
  q = deque()
  q.append([(x,y)])
  
  neighbours = [(1,0), (-1,0), (0,1), (0,-1)]

  while len(q) > 0:
    path = q.popleft()
    x,y = path[-1]

    if (x, y) in visited:
      continue

    visited.add((x, y))

    for mx,my in neighbours:
      nx, ny = x + mx, y + my
      if inBounds(nx, ny, map) and map[ny][nx] != '#':
        new_path = list(path)
        new_path.append((nx,ny))
        q.append(new_path)

        if (nx, ny) == goal:
          return True, path
  return False


def findShortcuts(map, path):
  shortcuts = set()
  for i, (x,y) in enumerate(path):
    for j, (x2,y2) in enumerate(path[i+1:]):
      if euclidDistance(x,y,x2,y2) <= 20:

        shortcuts.add((i,j+1+i))
      
  
  return shortcuts

def checkDir(p1, p2, map):
  x1, y1 = p1
  x2, y2 = p2

  if x1 < x2:
    # Moving right
    if map[y1][x1+1] != '#' or map[y2][x2-1] != '#': return False
  elif x2 < x1:
    # Moving left
    if map[y1][x1-1] != '#' or map[y2][x2+1] != '#': return False
  
  if y1 < y2:
    # Moving down
    if map[y1 + 1][x1] != '#' or map[y2-1][x2] != '#': return False
  
  elif y2 < y1:
    # Moving up
    if map[y1 - 1][x1] != '#' or map[y2+1][x2] != '#': return False
  
  return True


def drawPath(path, map, shortcutI, shortcutJ):
  pathSet = set(path)

  for y in range(len(map)):
    row  = ""
    for x in range(len(map[y])):
      if (x,y) in pathSet:
        if path[shortcutI] == (x,y):
          row += '1'
        elif path[shortcutJ] == (x,y):
          row += '2'
        else:
          row += "O"
      else: 
        row += map[y][x]
    print(''.join(row))

def checkCut(x,y,x2,y2,map):
  return checkDir((x,y), (x2,y2), map) and euclidDistance(x,y,x2,y2) <= 20


def euclidDistance(x1,y1,x2,y2):
  return abs(x2-x1) + abs(y2-y1)

code_path = []
start = (None, None)
goal = (None, None)
with open("test_input.txt", 'r') as f:
  for y, line in enumerate(f.readlines()):
    code_path.append(list(line.strip()))
    for x,c in enumerate(line.strip()):
      if c == 'S':
        start = (x,y)
      elif c == 'E':
        goal = (x,y)


path = shortest_path(start[0], start[1], goal[0], goal[1], code_path)[1]
path.append(goal)
shortcuts = findShortcuts(code_path, path)

print("FOUND")
count = 0
si, sj = 0, 0
seenCuts = set()
seenStarts = set()
seenEnds = set()

valid_cheats = []

for (i,j) in shortcuts:
  shortcut_path_length = len(path[:i+1]) + euclidDistance(path[i][0], path[i][1], path[j][0], path[j][0]) + len(path[j:])
  if len(path) - shortcut_path_length >= 76 and (i,j) not in seenCuts and i not in seenStarts and j not in seenEnds:
    print(f"Found shortcut with length {shortcut_path_length}")
    print(f"Path length is {len(path)}")
    seenCuts.add((i,j))
    seenStarts.add(i)
    seenEnds.add(j)
    
    valid_cheats.append((i,j))

    si, sj = i,j
    count += 1


for si, sj in valid_cheats:
  drawPath(path, code_path, si, sj)
  print()
print(count)

print(checkDir((1,3,),(4,7), code_path))