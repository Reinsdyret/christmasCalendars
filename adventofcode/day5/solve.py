

with open("input.txt", 'r') as f:
  found_blank_line = False
  fresh_ranges = []
  fresh_start_end = []
  count = 0
  
  for line in f.readlines():
    if line.strip()  == '':
      found_blank_line = True
      continue
    if not found_blank_line:
      start, end = map(int, line.strip().split('-'))
      fresh_ranges.append(range(start, end + 1))
      fresh_start_end.append((start, end))
    else:
      id = int(line.strip())
      for range in fresh_ranges:
        if id in range:
          count += 1
          break
  
  # Part two
  count_part_two = 0
  fresh_start_end.sort(key=lambda x: (x[0], x[1]))
  
  i = 0
  while i < len(fresh_start_end):
    start, end = fresh_start_end[i]
    i += 1
    largest_end = end
    while i < len(fresh_ranges) and (start == fresh_start_end[i][0] or start < fresh_start_end[i][0] <= largest_end):
      if fresh_start_end[i][1] >= largest_end:
        largest_end = fresh_start_end[i][1]
      i += 1
    
    count_part_two += largest_end + 1 - start  
  
  print(f"Part 1: {count}")
  print(f"Part 2: {count_part_two}")