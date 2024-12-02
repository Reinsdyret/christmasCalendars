
lines = ""

with open("day8TestInput.txt",'r') as f:
    lines = f.readlines()

visibleTrees = (len(lines[0])*2 - 2) + (len(lines)*2 - 4)
print(visibleTrees)
visibleIndexesGlobal = []

for i in range(1,len(lines)-1):
    line = lines[i]
    line = line.replace('\n','')
    visibleIndexes = []
    highestTree = int(line[0])
    # Checking row left to right
    for j in range(1,len(line)-1):
        print(line[j])
        height = int(line[j])
        if height > highestTree:
            highestTree = height
            visibleIndexes.append(j)
            visibleIndexesGlobal.append((i,j))

    # Checking row right to left
    highestTree = int(line[-1])
    for j in range(len(line)-2,0,-1):
        print(line[j])
        height = int(line[j])
        if height > highestTree:
            highestTree = height
            if j not in visibleIndexes:
                visibleIndexes.append(j)
                visibleIndexes.append((i,j))
    visibleTrees += len(visibleIndexes)

print(visibleTrees)
print(visibleIndexesGlobal)
