
def moveLast(str):
  for i in range(len(str) - 1, -1, -1):
    if str[i] == '.': continue
    for j in range(0, i):
      if str[j] == '.':
        #print(str)
        str[j] = str[i]
        str[i] = '.'
        break
        #print(str)
  return str

def moveLastFile(str):
  # I am very proud to say I did this myself
  # I am not proud that 5 min later I cannot read this code.
  # But I guess it works xd
  i = len(str) - 1
  while i > -1:
    if str[i] == '.':
      i -= 1
      continue
    
    j = i
    whole_file = []
    
    while str[j] == str[i]:
      whole_file.append(str[j])
      j -= 1
      
    for p in range(j):
      if str[p] != '.': continue
      
      if len(set(str[p:p+len(whole_file)])) == 1:
        for a in range(p, p + len(whole_file)):
          str[a] = whole_file[a - p]
          str[i - (a - p)] = '.'
        break
        
    i -= (i - j)

  return str

def getSum(str):
  total = 0
  for i, c in enumerate(str):
    
    if c == '.': continue
    total += i * int(c)
  return total

compacted_string = []

with open("input.txt", 'r') as f:
  line = f.readline().strip()
  for i in range(0, len(line), 2):
    compacted_string.extend( [str((i // 2))] * int(line[i]))
    if i < len(line) - 1:
      compacted_string.extend( ['.'] * int(line[i+1]))

print(compacted_string)
print(f"Part 1: {getSum(moveLast(compacted_string[:]))}")
print(f"Part 2: {getSum(moveLastFile(compacted_string[:]))}")