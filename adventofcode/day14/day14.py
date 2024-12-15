
width = 101
height = 103

guards = []

with open('input.txt','r') as f:
    for line in f.readlines():
        p, v = line.split()
        x,y = map(int, p[2:].split(','))
        dx, dy = map(int, v[2:].split(','))

        guards.append(((x + (dx * 100)) % width, (y + (dy * 100)) % height))


splitY = height // 2
splitX = width // 2

q1 = 0
q2 = 0
q3 = 0
q4 = 0

print(guards)

for (x,y) in guards:
    
    if x < splitX:
        if y < splitY:
            print(x,y, "In q1")
            q1 += 1
        elif y > splitY:
            q3 += 1
    elif x > splitX:
        if y < splitY:
            q2 += 1
        elif y > splitY:
            q4 += 1

print(q1*q2*q3*q4)
