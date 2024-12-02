

totalSum = 0
lines = 0

with open("day7Input.txt", 'r') as f:
    lines = f.readlines()


def rekursivDritt(j, lines):
    global totalSum
    dirSum = 0
    for i in range(j,len(lines)):
        print(lines[i])
        if lines[i] == "$ cd ..":
            if dirSum <= 100000: totalSum += dirSum
            return
        elif lines[i] == "$ ls" or lines[i][0] == "d":  continue
        elif lines[i][0] == "$": rekursivDritt(i+1, lines)
        else: dirSum += int(lines[i].split(" ")[0])
        if lines[i] == "36092 rjjrg.pjq": return
    if dirSum <= 100000: totalSum += dirSum

rekursivDritt(0,lines)
print(totalSum)


