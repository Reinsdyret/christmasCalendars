from copy import deepcopy

# Create map
map = []
with open("input.txt", 'r') as f:
    for line in f.readlines():
        map.append(list(line.strip()))

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

def pretty_map(map):
  for row in map:
    print(''.join(row))

def take_step(map, posx, posy):
  
  if posx < 0 or posy < 0 or posy >= len(map) or posx >= len(map[posy]):
    # To not let python do -1 list funky business
    raise IndexError

  # Im sorry this is the best I can think of (brain fried)
  match map[posy][posx]:
    case '^':
      if posy <= 0: raise IndexError
      if map[posy-1][posx] != '#' and map[posy-1][posx] != 'O':
        map[posy][posx] = '.'
        map[posy-1][posx] = '^'
        return (map, posx, posy-1)
      else:
        map[posy][posx] = '>'
        return (map, posx, posy)
    
    case 'v':
      if map[posy+1][posx] != '#' and map[posy+1][posx] != 'O':
        map[posy][posx] = '.'
        map[posy+1][posx] = 'v'
        return (map, posx, posy+1)
      else:
        map[posy][posx] = '<'
        return (map, posx, posy)
      
    case '<':
      if posx <= 0: raise IndexError
      if map[posy][posx-1] != '#' and map[posy][posx-1] != 'O':
        map[posy][posx] = '.'
        map[posy][posx-1] = '<'
        return (map, posx-1, posy)
      else:
        map[posy][posx] = '^'
        return (map, posx, posy)
      
    case '>':
      if map[posy][posx+1] != '#' and map[posy][posx+1] != 'O':
        map[posy][posx] = '.'
        map[posy][posx+1] = '>'
        return (map, posx + 1, posy)
      else:
        map[posy][posx] = 'v'
        return (map, posx, posy)
    
    case _:
      print("Not matched")
      print(posx,posy, map[posy][posx])
      raise RuntimeError


def loops(map, startx, starty):
  currx = startx
  curry = starty
  
  seen_states = set()
  seen_states.add((currx,curry,map[curry][currx]))
  
  while True:
    try:
      map, currx, curry = take_step(map, currx, curry)
      
      if currx < 0 or curry < 0 or curry >= len(map) or currx >= len(map[curry]):
        #print("YAA")
        return False
      
      if (currx,curry,map[curry][currx]) in seen_states:
        # Seen the state before => loop
        return True
      
      seen_states.add((currx,curry,map[curry][currx]))
      
    except IndexError:
      # Throws index error when guard is out of the area
      return False

path = []
map_copy = deepcopy(map)
guardX_copy = guardX
guardY_copy = guardY

# Get the path of the guard, this is where we should place barriers
while True:
  try:
    map_copy, guardX_copy, guardY_copy = take_step(map_copy, guardX_copy, guardY_copy)
    path.append((guardX_copy, guardY_copy))
  except IndexError:
    break

print(len(path))

visited_pos = set()
count = 0

# Try barriers on all spots in path
for i, (x,y) in enumerate(path):
  if i % 1000 == 0: print(i, len(path))
  
  # skip over seen, and dont let me put barrier on start pos
  if (x,y) in visited_pos: continue
  if (x,y) == (guardX, guardY): continue
  
  visited_pos.add((x, y))
  
  # Copy the map, i dont know if its really needed
  test_map = deepcopy(map)
  
  # Add barrier
  test_map[y][x] = 'O'
  
  if loops(test_map, guardX, guardY):
    #print("\n" + "-"*10 + f"\nMade it with {x = }, {y = }")
    #test_map = deepcopy(map)
    #test_map[y][x] = 'O'
    #pretty_map(test_map)
    count += 1
    
print(count)