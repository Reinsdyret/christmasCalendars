
def take_step(map, guardX, guardY):
    if map[guardY][guardX] == '<':
        if map[guardY][guardX - 1] == '#':
            map[guardY][guardX] = '^'
            return (map, guardX, guardY)
        else:
            map[guardY][guardX] = '.'
            map[guardY][guardX - 1] = '<'
            return (map, guardX - 1, guardY)
        
    if map[guardY][guardX] == '>':
        if map[guardY][guardX + 1] == '#':
            map[guardY][guardX] = 'v'
            return (map, guardX, guardY)
        else:
            map[guardY][guardX] = '.'
            map[guardY][guardX + 1] = '>'
            return (map, guardX + 1, guardY)
    
    if map[guardY][guardX] == 'v':
        if map[guardY + 1][guardX] == '#':
            map[guardY][guardX] = '<'
            return (map, guardX, guardY)
        else:
            map[guardY][guardX] = '.'
            map[guardY + 1][guardX] = 'v'
            return (map, guardX, guardY + 1)

    if map[guardY][guardX] == '^':
        if map[guardY - 1][guardX] == '#':
            map[guardY][guardX] = '>'
            return (map, guardX, guardY)
        else:
            map[guardY][guardX] = '.'
            map[guardY - 1][guardX] = '^'
            return (map, guardX, guardY - 1)
        
def pretty_map(map):
    for row in map:
        print(' '.join(row))


# Create map
map = []
with open("test_input.txt", 'r') as f:
    for line in f.readlines():
        map.append(list(line.strip()))


# Find guard
guardX = None
guardY = None
for i, row in enumerate(map):
    for j, v in enumerate(row):
        if v in ['v','<','>','^']:
            guardY = i
            guardX = j

count_guarded = 0

while True:
    try:
        map, newGuardX, newGuardY = take_step(map, guardX, guardY)
        if newGuardX != guardX or newGuardY != guardY:
            count_guarded += 1
            guardX = newGuardX
            guardY = newGuardY
    except IndexError:
        count_guarded += 1
        break

print(count_guarded)
