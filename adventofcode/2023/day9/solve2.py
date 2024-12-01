
def prevNumber(arr):
    temps = [arr]
    temp = []

    for i in range(len(arr) - 1):
        temp.append(arr[i + 1] - arr[i])

    temps.append(temp)

    while not all(x == 0 for x in temp):
        newtemp = []
        for i in range(len(temp) - 1):
            newtemp.append(temp[i + 1] - temp[i])

        temp = newtemp
        temps.append(temp)

    num = 0
    for t in temps[::-1]:
        num = t[0] - num

    return num


sum_histories = 0

with open('input.txt', 'r') as f:
    for line in f:
        numbers = line.strip().split(' ')
        sum_histories += prevNumber(list(map(int,numbers)))

print(sum_histories)
