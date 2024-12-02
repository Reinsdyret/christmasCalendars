
with open('day4Input.txt') as f:
    Lines = f.readlines()

count = 0

for line in Lines:
    if line == "\n": break
    a, b = line.split(",")
    x, y = a.split("-")
    x1, y1 = b.split("-")

    if   int(x1) <= int(x) <= int(y1): count += 1
    elif int(x1) <= int(y) <= int(y1): count += 1
    elif int(x)  <= int(x1)<= int(y): count += 1
    elif int(x)  <= int(y1)<= int(y): count += 1

print(count)

