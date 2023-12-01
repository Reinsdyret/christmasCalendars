
wordToNumberDict = {
        "one": '1',
        "two": '2',
        "three": '3',
        "four": '4',
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9',
        "zero": '0'
        }

def findWordValue(line):
    for i in range(len(line)):
        for j in range(i, len(line) + 1):
            if line[i:j] in wordToNumberDict:
                return i, wordToNumberDict[line[i:j]]
    return 9999, "-1"

def findLastWordValue(line):
    for i in range(len(line) - 1, 0, -1):
        for j in range(i, len(line) + 1):
            if line[i:j] in wordToNumberDict:
                return i, wordToNumberDict[line[i:j]]
    return 0, "-1"

def findIntValue(line):
    for i in range(len(line)):
        try:
            int(line[i])
            return i, line[i]
        except:
            continue

    return 9999999, 9999999

def findLastIntValue(line):
    for i in range(len(line)-1, -1, -1):
        try:
            int(line[i])
            return i, line[i]
        except:
            continue

    return 0, 0


total_sum = 0
with open('input.txt', 'r') as f:
    for line in f:
        if findWordValue(line) == None:
            indexInt, value = findIntValue(line)
            index, secondValue = findLastIntValue(line)
            total_sum += int(value + secondValue)

        fwIndex, fwValue = findWordValue(line)
        lwIndex, lwValue = findLastWordValue(line)

        #print(fwIndex, fwValue)
        #print(lwIndex, lwValue)

        fiIndex, fiValue = findIntValue(line)
        liIndex, liValue = findLastIntValue(line)

        #print(fiIndex, fiValue)
        #print(liIndex, liValue)

        if fwIndex < fiIndex:
            officialFirstValue = fwValue
        else:
            officialFirstValue = fiValue

        if lwIndex > liIndex:
            officialSecondValue = lwValue
        else:
            officialSecondValue = liValue

        total_sum += int(officialFirstValue + officialSecondValue)

print(total_sum)

