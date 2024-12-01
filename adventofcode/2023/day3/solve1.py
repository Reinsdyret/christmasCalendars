
engine_array = []

with open('input.txt', 'r') as f:
    for line in f:
        engine_array.append(line.strip())


def anySurroundingSymbols(y,x, engine_array):
    for i in range(max(y-1, 0), min(y+2, len(engine_array))):
        for j in range(max(0,x-1), min(len(engine_array[i]), x+2)):
            elem = engine_array[i][j]


            if not elem.isdigit() and elem != '.':
                return True


    return False

# Array for marking if a cel has been checked or not
checked = [ [False] * len(engine_array[0]) for x in range(len(engine_array))]

total_engine_sum = 0

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
        if anySurroundingSymbols(i,j, engine_array):
            symbolFound = True


        newX = j + 1
        nextNumber = engine_array[i][newX] if newX < len(engine_array[i]) else ""

        while nextNumber.isdigit():
            

            number += nextNumber
            
            checked[i][newX] = True

            
            if not symbolFound:
                if anySurroundingSymbols(i,newX, engine_array):
                    symbolFound = True
                

            

            newX += 1 
            if newX >= len(engine_array[i]):
                break
            nextNumber = engine_array[i][newX]

        if symbolFound:
            total_engine_sum += int(number)

print(total_engine_sum)





