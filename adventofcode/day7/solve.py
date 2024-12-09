
def concat(a,b):
  return int(str(a) + str(b))


def dfs(curr, rest, result, part2):
  if rest == []: return curr == result
  return dfs(curr + rest[0], rest[1:], result, part2) or dfs(curr * rest[0], rest[1:], result, part2) or (part2 and dfs(concat(curr, rest[0]), rest[1:], result, part2))


calibration_result1 = 0
calibration_result2 = 0

with open('input.txt', 'r') as f:
  for line in f.readlines():
    res, nums = line.split(':')
    res = int(res)
    nums = list(map(int, nums.strip().split(' ')))
    
    if dfs(nums[0], nums[1:], res, False):
      calibration_result1 += res
    if dfs(nums[0], nums[1:], res, True):
      calibration_result2 += res

print(calibration_result1)
print(calibration_result2)