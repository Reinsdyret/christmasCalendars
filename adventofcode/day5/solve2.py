import copy
import functools


order = {i: set() for i in range(1000)}

incorrect_lines = []

# Part 1
sum_total_correct = 0

@functools.cache
def checkValidLine(nums):
    seen = set()
    nums = list(map(int, nums.split(' ')))

    for num in nums:
        if len(order[num].intersection(seen)) >= 1:
            return False
        seen.add(num)

    return True

with open("input.txt", 'r') as f:
    lines = f.readlines()

    for i in range(len(lines)):
        if lines[i].strip() == "":
            break
            
        a, b = map(int, lines[i].strip().split('|'))
        order[a].add(b)
    
    i += 1

    for j in range(i, len(lines)):
        nums = list(map(int, lines[j].strip().split(',')))

        seen = set()
        
        if not checkValidLine(' '.join(map(str, nums))):
            incorrect_lines.append(nums)
            continue

from collections import deque

def top_sort(nodes, order):
    final_list = []
    in_degree = {u: 0 for u in nodes}

    queue = deque()

    for u in nodes:
        for v in nodes:
            if u in order[v]: in_degree[u] += 1
        if in_degree[u] == 0:
            queue.append(u)
        
    
    while len(queue) > 0:
        u = queue.popleft()
        final_list.append(u)
        in_degree[u] = -1

        for v in order[u]:
            if v in in_degree:
                in_degree[v] -= 1
                if in_degree[v] == 0: queue.append(v)

    return final_list

sum_total_incorrect = 0
for line in incorrect_lines:
    corrected = top_sort(line, order)
    sum_total_incorrect += corrected[len(corrected) // 2]

print(sum_total_incorrect)