commands = []

with open("input.txt", 'r') as f:
  for line in f.readlines():
    direction = line[0]
    amount = int(line[1:])
    commands.append((direction, amount))
    
    
dial = 50
counterZero = 0

for direction, amount in commands:
  if direction == "L":
    for i in range(amount):
      dial -= 1
      dial = (dial + 100) % 100
      if dial == 0:
        counterZero += 1
  else:
    for i in range(amount):
      dial += 1
      dial = (dial + 100) % 100
      if dial == 0:
        counterZero += 1
    
  dial = (dial + 100) % 100
  
  print(dial, counterZero)


print(counterZero)