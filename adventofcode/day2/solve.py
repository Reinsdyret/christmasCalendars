ranges = []

with open("input.txt", 'r') as f:
  line = f.readline().strip()
  all_ranges = line.split(',')
  for rang in all_ranges:
    start, end = rang.split('-')
    ranges.append(start)
    ranges.append(end)
    ranges.extend(range(int(start) + 1, int(end)))
      

result = 0

for num in ranges:
  numString = str(num)
  mid = (len(numString) + 1) // 2
  if numString[:mid] == numString[mid:]:
    result += int(num)
  
print(f"Part 1: {result}")

resultPartTwo = 0
for num in ranges:
  numString = str(num)
  mid = (len(numString) + 1) // 2
  invalid = False
  for length in range(1, mid + 1):
    part = numString[:length]
    times = len(numString) // length 
    if part * times == numString and times >= 2:
      resultPartTwo += int(num)
      break
    
print(f"Part 2: {resultPartTwo}")