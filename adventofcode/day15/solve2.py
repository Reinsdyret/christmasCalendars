from copy import deepcopy

def moveOne(x,y,dx,dy, map):
  if map[y][x] == '@':
    map[y + dy][x + dx] == '@'
    map[y][x] == '.'
    return True, (x + dx, y + dy), map
  
  elif map[y][x] == '[':
    map[y+dy][x+dx] = '['
    map[y+dy][x+dx+1] = ']'
    return True, (x + dx, y + dy), map
  
  elif map[y][x] == ']':
    map[y+dy][x+dx] = ']'
    map[y+dy][x+dx-1] = '['
    return True, (x + dx, y + dy), map
  
  return True, (x,y), map



def moveNew(x,y,dx,dy,map):
  print(map[y][x])
  if map[y][x] == '.': return True, (x,y), map
  map_copy = deepcopy(map)

  if map[y+dy][x+dx] == '#': return False, (x,y), map

  if map[y+dy][x+dx] in '[':
    if dx != 0:
      if moveNew(x+2,y+dy, dx,dy, map)[0]:
        return moveNew(x,y,dx,dy,map)
    if moveNew(x+dx,y+dy, dx,dy, map)[0]:
      return moveNew(x,y,dx,dy,map)
  
  else:
    #print(map[y][x], dx, dy)
    if map[y][x] == '[':
      if moveNew(x+1+dx,y+dy, dx,dy, map)[0]:
        return moveOne(x,y,dx, dy,map)
    
    elif map[y][x] == ']':
      if moveNew(x-1+dx, y+dy, dx,dy,map)[0]:
        return moveOne(x,y,-1+dx,dy,map)
      
    return moveOne(x,y,dx,dy,map)
  return False, (x,y), map_copy
        



def calculateGps(x,y):
  return 100 * y + x


with open("test_input_small2.txt", 'r') as f:
  lines = f.readlines()

# Read map (water)
warehouse = []
robot = (None, None)

for i in range(len(lines)):
  line = lines[i].strip()
  if line == '': break
  
  row = ""
  for j, c in enumerate(line):
    if c == '@':
      row += f"{c}."
      continue

    if c == 'O':
      row += '[]'
      continue
    
    row += 2*c
  warehouse.append(list(row))

for row in warehouse:
  print(''.join(row))

# Find robot
for y in range(len(warehouse)):
  for x in range(len(warehouse[y])):
    if warehouse[y][x] == '@':
      robot = (x,y)

# read and execute instructions
translate_instruction = {
  'v': (0,1),
  '^': (0,-1),
  '<': (-1,0),
  '>': (1,0)
}
for j in range(i, len(lines)):
  for instruction in lines[j].strip():
    print(instruction)
    dx, dy = translate_instruction[instruction]
    _, robot, warehouse = moveNew(robot[0], robot[1], dx,dy, warehouse)
    for row in warehouse:
      print(''.join(row))
    print()
  
for row in warehouse:
  print(''.join(row))

# Calculate total gps sum
total_gps = 0
for y in range(len(warehouse)):
  for x in range(len(warehouse[y])):
    if warehouse[y][x] == 'O':
      total_gps += calculateGps(x,y)

print(total_gps)
