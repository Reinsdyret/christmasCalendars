from copy import deepcopy

def take_step(map, guardX, guardY):
  if guardX >= len(map[0]) or guardY >= len(map):
    raise IndexError

  if map[guardY][guardX] == '<':
      if map[guardY][guardX - 1] == '#':
          map[guardY][guardX] = '^'
          return (map, guardX, guardY)
      else:
          map[guardY][guardX] = 'X'
          map[guardY][guardX - 1] = '<'
          return (map, guardX - 1, guardY)
      
  if map[guardY][guardX] == '>':
      if map[guardY][guardX + 1] == '#':
          map[guardY][guardX] = 'v'
          return (map, guardX, guardY)
      else:
          map[guardY][guardX] = 'X'
          map[guardY][guardX + 1] = '>'
          return (map, guardX + 1, guardY)
  
  if map[guardY][guardX] == 'v':
      if map[guardY + 1][guardX] == '#':
          map[guardY][guardX] = '<'
          return (map, guardX, guardY)
      else:
          map[guardY][guardX] = 'X'
          map[guardY + 1][guardX] = 'v'
          return (map, guardX, guardY + 1)

  if map[guardY][guardX] == '^':
      if map[guardY - 1][guardX] == '#':
          map[guardY][guardX] = '>'
          return (map, guardX, guardY)
      else:
          map[guardY][guardX] = 'X'
          map[guardY - 1][guardX] = '^'
          return (map, guardX, guardY - 1)

  print(map[guardY, guardX])
        
def pretty_map(map):
  for row in map:
    print(''.join(row))


# -----------------
# ---- PART 1 -----
# -----------------

# Create map
map = []
with open("input.txt", 'r') as f:
    for line in f.readlines():
        map.append(list(line.strip()))

map_copy = deepcopy(map)
# Find guard
guardX = None
guardY = None
for i, row in enumerate(map):
  if guardX != None: break
  for j, v in enumerate(row):
    if v in ['v','<','>','^']:
      guardY = i
      guardX = j
      break

guardX_copy = guardX
guardY_copy = guardY

count_guarded = 0

path = []

while True:
  try:
    path.append((guardX,guardY))
    map, guardX, guardY = take_step(map, guardX, guardY)
    if guardX < 0 or guardY < 0:
      break
  except IndexError:
    break

for row in map:
  count_guarded += row.count('X')
print(count_guarded)

#pretty_map(map)

