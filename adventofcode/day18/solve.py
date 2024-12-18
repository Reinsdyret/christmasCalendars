from collections import deque
import math
def inBounds(x,y,map):
  return 0 <= y < len(map) and 0 <= x < len(map[y])


def drawPath(path, map):
  pathSet = set(path)

  for y in range(len(map)):
    row  = ""
    for x in range(len(map[y])):
      if (x,y) in pathSet:
        row += "O"
      else: 
        row += map[y][x]
    print(''.join(row))


def drawMap(map):
  for row in map:
    print(''.join(row))


def shortest_path(x,y,map):
  goal = (len(map) - 1, len(map) - 1)
  visited = set()
  q = deque()
  q.append([(x,y)])
  
  neighbours = [(1,0), (-1,0), (0,1), (0,-1)]

  while len(q) > 0:
    path = q.popleft()
    #drawPath(path, map)
    x,y = path[-1]

    if (x, y) in visited:
      #print("seen", x,y)
      continue

    visited.add((x, y))

    for mx,my in neighbours:
      nx, ny = x + mx, y + my
      if inBounds(nx, ny, map) and map[ny][nx] != '#':
        new_path = list(path)
        new_path.append((nx,ny))
        q.append(new_path)

        if (nx, ny) == goal:
          #print("Found: ",  len(new_path) - 1)
          return True
  return False


WIDTH = 70
HEIGHT = 70
N_BYTES = 1024

byte_positions = set()
with open("test_input.txt", 'r') as f:
  for i, line in enumerate(f.readlines()):
    if i >= N_BYTES: break
    a,b = map(int, line.strip().split(','))
    byte_positions.add((a,b))

memory = []
for y in range(HEIGHT + 1):
  row = []
  for x in range(WIDTH + 1):
    if (x,y) in byte_positions:
      row.append('#')
    else:
      row.append('.')
  memory.append(row)

# Part 1
shortest_path(0,0, memory)



# Part 2


def add_bytes(byte_positions):
  memory = []
  for y in range(HEIGHT + 1):
    row = []
    for x in range(WIDTH + 1):
      if (x,y) in byte_positions:
        row.append('#')
      else:
        row.append('.')
    memory.append(row)
  return memory



byte_positions = []
with open("input.txt", 'r') as f:
  for i, line in enumerate(f.readlines()):
    a,b = map(int, line.strip().split(','))
    byte_positions.append((a,b))

# Just brute force :)
for i in range(N_BYTES-1, len(byte_positions)):
  if i % 100: print(i)
  memory = add_bytes(byte_positions[:i+1])
  #drawMap(memory)

  if not shortest_path(0,0,memory):
    print(byte_positions[i])
    break