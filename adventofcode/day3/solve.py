import re

def checktext(input_text):
    pattern = re.compile(r"^mul\([0-9]+,[0-9]+\)$")
    return pattern.match(input_text)

def checkdo(input_text):
    pattern = re.compile(r"^do\(\)$")
    return pattern.match(input_text)

def checkdont(input_text):
    pattern = re.compile(r"^don't\(\)$")
    return pattern.match(input_text)

# Part one
total_sum = 0

with open("input.txt", "r") as f:
    line = f.readline()
    for i in range(len(line)):
        print(i, len(line))
        for j in range(i, min(i+20, len(line))):
            substr = line[i:j+1]
            if checktext(substr):
                a, b = re.findall(r'[0-9]+', substr)
                total_sum += int(a) * int(b)

print(total_sum)

# Part two
total_sum = 0

do = True

with open("input.txt", "r") as f:
    line = f.readline()
    for i in range(len(line)):
        print(i, len(line))
        for j in range(i, min(i+20, len(line))):
            substr = line[i:j+1]

            do = not checkdont(substr) if do else checkdo(substr)

            if checktext(substr) and do:
                a, b = re.findall(r'[0-9]+', substr)
                total_sum += int(a) * int(b)

print(total_sum)
