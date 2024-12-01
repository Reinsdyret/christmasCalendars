
def getSumForLine(line):
    firstChar = None
    secondChar = None
    for c in line:
        try:
            int(c)
            if not firstChar:
                firstChar = c 
            secondChar = c 
        except:
            pass

    return int(firstChar + secondChar)

total_sum = 0


with open('input.txt', 'r') as f:
    for line in f:
        total_sum += getSumForLine(line)

print(total_sum)


