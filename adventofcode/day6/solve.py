from copy import deepcopy

def take_step(map, guardX, guardY):
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


# ----------------
# ---- PART 2 ----
# ----------------

def isLooping(map2, guardX, guardY):
  looped_count = 0
  path1 = []
  visited = set()
  while True:
    try:
      if (guardX, guardY, map2[guardY][guardX]) in visited:
        return True
      visited.add((guardX, guardY, map2[guardY][guardX]))
      map2, guardX, guardY = take_step(map2, guardX, guardY)
      path1.append((guardX, guardY))

      if guardX < 0 or guardY < 0 or guardX >= len(map2[0]) or guardY >= len(map2):
        return False


    except IndexError:
      return False
    except TypeError:
      print(map2[guardY][guardX])
      return False
  return False

count = 0
vis = set()
for i,(testX, testY) in enumerate(set(path)):
  if (testX, testY) in vis: continue
  vis.add((testX, testY))
  print(i, len(path))
  
  testMap = deepcopy(map_copy)
  testMap[testY][testX] = '#'
  
  if isLooping(testMap, guardX_copy, guardY_copy):
    count += 1

print(count)

