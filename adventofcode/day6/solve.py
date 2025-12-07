columns = []
operators = []

with open('testInput.txt', 'r') as f:
  for line in f.readlines():
    row = line.strip().split(' ')
    while '' in row: row.remove('')

    for j, num in enumerate(row):
      while len(columns) <= j:
        columns.append([])
      columns[j].append(num)
  
  for i in range(len(columns)):
    operators.append(columns[i].pop())

part_one_result = 0

for i, operator in enumerate(operators):
  col_result = columns[i][0]
  for num in columns[i][1:]:
    col_result = eval(f"{col_result} {operator} {num}")
  part_one_result += col_result

print(f"Part one: {part_one_result}")

# Part 2

def extractVerticalNums(column: list[str], max_length: int) -> list[int]:
  nums = [] * max_length

  for i in range(max_length):
    num = ""
    for num_str in col:
      # print(num_str)
      if num_str[i] == ' ':
        continue
      else:
        num += num_str[i]
    print(num)
    print()
    nums.append(int(num))
  
  return nums

# First add padding to all numbers that are short
part_two_columns = list(map(lambda col: list(map(str, col)), columns))

for col in part_two_columns:
  max_length = max(map(len, col))
  for i in range(len(col)):
    while len(col[i]) < max_length:
      col[i] = f' {col[i]}'
      
# print(part_two_columns)
# print(part_two_columns[0])

part_two_result = 0

for i, operator in enumerate(operators):
  col = part_two_columns[i]
  max_length = max(map(len, col))
  nums = extractVerticalNums(col, max_length)
  total_sum = nums[0]
  for num in nums[1:]:
    total_sum = eval(f"{total_sum} {operator} {num}")
  part_two_result += total_sum

print(part_two_result)