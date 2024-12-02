


lines = []
with open("day10Input.txt", 'r') as f:
    lines = f.readlines()

rows = []

for i in range(6):
    row = []
    for i in range(40):
        row.append(".")

    rows.append(row)

cycle = 0
x = 1


def shouldDrawPixel(cycle, x):
    if x in range((cycle % 40) - 1,(cycle % 40)+2): return True
    return False


def doCycle(cycle, x, words, rows):
    if words[0] == "noop":
        if shouldDrawPixel(cycle, x):
            row = cycle // 40
            index = cycle % 40
            rows[row][index] = "#"
        cycle += 1
        return (cycle,x,rows)
    elif words[0] == "addx":
        if shouldDrawPixel(cycle, x):
            row = cycle // 40
            index = cycle % 40
            rows[row][index] = "#"
        cycle+=1
        return doCycle(cycle, x, words[1:], rows)
    if shouldDrawPixel(cycle, x):
            row = cycle // 40
            index = cycle % 40
            rows[row][index] = "#"
    cycle += 1
    x += int(words[0])
    return (cycle,x, rows)

for line in lines:
    words = line.split()
    cycle, x, rows = doCycle(cycle,x,words, rows)

for row in rows:
    print("".join(row))
 
