
def process_dict(current_dict, seeds):
    if len(current_dict) == 0:
        return seeds

    seed_copy = seeds
    for i in range(len(seeds)):
        if seeds[i] in current_dict:
            seed_copy[i] = current_dict[seeds[i]]

    return seed_copy

seeds = []

with open('input.txt', 'r') as f:
    lines = f.readlines()
    seeds = list(map(int, lines[0].split(':')[1].strip().split(' ')))

    current_dict = {}
    for i in range(3, len(lines)):
        if lines[i].strip() == '' or lines[i][-1].strip() == ':':
            seeds = process_dict(current_dict, seeds)
            current_dict = {}
            continue

        destination_start, source_start, range_length = list(map(int,lines[i].split(' ')))
        for j in range(range_length):
            current_dict[source_start + j] = destination_start + j

        if i % 100 == 0:
            print(i)

    print(seeds)




