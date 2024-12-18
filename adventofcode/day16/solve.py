import math
import heapq

def inboundsAndNotHash(x, y, map):
  return 1 <= y < len(map) - 1 and 1 <= x < len(map[y]) - 1 and map[y][x] != '#'


def dijsktra(currX, currY, direction, map):
  if map[currY][currX] == 'E': return 0

  q = [(0,currX,currY,direction)]

  dir_move_neigh = {
    'right': (1, 0, 'up', 'down'),
    'left': (-1, 0, 'up', 'down'),
    'up' : (0, -1, 'left', 'right'),
    'down' : (0, 1, 'left', 'right'),
  }

  costs = {}

  while q:
    cost,x,y,dir = heapq.heappop(q)

    if map[y][x] == 'E':
      return cost

    if (x,y,dir) in costs and cost > costs[(x,y,dir)]:
      continue

    mx, my, dir1, dir2 = dir_move_neigh[dir]

    if inboundsAndNotHash(x + mx, y + my, map):
      if (x + mx, y + my, dir) not in costs or cost + 1 < costs[(x+mx,y+my,dir)]:
        costs[(x+mx,y+my,dir)] = cost + 1
        heapq.heappush(q,(cost + 1,x+mx, y+my, dir))
    
    new_cost = 1000 + cost
    if (x,y,dir1) not in costs or costs[(x,y,dir1)] > new_cost:
      costs[(x,y,dir1)] = new_cost
      heapq.heappush(q,(cost + 1000,x,y,dir1))
    
    if (x,y,dir2) not in costs or costs[(x,y,dir2)] > new_cost:
      costs[(x,y,dir2)] = new_cost
      heapq.heappush(q,(cost + 1000, x,y,dir2))


  return -1


maze = []

with open("input.txt", 'r') as f:
  for line in f.readlines():
    maze.append(list(line.strip()))

startX = 1
startY = len(maze) - 2

print(dijsktra(startX, startY, 'right', maze))