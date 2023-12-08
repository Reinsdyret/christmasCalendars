from collections import deque
import sys


def seedrange(i, seedpairs):
    start, delta = (seedpairs[i], seedpairs[i+1])

    return range(start, start + delta)


with open('input.txt', 'r') as f:
    lines = f.readlines()
    seeds = deque()
    seedpairs = list(map(int, lines[0].split(':')[1].strip().split(' ')))


    #i1 = 0
    #i2 = 1
    #while i2 < len(seedpairs):
    #    start, length = (seedpairs[i1], seedpairs[i2])

    #    seeds.extend(range(start, start+length))

    #    i1 += 1
    #    i2 += 1
    #    print(i2)

    translation_dicts = []


    changed = [False] * len(seeds)
    new_dict = {}
    for i in range(3, len(lines)):
        if lines[i].strip() == '' or lines[i].strip()[-1] == ':' or len(lines[i].split(' ')) < 3:
            changed = [False] * len(seeds)
            translation_dicts.append(new_dict)
            new_dict = {}
            continue

        #print(lines[i].strip())
        destination_start, source_start, range_length = list(map(int,lines[i].strip().split(' ')))

        #print(f"Current input: {destination_start} {source_start} {range_length}")
        
        new_dict[(source_start, range_length)] = (destination_start, range_length)

    min_number = float('inf')


    for i in range(len(seedpairs) // 2):
        print(i)
        print(set(seedrange(i, seedpairs)))
        for seed in seedrange(i, seedpairs):
            print(seed)
            for dic in translation_dicts:
                for (start, delta) in dic:
                    if seed in range(start, start + delta):
                        diff = seed - start
                        destination = dic[(start, delta)][0]
                        seed = destination + diff

                        break
            if seed < min_number: min_number = seed

    print(min_number)





    #print(translation_dicts)

    #print(seeds)
   # print(min(seeds))




