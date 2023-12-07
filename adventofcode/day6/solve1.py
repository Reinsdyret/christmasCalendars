

def findXs(time, record):
    xs = [x for x in range(0, time) if x * (time - x) > record]

    return len(xs)


# Part 1
print(findXs(61, 430) * findXs(67, 1036) * findXs(75, 1307) * findXs(71,1150))

# Part 2, a little slow but works :)
print(findXs(61677571, 430103613071150))

