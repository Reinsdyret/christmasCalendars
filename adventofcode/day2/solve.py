count = 0

levels = []

with open("input.txt", "r") as f:
    for line in f.readlines():
        levels.append(list(map(int, line.strip().split(' '))))

strictlyIncreasing = lambda arr: all([arr[i] < arr[i+1] for i in range(len(arr) - 1)])
strictlyDecreasing = lambda arr: all([arr[i] > arr[i+1] for i in range(len(arr) - 1)])

diffCheck = lambda arr: all([1 <= abs(arr[i] - arr[i+1]) <= 3 for i in range(len(arr) - 1)])

# Part one
for level in levels:
    if (strictlyIncreasing(level) or strictlyDecreasing(level)) and diffCheck(level):
        count += 1

print(f"Part one result is: {count}")


# Part two
count = 0

for level in levels:
    level_tests = []
    for i in range(len(level)):
        level_copy = level[:]
        level_copy.pop(i)

        level_tests.append((strictlyIncreasing(level_copy) or strictlyDecreasing(level_copy)) and diffCheck(level_copy))
    
    if any(level_tests): count += 1

print(f"Part two result is {count}")
