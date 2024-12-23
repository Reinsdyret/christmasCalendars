import functools

def countTrue(l):
  count = 0
  for i in l:
    if type(i) == list:
      count += countTrue(i)
    else:
      if i == True: count += 1
  
  return count

@functools.cache
def checkPossibleDesign(design):
  if design == "": return 1
  count = 0
  for pattern in patterns:
    if pattern == design[:len(pattern)]:
      count += checkPossibleDesign(design[len(pattern):])
  
  return count

lines = []

count = 0

with open("input.txt", 'r') as f:
  lines = f.readlines()
  patterns = set(map(lambda a: a.strip(), lines[0].split(',')))

  for i,line in enumerate(lines[2:]):
    if i % 10 == 0: print(i)
    count += checkPossibleDesign(line.strip())

print(count)