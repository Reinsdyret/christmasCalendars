import functools

@functools.cache
def checkPossibleDesign(design):
  if design == "": return True
  posibilities = []
  for pattern in patterns:
    if pattern == design[:len(pattern)]:
      posibilities.append(checkPossibleDesign(design[len(pattern):]))
  
  return any(posibilities)

lines = []

count = 0

with open("input.txt", 'r') as f:
  lines = f.readlines()
  patterns = set(map(lambda a: a.strip(), lines[0].split(',')))

  for i,line in enumerate(lines[2:]):
    print(i)
    if checkPossibleDesign(line.strip()):
      count += 1

print(count)