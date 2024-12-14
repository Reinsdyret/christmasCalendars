
def extractNumber(line, splitting):
  _, info = line.split(':')
  a, b = info.split(',')
  x = int(a.split(splitting)[1])
  y = int(b.split(splitting)[1])
  
  return (x,y)


def det(xa, ya, xb, yb):
  return xa * yb - ya * xb


def solve(xa, ya, xb, yb, prizeX, prizeY):
  d = det(xa, ya, xb, yb)
  
  if d == 0:
    pressesA = prizeX // xa
    pressesB = prizeX // xb
    return int(pressesA * 3 + pressesB)
  
  pressesA = (prizeX * yb - prizeY * xb) / d # I credit chatGPT that helped me do the linear algebra for this
  pressesB = (xa * prizeY - ya * prizeX) / d
  
  if not pressesA.is_integer() or not pressesB.is_integer() or pressesA < 0 or pressesB < 0:
    #print("NO SOLUTION")
    return 0
  
  return int(pressesA * 3 + pressesB)

with open("input.txt", 'r') as f:
  lines = f.readlines()
  i = 0
  
  total_cost = 0
  
  while i < len(lines):
    #print(lines[i:i+3])
    a = lines[i]
    b = lines[i + 1]
    c = lines[i + 2]
    
    xa, ya = extractNumber(a, '+')
    xb, yb = extractNumber(b, '+')
    
    prizeX, prizeY = extractNumber(c, '=')
        
    cost = solve(xa, ya, xb, yb, prizeX + 10000000000000, prizeY + 10000000000000)
    print(cost)
    
    total_cost += cost
    
    i += 4
    
  print(total_cost)