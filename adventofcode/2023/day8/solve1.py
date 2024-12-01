node_map = {}

with open('input.txt', 'r') as f:
    lines = f.readlines()
    instructions = lines[0].strip()

    for line in lines[2:]:
        print(line)
        splitted = line.split('=')

        start = splitted[0].strip()
        left_right = splitted[1].strip('()')

        while '(' in left_right or ')' in left_right:
            left_right = left_right.replace('(', '')
            left_right = left_right.replace(')', '')

        left, right = map(str.strip, left_right.split(','))

        node_map[start] = (left,right)


node = "AAA"
steps = -1

for instruction in instructions*1000:
    steps += 1
    if node == "ZZZ":
        break

    if instruction == 'R':
        node = node_map[node][1]

    if instruction == 'L':
        node = node_map[node][0]

print(steps)

