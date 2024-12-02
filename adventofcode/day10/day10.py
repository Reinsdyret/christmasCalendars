

lines = []
with open("day10Input.txt", 'r') as f:
    lines = f.readlines()

cycle = 1
x = 1
cycles_to_sum = [20,60,100,140,180,220]
sum_strengths = 0


def doCycle(cycle, cycles_to_sum, sum_strengths, x, words):
    if cycle in cycles_to_sum: 
        sum_strengths += cycle * x
        print(f"{cycle=} {x=} {cycle * x=}")
    if words[0] == "noop":
        cycle += 1
        return (cycle,cycles_to_sum,sum_strengths,x)
    elif words[0] == "addx":
        cycle+=1
        return doCycle(cycle, cycles_to_sum, sum_strengths, x, words[1:])
    cycle += 1
    x += int(words[0])
    return (cycle,cycles_to_sum,sum_strengths,x)
    


for line in lines:
    words = line.split()
    cycle, cycles_to_sum, sum_strengths, x = doCycle(cycle, cycles_to_sum, sum_strengths, x, words)

print(sum_strengths)

