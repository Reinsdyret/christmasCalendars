import matplotlib.pyplot as plt

def drawGuards(guardsPos, i):
    fig = plt.figure()
    plt.title(f'{i}')
    plt.plot([x[0] for x in guardsPos], [x[1] for x in guardsPos], 'bo')
    plt.savefig(f'{iteration}.png')
    plt.close()
                


width = 101
height = 103


guardsPos = []
guardsVel = []

with open('input.txt','r') as f:
    for line in f.readlines():
        p, v = line.split()
        x,y = map(int, p[2:].split(','))
        dx, dy = map(int, v[2:].split(','))

        guardsPos.append((x, y))
        guardsVel.append((dx, dy))


iteration = 742
maxIteration = 20000
while iteration < maxIteration:
    drawGuards(guardsPos, iteration)

    for i, (x,y) in enumerate(list(guardsPos)):
        guardsPos[i] = ((x + guardsVel[i][0]) % width, (y + guardsVel[i][1]) % height)

    iteration += 1
    #print(iteration)

