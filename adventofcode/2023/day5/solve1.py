
with open('input.txt', 'r') as f:
    lines = f.readlines()
    seeds = list(map(int, lines[0].split(':')[1].strip().split(' ')))

    changed = [False] * len(seeds)
    for i in range(3, len(lines)):
        if lines[i].strip() == '' or lines[i].strip()[-1] == ':':
            changed = [False] * len(seeds)
            continue

        destination_start, source_start, range_length = list(map(int,lines[i].split(' ')))

        #print(f"Current input: {destination_start} {source_start} {range_length}")
        
        for j in range(len(seeds)):
            if seeds[j] in range(source_start, source_start + range_length) and changed[j] == False:
                delta = seeds[j] - source_start

                seeds[j] = destination_start + delta
                changed[j] = True
        #print(seeds)

    print(seeds)
    print(min(seeds))




