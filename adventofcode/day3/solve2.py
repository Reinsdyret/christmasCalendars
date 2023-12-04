engine_array = []

with open('input.txt', 'r') as f:
    for line in f:
        engine_array.append(line.strip())


def anySurroundingStar(y,x,engine_array):
    for i in range(max(y-1, 0), min(y+2, len(engine_array))):
        for j in range(max(0,x-1), min(len(engine_array[i]), x+2)):
            elem = engine_array[i][j]


            if elem == '*':
                return True, (i,j)

    return False, (False, False)

# Array for marking if a cel has been checked or not
checked = [ [False] * len(engine_array[0]) for x in range(len(engine_array))]


gear_dict = dict()

for i in range(len(engine_array)):
    for j in range(len(engine_array[i])):

        if checked[i][j]: continue 

        number = engine_array[i][j]
        if not number.isdigit(): continue

        # Flag to signal that some digit in the number has a symbol next to it
        symbolFound = False

        # Signal that digit is checked 
        checked[i][j] = True
        # Test if this digit is next to symbol
        starFound, (symbolY, symbolX) = anySurroundingStar(i,j, engine_array)
        


        newX = j + 1
        nextNumber = engine_array[i][newX] if newX < len(engine_array[i]) else ""

        while nextNumber.isdigit():
            

            number += nextNumber
            
            checked[i][newX] = True

            
            if not starFound:
                starFound, (symbolY, symbolX) = anySurroundingStar(i,newX,engine_array)

            newX += 1 
            if newX >= len(engine_array[i]):
                break
            nextNumber = engine_array[i][newX]

        if starFound:
            if symbolY in gear_dict:
                if symbolX in gear_dict[symbolY]:
                    gear_dict[symbolY][symbolX].append(int(number))

                else:
                    gear_dict[symbolY][symbolX] = [int(number)]
            else:
                gear_dict[symbolY] = {symbolX : [int(number)]}



total_sum = 0

for y in gear_dict:
    for x in gear_dict[y]:
        theGears = gear_dict[y][x]
        if len(theGears) == 2:
            total_sum += theGears[0] * theGears[1]
print(gear_dict[1])
print(engine_array[1][4])
print(anySurroundingStar(2,3,engine_array))
print(total_sum)



