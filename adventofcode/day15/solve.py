
def move(x,y,mx,my, map):
  if map[y+my][x+mx] == '#': return False, (x,y), map

  if map[y+my][x+mx] == '.':
    map[y+my][x+mx] = map[y][x]
    map[y][x] = '.'

  elif move(x+mx, y+my, mx, my, map)[0]:
    map[y+my][x+mx] = map[y][x]
    map[y][x] = '.'

  else:
    return False, (x,y), map
  
  return True, (x+mx, y+my), map


def calculateGps(x,y):
  return 100 * y + x


with open("input.txt", 'r') as f:
  lines = f.readlines()

# Read map (water)
warehouse = []
robot = (None, None)

for i in range(len(lines)):
  if lines[i].strip() == '': break
  warehouse.append(list(lines[i].strip()))
  if '@' in lines[i]: robot = (i, lines[i].index('@'))

# read and execute instructions
translate_instruction = {
  'v': (0,1),
  '^': (0,-1),
  '<': (-1,0),
  '>': (1,0)
}
for j in range(i, len(lines)):
  for instruction in lines[j].strip():
    dx, dy = translate_instruction[instruction]
    _, (x,y), warehouse = move(robot[0], robot[1], dx, dy, warehouse)

    robot = (x,y)

# Calculate total gps sum
total_gps = 0
for y in range(len(warehouse)):
  for x in range(len(warehouse[y])):
    if warehouse[y][x] == 'O':
      total_gps += calculateGps(x,y)

print(total_gps)
