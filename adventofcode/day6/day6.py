def startSignal(line):
    charSet = set()
    for i in range(0, len(line), 4):
        for j in range(i, i+4):
            charSet.add(line[j])
            print(len(charSet))
        if (len(charSet) == 4):
            return i
            break
        else:
            charSet = set()

def message(line, start):
    for i in range(start, len(line)):
        print(len(set(line[i:i+14])))
        if len(set(line[i:i+14])) == 14: return i+14

with open("day6Input.txt") as f:
    inputLine = f.readline()
    start = startSignal(inputLine)
    print(message(inputLine, start))


