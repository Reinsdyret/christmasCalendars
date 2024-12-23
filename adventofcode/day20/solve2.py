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


def euclidDistance(x1,y1,x2,y2):
  return abs(x2-x1) + abs(y2-y1)


def find_shortcuts(x,y,gx,gy,map, race_path, max_length):
  q = deque()
  q.append((x,y,[(x,y)],0))

  paths = []

  moves = [
    (1,0),
    (-1,0),
    (0,1),
    (0,-1)
  ]
  
  while len(q) > 0:
    print(x,y)
    x,y,path,depth = q.popleft()

    if depth > 20: continue
    

    for mx, my in moves:

      if (x+mx,y+my) in path: continue

      if inBounds(x + mx, y + my, map):
        nx, ny = x+mx, y+my
        if euclidDistance(x,y,gx,gy) >= euclidDistance(nx,ny,gx,gy):
          new_path = path + [(nx,ny)]
          
          q.append((nx, ny, new_path, depth + 1))
        
          if (nx, ny) in race_path:
            paths.append(new_path)
  return paths

def get_length_with_cut(cut, path):
  cutStartIndex = path.index(cut[0])
  cutEndIndex = path.index(cut[-1])

  return len(path[:cutStartIndex]) + len(cut) + len(path[cutEndIndex + 1:])


def drawPath(path, map, cut):
  pathSet = set(path[1:])

  for y in range(len(map)):
    row  = ""
    for x in range(len(map[y])):
      if (x,y) in cut[1:]:
        row += str(cut.index((x,y)))
      elif (x,y) in pathSet:
        row += "O"
      else: 
        row += map[y][x]
    print(''.join(row))



time_to_save = 64
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

path = shortest_path(start[0], start[1], goal[0],goal[1], code_path)[1]

shortcuts = find_shortcuts(start[0], start[1], goal[0], goal[1], code_path, path,time_to_save)
print(len(shortcuts))

count = 0
seen = set()
for shortcut in shortcuts:
  if len(shortcut) == 9:
    print("WOW")
  
  if len(path) - get_length_with_cut(shortcut, path) >= time_to_save and (shortcut[0], shortcut[-1]) not in seen:
    seen.add((shortcut[0], shortcut[-1]))
    count += 1
    drawPath(path, code_path, shortcut)
    print(len(shortcut))
    print()

print(count)
    