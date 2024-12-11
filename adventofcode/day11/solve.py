
mem = {}

def evolveStone(stone: str):
  if stone == '0':
    return '1', None
  
  if len(stone) % 2  == 0:
    mid = len(stone) // 2
    stoneA = stone[:mid]
    stoneB = stone[mid:]
  
    return stoneA, str(int(stoneB))
  
  return str((int(stone) * 2024)), None

def runEvolution(stone, n, mem):
  if n == 0: return 1
  
  if stone in mem:
    if n in mem[stone]:
      return mem[stone][n]
  else:
    mem[stone] = {}

  a, b = evolveStone(stone)
  
  if b != None:
    res = runEvolution(a, n-1, mem) + runEvolution(b, n-1, mem)
    mem[stone][n] = res
    return res
  
  res = runEvolution(a, n-1, mem)
  mem[stone][n] = res
  return res

with open("input.txt", 'r') as f:
  stones = f.readline().strip().split(' ')
  print(stones)
  print(sum(map(lambda s: runEvolution(s, 75, mem), stones)))

