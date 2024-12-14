

def extractNumber(line, splitting):
  _, info = line.split(':')
  a, b = info.split(',')
  x = int(a.split(splitting)[1])
  y = int(b.split(splitting)[1])
  
  return (x,y)


def findMaxCost(xa, ya, xb, yb, prizeX, prizeY):
  maxA = 300
  maxB = 300
  
  if prizeX % xa == 0 and prizeY % ya == 0:
    if prizeX / xa == prizeY / ya:
      maxA = int(prizeX / xa) * 3
    
  if prizeX % xb == 0 and prizeY % yb == 0:
    if prizeX / xb == prizeY / yb:
      maxB = int(prizeX / xb)
      
  return min(maxA, maxB)


def pressButtons(xa, ya, xb, yb, prizeX, prizeY, cache, cost, times, maxCost):
  #print(prizeX)
  if prizeX == 0 and prizeY == 0:
    #print("HIT")
    return cost
  
  if cost > maxCost: return -1
  
  if (xa, ya, xb, yb, prizeX, prizeY) in cache:
    return cache[(xa, ya, xb, yb, prizeX, prizeY)]
  
  if (prizeX < xa and prizeX < xb) or (prizeY < ya and prizeY < yb):
    return -1
  
  if times >= 100:
    return -1
  
  resultPressA = pressButtons(xa, ya, xb, yb, prizeX - xa, prizeY - ya, cache, cost + 3, times + 1, maxCost)
  if (xa, ya, xb, yb, prizeX - xa, prizeY - ya) in cache:
    cache[(xa, ya, xb, yb, prizeX - xa, prizeY - ya)] = min(cache[(xa, ya, xb, yb, prizeX - xa, prizeY - ya)], resultPressA)

  #print(resultPressA)
  resultPressB = pressButtons(xa, ya, xb, yb, prizeX - xb, prizeY - yb, cache, cost + 1, times + 1, maxCost)
  if (xa, ya, xb, yb, prizeX - xb, prizeY - yb) in cache:
    cache[(xa, ya, xb, yb, prizeX - xb, prizeY - yb)] = min(cache[(xa, ya, xb, yb, prizeX - xb, prizeY - yb)], resultPressB)
  
  
  if resultPressA == -1 and resultPressB == -1:
    return -1


  return min([c for c in [resultPressA, resultPressB] if c != -1])


games = []
game = ()

with open("test_input.txt", 'r') as f:
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
    
    maxCost = findMaxCost(xa,ya,xb,yb, prizeX, prizeY)
    print(maxCost)
        
    cost = pressButtons(xa, ya, xb, yb, prizeX, prizeY, {}, 0, 0, maxCost)
    print(cost)
    
    total_cost += cost
    
    i += 4
    
  print(total_cost)